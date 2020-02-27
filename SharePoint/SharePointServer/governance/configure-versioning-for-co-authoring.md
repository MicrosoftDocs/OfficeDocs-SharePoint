---
title: "Configure versioning for co-authoring in SharePoint 2013"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: d0db716b-1ee7-42c7-b8cf-694360b39d56
description: "Learn how to configure SharePoint document library versioning settings to support co-authoring."
---

# Configure versioning for co-authoring in SharePoint 2013

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Document library versioning is the method by which successive iterations of a document are numbered and saved. By default, versioning is disabled in SharePoint Server 2013 document libraries . We recommend that you enable this feature for document libraries in which users plan to co-author documents or presentations.
  
Before you configure versioning for co-authoring, review [Overview of co-authoring in SharePoint Server](co-authoring-overview.md).
  
    
## Configure versioning for co-authoring in SharePoint Server 2013
<a name="bkmk_vers"> </a>

SharePoint versioning helps protect documents and prevent data loss by allowing authors to roll back to a previous document version when the current version contains unwanted changes. 
  
Do not enable minor versioning in document libraries that contain OneNote notebooks. Minor versioning can result in synchronization errors that prevent edits from being saved.
  
When multiple authors work on the same document, edits are retained on the server as document versions. To limit server storage usage, you can limit the number of retained versions. If you enable major versioning in a document library that contains OneNote notebooks, we recommend that you specify the maximum number of versions so you can use disk space more efficiently. 
  
 **To enable versioning**
  
1. Browse to the document library that you want to configure.
    
2. In the toolbar, on the **LIBRARY** tab, in the **Settings** group, choose **Library Settings**.
    
3. In **General Settings**, choose **Versioning settings**.
    
4. In **Document Version History**, select **Create major versions**.
    
5. To specify a version retention limit, select **Keep the following number of major versions** and in the text box, type the number of versions. 
    
## Configure Require Check Out in SharePoint Server 2013
<a name="bkmk_req_co"> </a>

When a document is checked out of a document library, the document is locked. This makes it unavailable for co-authoring. Therefore, the **Require Check Out** setting should not be enabled in document libraries that are used for co-authoring. By default, for SharePoint Server 2013 document libraries, this setting is not enabled. 
  
 **To disable Require Check Out**
  
1. Browse to the document library that you want to configure.
    
2. In the toolbar, on the **LIBRARY** tab, in the **Settings** group, choose **Library Settings**.
    
3. In **General Settings**, choose **Versioning settings**.
    
4. In **Require Check Out**, select **No** (default). 
    
## See also
<a name="bkmk_req_co"> </a>

#### Concepts

[Overview of co-authoring in SharePoint Server](co-authoring-overview.md)
  
[Configure the co-authoring versioning period in SharePoint Server](configure-the-co-authoring-versioning-period.md)

