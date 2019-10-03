---
title: "The current server is running low on memory (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 63b9e454-f21e-4e0e-bc96-953c0a337c70
description: "Learn how to resolve the SharePoint Health Analyzer rule: The current server is running low on memory, for SharePoint Server."
---

# The current server is running low on memory (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The current server is running low on memory. 
  
 **Summary:** This rule only runs on servers that host the Distributed Cache service. The rule checks to see if the memory usage exceeds the predefined threshold on a server that hosts the Distributed Cache service. If it finds the total memory usage of the server is 85% or higher it then triggers an alert.
  
 **Cause:** SharePoint Server assigns 10 percent of the total physical memory on the server to the Distributed Cache service. The Distributed Cache service uses half of that memory for data storage and the other half for memory management overhead. When the cached data grows, the Distributed Cache service uses the entire 10 percent of the allocated memory. 
  
 **Resolution: Check memory usage on the server and free more memory, add more RAM to the server, increase the Distributed Cache service memory allocation**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Check memory usage on SharePoint Server by using Resource Manager.
    
3. Add more RAM to the server.
    
4. Increase the memory allocation of the Distributed Cache service:
    
    > [!NOTE]
    > When you add physical memory to the server, the Distributed Cache service doesn't automatically recalculate the 10% memory allocation. So you need to manually increase the Distributed Cache service memory allocation. 
  
1. Determine the total physical memory on the server that hosts the Distributed Cache service. For example if there is 16 GB of RAM available on the server, you reserve 2 GB of memory for other processes and services that run on the cache host. So 16 GB - 2 GB = 14 GB. This remaining memory is allocated to the Distributed Cache service..
    
2. Take half of the remaining memory and convert it to MB. for example, 14 GB/2 = 7 GB or 7168 MB. This is the cache size of the Distributed Cache service.
    
Use the following procedure to update the memory allocation accordingly.
    
**Change the memory allocation of the Distributed Cache**
  
1. (Optional) To check the existing memory allocation for the Distributed Cache service on a server, run the following command at the SharePoint Management Shell command prompt:
    
  ```
  Use-CacheCluster
  Get-AFCacheHostConfiguration -ComputerName ComputerName -CachePort "22233"
  
  ```

Where  _ComputerName_ is the computer name of the server that you are running the SharePoint Management Shell cmdlet on. 
    
2. To reconfigure the cache size of the Distributed Cache service, run the following command one time only on any cache host at the SharePoint Management Shell command prompt:
    
  ```
  Update-SPDistributedCacheSize -CacheSizeInMB CacheSize
  ```

Where  _CacheSize_ is the cache size's memory allocation assignment in MB. In the previous example, the cache size was calculated at 7168 MB for a server with 16 GB of total memory. 
    
3. Restart the Distributed Cache service on all cache hosts. To restart the Distributed Cache service, go to **Services on Server** in Central Administration, and **Start** the Distributed Cache service on all cache hosts in the farm. 
    
## See also

#### Other Resources

[Update-SPDistributedCacheSize](/powershell/module/sharepoint-server/Update-SPDistributedCacheSize?view=sharepoint-ps)

