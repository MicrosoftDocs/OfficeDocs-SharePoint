---
title: Troubleshooting Mover migration errors
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Troubleshooting Mover errors"
---
# Troubleshooting Mover migration errors

The following tables contain error messages you may encounter and how to resolve the issue.


## Mover migration errors

|Error|Action|
|:-----|:-----|
|Error: "The Office 365 connector has not been authorized in the Azure Tenant yet."|Authorize the connector by granting admin consent in the Azure Tenant for the "Office 365 Mover" App.|
|Error: "Authorization failure" shown on the connector.	|Confirm that the connector is fully authorized or Reauthorize the connector.
|Error: Migration failing while using a .csv file as source/destination reference|Confirm that the User Transfer Row has the correct syntax for both source and destination paths|
|Error: "Please retry" during migration.|Review log and confirm source/destination paths for user; check syntax if user transfer row was uploaded via .csv|
|Error: "Cannot claim this folder as it is claimed by owner" in migration logs.	|User does not have explicit ownership of this folder and it is shared to them.|
|Error: Migration crashes	|Review log data and determine the issue. Reauthorize the connector and rerun the migration.|
|Error: Transferred files show SYSTEM as "owner" and "last modified by"	|Ownership is dependent on, and set by, the connector data is being transferred from. Consult the guides file authorship section for your specific connector.|
|Error: Can't set permissions	|Confirm the syntax of the user permissions being set, check that the users exist in source/destination and that the User Row being transferred has explicit ownership over the data and it is not shared to them.|
|Error: "Refreshed OAuth Authorization Token: 404 Not Found" - "itemNotFound: The resource could not be found"	|Reauthorize (or delete and recreate) the connector and ensure that you have administrative privileges when authorizing.|
|Error: "A file with the name x already exists. It was last modified by  y. "|The app itself encountered an error while attempting to access the file. Rerunning the migration should clear this error.|
|Message: "Waiting on Microsoft batch Processing", Migration freezes  failed files not shown in logs|The data has not finished propagating yet for the logs, contact support if the migration doesn’t complete in 24 hours.|
|Error: Migration quickly says "complete", but the data didn’t transfer.|Ensure that the user has ownership of data in the source path and all data is not shared to them.|
|Error: "Unsuccessful HTTP response: Unable to update users. Required heading not found: id"|The ID column of each user needs to be the first column of the .csv in order to change already existing User Transfer Rows.|
|Error: "Transfer failed because the target folder for one of your connectors could not be set."|Ensure that there is no syntax errors for the destination path and that the folder does exist in the destination directory/account|
|Error: Stuck on “Loading Application” during account verification in IE Browser.|Use Chrome, Edge, or Firefox browsers|
|General: How to stop and restart a migration after recovering from an error...	|Check the box on the left of a User Transfer Row, and then click "Start Migrating x User" this will create an incremental transfer to pick up where you left off.|
|Error: "Source Initialization" or "Destination Initialization": Application has lost connection with the source connector. |Mover is no longer connected to the source or destination. Reauthorize the connector.|
|Error: Failed response: Upload Failed.|Mover is no longer able to upload. Reauthorize the connector and rerun the user transfer row.|
|Error: Item has no parent id|Files in the root directory of a OneDrive user often cause this error. Move the files into a folder or attempt rerun the user transfer rows until successful.|

## Other Mover errors

|Error|Action to take|
|:-----|:-----|
|Error: "Bad Request: Unable to update users. Required heading not found: id"|The ID column of each user needs to be the first column of the .csv in order to change already existing User Transfer Rows. For more information see: [Review users: editing](https://docs.microsoft.com/sharepointmigration/mover-review-users#editing)|
|Could not retrieve user count: user count could not be retrieved.|Reauthorize the connector.  See [Reauthorizing connectors](https://docs.microsoft.com/sharepointmigration/mover-manage-connectors#reauthorizing-connectors)|
|Error: Unable to get contents of this folder: Connection Error|Some IT departments don't want to do Box or Dropbox data migration themselves, so instead of using Box or Dropbox (Co-Admin) to O365, they are asking all their users to use Single User to OneDrive For Business (Single User). <br>- If your organization requires Multi-Factor Authentication (MFA) and you receive an authorization error, your conditional access policy may not be configured correctly.<br>- One workaround is for the administrator to disable MFA for these users during Mover migrations.<br>- Otherwise, you will need to contact "Azure Identity" support for help configuring conditional access policies.

