---
title: "Disable co-authoring in SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 7d2cbe64-5888-415e-81be-98b6921929de
description: "Learn how to disable co-authoring functionality in SharePoint Server by using Group Policy or by using PowerShell."
---

# Disable co-authoring in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Co-authoring in SharePoint Server makes it possible for multiple users to work on a document, at any time, without interfering with each other's changes. Although we have engineered co-authoring to be scalable and efficient, some organizations that have hardware limitations may want to turn off co-authoring to minimize any additional effects on server performance. 
  
This article describes how to disable co-authoring functionality in SharePoint Server by using Group Policy or by using PowerShell.
  
## Disable co-authoring in SharePoint Server

There are three ways to disable co-authoring:
  
- You can use Group Policy to disable co-authoring functionality on the client-side. For more information, see [Group Policy overview for Office 2013](/previous-versions/office/office-2013-resource-kit/cc179176(v=office.15)).
    
- You can use Microsoft PowerShell to set the DisableCoauthoring server property. This disables the co-authoring property for Word and PowerPoint documents on the server. This property applies to documents or presentations that are authored in Word 2010, Word 2013, Word Online, PowerPoint 2010, PowerPoint 2013 and PowerPoint Web App.
    
- You can enable the Require Check Out setting in a document library. This disables co-authoring in the document library. For more information, see [Configure Require Check Out in SharePoint Server 2013](configure-versioning-for-co-authoring.md#bkmk_req_co).
    
Procedures in this task:
  
- To disable co-authoring by using Group Policy
    
- To disable co-authoring for Word documents and PowerPoint presentations at the web service level by using Windows PowerShell
    
- To disable co-authoring for Word documents and PowerPoint presentations at the web application level by using Windows PowerShell
    
 **To disable co-authoring by using Group Policy**
  
1. Start **Group Policy Management**.
    
2. In **Group Policy Management**, expand the Forest and Domain nodes for the domain where you want to set the policy, and then expand **Group Policy Objects**.
    
3. Choose (right-click) the Group Policy Object where your co-authoring settings are configured, and then choose **Edit**.
    
4. For Word 2013, expand **User Configuration**, **Administrative Templates**, **Microsoft Word 2013**, **Collaboration Settings**, **Co-authoring**, and then open (double-click) **Prevent Co-authoring**.
    
    For PowerPoint 2013, expand **User Configuration**, **Administrative Templates**, **Microsoft PowerPoint 2013**, **Collaboration Settings**, **Co-authoring**, and then choose **Prevent Co-authoring**.
    
5. In the **Prevent Co-authoring Properties** dialog box, select **Enabled**, and then choose **OK**.
    
 **To disable co-authoring for Word documents and PowerPoint presentations at the web service level by using Windows PowerShell (save as script and run script)**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  $siteurl = "<servername>"
  $mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
  $mysite.WebApplication.WebService.DisableCoauthoring = $true;
  $mysite.WebApplication.WebService.Update();
  ```

3. Specify the following parameter:
    
|**Parameter**|**Value**|
|:-----|:-----|
| _servername_ <br/> |Server name  <br/> |
   
4. Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
5. Start the SharePoint 2013 Management Shell as Administrator.
    
6. Change to the directory to which you saved the file.
    
7. At the PowerShell command prompt, type the following command:
    
  ```
  ./SuggestedFileName.ps1
  ```

 **To disable co-authoring for Word documents and PowerPoint presentations at the web application level by using Windows PowerShell (save as script and run script)**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  $siteurl = "<servername>"
  $mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
  $mysite.WebApplication.DisableCoauthoring = $true;
  $mysite.WebApplication.Update();
  
  ```

3. Specify the following parameter:
    
|**Parameter**|**Value**|
|:-----|:-----|
| _servername_ <br/> |Server name  <br/> |
   
4. Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
5. Start the SharePoint 2013 Management Shell as Administrator.
    
6. Change to the directory to which you saved the file.
    
7. At the PowerShell command prompt, type the following command:
    
  ```
  ./SuggestedFileName.ps1
  ```

## See also

[Overview of co-authoring in SharePoint Server](co-authoring-overview.md)
  

