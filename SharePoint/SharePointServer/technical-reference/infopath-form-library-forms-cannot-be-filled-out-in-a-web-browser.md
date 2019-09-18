---
title: "InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server)"
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
ms.assetid: 7ebd1422-4f3d-44b9-8df6-75274c65b7e5
description: "Learn how to resolve the SharePoint Health Analyzer rule: InfoPath form library forms cannot be filled out in a Web browser, for SharePoint Server."
---

# InfoPath form library forms cannot be filled out in a Web browser (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** InfoPath form library forms cannot be filled out in a Web browser 
  
 **Summary:** InfoPath Forms Services users can publish browser-enabled form templates to a SharePoint Server form library but cannot open the forms in a Web browser. 
  
> [!NOTE]
> This issue only applies to forms published to form libraries. It does not apply to list forms or to forms that have been uploaded by farm administrators. 
  
 **Cause:** One or more of the following might be causing this: 
  
- The **Render form templates that are browser-enabled by users** check box in the SharePoint Central Administration website is cleared. 
    
- The following Windows PowerShell command has been run:  `Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $false`.
    
**Resolution: Enable browser rendering of user forms by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group. 
    
2. Start Central Administration.
    
3. In Central Administration, click **General Application Settings**.
    
4. On the General Application Settings page, in the **InfoPath Forms Services** section, click **Configure InfoPath Forms Services**.
    
5. On the Configure InfoPath Forms Services page, in the **User Browser-enabled Form Templates** section, select the **Render form templates that are browser-enabled by users** check box. 
    
6. Click **OK** at the bottom of the page. 
    
**Resolution: Enable browser rendering of user forms by using Microsoft PowerShell**
  
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
  Set-SPInfoPathFormsService -AllowUserFormBrowserRendering $true
  ```

For more information, see [Set-SPInfoPathFormsService](/powershell/module/sharepoint-server/Set-SPInfoPathFormsService?view=sharepoint-ps).
  

