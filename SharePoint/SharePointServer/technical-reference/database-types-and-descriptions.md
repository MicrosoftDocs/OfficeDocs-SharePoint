---
title: "Database types and descriptions in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: reference
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 9b1e8b21-7675-4186-beb6-3adeef4360e6
description: "Learn about sizing and location information for the databases that support SharePoint Server Databases."
---

# Database types and descriptions in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes the databases that are installed for SharePoint Server. Each database description includes information about sizing and placement. For more information see [Storage and SQL Server capacity planning and configuration (SharePoint Server)](../administration/storage-and-sql-server-capacity-planning-and-configuration.md).
  
Databases for SharePoint Server 2019 can be hosted in Microsoft SQL Server 2016 and Microsoft SQL Server 2017. Databases for SharePoint Server 2016 can be hosted in SQL Server 2014 Service Pack 1 (SP1) and SQL Server 2016. Databases for SharePoint Server 2013 can be hosted in SQL Server 2008 R2 with Service Pack 1 (SP1) or SQL Server 2012. For more information see [System requirements for SharePoint Servers 2016 and 2019](/sharepoint/install/system-requirements-for-sharepoint-server-2016) and [Hardware and software requirements for SharePoint 2013](../install/hardware-and-software-requirements-0.md).
  
All database names that are listed in this article are automatically created when you run the SharePoint Products Configuration Wizard. You do not have to use these naming conventions. You can either specify your own database names when you create them or change the names after they are created. For more information, see [Move or rename service application databases in SharePoint Server](../administration/move-or-rename-service-application-databases.md)
  
The database sizes listed in this article are based on the following ranges.
  
****

|**Descriptor**|**Size range**|
|:-----|:-----|
|Very Small  <br/> |Up to 100 megabyte (MB)  <br/> |
|Small  <br/> |1 gigabyte (GB) or less  <br/> |
|Medium  <br/> |Up to 100 GB  <br/> |
|Large  <br/> |Up to 1 terabyte  <br/> |
|Extra-large  <br/> |More than 1 terabyte  <br/> |
   
    
You can download the SharePoint Server 2016 database poster, as either a [PDF](http://download.microsoft.com/download/D/5/D/D5DC1121-8BC5-4953-834F-1B5BB03EB691/DBrefguideSPS2016_tabloid.pdf) or [Visio](http://download.microsoft.com/download/D/5/D/D5DC1121-8BC5-4953-834F-1B5BB03EB691/DBrefguideSPS2016_tabloid.vsdx) file. 
  
For a graphical overview of the databases that support SharePoint Server 2013, see [Database model](https://go.microsoft.com/fwlink/p/?LinkID=255376).
  
## SharePoint Server system databases
<a name="Sec1"> </a>

The following databases are part of all SharePoint Server deployments. These databases are installed when any SharePoint Server edition is deployed. The Configuration, Central Administration Content, and Content databases are the three databases that are automatically installed when you deploy SharePoint Server.
  
### Configuration

The configuration database contains data about the following:
  
- SharePoint databases
    
- Internet Information Services (IIS) web sites
    
- Web applications
    
- Trusted solutions
    
- Web Part packages
    
- Site templates
    
- Web applications
    
- Distributed Cache configuration objects
    
    The configuration database tracks the state of all servers in the farm that run the Distributed Cache service.
    
The configuration database also contains specific data for SharePoint Server farm settings, such as default quota settings and blocked file types.
  
**Configuration database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |SharePoint_Config  <br/> |
|Location requirements  <br/> |Must be co-located with the Central Administration database  <br/> |
|General size information and growth factors  <br/> |Small  <br/> Transaction log files that are stored in the configuration database are likely to become large. For more information, see [Additional notes](#notes).  <br/> |
|Read/write characteristics  <br/> |Read-intensive  <br/> |
|Recommended scaling method  <br/> |Must scale-up because only one configuration database is supported per farm. (Significant growth is unlikely.)  <br/> |
|Associated health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, SQL Server, and System Center Data Protection Manager. Backing up and restoring the configuration databases is special because of the transaction log. For more information, see [Additional notes](#notes).  <br/> |
|Default recovery model  <br/> |Full. We recommend that you keep the configuration database on the full recovery model and take backups to truncate the log files.  <br/> |
   
#### Additional notes
<a name="notes"> </a>

 **Transaction log files**. We recommend that you back up the transaction log for the configuration database regularly to force truncation. If you are mirroring your system, you should also keep the database running in full recovery mode. For more information, see [The Transaction Log (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715518&amp;clcid=0x409).
  
 **Backup and Restore**. The configuration database is backed up when you perform a SharePoint farm configuration and content backup. Note that some configuration settings from the database are exported and stored as XML file. When a farm is restored, the configuration database is not restored. Instead, the saved configuration settings are imported. The configuration database can be successfully backed up and restored by using SQL Server or other tools if the SharePoint farm is first taken offline.
  
> [!NOTE]
> Many configuration settings are not saved during a farm configuration-only backup or restore. These configuration settings may include particular Web application settings, service application settings, and settings that are specific to the local server. These settings are saved during a farm content and configuration backup. But some of them, such as service application proxy settings, cannot be restored during a farm recovery. For information about what is saved during a configuration backup, see [Back up farm configurations in SharePoint Server](../administration/back-up-a-farm-configuration.md). For information about how to document and copy configuration settings that are not backed up, see [Copy configuration settings between farms in SharePoint Server](../administration/copy-configuration-settings-between-farms.md). 
  
### Central Administration content

The Central Administration content database is considered to be a configuration database. It stores all configuration data for the Central Administration site collection. If SQL Server Power Pivot for SharePoint Server 2016 is installed, the Central Administration content database also stores the Excel Online worksheets and Power Pivot data files used in the Power Pivot Management Dashboard. 
  
> [!NOTE]
> Power Pivot for SharePoint can only be installed on SharePoint Server 2016 when you use SQL Server 2016 CTP 3.1 or later as the database server. 
  
For more information, download [Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016](http://go.microsoft.com/fwlink/p/?LinkID=717977&amp;clcid=0x409). For details about configuring and deploying business intelligence in a multiple server SharePoint Server 2016 farm, download [Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm](http://go.microsoft.com/fwlink/p/?LinkID=723106&amp;clcid=0x409). 
  
> [!NOTE]
> Excel Services and its associated business intelligence capabilities are no longer hosted on SharePoint Server 2016. Excel Services functionality is now part of Excel Online in Office Online Server (this is the next version of Office Web Apps Server), and SharePoint users can use the services from there. For more information, see [Office Online Server](/webappsserver/office-web-apps-server) and [Configure Excel Online administrative settings](/SharePoint/administration/configure-excel-services). 
  
If SQL Server 2012 Power Pivot for SharePoint 2013 is installed, the Central Administration content database also stores the Excel worksheets and Power Pivot data files used in the Power Pivot Management Dashboard. Note that Power Pivot for SharePoint 2013 can only be installed on SharePoint Server 2013.
  
**Central Administration content database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name prefix when it is installed by using the SharePoint Products Configuration Wizard  <br/> |SharePoint_AdminContent_\<GUID\>  <br/> |
|Location requirements  <br/> |Must be located on the same database engine instance with the configuration database.  <br/> |
|General size information, and growth factors  <br/> |Small  <br/> If you use Power Pivot for SharePoint and use the default settings that keep usage data collection and data refresh history for 365 days, the Central Administration content database will grow over the span of one year.  <br/> |
|Read/write characteristics  <br/> |Varies  <br/> |
|Recommended scaling method  <br/> |Must scale-up. The database must grow larger because only one Central Administration content database is supported per farm. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, SQL Server, and System Center Data Protection Manager. Backing up and restoring the Central Administration content databases is special. For more information, see [Additional notes](#notes2).  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
#### Additional notes
<a name="notes2"> </a>

 **Backup and restore**. The Central Administration content database is backed up when you perform a SharePoint farm configuration and content backup. When a farm is restored, the Central Administration content database is not restored. The Central Administration content database can be successfully backed up and restored by using SQL Server or other tools if the SharePoint farm is first taken offline.
  
### Content databases

Content databases store all content for a site collection. This includes site documents or files in document libraries, list data, Web Part properties, audit logs, and sandboxed solutions, in addition to user names and rights.
  
All of the files that are stored for a specific site collection are located in one content database on only one server. A content database can be associated with more than one site collection.
  
Content databases also store the following:
  
- Project Server 2016 data and objects
    
- Power Pivot for SharePoint user data
    
> [!NOTE]
> Note that Power Pivot for SharePoint can only be installed on SharePoint Server 2016 when you use SQL Server 2016 CTP 3.1 or higher as the database server. Download SQL Server 2016 CTP 3.1 from [Microsoft Download Center](https://go.microsoft.com/fwlink/p/?LinkID=716860). 
  
Power Pivot for SharePoint 2013 can't be installed on SharePoint Foundation 2013, only on SharePoint Server 2013.
  
Note that to use the business intelligence (BI) tools in SharePoint Server 2013 you must install SQL Server 2012 with Service Pack 1 (SP1) or SQL Server 2014, 64-bit version. For more information, see [System requirements for SharePoint Servers 2016 and 2019](/sharepoint/install/system-requirements-for-sharepoint-server-2016) and [Software requirements for business intelligence in SharePoint Server](../administration/software-requirements-for-business-intelligence.md).
  
**Content database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |WSS_Content  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |We recommend limiting the size of content databases to 200 GB to help ensure system performance. For more information, see [Additional notes](#notes3).  <br/> Content database size varies significantly by usage. For more information, see [Additional notes](#notes3).  <br/> |
|Read/write characteristics  <br/> |Varies by usage. For example, collaboration environments are write-intensive and document management environments are read-intensive.  <br/> |
|Recommended scaling method  <br/> |Content databases that support a site collection must scale-up. The database must be able to grow larger as needed. You can create additional site collections that are associated with a Web application and associate the new site collection with a different content database. If a content database is associated with multiple site collections, you can move a site collection to another database. For information about how to size content databases, see [Storage and SQL Server capacity planning and configuration (SharePoint Server)](../administration/storage-and-sql-server-capacity-planning-and-configuration.md).  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, SQL Server, and System Center Data Protection Manager.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
#### Additional notes
<a name="notes3"> </a>

 **Recommended content database size limitations**
  
Content database sizes up to 1 terabyte are supported only for large, single-site repositories and archives in which data remains reasonably static, such as reference document management systems and Records Center sites. Larger database sizes are supported for these scenarios because their I/O patterns and typical data structure formats have been designed for, and tested at, larger scales. For more information about large-scale document repositories, see "Estimate Performance and Capacity Requirements for Large Scale Document Repositories", available from [Storage and SQL Server capacity planning and configuration (SharePoint Server)](../administration/storage-and-sql-server-capacity-planning-and-configuration.md).
  
 **Content database size estimation**
  
Content database size varies significantly with the usage of the site. Growth factors include the number of documents, number of users, use of versioning, use of Recycle Bins, size of quotas, whether the audit trail is configured, and how many items are chosen for auditing.
  
If Power Pivot for SharePoint is being used, the Excel Online files stored in SharePoint Server 2016 grow larger, which increases the size of the content database. For more information, see [PowerPivot for SharePoint (SSAS)](http://go.microsoft.com/fwlink/p/?LinkID=733878&amp;clcid=0x409).
  
If Power Pivot for SharePoint is being used, the Excel files stored in SharePoint Server 2013 grow larger, which increases the size of the content database. For more information, see [Plan a PowerPivot Deployment in a SharePoint Farm](https://go.microsoft.com/fwlink/p/?LinkID=186698).
  
For detailed recommendations about how to calculate the size of a content database, see [Storage and SQL Server capacity planning and configuration (SharePoint Server)](../administration/storage-and-sql-server-capacity-planning-and-configuration.md).
  
### SharePoint Server service application databases
<a name="Sec2"> </a>

The following service application databases are available in SharePoint Server deployments.
  
### App Management database
<a name="Sec2"> </a>

The App Management database is used by the App Management Service application. It stores the app licenses and permissions that are downloaded from the SharePoint Store or App Catalog.
  
**App Management database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |AppMng_Service_DB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small. Scale-up when the service application database reaches 10 GB. Scale out only on SharePoint Online.  <br/> |
|Read/write characteristics  <br/> |Write-heavy during apps installation and license renewal.  <br/> |
|Recommended scaling method  <br/> |App License Management databases can scale out only on SharePoint Online.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Business Data Connectivity service application database
<a name="Sec2"> </a>

The Business Data Connectivity service application database stores external content types and related objects.
  
**Business Data Connectivity database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Bdc_Service_DB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small. Size is determined by the number of connections.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Must scale-up. The database must grow larger, because only one Business Data Connectivity database is supported per farm. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Search service application databases
<a name="Sec2"> </a>

The Search service application has four databases that support SharePoint Server 2016. The four Search service application databases are shown in the following list. The tables that follow the list display the relevant database information.
  
- **Search Administration:** The Search Administration database hosts the Search service application configuration and access control list (ACL) for the crawl component. 
    
- **Analytics Reporting:** The Analytics Reporting database stores the results for usage analysis reports and extracts information from the Link database when needed. 
    
- **Crawl:** The Crawl database stores the state of the crawled data and the crawl history. 
    
- **Link:** The Link database stores the information that is extracted by the content processing component and the click through information. 
    
 **Important:**
  
In SharePoint 2013 the backup and restore process for all Search service application databases with SQL Server tools is limited to the following specific scenarios:
  
- Backup and Restore of the Search Administration database can be done for configuration migration or upgrade activity.
    
- Perform a backup and restore of Search service application databases only when the SharePoint farm is fully stopped. When the SharePoint farm is stopped you can back up the farm to snapshots or make a backup with SQL Server tools to ensure the search indexes are synchronized with the search databases. Note that a restore must include all of this backup set.
    
- We do not support restoring search database backups that are not synchronized with the search indexes. This might result in unexpected search experiences and has a high risk of search index corruption. You should perform all database backups within the same time frame to avoid databases that are out of sync with each other.
    
**Search Administration database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_DB_\<GUID\>  <br/> |
|Location requirements  <br/> |The Administration database should fit into RAM on the server so that the server can handle the end-user query load most efficiently. Because of this requirement, it is usually best not to have the Administration and Crawl databases located on the same server.  <br/> |
|General size information and growth factors  <br/> |Medium. The factors that influence growth include the number of best bets, the number of content sources and crawl rules, the security descriptions for the corpus, and how much traffic.  <br/> |
|Read/write characteristics  <br/> |Equal read/write ratio  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. Scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
**Analytics Reporting database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_AnalyticsReportingStoreDB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Medium to large.  <br/> |
|Read/write characteristics  <br/> |Write heavy during nightly analytics update.  <br/> |
|Recommended scaling method  <br/> |Scale out by creating additional Analytics Reporting database using a split operation when the main database becomes \>200 GB.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
**Crawl database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_CrawlStoreDB_\<GUID\>  <br/> |
|General size information and growth factors  <br/> |Medium.  <br/> |
|Read/write characteristics  <br/> |Read heavy.  <br/> |
|Recommended scaling method  <br/> |Scale out by creating additional Crawl database per every 20 million items crawled.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
**Link database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_LinkStoreDB_\<GUID\>  <br/> |
|Location requirements  <br/> |We recommend that if you have sites that have heavy traffic, the Link database should use separate spindles from other databases.  <br/> |
|General size information and growth factors  <br/> |Medium to Large. The Link database grows on disk by 1 GB per 1 million documents fed. The click through data grows linearly with query traffic, 1 GB per million queries.  <br/> |
|Read/write characteristics  <br/> |Write heavy during content processing.  <br/> |
|Recommended scaling method  <br/> |Scale out by creating additional Link database per every 60 million documents crawled. Also add additional Link database per 100 million expected queries per year.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
### Secure Store Service database
<a name="Sec2"> </a>

The Secure Store Service application database stores and maps credentials, such as account names and passwords.
  
**Secure Store database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Secure_Store_Service_DB_\<GUID\>  <br/> |
|Location requirements  <br/> |For secure credential storage, we recommend that the Secure Store database be hosted on a separate database instance or database server that has access limited to one administrator. By default, if the database is hosted on the default SharePoint database server and instance, all database administrators will have access to the Secure Store database.  <br/> |
|General size information and growth factors  <br/> |Small. Size and growth are determined by the number of target applications, number of credential fields per target application, and the number of users stored in each target application. If auditing is turned on, the number of read and write operations performed against a given target application also affects size.  <br/> |
|Read/write characteristics  <br/> |Equal read/write ratio  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Usage and Health Data Collection database
<a name="Sec2"> </a>

The Usage and Health Data Collection database is used by the Usage and Health Data Collection service application. It stores health monitoring and usage data temporarily, and can be used for reporting and diagnostics. The Usage and Health Data Collection database is the only SharePoint database that supports schema modifications.
  
**Usage database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |SharePoint Servers 2019 and 2016 = WSS_Logging  <br/> SharePoint 2013 = SharePoint_Logging  <br/> |
|Location requirements  <br/> |The Usage and Health Data Collection database is very active, and should be put on a separate disk or spindle, if it is possible.  <br/> |
|General size information and growth factors  <br/> |Extra large. Database size depends on the retention factor, number of items enabled for logging and external monitoring, how many Web applications are running in the environment, how many users are currently working, and which features are enabled.  <br/> |
|Read/write characteristics  <br/> |Write-heavy  <br/> |
|Recommended scaling method  <br/> |Must scale-up. That is, the database must grow larger, because only one Usage and Health Data Collection service application instance is supported per farm.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
### Subscription Settings Service database
<a name="Sec2"> </a>

The Microsoft SharePoint Foundation Subscription Settings service application database stores features and settings for hosted customers. The Subscription Settings service application and database are not created by the SharePoint Products Configuration Wizard — they must be created by using PowerShell cmdlets or SQL Server. For more information, see [New-SPSubscriptionSettingsServiceApplication](/powershell/module/sharepoint-server/New-SPSubscriptionSettingsServiceApplication?view=sharepoint-ps).
  
**Subscription Settings database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the PowerShell **New-SPSubscriptionSettingsServiceApplication** cmdlet  <br/> |SettingsServiceDB  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small. Size is determined by the number of tenants, farms, and features supported.  <br/> |
|Read/write characteristics  <br/> |The subscription database is read-heavy.  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### SharePoint User Profile service application databases
<a name="Sec2"> </a>

The User Profile service has three databases that support SharePoint Servers 2019 and 2016. The three User Profile service databases are shown in the following list. The tables that follow the list display the relevant database information.
  
- **Profile:** The Profile database stores and manages users and associated information. It also stores information about a user's social network in addition to memberships in distribution lists and sites. 
    
- **Synchronization:** The Synchronization database stores configuration and staging data for use when profile data is being synchronized with directory services such as Active Directory. 
    
- **Social Tagging:** The Social Tagging database stores social tags and notes created by users, alongside their respective URLs. 
    
**Profile database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_ProfileDB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Medium to large. Growth factors include additional users and the use of news feeds. News feeds grow with user activities. The default is to maintain the last two weeks of activity, after which a time job deletes the news feed items older than two weeks.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
**Synchronization database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_SyncDB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Medium to large. Growth factors include the number of users, groups, and the ratio of users to groups.  <br/> |
|Read/write characteristics  <br/> |Equal read/write ratio.  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
**Social Tagging database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_SocialDB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small to extra-large. Growth factors include the number of tags, ratings, and notes that have been created and used.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
### Word Automation Services service application database
<a name="Sec2"> </a>

The Word Automation Services database stores information about pending and completed document conversions and updates. The Word Automation Services Timer Job processes and distributes this information as queued conversion job items to application servers.
  
**Word Automation Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |WordAutomationServices_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Read-heavy, once per conversion item.  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Managed Metadata Service service application database
<a name="Sec2"> </a>

The Managed Metadata service application database stores managed metadata and syndicated content types. Managed metadata consists of terms in a hierarchical structure that can be used for tagging content and building site collections.
  
 **Important:**
  
The Managed Metadata Service is the taxonomy service and provides the Term Store Management Tool in the SharePoint Central Administration website. This tool can also be accessed from each site collection. You can navigate there using the Site Settings menu, and clicking **Term Store Management**.
  
The Managed Metadata service application database stores the taxonomy, (terms, structure, and metadata). The Managed Metadata Service is also required for content type syndication, even though this is not a feature of the service, most organizations deploy Managed Metadata using content types so the two are often deployed together.
  
**Managed Metadata database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |Managed Metadata Service_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Medium. Growth factors include the amount of managed metadata.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. Scale out by creating additional instances of the service application  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### SharePoint Translation Services service application database
<a name="Sec2"> </a>

The Machine Translation Services stores information about pending and completed batch document translations with file extensions that are enabled.
  
**Machine Translation Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |TranslationService_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. You can scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale, requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Project Server service application database
<a name="Sec2"> </a>

> [!IMPORTANT]
> The Project Server service application database is only found in SharePoint Server 2013. Project Servers 2019 and 2016 don't create a database in SharePoint Server but use the Content database (WSS_Content). 
  
Project Server creates a separate database for each instance of Project Web App. Each Project Web App database contains the following data:
  
- All Project and Portfolio Management (PPM) data
    
- Time tracking and Timesheet data
    
- Aggregated SharePoint project site data
    
**Project Server database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |ProjectWebApp  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small to medium.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the SQL Server that hosts the Project Web App database. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server 2013 backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### SQL Server Power Pivot Service service application database
<a name="Sec2"> </a>

The Power Pivot Service database stores data refresh schedules, and Power Pivot usage data that is copied from the central usage data collection database.
  
When being used, Power Pivot stores additional data in content databases and in the Central Administration Content database (WSS_Content).
  
 **Important:**
  
- SQL Server Power Pivot for SharePoint Server 2016 requires SQL Server2016 CTP 3.1 or later Analysis Services (SSAS), Business Intelligence or Enterprise edition.
    
- SQL Server 2012 Power Pivot for SharePoint 2013 requires SQL Server 2012 Analysis Services (SSAS), Business Intelligence or Enterprise edition.
    
**Power Pivot database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |DefaultPowerPivotServiceApplicationDB_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### PerformancePoint Services service application database
<a name="Sec2"> </a>

The PerformancePoint Services database stores temporary objects and persisted user comments and settings.
  
**PerformancePoint Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |PerformancePoint Service Application _\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Small.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database that supports the service application instance. Scale out by creating additional instances of the service application, however, the decision to create a separate service application is likely to be based on business, rather than scale requirements.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### State Service service application database
<a name="Sec2"> </a>

The State Service database stores temporary state information for InfoPath Forms Services, Exchange Server, the chart Web Part, and Visio Services.
  
**State Service database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when installed by using the SharePoint Products Configuration Wizard  <br/> |StateService_\<GUID\>  <br/> |
|Location requirements  <br/> |None  <br/> |
|General size information and growth factors  <br/> |Medium to large, depending on usage of features that store data in the State Service database.  <br/> |
|Read/write characteristics  <br/> |Read-heavy  <br/> |
|Recommended scaling method  <br/> |Scale out by creating another State Service database with Microsoft PowerShell cmdlets.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SharePoint Server backup and restore, PowerShell, and SQL Server.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
## SQL Server system databases
<a name="Sec3"> </a>

SharePoint Server is built on SQL Server and uses the SQL Server system databases. SQL Server does not let users directly update information in system objects such as system tables, system stored procedures, and catalog views. Instead, SQL Server provides a complete set of administrative tools that let users fully administer their system and manage all users and objects in a database. For more information about the SQL Server system databases, see [System Databases](http://go.microsoft.com/fwlink/p/?LinkID=733887&amp;clcid=0x409).
  
### master database

The master database records all the system-level information for a SQL Server instance. This includes logins, configurations, and other databases.
  
**master**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |master  <br/> |
|Location requirements  <br/> |The master database must be located on the same SQL Server instance that SharePoint uses.  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Varies  <br/> |
|Recommended scaling method  <br/> |Scale-up. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
### model database

The model database is used as the template for all databases created on the SQL Server instance. Any modifications made to the model database are also applied to all databases created afterward.
  
**model**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |model  <br/> |
|Location requirements  <br/> |The model database must be located on the same SQL Server instance that SharePoint uses.  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Varies  <br/> |
|Recommended scaling method  <br/> |Scale-up. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### msdb database

The msdb database is used by SQL Server Agent for scheduling alerts and jobs.
  
**msdb**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |msdb  <br/> |
|Location requirements  <br/> |The msdb database must be located on the same SQL Server instance that SharePoint uses.  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Varies  <br/> |
|Recommended scaling method  <br/> |Scale-up. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
### tempdb database

The tempdb database holds temporary objects or intermediate result sets. For example, it holds all temporary tables, temporary stored procedures, and any other temporary storage needs. The tempdb is recreated every time SQL Server starts.
  
**tempdb**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |tempdb  <br/> |
|Location requirements  <br/> |Locate on a fast disk, on a separate spindle from other databases. Create as many files as needed to maximize disk bandwidth. Using multiple files reduces tempdb storage contention and yields significantly better scalability. However, do not create too many files because this can decrease performance and increase management overhead. As a general guideline, create one data file for each CPU on the server and adjust the number of files up or down as necessary. Note that a dual-core is two CPUs.  <br/> |
|General size information and growth factors  <br/> |Medium, depending on activities such as how many users are using the system, in addition to the specific processes that are running. For example, online rebuilds of large indexes, or large sorts cause the database to grow quickly.  <br/> |
|Read/write characteristics  <br/> |Varies  <br/> |
|Recommended scaling method  <br/> |Scale-up. (Significant growth is unlikely.)  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Simple  <br/> |
   
## SQL Server Reporting Services databases
<a name="Sec4"> </a>

The following SQL Server Reporting Services (SSRS) can be used as part of a SharePoint Server 2016 deployment.
  
 **Important:**
  
If you are running Access Services in SharePoint Server 2013, then SQL Server 2012 is required. The requirements for Reporting Services depend on the mode in which you are running, as follows:
  
- Local mode requires only SharePoint Server 2013 and the SQL Server Reporting Services Add-in.
    
- Connected mode requires SharePoint Server 2013, the SSRS Add-in, and SQL Server 2016, available in Standard or Enterprise Edition.
    
### Report Server Catalog database

The SQL Server Reporting Services Report Server Catalog database stores all report metadata including report definitions, report history and snapshots, and scheduling information. When Report Server Catalog is used, report documents are stored in SharePoint content databases.
  
**Report Server Catalog**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |ReportingService_\<GUID\>  <br/> |
|Location requirements  <br/> |Must be located on the same database server as the ReportServerTempDb database.  <br/> |
|General size information and growth factors  <br/> |Small  <br/> |
|Read/write characteristics  <br/> |Read heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### ReportServerTempDB database

The SQL Server Reporting Services ReportServerTempDB database stores all the temporary snapshots while reports are running.
  
**ReportServerTempDB**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |ReportingService_\<GUID\>_TempDB  <br/> |
|Location requirements  <br/> |Must be located on the same database server as the Report Server Catalog database.  <br/> |
|General size information and growth factors  <br/> |This database size varies and goes from small to extra-large frequently. The size depends on use of cached report snapshots.  <br/> |
|Read/write characteristics  <br/> |Read heavy  <br/> |
|Recommended scaling method  <br/> |Scale-up the database.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore, but we do not recommend that you back up this database.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
### Report Server Alerting database

The Report Server Alerting database stores all Data Alerts metadata and runtime information that is required to produce Data Alerts for Reporting Services operational reports. Data from reports is processed in the database to match rules that are defined in Alert Definitions.
  
**Report Server Alerting**

|**Category**|**Description**|
|:-----|:-----|
|Default database name  <br/> |ReportingService_\<GUID\>_Alerting  <br/> |
|Location requirements  <br/> |Must be located on the same database server as the Report Server Catalog database.  <br/> |
|General size information and growth factors  <br/> |This database size varies and goes from small to extra-large frequently. The size depends on use of Data Alerts.  <br/> |
|Read/write characteristics  <br/> |Equal read heavy and write heavy.  <br/> |
|Recommended scaling method  <br/> |Scale-up to optimize the file I/O and memory usage.  <br/> |
|Associated Health rules  <br/> |None  <br/> |
|Supported backup tools  <br/> |SQL Server backup and restore.  <br/> |
|Default recovery model  <br/> |Full  <br/> |
   
## See also
<a name="Sec4"> </a>

#### Concepts

[Technical reference for SharePoint Server](technical-reference.md)
  
[Manage databases in SharePoint Server](../administration/database-management.md)
#### Other Resources

[SQL Server 2017](https://www.microsoft.com/en-us/sql-server/sql-server-2017)

[SQL Server 2016](https://www.microsoft.com/en-us/sql-server/sql-server-2016)
  
[SQL Server 2014 Service Pack 1 release information](https://support.microsoft.com/en-us/kb/3058865)

