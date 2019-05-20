---
title: "Plan a Business Connectivity Services solution in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 45e8f120-3d0c-4b5f-bf5f-0bc4e3c679d7
description: "Create a plan for your Microsoft Business Connectivity Services solution in SharePoint Server."
---

# Plan a Business Connectivity Services solution in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Microsoft Business Connectivity Services solutions integrate external data deeply into SharePoint Server and Office. Each Business Connectivity Services solution is custom-built using Visual Studio. There are no out-of-the-box Business Connectivity Services configurations or templates that you can use.
  
This article takes you through five questions that you must answer before you can design your Business Connectivity Services solution. Be sure to collect all this information and communicate it to all the key stakeholders to review and approve. When you do this, you will help ensure that everyone involved has the same understanding of the needs of the project and how the solution will work.
  
    
## Where is the data?
<a name="section1"> </a>

Your first step in planning your Business Connectivity Services solution is to understand where the external data that you want is. You need to understand this from three perspectives.
  
You will need to know who has daily administrative responsibility over the external data source. This is the group that you will need to work with to help set up connectivity to the external data. They will be able to tell you how the data is made available for external consumption, how it is secured, and so on. You might need them to create credentials in the external system for you to use. Be prepared to answer their questions on the impact of your Business Connectivity Services solution on their data and their external system. 
  
### Network considerations

You also need to consider where the external data source is in relation to the network that Business Connectivity Services and your users will be on. To help you figure this out, draw a diagram of the three components on your network and see where they lie. For example, you can see whether they are all on your internal network and inside your firewall. Or, you could see that the Business Connectivity Services infrastructure and the external data source are separated by a firewall or boundary network and that they are on completely separate networks. Here are some basic rules that you can use to guide your design:
  
- If the external data source is outside of your network, such as on the Internet, Business Connectivity Services will need to communicate with the external data source through your corporate firewall and you need to plan for that traffic.
    
- Look at where the users will be accessing the Business Connectivity Services solution from. Be sure to consider if the data communications between the client and the Business Connectivity Services solution need to be encrypted and whether the underlying network infrastructure can support the added load. Also, make sure that the browsers and Office clients support the functionality that the solution provides.
    
## How is the data surfaced?
<a name="section2"> </a>

Business Connectivity Services solutions can connect to an external data source through OData, SQL Server, Windows Communication Foundation (WCF) service, and .NET Assemblies. You need to know (and you can find this out from the external system administrators) how the data is surfaced for external consumption. How the external data is surfaced determines what development tools you will use to create the external content type. The following table shows you which tools to use based on the external data source.
  
## How is the data secured?
<a name="section3"> </a>

Business Connectivity Services handles all authentications for communications between itself and the external system. Basically, Business Connectivity Services presents the external system with information that allows the external system to authenticate (determine whether you are who you say you are) the request and then authorize access to data in the external system. Business Connectivity Services supports many types of authentication.
  
For your Business Connectivity Services solution design, you have to know what authentication mechanism the external system requires. This way, you will know how to configure Business Connectivity Services so that it presents the authentication information in the manner that the external system requires. Business Connectivity Services supports three authentication models:
  
- **Credentials-based authentication** In credentials-based authentication models, credentials are passed from Business Connectivity Services to the external system. Credentials are a combination of a user name and some form of password. Business Connectivity Services has a number of ways of doing this, including passing the credentials of the user who is logged on, passing the credentials of the service that is making the request, or mapping the credentials of the user who is logged on to a different set of credentials that the external system recognizes. 
    
- **Claims-based authentication** In some authentication scenarios, the external system will not accept credentials directly from Business Connectivity Services. However, the external system will accept them from a third-party authentication service that it trusts. The third-party authentication service (a security token provider) accepts a grouping of information (known as assertions) about the requestor. The whole grouping is known as a claim, and a claim can contain more information about the requestor than just the user name and password. For example, a claim can contain metadata about the requestor, such as the requestor's email address or the security groups to which the requestor belongs. The third-party authentication service performs the authentication of the requestor based on the assertions in the claim and creates a security token for the requestor to use. The requestor (Business Connectivity Services) then presents the security token to the external system, and the external system looks to see what data the requestor has been authorized to access. 
    
- **Custom authentication** If the external system that you are working with does not support credentials-based or claims-based authentication, then you will have to develop, test, and implement a custom solution that takes the credentials that Business Connectivity Services can produce and translates them into a format that the external system will accept. You can implement a custom authentication solution for OData data sources that are secured either by OAuth or a custom ASP.NET HTTP module and are on premises. 
    
## How will the data be consumed?
<a name="section4"> </a>

As part of your requirement gathering, you need to find out from your business stakeholders what they need the solution to do and how they need users to interact with it. They might need the users to interact with the data in SharePoint Server, via external lists, and external Web Parts and in Office 2016 clients. Or, they might need the solution to surface data through an apps for Office and SharePoint application in SharePoint Online or an on-premises SharePoint Server installation. For more information about apps for Office and SharePoint, see [(OLD) Overview of apps for SharePoint 2016](/SharePoint/administration/plan-for-apps-for-sharepoint). Or, the solution might require some other combination of browser, client, and application access to the external data. 
  
How users access the data affects how you will scope the external content type that Business Connectivity Services uses to access the external data. If your Business Connectivity Services solution requires an apps for Office and SharePoint application, then the external content type must be scoped to that application. If your Business Connectivity Services solution will not use apps for Office and SharePoint to access external data, then the external content type must be scoped to the Business Data Connectivity service application.
  
 **Business Connectivity Services-scoped external content types** are stored centrally in the BDC Metadata Store and a farm administrator manages security on them. You can share these external content types with multiple Business Connectivity Services web applications. 
  
 **The apps for Office and SharePoint-scoped external content types** are stored as an XML file in the app for Office and SharePoint application itself. They cannot be used by any other apps for Office and SharePoint applications. 
  
 **Connection settings objects** can only be used with OData data sources. They contain connection information, such as a service address for the service that surfaces the external data, the type of authentication to use, the Internet-facing URL, and the names of any required certificates. Connection settings objects are separate objects from an external content type. When a Business Connectivity Services solution needs to connect to an external system, it uses the information in a connection settings object. You would typically choose to define the connection information separately from the external content type when the external content type developer doesn't know, or doesn't have access to, the necessary connection information when the external content type is developed. Both app-scoped external content types and service-scoped external content types can use connection settings objects. Connection settings objects can be used by multiple Business Connectivity Services solutions. Each solution must be granted permissions to use a connection settings object. 
  
## How will you assign permissions to the solution?
<a name="section5"> </a>

In every Business Connectivity Services solution, you must plan who will have which permissions on which objects. This is how you both restrict and grant access to the solution to the appropriate users in the appropriate way. You will have to work with the external system administrator and the SharePoint Server farm administrators, site collection administrators, and site administrators to configure permissions. At the most fundamental level however, here is what you must consider during your planning.
  
There are three fundamental roles that are involved with every Business Connectivity Services solution:
  
- **Administrative roles** These roles are responsible for managing permissions on the external system, creating and managing the Business Data Connectivity service application, importing Business Data Connectivity (BDC) models into the BDC Metadata Store, and managing permissions on the BDC Metadata Store and all the objects in it. If apps for SharePoint are using Business Connectivity Services, then the SharePoint Server farm administrators will also be involved with publishing the application and creating and managing connection objects. Generally, these duties are performed by people who are SharePoint Server farm administrators, people who are administrators of the external system, and anyone who has delegated administrative rights. 
    
- **Developer or designer roles** These roles are responsible for creating the external content types, the BDC models, and the apps for SharePoint that use Business Connectivity Services. They are the ones who are primarily responsible for understanding all the business needs for the solution. 
    
- **User roles** People in these roles consume and manipulate the external data in the Business Connectivity Services solution. There can be multiple user roles in your solution, each with different levels of permissions. For example, in a support-ticketing system scenario that uses Business Connectivity Services to integrate external information into the solution, the Tier I Help Desk technicians might be granted only the ability to read and start workflows on a ticket, while Tier II and Tier III technicians have the ability to update tickets. 
    
There are also four main aspects to every Business Connectivity Services solution for which you will manage permissions:
  
- **External system** Every external system will have a method for performing authentication and authorization. (For more information, see [How is the data secured?](plan-a-business-connectivity-services-solution.md#section3) earlier in this article.) You need to work with the external system administrator to identify how to grant access to the solution users according to the principle of least privileges. In general, you will map a group of users from the Business Connectivity Services side to a single account on the external system side and use the single external system account to restrict access. Another way is to do a 1:1 mapping between individual accounts on each system. In either case, unless the external system can directly accept the credentials with which the user authenticates to SharePoint Server, you will need to use the [Secure Store Service](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)). For more in-depth information about the authentication models that Business Connectivity Services supports, see [Business Connectivity Services security overview (SharePoint 2010)](https://go.microsoft.com/fwlink/p/?LinkId=254927).
    
- **Business Connectivity Services central infrastructure** In Central Administration, you manage the assignment of permissions to the BDC Metadata Store. In the BDC Metadata Store, you manage BDC models, external systems, and external content types. You must assign execute permissions on an external content type to all users who will be using the Business Connectivity Services solution. The following tables provide a detailed mapping of abilities, permissions, and objects. 
    
    **The BDC Metadata Store** This SQL Server database that stores the model definitions, external content types, and external system definitions. 
    
   **Table: Mapping permissions on the BDC Metadata Store**

|**To allow a user or group to…**|**Give them the following permissions…**|**On…**|
|:-----|:-----|:-----|
|Set permissions on any object contained in the BDC Metadata Store via propagation  <br/> |SetPermissions  <br/> |The BDC Metadata Store  <br/> |
   
    **The model** A model is a XML file that contains sets of descriptions of one or more external content types, the related external systems, and information that is specific to the environment, such as authentication properties. 
    
   **Table: Mapping permissions on the model**

|**To allow a user or group to…**|**Give them the following permissions…**|**On…**|
|:-----|:-----|:-----|
|Create new models  <br/> |Edit  <br/> |The BDC Metadata Store  <br/> |
|Edit a model  <br/> |Edit  <br/> |The model  <br/> |
|Set permissions on a model  <br/> |SetPermissions  <br/> |The model  <br/> |
|Import a model  <br/> |Edit  <br/> |The BDC Metadata Store  <br/> |
|Export a model  <br/> |Edit  <br/> |The model and all external systems in the model  <br/> |
   
    **The external system in the BDC Metadata Store** An external system is the metadata definition of a supported source of data that can be modeled, such as a database, web service, or .NET connectivity assembly. 
    
   **Table: Mapping permissions on the external system in the BDC Metadata Store**

|**To allow a user or group to…**|**Give them the following permissions…**|**On…**|
|:-----|:-----|:-----|
|Create new external systems  <br/> |Edit  <br/> |The BDC Metadata Store  <br/> |
|Edit an external system  <br/> |Edit  <br/> |The external system object  <br/> |
|Set permissions on the external system  <br/> |SetPermissions  <br/> |The external system object  <br/> |
   
    **External content type** An external content type is a reusable collection of metadata that defines a set of data from one or more external systems, the operations available on that data, and connectivity information related to that data. 
    
   **Table: Mapping permissions on the external content type**

|**To allow a user or group to …**|**Give them the following permissions …**|**On …**|
|:-----|:-----|:-----|
|Create new external content types  <br/> |Edit  <br/> |The external system  <br/> |
|Execute operations on an external content type  <br/> |Execute  <br/> |The external content type (method instances of the operation)  <br/> |
|Create lists of the external content type  <br/> |Selectable in clients  <br/> |The external content type  <br/> |
|Set permissions on the external content type  <br/> |SetPermissions  <br/> |The external content type  <br/> |
   
    **The method** A Business Data Connectivity method is an XML definition of how Business Connectivity Services can interact with an external data source. 
    
   **Table: Mapping permissions on the method**

|**To allow a user or group to …**|**Give them the following permissions …**|**On …**|
|:-----|:-----|:-----|
|Edit a method  <br/> |Edit  <br/> |The method  <br/> |
|Set permissions on a method  <br/> |SetPermissions  <br/> |The method  <br/> |
   
    **The method instance** A method instance describes, for a particular method, how to use a method by using a specific set of default values. 
    
   **Table: Mapping permissions on the method instance**

|**To allow a user or group to…**|**Give them the following permissions…**|**On…**|
|:-----|:-----|:-----|
|Edit a method instance  <br/> |Edit  <br/> |The method instance  <br/> |
|Execute a method instance  <br/> |Execute  <br/> |The method instance  <br/> |
|Set permissions on a method instance  <br/> |SetPermissions  <br/> |The method instance  <br/> |
   
- **The development environment** When you are developing a Business Connectivity Services solution, including the external content type, and any apps for SharePoint and connection settings objects, it is a best practice to use a development environment that is separate from your production environment. In the development environment, you can grant higher levels of permissions to the developers than you would usually do in your production environment. 
    
- **The user environment** All external data will be accessed through external lists, external data columns, Business Data Web Parts, apps for SharePoint, or Office. For apps for SharePoint, you can choose to let the app for Office and SharePoint enforce permissions. In this case, if the users can access the app for Office and SharePoint, then they can access all the external data that is surfaced in the app for Office and SharePoint. You will have to work with site and site collection administrators to plan and implement permissions to the external data in your solution. 
    
## See also
<a name="section5"> </a>

#### Concepts

[Overview of Business Connectivity Services in SharePoint Server](business-connectivity-services-overview.md)

