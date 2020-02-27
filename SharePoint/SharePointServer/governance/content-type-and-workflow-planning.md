---
title: "Plan content types and workflows in SharePoint Server"
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
ms.assetid: 7af845bc-f245-459f-871d-0ee06c64a184
description: "Learn how to integrate content types and workflows into your SharePoint Server document management solution."
---

# Plan content types and workflows in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes content types and workflows and provides guidance about how to plan to integrate them into your SharePoint Server document management solution. A content type is a reusable collection of metadata (columns), workflow, behavior, and other settings for a category of items or documents in a SharePoint Server list or document library. Content types enable you to manage the settings for a category of information in a centralized, reusable way. A workflow lets you attach a business process to items in SharePoint Server. 
  
Before you use the [Content type and workflow planning](https://go.microsoft.com/fwlink/p/?LinkID=165878) (https://go.microsoft.com/fwlink/p/?LinkID=165878) worksheet included with this article to plan your content types and workflows, ensure that you have read [Identify users and analyze document usage in SharePoint Server](identify-users-and-analyze-document-usage.md) and completed the "Analyze document usage" and the "Document participants" worksheets associated with that article. 
  
## Content type overview
<a name="overview"> </a>

A content type defines the attributes of a list item, a document, or a folder. Each content type can specify the following:
  
- Properties to associate with items of its type.
    
- Metadata to associate with items of its type.
    
- Workflows that can be started from items of its type.
    
- Information management policies to associate with items of its type.
    
- Document templates (for document content types).
    
- Custom features.
    
You can associate a content type with a list or library. When you do this, you are specifying that the list or library can contain items of that content type and that the **New** command in that list or library will let users create new items of that type. 
  
> [!NOTE]
> You can also associate properties, workflows, policies, and templates directly with a list or library. However, doing this can limit these associations to the list or library and is not reusable across your solution. In SharePoint Server 2013, site-level workflows can be associated with multiple lists or libraries. 
  
Document libraries and lists can contain multiple content types. For example, a library can contain both the documents and the graphics related to a project. When a list or library contains multiple content types, the following apply:
  
- By default, the **New** command in that list or library lets users select from all available content types when they create a new item. Content type owners can configure the **New** command to display only certain content types. 
    
- The columns associated with all available content types are displayed.
    
You can define custom content types in a site's content type gallery. A custom content type must be derived, directly or indirectly, from a core content type such as Document or Item. After it is defined in a site, a custom content type is available in that site and in all sites below that site. To make a content type most widely available throughout a site collection, define it in the content type gallery of the top-level site. In SharePoint Server, you can also create a custom content type inside a content type hub that is defined in a managed metadata service instance. When it is created in a content type hub, the content type will be available to other site collections that are part of web applications associated with that managed metadata service instance. 
  
> [!NOTE]
> The Managed Metadata service and the content type hub are not available in SharePoint Foundation 2013. 
  
For example, if your organization uses a particular contract template, in the content type gallery of the top-level site in a site collection, you can create a content type that defines the metadata for that contract, the contract's template, and workflows required to review and complete the contract. Then, any document library in your site collection to which you associate the Contract content type will include all these features and will enable authors to create new contracts based on the template.
  
In sites that are based on SharePoint Server, each default list item or library item, such as Contact, Task, or Document, has a corresponding core content type in the site's content type gallery. When you plan content types, you can use these core content type definitions as starting points and base new content types on existing ones as needed.
  
Content types are organized into a hierarchy that lets one content type inherit its characteristics from another content type. This inheritance enables classes of documents to share characteristics across an organization, and it enables teams to customize these characteristics for particular sites or lists.
  
For example, all user-deliverable documents in an enterprise might require a set of metadata, such as account number, project number, and project manager. By creating a top-level Customer Deliverable content type from which all other customer-deliverable document types inherit, you make sure that required information, such as account numbers and project numbers, will be associated with all variants of customer-deliverable documents in your organization. Note that if the content type owner adds another required column to the top-level Customer Deliverable content type, the content type owner can propagate the changes to all content types that inherit from it, which will add the new column to all customer deliverable documents.
  
### Properties integration with Office
<a name="officeintegration"> </a>

In the Microsoft Office system, when a user edits a document from a SharePoint Server document management server, a Document Information Panel is shown at the top of the document. The Document Information Panel displays an editable form of the document's properties on the server.
  
SharePoint Server makes it easy to customize the property form for a content type. When you configure a content type, you can start InfoPath, which generates a default property form that is based on the properties of the content type. The default form includes the same controls, layout, and schema that InfoPath would use if no custom form were defined. You can then customize and deploy the form as you would any other InfoPath form. For example, you can add your company logo, fonts, and color scheme to a form; connect it to a custom data source; add conditional logic; and design form features that are available to users based on their roles.
  
Along with editing properties in the Document Information Panel, authors who use Word can insert properties that are defined on the server into their documents. For example, if the document properties include a project manager name, this name can be inserted into the title page, the footer, or anywhere else the name is used in the document. If a new project manager is assigned to a project, the Project Manager property can be updated on the document management server. This updated project manager name will be reflected in every instance of this property that was inserted into a document.
  
### Using metadata with content types
<a name="metadata"> </a>

Metadata is information about a document that is used to categorize and classify your content. Metadata is associated with a content type as a column. Metadata can provide contextual information about your document by associating it with an author, subject, audience, language, and so on. Unlike properties, metadata are stored as columns and can be indexed and searched on by the SharePoint Search engine.
  
Metadata added at the site collection level can be associated with content types. By using metadata with content types, all later content types can inherit some or all the metadata from the parent content type at the site collection level. Additional metadata can then be added at a lower level, such as a single document.
  
### Column templates
<a name="columns"> </a>

Each item of metadata that is associated with a content type is a column, which is a location in a list to store information. Lists or libraries are often displayed graphically as columns of information. However, depending on the view associated with the list, the columns can appear in other forms, such as days in a calendar display. In forms associated with a list or library, columns are displayed as fields.
  
You can define columns for use in multiple content types. To do this, create them in a Column Templates gallery. There is a Column Templates gallery in each site in a site collection. As with content types, columns defined in the Column Templates gallery of a site are available in that site and in all sites below it.
  
### Folder content types
<a name="folders"> </a>

Folder content types define the metadata that is associated with a folder in a list or library. When you apply a folder content type to a list or library, the **New** command in that list or library will include the folder content type, which makes it possible for users create folders of that type. 
  
You can define views in a list or library that are available only in folders of a particular content type. This is useful when you want a folder to contain a particular kind of document and you want views in that folder to only display columns that are relevant to the document type that is contained in that folder.
  
By using the SharePoint Server object model, you can customize the **New** command for a folder content type so that when a user creates a new folder of that type, the folder is prepopulated with multiple files and documents based on templates that are stored on the server. This is useful, for example, for implementing a compound document type that requires multiple files to contribute to a single deliverable document. 
  
Document sets is a feature in SharePoint Server that lets you use Office to manage deliverables that span multiple documents. Document sets are special kinds of folders that are used to manage a single deliverable, or work product, which can include multiple documents in multiple locations. You create document sets by using extensible templates that are provided with SharePoint Server. You can also customize Document Set templates to represent the work products that are relevant to your organization. Document sets also include version control, which lets you capture the status of the complete document set at various points in its life cycle. For more information about document sets, see [Plan document sets in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ff603637(v=office.14)).
  
## Plan document content types
<a name="PlanDocContentTypes"> </a>

The first stage in planning document content types is to review each document type that is listed in your [Analyze document usage](https://go.microsoft.com/fwlink/p/?LinkId=165873) (https://go.microsoft.com/fwlink/p/?LinkId=165873) worksheet to determine whether an existing content type will work for that kind of document. Each document content type should inherit its settings directly from the core Document content type or from a content type that is descended from the Document content type. This ensures that the basic columns for your document types, such as Title and Created By, are present and that you can associate a template with the content type. If a core content type (such as Document) is sufficient, enter the content type name in the Content Type column of the "Analyze document usage" worksheet. 
  
> [!NOTE]
> Supported core content types do not include PDF files. 
  
For information about changing the core content types, download the white paper "[Guidance for editing pre-defined content types and site columns](https://go.microsoft.com/fwlink/p/?LinkId=260922)" (https://go.microsoft.com/fwlink/p/?LinkId=260922).
  
## Plan list content types
<a name="Lists"> </a>

The elements of a list content type include the columns of metadata that are associated with the content type and workflows that can run on items of that content type. Use a list content type to define a kind of list item that is unique to your solution. For example, in a customer call center solution, in which support professionals investigate and resolve customers' technical issues, a list content type could be used to standardize the data for each support incident and to track the incident by using a workflow.
  
## Plan workflows
<a name="bkmk_plan_workflows"> </a>

Workflows implement business processes on documents, web pages, forms, and list items in SharePoint Server. They can be associated with libraries, lists, or content types. 
  
In document management, use workflows to route documents from person to person so that they can each complete their document management tasks, such as reviewing documents, approving their publication, or managing their disposition. Also, use custom workflows to move documents from one site or library to another. For example, you can design a workflow to copy a document from one site to another when the document is scheduled to be archived.
  
SharePoint Server includes the Three-state workflow, which you can use to manage business processes that track the status of an item through three states or phases. SharePoint Server also includes the following workflows that address document management needs:
  
- **Collect Feedback** Sends a document for review. 
    
- **Approval** Sends a document for approval, often as a prerequisite to publishing it. 
    
- **Disposition** Manages document expiration and disposition. 
    
- **Collect Signatures** Routes a document for signatures. 
    
Associate a workflow with a content type when you want to make that workflow available when that content type is being used. For example, a purchase order content type could require approval by a manager before the transaction can be completed. To make sure that the Approval workflow is always available when a purchase order is initiated, create a Purchase Order content type and associate the Approval workflow with it. Then add the Purchase Order content type to any document libraries in which purchase orders will be stored.
  
To plan workflows for your document management solution, analyze each document content type that you plan to implement and identify the business processes that have to be available to run on content of that type. Then identify the workflows you will have to make available for that content.
  
The following is a sample table that analyzes workflows for a contract content type.
  
**Table: Workflows for a contract content type**

|**Contract process**|**Contract workflow**|
|:-----|:-----|
|Review drafts.  <br/> |Collect feedback  <br/> |
|Get approval from the manager and legal counsel.  <br/> |Approval  <br/> |
|Resolve open issues.  <br/> |Issue tracking  <br/> |
|Get signatures.  <br/> |Collect signatures  <br/> |
   

