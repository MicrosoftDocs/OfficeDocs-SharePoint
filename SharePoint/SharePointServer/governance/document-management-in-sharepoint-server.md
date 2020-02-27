---
title: "Document management in SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 809fe3d9-6121-4e2e-8556-c48a39756365
description: "Learn about the elements of a document management solution and the document management planning process in SharePoint Server."
---

# Document management in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article contains a high-level description of the various elements of a document management solution that is based on SharePoint Server.
  
Document management controls the life cycle of documents in your organization — how they are created, reviewed, and published, and how they are ultimately disposed of or retained. Although the term "management" implies that information is controlled from the top of the organization, an effective document management system should reflect the culture of the organization that uses it. The tools that you use for document management should be flexible enough to enable you to tightly control a document's life cycle, if that fits your enterprise's culture and goals, but also to let you implement a more loosely structured system, if that better suits your enterprise.
  
## The elements of a document management system
<a name="section1"> </a>

An effective document management solution specifies the following:
  
- What kinds of documents and other content can be created in an organization.
    
- What template to use for each kind of document.
    
- What metadata to provide for each kind of document.
    
- Where to store a document at each stage of its life cycle.
    
- How to control access to a document at each stage of its life cycle.
    
- How to move documents within the organization as team members contribute to the documents' creation, review, approval, publication, and disposition.
    
SharePoint Foundation 2013 includes features that implement all these aspects of document management. SharePoint Server includes the same features and also adds the following:
  
- What policies to apply to documents so that document-related actions are audited, documents are retained or disposed of appropriately, and content that is important to the organization is protected.
    
- How to handle documents as corporate records, which must be retained according to legal requirements and corporate guidelines.
    
To make sure that information workers can easily take advantage of these capabilities without having to depart from their day-to-day operations and familiar tools, applications in the Microsoft Office system — such as Microsoft Outlook and Word — also include features that support each stage in a document's life cycle.
  
## The planning process
<a name="section2"> </a>

The document management planning process consists of the following major steps:
  
1. **Identify document management roles** Ensure that your plans incorporate the feedback of your organization's key stakeholders, you have the best team to implement the solution, and you know who will participate in document management processes. 
    
2. **Analyze document usage** After you identify who works on documents, determine the kinds of documents that they work on and how they use them. . 
    
3. **Plan the organization of documents** You can organize documents in site collections, sites, and libraries. SharePoint Server offers a range of features to help organize and store documents, from specialized sites to loosely structured document libraries for quick document creation and collaboration. Within a library, you can additionally organize content into folders and subfolders. 
    
4. **Plan how content moves between locations** It might be necessary to move or copy a document from one site or library to another at different stages of its life cycle. 
    
5. **Plan content types** Use content types to organize information about documents, such as metadata, document templates, and workflow processes. This is an important step to help you organize your documents and enforce consistency across your organization. 
    
6. **Plan workflows** When you plan workflows for your organization, you can control and track how documents move from one team member to another as each participant collaborates in a document's life cycle. SharePoint Server includes workflows for common team tasks such as reviewing and approving documents. SharePoint Server also supports creating and installing custom workflows. 
    
7. **Plan content governance** You can plan the appropriate degree of control that is based on content type or storage location. For example, you might require that documents in a particular library be checked out before they can be edited. 
    
8. **Plan policies** For each content type, plan information management policies to make sure that documents are audited, retained, and otherwise handled according to your organization's institutional and legal requirements. SharePoint Server includes policies that implement auditing, document retention, and bar codes (to make sure that printed content can be correlated with corresponding electronic versions). 
    
    > [!NOTE]
    > Policies are not available in SharePoint Foundation 2013. 
  

