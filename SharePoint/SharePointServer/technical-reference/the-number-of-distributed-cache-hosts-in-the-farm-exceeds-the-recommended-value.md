---
title: "The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e56b99dc-3731-4cdd-8576-3777c3827e49
description: "Learn how to resolve the SharePoint Health Analyzer rule: The number of Distributed Cache hosts in the farm exceeds the recommended value, for SharePoint Server."
---

# The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The number of Distributed Cache hosts in the farm exceeds the recommended value. 
  
 **Summary:** On a farm with four or more servers, you must not start the Distributed Cache service on all servers on the farm. You can only run Distributed cache on SharePoint Server 2016 servers that are configured as Distributed cache role in MInRole. If you configure all servers as cache hosts, you may experience reliability and performance problems in the farm. For more information, see [Overview of MinRole Server Roles in SharePoint Server 2016](../install/overview-of-minrole-server-roles-in-sharepoint-server.md).
  
 **Cause:** The Distributed Cache service is started on every server on this farm. 
  
 **Resolution: Reduce the number of cache hosts by using Windows PowerShell.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  - Farm Administrators group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. Remove one or more servers from the cache cluster. On each server that you want to remove from the cache cluster, run the following cmdlet:
    
     `Remove-SPDistributedCacheServiceInstance`
    
4. Verify that the server is removed from the cache cluster. To do this, in the SharePoint Central Administration website, click **Manage services on server**, and then, on the **Services on Server** page, make sure that the Distributed Cache service is not listed for the server from which you removed the service. 
    
## See also
<a name="server"> </a>

#### Concepts

[Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md)
  
[Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md)
#### Other Resources

[Add-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Add-SPDistributedCacheServiceInstance?view=sharepoint-ps)
  
[Planning and using the Distributed Cache service](http://go.microsoft.com/fwlink/p/?LinkID=271302)

