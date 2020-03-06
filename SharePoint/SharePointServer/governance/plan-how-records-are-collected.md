---
title: "Plan ways to convert active documents to records in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/2/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: f3fae102-5b20-4c9f-9707-ab76c68be937
description: "Learn ways that users can turn active documents into records in the Records Center site in SharePoint Server."
---

# Plan ways to convert active documents to records in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
After you develop a file plan and design your records management solution in SharePoint Server, plan how active documents in your organization - electronic and hard copy - will become records. This article reviews techniques that you can use to declare active documents to be records and suggests one way to plan how items in your file plan will become records.
  
## Techniques for converting active documents to records in SharePoint Server
<a name="section1"> </a>

You can use the following techniques convert active documents to records:
  
- Manually declaring a document to be a record.
    
- Defining a policy that declares a document to be a record or sends a document to a Records Center site at a specified time.
    
- Creating a workflow that sends a document to a Records Center site.
    
- Using a custom solution that is based on the SharePoint object model.
    
### Creating records manually

If in-place records management is enabled for a document library, users can explicitly declare a document in the library to be a record by editing the document's compliance details. When the site collection administrator enables in-place records management, the site collection administrator specifies who should be able to declare and un-declare records, and whether users should be able to edit or delete documents after they become records.
  
If a connection to a Records Center site was created, users can manually send documents to the Records Center site by using the **Send to** command. When a farm administrator configures a connection to the Records Center site, this command becomes available on all active documents. Depending on how the connection is configured, documents can be either copied to the Records Center site, moved to the Records Center site, or moved to the Records Center site with a link to the document maintained. 
  
Although manually sending records to the Records Center site is not a practical large-scale solution, you can use it to supplement other methods of creating records.
  
### Defining a policy

A retention policy specifies actions to take on documents at certain points in time. Policy actions occur automatically. Users do not have to start the action.
  
Two policy actions relate specifically to managing records: transferring a document to another location, and declaring a document to be a record. If a connection to a Records Center site exists, you can create a policy that sends documents to a Records Center site. The policy also specifies whether to copy the document to the Records Center site, move it, or move it and leave a link in the document library. If in-place records management is enabled for the site, you can create a policy that declares a document to be a record. You can also use the SharePoint object model to create a custom action.
  
A retention policy can have multiple stages. For example, you could create a retention policy that deletes all earlier versions of a document one year after the document was last changed, and transfers the document to a Records Center site five years after the document was last changed.
  
If in-place records management is enabled for a site, the site can contain both active documents and records. In this case, you can specify different retention policies for active documents and records. For example, you could create a policy that declares an active document to be a record two years after the document was created, and create a second policy that deletes a record seven years after it was declared to be a record.
  
### Creating a workflow

When you use SharePoint Designer to create a workflow, you can add an action to send an item to a repository. By using this action, you can create workflows that send documents to a Records Center site. You can also include other actions in the workflow. For example, you could create a workflow that sends an email message to a document's author requesting approval, and then sends the document to a Records Center site. You could combine policies and workflows by creating a retention policy that runs the new workflow one year after a document is created.
  
You can also use the SharePoint object model to create a custom workflow that copies files to the Records Center site. A workflow that sends files to the Records Center site can be integrated into your document management system as part of a workflow that guides a document through its life cycle. For document types that have a predictable life cycle, such as expense reports, you could implement a workflow that guides the document through its various stages and, as a final step, sends a copy of the document to the Records Center site. The workflow could be triggered by creating a new document.
  
### Using a custom solution

You can develop custom solutions that use objects in the **Microsoft.Office.RecordsManagement.OfficialFileWSProxy** namespace to send content from other data sources to the Records Center site. For more information about how to implement custom solutions using the SharePoint Server object model, see the SharePoint Server [Software Development Kit](https://go.microsoft.com/fwlink/p/?LinkId=259788) (https://go.microsoft.com/fwlink/p/?LinkId=259788). 
  
## Completing your plan
<a name="section2"> </a>

After you develop the file plan and review the methods for moving content into the Records Center site, complete your file plan by determining how to send each kind of record to the Records Center site. The things to consider include the following:
  
- Is compliance enforced or voluntary?
    
- Can you depend on the cooperation of users in your organization to comply with records management processes? In general, avoid manual processes. However, where they are needed, create suitable training and monitoring to make sure that team compliance.
    
- Will content be stored on SharePoint Server document management servers?
    
- Are you maintaining physical content? Managing active physical content, such as hard copy or CD-ROM, and sending it to a records vault for retention (together with tracking the record in a Records Center site) requires unique planning not described in this topic. For example, if no electronic version of a paper document exists, you might have to track the item by using a list that has associated policies and workflows.
    
The following table shows how some records in a sample file plan will move to a Records Center site:
  
|**Documents**|**Description**|**Media**|**Source location**|**Becomes a record...**|
|:-----|:-----|:-----|:-----|:-----|
|Benefit plan  <br/> |Description of employee benefit plan.  <br/> |Web pages  <br/> |SharePoint Server document library  <br/> |Using a custom workflow associated with expiration policy  <br/> |
|Insurance plan  <br/> |Description of employee insurance plan.  <br/> |Print  <br/> |Physical document associated with list item in SharePoint Server  <br/> |By sending it to a physical vault and creating a list item in the Records Center site to track (using a barcode)  <br/> |
|Payroll timesheets  <br/> |Summaries of hours worked, overtime, and salaries paid.  <br/> |Electronic documents  <br/> |Payroll records server not based on SharePoint Server  <br/> |Using a custom program  <br/> |
|Product development files  <br/> |Specifications of products and associated documents.  <br/> |Electronic documents  <br/> |SharePoint Server document library  <br/> |Using custom workflow associated with expiration policy and manually by using **Send to** command  <br/> |
   

