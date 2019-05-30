---
title: "Plan for administrative and service accounts in SharePoint Server"
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.date: 8/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f07768d4-ca37-447a-a056-1a67d93ef540

description: "Learn about the accounts to use to manage SharePoint Server deployment scenarios and services."
---

# Plan for administrative and service accounts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
To install SharePoint Server, you have to have appropriate administrative and service accounts on servers running SharePoint Server and SQL Server. After installation, you need to have appropriate administrative and service accounts to modify and maintain the environment. The accounts that you require to complete these groups of tasks are not necessarily the same. This article describes the accounts that you require after installation for a single server environment and a server farm environment.
  
> [!IMPORTANT]
> Do not use service account names that contain the symbol $. 
  
    
Use this article along with [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
  
The initial deployment administrative and service accounts article describes the specific account and permissions that you need to grant prior to running Setup. 
  
This article does not describe the account requirements for using Secure Store service in SharePoint Server. For more information, see [Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)).
  
This article does not describe security roles and permissions required to administer in SharePoint Server.
  
## About administrative and service accounts
<a name="Section1"> </a>

This section lists and describes the accounts that you must plan for to manage servers running SQL Server or SharePoint Server. The accounts are grouped according to scope. 
  
After you complete installation and configuration of accounts, ensure that you do not use the Local System account to perform administration tasks or to browse sites. 
  
### Server farm-level accounts

The following table describes the accounts that are used to configure SQL Server database software and to install SharePoint Server.
  
|**Account**|**Purpose**|
|:-----|:-----|
|SQL Server service account  <br/> | SQL Server prompts for this account during SQL Server Setup. This account is used as the service account for the following SQL Server services:  <br/>  MSSQLSERVER  <br/>  SQLSERVERAGENT  <br/>  If you are not using the default instance, these services will be shown as:  <br/>  MSSQL  _\<InstanceName\>_ <br/>  SQLAgent  _\<InstanceName\>_ <br/> |
|Setup user account  <br/> | The user account that is used to run:  <br/>  If you run Microsoft PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database.  <br/>  Setup on each server computer  <br/>  SharePoint Products Configuration Wizard  <br/>  The Psconfig command-line tool  <br/>  The Stsadm command-line tool  <br/> |
|Server farm account  <br/> | This account is also referred to as the database access account.  <br/>  This account has the following properties:  <br/>  It's the application pool identity for the SharePoint Central Administration website.  <br/>  It's the process account for the Windows SharePoint Services Timer service.  <br/> |
   
### Service application accounts

The following table describes the accounts that are used to set up and configure a service application. Plan one set of an application pool and proxy group for each service application that you plan to implement.
  
For more information about service application endpoints, see [Using Service Endpoints](https://go.microsoft.com/fwlink/p/?LinkId=227293).
  
> [!NOTE]
> Excel Services and User Profile Synchronization service only apply to SharePoint 2013. 
  
|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Service Application Endpoint  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Access Services  <br/> |X  <br/> ||
|Business Data Connectivity service  <br/> |X  <br/> |X  <br/> |
|Secure Store Service  <br/> |X  <br/> ||
|Usage and Health Data Collection Service  <br/> |X  <br/> ||
|User Profile Service  <br/> |X  <br/> ||
|Visio Graphics Service  <br/> |X  <br/> ||
|Word Automation services  <br/> |X  <br/> ||
|Excel Services  <br/> |X  <br/> ||
|Managed Metadata Service  <br/> |X  <br/> ||
|PerformancePoint Service  <br/> |X  <br/> ||
|Search Service  <br/> |X  <br/> ||
 
**Note**: This account is used as the identity for the service application endpoint application pool. Unless there are specific isolation requirements, the application pool can be used to host multiple service application endpoints. For Excel Services, Managed Metadata service, PerformancePoint service, and Search service you must be a domain user account. Also Excel Services is only availalbe in SharePoint Server 2010 and 2013.

   
|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Security Token Service  <br/> |X  <br/> ||
|Application Discovery and Load Balancer Service  <br/> |X  <br/> |X  <br/> |
   
**Note**: This account is used as the identity for the service application endpoint application pool. This account must be the Farm Service Account and the SharePoint Products Configuration Wizard automatically creates the application pool.  <br/>

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Unattended Service  <br/>|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
 |Excel Services  <br/> |X  <br/> ||
 |PerformancePoint Service  <br/> |X  <br/> ||
 |Visio Graphics Service  <br/> |X  <br/> ||

**Note**: Excel Services used with workbooks to refresh data. It is required when workbook connections specify "None" for authentication, or when any credentials that are notWindows credentials are used to refresh data. PerformancePoint serivce used for authenticating with data sources. Visio service used with documents to refresh data. It is required when connecting to data sources that are external to SharePoint Server, such as SQL Server.
   

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Default Content Access  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|SharePoint Server Search  <br/> |X  <br/> ||
   
**Note**: The default account for crawling content. A Search service application administrator can create crawl rules to specify other accounts to crawl specific content.  Must have Read Access to the content being crawled.  Full Read permissions must be granted explicitly to content that is outside the local farm.  Full Read permissions are automatically configured for content databases in the local farm.


|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Search Service  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|SharePoint Server Search  <br/> |X  <br/> ||
   
**Note**: The Windows service account for the SharePoint Server Search service. This setting affects all Search service applications in the farm. Must be a domain user account. 

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|User Profile Synchronization Service  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|User Profile Synchronization Service  <br/> |X  <br/> ||
   
**Note**: This is the Windows service account for the User Profile Synchronization Service. Requires Log on Locally permission on the computer running the instance of the User Profile Synchronization Service.

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Synchronization Connection  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|User Profile Service  <br/> |X  <br/> ||
   
**Note**: This is the account used to perform synchronization with the remote directory service. There can be one account per synchronization connection.  Replicating Directory Changes permissions on the domains being synchronized.  Replicating Directory Changes permissions on the configuration partition of the domains being synchronized if the NetBIOS and fully qualified domain name (FQDN) names do not match. 

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|App Management Service  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|App management  <br/> |X  <br/> |X  <br/> |


**Note**: This account permits you to install SharePoint apps from the SharePoint Store or the App Catalog.


|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|PowerPoint Conversion Service  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|PowerPoint conversion service  <br/> |X  <br/> | |
   
**Note**: This account converts Microsoft PowerPoint presentations into various formats.  <br/>

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Machine Translation service  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Machine Translation service  <br/> |X  <br/> 
   
**Note**: This account performs automated machine translation.  <br/>

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Access Services 2013  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Access Services in SharePoint Server 2013  <br/> |X  <br/> ||
   
**Note** This account views, edits, and interacts with Access 2013 databases in a browser.  <br/> 

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Work Management  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Work management  <br/> |X  <br/>
   
**Note**: This account provides task aggregation across work management systems, including SharePoint products, Microsoft Exchange Server, and Microsoft Project Server.  <br/>

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Distributed Cache  <br/> |

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Distributed Cache  <br/> |X  <br/> |X  <br/> |
   
**Note**: This account provides in-memory caching services to several features in SharePoint Server. Some of the features that use the Distributed Cache service include:  <br/>  Newsfeeds  <br/>  Authentication  <br/>  OneNote client access  <br/>  Security Trimming  <br/>  Page load performance  <br/> 
   
### Additional application pool identity accounts

If you create additional application pools to host sites, plan for additional application pool identity accounts. The following table describes the application pool identity account. Plan one application pool account for each application pool that you plan to implement.
  
|**Account**|**Purpose**|
|:-----|:-----|
|Application pool identity  <br/> |The user account that the worker processes that service the application pool use as their process identity. This account is used to access content databases that are associated with the web applications that reside in the application pool.  <br/> |
   
## Single server standard requirements
<a name="Section2"> </a>

If you are deploying to a single server computer, account requirements are greatly reduced. In an evaluation environment, you can use a single account for all of the account purposes. In a production environment, ensure that the accounts that you create have the appropriate permissions for their purposes. 
  
For a list of account permissions for single server environments, see [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
  
## Server farm requirements
<a name="Section3"> </a>

If you are deploying to more than one server computer, use the server farm standard requirements to ensure that accounts have the appropriate permissions to perform their processes across multiple computers. The server farm standard requirements detail the minimum configuration that is necessary to operate in a server farm environment.
  
For a list of standard requirements for server farm environments, see the requirements listed in the [Technical reference: Account requirements by scenario](#Section7) section of this article. 
  
For some accounts, additional permissions or access to databases are configured when you run Setup. These are noted in the accounts planning tool. An important configuration for database administrators to be aware of is the addition of the **WSS_Content_Application_Pools** database role. Setup adds this role to the following databases: 
  
- SharePoint_Config database (configuration database)
    
- SharePoint_AdminContent database
    
Members of the **WSS_Content_Application_Pools** database role are granted the Execute permission to a subset of the stored procedures for the database. Additionally, members of this role are granted the Select permission to the Versions table (dbo.Versions) in the SharePoint_AdminContent database. 
  
For other databases, the accounts planning tool indicates that access to read from these databases is automatically configured. In some cases, limited access to write to a database is also automatically configured. To provide this access, permissions to stored procedures are configured.
  
## Technical reference: Account requirements by scenario
<a name="Section7"> </a>

This section lists account requirements by scenario:
  
- [Single server standard requirements](#Subsection1)
    
- [Server farm standard requirements](#Subsection2)
    
### Single server standard requirements
<a name="Subsection1"> </a>

#### Server farm-level accounts

|**Account**|**Requirements**|
|:-----|:-----|
|SQL Server service  <br/> |Local System account (default)  <br/> |
|Setup user  <br/> |Member of the Administrators group on the local computer  <br/> |
|Server farm  <br/> |Network Service (default)  <br/> No manual configuration is necessary.  <br/> |
   
#### Service application accounts

> [!IMPORTANT]
> Accounts in this table apply only to SharePoint Server. 
  
|**Account**|**Requirements**|
|:-----|:-----|
|SharePoint Server Search Service  <br/> |By default, this account runs as the Local System account.  <br/> If you want to crawl remote content by changing the default content access account or by using crawl rules, change this to a domain user account. If you do not change this account to a domain user account, you cannot change the default content access account to a domain user account or add crawl rules to crawl this content. This restriction is designed to prevent elevation of privilege for any other process running as the Local System account.  <br/> |
|Default Content Access  <br/> |No manual configuration is necessary if this account is only crawling local farm content. If you want to crawl remote content by using crawl rules, change this to a domain user account, and apply the requirements listed for a server farm.  <br/> |
|Content Access  <br/> |Same requirement as the default content access account.  <br/> |
|Profile import Default Access  <br/> |Same requirements as server farm.  <br/> |
|Excel Services Unattended Service  <br/> |Must be a domain user account.  <br/> |
   
#### Additional application pool identity accounts

|**Account**|**Requirements**|
|:-----|:-----|
|Application pool identity  <br/> |No manual configuration is necessary.  <br/> The Network Service account is used for the default web site that is created during Setup and configuration.  <br/> |
   
### Server farm standard requirements
<a name="Subsection2"> </a>

#### 

#### 

#### Server farm-level accounts

> [!IMPORTANT]
> The accounts in this table apply only to SharePoint Server 
  
|**Account**|**Requirements**|
|:-----|:-----|
|SQL Server service account  <br/> |Use either a Local System account or a domain user account.  <br/> If a domain user account is used, this account uses Kerberos authentication by default, which requires additional configuration in your network environment. If SQL Server uses a service principal name (SPN) that is not valid (that is, that does not exist in the Active Directory Domain Services (AD DS)service environment), Kerberos authentication fails, and then NTLM is used. If SQL Server uses an SPN that is valid but is not assigned to the appropriate container in AD DS, authentication fails. Authentication will always try to use the first SPN that it finds, so ensure that there are no SPNs assigned to inappropriate containers in AD DS.  <br/> If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant the machine account ( _(\<domain_name\>\\<SQL_hostname\>_) permissions to the external resource.  <br/> |
|Setup user account  <br/> | Domain user account.  <br/>  Member of the Administrators group on each server on which Setup is run.  <br/>  SQL Server login on the computer running SQL Server.  <br/>  Member of the Server admin SQL Server security role.  <br/>  If you run Stsadm commands that affect a database, this account must be a member of the **db_owner** fixed database role for the database.  <br/> |
|Server farm account  <br/> | Domain user account.  <br/>  Additional permissions are automatically granted for this account on web servers and application servers that are joined to a server farm.  <br/>  This account is automatically added as a SQL Server login on the computer running SQL Server and added to the following SQL Server security roles:  <br/> **dbcreator** fixed server role  <br/> **securityadmin** fixed server role  <br/> **db_owner** fixed database role for all databases in the server farm  <br/> > [!NOTE]>  If you configure the Secure Store Service, the server farm account will not automatically be given **db_owner** access to the Secure Store Service database.           |
   
#### Service application service accounts

> [!IMPORTANT]
> The accounts in this table apply only to SharePoint Server 
  
|**Account**|**Requirements**|
|:-----|:-----|
|SharePoint Server Search service account  <br/> | Must be a domain user account.  <br/>  Must not be a member of the Farm Administrators group.  <br/>  The following are automatically configured:  <br/>  Access to read from the configuration database, administration content database, the search administration database, crawl databases.  <br/>  Full Control access to the index partitions on the query servers.  <br/> |
|Default content access account  <br/> | Must be a domain user account.  <br/>  Must not be a member of the Farm Administrators group.  <br/>  Read access to external or secure content sources that you want to crawl by using this account.  <br/>  For sites that are not a part of the server farm, this account must explicitly be granted Full Read permissions on the web applications that host the sites.  <br/>  The following are automatically configured:  <br/>  Full Read permissions are automatically granted to content databases hosted by the server farm.  <br/> |
|Content access account  <br/> | Read access to external or secure content sources that this account is configured to access.  <br/>  For web sites that are not a part of the server farm, this account must explicitly be granted Full Read permissions on the web applications that host the sites.  <br/> |
|Profile import default access account  <br/> | Read access to the directory service.  <br/>  The account must have the Replicate Changes permission in AD DS.  <br/>  Manage User Profiles personalization services permission.  <br/>  View permissions on entities used in Business Data Catalog import connections.  <br/> |
|Excel Services unattended service account  <br/> |Must be a domain user account.  <br/> |
   
#### Additional application pool identity accounts

|**Account**|**Requirements**|
|:-----|:-----|
|Application pool identity  <br/> | No manual configuration is necessary.  <br/>  The following are automatically configured:  <br/>  Membership in the **SP_DATA_ACCESS** role for content databases and search databases associated with the web application.  <br/>  Membership in specific application pool roles for the configuration and the SharePoint_AdminContent databases.  <br/>  Additional permissions for this account to front-end web servers and application servers are automatically granted.  <br/> |
   
## See also
<a name="Section7"> </a>

#### Other Resources

[Plan for SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261834(v=office.14))

