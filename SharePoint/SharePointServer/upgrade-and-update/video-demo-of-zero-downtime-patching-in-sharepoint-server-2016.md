---
title: "Video demo of Zero Downtime Patching in SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: d454aed4-4e26-4ef1-9f72-a605af6ed2cd
description: "Take a SharePoint tutorial that can help you learn how to patch a server in a SharePoint Server 2016 farm by using Zero Downtime Patching."
---

# Video demo of Zero Downtime Patching in SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]  
  
## Overview

One of the new features in SharePoint Server 2016 is Zero Downtime patching.
  
Zero Downtime patching doesn't demand any server downtime while patching a SharePoint Server 2016 farm, but does require that your farm be set up in a Highly Available (HA) configuration (so that SharePoint roles are hosted on more than one server). That way, patching can be done in batches where certain of the redundant servers are taken out of load balancing, patched, replaced, and tested for soundness before the other servers follow through the same process.
  
There is a two-step process to patch a server in a SharePoint Server 2016 farm. First, you install the binaries of the patch to each server, this is called the patch phase. Second, after you finish the patch phase, you must complete the update installation by starting the build-to-build upgrade phase.
  
During Zero downtime patching, users can add and edit files and use search just as at any other time, accessing the servers still handled by the load balancer. Likewise, though the database schemas may differ between the patched and unpatched sides of the farm, SharePoint Server 2016 operates in a backward-compatible mode, and its databases are able to properly function, until patching completes.
  
This SharePoint tutorial explains how to patch a SharePoint Server 2016 HA farm from beginning to end, including the installation of the binary files on all servers, and the build-to-build (B2B) upgrade itself.
  
> [!VIDEO https://www.microsoft.com/videoplayer/embed/ec659395-d173-4c1b-bbcb-8a896498948c?autoplay=false]
  
> [!IMPORTANT]
> During the demonstration, the graceful shut down of Distributed Cache Service was discussed and demonstrated. The environment depicted is a test farm and the process shown is NOT how a customer should do this in a live environment. 
  
 **Important**: If you are actively using areas such as Microblogs, Newsfeeds etc. you will instead need to use the following steps to gracefully shut down the Distributed Cache Service on each Distributed Cache Server during the patch and upgrade sequence: 
  
 **Gracefully STOP Distributed Cache Service**
  
$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"
  
$serviceInstance = Get-SPServiceInstance | ? {($_.service.tostring()) -eq $instanceName -and ($_.server.name) -eq $env:computername}
  
$serviceInstance.Unprovision()
  
 **Start Distributed Cache Service**
  
$instanceName ="SPDistributedCacheService Name=AppFabricCachingService"
  
$serviceInstance = Get-SPServiceInstance | ? {($_.service.tostring()) -eq $instanceName -and ($_.server.name) -eq $env:computername}
  
$serviceInstance.Provision()
  
For reference, here is an overview of the steps, however for further detail on SharePoint patching please watch the video.
  
1. Remove the Front-end web server (SPWEB01) from the Load balancer.
    
2. Patch the front-end web server (SPWEB01) by using the STS &amp; WSS Packages.
    
3. Restart the front-end web server (SPWEB01).
    
4. Add the front-end web server (SPWEB01) back into the Load balancer.
    
5. Remove the front-end web server (SPWEB02) from the Load balancer.
    
6. Patch the front-end web server (SPWEB02).
    
7. Restart the front-end web server (SPWEB02) computer.
    
8. Patch the following Application servers: SPAPP01, SPDCH01, and SPSRCH01 in parallel, and then restart the computers.
    
9. Patch the following Application servers: SPAPP02, SPDCH02, and SPSRCH02 in parallel, and then restart the computers.
    
10. With the front-end web server (SPWEB02) out of the Load balancer (See step 7), Open the SharePoint 2016 Management Shell, and then run following PSConfig command:  `PSConfig.exe -cmd upgrade -inplace b2b -wait -cmd applicationcontent -install -cmd installfeatures -cmd secureresources -cmd services -install`
    
    > [!NOTE]
    > In the video, syntax is condensed to save time, but the full syntax listed in Step 10 is the recommend one to run. 
  
11. Once the upgrade is complete, add the front-end web server (SPWEB02) back into the Load balancer. Once the front-end web server (SPWEB02) has been added to the Load balancer, remove the front-end web server (SPWEB01).
    
12. On the front-end web server (SPWEB01) computer, run the PSConfig command from step 10.
    
13. Add the front-end web server (SPWEB01) back into the Load balancer.
    
14. On the Application server (SPAPP01), run the PSConfig command from Step 10.
    
15. On the Distributed Cache server (SPDCH01), run the PSConfig command from Step 10.
    
16. On the Search server (SPSRCH01), run the PSConfig command from Step10.
    
17. Once the upgrade has completed run the same steps (14-16) on 02 series servers (SPAPP02, SPDCH02, SPSRCH02).
    
> [!NOTE]
> We recommend to test pages throughout to ensure patching and upgrading of servers is complete. 
  
During the video the following Microsoft PowerShell script was used to take Servers out of the Azure Service Management Internal Load Balancer.
  
```
#Remove the SPWEB01 Azure Load Balanced EndPoint
$svc=<"NameYourLBService">
$vmname=<"NameofYourVM">
$epname="TCP-80-80"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add the SPWEB01 AzureEndpoint back
$ilb="minroleilb"
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM
# Remove the SPWEB02 Azure Load Balanced EndPoint for the patch install and build to build (B2B) phase
$vmname=<"NameofYourVM">
$epname="TCP-80-80-2"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add for the B2B SPWEB02 AzureEndPoint to ILB
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80-2"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM
# B2B for SPWEB01::::: Phase Remove the SPWEB01 Azure Load Balanced EndPoint
$svc=<"NameYourLBService">
$vmname=<"NameofYourVM">
$epname="TCP-80-80"
Get-AzureVM -ServiceName $svc -Name $vmname | Remove-AzureEndpoint -Name $epname | Update-AzureVM
#Add the SPWEB01 AzureEndpoint back
$ilb="minroleilb"
$prot="tcp"
$locport=80
$pubport=80
$epname="TCP-80-80"
$lbsetname=<"NameYourLB">
$vmname=<"NameofYourVM">
Get-AzureVM -ServiceName $svc -Name $vmname | Add-AzureEndpoint -Name $epname -LbSetName $lbsetname -Protocol $prot -LocalPort $locport -PublicPort $pubport -DefaultProbe -InternalLoadBalancerName $ilb | Update-AzureVM

```

For additional information about the Microsoft PowerShell for Azure cmdlets, see [Get-AzureVM](https://msdn.microsoft.com/en-us/library/mt126007.aspx) and [Add-AzureEndpoint](https://msdn.microsoft.com/en-us/library/mt589127.aspx)
  
## Related Topics

[Install a software update for SharePoint Server 2016](install-a-software-update.md)
  
[SharePoint Server 2016 zero downtime patching steps](sharepoint-server-2016-zero-downtime-patching-steps.md)
  
[Video: How to enable Remote Windows PowerShell to use with SharePoint Server](video-how-to-enable-remote-windows-powershell-to-use-with-sharepoint-server.md)
  

