---
title: "Set Default Organization Version Limits"
ms.reviewer: rekamath
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
description: "This article provides guidance on how Version History settings work."

---


## Trim Existing Versions from Sites or Libraries

As a SharePoint Site Administrator, you can queue a job to trim existing versions on your sites to reduce the version storage footprint of your site. You can also align existing version storage with updated version history limits by scheduling a job to trim existing versions. There are several things you need to consider before you decide to trim existing version history on a site or library. Version availability is critical for recovery scenarios like undoing unwanted changes. Versions deleted using trimming jobs are permanently deleted. This deletion workflow bypasses the normal recycle bin and deleted versions can't be recovered.

| **Phase** | **Recommended Actions** |
| --- | --- |
| Prepare | **Evaluate your recovery objectives and target version storage use:** Determine the right trim mode and trim scope that you will need to meet your organization’s recovery objectives.  <br><br>&nbsp;<br><br>**Review Impact:** Before committing to trim existing versions, you have the option to review the impact of the purge action by running a ‘What-if’ analysis operation of the selected trim mode on the specified scope. |
| Queue Job | Once you are ready to commit to a trim job, you can queue a version trimming job to asynchronously delete versions matching the criteria specified in the trim mode within a Site, Library or OneDrive user account. |
| Track Progress | &nbsp; |



:::image type="content" source="media/version-history/trimming-workflows.png" lightbox="media/version-history/trimming-workflows.png" alt-text="Diagram of trimming workflows":::

### Queue Trim Job

The version trimming workflow uses a job to asynchronously delete versions matching the criteria specified in the trim mode. To queue a trim job, you need to follow these steps:

1. **Set Trim Scope:** Determine the **Scope [Site, Library]** for version deletion. You can delete old file versions for all document libraries in a site or for a specific document library.

1. **Set Trim Mode:** Determine the **Trim Mode** you wish to apply for trimming file versions within the specified scope.

1. **Review Impact:** Before committing to trim existing versions, you can review the impact of the purge action by running a 'What-if' analysis operation of the selected trim mode on the specified scope.

1. **Queue Trim Job:** Once you're ready to commit to the trim, you can queue the job to asynchronously delete versions matching the trim mode criteria.

1. **Track progress:** You're able to monitor the progress of committed trim jobs to keep track of the deletion progress.  

### Review impact by running 'What-if' Analysis

Before committing to trim existing versions, you can review the impact of the purge action by running a 'What-if' analysis operation. Running a 'What-if' operation follows these steps:  

**Step 1: Generate a Version Storage Use report for a Site or Library:** This report can support multiple uses including version storage use analytics or to gain key insights on the impact of applying different trimming settings.

**Step 2: Run 'What-If' analysis** to preview the changes and analyze the user and storage savings impact of applying one of the trimming modes to the version storage report csv file.  

> [!IMPORTANT]
> - You need to be a Site Administrator of the site to generate reports and trim versions from document libraries in a site.
> - Depending on the size of the Site or Library, the job can take a few days to complete. Check the progress of the job until the status shows "completed".

### Trim Modes

Version trimming workflows allow you to select and apply one of the trimming modes for scheduling a trim job on a site or library.

- **Manual Expiration:** The manual expiration mode sets the target expiration date on matching versions with the specified value.

  :::image type="content" source="media/version-history/manual-expiration-trim-table.png" lightbox="media/version-history/manual-expiration-trim-table.png" alt-text="Diagram of manual expiration":::

The following are the known limitations.

1. The API doesn't delete versions created in the last 30 days. This means your input to the API can't be less than 30 days.

1. The API always deletes all versions that were created before January 1, 2023. If you want to trim versions, you can't keep any older than that. This means the value you use for the `DeleteBeforeDays` parameter should result in date after January 1, 2023.

   - **Manual Count Limit:** The manual count limit trim mode sets the target expiration date on oldest versions exceeding specified count limit to be deleted right away.

     :::image type="content" source="media/version-history/manual-count-limit-trim-table.png" lightbox="media/version-history/manual-count-limit-trim-table.png" alt-text="Diagram of manual count limit":::



### Learn More

For more information, check out the following resources:

- [Tutorial: Generate Version Usage Report](tutorial-generate-version-usage-report.md).
- [Tutorial: Run 'What-If' analysis](tutorial-run-what-if-analysis.md).
- [Tutorial: Queue Trim Job](tutorial-queue-a-trim-job.md).
