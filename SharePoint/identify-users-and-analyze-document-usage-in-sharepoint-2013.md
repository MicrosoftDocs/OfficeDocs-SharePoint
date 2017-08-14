---
title: Identify users and analyze document usage in SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: 185da9e8-9ed1-4bf1-bfb5-2a5a874f2a19
---


# Identify users and analyze document usage in SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-19* **Summary: ** Learn how to collect information about document users to plan your SharePoint Server 2013 document management solution.The first step to plan your document management solution is to identify users and analyze how documents are used. This article contains guidance to identify users and analyze document usage for your solution that is based on SharePoint Server 2013.Before reading this article, you should understand the document management planning process described in **Overview of document management in SharePoint 2013**.In this article:
-  [Identify users](#section1)
    
  
-  [Analyze document usage](#section2)
    
  
-  [Worksheets](#worksheets)
    
  

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
    
  

> [!NOTE:]

  
    
    

The information to collect includes the following:
- Document type, such as equity research note, employee performance review, internal memo, or product specification.
    
  
- The purpose of each document type, such as "gives customers recommendations about equities together with supporting data."
    
  
- The author of each document type (it is helpful to list the role of the author — such as "financial analyst or "product manager" — instead of individual names).
    
  
- The users of each document type, such as "customers" or "team members."
    
  
- The format of the document. If the document has to be converted from one format to another at any point in its life cycle, record that information.
    
  
- Other roles that apply to the document's life cycle, such as "technical reviewer" or "copy editor."
    
  
- Location of the document, such as "client computer," "web server," or "file server." Note that this question could have multiple answers, for example when a document is authored on a client computer and then published to a web server.
    
  
The following are examples of information that might be collected and recorded in the worksheet from two different organizations in an enterprise.
### Table: Example with research information

TypePurposeAuthorUser roleFormatOther rolesLocationEquity research note  <br/> Gives premium customers of a financial service guidance on whether to buy or sell one or more stocks  <br/> Financial analyst  <br/> Customer  <br/> DOCX (for authoring); PDF (for publishing)  <br/> Reviewer (technical); reviewer (legal); approver; copy editor; site administrator  <br/>  Authoring site <br/>  Testing site <br/> **Analysis**    The separate authoring and publishing formats require a format conversion. The large number of reviewers requires one or more workflows (business processes implemented on the server). The two sites (authoring and testing) require mechanisms for moving the content from one site to another.
### Table: Example with employee information

TypePurposeAuthorUser roleFormatOther rolesLocationEmployee performance review  <br/> Evaluates the performance of an employee — including self-evaluation and manager's evaluation  <br/> Information worker; manager  <br/> Managers; human resources specialists  <br/> .DOCX  <br/> Reviewer (human resources); reviewer (legal); approver (upper manager); records manager  <br/>  Client computer <br/>  E-mail server (as attachment) <br/>  Corporate web server <br/>  Corporate records center <br/> **Analysis**    Two authors and multiple reviewers require one or more workflows. The document is handled by many people, then is located in a corporate web server (presumably highly secured) and is managed in place or moved to a records center. The sensitive nature of this content requires Information Rights Management (IRM) on the desktops and servers, in addition to corporate policies and best practices (such as auditing) that protect the employee's privacy and the enterprise's legal standing.
> [!NOTE:]

  
    
    


## Worksheets
<a name="worksheets"> </a>

Use the following worksheets to record the information discussed in this article:
-  [Document management participants worksheet](https://go.microsoft.com/fwlink/p/?LinkId=165871) (https://go.microsoft.com/fwlink/p/?LinkId=165871)
    
  
-  [Analyze document usage worksheet](https://go.microsoft.com/fwlink/p/?LinkId=165873) (https://go.microsoft.com/fwlink/p/?LinkId=165873)
    
  

# See also

#### 

 **Plan document libraries in SharePoint 2013**
  
    
    
 [SharePoint 2013 for IT pros](https://technet.microsoft.com/en-us/sharepoint/fp142366)
  
    
    

  
    
    

