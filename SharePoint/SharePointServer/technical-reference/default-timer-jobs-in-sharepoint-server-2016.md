---
title: "Default timer jobs in SharePoint Server 2016"
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
ms.assetid: b23e4fb4-6ee1-451e-92b3-7c90be5dc7e7
description: "Learn about the default timer jobs in SharePoint Server."
---

# Default timer jobs in SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]
  
## Default timer jobs
<a name="DefaultJobs"> </a>

The following table lists the default timer jobs for SharePoint Server 2016.
  
|**Timer job**|**Description**|**Default schedule**|
|:-----|:-----|:-----|
|Access Services monitor  <br/> |Monitors the connectivity of Access Services on SharePoint Online and SQL Azure.  <br/> |5 minutes  <br/> |
|Access Services provider for SQL connection statistics (SQL Azure only)  <br/> |Provides the statistics on connections to SQL for Access Services (SQL Azure only).  <br/> |Daily  <br/> |
|Access Services provider for SQL Event Log (SQL Azure only)  <br/> |Gathers the SQL Server Event Log for Access Services (SQL Azure only).  <br/> |Daily  <br/> |
|App installation service  <br/> |Installs and uninstalls apps.  <br/> |5 minutes  <br/> |
|App state update  <br/> |Retrieves and applies updated information on apps from the SharePoint Store. It includes the availability of updates and information about disabled apps.  <br/> |Hourly  <br/> |
|Application addresses refresh  <br/> |Synchronizes connection information for remote service applications.  <br/> |15 minutes  <br/> |
|Application server administration service  <br/> |Manages shared service instances that may perform highly privileged operations. Requires that the SharePoint Administration service is running. The Search service instance is managed by this job on deployments other than stand-alone server deployments.  <br/> |1 minute  <br/> |
|Application server  <br/> |Manages shared service instances that do not perform highly privileged operations. The Search service instance is managed by this job on stand-alone server deployments.  <br/> |1 minute  <br/> |
|Audit log trimming  <br/> |Trims audit trail entries from site collections.  <br/> |Monthly  <br/> |
|Autohosted app instance counter  <br/> |Counts the number of autohosted app instances per site subscription.  <br/> |Weekly  <br/> |
|Bulk workflow task processing  <br/> |Processes bulk workflow task completion.  <br/> |Daily  <br/> |
|CEIP data collection  <br/> |Collects farm data for the Customer Experience Improvement Program.  <br/> |Daily  <br/> |
|Cell storage data cleanup  <br/> |Deletes temporary cell storage data and frees SQL Server disk space.  <br/> |15 minutes  <br/> |
|Change log  <br/> |Records many types of changes that you make to SharePoint sites. Removes expired entries from the change log of the web application.  <br/> |Weekly  <br/> |
|Compliance Dar Processing  <br/> |Processes data at rest compliance tasks.  <br/> |10 minutes  <br/> |
|Compliance Dar task house keeping  <br/> |Cleans up completed and failed data at rest compliance tasks.  <br/> |Daily  <br/> |
|Compliance high priority policy processing  <br/> |Processes high priority data at rest compliance tasks.  <br/> |15 minutes  <br/> |
|Compliance Policy Processing  <br/> |Processes compliance policies as defined in Policy Center and invokes appropriate actions on items.  <br/> |Daily  <br/> |
|Content organizer processing  <br/> |Processes documents in the drop-off library that match organizing rules.  <br/> |Daily  <br/> |
|Content type hub  <br/> |Tracks content type log maintenance and manages unpublished content types.  <br/> |Daily  <br/> |
|Content type subscriber  <br/> |Retrieves content type packages from the hub and applies them to the local content type gallery.  <br/> |Hourly  <br/> |
|Database Performance Metric Provider  <br/> ||1 minute  <br/> |
|Database wait statistics  <br/> |Periodically gathers database wait statistics.  <br/> |Hourly  <br/> |
|Dead site delete  <br/> |When auto site cleanup is enabled, sites that are not used in a certain period of time are deleted.  <br/> |Weekly  <br/> |
|Deferred access control list update  <br/> |Applies updates to access control lists (ACLs) resulting from broad security changes.  <br/> |1 minute  <br/> |
|Delete job history  <br/> |Deletes old entries from the timer job history.  <br/> |Daily  <br/> |
|Delete upgrade evaluation site collections  <br/> |Deletes upgrade evaluation site collections that are past their expiry date and sends notifications to those that are near expiry date.  <br/> |Daily  <br/> |
|Diagnostic data provider: app usage  <br/> |Periodically collects App statistics.  <br/> |Daily  <br/> |
|Diagnostic data provider: Event Log  <br/> |Collects Windows Event Log entries  <br/> |1 minute  <br/> |
|Diagnostic data provider: IO Intensive SQL Queries  <br/> |Collects a SQL trace of IO intensive SQL queries  <br/> |1 minute  <br/> |
|Diagnostic data provider: Per-database IO  <br/> |Collects IOs for each database file  <br/> |2 minutes  <br/> |
|Diagnostic data provider: Performance Counters - Database Servers  <br/> |Collects Performance Monitor Counters data on database servers.  <br/> **Important:** <br/> The timer service account must have enough permissions to collect counters on the database server. It should at least be a member of Performance Monitor Users.  <br/> |1 minute  <br/> |
|Diagnostic data provider: Performance Counters - Web Front Ends  <br/> |Collects Performance Monitor Counters data on web front ends.  <br/> |1 minute  <br/> |
|Diagnostic data provider: Site Size  <br/> |||
|Diagnostic data provider: SQL Blocking Queries  <br/> ||N/A  <br/> |
|Diagnostic data provider: SQL Blocking Reports  <br/> ||1 minute  <br/> |
|Diagnostic data provider: SQL Deadlocks  <br/> ||1 minute  <br/> |
|Diagnostic data provider: SQL DMV  <br/> ||30 minutes  <br/> |
|Diagnostic data provider: SQL Memory DMV  <br/> |Collects SQL Dynamic Management Views (DMV) data.  <br/> |N/A  <br/> |
|Diagnostic data provider: Trace Log  <br/> |Collects trace log entries and stores the usage data in the logging database.  <br/> ||
|Disk over quota warning  <br/> |Sends out disk over quota warning email notifications.  <br/> |Daily  <br/> |
|Disk quota warning  <br/> |Looks for sites that have exceeded the storage quota, and sends out disk quota warning email notifications.  <br/> |Weekly  <br/> |
|Document changed anti-virus processing  <br/> |NA  <br/> |Hourly  <br/> |
|Document full crawl anti-virus processing  <br/> |NA  <br/> |Hourly  <br/> |
|Document ID assignment  <br/> |Work item that assigns document ID to all items in the site collection.  <br/> |Daily  <br/> |
|Document ID enable/disable  <br/> |Work item that propagates content type changes across all sites when the Document ID feature is reconfigured.  <br/> |Daily  <br/> |
|Document Set fields synchronization  <br/> |Synchronizes metadata from the document set to the items inside the document library.  <br/> |15 minutes  <br/> |
|Document Set template update  <br/> |Propagates changes that are made to the document set template to the existing items.  <br/> |Hourly  <br/> |
|eDiscovery in-place hold processing  <br/> |The in-place hold timer job starts and releases the holds of SharePoint websites.  <br/> |Hourly  <br/> |
|Enterprise Metadata site data update  <br/> |Updates all site collections after a language pack addition or an Enterprise Metadata service application restore.  <br/> |Hourly  <br/> |
|Expiration policy  <br/> |Enumerates list items and looks for those with an expiration date that has already occurred. For those items, runs disposition processing. Disposition processing most often results in deleting items. But it can perform other actions, such as processing disposition workflows.  <br/> |Weekly  <br/> |
|Extension map refresh  <br/> |Checks for changes in the extension map data.  <br/> |1 minute  <br/> |
|File post processor  <br/> |Processes the files asynchronously after the file has been saved. The processing includes extraction of the file-specific metadata and generation of default thumbnails.  <br/> |1 minute  <br/> |
|Fix site storage metrics  <br/> |Fixes site storage metrics.  <br/> |Hourly  <br/> |
|Gradual site delete  <br/> |Deletes all the data from the host content database for all deleted site collections.  <br/> |Hourly  <br/> |
|Health analysis (Daily, Central Administration, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Central Administration web application and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health analysis (Daily, Central Administration, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Central Administration web application and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health analysis (Daily, Machine Translation service, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Machine Translation service application and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, Machine Translation service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the Machine Translation service application and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, Microsoft SharePoint Foundation Timer, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, Microsoft SharePoint Foundation Timer, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Daily, Microsoft SharePoint Foundation web application, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run SharePoint web applications and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Daily, Microsoft SharePoint Foundation web application, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs SharePoint web applications and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, User Profile service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service application and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, Visio Graphics service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs Visio Services in SharePoint Server 2016 and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Daily, Word Automation Services, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run Word Automation Services and the Usage and Health Data Collection service application.  <br/> |Daily  <br/> |
|Health Analysis (Hourly, distributed cache, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers that run the Distributed Cache service.  <br/> |Hourly  <br/> |
|Health Analysis (Hourly, Microsoft SharePoint Foundation Timer, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Hourly, Microsoft SharePoint Foundation Timer, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Hourly, Security Token Service, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Security Token Service (STS) and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Hourly, User Profile service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Hourly, Word Automation Services, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs Word Automation Services and the Usage and Health Data Collection service application.  <br/> |Hourly  <br/> |
|Health Analysis (Monthly, Microsoft SharePoint Foundation Timer, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Monthly  <br/> |
|Health Analysis (Monthly, User Profile Service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile Service and the Usage and Health Data Collection service application.  <br/> |Monthly  <br/> |
|Health Analysis (Weekly, Central Administration, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the Central Administration website and the Usage and Health Data Collection service application.  <br/> |Weekly  <br/> |
|Health Analysis (Weekly, Microsoft SharePoint Foundation Timer, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Weekly  <br/> |
|Health Analysis (Weekly, Microsoft SharePoint Foundation Timer, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the SharePoint Timer Service and the Usage and Health Data Collection service application.  <br/> |Weekly  <br/> |
|Health Analysis (Weekly, Microsoft SharePoint Foundation web application, all servers)  <br/> |Runs SharePoint Health Analyzer jobs on all servers in the farm that run SharePoint web applications and the Usage and Health Data Collection service application.  <br/> |Weekly  <br/> |
|Health Analysis (Weekly, User Profile service, any server)  <br/> |Runs SharePoint Health Analyzer jobs on the first server found in the farm that runs the User Profile service and the Usage and Health Data Collection service application.  <br/> |Weekly  <br/> |
|Hold processing and reporting  <br/> |Generates a hold report by enumerating items in a hold and updating them to remove them from hold, as appropriate.  <br/> |Daily  <br/> |
|Immediate Alerts  <br/> |Sends out immediate and scheduled alerts.  <br/> |5 minutes  <br/> |
|InfoPath Forms Services maintenance  <br/> |Performs maintenance operations on administrator-approved InfoPath Forms Services form templates across all front-end Web servers.  <br/> |Daily  <br/> |
|Information management policy  <br/> |Performs background processing for information policies, such as calculating updated expiration dates for items with a new retention policy.  <br/> |Weekly  <br/> |
|Internal app state update  <br/> |Retrieves and applies updated information on apps from App Catalogs.  <br/> |Hourly  <br/> |
|Large list automatic column index management  <br/> |Automatically manage list column indices for large lists.  <br/> |Daily  <br/> |
|License renewal  <br/> |Renews all licenses of the apps from the SharePoint Store.  <br/> |Hourly  <br/> |
|Licensing synchronizer  <br/> |Synchronizes trial expiration time licensing information to the configuration database.  <br/> |Hourly  <br/> |
|Machine Translation Service - Language Support  <br/> |Updates the languages available to the Machine Translation Service.  <br/> |Weekly  <br/> |
|Machine Translation Service - Machine Translation Service  <br/> |Initiates translation of documents that were submitted to the Machine Translation Service for asynchronous translation.  <br/> |15 minutes  <br/> |
|Machine Translation Service - Remove Job History  <br/> |Removes the history for expired jobs from the Machine Translation Service queue database.  <br/> |Weekly  <br/> |
|Microsoft SharePoint Foundation Usage Data Import  <br/> |Imports usage log files into the event store.  <br/> |5 minutes  <br/> |
|Microsoft SharePoint Foundation Usage Data Maintenance  <br/> |Performs maintenance in the logging database.  <br/> |Hourly  <br/> |
|Microsoft SharePoint Foundation Usage Data Processing  <br/> |Checks for expired usage data at the farm level and deletes the data. Expired usage data consists of records in the central usage data collection database that are older than 30 days.  <br/> |Daily  <br/> |
|Migration  <br/> |Background migration task.  <br/> |1 minute  <br/> |
|My Site cleanup  <br/> |Starts a workflow on a deleted user's My Site. The default behavior is to send an email message to the manager with a link to the deleted user's site. The email message contains a request to the manager to move any documents or data that the manager wants to preserve, because the site might be deleted in the future.  <br/> |Daily  <br/> |
|My Site host automatic upgrade  <br/> |Automatically upgrading for the My Site host.  <br/> |Daily  <br/> |
|My Site instantiation interactive request queue  <br/> |A timer job queue for interactive (web initiated) My Site instantiation requests.  <br/> |1 minute  <br/> |
|My Site instantiation non-interactive request queue  <br/> |A timer job queue for non-interactive (Office-client initiated) My Site instantiation requests.  <br/> |1 minute  <br/> |
|My Site second instantiation interactive request queue  <br/> |A second timer job queue for interactive (web initiated) My Site instantiation requests.  <br/> |1 minute  <br/> |
|My Sites automatic upgrade  <br/> |Automatically upgrading for the My Sites.  <br/> |Daily  <br/> |
|Notification  <br/> |Queries and updates the notification list and sends out pending scheduling notifications.  <br/> |Daily  <br/> |
|Over quota notification requests queue  <br/> |Queue for site over quota email notification requests.  <br/> |Hourly  <br/> |
|Password management  <br/> |Sends email and logs events for expiring passwords and password changes. This timer job helps ensure that managed passwords are changed before they expire.  <br/> |Daily  <br/> |
|Performance Metric Provider  <br/> |This diagnostic data provider collects the per metrics data.  <br/> |1 minute  <br/> |
|Persisted navigation term set synchronization  <br/> |Synchronizes the persisted copy of navigation term sets.  <br/> |Hourly  <br/> |
|Product version  <br/> |Checks the installation status of the computer and adds that data to the database.  <br/> |Daily  <br/> |
|Project Server: Active Directory Sync for Project Server service application  <br/> |Synchronizes Active Directory with Project Web App enterprise resource pools and security groups.  <br/> |Daily  <br/> |
|Project Server: alerts and reminders for Project Server service application  <br/> |Sends the alerts and reminders that were set up by Project Web App users.  <br/> |Daily  <br/> |
|Project Server: backup and restore for Project Server service application  <br/> |Backs up and restores Project Web App data to and from the archive store, using the schedule set by the Project Server administrator.  <br/> |Daily  <br/> |
|Project Server: database maintenance job for Project Server service application  <br/> |Performs routine maintenance on the Project Server database including defragmenting the indexes and updating the database usage.  <br/> |Daily  <br/> |
|Project Server: language installation for Project Server service application  <br/> |Completes installation of Project Web App language packs in the database, and ensures deployment of localized Report Center reports.  <br/> |Daily  <br/> |
|Project Server: monitor scheduled cube jobs for Project Server service applicatio  <br/> |Updates data analysis cubes that are scheduled in Project Web App.  <br/> |Hourly  <br/> |
|Project Server: product feedback job for Project Server service application  <br/> |Collects statistical data on the usage, reliability and performance of Project Server features and sends this information to Microsoft to be used to improve the product in future releases.  <br/> |Daily  <br/> |
|Project Server: Queue auto heal job for Project Server service application  <br/> |Attempts to automatically heal stuck Project Server queue jobs when the queue job is stuck at Waiting for Processing or Processing state due to internal errors.  <br/> |30 minutes  <br/> |
|Project Server: Queue maintenance job for Project Server service application  <br/> |Purges older Project Server queue jobs to maintain the performance of the Project Server queue.  <br/> |Daily  <br/> |
|Project Server: resource capacity refresh job for Project Server service application  <br/> |Refreshes the resource capacity information in Project Web App reporting.  <br/> |Daily  <br/> |
|Project Server: synchronization of Project Web App permissions to SharePoint Server permissions job for Project Server service application  <br/> |Synchronizes Project permissions to the SharePoint Server project sites. Users who can view or change projects in Project Web App are granted permissions to the SharePoint Server sites for those projects. You can change these permissions from the PWA Settings page.  <br/> |Daily  <br/> |
|Project Server: synchronization of SharePoint Server permissions to Project Web App permissions job for Project Server service application  <br/> |Synchronizes SharePoint Server permissions to Project Web App.  <br/> |1 minute  <br/> |
|Project Server: synchronize Exchange OOF calendar job for Project Server service application  <br/> |Synchronizes out-of-office time for users who select this option. Each user's Microsoft Exchange calendar synchronizes with their Project Web App resource calendar.  <br/> |Daily  <br/> |
|Project Server: task list synchronizer for SharePoint Tasks List Projects job for Project Server service application  <br/> |Updates Project Server with the latest changes from connected SharePoint Server Project Task Lists.  <br/> |5 minutes  <br/> |
|Project Server: workflow maintenance job for Project Server service application  <br/> |Maintains the health of Project Server workflows. It resolves issues between Enterprise Project Templates and workflows, updates the status of workflows, and closes completed workflows.  <br/> |Daily  <br/> |
|Recycle Bin  <br/> |Looks for content in the Recycle Bins and moves it to the next stage or deletes it.  <br/> |Weekly  <br/> |
|Repair orphan site collections  <br/> |Attempts to repair orphaned site collections  <br/> |Daily  <br/> |
|Request more quota  <br/> |Queues up requests for additional quota by the site collection admin and sends the request to the tenant admin.  <br/> |30 minutes  <br/> |
|Scheduled Approval  <br/> |Looks for content that is scheduled for approval and moves it to the next stage in the process.  <br/> |1 minute  <br/> |
|Scheduled Unpublish  <br/> |Looks for content that is scheduled to be unpublished and removes it.  <br/> |1 minute  <br/> |
|Search and process  <br/> |Processes a search result that is scoped to a site collection and puts search results on hold.  <br/> |Daily  <br/> |
|Search change log generator  <br/> |Generates appropriate change logs when SharePoint items change. This is required for search to function correctly.  <br/> |5 minutes  <br/> |
|Search engine sitemap  <br/> |Generates search engine sitemaps and updates robots.txt.  <br/> |Daily  <br/> |
|SharePoint BI maintenance  <br/> |Deletes temporary dashboard objects and user-persistent filter values from the database. The longevity of these values can be set on the PerformancePoint Services Settings page.  <br/> |Hourly  <br/> |
|SharePoint Server CEIP data collection  <br/> |Collects the Customer Experience Improvement Program data.  <br/> |Daily  <br/> |
|Site lookup refresh  <br/> |Checks the site map data for site lookup changes.  <br/> |1 minute  <br/> |
|Site master invalidation  <br/> |Checks the site masters in content DB for any feature or site definitions changes. If required, it recreates the site master.  <br/> |Hourly  <br/> |
|Site policy and Exchange site mailbox policy update  <br/> |Updates Exchange site mailboxes with the site policy of the associated SharePoint site.  <br/> |Daily  <br/> |
|Solution daily resource usage update  <br/> |Marks the daily boundary for sandboxed solution resource quota monitoring.  <br/> |Daily  <br/> |
|Solution resource usage log processing  <br/> |Aggregates resource usage data from sandboxed solution execution.  <br/> |5 minutes  <br/> |
|Solution resource usage update  <br/> |Records resource usage data from sandboxed solution execution, and sends email to owners of site collections that are exceeding their allocated resource quota.  <br/> |15 minutes  <br/> |
|State Service delete expired sessions  <br/> |Deletes expired data that is stored in the state service databases.  <br/> |Hourly  <br/> |
|Storage metrics processing  <br/> |Processes storage metrics changes for site collections.  <br/> |5 minutes  <br/> |
|Taxonomy groups replication  <br/> |A timer job for hybrid connected servers that updates the local SharePoint Server term store with the latest term changes made to the Enterprise Metadata service in the hybrid connected SharePoint Online tenant.  <br/> |Daily  <br/> |
|Taxonomy update scheduler  <br/> |Updates site collections with the latest term changes that were made to the Enterprise Metadata service.  <br/> |Hourly  <br/> |
|Timer service recycle  <br/> |Recycles the Timer service to free resources.  <br/> |Daily  <br/> |
|Translation Export Job Definition  <br/> |Exports page and list content to XLIFF for human translation or machine translation via the Machine Translation Service.  <br/> |15 minutes  <br/> |
|Translation Import Job Definition  <br/> |Imports translated page and list content from XLIFF to correct location in a site collection.  <br/> |15 minutes  <br/> |
|Unified policy onprem sync  <br/> |Synchronizes the unified policy from the master policy store for SharePoint Server.  <br/> |Hourly  <br/> |
|Unified policy sync status update  <br/> |Uploads the workoad policy synchronize status to the master policy store.  <br/> |5 minutes  <br/> |
|Upgrade site collections  <br/> |Upgrades site collections in a content database.  <br/> |10 minutes  <br/> |
|Upgrade site collections  <br/> |Upgrades site collections in a content database.  <br/> |Daily  <br/> |
|Upgrade site collections  <br/> |Upgrades site collections in a content database.  <br/> |Hourly  <br/> |
|Upgrade work item  <br/> |Processes deferred upgrade work items which were generated during an upgrade. For example, generating thumbnails for upgraded image libraries.  <br/> |Daily  <br/> |
|Upload App Analytics  <br/> |Uploads aggregated app usage data to Microsoft. Microsoft uses this data to improve the quality of apps in the marketplace. If you have multiple content farms connecting to the same search server, activate this feature only on one farm.  <br/> |Daily  <br/> |
|User Profile service application - activity feed  <br/> |Pre-computes activities to be shown in users' activity feeds.  <br/> |10 minutes  <br/> |
|User Profile service application - activity feed cleanup  <br/> |Cleans up pre-computed activities that are used in activity feeds that are older than 14 days. This job does not affect the User Profile change log.  <br/> |Daily  <br/> |
|User Profile service application - audience compilation  <br/> |Computes memberships of defined audiences.  <br/> |Weekly  <br/> |
|User Profile service application - background operations processing  <br/> |Runs background operations for the User Profile service application.  <br/> |5 minutes  <br/> |
|User Profile service application - feed cache full repopulation  <br/> |Handles the full repopulation of feed cache.  <br/> |5 minutes  <br/> |
|User Profile service application - feed cache repopulation  <br/> |Handles the repopulation of feed cache.  <br/> |5 minutes  <br/> |
|User Profile service application - My Site suggestions email  <br/> |Sends email messages that contain colleague and keyword suggestions to people who do not update their profiles often.  <br/> |Monthly  <br/> |
|User Profile service application - Per database User Profile to SharePoint full synchronization  <br/> |Synchronizes user information from the User Profile application to SharePoint users and from SharePoint site memberships to the User Profile application for a database.  <br/> |5 minutes  <br/> |
|User Profile service application - profile attribute sync  <br/> |Synchronizes Active Directory attributes to Profile database.  <br/> |10 minutes  <br/> |
|User Profile service application - social data maintenance  <br/> |Aggregates social tags and ratings and cleans the social data change log.  <br/> |Hourly  <br/> |
|User Profile service application - social rating synchronization  <br/> |Use to synchronize rating values between Social database and Content database.  <br/> |Hourly  <br/> |
|User Profile service application - Unified group processing high performance  <br/> |Runs the Unified Group site collection operations.  <br/> |1 minute  <br/> |
|User Profile service application - Unified group processing  <br/> |Runs the Unified Group site collection operations.  <br/> |1 minute  <br/> |
|User Profile service application - User change import  <br/> |Imports user property changes to the User Profile database.  <br/> |15 minutes  <br/> |
|User Profile service application - User PointPublishing processing  <br/> |Runs the User PointPublishing personal site collection operations.  <br/> |1 minute  <br/> |
|User Profile service application - User Profile Active Directory import  <br/> |Imports objects from Active Directory to the Profile database.  <br/> |5 minutes  <br/> |
|User Profile service application - user profile change cleanup  <br/> |Cleans up data that is 14 days old from User Profile change log.  <br/> |Daily  <br/> |
|User Profile service application - user profile change  <br/> |Processes changes to user profiles.  <br/> |Hourly  <br/> |
|User Profile service application - user profile language synchronization  <br/> |Looks for new language pack installations and makes sure that strings that relate to the user profile service are localized correctly.  <br/> |Hourly  <br/> |
|User Profile service application - User Profile to SharePoint full synchronization  <br/> |Synchronizes user information from the User Profile service application to SharePoint users and synchronizes site memberships from SharePoint to the User Profile service application.  <br/> |Hourly  <br/> |
|User Profile service application - User Profile to SharePoint language and region synchronization  <br/> |Synchronizes language and region information from the User Profile service application to SharePoint users.  <br/> |1 minute  <br/> |
|User Profile service application - User Profile to SharePoint quick synchronization  <br/> |Synchronizes user information from the User Profile service application to SharePoint users who were recently added to a site.  <br/> |5 minutes  <br/> |
|User Profile service application - User Profile to SharePoint synchronization alert  <br/> |Checks to see if the synchronization of user information from the User Profile application to SharePoint users is out of date.  <br/> |Hourly  <br/> |
|Variations create hierarchies job definition  <br/> |Creates a complete variations hierarchy by spawning all sites and pages from the source site hierarchy for all variation labels.  <br/> |Hourly  <br/> |
|Variations propagate list items job definition  <br/> |Propagates list items to variant sites.  <br/> |15 minutes  <br/> |
|Variations propagate page job definition  <br/> |Creates or updates peer pages of the source page that was approved or published in all target labels. The resulting peer pages are in an unpublished state.  <br/> |15 minute  <br/> |
|Variations propagate sites and lists  <br/> |Creates variant sites when the Variations Automatic Creation setting is enabled.  <br/> |30 minute  <br/> |
|Video query rule provisioner  <br/> |Provisions video query rule for a site when the Search service application becomes available.  <br/> |Daily  <br/> |
|Word Automation Services  <br/> |Processes and distributes queued conversion job items to application servers.  <br/> |15 minutes  <br/> |
|Word Automation Services - Remove Job History  <br/> |Removes the history for expired jobs from Word Automation Services.  <br/> |Weekly  <br/> |
|Workflow  <br/> |Processes workflow events that are in the scheduled items table, such as delays.  <br/> |5 minute  <br/> |
|Workflow auto cleanup  <br/> |Deletes tasks and instances in the workflow instance table for workflows that were marked completed more than  _n_ days in the past, where  _n_ is specified in the workflow association. Crawls through tasks and the workflow instance table.  <br/> |Daily  <br/> |
|Workflow failover  <br/> |Processes events for workflows that have failed and are marked to be retried.  <br/> |15 minute  <br/> |
   
## See also
<a name="DefaultJobs"> </a>

#### Other Resources

[Default timer jobs in SharePoint Server 2019](default-timer-jobs-in-sharepoint-server-2019.md)

[Default timer jobs in SharePoint 2013](default-timer-jobs-in-sharepoint-2013.md)

