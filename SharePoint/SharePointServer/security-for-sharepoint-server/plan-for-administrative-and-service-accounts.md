---
title: "Plan for administrative and service accounts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
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
> Do not use service account names that contain the symbol $ with the exception of using a Group Managed Service Account for SQL Server.
    
Use this article along with [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
  
The initial deployment administrative and service accounts article describes the specific account and permissions that you need to grant prior to running Setup. 
  
This article does not describe the account requirements for using Secure Store service in SharePoint Server. For more information, see [Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)).
  
## About administrative and service accounts
<a name="Section1"> </a>

This section lists and describes the accounts that you must plan for to manage servers running SQL Server or SharePoint Server. The accounts are grouped according to scope. 
  
After you complete installation and configuration of accounts, ensure that you do not use the Local System account to perform administration tasks or to browse sites. 
  
### Server farm-level accounts

The following table describes the accounts that are used to configure SQL Server database software and to install SharePoint Server.
  
|**Account**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|
|SQL Server service account| The SQL Server service account is used to run SQL Server. It is the service account for the following SQL Server services:  <br/>  MSSQLSERVER  <br/>  SQLSERVERAGENT  <br/>  If you do not use the default SQL Server instance, in the Windows Services console, these services will be shown as the following:  <br/>  MSSQL\<InstanceName\>  <br/>  SQLAgent\<InstanceName\>|Use either a domain user account or preferably, a [Group Managed Service Account](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview).  <br/> If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account or Group Managed Service Account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant permissions to the external resource to the machine account (\<domain_name\>\\<SQL_hostname\>).  <br/> The instance name is arbitrary and was created when SQL Server was installed.|
|Farm administrator user account| The farm administrator user account is a uniquely identifiable account assigned to a SharePoint administrator. It is used to run the following:  <br/>  Setup  <br/>  SharePoint Products Configuration Wizard| Domain user account.  <br/>  Member of the Administrators group on each SharePoint server in the farm.  <br/>  Member of the following SQL Server role (optional): **sysadmin** fixed server role.  <br/>  If you run Windows PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database or a member of the **sysadmin** fixed server role on SQL.|
|Farm service account| The farm service account is used to perform the following tasks:  <br/>  Act as the application pool identity for the SharePoint Central Administration website.  <br/>  Run the Microsoft SharePoint Foundation Workflow Timer Service.  | Domain user account.  <br/>  Additional permissions are automatically granted for the server farm account on Web servers and application servers that are joined to a server farm.  <br/>  The server farm account is automatically added as a SQL Server login on the computer that runs SQL Server. The account is added to the following SQL Server security roles:  <br/> * **dbcreator** fixed server role  <br/> * **securityadmin** fixed server role  <br/> * **db_owner** fixed database role for all SharePoint databases in the server farm  <br/> This account should not be used interactively by an administrator. |
   
### Service application accounts

The following table describes the accounts that are used to set up and configure a service application. Plan one set of an application pool and proxy group for each service application that you plan to implement.
  
For more information about service application endpoints, see [Using Service Endpoints](https://go.microsoft.com/fwlink/p/?LinkId=227293).
  
> [!NOTE]
> Excel Services and User Profile Synchronization Service only apply to SharePoint 2013. 
  
|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Service Application Endpoint||Run SharePoint Services Instances and Windows Services|Domain user account|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Access Services|X||
|Business Data Connectivity service|X|X|
|Secure Store Service|X||
|Usage and Health Data Collection Service|X||
|User Profile Service|X||
|Visio Graphics Service|X||
|Word Automation services|X||
|Excel Services|X||
|Managed Metadata Service|X||
|PerformancePoint Service|X||
|Search Service|X||
 
> [!NOTE]
> This account is used as the identity for the service application endpoint application pool. Unless there are specific isolation requirements, the application pool can be used to host multiple service application endpoints. For Excel Services, Managed Metadata service, PerformancePoint service, and Search service you must be a domain user account. Also Excel Services is only available in SharePoint Server 2013.

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Security Token Service|X||
|Application Discovery and Load Balancer Service|X|X|
   
> [!NOTE]
> This account is used as the identity for the service application endpoint application pool. This account must be the Farm Service Account and the SharePoint Products Configuration Wizard automatically creates the application pool.  

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Unattended Service|N/A|Used to execute functions on behalf of the user or service|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
 |Excel Services|X||
 |PerformancePoint Service|X||
 |Visio Graphics Service|X||

> [!NOTE]
> Excel Services used with workbooks to refresh data. It is required when workbook connections specify "None" for authentication, or when any credentials that are notWindows credentials are used to refresh data. PerformancePoint service is used for authenticating with data sources. Visio service is used with documents to refresh data. It is required when connecting to data sources that are external to SharePoint Server, such as SQL Server.
   
|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Default Content Access|Search|Crawl content|Read access to the content being crawled|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|SharePoint Server Search|X||
   
> [!NOTE]
> The default account for crawling content. A Search service application administrator can create crawl rules to specify other accounts to crawl specific content.  Must have Read Access to the content being crawled.  Full Read permissions must be granted explicitly to content that is outside the local farm.  Full Read permissions are automatically configured for content databases in the local farm. Requires **Manage auditing and security log** right in the Local User Policy on Windows file servers it is configured to crawl.

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Search Service|Search|Run the Windows Search services|Be a domain user account|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|SharePoint Server Search|X||

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Farm administrator|User Profile Synchronization Service|Runs the Forefront Identity Manager services|Farm administrator account; Local administrator where the User Profile Synchronization Service is started|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|User Profile Synchronization Service|X|N/A|

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Synchronization Connection|User Profile Service|Connect to user identity stores|Replicate directory changes (Active Directory), read access (other directories)|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|User Profile Service|X|N/A|
   
> [!NOTE]
> Replicating Directory Changes permissions on the configuration partition of the domains being synchronized if the NetBIOS and fully qualified domain name (FQDN) names do not match. 

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|App Management Service|N/A|Used to install SharePoint Add-ins|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|App management|X|X|

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|PowerPoint Conversion Service|PowerPoint Conversion Services|Convert PowerPoint files to other file formats|Farm administrator role (SharePoint Server 2013 only)|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|PowerPoint conversion service|X||

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Machine Translation service|Machine Translation service|Perform automated machine translations|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Machine Translation service|X||

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Access Services 2013|Access Services|Interact with Access 2013 databases in a browser|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Access Services in SharePoint Server 2013|X||

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Work Management|Work Management service|Provides task aggregation across SharePoint, Exchange, and Project Server.|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Work management|X||  

|**Account**|**Service**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|:-----|
|Distributed Cache|AppFabric Windows service|Runs Distributed Cache operations|N/A|

|**Service name**|**In SharePoint Server**|**In SharePoint Foundation**|
|:-----|:-----|:-----|
|Distributed Cache   |X   |X   |
   
> [!NOTE]
> Some of the features that use the Distributed Cache service include:Newsfeeds, Authentication, OneNote client access, Security Trimming, and improves Page load performance. At least one Distributed Cache server is required in the farm.
 
### Additional application pool identity accounts

If you create additional application pools to host sites, plan for additional application pool identity accounts. The following table describes the application pool identity account. Plan one application pool account for each application pool that you plan to implement.
  
|**Account**|**Purpose**|
|:-----|:-----|
|Application pool identity|The user account that the worker processes that service the application pool use as their process identity. This account is used to access content databases that are associated with the web applications that reside in the application pool.|
   
## Single server standard requirements
<a name="Section2"> </a>

If you are deploying to a single server, account requirements are greatly reduced. In an evaluation environment, you can use a single account for all of the account purposes. In a production environment, ensure that the accounts that you create have the appropriate permissions for their purposes. 
  
For a list of account permissions for single server environments, see [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
  
## Server farm requirements
<a name="Section3"> </a>

If you are deploying to more than one server, use the server farm standard requirements to ensure that accounts have the appropriate permissions to perform their processes across multiple computers. The server farm standard requirements detail the minimum configuration that is necessary to operate in a server farm environment.
  
For a list of standard requirements for server farm environments, see the requirements listed in the [Technical reference: Account requirements by scenario](#Section7) section of this article. 
  
For some accounts, additional permissions or access to databases are configured when you run the Configuration Wizard. These are noted in the accounts planning tool. An important configuration for database administrators to be aware of is the addition of the **WSS_Content_Application_Pools** database role. The Configuration Wizard adds this role to the following databases: 
  
- SharePoint_Config database (configuration database)
    
- SharePoint_Admin content database
    
Members of the **WSS_Content_Application_Pools** database role are granted the Execute permission to a subset of the stored procedures for the database. Additionally, members of this role are granted the Select permission to the Versions table (dbo.Versions) in the SharePoint_AdminContent database. 
  
For other databases, the accounts planning tool indicates that access to read from these databases is automatically configured. In some cases, limited access to write to a database is also automatically configured. To provide this access, permissions to stored procedures are configured.
  
## Technical reference: Account requirements by scenario
<a name="Section7"> </a>

This section lists account requirements by scenario:
  
- [Single server standard requirements](#Subsection1)
    
- [Server farm standard requirements](#Subsection2)
    
### Single server standard requirements
<a name="Subsection1"> </a>

> [!IMPORTANT]
> We do not recommend this configuration in a production environment.

#### Server farm-level accounts

|**Account**|**Requirements**|
|:-----|:-----|
|SQL Server service|Local System account (default)|
|Farm administrator user account  |Member of the Administrators group on the local computer.|
|Farm service  |Network Service (default)   No manual configuration is necessary.|

#### Service application accounts

> [!IMPORTANT]
> Accounts in this table apply only to SharePoint Server. 
  
|**Account**|**Requirements**|
|:-----|:-----|
|SharePoint Server Search Service|By default, this account runs as the Local System account.   If you want to crawl remote content by changing the default content access account or by using crawl rules, change this to a domain user account. If you do not change this account to a domain user account, you cannot change the default content access account to a domain user account or add crawl rules to crawl this content. This restriction is designed to prevent elevation of privilege for any other process running as the Local System account.|
|Default Content Access|No manual configuration is necessary if this account is only crawling local farm content. If you want to crawl remote content by using crawl rules, change this to a domain user account, and apply the requirements listed for a server farm.|
|Content Access|Same requirement as the default content access account.|
|Profile Synchronization account|Same requirements as server farm.|
|Excel Services Unattended Service|Must be a domain user account.|
   
#### Additional application pool identity accounts

|**Account**|**Requirements**|
|:-----|:-----|
|Application pool identity|No manual configuration is necessary.   The Network Service account is used for the default web site that is created during Setup and configuration.|
   
### Server farm standard requirements
<a name="Subsection2"> </a>

#### Server farm-level accounts
  
|**Account**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|
|SQL Server service account  <br/> | The SQL Server service account is used to run SQL Server. It is the service account for the following SQL Server services:  <br/>  MSSQLSERVER  <br/>  SQLSERVERAGENT  <br/>  If you do not use the default SQL Server instance, in the Windows Services console, these services will be shown as the following:  <br/>  MSSQL\<InstanceName\>  <br/>  SQLAgent\<InstanceName\>  <br/> |Use either a domain user account or preferably, a [Group Managed Service Account](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview).  <br/> If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account or Group Managed Service Account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant permissions to the external resource to the machine account (\<domain_name\>\\<SQL_hostname\>).  <br/> The instance name is arbitrary and was created when SQL Server was installed.  <br/> |
|Farm administrator user account  <br/> | The farm administrator user account is a uniquely identifiable account assigned to a SharePoint administrator. It is used to run the following:  <br/>  Setup  <br/>  SharePoint Products Configuration Wizard  <br/> | Domain user account.  <br/>  Member of the Administrators group on each SharePoint server in the farm.  <br/>  Member of the following SQL Server role (optional): **sysadmin** fixed server role.  <br/>  If you run Windows PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database or a member of the **sysadmin** fixed server role on SQL.  <br/> |
|Farm service account <br/> | The farm service account is used to perform the following tasks:  <br/>  Act as the application pool identity for the SharePoint Central Administration website.  <br/>  Run the Microsoft SharePoint Foundation Workflow Timer Service.  <br/> | Domain user account.  <br/>  Additional permissions are automatically granted for the server farm account on Web servers and application servers that are joined to a server farm.  <br/>  The server farm account is automatically added as a SQL Server login on the computer that runs SQL Server. The account is added to the following SQL Server security roles:  <br/> * **dbcreator** fixed server role  <br/> * **securityadmin** fixed server role  <br/> * **db_owner** fixed database role for all SharePoint databases in the server farm  <br/> This account should not be used interactively by an administrator. |
   
#### Service application service accounts

> [!IMPORTANT]
> Profile Synchronization account and Excel Services unattended service account only apply to SharePoint Server.
  
|**Account**|**Requirements**|
|:-----|:-----|
|SharePoint Server Search service account| Must be a domain user account.    Must not be a member of the Farm Administrators group.    The following are automatically configured:    Access to read from the configuration database, administration content database, the search administration database, crawl databases.    Full Control access to the index partitions on the query servers.|
|Default content access account| Must be a domain user account.    Must not be a member of the Farm Administrators group.    Read access to external or secure content sources that you want to crawl by using this account.    For sites that are not a part of the server farm, this account must explicitly be granted Full Read permissions on the web applications that host the sites.    The following are automatically configured:    Full Read permissions are automatically granted to content databases hosted by the server farm.|
|Content access account| Read access to external or secure content sources that this account is configured to access.    For web sites that are not a part of the server farm, this account must explicitly be granted Full Read permissions on the web applications that host the sites.|
|Profile Synchronization account|Read access to the directory service.    The account must have the Replicate Changes permission in Active Directory.    Manage User Profiles personalization services permission.    View permissions on entities used in Business Data Catalog import connections.|
|Excel Services unattended service account|Must be a domain user account.   |
   
#### Additional application pool identity accounts

|**Account**|**Requirements**|
|:-----|:-----|
|Application pool identity| No manual configuration is necessary.    The following are automatically configured:    Membership in the **SP_DATA_ACCESS** role for content databases and search databases associated with the web application.    Membership in specific application pool roles for the configuration and the SharePoint_AdminContent databases.    Additional permissions for this account to front-end web servers and application servers are automatically granted.|
