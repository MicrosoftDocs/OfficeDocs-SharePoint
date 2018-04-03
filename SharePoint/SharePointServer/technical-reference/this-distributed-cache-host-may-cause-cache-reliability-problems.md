---
title: "This Distributed Cache host may cause cache reliability problems (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 12/5/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 45b39899-1686-43e5-9073-e51d2979ba9b
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleThis Distributed Cache host may cause cache reliability problems, in SharePoint Server 2016 and SharePoint 2013."
---

# This Distributed Cache host may cause cache reliability problems (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "This Distributed Cache host may cause cache reliability problems", in SharePoint Server 2016 and SharePoint 2013. 
  
 **Rule Name:** This Distributed Cache host may cause cache reliability problems. 
  
 **Summary:** The Distributed Cache service on this cache host has been stopped but has not been unregistered from the farm. To avoid reliability issues, we recommend that you either start the Distributed Cache service on the server, or remove the cache host from the cache cluster. 
  
 **Cause:** The Distributed Cache service on this Distributed Cache host has been stopped but not unregistered from the farm. 
  
 **Resolution: Start the Distributed Cache service on the server by using Microsoft PowerShell.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Farm Administrators group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. On the server on which you want to start the Distributed Cache service, type the following command at the PowerShell command prompt:
    
  ```
  Add-SPDistributedCacheServiceInstance
  ```

4. In the SharePoint Central Administration website, click **Application Management**. In the **Service Applications** section, click **Manage services on server**. 
    
5. On the **Services on Server** page, verify that the Distributed Cache service is listed and the status is **Started**.
    
**Resolution: Remove the cache host from the cache cluster by using Windows PowerShell.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Farm Administrators group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. Type the following command at the PowerShell command prompt:
    
  ```
  Remove-SPDistributedCacheServiceInstance
  ```

    > [!NOTE]
    > This command stops the cache service and nonpersisted cached data will be lost. If you want to keep the cached data, use the graceful shutdown procedure that is described in [Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md), and then run the Remove-SPDistributedCacheServiceInstance cmdlet. The Remove-SPDistributedCacheServiceInstance cmdlet involves stopping and disabling the underlying AppFabric Caching service. Do not restart the AppFabric Caching service other than by running the Add-SPDistributedCacheServiceInstance cmdlet. 
  
    For more information, see [Remove-SPDistributedCacheServiceInstance](http://technet.microsoft.com/library/7cb14284-d0d8-4221-b81d-0a4470101880.aspx).
    
4. Verify that the server is removed from the cache cluster. To do this, in Central Administration, click **Manage services on server**, and then, on the **Services on Server** page, make sure that the Distributed Cache service is not listed. 
    
## See also
<a name="server"> </a>

#### Concepts

[Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md)
#### Other Resources

[Planning and using the Distributed Cache service](http://go.microsoft.com/fwlink/p/?LinkID=271302)

