---
title: "Identify users and analyze document usage in SharePoint Server"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 185da9e8-9ed1-4bf1-bfb5-2a5a874f2a19
description: "Learn how to collect information about document users to plan your SharePoint Server document management solution."
---

# Identify users and analyze document usage in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The first step to plan your document management solution is to identify users and analyze how documents are used. This article contains guidance to identify users and analyze document usage for your solution that is based on SharePoint Server.
  
## Identify users
<a name="section1"> </a>

To identify the stakeholders and participants in your document management solution, you can use a survey to collect information. For example, your survey might contain the following questions:
  
- Who in your organization creates documents?
    
- What kinds of documents do they create?
    
- What role does the user of the document have?
    
  - Who reviews documents?
    
  - Who edits documents?
    
  - Who uses documents?
    
  - Who approves the publication of documents?
    
  - Who designs websites used for hosting documents?
    
  - Who sets guidelines and policies for managing documents?
    
  - Who manages records in your organization?
    
  - Who deploys and maintains the servers on which documents are stored?
    
Identifying content stakeholders can help you make sure that your document management solution is comprehensive and that you design sites and document libraries that suit your enterprise's content needs and processes.
  
## Analyze document usage
<a name="section2"> </a>

After you identify your content stakeholders, collect information from them that will help you analyze how documents are used in your organization. This is an important part of the planning process because the analysis helps you determine the following:
  
- How document libraries should be structured.
    
- Which site templates to use.
    
- How many sites you will need.
    
- Which physical server topology you must have to implement your solution.
    
- Which information management policies to apply to the sites.
    
> [!NOTE]
> Information management policies are not available in SharePoint Foundation 2013. 
  
The information to collect includes the following:
  
- Document type, such as equity research note, employee performance review, internal memo, or product specification.
    
- The purpose of each document type, such as "gives customers recommendations about equities together with supporting data."
    
- The author of each document type (it is helpful to list the role of the author — such as "financial analyst or "product manager" — instead of individual names).
    
- The users of each document type, such as "customers" or "team members."
    
- The format of the document. If the document has to be converted from one format to another at any point in its life cycle, record that information.
    
- Other roles that apply to the document's life cycle, such as "technical reviewer" or "copy editor."
    
- Location of the document, such as "client computer," "web server," or "file server." Note that this question could have multiple answers, for example when a document is authored on a client computer and then published to a web server.
    
The following are examples of information that might be collected and recorded in the worksheet from two different organizations in an enterprise.
  
**Table: Example with research information**

|**Type**|**Purpose**|**Author**|**User role**|**Format**|**Other roles**|**Location**|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|Equity research note  <br/> |Gives premium customers of a financial service guidance on whether to buy or sell one or more stocks  <br/> |Financial analyst  <br/> |Customer  <br/> |DOCX (for authoring); PDF (for publishing)  <br/> |Reviewer (technical); reviewer (legal); approver; copy editor; site administrator  <br/> | Authoring site  <br/>  Testing site  <br/> |
   
 **Analysis** The separate authoring and publishing formats require a format conversion. The large number of reviewers requires one or more workflows (business processes implemented on the server). The two sites (authoring and testing) require mechanisms for moving the content from one site to another. 
  
**Table: Example with employee information**

|**Type**|**Purpose**|**Author**|**User role**|**Format**|**Other roles**|**Location**|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|Employee performance review  <br/> |Evaluates the performance of an employee — including self-evaluation and manager's evaluation  <br/> |Information worker; manager  <br/> |Managers; human resources specialists  <br/> |.DOCX  <br/> |Reviewer (human resources); reviewer (legal); approver (upper manager); records manager  <br/> | Client computer  <br/>  E-mail server (as attachment)  <br/>  Corporate web server  <br/>  Corporate records center  <br/> |
   
 **Analysis** Two authors and multiple reviewers require one or more workflows. The document is handled by many people, then is located in a corporate web server (presumably highly secured) and is managed in place or moved to a records center. The sensitive nature of this content requires Information Rights Management (IRM) on the desktops and servers, in addition to corporate policies and best practices (such as auditing) that protect the employee's privacy and the enterprise's legal standing. 
  
> [!NOTE]
> The Records Center is not available in SharePoint Foundation 2013. 
  
## Worksheets
<a name="worksheets"> </a>

Use the following worksheets to record the information discussed in this article:
  
- [Document management participants worksheet](https://go.microsoft.com/fwlink/p/?LinkId=165871) (https://go.microsoft.com/fwlink/p/?LinkId=165871) 
    
- [Analyze document usage worksheet](https://go.microsoft.com/fwlink/p/?LinkId=165873) (https://go.microsoft.com/fwlink/p/?LinkId=165873) 
    

