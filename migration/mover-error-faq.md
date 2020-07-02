---
title: Troubleshooting Mover migration errors
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
description: "Troubleshooting Mover errors"
---
# Troubleshooting Mover migration errors

|Message|Definition|
|:-----|:-----|
|Error: "The Office 365 connector has not been authorized in the Azure Tenant yet."|Authorize the connector by granting admin consent in the Azure Tenant for the "Office 365 Mover" App.|
|Error: "Authorization failure" shown on the connector.	|Confirm that the connector is fully authorize or Reauthorize the connector.
|Error: Migration failing while using a .csv file as source/destination reference|Confirm that the User Transfer Row has the correct syntax for both source and destination paths|
|Error: "Please retry" during migration.|Review log and confirm source/destination paths for user; check syntax if user transfer row was uploaded via .csv|
|Error: "Cannot claim this folder as it is claimed by owner" in migration logs.	|User does not have explicit ownership of this folder and it is simply shared to them.|
|Error: Migration crashes	|Review log data and determine the issue. Reauthorize the connector and rerun the migration.|
|Error: Transferred files show SYSTEM as "owner" and "last modified by"	|Ownership is dependent on, and set by, the connector data is being transferred from. Consult the guides file authorship section for your specific connector.|
|Error: Can't set permissions	|Confirm the syntax of the user permissions being set, check that the users exist in source/destination and that the User Row being transferred has explicit ownership over the data and it is not simply shared to them.|
|Error: "Refreshed OAuth Authorization Token: 404 Not Found" - "itemNotFound: The resource could not be found"	|Reauthorize (or delete and recreate) the connector and ensure that you have administrative privileges when authorizing.|
|Error: "A file with the name x already exists. It was last modified by  y ."|The app itself encountered an error while attempting to access the file. Rerunning the migration should clear this error.|
|Message: "Waiting on Microsoft batch Processing", Migration freezes  failed files not shown in logs|The data has not finished propagating yet for the logs, contact support if the migration doesn’t complete in 24 hours.|
|Error: Migration quickly says "complete", but the data didn’t transfer.|Ensure that the user has ownership of data in the source path and all data is not simply shared to them.|
|Error: "Unsuccessful HTTP response: Unable to update users. Required heading not found: id"|The ID column of each user needs to be the first column of the .csv in order to change already existing User Transfer Rows.|
|Error: "Transfer failed because the target folder for one of your connectors could not be set."|Ensure that there is no syntax errors for the destination path and that the folder does exist in the destination directory/account|
|Error: Stuck on “Loading Application” during account verification in IE Browser.|Use Chrome, Edge or Firefox browsers|
|General: How to stop and restart a migration after recovering from an error...	|Check the box on the left of an User Transfer Row and then click "Start Migrating x User" this will create an incremental transfer to pick up where you left off.|