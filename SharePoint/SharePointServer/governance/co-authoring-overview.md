---
title: "Overview of co-authoring in SharePoint Server"
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/7/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: f6accc60-23b8-4242-b12d-e118270251cf
description: "Provides information about co-authoring and the permissions and software versions that are required for co-authoring in SharePoint Server and SharePoint Online."
---

# Overview of co-authoring in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
 **Audience**: IT Professionals
  
Use the co-authoring feature in SharePoint Server or SharePoint Online to enable multiple users to work on a document, at any time, without interfering with each other's changes. Co-authoring removes barriers to server-based document collaboration and helps organizations to reduce the overhead associated with traditional document sharing through attachments. This functionality requires no additional server setup and is the default state for documents stored in SharePoint Server and SharePoint Online. Co-authoring functionality is managed by using the same tools and technologies that are already used to manage SharePoint, helping to minimize the impact on administrators. 
  
Office provides co-authoring functionality for Word, PowerPoint, OneNote, and Visio. If you are using SharePoint Online or have SharePoint Server configured to use Office Web Apps Server, users can also co-author documents in Word, PowerPoint, Excel, and OneNote Web Apps. 
  
> [!IMPORTANT]
> This article is for IT Professionals. It applies to planning for co-authoring in an organization. > **Are you looking for help with co-authoring?** You may be looking for [Document collaboration and co-authoring](https://go.microsoft.com/fwlink/p/?LinkId=275815), which will help you understand and use the co-authoring and versioning features of SharePoint Server. 
  
## Co-authoring functionality in SharePoint Server and SharePoint Online
<a name="bkmk_ca_in_sp"> </a>

In traditional collaboration, documents are shared via email attachments. Tracking versions and edits from multiple authors is difficult and time-consuming for users. Email systems have to contend with storing multiple copies of the same document, not to mention increased network traffic as documents are sent repeatedly.
  
The use of SharePoint to store documents for collaboration has reduced these problems by providing consistent access to up-to-date versions of documents, the ability to track earlier versions, and centralized management. Storing a single document, instead of many attachments, also reduces network and storage overhead.
  
But this solution hasn't been perfect. When one author has a document open, other authors can't work on it. If someone forgets to close a document or check it in, other users may be locked out indefinitely, a situation that often requires a call to the IT department.
  
Co-authoring in SharePoint Server addresses these issues by making it possible for multiple users to work on a document, at any time, without interfering with each other's changes. This approach streamlines many common document-collaboration scenarios. For example:
  
- Two or more authors work on different parts of a composite document. While one author works on his section of the document, another author can work on hers, without either interrupting the other's work.
    
- Several authors work on a composite slide show. Each author can add slides to the presentation and edit them, instead of working in isolation and trying to merge several documents and make them consistent all at the same time.
    
- A document is sent out to several experts and stakeholders, each of whom provides some edits or additions. No user's edits are lost, because they are all working on a central, server-stored document.
    
## Understanding the end-user experience of co-authoring in SharePoint Server and SharePoint Online
<a name="bkmk_understd"> </a>

Co-authoring is easy to use from the end user's point of view. When a user wants to work on a document in Word, PowerPoint, OneNote, Visio or one of the Office Web Apps, he or she merely opens it from SharePoint Server or SharePoint Online, as usual. If another user already has the document open, both users can edit the document at the same time. One exception to this is that users can co-author in Excel Web App only if everyone uses the Excel Web App to access the workbook. If anyone uses Excel (the client application) to access the workbook, co-authoring in Excel Web App will be disabled for that workbook while it is open in the client application. 
  
When a user saves a Word, PowerPoint, or Word Online document, other current users are notified that there are new edits. Those users can refresh their views immediately to see the changes or continue their work and refresh later to see the latest edits. PowerPoint Web App, and Excel Web App auto-save so that users can view any changes automatically. The authors can see one another's work, and everyone knows who is working on the document. SharePoint Server and SharePoint Online versioning and tracking tools protect the document so that authors can roll back unwanted changes. When Skype for Business is available, users can see the online status of fellow co-authors and start instant messaging conversations without leaving the document.
  
In OneNote and OneNote Web App, shared notebooks enable users to share notes seamlessly. When a user edits a page of the notebook, those edits are automatically synchronized with other users of that notebook so that everybody has a complete set of notes. Edits made by multiple users on the same page appear automatically, which enables near real-time collaboration. Versioning and other shared features in OneNote make it possible for users to roll back edits, show what edits are new, and determine who made a specific edit. 
  
The Excel client application does not support co-authoring workbooks in SharePoint Server. The Excel client application uses the Shared Workbook feature to support non-real-time co-authoring workbooks that are stored locally or on network (UNC) paths. Co-authoring workbooks in SharePoint is supported by using the Excel Web App. 
  
## Important planning considerations for co-authoring in SharePoint Server and SharePoint Online
<a name="bkmk_imp_consid"> </a>

There are several factors that administrators will want to consider when planning how to use co-authoring in their environment.
  
Co-authoring functionality in SharePoint is designed to be easy to set up and requires minimal effort to manage. But, there are several things to consider when you set up and manage co-authoring:
  
- **Permissions** - For multiple users to be able to edit the same document, users need edit permissions for the document library where that document is stored. The simplest way to guarantee that this is to give all users access to the SharePoint site where documents are stored. In cases in which only a subset of users should have permission to co-author documents in a particular library, SharePoint permissions can be used to manage access. For more information, see [Overview of site permissions in SharePoint Server](/sharepoint/sites/overview-of-site-permissions-in-sharepoint-server).
    
- **Versioning** -SharePoint Server versioning keeps track of changes to documents while they are being edited, and even stores earlier versions for reference. By default, this feature is turned off in SharePoint Server. SharePoint Server supports two kinds of versioning, major and minor. It is best that minor versioning remain off for document libraries that are used for co-authoring in OneNote, because it may interfere with the synchronization and versioning capabilities that are part of the product. This limitation only applies to minor versioning. Major versioning may be used with OneNote. For more information, see [How does versioning work in a list or library?](https://go.microsoft.com/fwlink/p/?LinkId=275819).
    
- **Number of versions** - The number of document versions retained affects storage requirements on the server. This number can be tuned in the document library settings to limit the number of versions retained. OneNote notebooks that are frequently updated may result in many versions being stored on the server. To avoid using unnecessary disk space, we recommend that an administrator set the maximum number of versions retained to a reasonable number on document libraries used to store OneNote notebooks. For more information, see [Enable and configure versioning for a list or library](https://go.microsoft.com/fwlink/p/?LinkId=275820)
    
- **Versioning period** - The versioning period determines how often SharePoint Server will create a version of a Word or PowerPoint document that is being co-authored. Setting this period to a low value will capture versions more often, for more detailed version tracking, but may require more server storage. The versioning period does not affect OneNote notebooks. This value can be altered by adjusting the coAuthoringVersionPeriod property on the server. For more information about adjusting this setting, see [Configure the co-authoring versioning period in SharePoint Server](configure-the-co-authoring-versioning-period.md).
    
- **Check out** - When a user checks out a document for editing, the document is locked for editing by that user. This prevents co-authoring. Do not enable the **Require Check Out** feature in document libraries in which co-authoring will be used. By default, **Require Check Out** is not enabled in SharePoint Server. Users should not check out documents manually when co-authoring is being used. For more information, see [Set up a library to require check-out of files](https://go.microsoft.com/fwlink/p/?LinkId=275822).
    
## Planning considerations for co-authoring in OneNote notebooks
<a name="bkmk_onenote"> </a>

Unlike Word and PowerPoint, OneNote stores version information within the file itself. For this reason, administrators should follow these recommended practices when storing OneNote notebooks in a SharePoint Server document library:
  
- Do not enable minor versioning. By default, minor versioning is not enabled in SharePoint Server.
    
- Major versioning is enabled in SharePoint Server by default. Set a reasonable maximum number of versions to store.  
    
## Performance and scalability considerations for co-authoring in SharePoint Server and SharePoint Online
<a name="bkmk_perf"> </a>

SharePoint Server and Office 2016 applications minimize the performance and scalability impact that is associated with co-authoring in your environment. Office clients do not send or download co-authoring information from the server until more than one author is editing. When a single user is editing a document, the performance impact resembles that of earlier versions of SharePoint.
  
Office clients are configured to reduce server impact by reducing the frequency of synchronization actions that are related to co-authoring when the server is under heavy load, or when a user is not actively editing the document. This helps reduce overall performance impact. 
  
## See also
<a name="bkmk_perf"> </a>

[Plan document versioning, content approval, and check-out controls in SharePointServer](versioning-content-approval-and-check-out-planning.md)

