---
title: "Verify each User Profile service application has a My Site host configured (SharePoint Server)"
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
ms.assetid: 2689bb6a-fd05-4273-87eb-daac5b2722f3
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify each User Profile service application has a My Site Host configured, for SharePoint Server."
---

# Verify each User Profile service application has a My Site host configured (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Verify each User Profile service application has a My Site Host configured. 
  
 **Summary:** Without a My Site host, end-users are not able to use personal sites or people profiles. Therefore, we recommend that if you create a User Profile Service service application, you also create a My Site host for the User Profile Service. 
  
 **Symptoms:** My Sites and other people profile features are not available to users. 
  
 **Cause:** The administrator who created the User Profile Service service application did not also create a My Site host. 
  
 **Resolution: Verify that a My Site site collection has been created**
  
- For information about setting up a My Site site collection, see [Configure My Sites in SharePoint Server](../install/configure-my-sites.md).
    
**Resolution: Associate the My Site host with a User Profile Service service application by using Microsoft PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Set-SPProfileServiceApplication [-Name <UserProfileServiceApplicationName>] -MySiteHostLocation <URL>
  ```

    Where:
    
  -  _\<UserProfileServiceApplicationName\>_ is the friendly name of the User Profile Service service application. If you only have one User Profile Service service application, you do not need to specify the name. 
    
  -  _\<URL\>_ is URL of an empty site collection that has no templates associated with it. 
    
## See also
<a name="server"> </a>

#### Other Resources

[Set-SPProfileServiceApplication](/powershell/module/sharepoint-server/Set-SPProfileServiceApplication?view=sharepoint-ps)

