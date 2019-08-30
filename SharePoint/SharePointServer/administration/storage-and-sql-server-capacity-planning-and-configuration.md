---
title: "Storage and SQL Server capacity planning and configuration (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: a96075c6-d315-40a8-a739-49b91c61978f
description: "Learn how to plan and configure the storage and database tier for SQL Server in SharePoint Server."
---

# Storage and SQL Server capacity planning and configuration (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The capacity planning information that we provide contains guidelines to help you plan and configure the storage and SQL Server database tier in a SharePoint Server environment. This information is based on testing performed at Microsoft on live properties. However, your results may vary based on the equipment you use and the features and functionality that you implement for your sites. 
  
Although tests were not run on SQL Server 2014 (SP1), SQL Server 2016 , or SQL Server 2017 RTM you can use these test results as a guide to help you plan for and configure the storage and SQL Server database tier in SharePoint Server 2019, 2016, and 2019 environments. For training about how to configure and tune SQL Server 2012, see [SQL Server 2012 for SharePoint Server 2013](#Section8A). Note that the test results are the same as in SharePoint 2013.  
  
Because SharePoint Server often runs in environments in which databases are managed by separate SQL Server database administrators, this document is intended for joint use by SharePoint Server farm implementers and SQL Server database administrators. It assumes significant understanding of both SharePoint Server and SQL Server.
  
This article assumes that you are familiar with the concepts that are presented in [Capacity management and sizing for SharePoint Server 2013](capacity-management-and-sizing-for-sharepoint-server-2013.md).
  
## Design and configuration process for SharePoint Servers 2016 and 2019 storage and database tier

We recommend that you break the storage and database tier design process into the following steps. These sections provide detailed information about each design step, including storage requirements and best practices:
  
1. [Gather storage and SQL Server space and I/O requirements](#Section1)
    
2. [Choose SQL Server version and edition](#Section2)
    
3. [Design storage architecture based on capacity and I/O requirements](#Section3)
    
4. [Estimate memory requirements](#Section4)
    
5. [Understand network topology requirements](#Section5)
    
6. [Configure SQL Server](#Section6)
    
7. [Validate and monitor storage and SQL Server performance ](#Section7)
    

<a name="Section1"> </a>
## Gather storage and SQL Server space and I/O requirements

Several SharePoint Server architectural factors influence storage design. The key factors are: the amount of content, enabled features, deployed service applications, number of farms, and availability requirements.
  
Before you start to plan storage, you should understand the databases that SharePoint Server can use. 
  
In this section:
  
- [Databases used by SharePoint Server](#section1a)
    
- [Understand SQL Server and IOPS](#Section1_5a)
    
- [Estimate core storage and IOPS needs](#sectoin1b)
    
- [Estimate service application storage needs and IOPS](#section1c)
    
- [Determine availability needs](#Section1d)
    

<a name="section1a"> </a>
### Databases used by SharePoint Server

The databases that are installed with SharePoint Servers 2016 and 2019 depend on the service applications that are used in the environment. All SharePoint Server environments rely on the SQL Server system databases. This section provides a summary of the databases installed with SharePoint Servers 2016 and 2019. For detailed database information, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md). 
  
Some SharePoint Server, SQL Server Database Engine, and SQL Server Reporting Services (SSRS) databases have specific location recommendations or requirements. For information about these database locations, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md). The **Quick reference guide: SharePoint Servers 2016 and 2019 Databases**, is available to download as either a [PDF](http://download.microsoft.com/download/7/9/7/79700E8E-9896-4657-B9E6-4940B295B71A/DBrefguideSPS2019_tabloid.pdf) or [Visio](http://download.microsoft.com/download/7/9/7/79700E8E-9896-4657-B9E6-4940B295B71A/DBrefguideSPS2019_tabloid.vsdx) file.  
  
The following databases are the SharePoint Server system databases and are installed automatically.
  
- Configuration
    
- Central Administration content
    
- Content (one or more)
    
The following list shows the SharePoint Server service applications that have databases:
  
- App Management Service
    
- Apps for SharePoint
    
- Business Data Connectivity
    
- Managed Metadata
    
- PerformancePoint Services
    
- Project Server (SharePoint Server 2013 only)
    
- Search Service
    
  - Search Administration
    
  - Analytics Reporting
    
  - Crawl
    
  - Link
    
- Secure Store Service
    
- SharePoint Translation Service
    
- SQL Server Power Pivot Service
    
- State Service
    
- Subscription Settings Service
    
- Usage and Health data collection
    
- User Profile Service
    
  - Profile
    
  - Social Tagging
    
  - Synchronization
    
- Word Automation Services
    
The following list shows the SharePoint Foundation 2013 databases:
  
- Configuration
    
- Central Administration content
    
- Content (one or more)
    
- App Management Service
    
- Search service application:
    
  - Search administration
    
  - Analytics Reporting (one or more)
    
  - Crawl (one or more)
    
  - Link (one or more)
    
- Secure Store Service
    
- Subscription Settings Service Application (if enabled through Windows PowerShell)
    
- Usage and Health Data Collection Service
    
- Word Conversion Service
    
If you are integrating further with SQL Server, your environment may also include additional databases, as in the following scenario. SQL Server Power Pivot for SharePoint can be used in a SharePoint Server 2016 environment only if you use SQL Server 2016 RTM Enterprise Edition and SQL Server 2016 SQL Server Analysis Services (SSAS). If in use, you must also plan to support the Power Pivot application database, and the additional load on the system. For more information, download the new [Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016](http://go.microsoft.com/fwlink/p/?LinkID=717977&amp;clcid=0x409) white paper. For details about configuring and deploying business intelligence in a multiple server SharePoint Server 2016 farm, download [Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm](http://go.microsoft.com/fwlink/p/?LinkID=723106&amp;clcid=0x409).
  
The SQL Server 2016 Reporting Services (SSRS) add-in can be used with any SharePoint Server 2016 environment. If you are using the add-in, plan to support the two SQL Server Reporting Services databases and the additional load that is required for SQL Server Reporting Services.
  
- SQL Server 2012 Power Pivot for SharePoint 2013 can be used in a SharePoint 2013 environment that includes SQL Server 2008 R2 Enterprise Edition and SQL Server Analysis Services. If in use, you must also plan to support the Power Pivot application database, and the additional load on the system. For more information, see [Plan a PowerPivot deployment in a SharePoint farm](https://go.microsoft.com/fwlink/p/?LinkID=186698) and the SQL Server PRO article [Understanding PowerPivot and Power View in Microsoft Excel 2013](https://go.microsoft.com/fwlink/p/?LinkId=317240).
    
- The SQL Server 2008 R2 Reporting Services (SSRS) plug-in can be used with any SharePoint 2013 environment. If you are using the plug-in, plan to support the two SQL Server 2008 R2 Reporting Services databases and the additional load that is required for SQL Server 2008 R2 Reporting Services.
 
> [!NOTE]
> SQL Server Reporting Services integration with SharePoint Server 2019 is no longer supported. For more information, see [Reporting Services Report Server (SharePoint Mode)](/sql/reporting-services/report-server-sharepoint/reporting-services-report-server-sharepoint-mode?view=sql-server-2016&viewFallbackFrom=sql-server-2017) and [Supported combinations of SharePoint and Reporting Services server](/sql/reporting-services/install-windows/supported-combinations-of-sharepoint-and-reporting-services-server?view=sql-server-2016).
    

<a name="Section1_5a"> </a>
### Understand SQL Server and IOPS

On any server that hosts a SQL Server instance, it is very important that the server achieve the fastest response possible from the I/O subsystem.
  
More and faster disks or arrays provide sufficient I/O operations per second (IOPS) while maintaining low latency and queuing on all disks.
  
You cannot add other types of resources, such as CPU or memory, to compensate for slow response from the I/O subsystem. However, it can influence and cause issues throughout the farm. Plan for minimal latency before deployment, and monitor your existing systems.
  
Before you deploy a new farm, we recommend that you benchmark the I/O subsystem by using the Diskspd Utility . Note that this tool works on all Windows Server versions with all versions of SQL Server. For more information, see [Diskspd Utility: A Robust Storage Testing Tool](http://go.microsoft.com/fwlink/?LinkID=797803&amp;clcid=0x409).
  
Stress testing also provides valuable information for SQL Server. For information, see [Storage Benchmarking with DiskSpd](http://go.microsoft.com/fwlink/?LinkID=797804&amp;clcid=0x409).
  
For detailed information about how to analyze IOPS requirements from a SQL Server perspective, see [Analyzing I/O Characteristics and Sizing Storage Systems for SQL Server Database Applications](http://go.microsoft.com/fwlink/p/?LinkId=317242).
  

<a name="sectoin1b"> </a>
### Estimate core storage and IOPS needs

Configuration and content storage and IOPS are the base layer that you must plan for in every SharePoint Server deployment. 
  

<a name="Section1b1"> </a>
#### Configuration storage and IOPS

Storage requirements for the Configuration database and the Central Administration content database are not large. We recommend that you allocate 2 GB for the Configuration database and 1 GB for the Central Administration content database. Over time, the Configuration database may grow beyond 1 GB. It does not grow quickly — it grows by approximately 40 MB for each 50,000 site collections. 
  
Transaction logs for the Configuration database can be large. Therefore, we recommend that you change the recovery model for the database from full to simple.
  
> [!NOTE]
> If you want to use SQL Server database mirroring to provide availability for the Configuration database, you must use the full recovery model. 
  
IOPS requirements for the Configuration database and Central Administration content database are minimal.
  
#### Content storage and IOPS
<a name="Section1b2"> </a>

Estimating the storage and IOPS required for content databases is not a precise activity. In testing and explaining the following information, we intend to help you derive estimates to use to determine the initial size of your deployment. However, when your environment is running, we expect that you'll revisit your capacity needs based on the data from your live environment. 
  
For more information about our overall capacity planning methodology, see [Capacity management and sizing for SharePoint Server 2013](capacity-management-and-sizing-for-sharepoint-server-2013.md).
  
#### Formula to estimate content database storage

The following process describes how to approximately estimate the storage required for content databases, without considering log files:
  
1. Use the following formula to estimate the size of your content databases:
    
    Database size = ((D × V) × S) + (10 KB × (L + ( V × D)))
    
    > [!NOTE]
    > The value, 10 KB, in the formula is a constant that approximately estimates the amount of metadata required by SharePoint Server. If your system requires significant use of metadata, you may want to increase this constant. 
  
2. Calculate the expected number of documents. This value is known as D in the formula. 
    
    How you calculate the number of documents will be determined by the features that you are using. For example, for My Sites or collaboration sites, we recommend that you calculate the expected number of documents per user and multiply by the number of users. For records management or content publishing sites, you may calculate the number of documents that are managed and generated by a process. 
    
    If you are migrating from a current system, it may be easier to extrapolate your current growth rate and usage. If you are creating a new system, review your existing file shares or other repositories and estimate based on that usage rate.
    
3. Estimate the average size of the documents that you'll be storing. This value is known as S in the formula. It may be worthwhile to estimate averages for different types or groups of sites. The average file size for My Sites, media repositories, and different department portals can vary significantly. 
    
4. Estimate the number of list items in the environment. This value is known as L in the formula. 
    
    List items are more difficult to estimate than documents. We generally use an estimate of three times the number of documents (D), but this will vary based on how you expect to use your sites. 
    
5. Determine the approximate number of versions. Estimate the average number of versions any document in a library will have. This value will usually be much lower than the maximum allowed number of versions. This value is known as V in the formula. 
    
    The value of V must be above zero. 
    
As an example, use this formula and the characteristics in the following table to estimate the required storage space for data files in a content database for a collaboration environment. The result is that you need approximately 105 GB.
  
|**Input**|**Value**|
|:-----|:-----|
|Number of documents (D)  <br/> |200,000  <br/> Calculated by assuming 10,000 users times 20 documents  <br/> |
|Average size of documents (S)  <br/> |250 KB  <br/> |
|List items (L)  <br/> |600,000  <br/> |
|Number of non-current versions (V)  <br/> |2  <br/> Assuming that the maximum versions allowed is 10  <br/> |
   
Database size = (((200,000 x 2)) × 250) + ((10 KB × ( 600,000 + ( 200,000 x 2))) = 110,000,000 KB or 105 GB 
  
> [!NOTE]
> Efficient File I/O in SharePoint Server is a storage method in which a file is split into pieces that are stored and updated separately. These pieces are streamed together when a user requests the file. This increases the I/O performance but it normally does not increase the file size. However, small files can see a small increase in the disk storage that is required. 
  
#### Features that influence the size of content databases

The following SharePoint Server features can significantly affect the size of content databases:
  
- **Recycle bins** Until a document is fully deleted from both the first stage and second stage recycle bin, it occupies space in a content database. Calculate how many documents are deleted each month to determine the effect of recycle bins on the size of content databases. 
    
- **Auditing** Audit data can quickly compound and use large amounts of space in a content database, especially if view auditing is turned on. Rather than letting audit data grow without constraint, we recommend that you enable auditing only on the events that are important to meet regulatory needs or internal controls. Use the following guidelines to estimate the space that you must reserve for auditing data: 
    
  - Estimate the number of new auditing entries for a site, and multiply this number by 2 KB (entries generally are limited to 4 KB, with an average size of about 1 KB).
    
  - Based on the space that you want to allocate, determine the number of days of audit logs you want to keep.
    
> [!NOTE]
> Office Online Server is the next version of Office Web Apps Server. Using Office Online Server with SharePoint Servers 2016 and 2019 doesn't affect the size of the content database. To deploy Office Online Server in your SharePoint Server 2016 farm, see [Deploy Office Online Server](/officeonlineserver/deploy-office-online-server). 
  
#### Estimate content database IOPS requirements

IOPS requirements for content databases vary significantly based on how your environment is being used, available disk space, and the number of servers that you have. In general, we recommend that you compare the predicted workload in your environment to one of the solutions that we tested. For more information, see [Performance and capacity test results and recommendations (SharePoint Server 2013)](performance-and-capacity-test-results-and-recommendations-for-sharepoint-2013.md).
  
In tests, we found that the content databases tend to range from 0.05 IOPS/GB to around 0.2 IOPS/GB. We also found that a best practice is to increase the top-end to 0.5 IOPS/GB. This is more than necessary and can be much more than you'll need in your environment. Note that if you use mirroring, this results in much more IO than the primary content databases. Simply be aware that the mirrored content databases are never lightweight.
  

<a name="section1c"> </a>
### Estimate service application storage needs and IOPS

After you estimate content storage and IOPS needs, you must determine the storage and IOPS required by the service applications that are being used in your environment. 
  
#### SharePoint Server service application storage and IOPS requirements
<a name="Section1c2"> </a>

To estimate the storage requirements for the service applications in the system, you must first be aware of the service applications and how you'll use them. Service applications that are available in SharePoint Server 2016 and that have databases are listed in the following tables. The storage and IOPs data for all of the service applications in SharePoint Servers 2016 and 2019 remains the same as in SharePoint Servers 2010 and 2013.
  
**Search service application storage and IOPS requirements**

|**Database**|**Scaling**|**Disk IOPS**|**Disk size**|**10M items**|**100M items**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Crawl  <br/> |One DB per 20M items  <br/> SQL IOPS: 10 per 1 DPS  <br/> |Medium/High  <br/> |Medium  <br/> |15GB  <br/> 2GB log  <br/> |110GB  <br/> 50GB log  <br/> |
|Link  <br/> |One DB per 60M items  <br/> SQL IOPS: 10 per 1M items  <br/> |Medium  <br/> |Medium  <br/> |10GB  <br/> 0.1GB log  <br/> |80GB  <br/> 5GB log  <br/> |
|Analytics Reporting  <br/> |Split when reaching 100-300GB  <br/> |Medium  <br/> |Medium  <br/> |Usage dependent  <br/> |Usage dependent  <br/> |
|Search Administration  <br/> |One DB  <br/> |Low  <br/> |Low  <br/> |0.4GB  <br/> 1GB log  <br/> |1GB data  <br/> 2GB log  <br/> |
   
**Service application storage requirements and IOPS recommendations**

|**Service application**|**Size estimation recommendation**|
|:-----|:-----|
|User Profile  <br/> |The User Profile service application is associated with three databases: Profile, Synchronization, and Social Tagging.  <br/> **Note:** The testing for the User Profile database storage requirements and IOPS recommendations is not yet complete. Check back for additional information.  <br/> For User Profile database information, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md).  <br/> |
|Managed Metadata Service  <br/> |The Managed Metadata service application has one database. The size of the database is affected by the number of content types and keywords used in the system. Many environments will include multiple instances of the Managed Metadata service application.  <br/> |
|Secure Store Service  <br/> |The size of the Secure Store service application database is determined by the number of credentials in the store and the number of entries in the audit table. We recommend that you allocate 5 MB for each 1,000 credentials for it. It has minimal IOPS.  <br/> |
|State Service  <br/> |The State service application has one database. We recommend that you allocate 1 GB for it. It has minimal IOPS.  <br/> |
|Word Automation Services  <br/> |The Word Automation service application has one database. We recommend that you allocate 1 GB for it. It has minimal IOPS.  <br/> |
|PerformancePoint Services  <br/> |The PerformancePoint service application has one database. We recommend that you allocate 1 GB for it. It has minimal IOPS.  <br/> |
|Business Data Connectivity service  <br/> |The Business Data Connectivity service application has one database. This database is small and significant growth is unlikely. It has minimal IOPS.  <br/> |
|App Management  <br/> |The App Management service application has one database. This database is small and significant growth is unlikely. It has minimal IOPS.  <br/> |
|Power Pivot  <br/> |The Power Pivot Service application has one database. This database is small and has no significant I/O impact. We recommend that you use the same IOPS as the SharePoint content database. Note that content databases have significantly higher I/O requirements than the Power Pivot service application database.  <br/> |
   

<a name="Section1d"> </a>
### Determine availability needs

Availability is how much a SharePoint Server 2016 environment is perceived by users to be available. An available system is a system that is resilient — that is, incidents that affect service occur infrequently, and timely and effective action is taken when they do occur. 
  
Availability requirements can significantly increase your storage needs. For detailed information, see [Create a high availability architecture and strategy for SharePoint Server](plan-for-high-availability.md). Also, see the SQL Server 2012 white paper [AlwaysOn Architecture Guide: Building a High Availability and Disaster Recovery Solutions by Using AlwaysOn Availability Groups](https://go.microsoft.com/fwlink/p/?LinkId=317243).
  
<a name="Section2"> </a>
## Choose SQL Server version and edition

We recommend that for SharePoint Servers 2016 and 2019 you consider running your environment on the Enterprise Edition of the following SQL Servers to take advantage of the additional performance, availability, security, and management capabilities that these versions provide. 

- SQL Server 2014 with Service Pack 1 (SP1) (SharePoint Server 2016 only)
 
- SQL Server 2016 (SharePoint Servers 2016 and 2019)
 
- SQL Server 2017 RTM (SharePoint Servers 2016 and 2019) 
 
For more information about the benefits of these versions, see [Features Supported by the Editions of SQL Server 2014](http://go.microsoft.com/fwlink/?LinkID=808793&amp;clcid=0x409), [Editions and supported features of SQL Server 2016](http://go.microsoft.com/fwlink/?LinkID=524888&amp;clcid=0x409), and [Editions and supported features of SQL Server 2017](https://go.microsoft.com/fwlink/?linkid=865116).
  
We recommend that for SharePoint Server 2013 you consider running your environment on the Enterprise Edition of SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, or SQL Server 2014 to take advantage of the additional performance, availability, security, and management capabilities that these versions provide. For more information about the benefits of SQL Server 2008 R2 with SP1, SQL Server 2012, and SQL Server 2014 Enterprise Edition, see [Features Supported by the Editions of SQL Server 2014](http://go.microsoft.com/fwlink/?LinkID=808793&amp;clcid=0x409), [Features Supported by the Editions of SQL Server 2012](/previous-versions/sql/sql-server-2012/cc645993(v=sql.110)), and [Features Supported by the Editions of SQL Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkId=317246).
  
In particular, you should consider your need for the following features: 
  
- **Backup compression** Backup compression can speed up any SharePoint backup, and is available in every edition of SQL Server 2008 and later. By setting the compression option in your backup script, or by configuring the server that is running SQL Server to compress by default, you can significantly reduce the size of your database backups and shipped logs. For more information, see [Backup Compression (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=717243&amp;clcid=0x409) for SQL Server 2014 and [Backup Compression (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=808797&amp;clcid=0x409) for SQL Server 2016 and SQL Server 2017 RTM. 
    
    > [!NOTE]
    > SQL Server data compression is not supported for SharePoint Server, except for the Search service application databases. 
  
- **Transparent data encryption** If your security requirements include the need for transparent data encryption, you must use SQL Server Enterprise Edition. 
    
- **Content deployment** If you plan to use the content deployment feature, consider SQL Server Enterprise Edition so that the system can take advantage of database snapshots. 
    
    > [!NOTE]
    > If you are using a Remote BLOB storage provider that does not support database snapshots, you can't use snapshots for content deployment or backup. 
  
- **Remote BLOB storage** If you want to take advantage of remote BLOB storage to a database or location outside the files associated with each content database, you must use the Enterprise Edition of: 
  
  **SharePoint Server 2019**

    - SQL Server 2016

    - SQL Server 2017 RTM
 
  **SharePoint Server 2016**

    - SQL Server 2014 (SP1) 

    - SQL Server 2016 
 
    - SQL Server 2017 RTM 
     
  **SharePoint 2013**

    - SQL Server 2008 R2 with SP1 

    - SQL Server 2012 Enterprise Edition 
    
- **Resource governor** Resource Governor is a technology introduced in SQL Server 2008 to enable you to manage SQL Server workloads and resources by specifying limits on resource consumption by incoming requests. Resource Governor enables you to differentiate workloads and allocate CPU and memory as they are requested, based on the limits that you specify. For more information about how to use Resource Governor, see [Resource Governor](https://msdn.microsoft.com/en-us/library/bb933866%28v=sql.120%29.aspx) for SQL Server 2014 and [Resource Governor](http://go.microsoft.com/fwlink/?LinkID=808798&amp;clcid=0x409) for SQL Servers 2016 and 2019. 
    
    We recommend that you use Resource Governor with SharePoint Server to:
    
  - Limit the amount of SQL Server resources that the web servers targeted by the search crawl component consume. As a best practice, we recommend limiting the crawl component to 10 percent CPU when the system is under load.
    
  - Monitor how many resources are consumed by each database in the system — for example, you can use Resource Governor to help you determine the best placement of databases among computers that are running SQL Server. 
    
- **Microsoft Power Pivot for SharePoint** Enables users to share and collaborate on user-generated data models and analysis in Excel on the web while automatically refreshing those analyses. You must have Office on the web to use Excel on the web with Power Pivot for SharePoint and SharePoint Server 2016. You can use SQL Server 2014 (SP1) or SQL Server 2016 RTM Enterprise Edition and SQL Server Analysis Services for business intelligence with SharePoint Server 2016. However, you can only use Power Pivot for SharePoint with SQL Server 2016 RTM, not with SQL Server 2014 (SP1). 
    
- **Power Pivot for SharePoint 2013** Enables users to share and collaborate on user-generated data models and analysis in Excel and in the browser while automatically refreshing those analyses. It is part of SQL Server 2008 R2 Analysis Services (SSAS) Datacenter and Enterprise Edition, SQL Server 2012 SP1 Analysis Services (SSAS) Enterprise Edition, and SQL Server 2014 Analysis Services (SSAS) Enterprise and Business Intelligence Edition. 
    
<a name="Section3"> </a>
## Design storage architecture based on capacity and I/O requirements

The storage architecture and disk types that you select for your environment can affect system performance.
  
In this section:
  
- [Choose a storage architecture](#Section31)
    
- [Choose disk types](#Section32)
    
- [Choose RAID types](#Section33)
    
### Choose a storage architecture
<a name="Section31"> </a>

SharePoint Server supports Direct Attached Storage (DAS), Storage Area Network (SAN), and Network Attached Storage (NAS) storage architectures, although NAS is only supported for use with content databases that are configured to use remote BLOB storage. Your choice depends on factors within your business solution and your existing infrastructure. 
  
Any storage architecture must support your availability needs and perform adequately in IOPS and latency. To be supported, the system must consistently return the first byte of data within 20 milliseconds (ms).
  
#### Direct Attached Storage (DAS)

DAS is a digital storage system that is directly attached to a server or workstation, without a storage network in between. DAS physical disk types include Serial Attached SCSI (SAS) and Serial Attached ATA (SATA).
  
In general, we recommend that you choose a DAS architecture when a shared storage platform can't guarantee a response time of 20 ms and sufficient capacity for average and peak IOPS.
  
#### Storage Area Network (SAN)

SAN is an architecture to attach remote computer storage devices (such as disk arrays and tape libraries) to servers in such a way that the devices appear as locally attached to the operating system (for example, block storage). 
  
In general, we recommend that you choose a SAN when the benefits of shared storage are important to your organization. 
  
The benefits of shared storage include the following:
  
- Easier to reallocate disk storage between servers.
    
- Can serve multiple servers.
    
- No limitations on the number of disks that can be accessed.
    
#### Network Attached Storage (NAS)

A NAS unit is a self-contained computer that is connected to a network. Its sole purpose is to supply file-based data storage services to other devices on the network. The operating system and other software on the NAS unit provide the functionality of data storage, file systems, and access to files, and the management of these functionalities (for example, file storage). 
  
> [!NOTE]
> NAS is only supported for use with content databases that are configured to use remote BLOB storage (RBS). Any network storage architecture must respond to a ping within 1 ms and must return the first byte of data within 20 ms. This restriction does not apply to the local SQL Server FILESTREAM provider, because it only stores data locally on the same server. 
  
> [!NOTE]
> Some confusion exists about if you use the Internet Small Computer System Interface (iSCSI) and assume that it is a NAS protocol. If you access this iSCSI storage through the Common Internet File System (CFIS), it is a NAS protocol. This means that you can't use this storage with content databases if they aren't configured to use RBS. If however, you access this iSCSI storage through a locally attached hard disk, it is considered a SAN architecture. This means that you can use it with NAS. 
  
### Choose disk types
<a name="Section32"> </a>

The disk types that you use in the system can affect reliability and performance. All else being equal, larger drives increase mean seek time. SharePoint Server supports the following types of drives:
  
- Small Computer System Interface (SCSI)
    
- Serial Advanced Technology Attachment (SATA) 
    
- Serial-attached SCSI (SAS)
    
- Fibre Channel (FC)
    
- Integrated Device Electronics (IDE)
    
- Solid State Drive (SSD) or Flash Disk
    
    For information about using solid state drives for storage in SQL Server, see the SQL Server PRO article [Using Solid State Disks in SQL Server Storage Solutions](https://go.microsoft.com/fwlink/p/?LinkId=317258).
    
### Choose RAID types
<a name="Section33"> </a>

RAID (Redundant Array of Independent Disks) is often used to both improve the performance characteristics of individual disks (by striping data across several disks) and to provide protection from individual disk failures.
  
All RAID types are supported for SharePoint Server. However, we recommend that you use RAID 10 or a vendor-specific RAID solution that has equivalent performance. 
  
When you configure a RAID array, make sure that you align the file system to the offset that is supplied by the vendor.
  
For more information about provisioning RAID for SQL Server, see [RAID](https://go.microsoft.com/fwlink/p/?LinkId=317259). 
  
<a name="Section4"> </a>
## Estimate memory requirements

The memory that is required for SharePoint Server is directly related to the size of the content databases that you are hosting on a server that is running SQL Server. 
  
As you add service applications and features, your requirements are likely to increase. The following table gives guidelines for how much memory we recommend.
  
|**Combined size of content databases**|**RAM recommended for computer running SQL Server**|
|:-----|:-----|
|Minimum for small production deployments  <br/> |8 GB  <br/> |
|Minimum for medium production deployments  <br/> |16 GB  <br/> |
|Recommendation for up to 2 terabytes  <br/> |32 GB  <br/> |
|Recommendation for the range of 2 terabytes to 5 terabytes  <br/> |64 GB  <br/> |
|Recommendation for more than 5 terabytes  <br/> |Additional RAM over 64 GB can improve SQL Server caching speed  <br/> |
   
> [!NOTE]
> These values are higher than those recommended as the minimum values for SQL Server because of the distribution of data required for a SharePoint Server environment. For more information about SQL Server system requirements, see [Hardware and Software Requirements for Installing SQL Server 2014](http://go.microsoft.com/fwlink/?LinkID=798764&amp;clcid=0x409) and [Hardware and Software Requirements for Installing SQL Server](http://go.microsoft.com/fwlink/?LinkID=808799&amp;clcid=0x409) for SQL Servers 2016 and 2017. 
  
For information about SQL Server capacity limits and specifications see [Compute Capacity Limits by Edition of SQL Server](http://go.microsoft.com/fwlink/?LinkID=808802&amp;clcid=0x409) and [Maximum Capacity Specifications for SQL Server](http://go.microsoft.com/fwlink/?LinkID=808804&amp;clcid=0x409).
  
Other factors that may influence the memory that is required include the following:
  
- The use of SQL Server mirroring.
    
- The frequent use of files larger than 15 megabytes (MB).
    
<a name="Section5"> </a>
## Understand network topology requirements

Plan the network connections within and between farms. We recommend that you use a network that has low latency.
  
The following list provides some best practices and recommendations:
  
- All servers in the farm should have LAN bandwidth and latency to the server that is running SQL Server. Latency should be no greater than 1 millisecond.
    
- We do not recommend a wide area network (WAN) topology in which a server that is running SQL Server is deployed remotely from other components of the farm over a network that has latency greater than 1 ms., because this topology has not been tested.
    
- Plan for an adequate WAN network if you plan to use SQL Server the AlwaysOn implementation suite, mirroring, log shipping, or Failover Clustering to keep a remote site up-to-date.
    
- We recommend that web servers and application servers have two network adapters: one network adapter to handle user traffic and the other to handle communication with the servers that are running SQL Server.
    
    > [!NOTE]
    > If you use iSCSI, make sure each network adapter is dedicated to either network communication or iSCI, not both. 
  
<a name="Section6"> </a>
## Configure SQL Server


The following sections describe how to plan to configure SQL Server for SharePoint Server.
  
In this section:
  
- [Estimate how many servers are required](#Section6_1)
    
- [Configure storage and memory](#Section6_2)
    
- [Set SQL Server options](#Section6_3)
    
- [Configure databases](#Section6_5)
    
### Estimate how many servers are required
<a name="Section6_1"> </a>

In general, SharePoint Server is designed to take advantage of SQL Server scale out. For example, SharePoint Server may perform better with many medium-size servers that are running SQL Server than with only several large servers.
  
Always put SQL Server on a dedicated server that is not running any other farm roles or hosting databases for any other application. The only exception to this recommendation is if you deploy the system on a stand-alone server for a development or a non-performance oriented test environment. Although SQL Server can run on the same server as SharePoint, we recommend running SQL Server on a separate server for better performance.
  
The following is general guidance for when to deploy an additional server that will run a SQL Server instance: 
  
- Add an additional database server when you have more than four web servers that are running at capacity. 
    
- Add an additional database server when your current server has reached its effective resource limits of RAM, CPU, disk IO throughput, disk capacity, or network throughput.
    
For more information, see [Compute Capacity Limits by Edition of SQL Server](http://go.microsoft.com/fwlink/?LinkID=808802&amp;clcid=0x409) and [Maximum Capacity Specifications for SQL Server](http://go.microsoft.com/fwlink/?LinkID=808804&amp;clcid=0x409).
  
To promote secure credential storage when you are running the Secure Store service application, we recommend that the Secure Store database be hosted on a separate database instance where access is limited to one administrator.
  
### Configure storage and memory
<a name="Section6_2"> </a>

On the server that is running SQL Server, we recommend that the L2 cache per CPU have a minimum of 2 MB to improve memory.
  
#### Follow vendor storage configuration recommendations

For optimal performance when you configure a physical storage array, adhere to the hardware configuration recommendations supplied by the storage vendor instead of relying on the default values of the operating system.
  
If you do not have guidance from your vendor, we recommend using the PowerShell storage cmdlets that are available for Windows Server 2012 R2. For more information, see [Storage Cmdlets in Windows PowerShell](/powershell/module/storage/index?view=win10-ps).
  
#### Provide as many resources as possible

Ensure that the SQL Server I/O channels to the disks are not shared by other applications, such as the paging file and Internet Information Services (IIS) logs.
  
Provide as much bus bandwidth as possible. Greater bus bandwidth helps improve reliability and performance. Consider that the disk is not the only user of bus bandwidth — for example, you must also account for network access.
  

<a name="Section6_3"> </a>
### Set SQL Server options

The following SQL Server settings and options should be configured before you deploy SharePoint Server.
  
- Do not enable auto-create statistics on a server that hosts SQL Server and supports SharePoint Server. SharePoint Server configures the required settings upon provisioning and upgrade. Auto-create statistics can significantly change the execution plan of a query from one instance of SQL Server to another instance of SQL Server. Therefore, to provide consistent support for all customers, SharePoint Server provides coded hints for queries as needed to provide the best performance across all scenarios.
    
- To ensure optimal performance, we strongly recommend that you set **max degree of parallelism (MAXDOP)** to 1 SQL Server instances that host SharePoint Server databases. For more information about how to set **max degree of parallelism**, see [Configure the max degree of parallelism Server Configuration Option](http://go.microsoft.com/fwlink/?LinkID=808807&amp;clcid=0x409).
    
### Configure databases
<a name="Section6_5"> </a>

The following guidance describes best practices to plan for as you configure each database in your environment.
  
#### Separate and prioritize your data among disks

Ideally, you should place the tempdb database, content databases, Usage database, search databases, and SQL Server 2014 (SP1), SQL Server 2016, SQL Server 2017 RTM, SQL Server 2008 R2 with SP1 and SQL Server 2012 transaction logs on separate physical hard disks.
  
The following list provides some best practices and recommendations for prioritizing data:
  
- When you prioritize data among faster disks, use the following ranking:
    
  - Tempdb data files and transaction logs
    
  - Database transaction log files
    
  - Search databases, except for the Search administration database
    
  - Database data files
    
    In a heavily read-oriented portal site, prioritize data over logs.
    
- Testing and customer data show that SharePoint Server farm performance can be significantly impeded by insufficient disk I/O for tempdb. To avoid this issue, allocate dedicated disks for tempdb. If a high workload is projected or monitored — that is, the average read action or the average write action requires more than 20 ms — you might have to ease the bottleneck by either separating the files across disks or by replacing the disks with faster disks. 
    
- For best performance, place the tempdb on a RAID 10 array. The number of tempdb data files should equal the number of core CPUs, and the tempdb data files should be set at an equal size. Count dual core processors as two CPUs for this purpose. Count each processor that supports hyper-threading as a single CPU. For more information, see [Optimizing tempdb Performance](http://go.microsoft.com/fwlink/p/?LinkID=148537).
    
- Separate database data and transaction log files across different disks. If files must share disks because the files are too small to warrant a whole disk or stripe, or you have a shortage of disk space, put files that have different usage patterns on the same disk to minimize concurrent access requests.
    
- Consult your storage hardware vendor for information about how to configure all logs and the search databases for write optimization for your particular storage solution.
    
#### Use multiple data files for content databases

Follow these recommendations for best performance:
  
- Only create files in the primary filegroup for the database.
    
- Distribute the files across separate disks. 
    
- The number of data files should be less than or equal to the number of core CPUs. Count dual core processors as two CPUs for this purpose. Count each processor that supports hyper-threading as a single CPU.
    
- Create data files of equal size. 
    
> [!IMPORTANT]
> Although you can use the backup and recovery tools that are built in to SharePoint Server to back up and recover multiple data files, if you overwrite in the same location, the tools can't restore multiple data files to a different location. For this reason, we strongly recommend that when you use multiple data files for a content database, you use SQL Server backup and recovery tools. For more information about how to back up and recover SharePoint Server, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md). 
  
For more information about how to create and manage filegroups, see [Physical Database Files and Filegroups](http://go.microsoft.com/fwlink/p/?LinkId=117909).
  
#### Limit content database size to improve manageability

Plan for database sizing that will improve manageability, performance, and ease of upgrade for your environment. 
  
To help ensure system performance, we recommended that you limit the size of content databases to 200 GB, except when specific usage scenarios and conditions support larger sizes. For more information about content database size limits, see the "Content database limits" section in [Software boundaries and limits for SharePoint Servers 2016 and 2019](../install/software-boundaries-and-limits-0.md).
  
We generally recommend that a site collection should not exceed 100 GB unless it is the only site collection in the database so that you can use the SharePoint Server granular backup tools to move a site collection to another database if you need to.
  
#### Proactively manage the growth of data and log files

We recommend that you proactively manage the growth of data and log files by considering the following recommendations:
  
- As much as possible, pre-grow all data and log files to their expected final size.
    
- We recommend that you enable autogrowth for safety reasons. Do not rely on the default autogrowth settings. Consider the following guidelines when you configure autogrowth:
    
  - When you plan content databases that exceed the recommended size (200 GB), set the database autogrowth value to a fixed number of megabytes instead of to a percentage. This will reduce the frequency with which SQL Server increases the size of a file. Increasing file size is a blocking action that involves filling the new space with empty pages.
    
  - If the calculated size of the content database is not expected to reach the recommended maximum size of 200 GB within the next year, set it to the maximum size the database is predicted to reach in a year — with 20 percent additional margin for error — by using the **ALTER DATABASE MAXSIZE** property. Periodically review this setting to make sure that it is still an appropriate value, depending on past growth rates. 
    
- Maintain a level of at least 25 percent available space across disks to allow for growth and peak usage patterns. If you are managing growth by adding disks to a RAID array or allocating more storage, monitor disk size closely to avoid running out of space.
    
<a name="Section7"> </a>
## Validate and monitor storage and SQL Server performance

Test that your performance and backup solution on your hardware enables you to meet your service level agreements (SLAs). In particular, test the I/O subsystem of the computer that is running SQL Server to make sure that performance is satisfactory.
  
Test the backup solution that you are using to make sure that it can back up the system within the available maintenance window. If the backup solution can't meet the SLAs your business requires, consider using an incremental backup solution such as Microsoft System Center Data Protection Manager. 
  
It is important to track the following resource components of a server that is running SQL Server: CPU, memory, cache/hit ratio, and I/O subsystem. When one or more of the components seems slow or overburdened, analyze the appropriate strategy based on the current and projected workload. For more information, see [Monitor and Tune for Performance](http://go.microsoft.com/fwlink/?LinkID=799158&amp;clcid=0x409) for SQL Server 2014 (SP1) and [Monitor and Tune for Performance](http://go.microsoft.com/fwlink/?LinkID=808808&amp;clcid=0x409) for SQL Server 2016 and SQL Server 2017 RTM. 
  
The following section lists the performance counters that we recommend that you use to monitor the performance of the SQL Server databases that are running in your SharePoint Server environment. Also listed are approximate healthy values for each counter.
  
For details about how to monitor performance and use performance counters, see [Windows Performance Monitor](http://go.microsoft.com/fwlink/?LinkID=799161&amp;clcid=0x409) and [Monitoring Performance](http://go.microsoft.com/fwlink/?LinkID=799160&amp;clcid=0x409).
  
### SQL Server counters to monitor

Monitor the following SQL Server counters to ensure the health of your servers:
  
- **General statistics** This object provides counters to monitor general server-wide activity, such as the number of current connections and the number of users connecting and disconnecting per second from computers that are running an instance of SQL Server. Consider monitoring the following counter: 
    
  - **User connections** This counter shows the number of user connections on your computer that is running SQL Server. If you see this number increase by 500 percent from your baseline, you may see a performance reduction. 
    
- **Databases** This object provides counters to monitor bulk copy operations, backup and restore throughput, and transaction log activities. Monitor transactions and the transaction log to determine how much user activity is occurring in the database and how full the transaction log is becoming. The amount of user activity can determine the performance of the database and affect log size, locking, and replication. Monitoring low-level log activity to gauge user activity and resource usage can help you identify performance bottlenecks. Consider monitoring the following counter: 
    
  - **Transactions/sec** This counter shows the number of transactions on a given database or on the entire server per second. This number is more for your baseline and to help you troubleshoot issues. 
    
- **Locks** This object provides information about SQL Server locks on individual resource types. Consider monitoring the following counters: 
    
  - **Average Wait Time (ms)** This counter shows the average amount of wait time for each lock request that resulted in a wait. 
    
  - **Lock Wait Time (ms)** This counter shows the wait time for locks in the last second. 
    
  - **Lock waits/sec** This counter shows the number of locks per second that couldn't be satisfied immediately and had to wait for resources. 
    
  - **Number of deadlocks/sec** This counter shows the number of deadlocks on the computer that is running SQL Server per second. This should not increase above 0. 
    
- **Latches** This object provides counters to monitor internal SQL Server resource locks called latches. Monitoring the latches to determine user activity and resource usage can help you identify performance bottlenecks. Consider monitoring the following counters: 
    
  - **Average Latch Wait Time (ms)** This counter shows the average latch wait time for latch requests that had to wait. 
    
  - **Latch Waits/sec** This counter shows the number of latch requests that couldn't be granted immediately. 
    
- **SQL Statistics** This object provides counters to monitor compilation and the type of requests sent to an instance of SQL Server. Monitoring the number of query compilations and recompilations and the number of batches received by an instance of SQL Server gives you an indication of how quickly SQL Server is processing user queries and how effectively the query optimizer is processing the queries. Consider monitoring the following counters: 
    
  - **SQL Compilations/sec** This counter indicates the number of times the compile code path is entered per second. 
    
  - **SQL Re-Compilations/sec** This counter indicates the number statement recompiles per second. 
    
- **Buffer Manager** This object provides counters to monitor how SQL Server uses memory to store data pages, internal data structures, and the procedure cache, and also counters to monitor the physical I/O as SQL Server reads and writes database pages. Consider monitoring the following counter: 
    
  - **Buffer Cache Hit Ratio**
    
  - This counter shows the percentage of pages that were found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups over the last few thousand page accesses. Because reading from the cache is much less expensive than reading from disk, you want this ratio to be high. Generally, you can increase the buffer cache hit ratio by increasing the memory available to SQL Server.
    
- **Plan Cache** This object provides counters to monitor how SQL Server uses memory to store objects such as stored procedures, unprepared and prepared Transact-SQL statements, and triggers. Consider monitoring the following counter: 
    
  - **Cache Hit Ratio**
    
  - This counter indicates the ratio between cache hits and lookups for plans.
    
### Physical server counters to monitor

Monitor the following counters to ensure the health of your computers that are running SQL Server:
  
- **Processor: % Processor Time: _Total** This counter shows the percentage of time that the processor is executing application or operating system processes other than Idle. On the computer that is running SQL Server, this counter should be kept between 50 percent and 75 percent. In case of constant overloading, investigate whether there is abnormal process activity or if the server needs additional CPUs. 
    
- **System: Processor Queue Length** This counter shows the number of threads in the processor queue. Monitor this counter to make sure that it remains less than two times the number of core CPUs. 
    
- **Memory: Available Mbytes** This counter shows the physical memory, in megabytes, available to processes running on the computer. Monitor this counter to make sure that you maintain a level of at least 20 percent of the total available physical RAM. 
    
- **Memory: Pages/sec** This counter shows the rate at which pages are read from or written to disk to resolve hard page faults. Monitor this counter to make sure that it remains under 100. 
    
For more information and memory troubleshooting methods, see the following resources:
  
- **SQL Server 2014 (SP1) -**[Monitor Memory Usage](http://go.microsoft.com/fwlink/?LinkID=799431&amp;clcid=0x409)
    
- [Monitor Disk Usage](http://go.microsoft.com/fwlink/?LinkID=799433&amp;clcid=0x409)
    
- [Monitor CPU Usage](http://go.microsoft.com/fwlink/?LinkID=799434&amp;clcid=0x409)
    
- **SQL Server 2016 &amp; SQL Server 2017 -**[Monitor Memory Usage](http://go.microsoft.com/fwlink/?LinkID=808809&amp;clcid=0x409)
    
- [Monitor Disk Usage](http://go.microsoft.com/fwlink/?LinkID=808810&amp;clcid=0x409)
    
- [Monitor CPU Usage](http://go.microsoft.com/fwlink/?LinkID=808811&amp;clcid=0x409)
    
For more information and memory troubleshooting methods, see [Monitoring Memory Usage](https://go.microsoft.com/fwlink/p/?LinkId=317260) for SQL Server 2008 R2 with SP1, [Monitoring Memory Usage](/previous-versions/sql/sql-server-2012/ms176018(v=sql.110)) for SQL Server 2012, and [Monitor Memory Usage](/sql/relational-databases/performance-monitor/monitor-memory-usage?view=sql-server-2014) for SQL Server 2014. 
  
### Disk counters to monitor

Monitor the following counters to ensure the health of disks. Note that the following values represent values measured over time — not values that occur during a sudden spike and not values that are based on a single measurement.
  
- **Physical Disk: % Disk Time: DataDrive** This counter shows the percentage of elapsed time that the selected disk drive is busy servicing read or write requests-it is a general indicator of how busy the disk is. If the **PhysicalDisk: % Disk Time** counter is high (more than 90 percent), check the **PhysicalDisk: Current Disk Queue Length** counter to see how many system requests are waiting for disk access. The number of waiting I/O requests should be sustained at no more than 1.5 to 2 times the number of spindles that make up the physical disk. 
    
- **Logical Disk: Disk Transfers/sec** This counter shows the rate at which read and write operations are performed on the disk. Use this counter to monitor growth trends and forecast appropriately. 
    
- **Logical Disk: Disk Read Bytes/sec** and **Logical Disk: Disk Write Bytes/sec** These counters show the rate at which bytes are transferred from the disk during read or write operations. 
    
- **Logical Disk: Avg. Disk Bytes/Read** This counter shows the average number of bytes transferred from the disk during read operations. This value can reflect disk latency — larger read operations can result in slightly increased latency. 
    
- **Logical Disk: Avg. Disk Bytes/Write** This counter shows the average number of bytes transferred to the disk during write operations. This value can reflect disk latency — larger write operations can result in slightly increased latency. 
    
- **Logical Disk: Current Disk Queue Length** This counter shows the number of requests outstanding on the disk at the time that the performance data is collected. For this counter, lower values are better. Values greater than 2 per disk may indicate a bottleneck and should be investigated. This means that a value of up to 8 may be acceptable for a logical unit (LUN) made up of 4 disks. Bottlenecks can create a backlog that can spread beyond the current server that is accessing the disk and result in long wait times for users. Possible solutions to a bottleneck are to add more disks to the RAID array, replace existing disks with faster disks, or move some data to other disks. 
    
- **Logical Disk: Avg. Disk Queue Length** This counter shows the average number of both read and write requests that were queued for the selected disk during the sample interval. The rule is that there should be two or fewer outstanding read and write requests per spindle. But this can be difficult to measure because of storage virtualization and differences in RAID levels between configurations. Look for larger than average disk queue lengths in combination with larger than average disk latencies. This combination can indicate that the storage array cache is being overused or that spindle sharing with other applications is affecting performance. 
    
- **Logical Disk: Avg. Disk sec/Read** and **Logical Disk: Avg. Disk sec/Write** These counters show the average time, in seconds, of a read or write operation to the disk. Monitor these counters to make sure that they remain below 85 percent of the disk capacity. Disk access time increases exponentially if read or write operations are more than 85 percent of disk capacity. To determine the specific capacity for your hardware, refer to the vendor documentation or use the Diskspd Utility, storage testing tool to calculate it. For more information, see [Diskspd: A Robust Storage Performance Tool](https://gallery.technet.microsoft.com/DiskSpd-A-Robust-Storage-6ef84e62).
    
  - **Logical Disk: Avg. Disk sec/Read** This counter shows the average time, in seconds, of a read operation from the disk. On a well-tuned system, ideal values are from 1 through 5 ms for logs (ideally 1 ms on a cached array), and from 4 through 20 ms for data (ideally less than 10 ms). Higher latencies can occur during peak times. However, if high values occur regularly, you should investigate the cause. 
    
  - **Logical Disk: Avg. Disk sec/Write** This counter shows the average time, in seconds, of a write operation to the disk. On a well-tuned system, ideal values are from 1 through 5 ms for logs (ideally 1 ms on a cached array), and from 4 through 20 ms for data (ideally less than 10 ms). Higher latencies can occur during peak times. However, if high values occur regularly, you should investigate the cause. 
    
    When you are using RAID configurations with the **Logical Disk: Avg. Disk Bytes/Read** or **Logical Disk: Avg. Disk Bytes/Write** counters, use the formulas listed in the following table to determine the rate of input and output on the disk. 
    
|**RAID level**|**Formula**|
|:-----|:-----|
|RAID 0  <br/> |I/Os per disk = (reads + writes) / number of disks  <br/> |
|RAID 1  <br/> |I/Os per disk = [reads + (2 × writes)] / 2  <br/> |
|RAID 5  <br/> |I/Os per disk = [reads + (4 × writes)] / number of disks  <br/> |
|RAID 10  <br/> |I/Os per disk = [reads + (2 × writes)] / number of disks  <br/> |
   
For example, if you have a RAID 1 system that has two physical disks, and your counters are at the values that are shown in the following table.
  
|**Counter**|**Value**|
|:-----|:-----|
|**Avg. Disk sec/Read** <br/> |80  <br/> |
|**Logical Disk: Avg. Disk sec/Write** <br/> |70  <br/> |
|**Avg. Disk Queue Length** <br/> |5  <br/> |
   
- The **I/O value per disk** can be calculated as follows: (80 + (2 × 70))/2 = 110 
    
- The **disk queue length** can be calculated as follows: 5/2 = 2.5 
    
- In this situation, you have a borderline I/O bottleneck.
    
### Other monitoring tools

You can also monitor disk latency and analyze trends by using the sys.dm_io_virtual_file_stats dynamic management view in SQL Server 2008. For more information, see [sys.dm_io_virtual_file_stats (Transact-SQL)](http://go.microsoft.com/fwlink/p/?LinkID=105587).
  
## SQL Server 2012 for SharePoint Server 2013
<a name="Section8A"> </a>

Thanks to Bill Baer, Microsoft Senior Product Marketing Manager and Brian Alderman, CEO and Founder of MicroTechPoint for providing a series of online SQL Server 2012 training modules. Special thanks to Channel 9 Microsoft for hosting these online training modules. The following training modules provide details about SQL Server 2012 database settings to help you learn how to improve SharePoint Server 2016 performance, availability, and security.
  
- [Tuning SQL Server 2012 for SharePoint 2013: (01) Key SQL Server and SharePoint Server Integration](http://channel9.msdn.com/Series/Tuning-SQL-Server-2012-for-SharePoint-2013/Tuning-SQL-Server-2012-for-SharePoint-2013-01-Key-SQL-Server-and-SharePoint-Server-Integration-Conce)
    
- [Tuning SQL Server 2012 for SharePoint 2013: (02) Best Practices for SQL Server Database Settings](http://channel9.msdn.com/Series/Tuning-SQL-Server-2012-for-SharePoint-2013/Tuning-SQL-Server-2012-for-SharePoint-2013-02-Best-Practices-for-SQL-Server-Database-Settings)
    
- [Tuning SQL Server 2012 for SharePoint 2013: (03) Server Settings for SQL Server](http://channel9.msdn.com/Series/Tuning-SQL-Server-2012-for-SharePoint-2013/Tuning-SQL-Server-2012-for-SharePoint-2013-03-Server-Settings-for-SQL-Server)
    
- [Tuning SQL Server 2012 for SharePoint 2013: (04) SQL Server and SharePoint Availability](http://channel9.msdn.com/Series/Tuning-SQL-Server-2012-for-SharePoint-2013/Tuning-SQL-Server-2012-for-SharePoint-2013-04-SQL-Server-and-SharePoint-Availability)
    
## See also
<a name="Section8A"> </a>

#### Concepts

[Overview of SQL Server in SharePoint Server 2016 and 2019 environments](overview-of-sql-server-in-sharepoint-server-2016-and-2019-environments.md)
  
[Optimize performance for SharePoint Server 2013](optimize-performance.md)
  
[Best practices for SQL Server in a SharePoint Server farm](best-practices-for-sql-server-in-a-sharepoint-server-farm.md)
  
[Performance planning in SharePoint Server 2013](performance-planning-in-sharepoint-server-2013.md)
  
[Capacity management and sizing for SharePoint Server 2013](capacity-management-and-sizing-for-sharepoint-server-2013.md)
  
[Capacity planning for SharePoint Server 2013](capacity-planning.md)
#### Other Resources

[Overview of SQL Server in a SharePoint Server 2013 environment](overview-of-sql-server-in-a-sharepoint-server-2013-environment.md)

