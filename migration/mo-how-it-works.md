---
title: "How the Migraiton Center works"
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
description: How the migration center works.
---


Configure:  
The first step is to download and configure  one or more local computers or VMs as a migration “client”. When you run the setup file, you will be prompted for two sets of credentials:  Your SharePoint Admin credentials to access your destination, and your windows credentials that have read access to any of the network file shares you plan to migrate.  This pair of credentials will be stored in the Migration manager. Once a “client” is setup, it will be available for tasks to be automatically assigned to it by the Migration manager.  The more clients you configure, the more resources Migration Manager/Center has to load balance the tasks you  create. 
Note:  Based on the size of the content you want to migrate, you can setup as many clients as you need. Follow the same instructions for your first client. If you are setting up multiple clients, we recommend that you download the client setup file to a shared location.   That way you can you can easily download the setup file on each of computer or VM.  



Create:  
Create your migration tasks.   In each task you will be prompted from a source URL (e.g., individual or a network file share), and a destination URL (a SharePoint document library or a OneDrive).  Additionally you can set task level or global settings that further filter the files that are being migrated.  For example, you may only want to migrate files created within a certain time period or exclude certain file types.
Migrate:  
Once you submit your task, the Migration Center will automatically assign it to one of your available clients.  Each task is automatically load balanced across your available pool of migration clients that you have configured.