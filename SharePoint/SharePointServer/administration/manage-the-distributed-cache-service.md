---
title: "Manage the Distributed Cache service in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5d120a41-37e5-4711-b31e-33e82b034af0
description: "Learn how to configure and manage the Distributed Cache service in SharePoint Server."
---

# Manage the Distributed Cache service in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
To perform management and operational tasks on the Distributed Cache service in SharePoint Server, an administrator must perform specific, ordered procedures. This article describes how to conduct several management and operational tasks on the Distributed Cache service. 
  
> [!IMPORTANT]
> The Distributed Cache service can end up in a nonfunctioning or unrecoverable state if you do not follow the procedures that are listed in this article. In extreme scenarios, you might have to rebuild the server farm. The Distributed Cache depends on Windows Server AppFabric as a prerequisite. Do not administer the **AppFabric Caching Service** from the **Services** window in **Administrative Tools** in **Control Panel**. Do not use the applications in the folder named **AppFabric for Windows Server** on the **Start** menu. Adding security for AppFabric with SharePoint distributed cache is not supported.

 
> [!IMPORTANT]
> Do not use service account names that contain the symbol $. 
  
    
## Start and stop the Distributed Cache service
<a name="startstopcache"> </a>

An administrator that performs maintenance and operational tasks might need to start and stop the Distributed Cache service. Some of these tasks include the following:
  
- Changing the default configuration of the server farm at installation time. The Distributed Cache service is started on all SharePoint servers at installation time. An administrator might want to stop the Distributed Cache service on some servers in the farm.
    
- Updating the server and there is only one Distributed Cache server in the SharePoint Server farm.
    
Stopping the cache results in partial data loss. The Feed Cache depends on the Distributed Cache service. Tags and document activities are saved only to the Feed Cache. Tags and document activities are not persisted to content databases. When the Distributed Cache service is stopped, tags and document activities are lost. When the Distributed Cache service is started, repopulation occurs when the feed cache repopulation timer job runs. One way to maintain the tags and document activities is to use the method described in [Perform a graceful shutdown of the Distributed Cache service by using a PowerShell script](manage-the-distributed-cache-service.md#graceful) later in this article. When the graceful shutdown of the Distributed Cache service method is used, all cache data is moved from one server to another server before the Distributed Cache service is stopped. 
  
> [!NOTE]
> If your cache hosts are part of a cache cluster, do not start or stop the Distributed Cache service as described here. Instead, see [Add or remove a server in a Distributed Cache cluster](manage-the-distributed-cache-service.md#addremove) later in this article. 
  
### To start and stop the Distributed Cache service by using Central Administration

1. In Central Administration, click **Application Management.**
    
2. In **Service Applications**, click **Manage Services on Server**.
    
3. On the **Services on Server** page, locate the **Distributed Cache** service. 
    
4. If the Distributed Cache service is started and you want to stop the service, under **Action**, click **Stop**. If the Distributed Cache service is stopped and you want to start the service, under **Action**, click **Start**.
    
### To start the Distributed Cache service by using SharePoint Management Shell

At the SharePoint Management Shell command prompt, run the following command:
  
```
$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"
$serviceInstance = Get-SPServiceInstance | ? {($_.service.tostring()) -eq $instanceName -and ($_.server.name) -eq $env:computername}
$serviceInstance.Provision()

```

### To stop the Distributed Cache service by using SharePoint Management Shell

At the SharePoint Management Shell command prompt, run the following command:
  
```
$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"
$serviceInstance = Get-SPServiceInstance | ? {($_.service.tostring()) -eq $instanceName -and ($_.server.name) -eq $env:computername}
$serviceInstance.Unprovision()

```

## Change the memory allocation of the Distributed Cache service
<a name="memory"> </a>

When SharePoint Server is installed, it assigns the Distributed Cache service 10 percent of the total physical memory on the server. The Distributed Cache service uses half of that memory allocation for data storage (also known as cache size), and the other half of that memory allocation is used for memory management overhead. When the cached data grows, the Distributed Cache service uses the entire 10 percent of the allocated memory.
  
You should increase the memory allocation of the Distributed Cache service in these scenarios: 
  
- When you add physical memory to the server. The Distributed Cache service does not automatically recalculate the 10% memory allocation, so when you increase the total physical memory on the server, you have to manually increase the Distributed Cache service's memory allocation. 
    
- When your server farm has a dedicated Distributed Cache server. Use the following method to calculate how much memory can be assigned to the Distributed Cache service:
    
1. Determine the total physical memory on the server. For this example, we will use 16 GB as the total physical memory available on the server.
    
2. Reserve 2 GB of memory for other processes and services that are running on the cache host. For example, 16 GB - 2 GB = 14 GB. This remaining memory is allocated to the Distributed Cache service.
    
3. Take half of the remaining memory, and convert it to MB. For example, 14 GB/2 = 7 GB or 7168 MB. This is the cache size of the Distributed Cache service.
    
4. Use the following procedure to update the memory allocation accordingly.
    
### Change the memory allocation of the Distributed Cache

Use this procedure to reconfigure the memory allocation of the cache size of the Distributed Cache service.
  
1. (Optional) To check the existing memory allocation for the Distributed Cache service on a server, run the following command at the SharePoint Management Shell command prompt:
    
  ```
  Use-CacheCluster
  Get-AFCacheHostConfiguration -ComputerName $Env:ComputerName -CachePort "22233"
  
  ```
Where:
    
  -  _ComputerName_ is the computer name of the server that you are running the SharePoint Management Shell cmdlet on. 
    
2. Stop the Distributed Cache service on all cache hosts. To stop the Distributed Cache service, go to **Services on Server** in Central Administration, and **Stop** the Distributed Cache service on all cache hosts in the farm. 
    
3. To reconfigure the cache size of the Distributed Cache service, run the following command one time only on any cache host at the SharePoint Management Shell command prompt:
    
  ```
  Update-SPDistributedCacheSize -CacheSizeInMB CacheSize
  ```
Where:
    
  -  _CacheSize_ is the cache size's memory allocation assignment in MB. In the previous example, the cache size was calculated at 7168 MB for a server with 16 GB of total memory. 
    
4. Restart the Distributed Cache service on all cache hosts. To restart the Distributed Cache service, go to **Services on Server** in Central Administration, and **Start** the Distributed Cache service on all cache hosts in the farm. 
    
## Add or remove a server in a Distributed Cache cluster
<a name="addremove"> </a>

An administrator can add or remove a server to a cache cluster, or might want to remove a server from the cache cluster, perform some operational or maintenance tasks on the server, and then rejoin or add the server to the cache cluster. When removing the server, the Distributed Cache service is stopped, then unregistered from the server. Unregistering the Distributed Cache service means that an administrator will not see the Distributed Cache service listed on the **Services on Server** page in Central Administration. Similarly, when a server is added, the Distributed Cache service is registered and then is started on the server. Registering the Distributed Cache service means that an administrator will see the Distributed Cache service listed on the **Services on Server** page in Central Administration. 
  
Use the following procedures to add and remove a server from a cache cluster. These SharePoint Management Shell cmdlets are run on the server being added or removed.
  
> [!NOTE]
> Before performing the following procedures, ensure the firewall allows Inbound ICMP (ICMPv4) traffic through it. For more information, see [Firewall configuration considerations](plan-for-feeds-and-the-distributed-cache-service.md#firewall). 
  
### Add a server to the cache cluster and starting the Distributed Cache service by using SharePoint Management Shell

At the SharePoint Management Shell command prompt, run the following command:
  
```
Add-SPDistributedCacheServiceInstance

```

### Remove a server from the cache cluster by using SharePoint Management Shell

At the SharePoint Management Shell command prompt, run the following command:
  
```
Remove-SPDistributedCacheServiceInstance

```

> [!IMPORTANT]
> This procedure will stop the cache service and nonpersisted cached data will be lost. If you want to keep the cached data, use the graceful shutdown procedure that is described in the next section. 
  
## Perform a graceful shutdown of the Distributed Cache service by using a PowerShell script
<a name="graceful"> </a>

In a SharePoint Server farm, a cache cluster exists when one or more cache hosts run the Distributed Cache service. In a SharePoint Server farm, one cache exists, and the cache spans the cache cluster. An administrator may need to move the cached contents to another cache host when applying updates to the server. To prevent data loss associated with moving the cached contents you need to perform a graceful shutdown of the server using the PowerShell script in the following procedure. The graceful shutdown procedure transfers all cached data from the cache host on which the graceful shutdown procedure is being run on to another cache host in the farm. The transfer process takes 15 minutes or more to run depending on how many items exist in the cache. 
  
### To perform a graceful shutdown of the Distributed Cache by using a PowerShell script

Use the following PowerShell script to perform a graceful shutdown of the Distributed Cache server in order to move the cached contents to another cache host. Ensure that you specify the correct node to shutdown and change the script as needed to name the correct parameters for your organization.
  
> [!NOTE]
> There is no need to remove the cache host from a cache cluster if you use the PowerShell script in the following procedure to perform a graceful shutdown. 
  
1. Verify that you meet the following minimum requirements:
    
  - See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
2. Copy the following variable declarations, and paste them into a text editor such as Notepad. Set parameter values specific to your organization. Save the file, and name it GracefulShutdown.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1. 
  
  ```
  ## Settings you may want to change for your scenario ##
  $startTime = Get-Date
  $currentTime = $startTime
  $elapsedTime = $currentTime - $startTime
  $timeOut = 900
  Use-CacheCluster
  try
  {
      Write-Host "Shutting down distributed cache host."
   $hostInfo = Stop-CacheHost -Graceful -CachePort 22233 -ComputerName sp2016App.contoso.com
   while($elapsedTime.TotalSeconds -le $timeOut-and $hostInfo.Status -ne 'Down')
   {
       Write-Host "Host Status : [$($hostInfo.Status)]"
       Start-Sleep(5)
       $currentTime = Get-Date
       $elapsedTime = $currentTime - $startTime
       $hostInfo = Get-CacheHost -HostName SP2016app.contoso.com -CachePort 22233
   }
   Write-Host "Stopping distributed cache host was successful. Updating Service status in SharePoint."
   Stop-SPDistributedCacheServiceInstance
   Write-Host "To start service, please use Central Administration site."
  }
  catch [System.Exception]
  {
   Write-Host "Unable to stop cache host within 15 minutes." 
  }
  ```

Where  _sp2016App.contoso.com_ is the computer domain name of Distributed Cache server you use. 
    
3. Open the SharePoint Management Shell
    
4. Change to the directory to which you saved the file.
    
5. At the PowerShell command prompt, type the following command:
    
  ```
  ./GracefulShutdown.ps1
  ```

For additional information about PowerShell scripts and .ps1 files, see [Running Windows PowerShell Scripts](/previous-versions/windows/it-pro/windows-powershell-1.0/ee176949(v=technet.10)).
    
## Change the service account
<a name="changesvcacct"> </a>

When the server farm is first configured, the server farm account is set as the service account of the AppFabric Caching service. The Distributed Cache service depends on the AppFabric Caching service. To change the service account of the AppFabric Caching service to a managed account:
  
1. Create a managed account. 
    
2. Set the Managed account as the service account on the AppFabric Caching service. At the SharePoint Management Shell command prompt, run the following command:
    
  ```
  $farm = Get-SPFarm
  $cacheService = $farm.Services | where {$_.Name -eq "AppFabricCachingService"}
  $accnt = Get-SPManagedAccount -Identity domain_name\user_name
  $cacheService.ProcessIdentity.CurrentIdentityType = "SpecificUser"
  $cacheService.ProcessIdentity.ManagedAccount = $accnt
  $cacheService.ProcessIdentity.Update() 
  $cacheService.ProcessIdentity.Deploy()
  ```

Where  _Domain_name\user_name_ is the domain name and user name of the SharePoint managed account. 
    
## Fine-tune the Distributed Cache service by using a PowerShell script
<a name="finetune"> </a>

**Monitoring**

You can monitor performance counters on the Distributed Cache servers to get a better understanding of cache performance issues.
Some of the [counters](https://docs.microsoft.com/previous-versions/appfabric/ff637725(v=azure.10)) that are typically useful to troubleshoot issues include:

1. %cpu used up by cache service

2. %time spent in GC by cache service

3. Total cache misses/sec - A high value here can indicate your application performance might suffer because it is not able to fetch data from cache. Possible causes for this include eviction and/or expiry
of items from cache.

4. Total object count - Gives an idea of how many items are in the cache. A big drop in object count could mean eviction or expiry is taking place.

5. Total client reqs/sec - This counter is useful in giving an idea of how much load is being generated on the cache servers from the application. A low value here usually means some sort of a bottleneck
outside of the cache server (perhaps in the application or network) and hence very little load is being placed on cache servers.

6. Total Evicted Objects - If cache servers are constantly evicting items to make room for newer objects in cache, it is usually a good indication that you will need more memory on the cache servers to hold
the dataset for your application.

7. Total failure exceptions/sec and Total Retry exceptions/sec

The Distributed Cache service setting for **MaxConnectionsToServer** is often tuned based on the number of CPUs that are used in the host computer. If, for instance you use multiple cores and then set the **MaxConnectionsToServer** setting to the same number of CPUs then the computer often uses too much memory and freezes. Similar issues happen when tuning the **DistributedLogonTokenCache** and **DistributedViewStateCache** settings. The default setting is 20ms but often exceptions are found when the token caching doesn't happen in the 20ms setting. Use the following PowerShell scripts to change the settings for max connections and timeouts in SharePoint Server 2016 and SharePoint Server 2013. 
  
 **To fine-tune the Distributed Cache service by using a PowerShell script**
  
1. Verify that you meet the following minimum requirements:
    
  - See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
  - You need to read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
2. Copy the following variable declarations, and paste them into a text editor such as Notepad. Set parameter values specific to your organization. Save the file, and name it MaxConnections.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1. 
  
  **SharePoint Server 2016 PowerShell script**
  ```
  Add-PSSnapin Microsoft.Sharepoint.Powershell -ea 0

  #DistributedLogonTokenCache
  $DLTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedLogonTokenCache
  $DLTC.MaxConnectionsToServer = 1
  $DLTC.requestTimeout = "3000"
  $DLTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedLogonTokenCache $DLTC

  #DistributedViewStateCache
  $DVSC = Get-SPDistributedCacheClientSetting -ContainerType DistributedViewStateCache
  $DVSC.MaxConnectionsToServer = 1
  $DVSC.requestTimeout = "3000"
  $DVSC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedViewStateCache $DVSC

  #DistributedAccessCache
  $DAC = Get-SPDistributedCacheClientSetting -ContainerType DistributedAccessCache
  $DAC.MaxConnectionsToServer = 1
  $DAC.requestTimeout = "3000"
  $DAC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedAccessCache $DAC

  #DistributedActivityFeedCache
  $DAF = Get-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedCache
  $DAF.MaxConnectionsToServer = 1
  $DAF.requestTimeout = "3000"
  $DAF.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedCache $DAF

  #DistributedActivityFeedLMTCache
  $DAFC = Get-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedLMTCache
  $DAFC.MaxConnectionsToServer = 1
  $DAFC.requestTimeout = "3000"
  $DAFC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedLMTCache $DAFC

  #DistributedBouncerCache
  $DBC = Get-SPDistributedCacheClientSetting -ContainerType DistributedBouncerCache
  $DBC.MaxConnectionsToServer = 1
  $DBC.requestTimeout = "3000"
  $DBC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedBouncerCache $DBC

  #DistributedDefaultCache
  $DDC = Get-SPDistributedCacheClientSetting -ContainerType DistributedDefaultCache
  $DDC.MaxConnectionsToServer = 1
  $DDC.requestTimeout = "3000"
  $DDC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedDefaultCache $DDC

  #DistributedSearchCache
  $DSC = Get-SPDistributedCacheClientSetting -ContainerType DistributedSearchCache
  $DSC.MaxConnectionsToServer = 1
  $DSC.requestTimeout = "3000"
  $DSC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedSearchCache $DSC

  #DistributedSecurityTrimmingCache
  $DTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedSecurityTrimmingCache
  $DTC.MaxConnectionsToServer = 1
  $DTC.requestTimeout = "3000"
  $DTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedSecurityTrimmingCache $DTC

  #DistributedServerToAppServerAccessTokenCache
  $DSTAC = Get-SPDistributedCacheClientSetting -ContainerType DistributedServerToAppServerAccessTokenCache
  $DSTAC.MaxConnectionsToServer = 1
  $DSTAC.requestTimeout = "3000"
  $DSTAC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedServerToAppServerAccessTokenCache $DSTAC

  #DistributedFileLockThrottlerCache
  $DFLTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedFileLockThrottlerCache
  $DFLTC.MaxConnectionsToServer = 1
  $DFLTC.requestTimeout = "3000"
  $DFLTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedFileLockThrottlerCache $DFLTC

  #DistributedSharedWithUserCache
  $DSWUC = Get-SPDistributedCacheClientSetting -ContainerType DistributedSharedWithUserCache
  $DSWUC.MaxConnectionsToServer = 1
  $DSWUC.requestTimeout = "3000"
  $DSWUC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedSharedWithUserCache $DSWUC

  #DistributedUnifiedGroupsCache
  $DUGC = Get-SPDistributedCacheClientSetting -ContainerType DistributedUnifiedGroupsCache
  $DUGC.MaxConnectionsToServer = 1
  $DUGC.requestTimeout = "3000"
  $DUGC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedUnifiedGroupsCache $DUGC 

  #DistributedResourceTallyCache
  $DRTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedResourceTallyCache
  $DRTC.MaxConnectionsToServer = 1
  $DRTC.requestTimeout = "3000"
  $DRTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedResourceTallyCache $DRTC

  #DistributedHealthScoreCache
  $DHSC = Get-SPDistributedCacheClientSetting -ContainerType DistributedHealthScoreCache
  $DHSC.MaxConnectionsToServer = 1
  $DHSC.requestTimeout = "3000"
  $DHSC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedHealthScoreCache $DHSC  
  ```
  **SharePoint Server 2013 PowerShell script**

  ```
  Add-PSSnapin Microsoft.Sharepoint.Powershell -ea 0

  #DistributedLogonTokenCache
  $DLTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedLogonTokenCache
  $DLTC.MaxConnectionsToServer = 1
  $DLTC.requestTimeout = "3000"
  $DLTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedLogonTokenCache $DLTC

  #DistributedViewStateCache
  $DVSC = Get-SPDistributedCacheClientSetting -ContainerType DistributedViewStateCache
  $DVSC.MaxConnectionsToServer = 1
  $DVSC.requestTimeout = "3000"
  $DVSC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedViewStateCache $DVSC

  #DistributedAccessCache
  $DAC = Get-SPDistributedCacheClientSetting -ContainerType DistributedAccessCache
  $DAC.MaxConnectionsToServer = 1
  $DAC.requestTimeout = "3000"
  $DAC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedAccessCache $DAC

  #DistributedActivityFeedCache
  $DAF = Get-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedCache
  $DAF.MaxConnectionsToServer = 1
  $DAF.requestTimeout = "3000"
  $DAF.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedCache $DAF

  #DistributedActivityFeedLMTCache
  $DAFC = Get-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedLMTCache
  $DAFC.MaxConnectionsToServer = 1
  $DAFC.requestTimeout = "3000"
  $DAFC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedActivityFeedLMTCache $DAFC

  #DistributedBouncerCache
  $DBC = Get-SPDistributedCacheClientSetting -ContainerType DistributedBouncerCache
  $DBC.MaxConnectionsToServer = 1
  $DBC.requestTimeout = "3000"
  $DBC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedBouncerCache $DBC

  #DistributedDefaultCache
  $DDC = Get-SPDistributedCacheClientSetting -ContainerType DistributedDefaultCache
  $DDC.MaxConnectionsToServer = 1
  $DDC.requestTimeout = "3000"
  $DDC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedDefaultCache $DDC

  #DistributedSearchCache
  $DSC = Get-SPDistributedCacheClientSetting -ContainerType DistributedSearchCache
  $DSC.MaxConnectionsToServer = 1
  $DSC.requestTimeout = "3000"
  $DSC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedSearchCache $DSC

  #DistributedSecurityTrimmingCache
  $DTC = Get-SPDistributedCacheClientSetting -ContainerType DistributedSecurityTrimmingCache
  $DTC.MaxConnectionsToServer = 1
  $DTC.requestTimeout = "3000"
  $DTC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedSecurityTrimmingCache $DTC

  #DistributedServerToAppServerAccessTokenCache
  $DSTAC = Get-SPDistributedCacheClientSetting -ContainerType DistributedServerToAppServerAccessTokenCache
  $DSTAC.MaxConnectionsToServer = 1
  $DSTAC.requestTimeout = "3000"
  $DSTAC.channelOpenTimeOut = "3000"
  Set-SPDistributedCacheClientSetting -ContainerType DistributedServerToAppServerAccessTokenCache $DSTAC
  ```
3. Open the SharePoint Management Shell
    
4. Change to the directory to which you saved the file.
    
5. At the PowerShell command prompt, type the following command:
    
  ```
  ./MaxConnections.ps1
  ```

For more information, see [Application Configuration Settings (Windows Server AppFabric Caching)](http://go.microsoft.com/fwlink/?LinkID=614970&amp;clcid=0x409). For additional information about Windows PowerShell scripts and .ps1 files, see [Running Windows PowerShell Scripts](/previous-versions/windows/it-pro/windows-powershell-1.0/ee176949(v=technet.10)).
    
## Repair a cache host
<a name="repair"> </a>

During installation, configuration, or maintenance activities, the Distributed Cache service might enter a non-functioning state. Evidence of a malfunctioning Distributed Cache service will appear in Health Rules in Central Administration, or when users use features in SharePoint Server that rely on the Distributed Cache. For example, the Newsfeed on a user's My Site will start reporting errors. Also, administrators might receive the error message "cacheHostInfo is **null** " when they run SharePoint Management Shell cmdlets to manage the Distributed Cache service. 
  
There are two steps to repair a cache host.
  
On the non-functioning Distributed Cache host, use the following procedures to restore the Distributed Cache host. 
  
1. At the SharePoint Management Shell command prompt, run the [Remove-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Remove-SPDistributedCacheServiceInstance?view=sharepoint-ps) cmdlet. 
    
2. At the SharePoint Management Shell command prompt, run the [Add-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Add-SPDistributedCacheServiceInstance?view=sharepoint-ps) cmdlet. 
    
    > [!NOTE]
    > If step 1 fails, manually remove the Distributed Cache service, use the following steps. 
  
  - At the SharePoint Management Shell command prompt, type the following syntax.
    
  ```
  $instanceName ="SPDistributedCacheService Name=AppFabricCachingService"
 
  $serviceInstance = Get-SPServiceInstance | ? {($_.service.tostring()) -eq $instanceName -and ($_.server.name) -eq $env:computername}

  If($serviceInstance -ne $null)
  {
  $serviceInstance.Delete()
  }
  
  ```

  - After the Distributed Cache Service has been manually deleted, run step 2 again.


## See also
<a name="repair"> </a>

#### Concepts

[Plan for feeds and the Distributed Cache service in SharePoint Server](plan-for-feeds-and-the-distributed-cache-service.md)

