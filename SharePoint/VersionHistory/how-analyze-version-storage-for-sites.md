---
title: "How Version History settings work"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/13/2023
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
description: "This article provides guidance on how to analyze version storage for sites ."

---

# How to Analyze Version Storage for Sites

Once you have set the `TargetExpirationDate` values for your report, you can choose to perform deeper analysis on the report to see the effect of the trimming before running an actual trim. You can perform this analysis on your own, but we also provide 2 recommended options for your analysis.  

## Option one: Analyze the report using excel

Open the shared Excel workbook **AnalyzeReportFile_Template.xlsx**. You can find the following worksheets in it.  

- **Configuration**: Use this worksheet to set the date range for generating the different report views. 
- **Dataset**: This is the raw dataset imported from the report file. Various reporting summary views are constructed from this dataset.
- **Preset Reports**: The following is a list of preset views that can be used to understand the impact of applying the selected setting on versions stored in the site:
    - **Summary**: Use this view to analyze the current state of version storage for this site and deleted version distribution under the new settings.
    - **Impacted Users**: Review the users whose versions would be impacted under the new settings.
    - **Version Count**: A table and graph showing the numbers of versions that will be available over time under the current schedule and the number of versions that will be available under the new schedule.
    - **Size of Versions Expired**: Compare the size of versions that will be deleted over time under the current schedule and the number of versions that will be available under the new schedule.
    - **File Level Analysis**: Review file level version deletions under the new settings  

Follow these steps to populate the workbook:

1. On the **Configuration** worksheet, enter the full path to the What-If report file in **Cell B3**.

:::image type="content" source="media/analyze-version-step1.PNG" alt-text="configuration worksheet":::

2. (Optional) If you want to change the date range of graphs in **Number of Versions Availabl**e worksheet, or **Size of Versions Expired** worksheet, change the corresponding values in Cells B6, B7, B10, and/or B11.  

:::image type="content" source="media/analyze-version-step2.PNG" alt-text="":::

3. On the top of Excel, click on the **Data** tab, then, in the Ribbon, click on the **Refresh All** button.

:::image type="content" source="media/analyze-version-step3.PNG" alt-text="":::

4. On the **Calculations** worksheet, autofill the **Number of Versions** and **Number of Versions Remaining After Deletion** columns.

:::image type="content" source="media/analyze-version-step4-a.PNG" alt-text="":::

:::image type="content" source="media/analyze-version-step4-b.PNG" alt-text="":::

5. On the **Impacted Users** worksheet, autofill the **Number of Versions Will be Deleted** column.

:::image type="content" source="media/analyze-version-step5.PNG" alt-text="":::

All worksheets should now be up to date. You can check the information you are interested in.

## Option two: Analyze the report using powershell

Save the script as a file named **AnalyzeReportFile.ps1.**

:::image type="content" source="media/analyze-report-powershell.PNG" alt-text="":::
analyze-report-powershell

Open PowerShell 7 and run the following command, replacing the placeholder values with the appropriate values.  

:::image type="content" source="media/analyze-report-powershell-command.PNG" alt-text="":::
analyze-report-powershell

The output displays four tables.

1. Current Expiration Schedule: this table contains a time-series summary for your versions as they are. It has these columns: 
    1. Date: a date,  
    1. NumberOfVersionsAvailable: the number of versions available on that date under the current schedule,  
    1. NumberOfVersionsExpired: the number of versions expired on that date under the current schedule, and  
    1. SizeOfVersionsExpiredMB: the size of versions expired on that date under the current schedule.  

:::image type="content" source="media/current-expiration-schedule.PNG" alt-text="":::
analyze-report-powershell

1. Target Expiration Schedule: the same as above but reflects that of the updated schedule instead. This is only helpful if you want to test out different expiration scenarios by changing the TargetExpirationDate column in the file version expiration report.  

:::image type="content" source="media/target-expiration-schedule.PNG" alt-text="":::
analyze-report-powershell

1. Files with Fewer Than 10 Versions: a list of the URLs, and the number of versions before and after the deletion for those files whose number of versions is fewer than 10 after immediate deletion (but was more than 10 before the immediate deletion).  

:::image type="content" source="media/files-with-fewer-than-10-versions.PNG" alt-text="":::
analyze-report-powershell

1. Users Impacted: the users whose versions would be immediately deleted. 

:::image type="content" source="media/users-impacted.PNG" alt-text="":::
analyze-report-powershell

Optionally, you may adjust the parameters: 

- `TimelineStartDate`: the starting date for Table 1 and 2 above.
- `TimelineStepDays`: the number of days in between rows for Table 1 and 2 above.  
- `TimelineNumSteps`: the number of rows to calculate for Table 1 and 2 above.  
- `ShowFilesWithFewerThanNVersions`: the threshold for the number of versions in Table 3 above.
