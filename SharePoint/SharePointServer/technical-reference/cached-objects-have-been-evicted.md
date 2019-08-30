---
title: "Cached objects have been evicted (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/22/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: bdb3b575-7c20-490d-9a28-e7108edabad5
description: "Learn how to resolve the SharePoint Health Analyzer rule: Cached objects have been evicted."
---

# Cached objects have been evicted (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Cached objects have been evicted 
  
 **Summary:** When the memory consumption of the cache service on a cache host exceeds the low watermark threshold, objects that have already expired are evicted. When memory consumption exceeds the high watermark threshold, objects are evicted from memory, whether they have expired or not, until memory consumption returns to the low watermark. Subsequently cached objects may be rerouted to other hosts to maintain an optimal distribution of memory. 
  
 **Cause:** There is not sufficient memory in the cache cluster. 
  
 **Resolution: Add more RAM to the server**
  
- You can add more RAM to the server to increase the memory. To identify the failing server: in the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** list. If there are multiple failing servers in a server farm, you must repeat this resolution on each failing server. 
    
**Resolution: Increase the memory allocation of the distributed cache**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  - Farm Administrators group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. Check the current distributed cache settings from usage. To do this, run the following command: 
    
     `Get-SPDistributedCacheClientSetting`
    
    For more information, see [Get-SPDistributedCacheClientSetting](/powershell/module/sharepoint-server/Get-SPDistributedCacheClientSetting?view=sharepoint-ps)
    
4. Stop the Distributed Cache service on all cache hosts in the farm. To do this, run the following command on each cache host:
    
     `Stop-SPDistributedCacheServiceInstance -Graceful`
    
    For more information, see "Perform a graceful shutdown of the Distributed Cache service" in [Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md).
    
5. To increase the cache size of the Distributed Cache service, run the following command one time only on any cache host at the PowerShell command prompt:
    
     `Update-SPDistributedCacheSize -CacheSizeInMB CacheSize`
    
    Where:
    
  -  _CacheSize_ is the cache size's memory allocation assignment in megabytes (MB). The default value is 5 percent of total system RAM. This value should not be more than 40 percent of total system RAM with a maximum limit of 16 gigabytes (GB). 
    
6. Start the Distributed Cache service on all cache hosts. To start the Distributed Cache service, go to the **Services on Server** page in Central Administration, and start the Distributed Cache service on all cache hosts in the farm. 
    
## See also
<a name="server"> </a>

#### Concepts

[Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md)
  
[Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md)
#### Other Resources

[Update-SPDistributedCacheSize](/powershell/module/sharepoint-server/Update-SPDistributedCacheSize?view=sharepoint-ps)
  
[Planning and using the Distributed Cache service](http://go.microsoft.com/fwlink/p/?LinkID=271302)

