---
title: "Step 2: Migrate SharePoint Server workflows with SPMT"
ms.reviewer:
ms.author: jhendr
author: JoanneHendrickson
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

## Migrations report

The migration task generates a workflow migration report titled *WorkflowMigrationReport.csv* for migrations, and *WorkflowScanReport.csv* for scans.  The reports are located in the *WF_xxx/Report/TaskReport_xxx/* folder.

|Column name|Notes|
|:-----|:-----|
|Source association URL|Source SharePoint object URL that is associated with the workflow. It can be URL of list, library, site |
|Destination association urURLl|Destination SharePoint object URL that is associated with the migrated Power Automate flow. It can be URL of list, library.|
|Source workflow URL|Location of the source workflow.|
|Destination workflow URL|The location where the workflow will be migrated.|
|Source workflow ID|ID of the source workflow|
|Destination flow ID|ID of the destination flow|
|Source workflow name|The name of the source workflow|
|Destination flow name|The name of your destination flow|
|Solution name|The name of Power Automate solution that contains the migrated flows. The flow owner can find migrated flows in the solution. |
|Source workflow owner|The creator of source workflow instance|
|Destination flow owner|The owner(s) of migrated Power Automate flow|
|Association type|Possible values: List, Site, or Content type|
|Workflow version|Possible values: Workflow2010, Workflow2013|
|Workflow template name|Workflow template name|
|Workflow accessed date|Latest execution/modification date of the workflow|
|Total action count|The count of actions for SPD workflow|
|Unsupported actions|List of actions that aren't supported by migration tool|
|Status|Possible values: Migrated, Failed, or Skipped, Scan Finished.|
|Result category|Possible values: Migrated, Scan Finished, SCAN FILTER, MIGRATION SKIP, SCAN FAILURE, FLOW CREATE FAILURE|
|Message|Error message|
|Error code||


## Migration errors

If a scan or migration fails, you'll receive a "Scan Failure", or "Flow create failure" error.

|Error message|Error code|Recommended action|
|:-----|:-----	|:-----|
|SharePoint workflow template isn't supported.|0x02110021|
|SharePoint workflow associated with a site or site level content type isn't supported.|0x02110022	|
|SharePoint workflow is filtered out because no new instances are allowed. |0x02210032	|Confirm the workflow is still in use. If you want to continue the migration, reactivate the workflow.	|
|SharePoint workflow is filtered out because no triggers are configured. |0x02210034|Confirm the workflow is still in use. If you want to continue the migration, please reactivate the workflow.|
|SharePoint workflow is filtered out because no sharepoint object is associated. |0x02210033|Check your workflow and associate it with a list or library|
|Workflow migration failed because flow approvers aren't found. |0x02810053| Check the user mapping file or AAD lookup to make sure the approver in Workflow can be mapped to a AAD user.|
|SharePoint workflow subscription found without a workflow definition. |0x02110002|	Confirm your workflow’s status	|
|SharePoint workflow is filtered out because its association list or content type is out of migration scope.|0x02210031|If you migrate workflows of a single list, try to perform workflow migration of its site. If the workflow is associated to a content type, manually create the content type on SPO list or library and try workflow migration again.|
|SharePoint workflow is skipped because it has been migrated before. |0x02810055|
|SharePoint Workflow definition contains unsupported actions. |0x02110026|

## Step 3:  [Activate workflows](spmt-workflow-step3.md)
