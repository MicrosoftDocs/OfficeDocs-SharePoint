---
title: How to use the Managed Solutions Gallery
ms.prod: SHAREPOINT
ms.assetid: 8926030c-ace4-4e32-ada6-3333b56812c3
---


# How to use the Managed Solutions Gallery
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2010, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* Learn how to use the Managed Solutions Gallery for code-based sandbox solutions in SharePoint Server 2016, SharePoint Server 2013, and SharePoint Server 2010.If you want to govern the activation of code-based sandbox solutions, you can utilize the Managed Solutions Gallery. This gallery is a specialized site collection and document library that identifies trusted code-based sandbox solutions within a SharePoint web application. Administrators with permission to upload solutions to the Managed Solutions Gallery can use this tool to determine which effectively approve the solutions they want to allow to activate within the web application.After an administrator uploads a solution to the Managed Solutions Gallery, site collection administrators can add and activate the solution using existing processes. Code-based sandbox solutions that are not in the Managed Solutions Gallery can't be activated by site collection administrators within the web application.
> [!IMPORTANT:]

  
    
    


## Overview

The Managed Solutions Gallery is a new feature in the September Public Update for code-based sandbox solutions which can be downloaded from here,  [SharePoint Updates](https://go.microsoft.com/fwlink/?LinkID=827479) https://go.microsoft.com/fwlink/?LinkID=827479
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

Before you can use the Managed Solutions Gallery, you must create a site collection on the Master Gallery, and then enable the functionality of the Managed Solutions Gallery. **Create and enable the Managed Solutions Gallery**
1.  Verify that you meet all of the following minimum requirements:
    
  - You must have membership in the securityadmin fixed server role on the SQL Server instance
    
  
  - You must have membership in the db_owner fixed database role on all databases that are to be updated.
    
  
  - You must be a member of the Administrators group on the server on which you are running the Windows PowerShell cmdlet.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
  
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012 R2 and Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
3. At the PowerShell command prompt, type the following command to create the site collection in the Managed Solutions Gallery.
    
  ```
  
# Creates a site collection and the Managed Solutions Gallery
$managedSolutionsGallerySite = New-SPSite -Url "http://localhost/sites/allowlist" -Template "STS#0" -Name " Managed Solutions Gallery site collection" -OwnerAlias "contoso\\admin" -OwnerEmail "admin@contoso.com"
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

We encourage customers that are considering moving away from the sandbox solution to the new SharePoint add-in model to review the considerations outlined here,  [Sandbox solution transformation guidance - InfoPath](http://go.microsoft.com/fwlink/?LinkID=827587&amp;clcid=0x409)SharePoint Add-ins are self-contained extensions of SharePoint websites that you create, and that run without custom code on the SharePoint server. To learn more about Add-ins see,  [SharePoint Add-ins](http://go.microsoft.com/fwlink/?LinkId=827588&amp;clcid=0x409)
# See also

#### 

 **Disable-SPUserSolutionAllowList**
  
    
    
 **Get-SPUserSolutionAllowList**
  
    
    

  
    
    

