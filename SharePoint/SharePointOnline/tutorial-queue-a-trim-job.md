---
title: "Tutorial: Queue a Trim job(Preview)"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 04/30/2024
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- SPO160
- SPS150
- MET150
description: "This article provides guidance on how to queue a Trim job for a site or document library."

---

# Tutorial: Queue a Trim job for a Site or Document Library(Preview)

In this tutorial, you'll learn how to trim existing versions from a site or library by queuing a trim job using PowerShell. You'll learn how to:

- Queue trim job to delete versions from a site
- Queue trim job to delete versions from a library.
- Check progress of your trim job
- Stop an in-progress trim job.


## Before you begin

Versions deleted using the batch delete trimming are permanently deleted and can't be recovered from the recycle bin. We recommend you prepare by performing the following actions: 
- Review your organization’s recovery objectives and version storage usage quota targets to help determine the trim action and scope needed to meet your requirements. 
- If needed, run an impact analysis to understand the trimming impact.
- Determine the scope of version deletion. You can create jobs to delete old file versions for all document libraries in a site or for a specific document library.  
- Determine the trim mode you want to apply on existing versions. You can choose to delete based on version age, count limit, or based on the automatic algorithm.


## Queue trim job to delete versions on Site

You can queue a job to trim versions for all document libraries in the site collection using the `New-SPOSiteFileVersionBatchDeleteJob` PowerShell command. 
- Use the `-<DeleteBeforeDays>` parameter to specify the age criteria you wish to apply for deleting versions. Versions older than the specified days are deleted asynchronously in batches in the upcoming days. 
- Use the `<MajorVersionLimit>` to specify the count limit of major versions to store. Oldest versions exceeding the specified count are deleted asynchronously in batches in the upcoming days. 
- Use the `<Automatic>` parameter to apply Automatic setting trimming logic on existing file versions. 


**Example: Queue trim job to delete versions based on age for all libraries on a Site.**

In the example below, the trim job is queued to  delete versions that are older than 180 days old for all document libraries in the site collection https://contoso.sharepoint.com.

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl -DeleteBeforeDays 180
```

**Example: Queue trim job to delete the oldest versions exceeding the specified count limit on a Site.**

In the example below, the trim job is queued to delete oldest versions that exceed 100 major version count limit for all document libraries in the site collection ‘https://contoso.sharepoint.com’.  

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl - MajorVersionLimit 100
```
**Example: Queue trim job to delete the versions based on the Automatic logic on a Site.**

In the example below, the trim job is queued to delete versions based on the Automatic algorithm for all document libraries in the site collection ‘https://contoso.sharepoint.com’.  

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl -DeleteBeforeDays 180
```

## Queue trim job to delete versions on a Document Library

You can queue a job to trim versions from a particular document library in the site collection using the `New-SPOListFileVersionBatchDeleteJob` PowerShell command. 
- Use the `<DeleteBeforeDays>` parameter to specify the age criteria you wish to apply for deleting versions. Versions older than the specified days are asynchronously in batches in the upcoming days. 
- Use the `<MajorVersionLimit>` to specify the count limit of major versions to store. Oldest versions exceeding the specified count are deleted asynchronously in batches in the upcoming days. 
- Use the `<Automatic>` parameter to apply Automatic setting trimming logic on existing file versions. 


**Example: Queue trim job to delete versions based on age on a single Library on a site.**

To delete versions that are older than 180 days in document library 'Documents' in the site collection `https://contoso.sharepoint.com`.

```PowerShell
New-SPOListFileVersionBatchDeleteJob -Site $siteUrl -list $libName -DeleteBeforeDays 180
```

## Cancel an in-progress Batch Trim Job

If needed, you can cancel an in-progress batch trim job. Once the cmdlet executes successfully, the in-progress job is stopped and no further deletions  happen. 

> [!NOTE]
> Stopping a trim job doesn't revert versions that have already been deleted.

**Example: Stop additional batch deletion on site scoped trim job.**

To stop the additional batch deletion for the site collection `https://contoso.sharepoint.com`.

```PowerShell
# connect to the site that contains the library

Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin
$Site = Get-PnPSite
Remove-PnPFileVersionBatchDeleteJob -Site $Site
```

**Example: Stop additional batch deletion on library scoped trim job.**

To stop the additional batch deletion for the document library Documents in site collection `https://contoso.sharepoint.com`.

```PowerShell
# connect to the site that contains the library
Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin
$Site = Get-PnPSite
Remove-PnPFileVersionBatchDeleteJob -Library $Library
```

