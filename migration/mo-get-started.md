---
title: "Get started with SharePoint Migration Orchestration"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- M365-collaboration
- IT_Sharepoint_Server_Top
- SPMigration
search.appverid: MET150
ms.custom: 
ms.assetid: 
description: Get started with SharePoint Migration Orchestration
---


# Get started with the SharePoint Migration Center 

Migrating large file share content to the cloud is a time and resource intensive process. It is usually necessary to scale up resources to accommodate the large volume of content that you are moving.  This comes at a high operational cost of individually managing each server and the migrations tasks that are running on it. You can’t automatically load balance your jobs, or view at a glance the progress and status of your project across all your devices.

## What is it?

The Migration Center is a feature in Office 365 that lets you centrally create, distribute and manage the migration of your file shares to SharePoint and OneDrive.

Located in the SharePoint Admin Center, the SharePoint Migration Center guides you through the setup of your devices and the creation of your tasks.  You can specify global or task specific settings, view all-up task progress, and download summary and detailed reports.

### How does it work? 

It works in three simple steps – connect, create and migrate.

- **Connect**. Connect your computer or VM to the SharePoint tenant where you want to migrate content

- **Create**. Create a task by entering the URL of the file share that you want to migrate (your source) and URL of the SharePoint site to where you are migrating (your destination) 

- **Migrate**.  After you click Migrate, Migration Center will do the rest. However many tasks you create, Migration Center will you can see their progress, download reports


## How do I get started? 

To get started, make sure you have:
 
- **Access to the destination**: You must be either a global admin or SharePoint Online admin to the Office 365 tenant to where you want to migrate your content.

- **Access to the source**: Windows credentials that have read access to any of the network file shares you plan to migrate 

- **Computer or VM** that has the necessary prerequisites installed:  See here for the [List of prerequisites](mo-setup-clients.md)  


### Related links

[How to set up multiple migration clients](mo-setup-clients.md)</br>
[How to create a migration task]()</br>
[Migration Center settings](mo-settings)</br>
[How to format your CSV file for bulk upload into the Migration Center](mo-bulk-upload-format.md)</br>