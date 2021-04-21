---
title: Migrating OneNote folders with the SharePoint Migration Tool (SPMT)
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to migrate OneNote folder using the SharePoint Migration Tool SPMT."
---

# How the SharePoint Migration Tool (SPMT) migrates OneNote folders

The SharePoint Migration Tool (SPMT) supports migrating your OneNote folders to Microsoft 365.  
But before migrating your OneNote folders, it's important to understand a little about their file structure.  

On your computer, a OneNote Notebook is presented as a normal folder. For each Notebook, there's a *.onetoc2* file created under the root folder of the Notebook folder. You can have as many Notebooks as you want.

![OneNote migration setting1](media/onenote-file-1.png)</br></br>

If you create section groups in your Notebook, those groups are also presented as a folder. Under each section group, you can create multiple sections, and each one of those sections will be presented as *.one* file in file system. 

You can create multiple pages within a section, but the content of those pages will be contained in the same *.one* file as the section to which they belong.

![OneNote migration setting2](media/onenote-file-2.png)

When you open the OneNote application, they appear like this:

![OneNote migration setting3](media/onenote-file-3.png)


Folders are migrated to SharePoint as **OneNote Notebook** content rather than a normal folder with files. They'll appear in SharePoint like this:

![OneNote migration setting6](media/onenote-file-5.png)
