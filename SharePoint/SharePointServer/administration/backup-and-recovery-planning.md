---
title: "Plan for backup and recovery in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 01abe8d2-33f8-48fe-af76-40522a5afe08
description: "Learn how to plan backup and recovery strategies for your SharePoint Server environments."
---

# Plan for backup and recovery in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Typically, you want to have a backup and recovery plan available before you deploy your SharePoint Server environment. You then need to maintain and update your backup and recovery plan as your SharePoint Server changes to protect your data.
  
The stages involved in planning for backup and recovery include determining backup and recovery strategies for a SharePoint Server environment and deciding which tools to use. The stages do not have to be done in the order listed, and the process may be iterative.
  
When you plan backup and recovery for disaster recovery, consider common events, failures, and errors; local emergencies; and regional emergencies. The sections in this article describe the stages that you must address in your backup and recovery plan. Each stage is a step toward the final goal of a good backup to use to recover your SharePoint Server farm. You can customize the stages to meet your needs. Note that your overall backup and recovery plan is dynamic and must reflect your current SharePoint Server environment.
  
For more information about SharePoint Server backup and recovery, see [Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md).
  
## Define business requirements for SharePoint farms and services

To define business requirements, determine the following for each farm and service in the environment: 
  
- Recovery point objective (RPO) is the objective for the maximum time period between the last available backup and any potential failure point. It is determined by how much data that the business can afford to lose if a failure were to occur. 
    
- Recovery time objective (RTO) is the objective for the maximum time that a data recovery process will take. It is determined by the time that the business can afford for the site or service to be unavailable. 
    
- Recovery level objective (RLO) is the objective that defines the granularity with which you must be able to recover data — whether you must be able to recover the whole farm, Web application, site collection, site, list or library, or item. 
    
Shorter RPO and RTO, and finer granularity of RLO, all typically cost more. 
  
## Choose what to protect and recover in your SharePoint environment

Your business requirements will help you determine which components of the environment that you must protect, and the granularity with which you must be able to recover them.
  
The following tables list components of a SharePoint environment that you might decide to protect, and the tools that can be used to back up and recover each component. As you'll notice, both tables are similar but specific backup components are shown for each SharePoint Server edition.
  
**SharePoint Server 2016 components for backup and recovery**

|**Component**|**SharePoint backup**|**SQL Server 2014 Service Pack 1 (SP1)**|**SQL Server 2016**|**System Center 2016 - Data Protection Manager Update Rollup 2 (UR2)**|**File system backup**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Farm  <br/> |Yes  <br/> |||Yes (6)  <br/> ||
|Service applications  <br/> |Yes  <br/> |||||
|Web application  <br/> |Yes  <br/> |||||
|Content databases  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> ||
|Site collection  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> ||
|Site  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes  <br/> ||
|Document library or list  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes  <br/> ||
|List item or document  <br/> ||||Yes  <br/> ||
|Content stored in remote BLOB stores  <br/> |Yes (3)  <br/> |Yes (3)  <br/> |Yes (3)  <br/> |Yes (3)  <br/> ||
|Customizations deployed as solution packages  <br/> |Yes (7)  <br/> |Yes (7)  <br/> |Yes (7)  <br/> |Yes (6, 7)  <br/> ||
|Changes to Web.config made by using Central Administration or an API  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes (4)  <br/> ||
|SharePoint configuration settings  <br/> |Yes (2, 8)  <br/> |Yes (2, 8)  <br/> |Yes (2, 8)  <br/> |Yes (2, 9)  <br/> ||
|Customizations not deployed as solution packages  <br/> ||||Yes, files can be recovered if protected as files. (4, 5)  <br/> |Yes  <br/> |
|Changes to Web.config not made by using Central Administration or an API  <br/> ||||Yes (4)  <br/> |Yes  <br/> |
|IIS configurations not set through SharePoint Server 2016  <br/> ||||Yes (5)  <br/> |Yes  <br/> |
|SQL Server Reporting Services databases  <br/> ||Yes  <br/> |Yes  <br/> |Yes  <br/> ||
   
(1) Farm-level and database-level backup and restore can be used for site collection recovery if a single site collection is stored in a database. 
  
(2) Farm-level and database-level backups can be used with SharePoint Server 2016 unattached database recovery to restore site collections, sites, lists, and configurations.
  
(3) Content stored in remote BLOB stores cannot be restored by using System Center Data Protection Manager. 
  
(4) Changes to Web.config can be backed up by using file system backup from DPM.
  
(5) IIS configurations can be recovered by using a bare-metal backup from DPM. 
  
(6) DPM can recover this item by using a combination of a bare-metal backup and SharePoint Server 2016 backup. It cannot be backed up and recovered as an object. 
  
(7) Fully-trusted solution packages are stored in the configuration database, and sandboxed solutions are stored in content databases. They can be recovered as part of farm or content database recovery.
  
(8) Configuration settings can be recovered from farm-level backups. For more information, see [Restore farms in SharePoint Server](restore-a-farm.md). 
  
(9) The Central Administration content database and the configuration database for a SharePoint Server 2016 farm can be recovered but only as part of a full-farm recovery to the same farm, with the same computers. 
  
For more information, see [Announcement: Protect your Server 2016 workloads with Enhanced Security](https://go.microsoft.com/fwlink/?linkid=857509).
  
**SharePoint 2013 components for backup and recovery**

|**Component**|**SharePoint backup**|**SQL Server 2008 with Service Pack 1 (SP1) and Cumulative Update 2**|**SQL Server 2012**|**System Center 2012 - Data Protection Manager (DPM)**|**File system backup**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Farm  <br/> |Yes  <br/> |||Yes (6)  <br/> ||
|Service applications  <br/> |Yes  <br/> |||||
|Web application  <br/> |Yes  <br/> |||||
|Content databases  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> ||
|Site collection  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> |Yes (1, 2)  <br/> ||
|Site  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes  <br/> ||
|Document library or list  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes (2)  <br/> |Yes  <br/> ||
|List item or document  <br/> ||||Yes  <br/> ||
|Content stored in remote BLOB stores  <br/> |Yes (3)  <br/> |Yes (3)  <br/> |Yes (3)  <br/> |Yes (3)  <br/> ||
|Customizations deployed as solution packages  <br/> |Yes (7)  <br/> |Yes (7)  <br/> |Yes (7)  <br/> |Yes (6, 7)  <br/> ||
|Changes to Web.config made by using Central Administration or an API  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes (4)  <br/> ||
|SharePoint configuration settings  <br/> |Yes (2, 8)  <br/> |Yes (2, 8)  <br/> |Yes (2, 8)  <br/> |Yes (2, 9)  <br/> ||
|Customizations not deployed as solution packages  <br/> ||||Yes, files can be recovered if protected as files. (4, 5)  <br/> |Yes  <br/> |
|Changes to Web.config not made by using Central Administration or an API  <br/> ||||Yes (4)  <br/> |Yes  <br/> |
|IIS configurations not set through SharePoint 2013  <br/> ||||Yes (5)  <br/> |Yes  <br/> |
|SQL Server Reporting Services databases  <br/> ||Yes  <br/> |Yes  <br/> |Yes  <br/> ||
   
(1) Farm-level and database-level backup and restore can be used for site collection recovery if a single site collection is stored in a database. 
  
(2) Farm-level and database-level backups can be used with SharePoint 2013 unattached database recovery to restore site collections, sites, lists, and configurations.
  
(3) Content stored in remote BLOB stores cannot be restored by using System Center Data Protection Manager.
  
(4) Changes to Web.config can be backed up by using file system backup from DPM.
  
(5) IIS configurations can be recovered by using a bare-metal backup from DPM. 
  
(6) DPM can recover this item by using a combination of a bare-metal backup and SharePoint 2013 backup. It cannot be backed up and recovered as an object. 
  
(7) Fully-trusted solution packages are stored in the configuration database, and sandboxed solutions are stored in content databases. They can be recovered as part of farm or content database recovery.
  
(8) Configuration settings can be recovered from farm-level backups. For more information, see [Restore farms in SharePoint Server](restore-a-farm.md). 
  
(9) The Central Administration content database and the configuration database for a SharePoint 2013 farm can be recovered but only as part of a full-farm recovery to the same farm, with the same computers. 
  
> [!NOTE]
> You can register SharePoint 2013 with Windows Server Backup by using the stsadm.exe **-o -registerwsswriter** operation to configure the Volume Shadow Copy Service (VSS) writer for SharePoint 2013. Windows Server Backup then includes SharePoint 2013 in server-wide backups. When you restore from a Windows Server backup, you can select SharePoint Foundation (regardless of which version of SharePoint 2013 is installed), and all components reported by the VSS writer for SharePoint 2013 on that server at the time of the backup will be restored. > Windows Server Backup is recommended only for use with for single-server deployments. 
  
### Choose what to recover from within SharePoint content databases
<a name="section2"> </a>

From within a content database, you can recover site collections, sites, lists and libraries.
  
Backup and recovery tools provide different levels of recovery for content in a content database. Recovering an object from within a content database is always more complex than recovering the whole content database.
  
### Protecting customizations
<a name="section2"> </a>

Customizations to SharePoint sites can include the following: 
  
- Master pages, page layouts and cascading style sheets. These objects are stored in the content database for a web application.
    
- Web Parts, site or list definitions, custom columns, new content types, custom fields, custom actions, coded workflows, or workflow activities and conditions.
    
- Third-party solutions and their associated binary files and registry keys, such as IFilters.
    
- Changes to standard XML files.
    
- Custom site definitions (Webtemp.xml).
    
- Changes to the Web.config file.
    
How customizations are deployed, and how changes are made to the Web.config file, have a significant effect on which tools can be used to back up and recover customizations. To provide the greatest opportunity for recovery, we recommend that you use solution packages to deploy customizations and use Central Administration or the SharePoint APIs and object model to configure the Web.config file.
  
### Protecting workflows
<a name="Workflow"> </a>

Workflows are a special case of customizations that you can back up and recover. Make sure that your backup and recovery plan addresses any of the following scenarios that apply to your environment:
  
- Declarative workflows, such as those that you created in SharePoint Designer, are stored in the content database for the site collection to which they are deployed. Backing up the content database protects these workflows.
    
- Custom declarative workflow actions have components in the following three locations: 
    
  - The Visual Studio assemblies for the Activities are stored in the global assembly catalog (GAC).
    
  - The XML definition files (.ACTIONS files) are stored in the 15\TEMPLATE\{LCID}\Workflow directory.
    
  - An XML entry to mark the activity as an authorized type is stored in the Web.config file for the Web applications in which it is used.
    
    If your farm workflows use custom actions, you should use a file backup system to protect these files and XML entries. Similar to SharePoint Server features such as Web Parts and event receivers, these files should be reapplied to the farm as needed after recovery.
    
- Workflows that depend on custom code, such as those that are created by using Visual Studio, are stored in two locations. The Visual Studio assemblies for the workflow are stored in the global assembly catalog (GAC), and the XML definition files are stored in the Features directory. This is the same as other kinds of SharePoint Server features such as Web Parts and event receivers. If the workflow was installed as part of a solution package, backing up the content database protects these workflows. 
    
- If you create a custom workflow that interacts with a site collection other than the one where the workflow is deployed, you must back up both site collections to protect the workflow. This includes workflows that write to a history list or other custom list in another site collection. Performing a farm backup is sufficient to back up all site collections in the farm and all workflows that are associated with them. For more information, see "Back up workflows in SharePoint" in [Back up customizations in SharePoint Server](back-up-customizations.md).
    
- Workflows that are not yet deployed must be backed up and restored separately like any other data file. When you are developing a new workflow but have not yet deployed it to the SharePoint Server farm, make sure that you back up the folder where you store your workflow project files by using Windows Server Backup or another file system backup application.
    
### Protecting service applications
<a name="Workflow"> </a>

Service applications in a SharePoint Server environment can be made up of both service settings and one or more databases, or only service settings. You cannot restore a complete service application by restoring the database only. However, you can restore the databases for a service application and then provision the service application. For more information, see [Restore service applications in SharePoint Server](restore-a-service-application.md). 
  
### Protecting SQL Server Reporting Services databases
<a name="Workflow"> </a>

SharePoint Server backup and recovery does not include SQL Server Reporting Services databases. You must use SQL Server tools for SharePoint Server. For more information, see [Backup and Restore Operations for Reporting Services](http://go.microsoft.com/fwlink/p/?LinkID=718025&amp;clcid=0x409).
  
## Choose SharePoint backup and recovery tools
<a name="ChooseTools"> </a>

To select the correct tools for backup and recovery, you must determine whether you can meet the continuity requirements that you have set for your business within your budget for time and resources. 
  
Key things to consider when you select tools include the following: 
  
- Speed of backup: Can the tool perform within the maintenance window for your databases? You should test any backup system to make sure that it meets your needs on your hardware. 
    
- Completeness of recovery. 
    
- Granularity of objects that can be recovered.
    
- Backup type supported (full, differential, or incremental).
    
- Complexity of managing the tool.
    
For detailed information about the backup and recovery systems that can be used with SharePoint Server, see the following resources:
  
- [Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md)
    
- [Backing Up and Restoring Databases in SQL Server](http://go.microsoft.com/fwlink/p/?LinkID=724311&amp;clcid=0x409)
    
- [DPM overview](http://go.microsoft.com/fwlink/p/?LinkID=512012&amp;clcid=0x409)
    
## Determine SharePoint backup and recovery strategies
<a name="DetermineStrategies"> </a>

Based on your business requirements, recovery needs, and the tools that you have selected, determine and document the backup and recovery strategies for your environment.
  
It is common for IT departments that support SharePoint Server environments to decide to use more than one tool to protect the environment, as they determine the strategies that they will use.
  
For example, in an environment that has databases that are managed by DBAs, the strategies in the following list might be employed:
  
- All databases are backed up by SQL Server for SharePoint Server. The backup interval that is set is based on the following:
    
  - The importance of the content or service.
    
  - The effect on performance that the backup has on the environment.
    
- Small, quickly changing, very high-business-affect content databases are additionally protected by SQL Server database snapshots that are stored on a separate physical disk. Only one snapshot is stored per database, and snapshots are discarded regularly so that the effect on performance is minimized. The snapshot interval that is set for each database is based on the following:
    
  - The importance of the content or service.
    
  - The standard rate of change for the database.
    
  - The effect on performance that the snapshot has on the environment.
    
  - The amount of space that is required to store the snapshot.
    
    Recovering from a snapshot is faster than standard recovery because a snapshot, and its underlying database, can be treated by SharePoint Server as an unattached database. However, creating snapshots can decrease the performance of the underlying database. We recommend that the effect that snapshots have on the performance of the system be tested before they are implemented, and that snapshots be discarded regularly to reduce the space that is required. 
    
    > [!NOTE]
    > If you are using Remote Blob Storage (RBS), and the RBS provider that you are using does not support snapshots, you cannot use snapshots for backup. For example, the FILESTREAM provider does not support snapshots. 
  
- SharePoint Server backup is used to protect service applications. The backup interval is based on the following:
    
  - The importance of the service.
    
  - The standard rate of change for the database.
    
  - The effect on performance that the backup has on the database.
    
- All restore operations are performed through SharePoint Server. The choice of which restore system to use is determined by the kind of backup that is available and the object being restored.
    
Other tools should be part of your business continuity strategy. Consider how you will use recycle bins and versioning in site collections throughout the environment. For more information, see [Plan for high availability and disaster recovery for SharePoint Server](high-availability-and-disaster-recovery-concepts.md).
  
## Plan for performance when designing your SharePoint backup and recovery strategy
<a name="PlanEnhancedPerformance"> </a>

As you plan your backup and recovery strategy, consider the following recommendations to help you decrease the effect of backup and recovery on system performance. 
  
By design, most backup jobs consume as many I/O resources as they can to finish the job in the available time for maintenance. Therefore, you might see disk queuing and you might see that all I/O requests come back more slowly than usual. This is typical and should not be considered a problem.
  
### Follow recommendations for configuring SQL Server and storage

Follow the general recommendations for configuring SQL Server and storage for a SharePoint Server environment. For more information, see [Storage and SQL Server capacity planning and configuration (SharePoint Server)](storage-and-sql-server-capacity-planning-and-configuration.md).
  
### Minimize latency between SQL Server and the backup location

In general, use a local disk instead of a network drive for backups. If you are backing up multiple servers, you may want to have a directly connected computer that both servers can write to. Network drives that have 1 millisecond or less latency between them and the computers that are running SQL Server will perform well. If your farm has multiple servers in it (including the computer that is running SQL Server, you must use UNC network paths for the SharePoint farm backup location.
  
### Avoid processing conflicts

Do not run backup jobs during times in which users must have access to the system. 
  
To avoid I/O bottlenecks, perform the main backup to a separate disk, and only then copy to tape.
  
Consider staggering backups so that not all databases are backed up at the same time.
  
SharePoint Server backups use SQL Server backups. When using compression with your backups, be careful not to overwhelm SQL Server. For example, some third-party backup tools compress data during backup, which can disrupt SQL Server performance. There are tools available to throttle the compression processes and control the effect on SQL Server.
  
### Follow SQL Server backup and restore optimization recommendations

If you are running SQL Server Enterprise, we recommend that you use backup compression. For more information, see [Backup Compression (SQL Server)](https://go.microsoft.com/fwlink/?linkid=857510).
  
If you are using SQL Server or SQL Server 2008 R2 Express backups, use a combination of full, differential, and transaction log backups for the full recovery model to minimize recovery time. Differential database backups are usually faster to create than full database backups, and they reduce the amount of transaction log required to recover the database.
  
If you are using the full recovery model in SQL Server 2008, we recommend that you use the truncate option during backup to avoid maintenance issues. 
  
For detailed recommendations about how to optimize SQL Server backup and restore performance, see [Optimizing Backup and Restore Performance in SQL Server](http://go.microsoft.com/fwlink/p/?LinkId=126630).
  
### Ensure sufficient write performance on the backup drive

Carefully consider whether to use redundant array of independent disks (RAID) on your disk backup device. For example, RAID 5 has low write performance, approximately the same speed as for a single disk. (This is because RAID 5 maintains parity information.) Using RAID 10 for a backup device may provide faster backups. For more information about how to use RAID with backups, see [Configure RAID for maximum SQL Server I/O throughput](http://go.microsoft.com/fwlink/p/?LinkId=126632 ).
  
## See also
<a name="PlanEnhancedPerformance"> </a>

#### Concepts

[Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md)
#### Other Resources

[Data Protection and Recovery](http://go.microsoft.com/fwlink/p/?LinkID=199237)

