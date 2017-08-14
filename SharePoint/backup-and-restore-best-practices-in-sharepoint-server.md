---
title: Backup and restore best practices in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: d7d2dff9-c7a9-402b-958a-d233cbacab8f
---


# Backup and restore best practices in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to implement best practices before you back up and restore a SharePoint Server 2016 and SharePoint Server 2013 farm.Best practices for backup and restore help make sure that backup and restore operations in SharePoint Server are successful and that the environment is protected against data loss or continuity gaps.In this article:
-  [Performance best practices](#section_perf)
    
  
-  [Quality assurance best practices](#section_QA)
    
  
-  [Procedural best practices](#section_PROC)
    
  

## Performance best practices for SharePoint backup and restore operations
<a name="section_perf"> </a>

Backup and restore operations consume server resources and limit server performance while the operations are running. Follow these recommended practices to help reduce resource usage and increase the performance of servers and the backup or restore task.
## Minimize latency between SQL Server and the backup location

In general, it is efficient to back up to a local disk on the database server instead of a network drive. You can then copy the data later to a shared folder on the network. Network drives with 1 millisecond or less latency between them and the database server perform well.
> [!NOTE:]

  
    
    

To avoid I/O bottlenecks, perform the main backup to a separate disk from the disk running SQL Server 2014, SQL Server 2008 R2 with Service Pack 1 (SP1) and SQL Server 2012UNRESOLVED_TOKEN_VAL(). For more information, see  [Define a Logical Backup Device for a Disk File (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717191&amp;clcid=0x409).By design, most backup jobs consume all available I/O resources to complete the job. Therefore, you might see disk queuing, which can result in greater than usual latency for I/O requests. This is typical and should not be considered a problem. For more information, see  [Monitor Disk Usage](http://go.microsoft.com/fwlink/p/?LinkID=717192&amp;clcid=0x409).
## Avoid processing conflicts

Do not run backup jobs during times when users need access to the system. Typically, systems run 24 hours a day, seven days a week. A best practice is to always run incremental backups to safeguard against server failure. Consider staggering backups so that all databases are not backed up at the same time.
## Keep databases small for faster recovery times

Keep databases small to speed both backup and restore. For example, use multiple content databases for a web application instead of one large content database. For more information, see  [Database types and descriptions in SharePoint Server](html/database-types-and-descriptions-in-sharepoint-server.md). For a graphical overview of the databases that support SharePoint Server 2016, see  [Quick reference guide: SharePoint Server 2016 databases](https://doc.co/qrafhS). You can also download this SharePoint Server 2016 database poster, as either a  [PDF](https://download.microsoft.com/download/D/5/D/D5DC1121-8BC5-4953-834F-1B5BB03EB691/DBrefguideSPS2016_tabloid.pdf) or [Visio](https://download.microsoft.com/download/D/5/D/D5DC1121-8BC5-4953-834F-1B5BB03EB691/DBrefguideSPS2016_tabloid.vsdx) file.
## Use incremental backups for large databases

Use incremental backups for large databases because you can make them quickly and maintain performance of the environment. Although you can restore full backups faster than incremental backups, continuous incremental backups minimize data loss. For more information about types of backups, see  [Backup Overview (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717240&amp;clcid=0x409).
## Use compression during backup

In some circumstances, you can use compression to decrease the size of backups and the time to complete each backup. Backup compression was introduced in SQL Server 2008 Enterprise. Backup compression increases CPU usage and this can affect SQL Server concurrent operations.
> [!IMPORTANT:]

  
    
    

For more information about how backup compression affects performance in SQL Server, see  [Backup Compression (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717243&amp;clcid=0x409).
## Follow SQL Server backup and restore optimization recommendations

SQL Server backups use a combination of full, differential, and transaction log backups (for the full or bulk-logged recovery model) to minimize recovery time. Differential database backups are usually faster to create than full database backups and reduce the number of transaction logs required to recover the database.If you are using the full recovery model, we recommend that you periodically truncate the transaction log files to avoid maintenance issues. For detailed recommendations about how to optimize SQL Server backup and restore performance, see  [Optimizing Backup and Restore Performance in SQL Server](http://go.microsoft.com/fwlink/p/?LinkId=126630).
## Use RAID 10 if you use RAID

Carefully consider whether to use redundant array of independent disks (RAID) on the device to which you back up data. For example, RAID 5 has slow write performance, approximately the same speed as for a single disk. This is because RAID 5 has to maintain parity information. RAID 10 can provide faster backups because it doesn't need to manage parity. Therefore, it reads and writes data faster. For more information about how to use RAID with backups, see  [Configure RAID for maximum SQL Server I/O throughput](http://go.microsoft.com/fwlink/p/?LinkId=126632 ) and [RAID Levels and SQL Server](http://go.microsoft.com/fwlink/p/?LinkId=282316).
## Configure SharePoint settings to improve backup or restore performance

You can only configure file compression and log file settings in PowerShell. You can configure backup and restore threads in both the SharePoint Central Administration website and PowerShell to increase backup or restore efficiency and performance.If you use the Export-SPWeb PowerShell cmdlet, you can use the NoFileCompression parameter. By default, SharePoint Server uses file compression while exporting web applications, site collection, lists, or document libraries. You can use this parameter to suppress file compression while exporting and importing. File compression can use up to 30% more resources. However, the exported file uses approximately 25% less disk space. If you use theNoFileCompression parameter when you export, you have to also use it when you import the same content.You can also use the NoLogFile parameter. By default, SharePoint Server always creates a log file when you export content. Although you can use this parameter to suppress log file creation to save resources, we recommend that you always create logs. Logs are important for troubleshooting and log creation does not use many resources such as CPU or memory.When you use the Backup-SPFarm cmdlet, you can also use theBackupThreads parameter to specify how many threads SharePoint Server will use during the backup process. A higher number of threads will consume more resources during backup. But the overall time to make the backup is decreased. Because each thread is recorded in the log files, the number of threads does affect log file interpretation. By default, three threads are used. The maximum number of available threads is 10.
> [!NOTE:]

  
    
    


## Consider site collection size when you determine the tools to use

If the business requires site collection backups in addition to farm-level or database-level backups, choose a backup tool that is based on the size of the site collection.
- **15-100 GB:** UsetheBackup-SPSite, a SharePoint Server tool, a SQL Server tool, or other database backup tool to protect the content database that contains the site collection. For more information, see  [Back up site collections in SharePoint Server](html/back-up-site-collections-in-sharepoint-server.md).
    
  
- **Larger than 100 GB:** Use a differential backup solution, such as SQL Server or System Center Data Protection Manager R2, instead of the built-in backup and recovery tools.
    
  

## Quality assurance best practices to back up a SharePoint farm
<a name="section_QA"> </a>

Follow these best practices to help ensure the quality of the backups of the farm environment and reduce the chances of data loss.
## Ensure you have enough storage space

Be certain that the system has enough disk space to accommodate the backup. Configure a backup job in Central Administration to verify the required disk space.
## Routinely test backup quality

Routinely test backups and validate their consistency. Run practice recovery operations to validate the contents of the backup and to make sure that you can restore the complete environment. To prepare for disaster recovery of geographically dispersed environments, set up a remote farm. Then you can restore the environment by using the database-attach method to upload a copy of the database to the remote farm and redirect users. Periodically perform a trial data recovery action to verify that the process correctly backs up files. A trial restoration can expose hardware problems that do not come up with software verifications and can also to make sure that the recovery time objectives (RTO) are met.
## Back up ULS trace logs

The SharePoint Server backup process doesn't back up the Unified Logging Service (ULS) trace logs. Data in ULS trace logs can be useful for performance analysis, troubleshooting, and monitoring compliance with service level agreements. Therefore, protect this data as part of the routine maintenance.By default, SharePoint log files are at C:\\Program files\\Common Files\\Microsoft Shared\\Web Server Extensions\\16\\Logs. The files are named with the server name followed by the date and time stamp. The SharePoint trace logs are created at set intervals and when you use the IISRESET command.
## Store a copy of backup files off-site

To safeguard against loss from a natural disaster that destroys the primary data center, maintain duplicate copies of backups in separate locations from the servers. Duplicate copies can help prevent the loss of critical data. As a best practice, keep three copies of the backup media, and keep at least one copy offsite in a controlled environment. This should include all backup and recovery materials, documents, database and transaction log backups, and usage and trace log backups.
## Procedural best practices to back up and restore SharePoint Server
<a name="section_PROC"> </a>

Use the following procedural best practices to plan and perform backup and restore operations.
## Use FQDN server names

When you refer to servers in a different domain, always use fully qualified domain names (FQDN).
## Keep accurate records

When you deploy SharePoint Server, record the accounts that you create, the computer names, passwords, and setup options. Keep this information in a safe and secure location. Possibly, keep multiple records to make sure this information is always available. 
## Have a recovery environment ready

Use a farm in a secondary location to validate the success of restore operations as part of your disaster recovery strategy. For more information, see  [Choose a disaster recovery strategy for SharePoint Server](html/choose-a-disaster-recovery-strategy-for-sharepoint-server.md). In a disaster recovery situation, you can then restore the environment by using the database-attach method to upload a copy of the database to the remote farm and redirect users. For more information, review and follow the steps in  [Restore farms in SharePoint Server](html/restore-farms-in-sharepoint-server.md). Also for a high availability solution, you can set up a standby environment that runs the same version of software as the production environment so that you can restore the databases and recover documents quickly. For more information, see  [Describing high availability](high-availability-and-disaster-recovery-concepts-in-sharepoint-server.md#DescHA).
## Schedule backup operations

Use PowerShell backup and recovery cmdlets to create a script file (*.ps1) and then schedule it to run with Windows Task Scheduler. This makes sure that all backup operations are run at the best time when the system is least busy and users are not accessing it. For more information, see the following:
-  [Running Scripts](https://go.microsoft.com/fwlink/p/?LinkID=178144)
    
  
- **Backup and recovery cmdlets in SharePoint Server 2016**
    
  

## Use the SQL FILESTREAM provider with BLOB storage

Remote BLOB Storage (RBS) is supported in a SharePoint Server farm. There are both pros and cons associated with using RBS in SharePoint Server. One related limitation of RBS with a SharePoint farm is that System Center Data Protection Manager cannot use the FILESTREAM provider to back up or restore RBS. SharePoint Server supports the FILESTREAM provider for backup and restore operations. A benefit of RBS with a SharePoint farm is that you can use either SharePoint tools or SQL Server tools to back up and restore the content database with the Remote BLOB Store (RBS) defined. This backs up and restores both the RBS and the content database. We do not recommend that you use RBS with other restore methods. For more information about the benefits and limitations of using RBS, see  [Deciding to use RBS in SharePoint Server](html/deciding-to-use-rbs-in-sharepoint-server.md). Download  [Microsoft SQL Server 2014 Feature Pack](http://go.microsoft.com/fwlink/p/?LinkID=733635&amp;clcid=0x409)that includes RBS.
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


# See also

#### 

 [Overview of backup and recovery in SharePoint Server](html/overview-of-backup-and-recovery-in-sharepoint-server.md)
  
    
    
 [Plan for backup and recovery in SharePoint Server](html/plan-for-backup-and-recovery-in-sharepoint-server.md)
  
    
    
 [Prepare to back up and restore farms in SharePoint Server](html/prepare-to-back-up-and-restore-farms-in-sharepoint-server.md)
  
    
    

#### 

 [Database Backup Encryption](http://go.microsoft.com/fwlink/p/?LinkID=733741&amp;clcid=0x409)
  
    
    

  
    
    

