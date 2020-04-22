---
title: Migration API permission guidance
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Migration API permission guidance"
---
## Unique permission & role assignment limits

### Unique permissions: 
For SharePoint and OneDrive, the number of unique ACLs for items in a list or library is limited to 50,000. Calls will fail if you attempt to apply permission on a structure with more than 50,000 unique ACLs. 
While the supported limit is 50,000, the recommended general limit is 5,000. Making changes to more than 5,000 uniquely permissioned items at a time slows migration performance. 

### Role assignment
There is a role assignment limit of 5,000 per ACL that also needs to be monitored.
  
### Understanding security scope during migration

There are security and permission limits you need to be mindful of when migrating a source with a large hierarchy of files and folders or one that has too many unique 
permissions. 

Determine how many items are in your source or root folder, including lists or other object types.  


#### Permission inheritance
There is a 100,000 limit on the number of items that can be updated or removed as a part of creating a new SharePoint security scope. If you are migrating from a source with a structure that has more than 100,000 children (e.g. files, folders, lists or other object types), you need to structure the migration by importing security in multiple places to avoid exceeding the 100K limit. If the threshold is reached, any VROOM invite, REST share link, or any other permission modifying function call, will trigger HTTP 429 throttles. Permissions will not be updated. 

To learn more about the service limits in SharePoint for Microsoft 365, see SharePoint Limits.

If you have a folder with greater than 100K items, we recommend one of the following approaches.

#### Method 1:  Restructure the source layout
The first option is to restructure your source layout.

First, scan and determine which folder structure that has greater than 100K items. Remember to evaluate your folder size starting from the lowest level of the folder hierarchy. If you start at the top, VROOM API will always propagate ACLs and you could exceed the limit.

Then restructure the folder structure in the source. For example, divide a single folder of 500K into 5 folders at the root so each folder has less than 100K items.
Make sure that there are no more than 50K unique ACLs in the structure. 

*Example:*
At the source, break up the structure into 4 folders, A, B, C, and D, ensuring each contains less than 100,000 items. Then perform the migration. 

Remember there are other limits that must be considered. See SharePoint limits for details. 
 
#### Method 2
  
Create your destination layout to avoid exceeding limits.

The alternate option is to keep your source layout, applying unique ACLs at the key folder level of the destination.

*Example:*

Your source has over 100K. At your target location, create folders titled A, B, C, and D and apply the unique ACLs and scope ID. This will break the inheritance. Then proceed with your content migration. 

Optionally, if you want to prevent sharing until migration is completed, set the ACL to NULL.

After the incremental migration has completed, and only if you previously set the ACL to NULL, you can reapply the unique ACL for folders A, B, C, D separately.   When you re-apply the ACL, evaluate your folder size starting at the lowest level of hierarchy. See

![Parent root folder](media/parent-root-folder.png)</br></br>
