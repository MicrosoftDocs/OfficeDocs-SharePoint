---
title: "Prepare to back up and restore farms in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 56ea0f40-426b-43da-aff5-187fe5adc946
description: "Learn how to prepare to back up and restore your SharePoint Server farm."
---

# Prepare to back up and restore farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
It is important to make sure that you have backed up and can recover the data that you need if a failure occurs. Consider the information, procedures, and precautions in this article before you back up and restore your environment. This article discusses restrictions and requirements for backup and recovery and how to create a shared folder on the network that can receive backed-up data.
  
## Requirements to back up and restore SharePoint Server

- Before you back up data, create a shared folder that stores the data. For best performance, create this folder on the database server. If you want to archive the backups to another server, you can copy the whole backup folder to that server after backup is complete. Be sure to copy and move the whole backup folder and not the individual backup folders under this folder.
    
- The SQL Server VSS Writer service, which is available with SQL Server 2008 R2 and SQL Server 2012 database software, must be started for the SharePoint Server 2013 VSS Writer service to work correctly. By default, the SharePoint Server 2013 VSS Writer service is not automatically started.
    
    This does not apply for SharePoint Server 2016 when you use SQL Server 2014 Service Pack 1 (SP1) or SQL Server 2016 because both of these database servers automatically start the VSS Writer service.
    
- For SharePoint Server 2013, make sure that the SharePoint Foundation 2013 Administration service is started on all farm servers before you perform a backup. By default, this service is not started on stand-alone installations.
    
- Make sure that the user accounts that you want to perform a backup have access to the shared backup folder.
    
- If you use Central Administration to back up, the database server's SQL service account, the Timer service account, and the Central Administration application pool identity account must have Full Control permissions to the backup locations.
    
- The database server and farm server that you want to back up must be able to connect to one another.
    
- If you use SQL Server with Transparent Data Encryption (TDE), and you use either SharePoint tools or SQL Server tools to back up your environment, the TDE encryption key is not backed up or restored. You must manually back up the key. When you restore the environment, you must manually restore the key before you restore the data. For more information, see [Understanding Transparent Data Encryption (TDE)](http://go.microsoft.com/fwlink/p/?LinkID=715574&amp;clcid=0x409).
    
### Restrictions when you back up and restore SharePoint Server

You can't back up or restore everything in a SharePoint environment. For more information about backup and recovery architecture and about backup and restore restrictions, see [Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md).
  
- You cannot use a backup made from one version to restore to another version.
    
- You can use a backup made from one version to upgrade to another version.
    
- The update level of the farm to which you restore cannot be lower than the update level of a backup.
    
    The destination farm must have the same or newer update level. For information about how to upgrade, see [Upgrade to SharePoint Server 2016](../upgrade-and-update/upgrade-to-sharepoint-server-2016.md).
    
If you perform a backup while a task that creates or deletes databases is running, pending changes might not be included in the backup.
  
Do not modify the spbackup.xml file. SharePoint Server uses this file. A change can make the backups unusable.
  
### How to create a shared folder

Use this procedure to create a shared folder on the network that can receive and hold backed up data. You can also use this shared folder when you restore data. If you already have a shared folder that serves this purpose, you do not have to perform this procedure. By performing the following procedure, you ensure that you can access the shared folder from the computer that runs SQL Server database software and from the computer that hosts the SharePoint Central Administration website.
  
 **To create a shared folder**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the computer on which you want to create the shared folder.
    
2. If you create the shared folder on a computer other than the one running SQL Server, make sure that the service account for SQL Server (MSSQLSERVER) is using a domain user account and that it has Full Control permissions on the shared folder.
    
3. On the server on which you want to store the backup data, create a folder.
    
4. On the **Sharing** tab of the **Properties** dialog box, click **Advanced Sharing**, and then click **Permissions**, add the following accounts and assign them Full Control of the shared folder:
    
   - SQL Server service account (MSSQLSERVER)
    
   - The SharePoint Central Administration application pool identity account
    
   - The SharePoint Timer service account.
    
## See also

#### Concepts

[Backup solutions in SharePoint Server](backup.md)
  
[Restore solutions in SharePoint Server](restore.md)

