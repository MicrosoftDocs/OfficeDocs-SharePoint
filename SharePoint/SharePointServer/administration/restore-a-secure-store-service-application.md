---
title: "Restore Secure Store Service applications in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 237d399e-b50b-42e6-90ff-e659a94d8099
description: "Learn how to restore the Secure Store Service application in SharePoint Server."
---

# Restore Secure Store Service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can restore the Secure Store service application by using the SharePoint Central Administration website or PowerShell. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

The Secure Store Service provides the capability of securely storing credential sets and associating credentials to specific identities or a group of identities.
  
Before you begin this operation, review the following information about the Secure Store service application:
  
- Every time that you enter a new passphrase, SharePoint Server creates a new Master Key and re-encrypts the credentials sets with that key. The passphrase gives you access to the Master Key created by SharePoint Server that is used to encrypt the credential sets.
    
- You will need the passphrase that was recorded when the Secure Store Service was backed up to restore the Secure Store Service.
    
## Using Central Administration to restore the Secure Store Service in SharePoint Server
<a name="proc1"> </a>

Use the following procedure to restore the Secure Store Service by using Central Administration.
  
 **To restore the Secure Store Service by using Central Administration**
  
1. Verify that the user account performing this procedure is a member of the Farm Administrators group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
4. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the backup that you want, or a farm-level backup, from the list of backups, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.
    
    > [!NOTE]
    > If the correct backup job does not appear, in the **Backup Directory Location** text box, type the path of the correct backup folder, and then click **Refresh**. You cannot use a configuration-only backup to restore the Secure Store Service. 
  
5. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, expand **Shared Services Applications** and select the check box that is next to the Secure Store Service application backup group, and then click **Next**.
    
6. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\Shared Services\Shared Services Applications\\<Secure Store Service name\>** appears in the **Restore the following component** list. 
    
    In the **Restore Options** section, under **Type of restore**, select the **Same configuration** option. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
    Click **Start Restore**.
    
7. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take a several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the path that you specified in step 3. 
    
8. After the restore operation has successfully completed, you must refresh the passphrase.
    
9. In Central Administration, on the home page, in the **Application Management** section, click **Manage service applications**.
    
10. On the Service Applications page, click the Secure Store Service name. You might receive an error that says "Unable to obtain master key."
    
11. On the Secure Store Service page, on the ribbon, click **Refresh Key**.
    
12. In the **Refresh Key** dialog box, type the passphrase in the **Pass Phrase** box, and then click **OK**.
    
## Using PowerShell to restore the Secure Store Service in SharePoint Server
<a name="proc2"> </a>

You can use PowerShell to restore the Secure Store Service.
  
 **To restore the Secure Store Service by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```
   Restore-SPFarm -Directory <BackupFolder> -Item <SecureStoreServicename> -RecoveryMethod Overwrite [-BackupId <GUID>] [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path for the backup folder where the service application was backed up. 
    
   -  _\<SecureStoreServicename\>_ is the name of the Secure Store Service application. 
    
    If you have multiple backups use the  `BackupId` parameter to specify which backup to use. To view all of the backups for the farm, type the following command at the PowerShell command prompt: 
    
   ```
   Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup
   ```

    > [!NOTE]
    > If you do not specify a value for the  `BackupId` parameter, the most recent backup will be used. You cannot restore the Secure Store Service from a configuration-only backup. 
  
4. After the restore operation has successfully completed, you must refresh the passphrase. At the PowerShell command prompt, type the following command:
    
   ```
   Update-SPSecureStoreApplicationServerKey -Passphrase <Passphrase>
   ```

    Where  _\<Passphrase\>_, is the one that you currently use.
    
For more information, see [Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps) and [Update-SPSecureStoreApplicationServerKey](/powershell/module/sharepoint-server/Update-SPSecureStoreApplicationServerKey?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## See also
<a name="proc2"> </a>

#### Concepts

[Back up the Secure Store Service in SharePoint Server](back-up-the-secure-store-service.md)

