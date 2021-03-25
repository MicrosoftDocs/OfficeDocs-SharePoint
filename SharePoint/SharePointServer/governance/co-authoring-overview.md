---
title: "Overview of co-authoring in SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: serdars
ms.date: 3/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: f6accc60-23b8-4242-b12d-e118270251cf
description: "Provides information about co-authoring and the permissions and software versions that are required for co-authoring in SharePoint Server and SharePoint in Microsoft 365."
---

# Overview of co-authoring in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Audience**: IT Professionals
  
Co-authoring in SharePoint Server lets multiple users work on a document, at any time, without interfering with each other's changes. Co-authoring removes barriers to server-based document collaboration. This feature helps organizations avoid unintentional multiple versions of documents by reducing the need to share attachments. This feature requires no extra server setup and is the default state for documents stored in SharePoint Server. You manage co-authoring by using the same tools and technologies that are already used to manage SharePoint.
  
Office provides co-authoring functionality for Word, PowerPoint, OneNote, and Visio. If you have SharePoint Server configured to use Office Web Apps Server, users can also co-author documents in Word, PowerPoint, Excel, and OneNote Web Apps.
  
> [!IMPORTANT]
> This article is for IT Professionals managing SharePoint Server.  **Are you looking for help with co-authoring?** You may be looking for [Document collaboration and co-authoring](https://go.microsoft.com/fwlink/p/?LinkId=275815), which will help you understand and use the co-authoring and versioning and applies to SharePoint in Microsoft 365.
  
## Co-authoring functionality in SharePoint Server
<a name="bkmk_ca_in_sp"> </a>

In traditional collaboration, documents are shared via email attachments. Tracking versions and edits from multiple authors is difficult and time-consuming for users. Email systems have to contend with storing multiple copies of the same document, not to mention increased network traffic as documents are sent repeatedly.
  
Storing documents for collaboration on SharePoint reduces these problems by: providing consistent access to up-to-date versions of documents, allowing users to track earlier versions, and centralizing management. Storing a single document, instead of many attachments, also reduces network and storage overhead.
  
But this solution hasn't been perfect. When one author has a document open, other authors can't work on it. Forgetting to close a document or check it in may lock out other users indefinitely, which can require help from the IT department to fix.
  
Co-authoring in SharePoint Server addresses these issues by making it possible for multiple users to work on a document, at any time, without interfering with each other's changes. This approach streamlines many common document-collaboration scenarios. For example:
  
- Two or more authors work on different parts of a composite document. While one author works on part A of the document, another author can work on part B, without either interrupting the other's work.

- Several authors work on a composite slide show. Each author adds slides to the presentation and edits them, instead of working on separate presentations and trying to merge them later.

- A document is sent out to several experts and stakeholders, and each of them provides some edits or additions. No user's edits are lost, because they're all working on a central, server-stored document.

## Understanding the end-user experience of co-authoring in SharePoint Server
<a name="bkmk_understd"> </a>

Co-authoring is easy to use from the end user's point of view. When a user wants to work on a document in Word, PowerPoint, OneNote, Visio or one of the Office Web Apps, they open it from SharePoint Server, as usual. If another user already has the document open, both users can edit the document at the same time. One exception to this is that users can co-author in Excel Web App only if everyone uses the Excel Web App to access the workbook. If anyone uses Excel (the client application) to access the workbook, co-authoring in Excel Web App turns off for that workbook while it's open in the client application.
  
When a user saves a Word, PowerPoint, or Word document, other current users are notified that there are new edits. Those users can refresh their views immediately to see the changes or continue their work and refresh later to see the latest edits. PowerPoint Web App, and Excel Web App autosave so that users can view any changes automatically. The authors see one another's work, and everyone knows who is working on the document. SharePoint Server versioning and tracking tools protect the document so that authors can roll back unwanted changes. When Skype for Business is available, users see the online status of fellow co-authors and start instant messaging conversations without leaving the document.
  
In OneNote and OneNote Web App, shared notebooks allow users to share notes seamlessly. When a user edits a page of the notebook, those edits automatically synchronize with other users of that notebook so that everybody has a complete set of notes. Edits made by multiple users on the same page appear automatically for nearly real-time collaboration. Versioning and other shared features in OneNote let users roll back edits, show what edits are new, and determine who made a specific edit.
  
The Excel client application doesn't support co-authoring workbooks in SharePoint Server. The Excel client application uses the Shared Workbook feature to support non-real-time co-authoring workbooks that are stored locally or on network (UNC) paths. Co-authoring workbooks in SharePoint is supported by using the Excel Web App.
  
## Important planning considerations for co-authoring in SharePoint Server
<a name="bkmk_imp_consid"> </a>

Co-authoring functionality in SharePoint is designed to be easy to set up and requires minimal effort to manage. But, there are several things to consider when you set up and manage co-authoring:
  
- **Permissions** - Each user who wants to edit a document needs edit permissions for the document library where that document is stored. The simplest way to guarantee that is to give all users access to the SharePoint site where documents are stored. In cases where only a subset of users should have permission to co-author documents in a particular library, SharePoint permissions can be used to manage access. For more information, see [Overview of site permissions in SharePoint Server](../sites/overview-of-site-permissions-in-sharepoint-server.md).

- **Versioning** - SharePoint Server versioning keeps track of changes to documents while they're being edited, and even stores earlier versions for reference. By default, this feature is turned off in SharePoint Server. SharePoint Server supports two kinds of versioning, major and minor. Minor versioning should remain off for document libraries that are used for co-authoring in OneNote, because it may interfere with OneNote's synchronization and versioning. This limitation only applies to minor versioning. Major versioning may be used with OneNote. For more information, see [How does versioning work in a list or library?](https://go.microsoft.com/fwlink/p/?LinkId=275819).

- **Number of versions** - The number of document versions kept affects storage requirements on the server. Tune this number in the document library settings to limit the number of versions. Frequently updated OneNote notebooks can result in many versions being stored on the server. To avoid using unnecessary disk space, set the maximum number of versions to a reasonable number on document libraries used to store OneNote notebooks. For more information, see [Enable and configure versioning for a list or library](https://go.microsoft.com/fwlink/p/?LinkId=275820)

- **Versioning period** - The versioning period determines how often SharePoint Server creates a version of a Word or PowerPoint document that is being co-authored. Setting this period to a low value captures versions more often, for more detailed version tracking, but may require more server storage. The versioning period doesn't affect OneNote notebooks. Adjust this value with the `coAuthoringVersionPeriod` property on the server. For more information about adjusting this setting, see [Configure the co-authoring versioning period in SharePoint Server](configure-the-co-authoring-versioning-period.md).

- **Check out** - When a user checks out a document for editing, the document is locked for editing by that user. This feature prevents co-authoring. Don't enable the **Require Check Out** feature in document libraries in which co-authoring will be used. By default, **Require Check Out** isn't enabled in SharePoint Server. Users shouldn't check out documents manually when co-authoring is being used. For more information, see [Set up a library to require check-out of files](https://go.microsoft.com/fwlink/p/?LinkId=275822).
    
## Planning considerations for co-authoring in OneNote notebooks
<a name="bkmk_onenote"> </a>

Unlike Word and PowerPoint, OneNote stores version information within the file itself. For this reason, administrators should follow these recommended practices when storing OneNote notebooks in a SharePoint Server document library:
  
- Don't turn on minor versioning. By default, minor versioning is turned off in SharePoint Server.

- Major versioning is turned on in SharePoint Server by default. Set a reasonable maximum number of versions to store.  
    
## Performance and scalability considerations for co-authoring in SharePoint Server
<a name="bkmk_perf"> </a>

SharePoint Server and Office applications minimize the performance and scalability impact that is associated with co-authoring in your environment. Office clients don't send or download co-authoring information from the server until more than one author is editing. When a single user is editing a document, the performance impact resembles that of earlier versions of SharePoint.
  
To reduce server impact, Office clients synchronize co-authoring actions less often when the server is under heavy load, or when users are not actively editing the document. This helps reduce overall performance impact.
  
## See also
<a name="bkmk_perf"> </a>

[Plan document versioning, content approval, and check-out controls in SharePointServer](versioning-content-approval-and-check-out-planning.md)