---
title: "Tutorial: Queue a trim job"
ms.reviewer: rekamath
ms.author: ruihu
author: maggierui
manager: jtemper
recommendations: true
ms.date: 10/03/2024
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
description: "This article provides guidance on how to queue a trim job for a site or document library."

---

# Tutorial: Queue a trim job for a site or document library

In this tutorial, you'll learn how to trim existing versions from a site or library by queuing a trim job using PowerShell. You'll learn how to:

- Queue a job to trim versions from a site.
- Queue a job to trim versions from a library.
- Check progress of your trim job.
- Stop an in-progress trim job.


## Before you begin

Versions deleted by a trim job are permanently deleted and can't be recovered from the recycle bin. We recommend you prepare by performing the following actions: 
- Review your **organization’s recovery objectives** and **version storage usage quota targets** to help determine the trim action and scope needed to meet your requirements.
 
- If needed, [run an impact analysis](tutorial-run-what-if-analysis.md) to understand the trimming impact.
- Determine the **scope of** version deletion. You can create jobs to delete old file versions for all document libraries in a site or for a specific document library.  
- Determine the **trim mode** you want to apply on existing versions. You can choose to delete based on version age, count limit, or based on the automatic algorithm.


## Queue a job to trim versions on site

You can queue a job to trim versions for all document libraries in the site collection using the `New-SPOSiteFileVersionBatchDeleteJob` PowerShell command. 
- Use the `<DeleteBeforeDays>` parameter to specify the age criteria you wish to apply for deleting versions. Versions older than the specified days are deleted asynchronously in batches in the upcoming days. 
- Use the `<MajorVersionLimit>` to specify the count limit of major versions to store. Oldest versions exceeding the specified count are deleted asynchronously in batches in the upcoming days. 
- Use the `<Automatic>` parameter to apply Automatic setting trimming logic on existing file versions. 


### Example: Queue a job to trim versions based on age for all libraries on a site

In the following example, the job is queued to trim versions that are older than 180 days for all document libraries in the site collection `https://contoso.sharepoint.com/sites/site1`.

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity https://contoso.sharepoint.com/sites/site1 -DeleteBeforeDays 180 
```

### Example: Queue a job to trim oldest versions exceeding the specified count limit on a site

In the example below, the job is queued to trim oldest versions that exceed 100 major version count limit for all document libraries in the site collection `https://contoso.sharepoint.com/sites/site1`.  

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity https://contoso.sharepoint.com/sites/site1 -MajorVersionLimit 100 -MajorWithMinorVersionsLimit 0
```
### Example: Queue a job to trim versions based on the automatic logic on a site

In the example below, the job is queued to trim versions based on the Automatic algorithm for all document libraries in the site collection `https://contoso.sharepoint.com/sites/site1`.  

```PowerShell
New-SPOSiteFileVersionBatchDeleteJob -Identity https://contoso.sharepoint.com/sites/site1 -Automatic 
```

## Queue a job to trim versions on a document library

You can queue a job to trim versions from a particular document library in the site collection using the `New-SPOListFileVersionBatchDeleteJob` PowerShell command. 
- Use the `<DeleteBeforeDays>` parameter to specify the age criteria you wish to apply for deleting versions. Versions older than the specified days are asynchronously in batches in the upcoming days. 
- Use the `<MajorVersionLimit>` to specify the count limit of major versions to store. Oldest versions exceeding the specified count are deleted asynchronously in batches in the upcoming days. 
- Use the `<Automatic>` parameter to apply Automatic setting trimming logic on existing file versions. 


### Example: Queue a job to trim versions based on age on a single library on a site

To delete versions that are older than 360 days in document library 'Documents' in the site collection `https://contoso.sharepoint.com`.

```PowerShell
New-SPOListFileVersionBatchDeleteJob -Site https://contoso.sharepoint.com -List "Documents" -DeleteBeforeDays 360 
```

## Track progress of a trim job

You can track progress of the trim job using the `Get-SPOSiteFileVersionBatchDeleteJobProgress` cmdlet.

In the following example, the cmdlet reports the progress of the trim job for `https://contoso.sharepoint.com/sites/site1`

```PowerShell
Get-SPOSiteFileVersionBatchDeleteJobProgress -Identity https://contoso.sharepoint.com/sites/site1
```

## Stop an in-progress trim job

If needed, you can cancel an in-progress trim job. Once the cmdlet executes successfully, the in-progress job is stopped and no further deletions happen. 

> [!NOTE]
> Stopping a trim job doesn't revert versions that have already been deleted.

### Example: Stop a site trim job

To stop an in-progress trim job from additional version trimming on the site collection `https://contoso.sharepoint.com/sites/site1`:

```PowerShell
Remove-SPOSiteFileVersionBatchDeleteJob -Identity https://contoso.sharepoint.com/sites/site1
```

### Example: Stop a library trim job

To stop an in-progress trim job from additional version trimming in document library 'Documents' in site collection `https://contoso.sharepoint.com/sites/site1`:

```PowerShell
Remove-SPOListFileVersionBatchDeleteJob -Site https://contoso.sharepoint.com/sites/site1 -List "Documents"
```

