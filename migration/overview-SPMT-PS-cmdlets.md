---
ms.date: 07/10/2023
title: "Migrate to SharePoint and OneDrive using PowerShell cmdlets"
audience:  ITPro
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: "Learn how the PowerShell cmdlets based on the SharePoint Migration Tool (SPMT) migration engine let you migrate to SharePoint in Microsoft 365."
---

# Migrate to SharePoint using PowerShell

This article is about the new PowerShell cmdlets based on the SharePoint Migration Tool (SPMT) migration engine. They can be used to move files from SharePoint 2010 and SharePoint 2013 on-premises document libraries and list items, and file shares to Microsoft 365.  For information on all current PowerShell cmdlets relating to SharePoint migration, see the [Microsoft SharePoint Migration Tool cmdlet reference](/powershell/spmt/intro).

The PowerShell cmdlets provide the same functionalities as the [SharePoint Migration Tool](introducing-the-sharepoint-migration-tool.md).

> [!NOTE]
> These PowerShell cmdlets are currently not available for users of Office 365 operated by 21Vianet in China.
  
## System requirements

### Recommended requirements for best performance*

| Description | Recommendation |
|:-----|:-----|
|CPU|64-bit Quad core processor or better|
|RAM|16 GB|
|Local Storage|Hard disk: 150 GB free space|
|Operating system|Windows Server 2016 Standard or Datacenter<br>Windows Server 2012 R2<br>Windows 10 client<br>.NET Framework 4.6.2|
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration|

> [!IMPORTANT]
> PowerShell 5.0x and .NET Framework 4.6.2 or higher are required to support the migration of file paths of up to 400 characters.

### Minimum requirements (expect slow performance)

| Description | Minimum requirement |
|:-----|:-----|
|CPU |64-bit 1.4 GHz 2-core processor or better |
|RAM |8 GB |
|Local Storage |Hard disk: 150 GB free space |
|Network card |High-speed Internet connection |
|Operating system |Windows Server 2008 R2<br>Windows 7<br>Windows 8 or 8.1<br/> .NET Framework 4.6.2 |
|Microsoft Visual C++ 2015 Redistributable |Required for OneNote migration.|
|PowerShell |PowerShell 5.x required to support migration of file paths of up to 400 characters. PowerShell 6.0 or higher isn't supported.|

## Before you begin

1. Provision your Microsoft 365 with either your existing active directory or one of the other options for adding accounts to Microsoft 365. See [Microsoft 365 integration with on-premises environments](/microsoft-365/enterprise/microsoft-365-integration) and [Add users to Microsoft 365 Apps for business](/microsoft-365/admin/add-users/add-users) for more information.
2. Open the folder:

   *$env:UserProfile\Documents\WindowsPowerShell\Modules\Microsoft.SharePoint.MigrationTool.PowerShell*

   Make sure you have DLLs inside of it, if you're using OneDrive you may need to copy the WindowsPowershell Folder into OneDrive / Documents.
3. From this location, run the following PowerShell command

   ```powershell
   Import-Module Microsoft.SharePoint.MigrationTool.PowerShell
   ```

## Create and initialize a migration session

<a name="Step1CreateInitialize"> </a>

- **[Register-SPMTMigration](/powershell/module/spmt/register-spmtmigration)**<br> This cmdlet creates and then initializes a migration session. The initialization configures migration settings at the session level. If no specific setting parameters are defined, default settings will be used.
After a session is registered, you can add a task to the session and start migration.

### Add a migration task

- **[Add-SPMTTask](/powershell/module/spmt/Add-SPMTTask)**<br>
Use this cmdlet to add a new migration task to the registered migration session. Currently there are three different types of tasks allowed:  File share task, SharePoint task and JSON defined task.  Note:  Duplicate tasks aren't allowed.
  
### Remove a task

- **[Remove-SPMTTask](/powershell/module/spmt/Remove-SPMTtask)**<br>
Use this cmdlet to remove an existing migration task from the registered migration.

### Start your migration

- **[Start-SPMTMigration](/powershell/module/spmt/start-spmtmigration)**<br>
This cmdlet will start the registered SPMT migration.

### Return the object of current session

- **[Get-SPMTMigration](/powershell/module/spmt/Get-SPMTMigration)**<br>
Return the object of the current session. This cmdlet includes the status of current tasks and current session level settings. Current task status includes:
  - Count of scanned files
  - Count of migrated files
  - Any migration error messages

### Stop your current migration

- **[Stop-SPMTMigration](/powershell/module/spmt/Stop-SPMTMigration)**<br>
This cmdlet will cancel the current migration.

### Show your migration status details in the console

- **[Show-SPMTMigration](/powershell/module/spmt/Show-SPMTMigration)**<br>
If you start the migration in *NoShow* mode, running the **Show-SPMTMigration** cmdlet will display the task ID, data source location, target location and migration status in the console. Pressing Ctrl+C will return to *NoShow* mode.  

### Remove the migration session

- **[Unregister-SPMTMigration](/powershell/module/spmt/Unregister-SPMTMigration)**<br>
Use this cmdlet to delete the migration session.

## Sample Scenarios

**Example 1:** IT admin adds a SharePoint on-prem task and starts migration in the background.

```powershell
#Define SharePoint 2013 data source#
$SourceSiteUrl = "http://YourOnPremSite/"
$OnPremUserName = "Yourcomputer\administrator"
$OnPremPassword = ConvertTo-SecureString -String "OnPremPassword" -AsPlainText -Force
$SPCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $OnPremUserName, $OnPremPassword
$SourceListName = "SourceListName"

#Define SharePoint target#
$SPOUrl = "https://contoso.sharepoint.com"
$UserName = "admin@contoso.onmicrosoft.com"
$PassWord = ConvertTo-SecureString -String "YourSPOPassword" -AsPlainText -Force
$SPOCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $UserName, $PassWord
$TargetListName = "TargetListName"

#Define File Share data source#
$FileshareSource = "YourFileShareDataSource"

#Import SPMT Migration Module#
Import-Module Microsoft.SharePoint.MigrationTool.PowerShell

#Register the SPMT session with SharePoint credentials#
Register-SPMTMigration -SPOCredential $SPOCredential -Force

#Add two tasks into the session. One is SharePoint migration task, and another is File Share migration task.#
Add-SPMTTask -SharePointSourceCredential $SPCredential -SharePointSourceSiteUrl $SourceSiteUrl  -TargetSiteUrl $SPOUrl -MigrateAll
Add-SPMTTask -FileShareSource $FileshareSource -TargetSiteUrl $SPOUrl -TargetList $TargetListName

#Start Migration in the console. #
Start-SPMTMigration
```

**Example 2:** IT admin wants to bring the migration from the background "NoShow mode" to the foreground, and run below the cmdlet so the migration progress is shown in the console.

```powershell
Show-SPMTMigration
```

**Example 3:**  IT Admin wants to do a bulk migration by loading a .csv file.  The sample file in this example is SPMT.csv.

```powershell
Load CSV;
$csvItems = import-csv "C:\spmt.csv" -Header c1,c2,c3,c4,c5,c6
ForEach ($item in $csvItems)
{
    Write-Host $item.c1
    Add-SPMTTask -FileShareSource $item.c1 -TargetSiteUrl $item.c4 -TargetList $item.c5 -TargetListRelativePath $item.c6
}
```

Two migration tasks are defined in the file of spmt.csv.

```dos
D:\MigrationTest\Files\Average_1M\c,,,https://SPOSite.sharepoint.com,Documents,Test
C:\work\Powershell\negative,,,https://SPOSite.sharepoint.com/,Documents,DocLibrary_SubfolderName
```

Code snippets for bulk migration by loading one JSON file:

```powershell
#Load JSON:
$jsonItems = Get-Content -Raw -Path  "C:\spmt.json" | ConvertFrom-Json
ForEach ($taskItem in $jsonItems.Tasks)
{
    $jsonString = ConvertTo-Json $taskItem -Depth 100
    Add-SPMTTask -JsonDefinition $jsonString -SharePointSourceCredential $onpremCredential
}
```

Three migration tasks are defined in the file of spmt.json.

```json
{
   "Tasks":[
      {
         "SourcePath":"http://On-prem/sites/test",
         "TargetPath":"https://YourSPO.sharepoint.com",
         "Items":{
            "Lists":[
               {
                  "SourceList":"list-01",
                  "TargetList":"list-01"
               }
            ],
            "SubSites":[

            ]
         }
      },
      {
         "SourcePath":"http://On-prem/sites/test",
         "TargetPath":"https://YourSPO.sharepoint.com",
         "Items":{
            "Lists":[
               {
                  "SourceList":"list-02",
                  "TargetList":"list-02"
               }
            ],
            "SubSites":[

            ]
         }
      },
      {
         "SourcePath":"http://On-prem/sites/test",
         "TargetPath":"https://YourSPO.sharepoint.com",
         "Items":{
            "Lists":[
               {
                  "SourceList":"doclib-01",
                  "TargetList":"doclib-01"
               }
            ],
            "SubSites":[

            ]
         }
      }
   ]
}
 ```

**Example 4:** Display migration progress

These samples show how to display the progress of your migration project. **Get-SPMTMigration** returns the object of current session. It includes current tasks status and current session level settings.
The status of current tasks includes:

- A count of scanned files.
- A count of filtered out files.
- A count of migrated files.
- A count of failed files.
- The migration progress of the current task (0 ~ 100).
- The current task status.
- Migration error messages, if there are any.

```powershell

# Start migration in the background
Start-SPMTMigration -NoShow

# Get the object of current migration
$session = Get-SPMTMigration

# Query migration status every 5 seconds until migration is finished
while ($session.Status -ne "Finished")
{
Write-Host $session.Status

    # Query migration progress of each tasks
    Foreach ($taskStatus in $session.StatusOfTasks)
    {
        $taskStatus.MigratingProgressPercentage
}

    Start-Sleep -Seconds 5
} 
 
```
