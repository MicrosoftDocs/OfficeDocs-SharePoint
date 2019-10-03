---
title: "Migration Assessment Scan Long OneDrive URLs"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/13/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: a2828065-b060-4784-9a7d-4c214b4054b1
description: "Learn how to fix issues with long OneDrive URLs during migration."
---

# Migration Assessment Scan: Long OneDrive URLs

Learn how to fix issues with long OneDrive URLs during migration.
  
## Overview

When you're moving a OneDrive site from your source to the target environment, the OneDrive URL will change formats. On the source platform the OneDrive sites are in the format of https://onedrive.contoso.com/personal/domain_user. On the target platform, the Domain_User portion of the URL will change to use the UPN for the user. This will look similar to https://onedrive.contoso.com/personal/user_contoso_com.
  
 **Example:**
  
If you used this file:
  
> https://OneDrive.contoto.com/personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx
    
The directory name of the file would be:
  
- Personal/contoso_bobsmith/Documents/Folder1/Folder2
    
> [!NOTE]
> There is a 400-character limit on the directory path to a file in SharePoint. 
  
After the migration, the file path will look like the following.
  
> Personal/bobsmith_contoso_com/Documents/Folder1/Folder2
    
Notice the URL is now 4 characters longer than it was before. Depending on how the UPNs are formed at your company, the change in length may be larger.
  
If the previous file in the source environment was 255 characters, the length after migration would be 259 characters. 
  
We have identified 4 different locations in which failures are likely to occur due to long URLs. As a result, we have 4 different reports concerning long URLs. The Scan Result Reports section covers each report along with the remediation that needs to occur.
  
## Data Migration

The migration of the source content resulting in the long URLs will fail. This will cause migration jobs to fail, which will prolong the migration project unnecessarily.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Review the reports and follow the remediation recommended for each report. In general, the remediation involves moving the content closer to the root of the site collection.
  
## Post Migration

Validate that your content has been migrated.
  
## Scan Result Reports

This scan results in 4 output files. Each file is for a specific long URL issue that will result in migration failures. **LongODBUrl-AllDocs-detail.csv** There are two limitations related to the length of the path to a given file: 
  
- The server relative path to the folder containing the file has a maximum of 400 characters. Using the following example file:
    
    https://OneDrive.contoto.com/Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx
    
    The directory name would be the following: Personal/contoso_bobsmith/Documents/Folder1/Folder2
    
    After the migration, the file path will look like the following. Notice the URL is now longer than it was before: Personal/bobsmith_contoso_com/Documents/Folder1/Folder2
    
- The server relative path to a file or folder has a total maximum of 400 characters. Using the following example file:
    
    https://OneDrive.contoto.com/Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx
    
    The server relative path to the file will look similar to the following: Personal/contoso_bobsmith/Documents/Folder1/Folder2/ProjectA.docx
    
If there are files listed in this report, the owners will need to move the files to shorter paths or delete the files. For example, they could move ProjectA.docx up to a folder directly under Documents, or they could delete the file if it is no longer needed.
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|LastContentModifiedDate  <br/> |Date/Time the site collection had content modified.  <br/> |
|TotalItemCount  <br/> |Total number of items found in the site collection.  <br/> |
|Hits  <br/> |Number of requests logged for the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DistinctUsers  <br/> |Number of distinct users that have accessed the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 days.  <br/> |
|UPN  <br/> |UPN that was used to determine the difference in the URL length. If the UPN is "\*\*\*\*" that indicates the owner did not have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName values in the SharePoint profile store was used.  <br/> |
|URLLengthDifference  <br/> |Amount the URL will grow when the site is renamed.  <br/> |
|File  <br/> |File that needs to be remediated.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   
 **LongODBUrl-NavNodes-detail.csv** Navigation nodes have a URL length limitation of 260 characters. This can lead to the URL field exceeding the maximum length. 
  
For example, you have a OneDrive site at https://OneDrive.contoso.com/personal/contoso_bobsmith. That site has a link in the Quick launch named Reports and the URL of the link points to https://onedrive.contoso.com/personal/contoso_bobsmith/documents/folder1/…folderN/Reports. During the migration, SharePoint will update the URL to point to /bobsmith_contoso_com/. The additional length added to the URL may result in the length being over 260 characters, which will cause the migration to fail.
  
To remediate this issue, you would move the reports folder close to the root of the /documents/ library and then update the quick launch link. Another option would be to remove the quick launch link.
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|UPN  <br/> |UPN that was used to determine the difference in the URL length. If the UPN is "\*\*\*\*" that indicates the owner did not have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used.  <br/> |
|URLLengthDifference  <br/> |URLLengthDifference Amount the URL will grow when the site is renamed.  <br/> |
|WebURL  <br/> |URL to the web that has the navigation node.  <br/> |
|NavigationNodeLocation  <br/> |Navigation Node titles showing where the navigation node lives. You can have multiple levels of navigation nodes, and this will help locate the offending node.  <br/> |
|NavigationNodeTitle  <br/> |Title of the impacted navigation node.  <br/> |
|NavigationNodeURL  <br/> |URL that will be too long after the site rename.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   
 **LongODBUrl-Perms-detail.csv** Permissions that are set on an object in SharePoint are tracked by the URL of that object. If you set permissions on a folder, SharePoint will store the relative path to the folder. If you set permissions on an item, SharePoint will store the server relative path to the item. 
  
As a result, during a site migration, the URLs associated with permissions will be updated. This may lead to failures if the new URL is too long.
  
The remediation for this is to move the affected object closer to the root of the site collection. Another option is to remove the distinct permissions from the items in the report.
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|UPN  <br/> |UPN UserPrincipalName that was used to determine the difference in the URL length. If the UPN is "\*\*\*\*" that indicates the owner did not have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used.  <br/> |
|URLLengthDifference  <br/> |Amount the URL will grow when the site is renamed.  <br/> |
|WebURL  <br/> |URL to the web hosting the secured object.  <br/> |
|SecuredObject  <br/> |This is the URL to the secured object that will be too long after the site rename. If you add permissions to a file, this is the server relative path to the file. If you set permissions on a folder, this is the server relative path to the folder.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   
 **LongODBUrl-Deps-detail.csv** Certain files can have additional dependencies. Those dependencies are tracked by the URL. During the migration if the dependency information is too long, the migration will fail. 
  
There are two limitations in this report to be aware of:
  
- FullURL has a limit of 260 characters. This is the file with the dependencies. To remediate if the FullURL is too long, either remove the file or move the file to a location closer to the root of the site collection.
    
- DependencyDescription has a limit of 270 characters. This is the dependency associated with the FullURL. To remediate the DependencyDescription, either remove the dependency or move the dependency closer to the root of the site collection.
    
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|UPN  <br/> |UPN that was used to determine the difference in the URL length. If the UPN is "\*\*\*\*", that indicates the owner did not have a UserPrincipalName set in their SharePoint profile. As a result, the average length of the UserPrincipalName in the SharePoint profile store was used.  <br/> |
|URLLengthDifference  <br/> |Amount the URL will grow when the site is renamed.  <br/> |
|FullURL  <br/> |URL to the file that has the dependencies  <br/> |
|DependencyDescription  <br/> |DependencyDescription Description associated with the dependency. This may be a URL that is getting renamed.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

