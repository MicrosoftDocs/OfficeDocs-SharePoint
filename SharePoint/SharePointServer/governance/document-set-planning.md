---
title: "Plan document sets in SharePoint Server 2013"
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: f3c0fda5-7a36-4c5d-801f-8a3baccb6d6a
description: "Learn about the Document Set feature in SharePoint Server, how to administer Document Sets, and plan for Document Set content types."
---

# Plan document sets in SharePoint Server 2013

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes Documents Sets and provides guidance on how you can integrate them with your SharePoint Server document management solution.
  
    
## About Document Sets
<a name="bkmk_about_ds"> </a>

Document Sets are a feature in SharePoint Server that enables an organization to manage a single deliverable, or work product, which can include multiple documents or files. A Document Set is a special kind of folder that combines unique Document Set attributes, the attributes and behavior of folders and documents, and provides a user interface (UI), metadata, and object model elements to help manage all aspects of the work product.
  
For teams and users in many organizations, a set of documents, or a work product, is needed to better manage a project or deliverable. For example, a legal team might need to collect, create, and manage various documents, photos, and audio files that are related to a particular case. Or, a sales team might need to compile documents from various sources to create and manage a request for proposal (RFP) for a potential client. Documents Sets provide those teams and users with the ability to manage those sets of documents as a single collection, deliverable, or work product. Document Set owners can then create a custom Welcome Page that can display the items included and important information about the work product.
  
In SharePoint Server, organizations that want to create and manage Document Sets consistently can configure a Document Set content type for each work product they typically create. A Document Set content type can then define approved content types, attributes, default items, columns, workflows, and policies. Additional customized Document Set content types can then be created from the parent content type, each inheriting properties and settings from the parent Document Set content type. After the content type is added to a library, users can then create a Document Set that inherits the attributes of the Document Set content type by using the **New** command. A Document Set content type provides additional settings that enable you to specify allowed content types, default content, shared columns, Welcome Page columns, and default Welcome Page view. 
  
For more information about content types, see [Plan content types and workflows in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262735(v=office.14)).
  
For more information about how to create and manage Document Sets in SharePoint Server 2013, see [Create and configure a new document set content type](https://office.microsoft.com/en-us/sharepoint-server-help/create-and-configure-a-new-document-set-content-type-HA102773262.aspx?CTT=1) in SharePoint Server 2013 Help. 
  
## Administering Document Sets
<a name="bkmk_admin_ds"> </a>

Document Sets in SharePoint Server share many of the same attributes and properties as folders. However there are some important considerations you should be aware of when planning a Document Set solution.
  
- There is no limit on the number of documents that can exist in a Document Set. However, display load times may be limited by the list view threshold which by default is set at 5,000 items. Folders are allowed in document sets, but metadata navigation cannot be used in a Document Set. Therefore, it is important to consider the possibility of exceeding list view thresholds and navigation design concerns when you determine how many items should exist in a Document Set. In addition, when you use the **Send to** feature with a Document Set, the sum for all documents in a Document Set cannot be larger than 50MB. For a collection or work product with a very large number of items, a folder structure in a document library may be a better solution. 
    
- There is no limit on the number of Document Sets that can exist in a document library. However, the number of Document Sets that can appear in lists will be limited by the list view threshold.
    
- When using shared metadata, if there are more than 10 items that are using shared metadata in a Document Set, metadata updates will be run by a timer job every 15 minutes. For example, if you have 10 documents in the top level of the library, and a single document in a Document Set with shared metadata, the time job will not run. But if you add another Document Set with 9 more documents, the timer job will run.
    
- When using Document Set routing, Document Sets that are sent to a content organizer will remain in the drop-off library and be moved to the appropriate location by the content organizer processing timer job, which by default runs daily.
    
To use Document Sets in a site collection, the Document Sets feature must be enabled.
  
 **To enable Document Sets feature for a site collection**
  
1. On the **Site Settings** page, under **Site Collection Administration**, click **Site collection features**.
    
2. On the **Features** page, for **Document Sets**, click **Activate**.
    
After the Document Sets feature is enabled, you can create Document Set content types.
  

