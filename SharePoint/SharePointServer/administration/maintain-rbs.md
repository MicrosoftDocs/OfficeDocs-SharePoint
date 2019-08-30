---
title: "Maintain RBS in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0adff5f5-26d3-439f-86fa-0f0f8e0b8fc5
description: "Learn how to perform maintenance tasks that are associated with Remote BLOB Storage (RBS) in SharePoint Server."
---

# Maintain RBS in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You perform most of the maintenance tasks associated with RBS in SharePoint Server by using the RBS Maintainer, which is a tool in SQL Server. The RBS Maintainer performs periodic garbage collection and other maintenance tasks for a SharePoint Server RBS deployment. You can schedule these tasks for each database that uses RBS by using Windows Task Scheduler or SQL Server Agent. You must provision the RBS Maintainer by using command-line parameters or through an XML file. In the case of mirrored or replicated databases, you can run the RBS Maintainer against any single instance.
  
    
## Configure RBS Garbage collection
<a name="proc1"> </a>

SharePoint Server automatically marks unreferenced or deleted BLOB data for removal. SharePoint Server counts references to BLOBs by looking at the list of BLOB IDs stored by SharePoint Server in its content databases at the time of removal. Any BLOB references that are present in the RBS store tables but absent in the content database are assumed to be deleted by SharePoint Server and will be marked for removal. BLOBs that are not present in the content database and were created before the orphan cleanup time window, described later in this article, are also assumed to be deleted by SharePoint Server and will be marked for removal. 
  
Because SharePoint Server tabulates BLOB references from the RBS columns of the content database, every RBS column must have a valid index before it can be registered in RBS.
  
The SQL Server RBS Maintainer tool removes the items marked by SharePoint Server for removal. You should schedule the clean-up tasks to be run during off-peak hours to reduce the effect on regular database operations.
  
RBS garbage collection is performed in the following three steps:
  
- Reference scan. The first step compares the contents of the RBS tables in the SharePoint Server content database that has RBS's own internal tables and determines which BLOBs are no longer referenced. Any unreferenced BLOBs are marked for deletion.
    
- Delete propagation. The next step determines which BLOBs were marked for deletion for some time longer than the garbage_collection_time_window value and deletes them from the BLOB store.
    
- Orphan cleanup. The final step determines whether any BLOBs are present in the BLOB store but absent in the RBS tables. These orphaned BLOBs are then deleted.
    
### Configuring RBS garbage collection

You can configure garbage collection by specifying the following RBS Maintainer settings and database settings:
  
- Maintainer schedule. This setting determines how often the RBS Maintainer will be run.
    
- Task Duration. This setting determines the maximum length that a single RBS Maintainer task can run. The default setting is two hours.
    
You should configure the RBS Maintainer so that its activity has minimal effect on regular activity. For information about database garbage collection settings, such as how to configure the settings, see [Running RBS Maintainer](https://go.microsoft.com/fwlink/p/?LinkId=199638).
  
## RBS and BLOB store consistency checks
<a name="proc2"> </a>

The RBS Maintainer verifies the integrity of RBS BLOB references and corrects any errors that are found. It performs several consistency checks for the database, such as verifying that indexes exist for the RBS columns, and verifying that all BLOBs that are referenced by SharePoint Server exist in RBS.
  
The Auxiliary Table Consistency Check verifies that the RBS auxiliary tables are in a consistent state. The checks performed are the following:
  
- Verify that each RBS table column has a valid index.
    
- Verify that RBS table columns exist; have enabled, valid indexes; and have the correct column type.
    
Although you can disable the following consistency checks, we recommend that you do not disable them because they help ensure the consistency of your RBS store. By default, the following consistency checks are enabled:
  
- Verify that all BLOBs that are referenced by SharePoint Server are present in the RBS tables.
    
- Verify that no BLOBs are marked as both in use and deleted.
    
Any discovered problems are logged and the RBS Maintainer attempts to fix them by creating missing index entries, unregistering missing columns, or marking in-use BLOBs as not deleted.
  
## Running the RBS Maintainer
<a name="proc3"> </a>

RBS requires you to define a connection string to each database that uses RBS before you run the RBS Maintainer. This string is stored in a configuration file in the  _\<RBS installation path\>_\Microsoft SQL Remote Blob Storage 10.50\Maintainer folder that is ordinarily created during installation. The RBS Maintainer can be run manually by executing the Microsoft.Data.SqlRemoteBlobs.Maintainer.exe program together with the command line parameters that are listed in [Running RBS Maintainer](https://blogs.msdn.microsoft.com/sqlrbs/2010/03/19/running-rbs-maintainer/). 
  
You must schedule a separate RBS Maintainer task for every database that uses RBS. The following steps describe how to schedule an RBS Maintainer task.
  
 **To schedule an RBS Maintainer task**
  
1. Verify that you have Write permissions for the folder where you installed RBS. 
    
2. Add a connection string to the  _\<RBS installation directory\>\_Maintainer\Microsoft.Data.SqlRemoteBlobs.Maintainer.exe.config file for the RBS Maintainer task that is to be performed. The RBS installer creates one connection string that is named RBSMaintainerConnection by using the connection information that was provided during setup. However, new connection strings must be added for every additional database.
    
    If you are using Windows authentication, the connection string does not have to be encrypted. You can add the unencrypted connection string by running the following command:
    
    **aspnet_regiis -pef connectionStrings . -prov DataProtectionConfigurationProvider**
  
 **rename web.config Microsoft.Data.SqlRemoteBlobs.Maintainer.exe.config**
    
    If you are using SQL authentication, the RBS Maintainer connection strings must be in an encrypted format. Therefore, to add connection strings, either the new strings must be encrypted or all the connection strings must be decrypted. Encrypted strings must be added one at a time. However all the connection strings can be decrypted at the same time by using the %windir%\Microsoft.net\Framework\ _\<version\>_\Aspnet_regiis.exe tool, which is distributed as a part of the Microsoft .NET Framework.
    
    Run the following commands to decrypt the connection strings and store the results in a Web.config file:
    
    **rename Microsoft.Data.SqlRemoteBlobs.Maintainer.exe.config web.config**
  
 **aspnet_regiis -pdf connectionStrings**
    
    Strings can then be added in decrypted form and the file can be encrypted and renamed to Microsoft.Data.SqlRemoteBlobs.Maintainer.exe.config by using the following commands:
    
    **aspnet_regiis -pef connectionStrings . -prov DataProtectionConfigurationProvider**
  
 **rename web.config Microsoft.Data.SqlRemoteBlobs.Maintainer.exe.config**
    
3. Create a Windows scheduler task to run the RBS Maintainer task for each applicable database. If you ran the RBS installer in GUI mode, it automatically created a Windows scheduler task. However, if you ran the RBS installer in command-line mode, you must follow these steps every time that you schedule a task to run the RBS Maintainer:
    
  - On the Start menu, click **Administrative Tools**, and then click **Task Scheduler**.
    
  - On the **Action** menu, click **Create Task**.
    
  - On the **Actions** tab, click **New**.
    
  - In the **New Action** dialog box, in the **Action** drop-down list, select **Start a program**.
    
  - Under **Settings**, in the **Program/script** box, browse to the Maintainer binary file  _\<RBS installation directory\>_\Maintainer\Microsoft.Data.SqlRemoteBlobs.Maintainer.exe, and in the **Add arguments (optional)** text box, add any optional arguments. The following default values are created by the installer: 
    
    \<-ConnectionStringName RBSMaintainerConnection\>, \<-Operation GarbageCollection ConsistencyCheck ConsistencyCheckForStores\>, \<-GarbageCollectionPhases rdo\>, \<-ConsistencyCheckMode r\>, \<-TimeLimit 120\>
    
  - Click **OK**.
    
  - On the **Triggers** tab, click **New**. 
    
  - In the **New Trigger** dialog box, schedule the task, and then click **OK**. We recommend that you schedule the task to run during low system activity times.
    
  - On the **General** tab, under **Security**, make sure that the user account has the appropriate permissions to run the task. You can change permissions by clicking **Change User or Group**.
    
  - On the **General** tab, click **Run whether user is logged on or not**, and then click **OK**.
    
## See also
<a name="proc3"> </a>

#### Concepts

[Overview of RBS in SharePoint Server](rbs-overview.md)
  
[Install and configure RBS with FILESTREAM in a SharePoint Server farm](install-and-configure-rbs.md)
  
[Set a content database to use RBS with FILESTREAM in SharePoint Server](set-a-content-database-to-use-rbs.md)
  
[Migrate content into or out of RBS in SharePoint Server](migrate-content-into-or-out-of-rbs.md)
  
[Disable RBS on content databases in SharePoint Server](disable-rbs-on-a-content-database.md)

