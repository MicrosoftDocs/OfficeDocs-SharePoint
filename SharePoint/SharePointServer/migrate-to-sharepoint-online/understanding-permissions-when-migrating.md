---
title: "Understanding permissions when migrating"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 4/6/2018
ms.audience: ITPro
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 
description: "Understanding how permissions work when migrating data from on-premises to SPO using the SharePoint Migration Tool"
---

# Understanding Permissions and the SharePoint Migration Tool

The SharePoint Migration Tool permission control is effected by various conditions.  The following table lists all the conditions and the corresponding results.

|**Source**|***Preserve user permissions* set to ON**|**Migrating to Target library root folder or sub folder?**|**Target library permission before migration**|**Target library permission after migration**|**Note**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|File share|No|Root folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed| migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Root folder|Unique|Unique|Role assignments of the target library and existing files won't be changed| migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Sub folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed| migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|No|Sub folder|Unique|Unique|Role assignments of the target library and existing files won't be changed| migrated files have Inherited permission (Inherited role assignments from target library)|
|File share|Yes|Root folder|Inherited|Unique|Role assignments of the target library will be replaced by that in source root folder| existing files with Inherited permission will still be Inherited permission but with new role assignment from target library| existing files with Unique permission won't be changed; migrated files without any permission in the source will have Inherited permission and Inherited role assignment from target library| migrated files with any permission in the source will carry over these permission as Unique permission.|
|File share|Yes|Root folder|Unique|Unique|Permission from the source folder will be added as new role assignments to the target library| existing files with Inherited permission will still be Inherited permission but with new role assignment from target library| existing files with Unique permission won't be changed; migrated files without any permission in the source will have Inherited permission and Inherited role assignment from target library| migrated files with any permission in the source will carry over these permission as Unique permission.|
|File share|Yes|Sub folder|Inherited|Inherited|Role assignments of the target library and existing files won't be changed| permission from source folder and files will be carried over to the target subfolder and corresponding files| which will have Unique permission| as new role assignments|
|File share|Yes|Sub folder|Unique|Unique|Role assignments of the target library and existing files won't be changed| permission from source folder and files will be carried over to the target subfolder and corresponding files| which will have Unique permission| as new role assignments|
|List/Document library |No|Root folder|Inherited|Inherited|Same as File share migration with same condition|
|List/Document library |No|Root folder|Unique|Unique|Same as File share migration with same condition|
|Document library |No|Sub folder|Inherited|Inherited|Same as File share migration with same condition|
|Document library |No|Sub folder|Unique|Unique|Same as File share migration with same condition|
|List/Document library |Yes|Root folder|Inherited|Unique|Same as File share migration with same condition|
|list/Document library |Yes|Root folder|Unique|Unique|Same as File share migration with same condition|
|Document library |Yes|Sub folder|Inherited|Inherited|Same as File share migration with same condition|
|Document library |Yes|Sub folder|Unique|Unique|Same as File share migration with same condition|
|Site/web|No|NA|Inherited|Inherited|Role assignment of target site/web will be unchanged|
|Site/web|No|NA|Unique|Unique|Role assignment of target site/web will be unchanged|
|Site/web|Yes|NA|Inherited |Unique|Role assignment of target site/web **will be replaced** by those in the source site/web|
|Site/web(A) with subsite B  (both migrated with SPMT)|Yes|NA|Subsite B or sub web Inherited from main site A|Subsite(B/web inherited from the new SPO main site A”|Site A is migrated as described for normal site migration|
|Site/web|Yes|NA|Unique|Unique|Role assignment of source site/web will be added as new role assignments to the target site/web|


