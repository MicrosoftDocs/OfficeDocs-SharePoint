---
ms.date: 12/02/2021
title: "Step 2: Migrate SharePoint Server workflows with SPMT"
ms.reviewer:
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid:
description: Overview Migrate your SharePoint Server workflows to Microsoft 365 using the SharePoint Migration Tool (SPMT)"
---
# Step 2 Migrate workflows to Power Automate

> [!NOTE]
> This feature is currently in public preview, and subject to change.

After configuring the required endpoints and configuring Power Automate, you're ready to start migrating your SharePoint Server workflows. You choose to either use SPMT or PowerShell.

>[!Note]
>SPMT will skip a workflow if it has already been successfully migrated. If you want to run a new migration to override the migrated flow, delete it from the destination before starting the migration.

## Migrate workflows using SPMT

1. Start SPMT, and then enter your Microsoft 365 username and password.
2. Select **Start your first migration**.
3. Select **SharePoint Server**.
4. Select the **Workflow migration** type.
</br>

   ![Select workflow migration](media/spmt-workflow-select.png)

5. Enter the SharePoint Server site URL where your content is located. 
6. Enter your username and password to the SharePoint Server site; it can be UserID or user email. Select **Sign in**.
7. Select which workflows to include in the migration. If you select the option for a specific list, you'll be prompted for the list name.

   ![spmt workflow source](media/spmt-workflow-select-source.png)

8. Enter your destination; the SharePoint site and list where you want to migrate your workflow.  Select the workflow environment. If the site or the list doesn't currently exist, they'll be created for you. Select **Next**.

   ![Select your destination and environment](media/spmt-workflow-select-environment.png)

9. This task is added to the list of migration tasks.  If you want to select another set of data files to migrate, select **Add a source**.  Otherwise, select **Next** to go to the next step.
10. On the settings page, turn on **Only perform scanning** to run workflow scanning.
11. In the **Power Automate flow owner** box, enter the email address of the new flow owner.

    ![Set your workflow settings](media/spmt-workflow-settings.png)

12. Select **View all settings**, and choose your option under **Handle Unsupported Action**. If you select **Stop workflow migration and report error**, SPMT will report an error on a workflow if it contains unsupported actions. Otherwise the unsupported actions are converted to Compose actions during migration. 
13. Select **Scan** to start scanning if “Only perform scanning” is selected; or select **Migrate** to start migration. 


## Migrate workflows using PowerShell

Alternatively, you can migrate your workflows to Power Automate using PowerShell.  
Before you proceed, make sure you've completed the steps in this article: [Step 1 - Configure endpoints and Power Automate](spmt-workflow-step1.md).

### Scan workflows

This command scans workflows of a given site or list and generates a scan report. 

```powershell

Register-SPMTMigration -ScanOnly $true -SPOCredential $targetCredential -UserMappingFile $userMappingFile -MigrationType WORKFLOW -DefaultFlowOwnerEmail  $defaultOwnerName -Force
...
Start-SPMTMigration

```

### Migrate workflows

This command:

- Migrates workflow of a site or list
- Generates a migration package
- Imports the package to Power Automate and 
- Generates a migration report. 

**MigrationType**

When MigrationType is WORKFLOW, if the structure hasn't been migrated yet, the command does migrate site or list structure (not content), then migrate its workflows.

**DefaultFlowOwnerEmail**

Default flow owner is required for OOTB Approval workflow because there isn’t an owner in workflow definition. After migration, only flow owner and Power Automate admin can access the migrated flows. If the given owner email isn't a valid user at destination, migration will fail. The flow owner also needs to have permission to access the destination SPO list.

```powershell

> Register-SPMTMigration -SPOCredential $targetCredential -UserMappingFile $userMappingFile -MigrationType WORKFLOW -DefaultFlowOwnerEmail $defaultOwnerName -Force
...
Start-SPMTMigration

```


### Sample PowerShell script

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

## Migrations report and error codes

The migration task generates a report titled *WorkflowMigrationReport.csv* for migrations, and another *WorkflowScanReport.csv* for scans. The reports are located in the *WF_xxx/Report/TaskReport_xxx/* folder.

>[!Note]
>[Learn more about the workflow reports and error codes](spmt-workflow-report-and-error-codes.md)

## Step 3:  [Activate workflows](spmt-workflow-step3.md)

