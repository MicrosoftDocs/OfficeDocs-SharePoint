---
title: Mover reports
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover reports"
---
# Reports

## Dashboard overview

The dashboard statistics given at the top of the **Migration Manager** provide a visual summary of your overall migration. This includes the number of users in the current selected migration, the number of files scanned or transfered, and the amount of data scanned or transfered; as well as any issues, errors, or failures that may have occured.

![migration manager dash](media/migration-manager-dash.png)

## Transfers

The **Transfers** section of the **Migration Manager** dashboard provides a brief rundown of all user transfers and scans.

- **New**: Number of individual users that have yet to be scanned or transfered.
- **Running**: Number of users that are currently running either a scan or a transfer.
- **Complete**: Number of users that have successfully completed scans or transfers.
- **Issues**: Number of users that encountered errors during a scan or a transfer.
- **Failures**: Number of users that failed to scan or transfer.

>[!Note]
>The total **Transfers** tally is from all users regardless of status.

![migration manager transfers](media/migration-manager-transfers.png)

## Files

The **Files** section of the **Migration Manager** dashboard provides a total of all files scanned and transfered across all users in a migration.

- **Complete**: Number of files that have successfully scanned or transfered.
- **Issues**: Number of files that have encountered issues and failed to scan or transfer.

>[!Note]
>The total number of **Files** is from both scanned and transfered users. Be aware that scanned files are marked as *Skipped* as they have yet to be transfered.

![migration manager files](media/migration-manager-files.png)

## Data

The **Data** section of the **Migration Manager** dashboard shows the total of all data scanned and transfered across all users in a migration.

- **Complete**: Amount of data that has been successfully scanned and transfered.
- **Issues**: Amount of data that encountered issues and has failed to scan or transfer.

>[!Note]
>The total amount of **Data** is from both scanned and transfered users. Be aware that scanned data is marked as *Skipped* as it has yet to be transfered.

![migration manager data](media/migration-manager-data.png)

           ## Active filter list

This provides the list of all current **Filters** that you can apply to the **Active Filter** search bar.

>[!Note]
>Applying the filters changes the statistic shown in the **Migration Manager** dashboard.

|**Filter label**|**Label effect**|
|:-----|:-----|
|Status|	Filters by status [for example, Failed, Success, User Does Not Exist, and so on.]|
|Files|	Filters based on files transfered, failed, and skipped.|
|Data	|Filters based on data that has transfered, failed, or skipped.|
|Success|	Displays all successful Data and Files transfered.|
|Failed	|Displays all Data and Files that have failed to transfer.|
|Skipped	|Displays all data and files that were skipped.|
|Schedule	|Displays all users with scheduled transfers [for example, Hourly, Daily, Weekly, Monthly].|
|Path	|Filters for specific source or destination path [for example, path:username].|
|Destination|	Filters for specific destination path [for exaample, path:@domain<spam><spam>.com].|
|Source|	Filters for specific source path [for example, path:foldername].|
|Destination path	|Functions the same as **Destination**.|
|Source path	|Functions the same as **Source**.|
|Tags	 |Lists transfers with previously implemented custom tags.|
|Notes	|Filters by keywords in previously implemented custom notes.|
|Code|	Filters for specific status codes.|
|Destination name|	Displays transfers with a specific destination name.|
|Source name|	Displays transfers with a specific source name.|

### Scan report

For more information about the scanning process, see the **Scanning** section.

After the scan report is downloaded and opened, look for these key items:

- Users with a failed status. We recommend rerunning the scan for these user(s).
- Users with one file or less. **Note**: Sharing permissions are still transfered.
- Users with the most data. Use this information to decide about a data distribution strategy that suits your needs. For more info about data distribution, see **here**.

![scan report example](media/scan-report-example.png)

### Migration report

The **Migration Report** provides an in-depth overview of your entire migration, including (but not limited to) speed and time statistics, totals for files and data transfered, and info relating to the latest run.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Report**.

The CSV report provides the following information for each user pairing:

|**Header/Statistic**|**Definition**|
|:-----|:-----|
|Schedule ID|	Our internal reference unique to the user pairing created.|
|Source|	Source directory path.|
|Destination	|Destination directory path.|
|Tags	|If you have used our tags feature, you'll see them here. Use tags to differentiate operational departments, to flag specific users, and so on.|
|Notes|	If you have added Notes to user pairings in the **Migration Manager**, they'll appear here, for example, *Remind me to check the logs on this user* or *Weird folder problem - ask support*.|
|First Run Start|	When the first transfer for this user pairing began.|
|Files Transfered	|Total files transfered.|
|MB Transfered	|Total data (MB) transfered.|
|Times run|	Total number of times this user pairing has been run.|
|Total Duration	|Total duration of each time this user pairing has been run.|
|Average File Velocity (files/hour)|	Files transfered, divided by the total duration.|
|Average Data Velocity (MB/hour)	|Data (MB) transfered, divided by the total duration.|
|Last Status|	Last status of the user pairing.  This is also reflected by the color of each row in the **Migration Manager**. Examples include *Success*, *Some Problems*, *Failure*.|
|Last Status Code|	Internal reference number refering to the last status of the user pairing.|
|Last Skipped|	Number of skipped files in the last run.|
|Last Files|	Number of files transfered in the last run.|
|Last MB	|Volume of data (MB) transfered in the last run.|
|Last MB Skipped	|Volume of data (MB) skipped in the last run.|
|Last Failed Files	|Number of files that failed to transfer in the last run.|
|Last Folders Listed	|Number of folders that we opened/created in the last run.|
|Last Folders Failed	|Number of folders that we failed to open/create in the last run.|
|Last Run Start	|When the latest transfer on this user pairing began.|
|Last Run End	|When the latest transfer on this user pairing finished.|
|Last Run Duration	|How long the latest transfer for this user pairing took to complete.|
|Last File Velocity (files/hour)	|Files transfered, divided by the total duration for the last run.|
|Last Data Velocity (MB/hour)|	Data (MB) transfered, divided by the total duration for the last run.|

Download an example CSV:

[example_migration_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_report.csv)

### Migration table report

The **Migration Table Report** generates an overview of your entire migration based on the custom designated columns you have set.

To edit report columns, in the **Migration Manager**, select **Migration Actions**, and select **Customize Columns**. Here you can set and reorganize which **Columns** you want to display when you download the CSV report.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Table Report**.

![migration table example](media/migration-table-example.png)

Download an example CSV:

[example_migration_table_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_table_report.csv)

### Migration error report

The **Migration Error Report** generates a simplified **Migration Report** that focuses on any problematic files, folders, permission errors, or general errors.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Error Report**.

![migration error example](media/migration_error_example.png)

Download an example CSV:

[example_migration_error_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_error_report.csv)
