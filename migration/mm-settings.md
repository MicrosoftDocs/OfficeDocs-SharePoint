---
title: "Migration Manager settings"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
description: "A complete listing of the Migration Manager basic and advanced settings." 
---

# Migration Manager Settings

>[!Note]
>Features noted in this topic are part of a preview release. The content and the functionality are subject to change and are not subject to the standard SLAs for support.


The following table details the settings available in the Migration Manager. Advanced settings should only be changed or managed by your IT professional. 

**General**
 
|**Setting**|**Description**|
|:-----|:-----|
|Only perform scanning|If you wish to scan the files as a pre-assessment to migration, turn **Only perform scanning** on.|
|Preserve file share permissions.|Preserve permissions on the files migrated.|


**Users**

|**Setting**|**Description**|
|:-----|:-----|
|Azure Active Directory lookup |By default, this is set to **On**. If no user mapping file is provided by the user, then Azure Active Directory is used as the default for user mapping.|
|User mapping file|By default,  *Azure AD lookup*  is used to map users when submitting migration jobs. If you wish to use your own mapping file, select the file to be used by clicking **Choose file**. If you choose to use a custom user mapping file and want to preserve user permissions, turn off  *Azure Active Directory lookup*. By doing so, if a user isn't found in the mapping file, the tool won't look it up in AAD.|


**Filters**

|**Setting**|**Description**|
|:-----|:-----|
|Migrate hidden files|If set to **Off**, hidden files will **not** be migrated.|
|Migrate files created after|Only migrate files created after the selected date. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention.|
|Migrate files modified after|Only migrate files modified after the selected date. This may be to limit the number of files migrated or to adhere to overall company governance policy regarding file retention. |
|Do not migrate files with these extensions|Enter a list of file extensions of file types you do not want to migrate. Separate each extension entered with a colon. Do not include the dot.  Example: TXT:EXE:JPEP: </br> **Note** For files with multiple file extensions, eg. .ext1.ext2, add only the last extension, ext2, to the exclusion list.|
|Migrate files and folders with invalid characters|By default, the setting is set to **On**. This is the recommended setting. The tool will attempt to move all the files without filtering on characters. If any file can't be accepted into SPO, a failure message will be generated for that file.  <br/><br/>  If set to **Off**, the tool will skip any potential special characters. While this can improve performance when the source potentially contains a high number of files containing invalid characters, it also has drawbacks. To prevent malicious activities, source packages that generate more than 100 errors to the destination server will be blocked. As a result, all valid files in that package would also be blocked.  <br/> |
|Migrate OneNote folder as OneNote notebook <br/>|By default, this is set to **Off**. When set to **Off**, OneNote folders it will display as a regular folder in SharePoint.  If set to **On** the migrated notebook folder will display as a OneNote link in SharePoint.<br/>|


**Advanced**

|**Setting**|**Description**|
|:-----|:-----|
|Migration auto re-run|Upon failure, re-try task up to 4 times.|
|Migration Manager work folder|By default, the working folder is `%appdata%\Microsoft\SPMigration`. Please make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate.|