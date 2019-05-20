---
title: "Configure the co-authoring versioning period in SharePoint Server"
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 59f3af85-89f9-43ba-b364-28a810cae42e
description: "Learn how to specify how often SharePoint Server stores a version of a document that is being edited."
---

# Configure the co-authoring versioning period in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The CoauthoringVersionPeriod property specifies, in minutes, how often SharePoint stores a version of a document that is being edited. This article describes how to use Microsoft PowerShell to configure the CoauthoringVersionPeriod property. For more information about document library versioning, see [Configure versioning for co-authoring in SharePoint 2013](configure-versioning-for-co-authoring.md).
  
## Configure the co-authoring versioning period in SharePoint Server 2013

When versioning is turned on, SharePoint Server 2013 takes periodic snapshots of documents, saving them for later reference. This information can provide an edit trail that may be useful for seeing who changed a document, rolling back to an earlier version, or for compliance reasons. 
  
You can configure the CoauthoringVersionPeriod property by using the Microsoft PowerShell. If the value is set to 0, SharePoint Server 2013 captures every change made by a new user in a different version of the document. If the value is set to a very large number, SharePoint Server 2013 creates one version for the whole editing session. This latter behavior matches the behavior of files that are not co-authored and files that were created in earlier versions of SharePoint Server 2013 or SharePoint Foundation.
  
 **To configure the co-authoring versioning period by using Windows PowerShell (save as script and run script)**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Paste the following code into a text editor, such as Notepad:
    
  ```
  $siteurl ="<ServerName>" 
  $mysite=new-object Microsoft.SharePoint.SPSite($siteurl)
  $mysite.WebApplication.WebService.CoauthoringVersionPeriod = <Time>
  $mysite.WebApplication.WebService.Update()
  ```

3. Specify the following parameters:
    
   **Parameters to configure the co-authoring versioning period**

|**Parameter**|**Value**|
|:-----|:-----|
| _ServerName_ <br/> |Server name  <br/> |
| _Time_ <br/> |Number in minutes  <br/> |
   
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

#### Concepts

[Configure versioning for co-authoring in SharePoint 2013](configure-versioning-for-co-authoring.md)
  
[Overview of co-authoring in SharePoint Server](co-authoring-overview.md)

