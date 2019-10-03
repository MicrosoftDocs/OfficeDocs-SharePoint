---
title: "Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 10/24/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d7d023a6-0d61-47ae-b442-3fd8108bcbb7
description: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is unexpectedly configured on server(s), for SharePoint Server 2016."
---

# Distributed cache service is unexpectedly configured on server(s) (SharePoint Server 2016)

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]
  
 **Rule Name:** Distributed cache service is unexpectedly configured on server(s). 

 **Summary:** The distributed cache service instance should not be configured for the failing servers. Remove the distributed cache service instances from the failing servers. 
  
Typically when you see this rule, it states that the distributed cache service is running on a server that doesn't support this service. The distributed cache service should only run on servers that are assigned to the following roles:
  
- Distributed Cache
    
- ﻿Front-end with Distributed Cache
    
- ﻿Single-Server Farm
    
- ﻿Custom
    
For more information, see [Description of MinRole and associated services in SharePoint Server 2016](../administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md).
  
 **Cause:** This rule occurs when you have configured the distributed cache service on a server that is not supposed to run this service in a SharePoint Server 2016 farm. 
  
 **Resolution: Remove the distributed cache service instances from the failing servers**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPDistributedCacheServiceInstance?view=sharepoint-ps). 
  
2. Start the SharePoint 2016 Management Shell on each failing server.
    
3. Type the following command at the PowerShell command prompt on each failing server:
    
  ```
  Remove-SPDistributedCacheServiceInstance
  ```

For more information, see [Remove-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Remove-SPDistributedCacheServiceInstance?view=sharepoint-ps).
  

