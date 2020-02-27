---
title: "Plan Visio Services security in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6d871772-b90b-4e48-9122-a6d9a1122b8d
description: "Learn about security considerations for data-connected diagrams rendered in Visio Services."
---

# Plan Visio Services security in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In addition to the security requirements to deploy SharePoint Server, you should also review security considerations for a deployment that includes Visio Services. Visio Services enables you to render Visio diagrams in a browser window. These diagrams can be connected to external data, and diagram elements can be updated based on that data. Security is an important component for enabling these data-rendering scenarios. Visio Services gives you a significant level of fine-grained control for the processing and displaying of Visio diagrams and what data sources they can connect to.
  
## Store Visio diagrams in SharePoint document libraries

Visio diagrams must be stored in SharePoint document libraries to be opened by Visio Services. SharePoint Server maintains an access control list (ACL) for the files that are contained in the document library. By setting the library rules correctly you can limit access to a particular diagram.
  
## Visio diagrams that are connected to data

The Visio Graphics Service can connect to data sources. These include SharePoint lists (including external lists), databases such as SQL Server, and custom data sources. You can control access to specific data sources by explicitly defining the data providers that are trusted and configuring them in the list of trusted data providers.
  
> [!NOTE]
> Visio Services accesses external data sources by using a delegated Windows identity. Consequently, external data sources must reside within the same domain as the SharePoint Server farm or Visio Services must be configured to use the Secure Store Service. If Secure Store is not used and external data sources do not reside within the same domain, authentication to the external data sources will fail. 
  
When Visio Services loads a data connected diagram, the service checks the connection information that is stored in the diagram to determine whether the specified data provider is a trusted data provider. If the provider is specified on the Visio Services trusted data provider list, a connection is tried; otherwise, the connection request is ignored.
  
Once an administrator has configured Visio Services to enable connections to a particular data source, there are additional security configurations that must be made, depending on the kind of the data source. The following data sources are supported by Visio Services:
  
- SharePoint lists, including external lists enabled through Microsoft Business Connectivity Services
    
- Databases such as SQL Server databases
    
- Custom Data Providers
    
### Visio diagrams that are connected to SharePoint lists

Visio diagrams can be connected to SharePoint lists on the same farm that the diagram is hosted on. The user viewing the diagram must have access to both the diagram and the SharePoint list that the diagram is connected to. These permissions and credentials are managed by SharePoint Server. 
  
Visio diagrams can also be connected to external lists by using Microsoft Business Connectivity Services. External lists exposed through a Microsoft Business Connectivity Services External Content Type can be connected to a Visio diagram in Visio and the data can be refreshed through Visio Services. In order for a user to access data in an External List, the user must have permissions to access the External Content Type and permissions to access the external data source.
  
### Visio diagrams that are connected to SQL Server databases

When a Visio diagram is connected to a SQL Server database, Visio Services uses additional security configuration options to establish a connection between the Visio Graphics Service and the database. 
  
The authentication methods supported by Visio Services are as follows:
  
- **Integrated Windows authentication** In this security model the Visio Graphics Service uses the diagram viewer's identity to authenticate with the database. Integrated Windows authentication with Kerberos constrained delegation is more helpful for increasing security than the other authentication methods shown in this list. This configuration requires constrained Kerberos delegation to be enabled between the application server that is running the Visio Graphics Service and the database server. The database itself might require additional configuration to enable Kerberos-based authentication. 
    
- **Secure Store Service** In this security model the Visio Graphics Service uses the Secure Store Service to map the user's credentials to a different credential that has access to the database. Secure Store supports individual and group mappings for both Integrated Windows authentication and other forms of authentication such as SQL Server Authentication. This gives administrators more flexibility in defining one-to-one, many-to-one, or many-to-many relationships. 
    
- **Unattended Service Account** For ease of configuration the Visio Graphics Service provides a special configuration where an administrator can create a unique mapping associating all users to a single account by using a Secure Store target application. This mapped account, known as the unattended service account, must be a low-privilege Windows domain account that is given access to databases. The Visio Graphics Service impersonates this account when it connects to the database if no other authentication method is specified. Note that this approach does not enable personalized queries against a database and does not provide auditing of database calls. This authentication method is the default authentication method that is used when you connect to SQL Server databases: if no ODC file is used in the Visio diagram that specifies a different authentication method, then Visio Services uses the credentials specified by the unattended account to connect to the SQL Server database. 
    
In a larger server farm it is likely that Visio diagrams will use a mix of the authentication methods described here. It is important to be aware of the following things:
  
- Visio Services supports usage of both Secure Store and the unattended service account in the same farm. In diagrams that are connected to SQL Server data but do not use ODC files, the unattended account is required and always used.
    
- If Integrated Windows authentication is selected, and authentication to the data source fails, Visio Services will not attempt to render the diagram using the unattended service account.
    
- Integrated Windows authentication can be used together with Secure Store by configuring diagrams to use a Secure Store target application for those diagrams that require specific credentials.
    
## See also

#### Other Resources

[Secure Store for Business Intelligence service applications](/SharePoint/administration/secure-store-for-business-intelligence-service-applications)

