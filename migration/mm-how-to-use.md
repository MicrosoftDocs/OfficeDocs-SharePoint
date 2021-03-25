---
title: "How to use Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: How to use Migration Manager in the SharePoint admin center to move your content to Microsoft 365.
---
# Step 2: Create a migration task with Migration Manager

Migration Manager is located in the modern SharePoint admin center. You will be guided through agent setup and creating your file share migration tasks.    

## Before you begin

Before you create your first migration task, do the following checks: 


|**Check**|**Do**|
|:-----|:-----|
|[Prerequisites](./mm-setup-clients.md#prerequisites)|Make sure all system prerequisites have been met on your local computer or VM before running the Migration Manager agent setup file.|
|[Required Endpoints](./mm-setup-clients.md#required-endpoints)|Review the required Endpoints|
|[Government cloud](mm-gov-cloud.md)|If you are on a Government cloud, make sure your settings are correctly configured before you begin.|
|[Set up your Migration Manager agent](mm-setup-clients.md#set-up-an-agent)|You can set up as many agents as needed to scale your project.|



## Source and destination
For every migration task you create, you'll be prompted for a **source** and a **destination**. The credentials that you used to set up your agents have permission to access to any file share you plan to migrate.

- **Source** - The source is where your file share content currently exists. File shares include centralized file hosting on a network server, a network drive, or shared files or disks on a local computer. Often referred to as a "Z drive" on networked computers, it's a shared drive somewhere on the network. You'll need to know the path of the file share and enter it using the format:  **<spam><spam>\\\contoso\fileshare.**<spam><spam>

- **Destination** - The destination is where in Microsoft 365 you want to copy your content. It can be a SharePoint site, OneDrive, or a Teams location. Decide where you want the content to be, and then enter the specific location URL. 

## Create a migration task

  
1. Go to the [Migration page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.   
2. Select **Add task**.   
3. Under Method, select either **Single source and destination** or **Bulk migration**. If you have only a few file shares to migrate, select the single source and destination method. If you are migrating content from a large number of file shares, select bulk migration.
4. **Source**. Enter the path to the file share that contains the content you want to migrate.  Use the format \\contoso\fileshare. Select **Next**.
5. **Destination**. Enter the SharePoint site, OneDrive, or Teams location where you want to migrate your content. 
6. Select the specific location in your destination. Depending on your destination, the location could be a document folder or Teams channel. Select **Next**.
7. In the **Task name** box, enter a friendly name to identify your task. 
8. Review your settings to make certain they're set correctly for you. Select **Run now**. To learn more about specific settings, see [Migration Manager settings](mm-settings.md).
9. This task is added to the list. For each file share you want to migrate, select **Add task**.

>[!Note]
>Each agent can have up to 10 tasks in its queue.