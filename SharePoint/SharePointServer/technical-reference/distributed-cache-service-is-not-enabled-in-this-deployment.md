---
title: "Distributed cache service is not enabled in this deployment (SharePoint Server)"
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
ms.assetid: 6e743c5b-b70c-4e86-ae31-e5ffcc0c099a
description: "Learn how to resolve the SharePoint Health Analyzer rule: Distributed cache service is not enabled in this deployment, for SharePoint Server."
---

# Distributed cache service is not enabled in this deployment (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Distributed cache service is not enabled in this deployment. 
  
 **Summary:** The Distributed Cache service is started on all servers that run SharePoint products at installation time. However, an administrator that performs maintenance and operational tasks might need to start and stop the Distributed Cache service. This event occurs when the Distributed Cache service is stopped. 
  
 **Cause:** The Distributed Cache service is disabled on this server. 
  
 **Resolution: Enable the Distributed Cache service by using Microsoft PowerShell.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Farm Administrators group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. On the server on which you want to enable the Distributed Cache service, run the following command:
    
     `Add-SPDistributedCacheServiceInstance`
    
4. Verify that the Distributed Cache service is started. To do this, in the SharePoint Central Administration website, click **Application Management**. In the **Service Applications** section, click **Manage services on server**. On the **Services on Server** page, make sure that the Distributed Cache service is listed, and the status is **Started**. 
    
## See also
<a name="server"> </a>

#### Concepts

[Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md)
  
[Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md)
#### Other Resources

[Add-SPDistributedCacheServiceInstance](/powershell/module/sharepoint-server/Add-SPDistributedCacheServiceInstance?view=sharepoint-ps)
  
[Planning and using the Distributed Cache service](http://go.microsoft.com/fwlink/p/?LinkID=271302)

