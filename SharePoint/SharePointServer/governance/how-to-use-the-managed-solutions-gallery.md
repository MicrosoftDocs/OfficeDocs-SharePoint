---
title: "How to use the Managed Solutions Gallery"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 8926030c-ace4-4e32-ada6-3333b56812c3
description: Learn how to use the Managed Solutions Gallery for code-based sandbox solutions in SharePoint Server.

---

# How to use the Managed Solutions Gallery

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Learn how to use the Managed Solutions Gallery for code-based sandbox solutions in SharePoint Server 2013, SharePoint Server 2016, and SharePoint Server 2019.
  
If you want to govern the activation of code-based sandbox solutions, you can utilize the Managed Solutions Gallery. This gallery is a specialized site collection and document library that identifies trusted code-based sandbox solutions within a SharePoint web application. Administrators with permission to upload solutions to the Managed Solutions Gallery can use this tool to determine which effectively approve the solutions they want to allow to activate within the web application.
  
After an administrator uploads a solution to the Managed Solutions Gallery, site collection administrators can add and activate the solution using existing processes. Code-based sandbox solutions that are not in the Managed Solutions Gallery can't be activated by site collection administrators within the web application.
  
> [!IMPORTANT]
> When an InfoPath form that contains custom code is published in a web application with a Managed Solutions Gallery, the form no longer renders in a browser. It also creates a category of sandbox solution that cannot be approved using the Managed Solutions Gallery, so publishing fails and the form can no longer be rendered by InfoPath Forms Services. For additional information, see [InfoPath Forms Containing Code Fail to Activate when using the Managed Solutions Gallery](https://support.microsoft.com/en-us/kb/3192603). 
  
## Overview

The Managed Solutions Gallery is a new feature in the September Public Update for code-based sandbox solutions which can be downloaded from here, [SharePoint Updates](https://go.microsoft.com/fwlink/?LinkID=827479) https://go.microsoft.com/fwlink/?LinkID=827479 
  
> [!NOTE]
> The September Public Update includes the English-language version of the Managed Solutions Gallery. A future Public Update will include the Multi-language versions of the Managed Solutions Gallery. 
  
> [!NOTE]
> To initially setup and configure the Managed Solutions Gallery is only available by using the following Microsoft PowerShell cmdlets: [New-SPUserSolutionAllowList](/powershell/module/sharepoint-server/New-SPUserSolutionAllowList?view=sharepoint-ps), [Enable-SPUserSolutionAllowList](/powershell/module/sharepoint-server/Enable-SPUserSolutionAllowList?view=sharepoint-ps). To use these cmdlets you must use elevated administrator privileges, by using RunAs Administrator. > Once the gallery is configured, it is treated as a document library (that is, SPList) and can be managed by using the user interface. 
  
Before you can use the Managed Solutions Gallery, you must create a site collection on the Master Gallery, and then enable the functionality of the Managed Solutions Gallery.
  
 **Create and enable the Managed Solutions Gallery**
  
1.  Verify that you meet all of the following minimum requirements: 
    
  - You must have membership in the securityadmin fixed server role on the SQL Server instance
    
  - You must have membership in the db_owner fixed database role on all databases that are to be updated.
    
  - You must be a member of the Administrators group on the server on which you are running the Microsoft PowerShell cmdlet.
    
    An administrator can use the [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps) cmdlet to grant permissions to use SharePoint Server  cmdlets. 
    
2. Start the SharePoint Management Shell.
    
 
   
3. At the PowerShell command prompt, type the following command to create the site collection in the Managed Solutions Gallery.
    
  ```
  # Creates a site collection and the Managed Solutions Gallery
  $managedSolutionsGallerySite = New-SPSite -Url "http://localhost/sites/allowlist" -Template "STS#0" -Name " Managed Solutions Gallery site collection" -OwnerAlias "contoso\admin" -OwnerEmail "admin@contoso.com"
  ```

  ```
  $managedSolutionsGallery = New-SPUserSolutionAllowList -Site $managedSolutionsGallerySite -ListTitle "Managed Solutions Gallery"
  ```

4. At the PowerShell command prompt, type the following command to enable the functionality of the Managed Solutions Gallery.
    
  ```
  # Enables the Managed Solutions Gallery functionality
  Enable-SPUserSolutionAllowList
  ```

    If you want to disable the functionality of the Managed Solutions Gallery, you can run the **Disable-SPUserSolutionAllowList** cmdlet. 
    
## Transform your sandbox solutions to the SharePoint add-in model

We encourage customers that are considering moving away from the sandbox solution to the new SharePoint add-in model to review the considerations outlined here, [Sandbox solution transformation guidance - InfoPath](http://go.microsoft.com/fwlink/?LinkID=827587&amp;clcid=0x409)
  
SharePoint Add-ins are self-contained extensions of SharePoint websites that you create, and that run without custom code on the SharePoint server. To learn more about Add-ins see, [SharePoint Add-ins](http://go.microsoft.com/fwlink/?LinkId=827588&amp;clcid=0x409)
  
## See also

#### Other Resources

[Disable-SPUserSolutionAllowList](/powershell/module/sharepoint-server/Disable-SPUserSolutionAllowList?view=sharepoint-ps)
  
[Get-SPUserSolutionAllowList](/powershell/module/sharepoint-server/Get-SPUserSolutionAllowList?view=sharepoint-ps)

