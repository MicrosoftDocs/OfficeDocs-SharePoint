---
title: "Get started with Migration Manager"
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
description: Get started with Migration Manager
---


# Get started with the Migration Manager

Migrating large file share content to the cloud is a time and resource intensive process. It is usually necessary to scale up resources to accommodate the large volume of content that you are moving.  This comes at a high operational cost of individually managing each server and the migrations tasks that are running on it. You can’t automatically load balance your jobs, or view at a glance the progress and status of your project across all your devices.

The Migration Manager answers those challenges by providing you a centralized way of connecting servers, creating tasks, having the Migration Manager automatically load balance your migration tasks.  

Located in the SharePoint Admin Center, the Migration Manager guides you through the setup of your devices and the creation of your tasks.  You can specify global or task specific settings, view all-up task progress, and download summary and detailed reports.

You can have an aggregate "all-up" view of your migration project from one location.   and manage the migration of your file shares to SharePoint and OneDrive. You can specify global or task specific settings, view all-up task progress, and download summary and detailed reports.



### How does it work? 

It works in three simple steps – connect, create and migrate.

- **Connect**. Connect your computer or VM to the SharePoint tenant where you want to migrate content

- **Create**. Create a task by entering the URL of the file share that you want to migrate (your source) and URL of the SharePoint site to where you are migrating (your destination) 

- **Migrate**.  After you click Migrate, Migration Manager will do the rest. However many tasks you create, Migration Manager will you can see their progress, download reports


## How do I get started? 

To get started, make sure you have:
 
- **Access to the destination**: You must be either a global admin or SharePoint Online admin to the Office 365 tenant to where you want to migrate your content.

- **Access to the source**: Windows credentials that have read access to any of the network file shares you plan to migrate 

- **Computer or VM** that has the necessary prerequisites installed:  See here for the [List of prerequisites](mo-setup-clients.md)  


### Related links

[How to set up multiple clients in Migration Manager](mo-setup-clients.md)</br>
[How to create a task in Migration Manager]()</br>
[Migration Manager settings](mo-settings)</br>
[How to format your CSV file for bulk upload into the Migration Manager](mo-bulk-upload-format.md)</br>