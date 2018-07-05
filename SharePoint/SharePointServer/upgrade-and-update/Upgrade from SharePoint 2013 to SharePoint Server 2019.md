---
title: "Upgrade from SharePoint Server 2013 to SharePoint Server 2019"
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d47575fa-bb85-4017-8db7-5e25f98ba171
description: "Summary: "Upgrade from SharePoint Server 2013 to SharePoint Server 2019."
---

# High level overview to upgrade from SharePoint 2013 to SharePoint Server 2019

 **Summary:** Learn the overview steps required to upgrade SharePoint Server 2013 environment to SharePoint Server 2019. 
  

## Overview
<a name="Overview"> </a>

The upgrade scenario has not changed in SharePoint Server 2019. There is no direct upgrade path from 2013 to 2019. To upgrade to SharePoint Server 2019, you must upgrade SharePoint 2013 to SharePoint Server 2016, and then upgrade to SharePoint Server 2019.  Your databases must be at a SharePoint Server 2016 RTM version or higher when you upgrade to SharePoint Server 2019. Any database with a lower version will be locked and upgrade will not start. 

For a visual look of the high-level steps, refer to <Download Center to vsd and pdf>

[!NOTE]
The steps for creating and restoring service applications only applies to these six: 

•	Secure Store service application<br/> 
•	Business Data Connectivity service application<br/> 
•	Managed Metadata service application<br/> 
•	PerformancePoint Services service application<br/> 
•	User Profile service application<br/>
•	Search service application

For the specific, end to end steps to upgrade SharePoint 2013 to SharePoint Server 2016, see [Upgrade to SharePoint Server 2016](https://docs.microsoft.com/en-us/SharePoint/upgrade-and-update/upgrade-to-sharepoint-server-2016)

## Steps to Upgrade

### 2013

In SharePoint 2013, if you have any web applications that are in windows authentication mode, you should convert them to claims authentication. Claims authentication is the default mode in SharePoint Server 2016 and SharePoint Server 2019.

Next, upgrade all the site collections from 14 mode to 15 mode by using the [Upgrade-SPSite](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/upgrade-spsite?view=sharepoint-ps) cmdlet.  Any database with a 14 version will be locked and prevented from upgrading to SharePoint Server 2016.  After the site collections have been upgraded, create a backup of all content and service application databases from your old farm (for example, SQLOLD1).  Restore these databases to a new farm’s SQL Server in SharePoint Server 2016 (for example, SQLNEW1).

### 2016

In SharePoint Server 2016, build a new farm that includes service applications. When the service applications are created use the existing database names that reside on SQLNEW1.  After the new farm is created, create a new web application with a temporary database.  Install any full trust solutions, administrator approved InfoPath forms, etc.  Dismount the temporary content database from the web application.

[!NOTE]
You may need to delete the temporary content database from the SQL Server.

Start the upgrade process to SharePoint Server 2016 by running the [Mount-SPContentDatabase](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps) cmdlet on the restored content databases from SQLNEW1.  After the upgrade process is complete, perform any individual configuration changes that are not part of the service application and content databases, such as incoming/outgoing email settings, etc.

### 2019

The steps to upgrade from SharePoint Server 2016 to SharePoint Server 2019 are the same as going from SharePoint 2013 to SharePoint Server 2016 except for converting web applications to claims authentication and upgrading database modes to level 15. These are not required.

Create a backup of all content and service application databases from your old farm (for example, SQL2016OLD1).  Restore these databases to a new farm’s SQL Server in SharePoint Server 2019 (for example, SQL2019NEW1).

In SharePoint Server 2019, build a new farm that includes service applications. When the service applications are created use the existing database names that reside on SQL2019NEW1.  After the new farm is created, create a new web application with a temporary database.  Install any full trust solutions, administrator approved InfoPath forms, etc.  Dismount the temporary content database from the web application.

[!NOTE]
You may need to delete the temporary content database from the SQL Server.

Start the upgrade process to SharePoint Server 2016 by running the [Mount-SPContentDatabase](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps) cmdlet on the restored content databases from SQLNEW1.  After the upgrade process is complete, perform any individual configuration changes that are not part of the service application and content databases, such as incoming/outgoing email settings, etc.

## See Also

[Overview of the upgrade process to SharePoint Server 2019](overview-of-the-upgrade-process-2019.md)