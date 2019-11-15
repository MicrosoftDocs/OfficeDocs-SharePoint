---
title: "Which tool to use when migrating to SharePoint or OneDrive?"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: conceptual
ms.service: sharepoint-online
localization_priority: Normal
search.appverid: MET150
msCollection: 
- SPMigration
- M365-collaboration
description: "Which tool to use when migrating to SharePoint or OneDrive?"
---

# Which tool to use

Moving content to SharePoint Online or OneDrive for Business? There are several tools and methods you can use to migrate content to SharePoint Online or OneDrive, depending on the size and quantity of files you need to move.

To learn more about what method is best for you, see

|**Tool/method**|**Description**|**Best for**|
|:-----|:-----|:-----|
|SharePoint Migration Tool|The SharePoint Migration Tool (SPMT) can migrate your files from SharePoint on-premises document libraries, lists or regular files shares.</br>Download either the current release or the latest public preview: </br></br>[SharePoint Migration Tool (current release)](http://spmtreleasescus.blob.core.windows.net/install/default.htm) or </br>[SharePoint Migration Tool Public Preview](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)|Ideal for migrating SharePoint Server 2010 & 2013 environments or smaller file shares.|
|PowerShell|Using the PowerShell version of the SPMT. See [Migrate to SharePoint Online using PowerShell](https://docs.microsoft.com/sharepointmigration/overview-spmt-ps-cmdlets).|SPMT is ideal for migrating SharePoint Server 2010 & 2013 environments or smaller file shares via PowerShell. |
|Migration Manager (preview)|Available in the SharePoint Admin center, Migration Manager provides a centralized way of connecting servers, creating tasks, and automatically distributing your migration tasks.|Ideal for customers migrating large file shares.|
|Mover|Service for cloud to cloud migration. To learn more, see: [Mover](https://mover.io/)|Ideal for migrating data from other cloud service providers into OneDrive or SharePoint. Mover supports migration from over a dozen cloud service providers, including Box, Dropbox, Egnyte, and Google Drive. Use Mover to migrate from one SharePoint tenant to another.|
|Azure Data Box| The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy TBs of data from your servers to the device, ship it back to Microsoft, and your data is copied into Azure. One your data is in Azure, use SPMT to migrate content to SharePoint. </br> To learn more, see [Migrate using the Azure Data Box](/migration/how-to-migrate-file-share-content-to-SPO-using-AzureDataBox.md)|Ideal when you want remove the dependency on your WAN link to transfer data. Suitable for one-time migrations.|
|OneDrive sync app  <br/> |After installing the OneDrive sync app and syncing your library, you can drag and drop files to a folder on the computer and the content will automatically sync with either OneDrive or SharePoint.  <br/> To learn more, see:  [OneDrive Sync client](https://docs.microsoft.com/onedrive/one-drive-sync)|Ideal for individuals wanting to move files.|
|Manual upload  <br/> |Uploading files one at a time from the SharePoint Online tenant. <br/> |Best for smaller files.|

>[!Note]
>When you migrate your content to SharePoint Online or OneDrive, you are copying the files.  Your source files are not deleted.
