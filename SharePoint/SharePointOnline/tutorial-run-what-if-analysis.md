---
title: "Tutorial: Run 'What-If' analysis (Preview)"
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
description: "This article provides guidance on how to run 'What-If' analysis on Version storage report file."

---

# Tutorial: Run 'What-If' Analysis on Version storage report file (Preview)

In this tutorial, we discuss how to leverage provided scripts and excel examples to understand the impact of applying either Automatic or Manual limits on version storage or impacted users. You will learn how to: :

- Run impact analysis of setting Automatic limits.
- Run impact analysis of expiring versions older than specified days.
- Run impact analysis of storing version within specified count limits.

## Before you begin

In the previous tutorial, you had generated a version storage usage report. This tutorial assumes that the report generation job has successfully completed and the report is fully populated.<br>
Start by downloading the report file to your local computer. Use the scripts provided below to apply the desired setting on the file.


## Run impact analysis of setting Automatic Version history limits

Here's an example of PowerShell script you could apply to generate a What-If Report file that applies the **Automatic Expiration**  policy on the report file `C:\Report.csv`.  

```PowerShell
ScheduleUpdate_Auto.ps1 
    param (
     [Parameter(Mandatory=$true)][string] $ImportPath, 
     [Parameter(Mandatory=$true)][string] $ExportPath
    )

    $Schedule = Import-Csv -Path $ImportPath
    $Schedule |
      ForEach-Object {
        $_.TargetExpiration Date = $_.AutomaticPolicy Expiration Date
      }
    $Schedule |
     Export-Csv -Path $ExportPath -UseQuotes AsNeeded
```

:::image type="content" source="media/version-history/expiration-automation.png" lightbox="media/version-history/expiration-automation.png" alt-text="expiration automation":::

## Run impact analysis of setting Manual Expiration limits

Here's an example of PowerShell script to generate a What-If Report file. It applies **Manual Expiration** with expire-after days set to **30** on the report file `C:\Report.csv`.  

```PowerShell
ScheduleUpdate_ExpireAfter.ps1
        param (
         [Parameter(Mandatory=$false)][string]$ImportPath,
         [Parameter(Mandatory=$false)][string]$ExportPath,
         [Parameter(Mandatory=$false)][string]$ExpireAfter
        )
function StringToDateTime($Value) { return [string]::IsNullOrEmpty($Value) ? $null : 
[DateTime]::ParseExact($Value, "yyyy-MM-ddTHH:mm:ssK", $null) }
function DateTimeToString( $Value) { return $null -eq $Value ? "" : $Value.ToString("yyyyMM-ddTHH:mm:ssK") } 
$Schedule = Import-Csv -Path $ImportPath 
$Schedule | 
 ForEach-Object { 
  $SnapshotDate = StringToDateTime -Value $_.SnapshotDate
  $TargetExpirationDate = $SnapshotDate.AddDays($ExpireAfter)
  $_.TargetExpirationDate = DateTimeToString -Value $TargetExpirationDate
 } 
$Schedule | 
  Export-Csv -Path $ExportPath -UseQuotes AsNeeded
```

:::image type="content" source="media/version-history/manual-expiration.png" lightbox="media/version-history/manual-expiration.png" alt-text="manual expiration":::

## Run impact analysis of setting Manual Count Limits

Here's an example of PowerShell script to generate a What-If Report file. It applies a **Manual with Count Limits** policy with major version limit set to **50** on the report file `C:\Report.csv`.

```PowerShell
ScheduleUpdate_Count.ps1
 param (
 [Parameter(Mandatory=$true)][string]$ImportPath,
 [Parameter(Mandatory=$true)][string]$ExportPath,
 [Parameter(Mandatory=$true)][string]$MajorVersionLimit
)

class FileIdentifier {
  [string] $WebId
  [string] $DocId
  [string] ToString() {
    return "WebId: $($this.WebId) DocId: $($this.DocId) " 
  }
  [int] GetHashCode()
  {
  return [HashCode]::Combine($this.WebId, $this.DocId)
  }
  [boolean] Equals($other)
  {
  return ($other.WebId -eq $this.WebId) -and 
    ($other.DocId -eq $this.DocId) 
  }
}
$Schedule = Import-Csv -Path $ImportPath 
$FileMajorVersionCountDict = @{}
$PreviousWebId = [Guid]::Empty
$PreviousDocId = [Guid]::Empty
foreach ($Version in $Schedule)
{ 
  $WebId = [string]::IsNullOrEmpty($Version."WebId.Compact") ? $PreviousWebId : 
[Guid]::Parse($Version."WebId.Compact")
  $DocId = [string]::IsNullOrEmpty($Version."DocId.Compact") ? $PreviousDocId : 
[Guid]::Parse($Version."DocId.Compact")
 
  $PreviousWebId = $WebId
  $PreviousDocId = $DocId
 
  if (($PreviousWebId -eq [Guid]::Empty) -or ($WebId -eq [Guid]::Empty) -or 
     ($PreviousDocId -eq [Guid]::Empty) -or ($DocId -eq [Guid]::Empty))
  {
     throw "Compact column error."
  }
 
  # skip minor versions
  if ([int]::Parse($Version.MinorVersion) -ne 0)
  {
     continue
  }
  $Fid = [FileIdentifier] @{ WebId = $WebId; DocId = $DocId; } 
  if (-not $FileMajorVersionCountDict.ContainsKey($Fid))
  {
     $FileMajorVersionCountDict[$Fid] = New-Object System.Collections.Queue
  }
  $FileMajorVersionCountDict[$Fid].Enqueue([int]::Parse($Version.MajorVersion))
  if ($FileMajorVersionCountDict[$Fid].Count - $MajorVersionLimit -gt 1)
```

:::image type="content" source="media/version-history/manual-with-count-limits-b.png" lightbox="media/version-history/manual-with-count-limits-b.png" alt-text="manual with count limits-b":::

