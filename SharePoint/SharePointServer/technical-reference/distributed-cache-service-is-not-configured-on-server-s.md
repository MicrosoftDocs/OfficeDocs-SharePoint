---
title: "Distributed cache service is not configured on server(s) (SharePoint Server 2016)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0e24bb6a-8977-467f-bf69-0cfef1c8e288
description: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is not configured on server(s), for SharePoint Server."
---

# Distributed cache service is not configured on server(s) (SharePoint Server 2016)

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]
  
 **Rule Name:** Distributed cache service is not configured on server(s). 

 **Summary:** The distributed cache service should be configured for the failing servers. Register the distributed cache host on the failing servers, and then start the service instances. 
  
 **Cause:** This rule occurs when you have used the MinRole feature in SharePoint Server 2016 to assign a distributed cache role to a server or servers but haven't registered the distributed cache host or started the service. 
  
 **Resolution: Use the Add-SPDistributedCacheServiceInstance cmdlet to register a cache host**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint 2016 Management Shell on each failing server.
    
3. Type the following command at the PowerShell command prompt on each failing server:
    
  ```
  Add-SPDistributedCacheServiceInstance
  ```

For more information, see [Add-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Add-SPDistributedCacheServiceInstance?view=sharepoint-ps).
  
## Related Topics

[Description of MinRole and associated services in SharePoint Server 2016](../administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md)
  

