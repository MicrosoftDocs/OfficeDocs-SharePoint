---
title: "File and folder permissions when using the SharePoint Migration Tool"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
mscollection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.assetid: 
description: "File and folder permissions when using the SharePoint Migration Tool (SPMT)."
---

# File and folder permissions when using the SharePoint Migration Tool


## What happens to the permissions on a file when it is migrated?

The location of your on-premises data, and whether you have synchronized your Active Directory accounts to Azure Active Directory (AAD), can affect the permission settings on your files after they have been migrated to SharePoint Online.

 **Syncing your environment:** In order to maintain existing on-premises file permissions, there must be a corresponding user in SPO. The easiest way to accomplish this is to synchronize your Active Directory accounts to Azure Active Directory (AAD). 
  
  
|How |**File share**|**SharePoint on-prem files**|
|:-----|:-----|:-----|
|User mapped between on-premises and SPO (either Dirsync has been run or a user mapping file provided)  <br/> |There are only two types of permissions that will be migrated: **Read** and **Write**.  <br/> If a file has **Write** permission for user1, then the file will be set to **Contribute** for user1 in SPO. If a file has **Read** permission for user1, then the file will be set to **Read** for user1 in SPO.           Note: At this time, the special permissions, such as **Deny**, will not be saved.  <br/> |All the unique permissions on a file will be migrated to SPO. Inherited permissions will not be migrated.  <br/> |
|No user mapping (not synced, no user mapping file)  <br/> |Files will be assigned the default permission of the location to which it has been migrated in SPO.  <br/> |Files will be assigned the default permission of the location to which it has been migrated in SPO.  <br/> |
   
### Permissions conditions and results

The SharePoint Migration Tool permission control is effected by various conditions.  The following table lists all the conditions and the corresponding results.

|**Source**|**Preserve user permissions setting set to On**|**Migrating to**|**Target library permission before migration**|**Target library permission after migration**|**Note**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|File share|No|Root folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed; migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Root folder|Unique|Unique|Role assignments of the target library and existing files won't be changed; migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Sub folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed; migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Sub folder|Unique|Unique|Role assignments of the target library and existing files won't be changed; migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|Yes|Root folder|Inherited|Unique|Role assignments of the target library will be replaced by that in source root folder. Existing files with inherited permissions will still be inherited permission but with a new role assignment from target library. Existing files with Unique permissions won't be changed. Migrated files without any permission in the source will have inherited permissions and inherited role assignments from the target library. Migrated files with any permissions in the source will carry over these permissions as unique.|
|File share|Yes|Root folder|Unique|Unique|Permissions from the source folder will be added as new role assignments to the target library. Existing files with inherited permissions will still be inherited permissions but with a new role assignment from the target library. Existing files with unique permissions won't be changed. Migrated files without any permissions in the source will have inherited permissions and inherited role assignments from the target library. Migrated files with any permissions in the source will carry over these permissions as Unique.|
|File share|Yes|Sub folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed. Permissions from source folder and files will be carried over to the target subfolder and corresponding files, which will have Unique permissions as new role assignments.|
|File share|Yes|Sub folder|Unique|Unique|Role assignments of the target library and existing files won't be changed. Permissions from source folder and files will be carried over to the target subfolder and corresponding files which will have Unique permission as new role assignments.|
|List/Document library |No|Root folder|Inherited|Inherited|Same as File share migration with same condition|
|List/Document library |No|Root folder|Unique|Unique|Same as File share migration with same condition|
|Document library |No|Sub folder|Inherited|Inherited|Same as File share migration with same condition|
|Document library |No|Sub folder|Unique|Unique|Same as File share migration with same condition|
|List/Document library |Yes|Root folder|Inherited|Unique|Same as File share migration with same condition|
|list/Document library |Yes|Root folder|Unique|Unique|Same as File share migration with same condition|
|Document library |Yes|Sub folder|Inherited|Inherited|Same as File share migration with same condition|
|Document library |Yes|Sub folder|Unique|Unique|Same as File share migration with same condition|
|Site/Web|No|NA|Inherited|Inherited|Role assignment of target site/web will be unchanged|
|Site/Web|No|NA|Unique|Unique|Role assignment of target site/web will be unchanged|
|Site/Web|Yes|NA|Inherited |Unique|Role assignment of target site/web **will be replaced** by those in the source site/web|
|Site/Web(A) with Subsite B  (both migrated with SPMT)|Yes|NA|||Subsite B or sub web inherited from main Site A Subsite B/web unique from the new SPO main site A Site A is migrated as described for normal site migration.  Subsite B becomes unique and role assignment **will be replaced** by those in the source Subsite B|
|Site/Web|Yes|NA|Unique|Unique|Role assignment of source site/web will be added as new role assignments to the target site/web|


