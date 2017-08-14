---
title: Best practices for SQL Server in a SharePoint Server farm
ms.prod: SHAREPOINT
ms.assetid: d1c43543-2363-4762-882f-13f06295d0d5
---


# Best practices for SQL Server in a SharePoint Server farm
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-07* **Summary:** Learn how to implement best practices for SQL Server in a SharePoint Server 2016 and SharePoint Server 2013 farm.When you configure and maintain SharePoint Server 2016 relational databases on SQL Server 2014 with Service Pack 1 (SP1) or SQL Server 2016, you have to choose options that promote performance and security. Likewise, you have to choose options that promote performance and security when you configure and maintain SharePoint Server 2013 relational databases on SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, and SQL Server 2014.The best practices in this article are ordered based on the sequence in which they would apply, from installing and configuring SQL Server, to deploying SharePoint Server, and then maintaining the farm. Most of the practices apply to all versions of SQL Server. Practices that are unique to SQL Server versions are shown in separate sections. 
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    


## Use a dedicated server for SQL Server

To ensure optimal performance for farm operations, we recommend that you install SQL Server on a dedicated server that does not run other farm roles and does not host databases for other applications. The only exception is deployment of SharePoint Server 2016 in a Single-Server farm role or SharePoint 2013 on a stand-alone server, which is meant for development or testing, and is not recommended for production use. For more information, see  [Description of MinRole and associated services in SharePoint Server 2016](html/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md) and [Install SharePoint Server 2016 on a single server with SQL Server](html/install-sharepoint-server-2016-on-a-single-server-with-sql-server.md).
> [!NOTE:]

  
    
    


## Configure specific SQL Server settings before you deploy SharePoint Server

To ensure consistent behavior and performance, configure the following options and settings before you deploy SharePoint Server. 
- Do not enable auto-create statistics on SharePoint content databases. Enabling auto-create statistics is not supported for SharePoint Server. SharePoint Server configures the required settings during provisioning and upgrade. Manually enabling auto-create statistics on a SharePoint database can significantly change the execution plan of a query. The SharePoint databases either use a stored procedure that maintains the statistics (proc_UpdateStatistics) or rely on SQL Server to do this. 
    
  
- Set max degree of parallelism (MAXDOP) to 1 for instances of SQL Server that host SharePoint databases to make sure that a single SQL Server process serves each request. 
    
    > [!IMPORTANT:]
      
- To help simplify maintenance, such as to make it easier to move databases to another server, create DNS aliases that point to the IP address for all instances of SQL Server. For more information about DNS or Hostname aliases, see  [How to Add a Hostname Alias for a SQL Server Instance](https://go.microsoft.com/fwlink/p/?LinkID=279159).
    
  
For more information about these SQL Server settings and options, see  [Set SQL Server options](storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md#Section6_3).
## Harden the database server before you deploy SharePoint Server

We recommend that you plan for, and harden the database server before you deploy SharePoint Server. For more information, see:
-  [Securing SQL Server](http://go.microsoft.com/fwlink/?LinkID=809089&amp;clcid=0x409)
    
  
-  [Configure SQL Server security for SharePoint Server 2016](html/configure-sql-server-security-for-sharepoint-server-2016.md)
    
  
-  [Securing SharePoint: Harden SQL Server in SharePoint Environments](https://blogs.technet.com/b/rycampbe/archive/2013/10/14/securing-sharepoint-harden-sql-server-in-sharepoint-environments.aspx)
    
  
-  [Security Center for SQL Server Database Engine and Azure SQL Database](http://go.microsoft.com/fwlink/?LinkID=800298&amp;clcid=0x409)
    
  

## Configure database servers for performance and availability

As is the case with front-end servers and application servers, the configuration for database servers affects how well SharePoint Server performs. Some databases have to be on the same server as other databases. Conversely, some databases cannot be on the same server as other databases. For more information, see  [Description of MinRole and associated services in SharePoint Server 2016](html/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md) and [Storage and SQL Server capacity planning and configuration (SharePoint Server)](html/storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md).For guidance about highly available databases that use mirroring, see  [Database Mirroring (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=718062&amp;clcid=0x409).
## SQL Server Failover Clustering and Always On Availability Groups

SQL Server 2012 introduced the AlwaysOn Availability Groups feature. This feature is a high availability and disaster recovery solution that's an alternative to database mirroring and log shipping solutions. AlwaysOn Availability Groups now support up to nine availability replicas.
> [!NOTE:]

  
    
    

AlwaysOn Availability Groups require a Windows Server Failover Clustering (WSFC) cluster. A WSFC resource group is created for every availability group that is created. For more information, see the following resources:
-  [AlwaysOn Availability Groups (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=718032&amp;clcid=0x409)
    
  
-  [Overview of AlwaysOn Availability Groups (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=809090&amp;clcid=0x409)
    
  
-  [Failover Clustering and Always On Availability Groups (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=800301&amp;clcid=0x409)
    
  

## Design storage for optimal throughput and manageability

We recommend that you separate, and prioritize your data among the drives on the database server. Ideally, you should place the tempdb database, content databases, usage database, search databases, and transaction logs on separate physical hard disks. The following list provides some guidance. For more information, see  [Configure databases](storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md#Section6_5).
- For collaboration or update-intensive sites, use the following ranking for storage distribution.
    
    The highest ranked item should be in the fastest drives.
    
1. tempdb data files and transaction logs
    
  
2. Content database transaction log files
    
  
3. Search databases, except for the Search administration database
    
  
4. Content database data files
    
  
- In a heavily read-oriented portal site, prioritize data and search over transaction logs as follows.
    
    The highest ranked item should be in the fastest drives.
    
1. tempdb data files and transaction logs
    
  
2. Content database data files
    
  
3. Search databases, except for the Search administration database
    
  
4. Content database transaction log files
    
  
- Testing and user data shows that insufficient disk I/O for tempdb can significantly impede overall farm performance. To avoid this issue, allocate dedicated disks for the drive that stores tempdb data files.
    
  
- For best performance, use a RAID 10 array for the drive that stores tempdb data files. The number of tempdb data files should equal the number of CPU cores, and each tempdb data file should be set to the same size.
    
  
- Separate database data and transaction log files across different disks. If data and log files must share disks due to space limitations, put files that have different usage patterns on the same disk to minimize concurrent access requests.
    
  
- Use multiple data files for heavy-use content databases, and put each on its own disk
    
  
- To improve manageability, monitor and make adjustments as needed to keep content databases below 200 GB, rather than restrict the database size.
    
    > [!NOTE:]
      
Proper configuration of I/O subsystems is very important to the optimal performance and operation of SQL Server systems. For more information, see  [Monitoring Disk Usage](https://social.technet.microsoft.com/wiki/contents/articles/3214.monitoring-disk-usage.aspx)
> [!TIP:]

  
    
    


## Proactively manage the growth of data and log files

Following are recommendations to proactively manage the growth of data and log files:
- When possible, increase all data files and log files to their expected final size, or periodically increase these at set periods, for example, every month or every six months, or before rollout of a new storage-intensive site such as during file migrations. 
    
  
- Enable database autogrowth as a protective measure to make sure that you do not run out of space in data and log files. Consider the following: 
    
    > [!IMPORTANT:]
      

  - The default settings for a new database are to grow by 1 MB increments. Because this default setting for autogrowth results in increases in the size of the database, do not rely on the default setting. Instead, use the guidance provided in  [Set SQL Server options](storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md#Section6_3).
    
  
  - Set autogrowth values to a fixed number of megabytes instead of to a percentage. The bigger the database, the bigger the growth increment should be. 
    
    > [!NOTE:]
      

    Consider for example, a scenario where content is gradually increased, say at 100MB increments, and autogrowth is set at 10MB. Then suddenly a new document management site requires a very large amount of data storage, perhaps with initial size of 50 GB. For this large addition, growth at 500 MB increments is more appropriate than 10MB increments. 
    
  
  - For a managed production system, consider autogrowth to be merely a contingency for unexpected growth. Do not use the autogrow option to manage your data and log growth on a day-to-day basis. Instead, set the autogrowth to allow for an approximate size in one year and then add a 20 percent margin for error. Also set an alert to notify you when the database runs low on space or approaches a maximum size.
    
  
- Maintain a level of at least 25 percent available space across drives to accommodate growth and peak usage patterns. If you add drives to a RAID array or allocate more storage to manage, monitor capacity closely to avoid running out of space.
    
  

## Continuously monitor SQL Server storage and performance

We recommend that you continuously monitor SQL Server storage and performance to make sure that each production database server is adequately handling the load put on it. Additionally, continuous monitoring enables you to establish benchmarks that you can use for resource planning. Take a comprehensive view of resource monitoring. Do not limit monitoring to resources that are specific to SQL Server. It is equally important to track the following resources on computers that are running SQL Server: CPU, memory, cache/hit ratio, and the I/O subsystem.When one or more of the server resources seems slow or overburdened, consider the following performance guidelines based on the current and projected workload.
-  [Monitor and Tune for Performance](http://go.microsoft.com/fwlink/?LinkID=718063&amp;clcid=0x409)
    
  
-  [Performance Monitoring and Tuning Tools](http://go.microsoft.com/fwlink/?LinkID=809092&amp;clcid=0x409)
    
  
-  [Server Performance and Activity Monitoring](http://go.microsoft.com/fwlink/?LinkID=809093&amp;clcid=0x409)
    
  
-  [Windows Performance Monitor](http://go.microsoft.com/fwlink/?LinkID=809094&amp;clcid=0x409)
    
  

## Use backup compression to speed up backups and reduce file sizes

Backup compression can speed up SharePoint backup operations. It is available in SQL Server Standard and Enterprise Edition. If you set the compression option in your backup script or configure SQL Server to compress by default, you can significantly reduce the size of your database backups and shipped logs. For more information, see  [Backup Compression (SQL Server)](http://go.microsoft.com/fwlink/?LinkID=717243&amp;clcid=0x409) and [Data Compression](http://go.microsoft.com/fwlink/?LinkID=718120&amp;clcid=0x409), or  [Enable Compression on a Table or Index](http://go.microsoft.com/fwlink/?LinkID=798229&amp;clcid=0x409)
## Acknowledgements

The SharePoint Server Content Publishing team thanks the following contributors to this article:
- Kay Unkroth, Senior Program Manager, SQL Server
    
  
- Chuck Heinzelman, Senior Program Manager, SQL Server
    
  

# See also

#### 

 [Overview of SQL Server in a SharePoint Server 2016 environment](html/overview-of-sql-server-in-a-sharepoint-server-2016-environment.md)
  
    
    
 [Storage and SQL Server capacity planning and configuration (SharePoint Server)](html/storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md)
  
    
    

#### 

 [Securing SharePoint: Harden SQL Server in SharePoint Environments](https://blogs.technet.com/b/rycampbe/archive/2013/10/14/securing-sharepoint-harden-sql-server-in-sharepoint-environments.aspx)
  
    
    

  
    
    

