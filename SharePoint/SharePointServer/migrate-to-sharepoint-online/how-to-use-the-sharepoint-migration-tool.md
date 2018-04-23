---
title: "How to use the SharePoint Migration Tool"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 4/10/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.custom: Strat_SP_gtc
ms.assetid: 65462df1-42fe-40cf-88f7-e39f82f5130f

description: "The SharePoint Migration Tool is a tool that migrates your files from SharePoint on-premises document libraries or regular file shares and easily moves them to your SharePoint Online tenant. It is available to all Office 365 users."
---

# How to use the SharePoint Migration Tool

The SharePoint Migration Tool (SPMT) is a tool that migrates your files from SharePoint on-premises document libraries or regular file shares and easily moves them to your SharePoint Online tenant. It is available to all Office 365 users.
  
> [!Note]
> A portion of this article discusses features currently in beta release of the Microsoft product, SharePoint Migration Tool. Beta features are noted in the context of the text. The information in this article is provided as-is and is subject to change without notice. 

>[!NOTE]
> The new V2 beta release is now available for download. 
>To install the new V2 beta release, download it here: [SharePoint Migration Tool V2 Beta release](http://spmtreleasescus.blob.core.windows.net/betainstall/default.htm). 


>[!NOTE]
>To install the current release download here: [SharePoint Migration Tool Version 1](http://spmtreleasescus.blob.core.windows.net/install/default.htm).

> [!NOTE]
> Currently the **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. 
  
## Before you begin

When you first launch the SharePoint Migration Tool (SPMT), you will be prompted for your Office 365 username and password. The Office 365 credentials you provide will be where the files will be migrated.
  
### Recommended requirements for best performance

|**Recommendation**||
|:-----|:-----|
|CPU  <br/> |64-bit Quad core processor or better  <br/> |
|RAM  <br/> |16 GB  <br/> |
|Local Storage  <br/> |Solid state disk: 150 GB free space  <br/> |
|Network card  <br/> |1 Gbps  <br/> |
|Operating system  <br/> |Windows Server 2012 R2 or Windows 10 client  <br/> .NET Framework 4.6.2  <br/> |
|Microsoft Visual C++ 2015 Redistributable  <br/> |Required for OneNote migration.  <br/> |
   
### Minimum requirements (expect slow performance)

|**Minimum requirement**||
|:-----|:-----|
|CPU  <br/> |64-bit 1.4 GHz 2-core processor or better  <br/> |
|RAM  <br/> |8 GB  <br/> |
|Local Storage  <br/> |Hard disk: 150 GB free space  <br/> |
|Network card  <br/> |High-speed Internet connection  <br/> |
|Operating system  <br/> |Windows Server 2008 R2, Windows 7 updated or better  <br/> .NET Framework 4.6.2  <br/> |
|Microsoft Visual C++ 2015 Redistributable  <br/> |Required for OneNote migration.  <br/> |
   
## What happens to the permissions on a file when it is migrated?

The location of your on-premises data, and whether you have synchronized your Active Directory accounts to Azure Active Directory (AAD), can affect the permission settings on your files after they have been migrated to SharePoint Online.

See [Understanding Permissions and the SharePoint Migration Tool](..//migrate-to-sharepoint-online/understanding-permissions-when-migrating.md) for a complete explanation of permission settings.
  
> [!NOTE]
> Certain settings can affect how permissions on your files will be handled. See the [Advanced Settings](how-to-use-the-sharepoint-migration-tool.md#BKMK_Settings_1_1) section below, specifically the  *Azure Active Directory lookup*  ,  *Preserve permissions*  , and  *User Mapping file*  settings. 
  
 **Syncing your environment:** In order to maintain existing on-premises file permissions, there must be a corresponding user in SPO. The easiest way to accomplish this is to synchronize your Active Directory accounts to Azure Active Directory (AAD). 
  
> [!NOTE]
> You can upload a custom user mapping file to the SharePoint Migration Tool. 
  
||**File share**|**SharePoint on-prem files**|
|:-----|:-----|:-----|
|User mapped between on-premises and SPO (either Dirsync has been run or a user mapping file provided)  <br/> |There are only two types of permissions that will be migrated: **Read** and **Write**.  <br/> If a file has **Write** permission for user1, then the file will be set to **Contribute** for user1 in SPO. If a file has **Read** permission for user1, then the file will be set to **Read** for user1 in SPO.           Note: At this time, the special permissions, such as **Deny**, will not be saved.  <br/> |All the unique permissions on a file will be migrated to SPO. Inherited permissions will not be migrated.  <br/> |
|No user mapping (not synced, no user mapping file)  <br/> |Files will be assigned the default permission of the location to which it has been migrated in SPO.  <br/> |Files will be assigned the default permission of the location to which it has been migrated in SPO.  <br/> |
   
## Where is your data currently located?

Before you start using the SharePoint Migration Tool (SPMT), note where your data is located and where you want those files. You will be prompted for the current location of your data files and the location of the SharePoint Online site collection where you want them moved. The SharePoint Migration Tool lets you select from two sources from which to migrate your data: from an on-premises SharePoint Server 2013 site or from a local file share or network path.
  
- **SharePoint on-premises:** If you select the SharePoint on-premises option, you will be asked to enter the name of the SharePoint Server site where your files are located and prompted for your credentials for that site. You will indicate what document library you wish to migrate. 
    
    > [!NOTE]
    > The SharePoint Migration Tool supports SharePoint Server 2013. 
  
- **File share:** If you select the file share option, you will be asked to enter the location of the file share, the URL of the SharePoint Online site, and the document library where they will be moved. 
    
## Using the SharePoint Migration tool

If you don't have it yet, you have two options:  To install the current release download here: [SharePoint Migration Tool Version 1.1.90.1](http://spmtreleasescus.blob.core.windows.net/install/default.htm)

If you wish to install the new V2 beta release, download it here:  [SharePoint Migration Tool V2 Beta release](http://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)
  
 **Migrating data files from SharePoint Server document libraries**
  
1. Start the SharePoint Migration Tool, and then click **Next**.
    
2. Enter your Office 365 username and password, and then click **Sign in.**
    
3. Select **Choose a source and destination**.
    
4. Select **SharePoint Server (on-premises).**
    
5. Enter the SharePoint Server 2013 site URL where your data is currently located. Click **Next**.
    
    > [!IMPORTANT]
    > Proxy connections are not supported. Using Proxy connections will yield errors such as "SharePoint login fail" or "cannot load document library". 
  
6. Enter your username and password to the SharePoint Server site; username must use the format of someone@example.com. Click **Sign in**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 

    **Note:**  SPMT Version 2, currently in beta, supports the following authentication methods:

    - NTLM
    - Kerberos
    - Forms
    - ADFS
    - Multi-factor authentication
    - SAML based claims
    - Client certificate authentication

        **Important Note:**  If the on-perm server is configured to support multiple authentication methods including the Windows authentication, then Windows authentication will not be supported. If this describes your environment, use other authentication methods instead of Windows authentication. 
  
7. Choose the document library where your files are located. The drop-down list will contain all your possible choices.
    
8. Enter the URL of the SharePoint Online site where you want your files migrated.
    
9. Select the document library to where your files will be moved.
    
10. Click **Add**. This task will be added to the list. If you want to select another set of data files to migrate, click **Choose a source and destination**.
    
 **Migrating data files from a local file share**
  
1. Start the SharePoint Migration Tool, and then click **Next**.
    
2. Enter your Office 365 username and password, and then click **Sign in.**
    
3. Select **Choose a source and destination**.
    
4. Select **File share**.
    
5. Enter the path of the file share where your data is located. Click **Next**.
    
6. Enter the URL of the SharePoint Online site where you want your files migrated, and then enter your username and password to the SharePoint Server site. Click **Sign in**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 
  
7. Choose the document library to where your files will be moved.
    
8. Click **Add**. This task will be added to the list. If you want to select another set of data files to migrate, click **Choose a source and destination**.
    
9. When you have finished selecting your sources, click **Migrate**.
    
## Bulk migration using a JSON or CSV file

If you have many sources to migrate, you can use either a JSON or CSV file to do a bulk migration.

>[!Note]
>The use of JSON files for bulk import are only supported in the V2 Beta release.
  
For more information on how to create a JSON or CSV file for data content migration, see [How to format your JSON or CSV file for data content migration](how-to-format-your-csv-file-for-data-content-migration.md).
  
 **To use a JSON or CSV file for bulk migration**
  
1. Open the SharePoint Migration Tool, and then click **Next**.
    
2. Enter your Office 365 username and password, and then click **Sign in**.
    
3. Select **JSON or CSV file for bulk migration**. Enter the location of your file, or click **Choose File** to locate it. Click **Add**.
    
    > [!NOTE]
    > If you are migrating files from an on-premises SharePoint Server, you will be prompted for your username and password for that site unless you provided those credentials in previous steps. 
  
    > [!NOTE]
    > Any errors in your file it will be detected on a line-by-line basis. The error will indicate which line or lines contains the errors. You will not be able to proceed until you correct the errors in your file. 
  
    > [!IMPORTANT]
    > Proxy connections are not supported. Using Proxy connections will yield errors such as "SharePoint login fail" or "cannot load document library". 
  
5. If your JSON or CSV file is successfully added without errors, the job will be added to your list of sources and destinations.
    
6. If you want to select another set of data files to migrate, click **Choose a source and destination**.
    
7. When you have finished selecting your sources, click **Migrate**.
    
## Monitoring and reporting status of migration jobs

After you click **Migrate**, the progress of your migration jobs will be displayed. As they complete, you can view either detailed or summary reports of an individual job or a single summary report that includes all migration jobs submitted during this session.
  
 **To view detailed reports**
  
1. Click the down arrow directly below the migration job.
    
2. Click **View Task Report**. A folder opens containing three different reports:
    
  - FilesReport.csv
    
  - FilesSummary.csv
    
  - ScanSummary.csv
    
 **To view a summary report all submitted jobs**
  
- Click **Open Report**.
    
    A report folder opens containing the summary report.
    
## Resuming migration jobs

If you need to close the migration tool before a submitted job has completed, you can restart the tool from any computer.
  
> [!NOTE]
> To resume a submitted migration job, it has to have been running  *at least* **5 minutes**. It will be paused at the point you closed the SharePoint Online Migration Tool. If your submitted job was running less than 5 minutes before the tool closed, you must resubmit the job.   
 **To resume migration jobs**
  
1. Launch the SharePoint Migration Tool. Click **Sign In** using the same Office 365 username and password you used when you originally submitted the job. 
    
2. After you sign in, a screen displays any paused migrations, providing details about what has been completed and what remains.
    
3. If you want to add additional migration tasks, click **Select new sources and destinations**. Otherwise, click **Next**. Your migration jobs will be resumed. If you are migrating files from an on-premises SharePoint Server, you will be prompted for your username and password for that site.
    
## Incremental migration

After a migration task has completed, it can also be saved to be rerun at a later date, allowing you to move only those new or updated files in the source location. 
  
By default, the setting for Incremental migration is **on**. To change this, go to **Settings**,  *Enable incremental migration*  . 
  
> [!NOTE]
> If you wish to make changes to this setting, do so before your initial migration job is submitted. This setting is global; it will apply to all subsequent tasks you submit. 
  
When this setting is on, an incremental check of the SharePoint Online target environment will be performed. Files will be evaluated as follows:
  
|**Status**|**Result**|
|:-----|:-----|
|Modified time of the source file is earlier than the modified time of the target file.  <br/> |File will not be migrated.  <br/> |
|Files or lists exist in the SPO target location.  <br/> |Migration will skip those existing objects during scan.  <br/> |
|Time stamp on files or object in the source location changes during migration  <br/> |Only the changed file will be migrated.  <br/> |
|Source is a file share.  <br/> |Validation for migration will be based on the file/folder path.  <br/> |
|Source is an on-premises SharePoint Server/  <br/> |Validation for migration will be based on list item GUID. Use the folder path as a fallback.  <br/> |
   
> [!NOTE]
> Excluding the first initial round, if there are newly updated source files or failed migration files, an SPMT run will be triggered up to 5 additional rounds. 
  
1. Start the SharePoint Migration Tool, and then click **Next**.
    
2. Enter your Office 365 username and password, and then click **Sign in.**
    
3. The screen titled "Where's your data" displays. Click **Cancel**.
    
4. Enter your tasks as usual, and then migrate.
    
5. After a task completes, click **Yes** when you see the following prompt: 
    
    ![Incremental migration save prompt](../media/b365559d-fb07-467f-b59d-a0fd9ef360ed.png)
  
## Advanced Settings
<a name="BKMK_Settings"> </a>

Advanced settings should only be changed or managed by your IT professional. The advanced settings are in the following categories:
  
|**Setting**|**Description**|
|:-----|:-----|
|Only perform scanning  <br/> |If you wish to scan the files as a pre-assessment to migration, turn **Only perform scanning** on.  <br/> |
|Enable incremental migration  <br/> |The default setting is set to **On**. This lets you rerun the migration jobs at a later date, migrating only the changes or additions since the previous run.  <br/> Important: If you wish to be able to submit the same job again for incremental migration, this setting must be set to **On** * before *  the initial migration job is submitted.  <br/> |
|Migrate file version history  <br/> |If set to **No**, only the most recent version of the file will be migrated. If set to **Yes**, you can choose whether to keep all versions, or limit it to a specific number.  <br/> |
|Do not migrate hidden files  <br/> |If set to **On**, hidden system files will **not** be migrated.  <br/> |
|Do not migrate files created before  <br/> |If you choose to limit which files are migration based on  *creation date*  , set your values in this section. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.  <br/> |
|Do not migrate files modified before  <br/> |If you choose to limit what files are migration based on  *modified date,*  set your values in this section. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.  <br/> |
|Do not migrate files with these extensions  <br/> |To prevent certain file types from migrating, list each extension, separating it with a vertical bar. For example, mp4|avi|mkv. Do not include the leading **"."** before the extension name.  <br/> |
|Do not migrate files and folders with invalid characters  <br/> |By default, the setting is set to **Off**. This is the recommended setting. The tool will attempt to move all the files without filtering on characters. If any file can't be accepted into SPO, a failure message will be generated for that file.  <br/> If set to **On**, the tool will skip any potential special characters. While this can improve performance when the source potentially contains a high number of files containing invalid characters, it also has drawbacks. To prevent malicious activities, source packages that generate more than 100 errors to the destination server will be blocked. As a result, all valid files in that package would also be blocked.  <br/> |
|Migrate OneNote folder as OneNote notebook <br/>|By default, this is set to **Off**. When set to **Off**, OneNote folders will not  migrate over as a notebook.<br/>|
|Azure Active Directory lookup  <br/> |By default, this is set to **On**. If no User mapping file is provided by the user, then Azure Active Directory is used as the default for user mapping.  <br/> |
|Preserve user permissions  <br/> |By default, this is set to **On**. If set to **Off**, no permissions will be preserved.  <br/> |
|Skip list with audience targeting enabled <br/>|By default, this is set to **On**.  When set to **On**, SharePoint on-premises lists with audience targeting enabled will be skipped and not migrated.<br/>|
|User mapping file  <br/> |By default,  *Azure AD lookup*  is used to map users when submitting migration jobs. If you wish to use your own mapping file, select the file to be used by clicking **Choose file**. If you choose to use a custom user mapping file and you want to preserve user permissions, turn off  *Azure Active Directory lookup*  . By doing so, if a user isn't found in the mapping file, the tool won't look it up in AAD.  <br/> |
|SharePoint Migration Tool work folder  <br/> |By default, a temp folder will be created. If you wish to specify a specific working folder, enter the name here.   <br/> **Note:** By default, the working folder is *%appdata%\Microsoft\MigrationTool* . Please make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate. <br/> |
|Use custom Azure storage  <br/> |If you wish to use your own Azure storage, set this value to **On**.  <br/> If you choose to turn on, additional fields will display to enter your account and key, and settings to select if you want to enable or disable encryption, and whether temporary files are deleted when migration is complete.  <br/> **Note: ** This feature is supported only for  *General Purpose storage accounts*  as General Purpose accounts support Azure blobs and queues. This feature is not available for Blob Storage accounts.  <br/> |
   
## Related Topics
<a name="BKMK_Settings"> </a>

[Introducing the SharePoint Migration Tool](introducing-the-sharepoint-migration-tool.md)
  
[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to format your JSON or CSV file for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint Online and OneDrive Migration Speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint Migration Tool Feedback and Support Forum](https://social.technet.microsoft.com/Forums/en-US/home?forum=SharePointMigrationTool)
  

