---
title: "SharePoint Migration Tool Settings"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration


description: "A complete listing of the SharePoint Migration basic and advanced settings." 
---

# SharePoint Migration Tool Settings

The following table details the settings available in SPMT.  Advanced settings should only be changed or managed by your IT professional. 

> [!Note] 
> Some Settings that are available only in the SPMT V3 Initial Release are indicated below. 
 



  
|**Setting**|**Description**|
|:-----|:-----|
|Only perform scanning  <br/> |If you wish to scan the files as a pre-assessment to migration, turn **Only perform scanning** on.  <br/> |
|Enable incremental migration  <br/> |The default setting is set to **On**. This lets you rerun the migration jobs at a later date, migrating only the changes or additions since the previous run.  <br/> Important: If you wish to be able to submit the same job again for incremental migration, this setting must be set to **On** * before *  the initial migration job is submitted.  <br/> |
|Migrate file version history  <br/> |If set to **Off**, only the most recent version of the file will be migrated. If set to **On**, you can choose whether to keep all versions, or limit it to a specific number.  <br/> |
|Migrate hidden files  <br/> |If set to **Off**, hidden system files will **not** be migrated.  <br/> |
|Migrate files created before  <br/> |If you choose to limit which files are migration based on  *creation date*  , set your values in this section. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.  <br/> |
Migrate files modified before  <br/> |If you choose to limit what files are migration based on  *modified date,*  set your values in this section. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.  <br/> |
|Do not migrate files with these extensions. <br/> |To prevent certain file types from migrating, list each extension, separating it with a vertical bar. <br/> |
|Migrate files and folders with invalid characters  <br/> |By default, the setting is set to **Off**. This is the recommended setting. The tool will attempt to move all the files without filtering on characters. If any file can't be accepted into SPO, a failure message will be generated for that file.  <br/> If set to **On**, the tool will skip any potential special characters. While this can improve performance when the source potentially contains a high number of files containing invalid characters, it also has drawbacks. To prevent malicious activities, source packages that generate more than 100 errors to the destination server will be blocked. As a result, all valid files in that package would also be blocked.  <br/> |
|Migrate OneNote folder as OneNote notebook <br/>|By default, this is set to **Off**. When set to **Off**, OneNote folders will not migrate over as a notebook.  At this time the ability to migrate notebooks on SharePoint on-premises is disabled.<br/>|
|Azure Active Directory lookup  <br/> |By default, this is set to **On**. If no User mapping file is provided by the user, then Azure Active Directory is used as the default for user mapping.  <br/> |
|Preserve user permissions  <br/> |By default, this is set to **On**. If set to **Off**, no permissions will be preserved.  <br/> |
|Skip list with audience targeting enabled <br/>|By default, this is set to **On**.  When set to **On**, SharePoint on-premises lists with audience targeting enabled will be paused and the user will be prompted for confirmation before continuing.<br/>|
|User mapping file  <br/> |By default,  *Azure AD lookup*  is used to map users when submitting migration jobs. If you wish to use your own mapping file, select the file to be used by clicking **Choose file**. If you choose to use a custom user mapping file and you want to preserve user permissions, turn off  *Azure Active Directory lookup*. By doing so, if a user isn't found in the mapping file, the tool won't look it up in AAD.  <br/> |
|SharePoint Migration Tool work folder  <br/> |By default, a temp folder will be created. If you wish to specify a specific working folder, enter the name here.   <br/> **Note:** By default, the working folder is *%appdata%\Microsoft\MigrationTool* . Please make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate. <br/> |
|Use custom Azure storage  <br/> |If you wish to use your own Azure storage, set this value to **On**.  <br/> If you choose to turn on, additional fields will display to enter your account and key, and settings to select if you want to enable or disable encryption, and whether temporary files are deleted when migration is complete.  <br/> **Note: ** This feature is supported only for  *General Purpose storage accounts*  as General Purpose accounts support Azure blobs and queues. This feature is not available for Blob Storage accounts.  <br/> |
   
## Related Topics
<a name="BKMK_Settings"> </a>
  
[SharePoint Migration Tool Feedback and Support Forum](https://social.technet.microsoft.com/Forums/en-US/home?forum=SharePointMigrationTool)
  

