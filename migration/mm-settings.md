---
title: "Migration Manager settings"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
description: "A complete listing of the Migration Manager basic and advanced settings." 
---

# Migration Manager Settings



The following table details the settings available in the Migration Manager. Only your IT professional should manage the Advanced settings.

**General**
 
|**Setting**|**Description**|
|:-----|:-----|
|Only perform scanning|If you wish to scan the files as a pre-assessment to migration, this setting should be set to **On**.|
|Preserve file share permissions.|Preserve permissions on the files migrated.|


**Users**

|**Setting**|**Description**|
|:-----|:-----|
|Azure Active Directory lookup |By default, this setting is set to **On**. If no user mapping file is provided by the user, then Azure Active Directory is used as the default for user mapping.|
|User mapping file|By default,  *Azure AD lookup*  is used to map users when submitting migration jobs. If you wish to use your own mapping file, select the file to be used by clicking **Choose file**. </br> If you choose to use a custom user mapping file and want to preserve user permissions, turn off  *Azure Active Directory lookup*. By doing so, if a user isn't found in the mapping file, the tool won't look it up in Azure AD.</br> You can also leave **Azure Active Directory** setting on AND use a custom mapping file.  If domain users can't be found in the mapping file, the tool will auto-detect destination users and its source user’s SID.|


**Filters**

|**Setting**|**Description**|
|:-----|:-----|
|Migrate hidden files|If set to **Off**, hidden files will **not** be migrated.|
|Migrate files created after|Only migrate files created after the selected date. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.|
|Migrate files modified after|Only migrate files modified after the selected date. This setting can be used to limit the number of files migrated or to adhere to overall company governance policy regarding file retention. |
|Do not migrate files with these extensions|Enter a list of file extensions of file types you do not want to migrate. Separate each extension entered with a colon. Do not include the dot.  Example: TXT:EXE:JPEG: </br> **Note**: For files with multiple file extensions, for example.ext1.ext2, add only the last extension, ext2, to the exclusion list.|
|Migrate files and folders with invalid characters|By default, the setting is set to **On**. This is the recommended setting. The tool will attempt to move all files without filtering on characters. If any file can't be accepted, a failure message will be generated for that file.  <br/><br/>  If set to **Off**, the tool will skip any potential special characters. While this can improve performance when the source potentially contains a high number of files containing invalid characters, it also has drawbacks. To prevent malicious activities, source packages that generate more than 100 errors to the destination server will be blocked. As a result, all valid files in that package would also be blocked.  <br/> |
|Migrate OneNote folder as OneNote notebook <br/>|By default, this setting is **Off**. When set to **Off**, OneNote folders it will display as a regular folder in SharePoint.  If set to **On**, the migrated notebook folder will display as a OneNote link in SharePoint.<br/>|

**Advanced**

|**Setting**|**Description**|
|:-----|:-----|
|Migration auto rerun|Upon failure, retry task up to four times.|
|Migration Manager work folder|A temporary working folder is created named `%appdata%\Microsoft\SPMigration`. </br></br> Make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate.|
