---
title: "Overview of Business Connectivity Services in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 02f10b70-d634-41ae-914e-5de337c8b408
description: "Understand Microsoft Business Connectivity Services and how it brings external data into SharePoint Server and Office."
---

# Overview of Business Connectivity Services in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article introduces you to Microsoft Business Connectivity Services. After you read this article you'll understand:
  
- What Business Connectivity Services is.
    
- The business problems that Business Connectivity Services solves for and when to use it.
    
- How Business Connectivity Services works.
    
- What the three basic Business Connectivity Services solutions are and what they look like.
    
This article is your starting place for using Business Connectivity Services to create data integration solutions in SharePoint Server and Office 2016. You have to understand the concepts in this article before you can move on to planning, developing, and installing Business Connectivity Services data integration solutions. The examples in this article are used throughout the remainder of the Business Connectivity Services documentation.
  
    
## What is Business Connectivity Services?
<a name="section1"> </a>

With Business Connectivity Services, you can use SharePoint Server and Office clients as interfaces to data that doesn't live in SharePoint Server itself. Business Connectivity Services can connect to data that is available through a database, a web service, or data that is published as an OData source or many other types of external data. Business Connectivity Services does this through out-of-the box or custom connectors. The connectors, as the name implies, are the communication bridge between SharePoint Server and the external system that hosts the external data.
  
Using Business Connectivity Services, you can perform different operations on the data such as Create, Read, Update, Delete, and Query (CRUDQ). Depending on the operations that are enabled, the changes made to the data in SharePoint Server or Office can be automatically synchronized back to the external data source. You can also take the data offline to work on it, and search the external data by using SharePoint Search.
  
SharePoint Server has several ways to present the external data. Probably the most common way is to present the data in an external list. External lists look and feel like regular SharePoint lists, except that they can only display external data. If you want to integrate external data alongside other data in a list or library, you would use an external data column. An external data column is a column type that you can create and add to a SharePoint list just as you would add a **Person or Group** or **Date and Time** column, except that it is displays external data. SharePoint Server includes Business Data Web Parts for presenting and interacting with external data and apps for SharePoint, which can also use external data. 
  
### Examples of Business Connectivity Services solutions

You can use Business Connectivity Services to build many types of data integration solutions. Here are some examples.
  
- **Help desk** Enterprise help desks that provide internal technical support can use Business Connectivity Services. For example, the support tickets and the knowledge base that the help desk technicians use are stored in two separate databases, both of which are not in SharePoint Server. By using Business Connectivity Services, the company can retrieve data from both sources, filter and sort it, and then present it for interaction in an external list in SharePoint Server. What's more, with the correctly configured permissions, the help desk technicians can manipulate the data, while users with support questions only have permissions to search for their open support tickets to check the status. Open support tickets can be routed through predefined steps by workflows. 
    
- **Sales dashboard** A sales dashboard application helps sales associates in an organization quickly find the information that they need and enter new data. Sales orders and customer information are managed in an external application, such as Salesforce.com, and integrated into the solution by using Business Connectivity Services. Depending on their roles, team members can view sales analytics information, individual team members' sales performance data, sales leads, and a customer's contact information and orders. Sales professionals can view their daily calendars, view tasks assigned to them by their managers, collaborate with team members, and read industry news from a web browser. By using Word 2016, managers can author monthly status reports that include data from the external systems. 
    
### What distinguishes Business Connectivity Services from similar solutions?

Business Connectivity Services is just one way to integrate external data into SharePoint Server and Office 2016 client-based business data solutions. There are custom Java script-based solutions, custom data connections, and custom-coded Web Parts. In addition, apps for Office are also available. apps for Office can access external data directly or use the Business Connectivity Services APIs and the centralized Business Connectivity Services infrastructure. While each of these has its purpose, Business Connectivity Services offers several advantages for enterprise-scale data integration. 
  
 **Centralized infrastructure** Business Connectivity Services connects to external data using a definition called an external content type. External content types are centrally stored and secured and can be shared by many Business Connectivity Services solutions. External content types allow you to deeply integrate external data into SharePoint Server and Office 2016 solutions. The Business Connectivity Services infrastructure is very similar in server and client environments. Because of this, the developer can create an external content type and with minimal administrative intervention and that external content type can be used in both client and server solutions.
  
 **Managed authentication** Another advantage of the centralized infrastructure in Business Connectivity Services is that it handles the security transactions with the external system. When the developer creates the external content type, information about which authentication protocol and credentials to use is included. Business Connectivity Services passes this configuration information to the appropriate connector and the connection is made. This means that users don't have to provide any additional credentials when they want to work with the external data from SharePoint Server. On the client-side, users must know the credentials that the external system requires and provide the credentials the first time that they access the external data. The credentials are then stored on the Windows client. 
  
 **Search external content** Because the Business Connectivity Services infrastructure is built into SharePoint Server, it takes advantage of common SharePoint Server features such as Search. The external data is defined as a content source that SharePoint Server crawls and indexes. The search results from external data are security trimmed — meaning the user only sees what they have permissions to see — just as all other search results in SharePoint Server are. 
  
## How does Business Connectivity Services work?
<a name="section2"> </a>

Business Connectivity Services has server-side components and client-side components. Business Connectivity Services solutions can include one or the other or both in a single solution. These two component stacks work completely independently of one another. However, they are structured very similarly. They both use the same configuration data. For the server-side, the configuration data is stored in an external content type. External content types are stored in the Business Data Connectivity (BDC) Metadata Store database. For the client-side, the configuration data is stored in a BDC model on the client in the BDC client-side cache. The BDC model is just a version of the external content type that is exported to an XML file. The XML file is imported into the Office client. The server component stack and the client component stack can access the same external content sources. The two stacks are distinguished by the user interfaces, where and how the data that define the external connection and external system are stored, and where the services run.
  
### Server-side solutions

In Business Connectivity Services server-side solutions, users interact only with external data in a browser on a SharePoint site. This can be on any type of SharePoint site that supports external lists, external data columns, external Web Parts, or apps for SharePoint. SharePoint Enterprise Search of external data is supported in the browser as well.
  
For Business Connectivity Services to connect to an external data source and interact with the data there, that external system must be defined in an external content type in a way that Business Connectivity Services understands. An external content type contains the name of the external system and what kind of data source it is, what type of authentication to use for connections, where it can connect to, which operations can be performed, and, optionally, any filters and sorting instructions to be used so that only the desired data is returned and that the data is in the correct order.
  
### Client-side solutions

In the client-side version of Business Connectivity Services solutions, the Office applications interact with external data. A client-side solution can run independently of SharePoint. Not all of the Office applications interact with external data and some of them only do so in a read-only manner. The following table provides details on which operations are supported, how the applications can access the data, and how the connection is made. 
  
**Table: Applications and operations supported in Business Connectivity Services**

|**Application**|**Supported operations**|**Access external data online or offline**|**ClickOnce or import BDC model**|
|:-----|:-----|:-----|:-----|
|Word  <br/> |Read only  <br/> |Online  <br/> |Import BDC model  <br/> |
|Access  <br/> |CRUDQ  <br/> |Online  <br/> |Import BDC model  <br/> |
|Visio  <br/> |Read only  <br/> |Online and offline  <br/> |Import BDC model  <br/> |
|InfoPath  <br/> |CRUDQ  <br/> |Online and offline  <br/> |Import BDC model  <br/> |
|Excel  <br/> |CRUDQ  <br/> |Online  <br/> |Import BDC model  <br/> |
   

