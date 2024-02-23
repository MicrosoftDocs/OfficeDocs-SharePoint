---
title: "Tutorial: Generate and Analyze Version Usage Report for SharePoint Site"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 02/22/2024
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
description: "This article provides guidance on how to generate and analyze Version Usage Report for SharePoint Site."

---

# Tutorial: Generate Version Usage Report (Preview)

By understanding version storage on a site, you can better optimize the version history settings to meet your organization’s recovery objectives and manage storage costs.

This tutorial shows you how to generate a version storage use report and analyze it to better understand the version storage footprint of the site. The report can also be used to perform ‘What-if’ analysis of applying different version limits or trimming existing versions.  

In this tutorial we cover how to:

- Generate Version storage use report file for Site or Library.
- Check progress of report generation.
- Understand the report file.
- Analyze version storage use using Excel or PowerShell.

## Generate Version Use Report for Sites or Library

Before you begin, determine the **Report Scope** (Site or Document Library); **Report Location** (a location within a SharePoint document library that you want to save the report to). The Report Location tells us where to generate a report file, and it should be a link to a file and there can't be a file with the same name.

Here’s an example of the PowerShell script that generates a **site-scoped** report at the `report location`, `https://contoso.sharepoint.com/SharedDocuments/SiteReport.csv`.  

> [!NOTE]
> The report location is within a SharePoint document library.

```PowerShell
# Connect to the site that you would like to run a report on
Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin

#Get the site object and start a report.
$Site = Get-PnPSite

New-PnPFileVersionExpirationReportJob -Site $Site -ReportUrl 
"https://contoso.sharepoint.com/Shared Documents/SiteReport.csv"
```

:::image type="content" source="media/version-history/powershell-site-scoped-1.png" lightbox="media/version-history/powershell-site-scoped-1.png" alt-text="powershell site scoped 1":::

Here’s a PowerShell script that generates a **library-scoped** report at the **report location**, `https://contoso.sharepoint.com/Shared Documents/SiteReport.csv.` Ensure that the report location is within a SharePoint document library.

> [!NOTE]
> The report location is within a SharePoint document library.

```PowerShell
# Connect to the site that you would like to run a report on 
Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin

#Get the library object and start a report. 
$Library = Get-PnPList "MyLibrary"

New-PnPFileVersionExpirationReportJob -Library $Library - ReportUrl 
https://contoso.sharepoint.com/Shared Documents/LibraryReport.csv
```

:::image type="content" source="media/version-history/library-scoped-report-powershell.png" lightbox="media/version-history/library-scoped-report-powershell.png" alt-text="library scoped report powershell":::

> [!IMPORTANT]
> The file version report generation job is complete asynchronously over the next few days. The completion time of the report depends on the size of your library or site.
>
> While the job is processing, you will see the report file being gradually populated. Do not update the file during this time, as it may lead to job failure. Check the progress of the report generation to ensure that the report is fully populated and ready to process.
>
> If you want to cancel a report generation in progress, you can simply delete the report file.

## Check Report Generation Progress

Here’s a PowerShell script that allows you to check if your **site scoped report** is fully populated and ready to be analyzed.

```PowerShell
# Connect to the site that you would like to run a report on
Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin 

#Get the site object and check the status of the report.
$Site Get-PnPSite

Get-PnPFileVersionExpirationReport JobProgress -Site $Site -ReportUrl 
"https://contoso.sharepoint.com/Shared Documents/SiteReport.csv"
```

:::image type="content" source="media/version-history/site-scoped-report.png" lightbox="media/version-history/site-scoped-report.png" alt-text="site scoped report":::

Here’s a PowerShell script that allows you to check if your **library scoped report** is fully populated and ready to be analyzed.

```PowerShell
# Connect to the site that contains the library
Connect-PnPOnline -Url "https://contoso.sharepoint.com" -UseWebLogin

#Get the library object check the status of the report. 
$Library = Get-PnPList "MyLibrary"

Get-PnPFileVersionExpirationReport JobProgress -Library $Library -ReportUrl 
"https://contoso.sharepoint.com/Shared Documents/Library Report.csv"    
```

:::image type="content" source="media/version-history/library-scoped-report-analysed.png" lightbox="media/version-history/library-scoped-report-analysed.png" alt-text="library scoped report analysed":::

The cmdlet returns in JSON format, and the value appears as one of the following values:

```PowerShell
JSON Response Value and Explanations

{"status": "covmpleted"}: the job is complete, and the report is fully populated.
{"status": "in_progress"}: there is an active job, and the report is partially populated.
{"status": "no_report_found"}: there are no active jobs populating this file.
{"status": "failed", "error_message": "<error message>"}; there are no active jobs 
populating this file, but there was one and it failed.
```

## Understand Version Report File

Here’s an example of file version expiration report and its column breakdown.

:::image type="content" source="media/version-history/expiration-report.png" lightbox="media/version-history/expiration-report.png" alt-text="expiration report":::

There are 12 rows in this table. The first row is the header row. The compact columns are denoted with *.Compact* post-fix. The other 11 rows represent file versions, where each row represents 1 version.

Let’s go through the first file version displayed in this report.  

- `WebId`, `DocId`, `MajorVersion`, and `MinorVersion` uniquely identify this version in your SharePoint site.  

- `WebUrl` indicates the version in the [web](https://contoso.sharepoint.com), and `FileUrl` indicates that the file for this version is located at DocLib/MyDocument.docx. In other words, it is in a Document Library called `DocLib`, while the file is in the root folder of `DocLib` and is named MyDocument.docx.  

- `Size` indicates that the version takes 92,246 bytes of storage.  

- The next two columns, `ModifiedBy_UserId` and `ModifiedBy_DisplayName` indicate that the user, Michelle Harris (with user ID 6), has created this version.  

- `LastModifiedDate` indicates that the version’s content was last modified on March 13, 2023, at 22:36:09 UTC. `SnapshotDate` displays that the version became a historical version on March 20, 2023, at 16:56:51 UTC. `IsSnapshotDateEstimated` shows that `SnapshotDate` is the actual snapshot date.  

- `CurrentExpirationDate` indicates that this version is currently set to never expire. `AutomaticPolicyExpirationDate` shows that under the automatically expire policy, this version is also set to never expire. `TargetExpirationDate` indicates that if we follow this schedule for trimming, we would set this version to never expire.  

Let’s look at the third version.  

The `WebId` and `DocId` values are empty because these columns are compact columns, denoted by *.Compact* post-fix, it means they should have values. If we look for the last nonempty above that row, we find `WebId` as `4c7a58c1-01f2-4fa3-a730-44081a44f689`, and `DocId` as `18c3e09c-b5be-48e7-a754-7a2ce53e0999`.

We can also see that the `TargetExpirationDate` is set for April 19, 2023, at 18:08:53 UTC. It means if we trim based on this schedule, we would be setting the expiration date for this version to that time. However, at the time of this documentation is written, it passed April 19, 2023. Instead of setting the version to expire, the document is deleted immediately.

> [!NOTE]
> All date times are represented in the round-trip format. For more information, see [Standard date and time format strings - .NET | Microsoft Learn](/dotnet/standard/base-types/standard-date-and-time-format-strings)

## Analyze Version Storage for Sites

After configuring the `TargetExpirationDate` values for your report, you can choose to perform deeper analysis to see the impact of the trimming before running an actual trim. You can perform this analysis independently, or alternatively, we provide two recommended options for your analysis.  

### Option one: Analyze the report using Excel

Open the shared Excel workbook **AnalyzeReportFile_Template.xlsx**. You can find the following worksheets in it.  

- **Configuration**: Use this worksheet to set the date range for generating the different report views.
- **Dataset**: This worksheet is the raw dataset imported from the report file. Various reporting summary views are constructed from this dataset.
- **Preset Reports**: Here's a list of preset views that can be used to understand the impact of applying the selected setting on versions stored in the site:
    - **Summary**: Analyze the current state of version storage for this site and deleted version distribution under the new settings.
    - **Impacted Users**: Review the users whose versions would be impacted under the new settings.
    - **Version Count**: A table and graph showing the numbers of versions that will be available over time under the current schedule and the number of versions that will be available under the new schedule.
    - **Size of Versions Expired**: Compare the size of versions that will be deleted over time under the current schedule and the number of versions that will be available under the new schedule.
    - **File Level Analysis**: Review file level version deletions under the new settings.  

Populate the workbook by following these steps:

1. On the **Configuration** worksheet, enter the full path to the What-If report file in **Cell B3**.

:::image type="content" source="media/version-history/analyze-version-step1.png" lightbox="media/version-history/analyze-version-step1.png" alt-text="configuration worksheet":::

2. If you want to change the date range of graphs in **Number of Versions Available** worksheet, or **Size of Versions Expired** worksheet, change the corresponding values in Cells B6, B7, B10, and/or B11. It's optional.  

:::image type="content" source="media/version-history/analyze-version-step2.png" lightbox="media/version-history/analyze-version-step2.png" alt-text="analyze version configuration":::

3. At the top of Excel, select **Data** tab, and in the Ribbon, select **Refresh All** button.

:::image type="content" source="media/version-history/analyze-version-step3.png" lightbox="media/version-history/analyze-version-step3.png" alt-text="analyze version data tab":::

4. On the **Calculations** worksheet, autofill the **Number of Versions** and **Number of Versions Remaining After Deletion** columns.

:::image type="content" source="media/version-history/analyze-version-step4-a.png" lightbox="media/version-history/analyze-version-step4-a.png" alt-text="Calculations worksheet 1":::

:::image type="content" source="media/version-history/analyze-version-step4-b.png" lightbox="media/version-history/analyze-version-step4-b.png" alt-text="Calculations worksheet 2":::

5. On the **Impacted Users** worksheet, autofill the **Number of Versions Will be Deleted** column.

:::image type="content" source="media/version-history/analyze-version-step5.png" lightbox="media/version-history/analyze-version-step5.png" alt-text="Impacted Users worksheet":::

All worksheets should now be up to date. You can check the information you're interested in.

### Option two: Analyze the report using PowerShell

1. Save the script as a file named **AnalyzeReportFile.ps1.**

```PowerShell

Param(
     [Parameter(Mandatory=$true)][string] $ReportLocalFilePath,
     [Parameter(Mandatory=$false)][int]$ShowFilesWithFewerThanNVersions=10,
     [Parameter(Mandatory=$false)][DateTime]$TimelineStartDate=[DateTime]::Now,
     [Parameter(Mandatory=$false)][int]$TimelineStepDays=10,
     [Parameter(Mandatory=$false)][int]$TimelineNumSteps=10
)
function Import-Dataset($DatasetFilePath)
{
     $Dataset = Import-CSV $DatasetFilePath
     $Columns = $Dataset `
     | Get-Member -MemberType 'NoteProperty' `
     | Select-Object -ExpandProperty Name
     $CompactColumns = $Columns | Where-Object { $_ -Match ".Compact" } 
     $Timer = [Diagnostics.Stopwatch]::StartNew()
     for ($RowIndex = 0; $RowIndex -lt $Dataset.Count; $RowIndex++)
     {
         if ($RowIndex -gt 0)
         { $PrevRow = $Dataset[$RowIndex-1]
         }
         $Row = $Dataset[$RowIndex]
         foreach ($ColName in $Columns)
         {
             if ([string]::IsNullOrEmpty($Row.$ColName))
             {
             if (($ColName -in $CompactColumns) -and ($RowIndex -gt 0))
             { $Row.$ColName = $PrevRow.$ColName
             }
             else
             { $Row.$ColName = $null
             }
      }
     }
     $Row."WebId.Compact" = [Guid]$Row."WebId.Compact"
     $Row."DocId.Compact" = [Guid]$Row."DocId.Compact"
     $Row."MajorVersion" = [Int32]$Row."MajorVersion"
     $Row."MinorVersion" = [Int32]$Row."MinorVersion"
     $Row."WebUrl.Compact" = [String]$Row."WebUrl.Compact"
     $Row."FileUrl.Compact" = [String]$Row."FileUrl.Compact"
     $Row."Size" = [Int64]$Row."Size"
     $Row."ModifiedBy_UserId.Compact" = [Int32]$Row."ModifiedBy_UserId.Compact"
     $Row."ModifiedBy_DisplayName.Compact" = [String]$Row."ModifiedBy_DisplayName.Compact"
     $Row."LastModifiedDate" = [DateTime]$Row."LastModifiedDate"
     $Row."SnapshotDate" = [DateTime]$Row."SnapshotDate"
     $Row."IsSnapshotDateEstimated" = [bool]$Row."IsSnapshotDateEstimated"
     $Row."CurrentExpirationDate" = [System.Nullable[DateTime]]$Row."CurrentExpirationDate"
     $Row."AutomaticPolicyExpirationDate" = [System.Nullable[DateTime]]$Row."AutomaticPolicyExpirationDate"
     $Row."TargetExpirationDate" = [System.Nullable[DateTime]]$Row."TargetExpirationDate"
 
$Percent = [Math]::Ceiling(100 * $RowIndex / $Dataset.Count)
 Write-Progress `
     -Activity "Reading dataset" `
     -Status "$Percent% Complete ($($RowIndex + 1) / $($Dataset.Count) rows):" `
     -PercentComplete $Percent `
     -SecondsRemaining $(($Dataset.Count - ($RowIndex + 1)) / (($RowIndex + 1) / $Timer.Elapsed.Totalseconds))
  }
  $Timer.Stop()
  return $Dataset
}
function Get-NumVersionExpiresByDate($Dataset, $ColName, $DateCutoff)
{
     $VersionsExpired = $Dataset | Where-Object { ($null -ne $_.$ColName) -and ($_.$ColName -le $DateCutoff) }
     $IsTodayStr = ""
     If ((Get-Date).Date -eq ($DateCutoff).Date) 
     {
         $IsTodayStr = "*"
     }
     return [PSCustomObject]@{
         Today = $IsTodayStr
         Date = $DateCutoff
         NumberOfVersionsAvailable = $Dataset.Count - $VersionsExpired.Count
         NumberOfVersionsExpired = $VersionsExpired.Count
         SizeOfVersionsExpiredInBytes = ($VersionsExpired | Measure-Object Size -Sum).Sum
         }
}
function Get-FilesWithFewerThanNVersions($Dataset, $NumVersions)
{
 $AvailableVersionsByFile = $Dataset `
```

2. Open PowerShell 7 and run the following command, replacing the placeholder values with the appropriate values.  

```PowerShell
Using AnalyzeReportFile.ps1
. “<path to AnalyzeReportFile.ps1>” –ReportLocalFilePath “<path to the file 
version expiration What-If report .csv file>”
```

:::image type="content" source="media/version-history/analyze-report-powershell-command.png" lightbox="media/version-history/analyze-report-powershell-command.png" alt-text="analyze report powershell command":::

3. The output displays four tables:

- **Current Expiration Schedule:** this table contains a time-series summary for your versions as they are. It has the following columns:
    1. **Date**: the first column represents the date.
    1. **NumberOfVersionsAvailable**: the number of versions available on that date under the current schedule.  
    1. **NumberOfVersionsExpired**: the number of versions expired on that date under the current schedule.  
    1. **SizeOfVersionsExpiredMB**: the size of versions expired on that date under the current schedule.  

:::image type="content" source="media/version-history/current-expiration-schedule.png" lightbox="media/version-history/current-expiration-schedule.png" alt-text="Current Expiration Schedule":::

- **Target Expiration Schedule:** this table is the same as Current Expiration Schedule but reflects the updated schedule instead. This table is only helpful if you want to test out different expiration scenarios by changing the **TargetExpirationDate** column in the file version expiration report.  

:::image type="content" source="media/version-history/target-expiration-schedule.png" lightbox="media/version-history/target-expiration-schedule.png" alt-text="Target Expiration Schedule":::

- **Files with Fewer Than 10 Versions:** a list of the URLs, and the number of versions before and after the deletion for those files whose number of versions is fewer than 10 after immediate deletion (but was more than 10 before the immediate deletion).  

:::image type="content" source="media/version-history/files-with-fewer-than-10-versions.png" lightbox="media/version-history/files-with-fewer-than-10-versions.png" alt-text="Files with Fewer Than 10 Versions":::

- **Users Impacted:** the users whose versions would be immediately deleted.

:::image type="content" source="media/version-history/users-impacted.png" lightbox="media/version-history/users-impacted.png" alt-text="Users Impacted":::

Optionally, you can adjust the parameters:

- `TimelineStartDate`: the starting date for Table 1 and 2 above.
- `TimelineStepDays`: the number of days in between rows for Table 1 and 2 above.  
- `TimelineNumSteps`: the number of rows to calculate for Table 1 and 2 above.  
- `ShowFilesWithFewerThanNVersions`: the threshold for the number of versions in Table 3 above.

