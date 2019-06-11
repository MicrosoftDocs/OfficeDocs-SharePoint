---
title: "Migration Assessment Scan Browser File Handling"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
ms.custom:
ms.assetid: a65e4c80-cb0a-4944-a3a3-807d01b1f756
description: "Learn how to mitigate issues with Browser File Handling during migration."
---

# Migration Assessment Scan: Browser File Handling

Learn how to mitigate issues with Browser File Handling during migration.
  
## Overview

The Browser File Handling settings on the Web Applications in SharePoint impact how you can browse certain file types. The source environment allowed you to change this setting from Strict to Permissive. The Permissive setting enables you to open all file types within the browser. However, in the target environment, the Strict setting is enforced and cannot be modified. As a result, you may find some file types will not open in the browser post migration. For example, \*.htm and \*.html files in document libraries will no longer open in the browser. Users will be prompted to download the files.
  
The main reason for the change is that the Strict setting is more secure. There is a potential elevation of privilege scenario where a malicious user with contributor access to a site could create an HTML file that contains JavaScript that runs against a different site collection that they do not have permissions to. They then have a user that does have permissions to browse the page, which results in the elevated user executing the JavaScript and accessing the data that the malicious user was after.
  
## Data Migration

Data will be migrated, but the behavior with the HTM and HTML files will change from opening within the browser to prompting the user to download. If you have an HTM or HTML page as the target of a Page View web part, when the page renders, you will get a prompt to download the HTM or HTML file. The Page Viewer web part renders as an iframe, so there is a background request for the HTM or HTML page, which results in the download prompt. You are unable to rename the file extension in the browser. However, if you rename the files using SharePoint Designer, you will get a prompt to fix the URL reference.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

The provided report will contain a list of all the HTM and HTML files in your environment. Contact the site owners to ensure they are aware of the issue. If the files are required to open in the browser, rename them to \*.aspx. Uploading an ASPX file requires Designer access to a site collection, which reduces the footprint of the risk to people that have more permissions than Contribute. A contributor is able to create wiki pages on some document libraries, which are technically ASPX pages, however, the contributor permissions will restrict the user's ability to add or configure web parts that would expose a cross site scripting attack on these pages. For example, the following will occur for a contributor attempting to add web parts to an ASPX page:
  
- Content Editor web part is not available as an option.
    
- Script Editor web part is available, but will not allow a user to submit anything with \<script\> tags.
    
- Page Viewer web part does not allow a contributor to modify the URL setting. Blocking them from pointing the user to a malicious page.
    
Options for renaming the file extension of a file:
  
- Open the site in SharePoint Designer and rename the file.
    
- Programmatically rename files using SPFile.MoveTo() via CSOM.
    
## Post Migration

Validate that your pages render as expected.
  
## Scan Result Reports

The following table describes the columns in the **BrowserFileHandling-detail.csv** report. 
  
This scan report contains all the \*.htm and \*.html files that will be impacted by the Browser File Handling change from Permissive to Strict.
  
|**Column﻿**|**Description﻿**|
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
|File﻿  <br/> |Url to the file impacted by the change.﻿  <br/> |
|TimeCreated﻿  <br/> |Date and time the file was created.﻿  <br/> |
|TimeModified﻿  <br/> |Date and time the file was modified﻿.  <br/> |
|ModifiedBy﻿  <br/> |User that modified the file last.﻿  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

