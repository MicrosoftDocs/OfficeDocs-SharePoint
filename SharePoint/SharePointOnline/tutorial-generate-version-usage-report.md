---
title: "Tutorial: Generate and analyze version usage report"
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
description: "This article provides guidance on how to generate and analyze version usage report for SharePoint Site."

---

# Tutorial: Generate and analyze version usage report for SharePoint site

By understanding version storage on a site, you can better optimize the Version history settings to meet your organization’s recovery objectives and manage storage costs.

This tutorial shows how you can generate a version storage usage report and analyze it to better understand the version storage footprint of the site. The report can also be used to [run ‘what-if’ analysis](tutorial-run-what-if-analysis.md) of applying different version limits or trimming existing versions.  

In this tutorial we cover how to:

- Generate version storage usage report file for site or library.
- Check progress of report generation.
- Understand the report file.
- Analyze version storage use using Excel or PowerShell.

In later tutorials, review how you can run impact analysis on the generated CSV report.

## Before you begin

1.	Identify the SharePoint site, OneDrive account, or document library whose version storage usage you want to understand. 
2. Choose a location within the SharePoint document library that you want to save the report to. 
1. [Download the latest SharePoint Online Management Shell](https://www.microsoft.com/en-us/download/details.aspx?id=35588).

> [!NOTE]
> 1. The report file is generated within the report location specified. 
> 2. The report location must be within a SharePoint document library itself. 
> 3. There cannot be a file with the same name as the report in the document library.  


## Generate version usage report for sites or library

You can generate a report on the current version storage use on a site by running the `New-SPOSiteFileVersionExpirationReportJob` command or on a library by running the `New-SPOListFileVersionBatchDeleteJob` command.

In the following example, a job is queued to generate a site-scoped report at the report location, `https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv`.  

```PowerShell
New-SPOSiteFileVersionExpirationReportJob -Identity https://contoso.sharepoint.com/sites/site1 -ReportUrl "https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv"  
```
In the following example, a job is queued to generate a library-scoped report at the report location, `https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv`.  

```PowerShell
New-SPOListFileVersionExpirationReportJob -Site https://contoso.sharepoint.com/sites/site1 -List "Documents" -ReportUrl "https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv"
```   

## Check progress on the report generation 

Use the `Get-SPOListFileVersionExpirationReportJobProgress` command to track the progress of report generation request.  

The example below shows how you can check if your **site scoped report** is fully populated and ready to be analyzed.  

```PowerShell
Get-SPOSiteFileVersionExpirationReportJobProgress -Identity https://contoso.sharepoint.com/sites/site1 -ReportUrl "https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv"
```

The example below shows how you can check if your **library scoped report** is fully populated and ready to be analyzed.
  

```PowerShell
Get-SPOListFileVersionExpirationReportJobProgress -Site https://contoso.sharepoint.com/sites/site1 -List "Documents" -ReportUrl "https://contoso.sharepoint.com/sites/sites1/reports/MyReports/VersionReport.csv"    
```

The cmdlet will return a response in JSON format. The returned json response has a key named status. Refer to the table below for one of the following expected values:  

| JSON Status Response | Explanation |
| --- | --- |
| “completed” | The job has successfully completed and the report is fully populated. |
| “in_progress” | There is an active job. The report is partially populated. |
| “no_report_found” | There are no active jobs populating the specified file. |
| “failed” | The job to generate the report has failed due to the error message. Check “error_message” for the error message from the failure. |

## Understand version report file

The generated report is in CSV format with each row corresponds to a file version.
Here’s an example of file version expiration report and its column breakdown.  

:::image type="content" source="media/version-history/expiration-report.png" lightbox="media/version-history/expiration-report.png" alt-text="Screenshot of expiration report.":::

The first row is the header with the column identifiers containing File Version Identifiers, Version Metadata information, and expiration timestamp. Compact columns are denoted with `.Compact` post-fix that won’t repeat values if two consecutive rows have the same value. The other rows represent file versions, where each row represents a single version.  
Let’s go through the first file version displayed in this report.  

- File version identifiers: `WebId`, `DocId`, `MajorVersion`, and `MinorVersion` uniquely identify each version in your SharePoint site.  

- Version metadata identifiers:`WebUrl` indicates the version in `https://contoso.sharepoint.com`, and `FileUrl` indicates that the file for this version is located at     DocLib/MyDocument.docx. In other words, it is in a Document Library called `DocLib`, while the file is in the root folder of `DocLib` and is named MyDocument.docx.  

- `Size` indicates that the version takes 92,246 bytes of storage.  

- The next two columns, `ModifiedBy_UserId` and `ModifiedBy_DisplayName` indicate that the user Michelle Harris (with user ID 6) has created this version.  

- `LastModifiedDate` indicates that the version’s content was last modified on March 13, 2023, at 22:36:09 UTC. `SnapshotDate` displays that the version became a historical version on March 20, 2023, at 16:56:51 UTC. `IsSnapshotDateEstimated` shows that `SnapshotDate` is the actual snapshot date.  

- Expiration schedule identifiers:`CurrentExpirationDate` indicates that this version is currently set to never expire. `AutomaticPolicyExpirationDate` shows that under the automatically expire policy, this version is also set to never expire. `TargetExpirationDate` indicates that if we follow this schedule for trimming, we would set this version to never expire.  

Let’s look at the third version.  

The `WebId` and `DocId` values are empty because these columns are compact columns, denoted by *.Compact* post-fix, it means they should have values. If we look for the last nonempty above that row, we find `WebId` as `4c7a58c1-01f2-4fa3-a730-44081a44f689`, and `DocId` as `18c3e09c-b5be-48e7-a754-7a2ce53e0999`.

We can also see that the `TargetExpirationDate` is set for April 19, 2023, at 18:08:53 UTC. It means if we trim based on this schedule, we would be setting the expiration date for this version to that time. However, at the time this documentation was written, it passed April 19, 2023. Instead of setting the version to expire, the document is deleted immediately.

> [!NOTE]
> All date times are represented in the round-trip format. For more information, see [Standard date and time format strings - .NET | Microsoft Learn](/dotnet/standard/base-types/standard-date-and-time-format-strings)

## Analyze version storage for sites

After configuring the `TargetExpirationDate` values for your report, you can choose to perform deeper analysis to see the impact of the trimming before running an actual trim. You can perform this analysis independently, or alternatively, we provide two recommended options for your analysis.  

### Option one: Analyze the report using Excel

Open the shared Excel workbook [AnalyzeReportFile_Template.xlsx](https://download.microsoft.com/download/b/f/e/bfed7844-b840-4854-8897-1272e914ccdd/AnalyzeReportFile_Template.xlsx). You can find the following worksheets in it.  

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

:::image type="content" source="media/version-history/analyze-version-step1.png" lightbox="media/version-history/analyze-version-step1.png" alt-text="Screenshot of configuration worksheet.":::

2. If you want to change the date range of graphs in **Number of Versions Available** worksheet, or **Size of Versions Expired** worksheet, change the corresponding values in Cells B6, B7, B10, and/or B11. It's optional.  

:::image type="content" source="media/version-history/analyze-version-step2.png" lightbox="media/version-history/analyze-version-step2.png" alt-text="Screenshot of analyze version configuration.":::

3. At the top of Excel, select the **Data** tab, and in the Ribbon, select the **Refresh All** button.

:::image type="content" source="media/version-history/analyze-version-step3.png" lightbox="media/version-history/analyze-version-step3.png" alt-text="Screenshot of analyze version data tab.":::

4. On the **Calculations** worksheet, autofill the **Number of Versions** and **Number of Versions Remaining After Deletion** columns.

:::image type="content" source="media/version-history/analyze-version-step4-a.png" lightbox="media/version-history/analyze-version-step4-a.png" alt-text="Screenshot of calculations worksheet 1.":::

:::image type="content" source="media/version-history/analyze-version-step4-b.png" lightbox="media/version-history/analyze-version-step4-b.png" alt-text="Screenshot of calculations worksheet 2.":::

5. On the **Impacted Users** worksheet, autofill the **Number of Versions Will be Deleted** column.

:::image type="content" source="media/version-history/analyze-version-step5.png" lightbox="media/version-history/analyze-version-step5.png" alt-text="Screenshot of impacted users worksheet.":::

All worksheets should now be up to date. You can check the information you're interested in.

### Option two: Analyze the report using PowerShell

1. Save the script as a file named **AnalyzeReportFile.ps1.**

```PowerShell
# save this file as AnalyzeReportFile.ps1

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
    {
      $PrevRow = $Dataset[$RowIndex-1]
    }
    $Row = $Dataset[$RowIndex]
   
    foreach ($ColName in $Columns)
    {
      if ([string]::IsNullOrEmpty($Row.$ColName))
      {
        if (($ColName -in $CompactColumns) -and ($RowIndex -gt 0))
        {
          $Row.$ColName = $PrevRow.$ColName
        }
        else
        {
          $Row.$ColName = $null
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
    $Row."ModifiedBy_UserId.Compact" = [String]$Row."ModifiedBy_UserId.Compact"
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
    Today              = $IsTodayStr
    Date              = $DateCutoff
    NumberOfVersionsAvailable    = $Dataset.Count - $VersionsExpired.Count
    NumberOfVersionsExpired     = $VersionsExpired.Count
    SizeOfVersionsExpiredInBytes  = ($VersionsExpired | Measure-Object Size -Sum).Sum
  }
}
function Get-FilesWithFewerThanNVersions($Dataset, $NumVersions)
{
  $AvailableVersionsByFile = $Dataset `
    | Where-Object { ($null -eq $_.TargetExpirationDate) -or ($_.TargetExpirationDate -gt [DateTime]::Now) } `
    | Group-Object -Property WebId.Compact, DocId.Compact
  $AvailableFilesWithNotEnoughVersions = @{}
  # Files with some versions left but not enough
  $AvailableVersionsByFile `
    | Where-Object Count -lt $NumVersions `
    | ForEach-Object { $AvailableFilesWithNotEnoughVersions[$_.Name] = $_.Count }
  # Files with 0 versions left
  $Dataset `
    | Group-Object -Property WebId.Compact, DocId.Compact `
    | Where-Object { $AvailableVersionsByFile.Name -notcontains $_.Name } `
    | ForEach-Object { $AvailableFilesWithNotEnoughVersions[$_.Name] = 0 }
  # Stitch all of the data together
  return $Dataset `
    | Group-Object -Property WebId.Compact, DocId.Compact `
    | Where-Object Count -ge $NumVersions `
    | Where-Object { $AvailableFilesWithNotEnoughVersions.Contains($_.Name) } `
    | ForEach-Object `
      {
        $fileUrl = $_.Group[0]."WebUrl.Compact" + "/" + $_.Group[0]."FileUrl.Compact"
        $numberOfVersionsAvailableBeforeTrim = $_.Count
        $numberOfVersionsAvailableAfterTrim = $AvailableFilesWithNotEnoughVersions[$_.Name]
        $numberOfVersionsTrimmed = $numberOfVersionsAvailableBeforeTrim - $numberOfVersionsAvailableAfterTrim
        [PSObject]::new() | 
          Add-Member -PassThru -NotePropertyMembers ([Ordered]@{
            FileUrl = $fileUrl
            NumberOfVersionsAvailableBeforeTrim = $numberOfVersionsAvailableBeforeTrim
            NumberOfVersionsAvailableAfterTrim = $numberOfVersionsAvailableAfterTrim
            NumberOfVersionsTrimmed = $numberOfVersionsTrimmed
          })
      } `
    | Sort-Object -Property NumberOfVersionsAvailableAfterTrim
}
function Get-MostImpactedUsers($Dataset)
{
  $VersionsExpired = $Dataset | Where-Object { ($null -ne $_.TargetExpirationDate) -and ($_.TargetExpirationDate -le [DateTime]::Now) }
  return $VersionsExpired `
    | Group-Object -Property ModifiedBy_UserId.Compact `
    | Select-Object `
      @{ L = "UserId"; E = { $_.Group[0]."ModifiedBy_UserId.Compact" } }, `
      @{ L = "UserDisplayName"; E = { $_.Group[0]."ModifiedBy_DisplayName.Compact" } },
      @{ L = "NumberOfVersionsTrimmed"; E = { $_.Count } } `
    | Sort-Object -Property NumberOfVersionsTrimmed -Descending
}
$Dataset = Import-Dataset -DatasetFilePath $ReportLocalFilePath
$CurrentExpirationSummaryTable = @()
$TargetExpirationSummaryTable = @()
$Timer = [Diagnostics.Stopwatch]::StartNew()
for ($Step = 0; $Step -lt $TimelineNumSteps; $Step++)
{
  $DateCutOff = $TimelineStartDate.AddDays($TimelineStepDays * $Step)
  $CurrentExpirationSummaryTable += `
    Get-NumVersionExpiresByDate -Dataset $Dataset -ColName CurrentExpirationDate -DateCutoff $DateCutOff
  $TargetExpirationSummaryTable += `
    Get-NumVersionExpiresByDate -Dataset $Dataset -ColName TargetExpirationDate -DateCutoff $DateCutOff
}
$Timer.Stop()
Write-Host "===========================" -ForegroundColor Yellow
Write-Host "Current Expiration Schedule" -ForegroundColor Yellow
Write-Host "===========================" -ForegroundColor Yellow
$CurrentExpirationSummaryTable | Format-Table -Autosize | Out-String | Write-Host
Write-Host "Total elapsed seconds: $($Timer.Elapsed.TotalSeconds / 2)" -ForegroundColor Green
Write-Host
Write-Host "==========================" -ForegroundColor Yellow
Write-Host "Target Expiration Schedule" -ForegroundColor Yellow
Write-Host "==========================" -ForegroundColor Yellow
$TargetExpirationSummaryTable | Format-Table -Autosize | Out-String | Write-Host
Write-Host "Total elapsed seconds: $($Timer.Elapsed.TotalSeconds / 2)" -ForegroundColor Green
Write-Host
Write-Host "================================" -ForegroundColor Yellow
Write-Host "Files with Fewer Than $ShowFilesWithFewerThanNVersions Versions" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Yellow
$Timer = [Diagnostics.Stopwatch]::StartNew()
Get-FilesWithFewerThanNVersions -Dataset $Dataset -NumVersions $ShowFilesWithFewerThanNVersions | Format-Table -Autosize | Out-String | Write-Host
$Timer.Stop()
Write-Host "Total elapsed seconds: $($Timer.Elapsed.TotalSeconds)" -ForegroundColor Green
Write-Host
Write-Host "==============" -ForegroundColor Yellow
Write-Host "Users Impacted" -ForegroundColor Yellow
Write-Host "==============" -ForegroundColor Yellow
$Timer = [Diagnostics.Stopwatch]::StartNew()
Get-MostImpactedUsers -Dataset $Dataset | Format-Table -Autosize | Out-String | Write-Host
$Timer.Stop()
Write-Host "Total elapsed seconds: $($Timer.Elapsed.TotalSeconds)" -ForegroundColor Green
Write-Host
```

2. Open PowerShell and run the following command, replacing the placeholder values with the appropriate values.  

> [!NOTE]
> Use PowerShell 7 to run the commands. You can install PowerShell 7 by following these instructions: [Installing PowerShell on Windows - PowerShell | Microsoft Learn](/powershell/scripting/install/installing-powershell-on-windows).

```PowerShell
. “<path to AnalyzeReportFile.ps1>” –ReportLocalFilePath “<path to the file version expiration What-If report .csv file>”
```

:::image type="content" source="media/version-history/analyze-report-powershell-command.png" lightbox="media/version-history/analyze-report-powershell-command.png" alt-text="Screenshot of analyze report powershell command.":::

3. The output displays four tables:

- **Current Expiration Schedule:** this table contains a time-series summary for your versions as they are. It has the following columns:
    1. **Date**: the first column represents the date.
    1. **NumberOfVersionsAvailable**: the number of versions available on that date under the current schedule.  
    1. **NumberOfVersionsExpired**: the number of versions expired on that date under the current schedule.  
    1. **SizeOfVersionsExpiredMB**: the size of versions expired on that date under the current schedule.  

:::image type="content" source="media/version-history/current-expiration-schedule.png" lightbox="media/version-history/current-expiration-schedule.png" alt-text="Screenshot of Current Expiration Schedule.":::

- **Target Expiration Schedule:** this table is the same as Current Expiration Schedule but reflects the updated schedule instead. This table is only helpful if you want to test out different expiration scenarios by changing the **TargetExpirationDate** column in the file version expiration report.  

:::image type="content" source="media/version-history/target-expiration-schedule.png" lightbox="media/version-history/target-expiration-schedule.png" alt-text="Screenshot of Target Expiration Schedule.":::

- **Files with Fewer Than 10 Versions:** a list of the URLs, and the number of versions before and after the deletion for those files whose number of versions is fewer than 10 after immediate deletion (but was more than 10 before the immediate deletion).  

:::image type="content" source="media/version-history/files-with-fewer-than-10-versions.png" lightbox="media/version-history/files-with-fewer-than-10-versions.png" alt-text="Screenshot of files with fewer than 10 Versions.":::

- **Users Impacted:** the users whose versions would be immediately deleted.

:::image type="content" source="media/version-history/users-impacted.png" lightbox="media/version-history/users-impacted.png" alt-text="Screenshot of Users Impacted.":::

Optionally, you can adjust the parameters:

- `TimelineStartDate`: the starting date for Table 1 and 2 above.
- `TimelineStepDays`: the number of days in between rows for Table 1 and 2 above.  
- `TimelineNumSteps`: the number of rows to calculate for Table 1 and 2 above.  
- `ShowFilesWithFewerThanNVersions`: the threshold for the number of versions in Table 3 above.

