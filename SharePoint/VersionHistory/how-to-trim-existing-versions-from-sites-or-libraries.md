---
title: "How to Trim Existing Versions from Sites or Libraries"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/12/2023
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
description: "This article provides guidance on how to trim existing versions from sites or libraries."

---

# How to Trim Existing Versions from Sites or Libraries

This article describes how Site Administrators can trim existing version history on a Site or Document Library. Trimming existing versions is performed in the following sequence of steps:  

1. **Generate a ‘What-If File Expiration report’ for Site or Document Library**. Depending on the size of the Site or Library, the job can take a couple of days to complete. Check the progress of the job until the status returns as “complete.”  

1. **Update the ‘What-If File Expiration report’ to apply one of the 3 different trimming modes**: Download the report file to your local computer and apply the provided scripts to apply the desired setting to the file - **Automatic**, **Manual Expiration Limits** or **Manual with Count Limits Only**. If needed, you could apply PowerShell and Excel examples to understand the impact of the selected setting on version storage or impacted users. This step converts the ‘What-If File Expiration report’ into the ‘Schedule input file’ needed to queue a scheduling job.  

1. **Schedule the job to trim versions for your Sites or Libraries**: You can optimize the size of ‘Schedule Input File’ by applying the scripts provided. Then upload the ‘Schedule Input file’ to SharePoint a document library in the same site as the site you're deleting versions from followed by queuing the trimming job. Once the job is queued, you can check the status of your trimming job.
 
> [!IMPORTANT]
> You need to be a Site Administrator of the site to generate reports and trim versions from document libraries in a site.

## Step 1: Generate ‘What-If’ Report for Sites or Library

- Before you begin, determine the **Report Scope** (Site or Document Library) and the **Report Location** (a location within your SharePoint site that you want to save the report to).

- Here’s a PowerShell script that generates a **site-scoped** report at the **report location**, `https://contoso.sharepoint.com/Shared Documents/SiteReport.csv.` Ensure that the report location is within a SharePoint document library.

:::image type="content" source="media/generate-powershell.PNG" alt-text="":::

:::image type="content" source="media/generate-powershell-1.PNG" alt-text="":::

- Here’s a PowerShell script that generates a **library-scoped** report at the **report location**, `https://contoso.sharepoint.com/Shared Documents/SiteReport.csv.` Ensure that the report location is within a SharePoint document library.

> [!IMPORTANT]
> The file version report generation job is complete asynchronously over the next few days. The completion time of the report depends on the size of your library or site.
> While the job is processing, you will see the report file being gradually populated. Do not update the file during this time, as it may lead to job failure. Check the progress of the report generation to ensure that the report is fully populated and ready to process.
> If you want to cancel a report generation in progress, you can simply delete the report file.

:::image type="content" source="media/library-scoped-report-powershell.PNG" alt-text=""::: 

### Check the progress of generating a file version expiration report 

- Here’s a PowerShell script that allows you to check if your **site scoped report** is fully populated and ready to be analyzed.

:::image type="content" source="media/site-scoped-report.PNG" alt-text=""::: 

- Here’s a PowerShell script that allows you to check if your **library scoped report** is fully populated and ready to be analyzed.

:::image type="content" source="media/library-scoped-report-analysed.PNG" alt-text="":::

- The API returns in JSON format, and the value will look like one of the following values:
 
:::image type="content" source="media/json-powershell.PNG" alt-text="":::

## Step 2: Update File Version Expiration Report File with Desired Trimming Setting

- Here's an example of PowerShell script you could apply to generate a What-If Report file that applies the **Automatic Expiration**  policy on the report file `C:\Report.csv`.  

:::image type="content" source="media/expiration-automation.PNG" alt-text="":::

- Here's an example of PowerShell script to generate a What-If Report file. It applies **Manual Expiration** with expire-after days set to 30 on the report file `C:\Report.csv`.  

:::image type="content" source="media/manual-expiration.PNG" alt-text="":::

- Here's an example of PowerShell script to generate a What-If Report file, It applies a **Manual with Count Limits** policy with major version limit set to 50 on the report file `C:\Report.csv`.

:::image type="content" source="media/manual-with-count-limits-a.PNG" alt-text="":::

:::image type="content" source="media/manual-with-count-limits-b.PNG" alt-text="":::

## Step 3: Schedule Job to Trim Existing Versions

### Optimize the File Expiration Report

- Use the `OptimizeScheduleFile.ps1` script to optimize the File Expiration Report in PowerShell. <br>`. <Path to OptimizeScheduleFile.ps1>” -ImportPath “<Path to the schedule file>” -ExportPath “<Path to the optimized schedule file>`

- For instance, if your folder has the script and the schedule file, Schedule.csv, and you want to create an optimized schedule file named `Schedule_Optimized.csv` under the same folder, you can execute the command in PowerShell. You'll see a new file `Schedule_Optimized.csv` in folder.  

### Queue Version Trimming Job

- Upload the new schedule file to a document library that is in the same site collection as the one you're deleting version from.

:::image type="content" source="media/schedule-optimiser.PNG" alt-text="":::

- Use cmdlet included in VersionUtils.ps1 script to queue a version expiration scheduling job.

- For example, if you're scheduling a job for the [site](https://contoso.sharepoint.com), using the schedule file `https://contoso.sharepoint.com/Shared Documents/Schedule.csv`, run the following command in PowerShell.

:::image type="content" source="media/schedule-a-job-powershell.PNG" alt-text="":::

:::image type="content" source="media/schedule-a-job-powershell-1.PNG" alt-text="":::

- Then, all the versions in the schedule file update their expiration time to your specified time. It completes asynchronously in the upcoming days. The specific length of time is dependent on how many versions are being deleted or expired.  

### Check progress for a file version expiration scheduling job

- Use the cmdlet included in `VersionUtils.ps1` script to check the status of a version expiration scheduling job.  

- For example, if you're scheduling a job for the [site](https://contoso.sharepoint.com), using the schedule file `https://contoso.sharepoint.com/Shared Documents/Schedule.csv`, run the following command in PowerShell.

:::image type="content" source="media/version-expiration-scheduling-job.PNG" alt-text="":::

- JSON strings are returned in one of the following formats:

:::image type="content" source="media/version-expiration-scheduling-job-json.PNG" alt-text="":::

