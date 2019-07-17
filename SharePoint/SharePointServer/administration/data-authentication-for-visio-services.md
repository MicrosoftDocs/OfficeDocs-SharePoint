---
title: "Data authentication for Visio Services in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 918a570e-ce86-4ff7-857f-d08dbb35d08d
description: "Visio Services supports connections with Excel workbooks, SharePoint lists, SQL Server databases, and OLE DB and ODBC data sources."
---

# Data authentication for Visio Services in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Data sources are categorized as internal or external as follows: 
  
- Internal: Data hosted within the SharePoint farm, such as an Excel workbook or a SharePoint list.
    
- External: SQL Server data, or an OLE DB or ODBC data source.
    
Retrieving data from a data source requires a user to be authenticated by the data source and then authorized to access the data that it contains. In the case of a diagram, Visio Services authenticates to the data source on behalf of the user who is viewing it in order to refresh the data to which the diagram is connected.
  
Which authentication method Visio Services can use to retrieve data depends on the type of the underlying data source, as outlined in the following table. For data sources that support more than one authentication method, the data connection must specify which one to use.
  
|**Data source**|**Authentication method**|
|:-----|:-----|
|SharePoint lists  <br/> |SharePoint user permissions  <br/> |
|Excel workbooks  <br/> |SharePoint user permissions  <br/> |
|SQL Server  <br/> | One of:  <br/>  Windows authentication (integrated security)  <br/>  using Kerberos Constrained Delegation  <br/>  using Secure Store  <br/>  using the Unattended Service Account  <br/>  SQL Server Authentication  <br/> |
|OLE DB/ODBC  <br/> |Varies per data source, typically a user-name and password pair stored in the connection string.  <br/> |
   
Custom data providers can also be used. 
  
The following data sources are supported in Visio but not in Visio Services:
  
- Access databases
    
- Excel workbooks not hosted on SharePoint Server
    
- OLAP
    
## Connect Visio Services to data hosted on SharePoint Server

Visio Services supports data-connected diagrams that are connected to data hosted within the SharePoint farm, including the following:
  
- Excel workbooks residing in a document library
    
- Data in SharePoint lists
    
### Connect to Excel workbooks

Visio Services uses the diagram viewer's SharePoint Server credentials to connect to an .xlsx Excel workbook. For the authentication operation to succeed, the following conditions must be met:
  
- [Office Online Server](/webappsserver/office-web-apps-server) must be provisioned correctly and configured on the SharePoint farm. 
    
- The workbook must be hosted on the same farm as the diagram.
    
- The diagram viewer must have at least "read" permissions to the Excel workbook.
    
No other configuration steps are required to enable this kind of data connection.
  
> [!NOTE]
> As part of connecting to an Excel workbook, Visio Services requests that Excel Online refresh the workbook if it contains connections to external data. In this case, the diagram viewer's identity is passed on to Excel Online so that Excel Online can authenticate to underlying data sources to refresh the workbook. 
  
### Connect Visio Services to SharePoint lists

Visio Services uses the diagram viewer's SharePoint Server credentials to connect to a SharePoint list. For the authentication operation to succeed the following conditions must be met:
  
- In order for a user to access data in an External List, the user must have permissions to access the External Content Type and permissions to access the external data source.
    
- The diagram viewer must have at least "read" permissions to the SharePoint list.
    
No other configuration steps are required to enable this kind of data connection.
  
## Connect Visio Services to external data

Visio Services can connect to various external data sources, including SQL Server, OLE DB/ODBC, and custom data providers. To connect to the data source, Visio Services uses a specific data provider for each data source.
  
As a security measure, Visio Services must explicitly trust data providers before they can be used.
  
Connecting to a SQL Server data source can be done by using either:
  
- Windows authentication
    
- SQL Server Authentication
    
Other data sources use a connection string usually consisting of a user name and password.
  
### Data connections

Visio diagrams use one of two kinds of connections:
  
- Embedded connections
    
- Linked connections
    
Embedded connections are stored as part of the Visio diagram. Linked connections are stored externally to a diagram in Office Data Connection (ODC) files. To use a linked connection, a diagram must reference an .odc file that is also stored in the same farm as the diagram. Each data connection consists of:
  
- A connection string
    
- A query string
    
- An authentication method
    
- Optionally, some metadata required to retrieve external data
    
Each kind of connection has its advantages and drawbacks discussed here; choose the one that best suits your scenario.
  
|**Connection type**|**Embedded connections**|**ODC files**|
|:-----|:-----|:-----|
|Data sources supported  <br/> | SQL Server  <br/>  OLE DB/ODBC  <br/>  Excel workbooks  <br/>  SharePoint lists  <br/>  Custom Data Providers  <br/> | SQL Server (supports all authentication methods)  <br/>  OLE DB/ODBC  <br/> |
|Advantages  <br/> | All connection information is stored in the diagram.  <br/>  Embedded connections require little administrative overhead to support.  <br/>  Embedded connections are easy to create.  <br/> | Linked connections can be centrally stored, managed, audited, shared and access to them controlled by using a data connection library.  <br/>  Diagram authors can use existing connections without having to create queries and connection strings.  <br/>  If the data connection details for a data source change, an administrator only need update one ODC file. Thanks to that change, all diagrams that refer to the ODC file will use the updated connection information when the next refresh occurs. (An example of this scenario is when the database server is moved or the database name is changed.)  <br/> |
|Drawbacks  <br/> | If the data connection details for a data source change, all diagrams with embedded connections to that data source will have to be republished with updated connection information.  <br/>  Embedded data connections are more difficult to audit by SharePoint administrators.  <br/> | Linked connections may require the help of a SharePoint administrator to share, manage and secure.  <br/>  Linked connections are saved in clear text and may contain database passwords. Extra care must be taken to help secure these files.  <br/> |
   
Choose a linked data connection, by using an ODC file, for scenarios in which you must have a data connection to an enterprise-scale relational data source such as SQL Server. Linked data connections are most useful in scenarios in which they will be shared across many users and in which administrator control of the connection is important.
  
> [!NOTE]
> If you are using Visio 2010, ODC files must first be created in Excel and exported to SharePoint Server before it can be used with Visio Services. 
  
Choose an embedded connection for scenarios in which you have to have a quick data connection to a small or file-based data source that will only be used by some users.
  
ODC files can be stored in a data connection library, a special kind of SharePoint document library. Centralizing data connections in such a document library has several advantages:
  
- Administrators can restrict write access to a data connection library to trusted data connection authors to make sure that only well tested and secure data connections are used by diagram authors.
    
- Administrators have a single location to manage data connections for a large group of users.
    
- Administrators can easily approve, audit, revert and manage data connection files by using document library versioning and workflow features.
    
- End-users only have a single location to find diagram data, reducing confusion and user training.
    
### Windows authentication

 This kind of credential is common on Windows networks and is the same credential used to log on to computers on a Windows domain. Windows credentials are considered a more secure and manageable means of controlling access to SQL Server databases. However, one obstacle to using Windows authentication with Visio Services is the Windows double-hop security measure, wherein a user's credentials cannot be passed across more than one computer in a Windows network. Given that Visio Services is a multi-tiered system, special authentication methods are required for Visio Services to retrieve data on behalf of the end-user. 
  
Windows authentication requires that Visio Services present to SQL Server a set of Windows credentials. There are several options for doing this. The authentication method to choose depends on various factors as outlined in the following table. Choose the one that best suits your scenario.
  
|**Authentication method**|**Kerberos constrained delegation**|**Secure Store**|**Unattended Service Account**|
|:-----|:-----|:-----|:-----|
|Description  <br/> |Using Kerberos constrained delegation, the diagram viewer's Windows credentials are sent to the data source directly.  <br/> |Using Secure Store, the viewer's Windows credentials are mapped to another set of credentials specified in a Secure Store target application.  <br/> |Using Secure Store, all viewers are mapped to a specific set of credentials called the Unattended Service Account that is stored in a specific Secure Store target application specified in Visio Services Global Settings.  <br/> |
|Data connection credentials  <br/> |The Windows credentials of the diagram viewer.  <br/> |The credentials specified in the Secure Store target application.  <br/> |The credentials of the Unattended Service Account.  <br/> |
|Advantages  <br/> | The Kerberos protocol is an industry standard in credentials management.  <br/>  Kerberos ties into the existing Active Directory infrastructure.  <br/>  Kerberos delegation enables auditing of individual accesses to a data source.  <br/>  Given that the diagram viewer's identity is known, diagram creators can embed personalized database queries into diagrams.  <br/> | Secure Store is part of SharePoint Server and is easier to configure than Kerberos authentication.  <br/>  Mappings are flexible: a user can be mapped either 1-to-1 or many-to-1.  <br/>  Non-Windows credentials can be used to connect to data sources that do not accept Windows credentials.  <br/>  Mappings created for Visio can be re-used by other business intelligence applications such as Excel Online.  <br/> | The Unattended Service Account is the easiest authentication method to deploy and setup.  <br/>  The Unattended Service Account does not require much administrative overhead.  <br/> |
|Drawbacks  <br/> | Additional administrative effort required to configure for SharePoint Server and Visio Services.  <br/> | Establishing and managing mapping tables requires some administrative overhead.  <br/>  Secure Store allows limited auditing. In the many-to-1 scenario, individual incoming users are mapped into the same credentials through a target application, effectively blending them into one user.  <br/> | Given that everyone is mapped to the same credentials, an administrator cannot distinguish who accessed a data source.  <br/> |
|For the authentication operation to succeed …  <br/> | Kerberos constrained delegation must be set up on the SharePoint farm.  <br/> | Secure Store must be provisioned and configured on the farm. It must also contain appropriate mapping information for a particular incoming user. Additionally the mapping information may need to be updated periodically to reflect password changes on the mapped account.  <br/> | Secure Store must be provisioned and configured on the farm. It must also contain the credentials for the Unattended Service Account. Additionally the mapping information may need to be updated periodically to reflect password changes on the mapped account.  <br/>  The Unattended Service Account must be configured in Visio Services Global Settings.  <br/> |
   
#### Kerberos constrained delegation

Choose Kerberos constrained delegation for more secure and faster authentication to enterprise-scale relational data sources that support Windows authentication. 
  
#### Secure Store

Choose Secure Store for authentication to enterprise-scale relational data sources that may support Windows Authentication. Secure Store is also useful in scenarios in which you want to control user credential mappings.
  
#### Unattended Service Account

For ease of configuration the Visio Graphics Service provides a special configuration where an administrator can create a unique mapping where all users are mapped to a single set of credentials.
  
This account, known as the Unattended Service Account, must be a low-privilege Windows domain account. Visio Services impersonates this account when it connects to a data source on behalf of a diagram viewer. 
  
It is a best practice to give this account as few network permissions as possible, typically only to log on to the network and to access the data source that you want users to connect to. For better security, be sure that the Unattended Service Account does not have access to the SharePoint Configuration and Content databases.
  
The Unattended Service Account is used by Visio Services in the following circumstances:
  
- When an ODC file specifies the use of the Unattended Service Account for either Windows or SQL Server Authentication
    
- When no ODC is used, and Kerberos authentication fails
    
> [!NOTE]
> The unattended account can be a local computer account of type Windows. If the unattended service account is configured as a local computer account, make sure that the configuration is identical on every application server that is running Visio Services. For manageability reasons, the best practice is to use a domain account 
  
Choose the Unattended Service Account when you connect to small ad-hoc deployments in which security is less important or for which speed of deployment is very important.
  
For information about how to use the Unattended Service Account with Visio Services, see [Secure Store for Business Intelligence service applications](/SharePoint/administration/secure-store-for-business-intelligence-service-applications). 
  
### SQL Server Authentication

SQL Server Authentication requires that Visio Services present a SQL Server user name and password to a SQL Server data source to authenticate. Visio Services extracts this user name and password from the data connection's connection string and passes it to the data source.
  
To reduce security risks, Visio Services impersonates the Unattended Service Account when it connects to such a data source.
  
### Authentication against OLE DB/ODBC data sources

Authentication to third-party data sources typically requires that Visio Services present a user name and password to a data source. Like SQL Server Authentication, Visio Services extracts this user name and password from the data connection's connection string and passes them to the data source.
  
To reduce security risks, Visio Services impersonates the Unattended Service Account when it connects to such a data source.
  
## Visio Services data refresh

Visio Services supports refreshing diagrams connected to one or more of the following data sources:
  
- SQL Server
    
- SharePoint lists
    
- Excel workbooks hosted in SharePoint Server
    
- Oracle 9i, 9iR2, 10g, 10gR2, 11g, 11gR2, and DB2 9.2
    
> [!NOTE]
> If the data source that you plan to connect to is not in the list above, you can add support for it by creating a Visio Custom Data Provider. This technology enables you to wrap your existing data sources into one that Visio Services can consume. 
  
Refresh can be triggered in one of following ways from the browser:
  
- The end-user opens the diagram.
    
- The end-user clicks on the refresh button on an already open diagram.
    
- The end-user loads a page that contains the Visio Web Access Web Part which was configured by a site designer to refresh automatically .
    
    > [!NOTE]
    > A SharePoint site designer must place the Visio Web Access Web Part on a page and configure it to refresh periodically. 
  
If there are no previously cached versions of this diagram, any of these actions will trigger a refresh and update the diagram. For information about how to configure cache settings for Visio Services, see [Configure Visio Services](/SharePoint/administration/configure-visio-services).
  

