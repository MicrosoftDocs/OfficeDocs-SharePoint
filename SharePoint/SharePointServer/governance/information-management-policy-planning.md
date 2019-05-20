---
title: "Plan for information management policy in SharePoint Server"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 4de4007d-a45f-419d-9512-824421e14380
description: "Learn how to use information management policies in SharePoint Server."
---

# Plan for information management policy in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
An information management policy is a set of rules for a type of content. Each rule in a policy is a policy feature. For example, an information management policy feature could specify how long a type of content should be retained, or it could provide document auditing. Information management policies enable you to control who can access your organizational information, what they can do with it, and how long the information should be retained.
  
## Information management policies and policy features
<a name="section1"> </a>

> [!NOTE]
> In this article, the term policy refers to information management policy unless otherwise specified. 
  
Policies can be implemented to help an organization comply with legally mandated requirements, such as the need to retain records. For example, a Human Resources policy, used in an organization to ensure that employee records are handled in compliance with legally recommended guidelines, could include the following policy features:
  
- Auditing, to record the editing and viewing history of each employee-related document.
    
- Retention, to ensure that work-in-progress content is not kept for an unnecessarily long time.
    
- Print restrictions, to ensure that sensitive employee-related documents are printed only on secure printers. Note that this is an example of a custom policy feature that must be implemented by using the SharePoint Server object model or obtained from a third-party software vendor.
    
Policy features are implemented as programs that run on SharePoint Server. They can be enabled and configured by a server administrator and, when they are enabled, they can be used by site administrators to define policies. SharePoint Server includes policy features to help you manage your content. By using the SharePoint Server object model, you can design and install custom policy features that meet unique enterprise needs.
  
When your organization uses Office client applications together with SharePoint Server, policies are enforced both on the server and in the client applications. This is done transparently; policy features that apply to a document are described in a policy statement that is associated with the document, and policy-aware applications prevent users from doing tasks that violate the document's policy.
  
To implement a policy, associate it with content types, libraries, or lists in sites.
  
You can associate a policy with a library, list, or content type in the following ways:
  
- **Associate policy features with a Site Collection policy and then associate that policy with a content type or with a list or library.** The top-level site of a site collection includes a Site Collection Policies gallery where administrators of the top-level site can create new policies. After creating a Site Collection policy, you can export it so that administrators of other site collections can import it into their Site Collection Policies galleries. This lets you standardize policies across your organization. 
    
    When a Site Collection policy is associated with a content type and that content type is associated with a list or library, the owner of the list or library cannot modify the Site Collection policy in the list or library. This ensures that policies that are assigned to a content type are enforced at each level of the site hierarchy.
    
- **Associate a set of policy features directly with a content type, and then add that content type to one or more lists or libraries.** To ensure that a policy that is created by using this method will be used in the whole site collection, associate it with a content type in the Site Content Type gallery of the top-level site collection. Then every item of that content type in the site collection, and every item of a content type that inherits from the original content type, will have the policy. When you use this method of associating a policy with a content type, it is harder to reuse the policy in other site collections, because policies created by using this method cannot be exported. 
    
    > [!NOTE]
    > To more tightly control which policies are being used in a site collection, site collection administrators can disable the ability to set policy features directly on a content type. When setting policy features on a content type is restricted, content type designers can only associate policies from the Site Collection Policies gallery with content types. 
  
- **Associate a set of policy features directly with a list or library.** You can only use this method if the list or library does not support multiple content types. This method of creating a policy is only useful for a narrowly defined policy that applies to a single list or library. 
    
    > [!NOTE]
    > To more tightly control which policies are being used in a site collection, site collection administrators can disable the ability to set policy features directly on a library. When setting policy features on a library is restricted, content type designers can only associate policies from the Site Collection Policies gallery with libraries. 
  
## Information management policy integration with Office system applications
<a name="section3"> </a>

SharePoint Server information management policies are exposed in Office client applications. When you configure an information management policy on the server, you can write a policy statement that informs information workers about the policies that are enforced on documents. For example, the policy statement might indicate that a document will be deleted after a certain time or that it contains sensitive information that should not be communicated outside the company. The statement might even provide a contact name if the information worker needs more information about the policy.
  
Custom policy features can be integrated in Office client applications. However, you must implement policy-specific behaviors that you want to be available from Office client applications, and you must give users a way to install these behaviors on their client computers via mechanisms such as add-ins to make them available from Office client applications. For example, if you implement a custom policy feature that restricts the printers that can be used to print a content type, you must provide a custom add-in for Microsoft Office client applications to enforce the restriction from these applications.
  
## Policy features available in SharePoint Server
<a name="section4"> </a>

This section describes the policy features that are included in SharePoint Server.
  
- **Retention** The Retention policy feature lets you define retention stages, with an action that happens at the end of each stage. For example, you could define a two-stage retention policy on all documents in a specific library that deletes all previous versions of the document one year after the document is created, and declares the document to be a record five years after the document is created. 
    
    The actions that can occur at the end of a stage include the following:
    
  - Moving the item to the Recycle Bin
    
  - Permanently deleting the item
    
  - Transferring the item to another location
    
  - Starting a workflow
    
  - Skipping to the next stage
    
  - Declaring the item to be a record
    
  - Deleting all previous drafts of the item
    
  - Deleting all previous versions of the item
    
- **Auditing** The Auditing policy feature logs events and operations that are performed on documents and list items. You can configure Auditing to log events such as the following: 
    
  - Editing a document or item
    
  - Viewing a document or item
    
  - Checking a document in or out
    
  - Changing the permissions for a document or item
    
  - Deleting a document or item
    
- **Labeling** The Labeling policy feature specifies a label to associate with a type of document or list item. Labels are searchable text areas that SharePoint Server generates based on properties and formatting that you specify. For example, in a law firm, a document related to a legal matter could include a label that contains the clients' names, the case number, and the attorney assigned to the matter. Labels are especially useful in printed versions of documents as a way to display document properties in printed copy. Along with using labels for documents, you can associate a label with a list item and include that label in views of the list. 
    
    > [!NOTE]
    > The label policy feature has been deprecated and should not be used in SharePoint Server 2013 or SharePoint Server 2016. 
  
- **Barcode** The Barcode policy feature enables you to track physical copies of a document by creating a unique identifier value for a document and inserting a bar code image of that value in the document. By default, bar codes are compliant with the common Code 39 standard (ANSI/AIM BC1-1995, Code 39), and you can plug in other bar code providers by using the policies object model. 
    
## Plan document policies
<a name="section5"> </a>

When you plan your solution's policies, first determine organization-wide policy needs, and then design Site Collection policies to meet those needs and distribute those policies for inclusion in the Site Collection Policy galleries of all relevant site collections. This might require planning custom policy features. Note that, if your policy requires custom policy features and resources, those features and resources must be installed and enabled on all server farms on which your solution is used.
  
A typical example of an organization-wide policy is one that is designed to promote best practices in auditing and retaining product specifications across the divisions of an organization. A single Site Collection policy is designed to be applied to all product specifications so that they are consistently audited and retained. After the Site Collection policy is designed and tested, it is exported and then imported to Site Collection Policy galleries of other site collections in which product specifications are stored. It is then associated with all product specification content types in the various site collections to impose the policy on all product specifications.
  

