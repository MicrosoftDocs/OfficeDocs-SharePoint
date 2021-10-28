---
title: Running the Mover migration
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Running the mover migration"
---
# Running the Mover migration

## Scanning

Scanning your source data is key to running a smooth and stress-free migration. For the full list of key data necessary for a smooth migration, see this **checklist**.

>[!Note]
>Scanned data is marked as *Skipped* as scanning does not transfer data; it simply counts the data that we would normally transfer from the source.
>
>After a transfer is scanned, the source/destination are effectively *locked in.* Be sure to double-check that they are correct, and not left blank.

## Running the scan

You now have a list of users appearing in the migration, complete with destination set up.

To start the scanning source data process:

- Select all users. At the top of the navigation bar, select the checkbox.

After you select all users, select **Scan X Users**.

![scan users](media/scan-users.png)

After the scan has successfully completed, the users appear in green. The scan time varies depending on the data amount in the source.

After users appear in green, yellow, or red, on the top right side of your screen, select **Migration Actions**, and then select **Scan Report**.

>[!Note]
>If your scan encounters an error or crashes, our app automatically reruns the scan up to three times to attempt to resolve the issue.

![scan report migration](media/mover-scan-report-migration.png)

For in-depth info about **Scan Report**, see the **Reports** subsection under the **Scan Report** section of this guide.

## Managing Users Who Own Large Amounts of Data 

Upon completing your Scan, download the scan reports and review/address any large Source data owners. 
 
The more users simultaneously being transferred, the higher our throughput for your migration. Users with large data sets should be broken into smaller Service Accounts to facilitate faster transfers. 
To maximize throughput, users should not own greater than 400,000 items or 5 TB of data. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds. 

**Examples**

|Size|Action| 
|:-----|:-----| 
|If a user owns more than 400,000 items, this should be |divided between 4 users so that each user owns 100,000 items. |
|If a user owns more than 5 TB of data, this should be |divided between 5 users so that each user owns 1 TB.| 
 
To create Service Accounts, work with your Source Cloud Storage Admin to carry out the following: 

1.	Once you have identified a large user, determine how many Service Accounts will be required (see example above). 
2.	Create the Service Accounts and assign them a license. 
3.	From the original large user, identify the folder(s) you would like to assign to the Service Account. 
4.	Change the ownership of said folder(s) to the new Service Account. 
This may require that the original owner first share it with the new owner, where  the new owner would have to accept, then the original owner will then have the  option to select them as owner. 
5.	When it comes to migrating the Service Account, create a corresponding OneDrive user/SharePoint site to migrate the new Service Account content to.
6. Before making any changes, you should reach out to your tenant administrator, investigate any source custom solutions or ​integrations that you might be using, and determine if these ownership changes will have any impact.
 
When mapping please ensure that each Service Account has its own unique matching Destination account to optimize performance. 

|Source Path|Destination Path |
|:-----|:-----|
|originaluser@contoso.com|originaluser@contoso.com/[upload folder]* |
|serviceaccount1@contoso.com |serviceaccount1@contoso.com/[upload folder]* |
|serviceaccount2@contoso.com |serviceaccount2@contoso.com/[upload folder]* |
|serviceaccount3@contoso.com |serviceaccount3@contoso.com/[upload folder]* |
* = optional folder 


## Migrating users

We recommend starting slowly. Test one user, then three to five. If all looks good, and you see data being downloaded and uploaded, start queuing everyone, and stage the rest of your users.

1. To select a user(s), check their row's respective checkbox.
2. Select **Start Migrating X Users.**
3. Review your migration summary. This informs you which user is being copied, where they are transferring from, and where to, as well as when the transfer begins.
4. Review and agree to our terms and conditions, and then select **Continue**. Your users are immediately queued for migration.

![start migration](media/mover-start-migration.png)

>[!Note]
>If your transfer encounters an error or crashes, our app automatically reruns the transfer up to three times to attempt to resolve the issue.

### Canceling users

To cancel a currently running transfer:

1. Find the transfer(s) you want to cancel, and select them. A running transfer is in blue and have a status of **Running** or **Queued**.
2. For multiple users, select the **User Actions** dropdown, or right-click on a single user.
3. Select ***Cancel X Transfers**.

This action stops the transfer as soon as possible (usually within a few seconds).

### Rerunning users

The best way to resolve any issues with a transfer is to rerun it. This action checks over all the files in your destination, compares them to the source, and then transfers over the new or modified files.

All transfers take advantage of our incremental feature and only transfers new or modified data differences between your source and Office 365.

As long as a transfer is not running, to restart a transfer, you can re-queue a user.

To rerun or restart your transfer, complete the following steps:

1. Select the or user(s) you want to rerun.
2. To run the users again, at the top right, select **Start Migrating X Users**.
