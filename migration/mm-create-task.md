---
title: "Create a task Migration Manager"
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
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Create a task in Migration Manager
---

# Create a task in Migration Manager

The Migration Manager centralizes the management of large file share migrations by configuring one or more computers or virtual machines (VMs) as migration "agents". To do this, you download and run a setup file on each computer.  

When you run the setup file, you are prompted for two sets of credentials: SharePoint Admin credentials to access your destination, and Windows credentials that have read access to any of the network file shares you plan to migrate. This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available "agent" to which it can automatically distribute migrations tasks.

After a agent is configured, anyone with the permission to go into the SharePoint Admin center can create tasks. The tasks will be automatically distributed to one of the configured agents.


## Before you begin
 
You must have agents set up prior to creating a task. See the setting up the agent topic.





## Create a new task

1. Go to the [Migration Manager page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Enter the username and password that has access to all content of the file shares you will be migration.
3. Select Add Task.
4. Add a source
5. Add a destination
6. 
7. Enter your SharePoint admin username and password. These are to the SharePoint environment where you will be migrating your content. Select **Next**.
8. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
9. Test agent access (optional) or click **Close**.

On completion this computer will be added to the available agents that the Migration Manager can assign tasks.

>[!Important]
> Passwords are not stored in the installer.

