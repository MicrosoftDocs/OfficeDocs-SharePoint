---
title: "Plan document versioning, content approval, and check-out controls in SharePointServer"
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: b607e000-9436-4cbb-b6aa-9e76d70a4314
description: "Learn how to use versioning, content approval, and check-out in SharePoint Server to control document versions throughout their life cycle."
---

# Plan document versioning, content approval, and check-out controls in SharePointServer

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to plan to use versioning, content approval, and check-out in SharePoint Server to control document versions throughout their life cycle.
  
## About versioning, content approval, and check-outs
<a name="bkmk_about"> </a>

SharePoint Server includes the following features that can help you control documents in a document library: 
  
- Versioning is the method by which successive iterations of a document are numbered and saved. 
    
- Content approval is the method by which site members who have approver permissions control the publication of content. 
    
- Check-out and Check-in are the methods by which users can better control when a new version of a document is created and also comment on changes that they made when they check a document in. 
    
You configure settings for the content governance features discussed in this article in document libraries. To share these settings across libraries in your solution, you can create document library templates that include your content governance settings. This makes sure that new libraries will reflect your content governance decisions.
  
For more information about versioning, see [Enable and configure versioning for a list or library](https://go.microsoft.com/fwlink/?LinkId=275820).
  
## Plan versioning
<a name="bkmk_plan_versioning"> </a>

The default versioning control for a document library depends on the site collection template. However, you can configure versioning control for a document library depending on your particular requirements. Each document library can have a different versioning control that best suits the kind of documents in the library. SharePoint Server has three versioning options:
  
- **No versioning** Specifies that no earlier versions of documents are saved. When versioning is not being used, earlier versions of documents are not retrievable, and document history is also not retained because comments that accompany each iteration of a document are not saved. Use this option on document libraries that contain unimportant content or content that will never change. 
    
- **Create major versions** Specifies that numbered versions of documents are retained by using a simple versioning scheme (such as 1, 2, 3). To control the effect on storage space, you can specify how many earlier versions to keep, counting back from the current version. 
    
    In major versioning, every time that a new version of a document is saved, all users who have permissions to the document library will be able to view the content. Use this option when you do not want to differentiate between draft versions of documents and published versions. For example, in a document library that is used by a workgroup in an organization, major versioning is a good choice if everyone on the team must be able to view all iterations of each document.
    
- **Create major and minor (draft) versions** Specifies that numbered versions of documents are retained by using a major and minor versioning scheme (such as 1.0, 1.1, 1.2, 2.0, 2.1). Versions ending in **.0** are major versions and versions ending with non-zero extensions are minor versions. Previous major and minor versions of documents are saved together with current versions. To control the effect on storage space, you can specify how many previous major versions to keep, counting back from the current version. You can also specify how many major versions being kept should include their respective minor versions. For example, if you specify that minor versions should be kept for two major versions and the current major version is 4.0, then all minor versions starting at 3.1 will be kept. 
    
    In major and minor versioning, any user who has read permissions can view major versions of documents. You can specify which users can also view minor versions. Typically, we recommend that you grant permissions to view and work with minor versions to the users who can edit items, and restrict users who have read permissions to viewing only major versions.
    
    Use major and minor versioning when you want to differentiate between published content that can be viewed by an audience and draft content that is not yet ready for publication. For example, on a human resources Web site that describes organizational benefits, use major and minor versioning to restrict employees' access to benefits descriptions while the descriptions are being revised.
    
> [!NOTE]
> When you create a new version of a document, [the incremental changes are stored in SQL Server](https://go.microsoft.com/fwlink/?LinkId=303695), rather than a complete new copy of the document. This provides the most efficient storage and helps reduce overall storage requirements. 
  
## Plan content approval
<a name="bkmk_plan_conapprov"> </a>

Use content approval to formalize and control making content available to an audience. For example, an enterprise that publishes content as one of its products or services might require a legal review and approval before publishing the content. 
  
A document draft awaiting content approval is in the Pending status. When an approver reviews the document and approves the content, it becomes available for viewing by users who have read permissions. A document library owner can enable content approval for a document library and, optionally, can associate a workflow with the library to run the approval process.
  
The way that documents are submitted for approval varies depending on the versioning settings in the document library:
  
- **No versioning** If versioning is not being used and changes to a document are saved, the document's status becomes Pending. SharePoint Server keeps the earlier version of the document so that users who have read permissions can still view it. After the pending changes are approved, the new version of the document is made available for viewing by users who have read permissions and the earlier version is not retained. 
    
    If versioning is not being used and a new document is uploaded to the document library, it is added to the library in the Pending status and is not viewable by users who have read permissions until it is approved.
    
- **Create major versions** If major versioning is being used and changes to a document are saved, the document's status becomes Pending and the previous major version of the document is made available for viewing by users who have read permissions. After changes to the document are approved, a new major version of the document is created and made available to users who have read permissions, and the previous major version is saved to the document's history list. 
    
    If major versioning is being used and a new document is uploaded to the document library, it is added to the library in the Pending status and is not viewable by users who have read permissions until it is approved as version 1.
    
- **Create major and minor (draft) versions** If major and minor versioning is being used and changes to a document are saved, the author has the choice of saving a new minor version of the document as a draft or creating a new major version, which changes the document's status to Pending. After the changes to the document are approved, a new major version of the document is created and made available to users who have read permissions. In major and minor versioning, both major and minor versions of documents are kept in a document's history list. 
    
    If major and minor versioning is being used and a new document is uploaded to the document library, it can be added to the library either in the Draft status as version 0.1 or the author can immediately request approval. In this case, the document's status becomes Pending.
    
## Plan check-out and check-in
<a name="bkmk_plan_checkin"> </a>

You can require users to check out documents from a document library before they edit the documents. The benefits of requiring check-out and check-in include the following:
  
- Better control of when document versions are created. When a document is checked out, the author can save the document without checking it in. Other users of the document library will be unable to see these changes, and a new version is not created. A new version (visible to other users) is only created when an author checks in a document. This gives the author more flexibility and control.
    
- Better capture of metadata. When a document is checked in, the author can write comments that describe the changes that were made to the document. This creates an ongoing historical record of the changes that were made to the document.
    
If your solution requires users to check in and check out documents to edit them, you can use features in Office client applications that support these actions. Users can check out documents, undo check-outs, and check in documents from Office client applications.
  
When a document is checked out, it is locked for exclusive editing by the user. When the user saves edits to this file, the changes are uploaded and saved to the server. The changes are private to the user and not visible to others. When the user is ready to check in the document, the latest changes are made visible to others and published.
  
From Office client applications, users can also choose to leave checked-out documents on the server by changing content editing options.
  
> [!NOTE]
> You should not check out a document when you use the co-authoring functionality. 
  

