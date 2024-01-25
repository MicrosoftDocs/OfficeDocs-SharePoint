---
ms.date: 02/22/2022
title: "Migrate SharePoint workflows to Power Automate using PowerShell"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
ms.assetid: 
description: "Learn how to migrate SharePoint workflows to Power Automate using PowerShell cmdlets."
---


# Migrate SharePoint Server workflows to Power Automate using PowerShell

Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. 

You can now migrate:

- **SharePoint Server 2010** out of the box (OOTB) approval and collect feedback workflows to PowerAutomate.
- List and library "out-of-box" (OOTB) approval workflows
- Workflow definitions and associations

>[!Note]
> Workflows created with SharePoint Designer or SharePoint Server 2013 are currently not supported.

>[!Note]
>To migrate workflows using SPMT, see [Migrate SharePoint Server 2010 workflows to Power Automate using SPMT](spmt-workflow-overview.md)

## Before you begin

Before you begin your workflow migration, you must first:

- Configure the required endpoints. 
- Configure Power Automate. If you have never used Power Automate with this tenant before, you must configure it before you begin migration. We recommend using Edge or Internet Explorer.

For the detailed steps see:
- [**Step 1 - Configure endpoints and Power Automate**](spmt-workflow-step1.md).

## Scan workflows

This command scans workflows of a given site or list and generates a scan report. 

```powershell

Register-SPMTMigration -ScanOnly $true -SPOCredential $targetCredential -UserMappingFile $userMappingFile -MigrationType WORKFLOW -DefaultFlowOwnerEmail  $defaultOwnerName -Force
...
Start-SPMTMigration

```

## Migrate workflows

This command does the following:

-  Migrates workflow of a site or list
-  Generates a migration package
-  Imports the package to Power Automate and 
-  Generates a migration report. 

**MigrationType**

When MigrationType is WORKFLOW, if the structure hasn't been migrated yet, the command does migrate site or list structure (not content), then migrate its workflows.

**DefaultFlowOwnerEmail**

Default flow owner is required for OOTB Approval workflow because there isn’t an owner in workflow definition. After migration, only flow owner and Power Automate admin can access the migrated flows. If the given owner email isn't a valid user at destination, migration will fail. The flow owner also needs to have permission to access the destination SPO list.

```powershell

> Register-SPMTMigration -SPOCredential $targetCredential -UserMappingFile $userMappingFile -MigrationType WORKFLOW -DefaultFlowOwnerEmail $defaultOwnerName -Force
...
Start-SPMTMigration

```


## Sample PowerShell script

```powershell

Import-Module "$((Resolve-Path .\).Path)\Microsoft.SharePoint.MigrationTool.PowerShell.dll"

clear
Remove-Variable * -ErrorAction SilentlyContinue

$currentFolder = (Resolve-Path .\).Path
$userMappingFile = "$($currentFolder)\Sample-UserMap.csv"
$defaultOwnerName = "please enter flow owner email here"

$targetSite = "please enter destination site URL here"
$targetUserName = "please enter destination site admin user email here"
$targetPassWord = ConvertTo-SecureString -String "please enter destination user password here" -AsPlainText -Force 
$targetCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $targetUserName, $targetPassWord

Register-SPMTMigration -SPOCredential $targetCredential -UserMappingFile $userMappingFile -IgnoreUpdate -MigrationType WORKFLOW -DefaultFlowOwnerEmail $defaultOwnerName -Force

$sourceSite = "please enter source site URL here"
$sourceUsername = "please enter source site admin username here"
$sourcePassword = ConvertTo-SecureString -String "please enter destination user password here" -AsPlainText -Force
$sourceCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $sourceUsername, $sourcePassword
Add-SPMTTask -SharePointSourceCredential $sourcecredential -SharePointSourceSiteUrl $sourceSite -TargetSiteUrl $targetSite `
#-SourceList "please enter source list name here" -TargetList "please enter destination list name here"

Write-Host "Start migration"
$StartTime = [DateTime]::UtcNow

# Let the migration run in background using NoShow mode
Start-SPMTMigration

$migration = Get-SPMTMigration

# open report folder
start $migration.ReportFolderPath

```

