---
title: Authorizing the Dropbox Connector
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Authorizing the Dropbox Connector"
---
# Authorizing Dropbox Connector

## Dropbox FAQ

### What happens to my unmounted folders?

Dropbox supports a selective sync function that can cause problems when trying to transfer a shared folder that is *mounted* in a specific way in Dropbox's file system. These folders cannot be transferred, but we can detect these folders upon request to help identify them.

### What about Dropbox Team folders?

For easy access, our app displays Team Folders in the root of your connector (among the users).

The way Dropbox structures the source Team Folders is reflected in the auto-discover feature as:
*/Your team's shared workspace*.

To set a source path as a Dropbox Team folder, you need to use a .csv file and direct it to a specific team folder within this shared workspace root directory.

The formatting for a Dropbox Team Folder source path should be something similar to this:

- */Your team’s shared workspace/TeamFolder Name*


### How does Dropbox manage sharing and permissions?

Dropbox restricts sharing based on files or folders already shared. If you have a shared folder, Dropbox doesn't allow you to change the sharing permissions of the individual subfolders or files within that folder. You are also not allowed to modify the sharing scheme parent until you have unshared the subfolder.


## Authorizing Dropbox Business (Multi-User)

Authorizing **Dropbox Business** as an administrator is straightforward. To authorize or add a Multi-User Dropbox Business account as a connector, follow these steps.

>[!Important]
>You MUST be an Administrator. A non-administrator account does not work.

1. In the **Transfer Wizard**, select **Authorize New Connector**.</br>

![authorize dropbox connector](media/auth-dropbox-connector.png)</br>

2. In the **Connector** list, find **Dropbox**.
3. Select **Authorize**.

![authorize source connector](media/mover-auth-source-connector.png)</br>

4. A new window (tab) opens. Name your Connector \<optional\>.</br>

![Name new dropbox connector](media/name-new-dropbox-connector.png)</br>

5. Select **Authorize** again.

6. If you aren't logged in, you can use either your Dropbox credentials or an SSO account to grant access.

![Sign in to Dropbox](media/dropbox-signin.png)</br>

7.  To grant our app access to your Dropbox Account, select **Allow**.</br>

![Grant access to Dropbox account](media/grant-access-dropbox-account.png)</br>


## Connect your source Dropbox account

If you aren't already connected after you have authorized your source, select **Dropbox**, and load the connector. An icon appears, and shows you how many users you are migrating.

![execution select Dropbox source](media/execution-select-Dropbox-source.png)



