---
title: The current server is running low on memory (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 63b9e454-f21e-4e0e-bc96-953c0a337c70
---


# The current server is running low on memory (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The current server is running low on memory" for SharePoint Server 2016. **Rule Name:**   The current server is running low on memory. **Summary:**    This rule only runs on servers that host the Distributed Cache service. The rule checks to see if the memory usage exceeds the allocated amount for a server that hosts the Distributed Cache service. If it finds the memory usage has exceeded the allocated amount then it triggers an alert. **Cause:**   SharePoint Server 2016 assigns 10 percent of the total physical memory on the server to the Distributed Cache service. The Distributed Cache service uses half of that memory for data storage and the other half for memory management overhead. When the cached data grows, the Distributed Cache service uses the entire 10 percent of the allocated memory. **Resolution: Check memory usage on the server and free more memory, add more RAM to the server, increase the Distributed Cache service memory allocation**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Check memory usage on SharePoint Server by using Resource Manager.
    
  
3. Add more RAM to the server.
    
  
4. Increase the memory allocation of the Distributed Cache service:
    
    > [!NOTE:]
      

1. Determine the total physical memory on the server that hosts the Distributed Cache service. For example if there is 16 GB of RAM available on the server, you reserve 2 GB of memory for other processes and services that run on the cache host. So 16 GB - 2 GB = 14 GB. This remaining memory is allocated to the Distributed Cache service..
    
  
2. Take half of the remaining memory and convert it to MB. for example, 14 GB/2 = 7 GB or 7168 MB. This is the cache size of the Distributed Cache service.
    
    Use the following procedure to update the memory allocation accordingly.
    
  
 **Change the memory allocation of the Distributed Cache**
1. (Optional) To check the existing memory allocation for the Distributed Cache service on a server, run the following command at the SharePoint Management Shell command prompt:
    
  ```
  
Use-CacheCluster
Get-AFCacheHostConfiguration -ComputerName ComputerName  -CachePort "22233"

  ```


    Where  *ComputerName*  is the computer name of the server that you are running the SharePoint Management Shell cmdlet on.
    
  
2. To reconfigure the cache size of the Distributed Cache service, run the following command one time only on any cache host at the SharePoint Management Shell command prompt:
    
  ```
  
Update-SPDistributedCacheSize -CacheSizeInMB CacheSize
  ```


    Where  *CacheSize*  is the cache size's memory allocation assignment in MB. In the previous example, the cache size was calculated at 7168 MB for a server with 16 GB of total memory.
    
  
3. Restart the Distributed Cache service on all cache hosts. To restart the Distributed Cache service, go to **Services on Server** in Central Administration, and **Start** the Distributed Cache service on all cache hosts in the farm.
    
  

