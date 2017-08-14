---
title: Back up the Secure Store Service in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: d08d6d65-23c2-48cb-a871-1e021a382e5e
---


# Back up the Secure Store Service in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-26* **Summary:** Learn how to back up the Secure Store Service Application in SharePoint Server 2016 and SharePoint Server 2013.You can back up the Secure Store Service by using the SharePoint Central Administration website, or Microsoft PowerShell. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Use Windows PowerShell to back up the Secure Store Service in SharePoint](#proc1)
    
  
-  [Use Central Administration to back up the Secure Store Service in SharePoint](#proc2)
    
  

## Before you begin
<a name="begin"> </a>

The Secure Store Service provides the capability of securely storing credential sets and associating credentials to specific identities or a group of identities. Every time that you enter a new passphrase, Sharepoint_Server creates a new Master Key and re-encrypts the credentials sets with that key. The passphrase gives you access to the Master Key created by Sharepoint_Server that is used to encrypt the credential sets.You should back up the Secure Store Service and record the passphrase after the Secure Store Service is first configured and again every time that you make configuration changes to the Secure Store Service or re-encrypt the credential information.Before you begin this operation, review the following information:
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder.
    
  
- Record the passphrase. You will need the passphrase when you access the restored Secure Store Service.
    
  
- Ensure that you back up the Secure Store Service every time that you change or refresh the Master Key. When you change or refresh the Master key, the database is automatically re-encrypted with the new key. Backing up the Secure Store Service makes sure that the database and the Master key are synchronized.
    
  
- Keep the passphrase in a secure location.
    
  

## Use PowerShell to back up the Secure Store Service in SharePoint
<a name="proc1"> </a>

You can use PowerShell to back up the Secure Store Service manually or as part of a script that can be run at scheduled intervals. **To back up the Secure Store Service by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2016 Products cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Backup-SPFarm -Directory  <BackupFolder> -BackupMethod Full -Item <SecureStoreService > [-Verbose]
  ```


    
    
    Where:
    
  -  *<BackupFolder>*  is the path of a folder on the local computer or on the network in which you want to store the backups.
    
  
  -  *<SecureStoreService>*  is the name of the Secure Store Service application that you want to back up.
    
  

    > [!NOTE:]
      
For more information, see **Backup-SPFarm**.
> [!NOTE:]

  
    
    


## Use Central Administration to back up the Secure Store Service in SharePoint
<a name="proc2"> </a>

You can use Central Administration to back up the Secure Store Service. **To back up the Secure Store Service by using Central Administration**
1. Verify that the user account that performs this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
  
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
  
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, expand the **Shared Services Applications** node, select the Secure Store Service application from the list of components, and then click **Next**.
    
    > [!NOTE:]
      
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the ** Backup Type** section, select **Full**.
    
  
6. In the **Backup File Location** section, in the **Backup location box**, type the path of the backup folder, and then click **Start Backup**.
    
  
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 5.
    
  

# See also

#### 

 [Restore Secure Store Service applications in SharePoint Server](html/restore-secure-store-service-applications-in-sharepoint-server.md)
  
    
    

  
    
    

