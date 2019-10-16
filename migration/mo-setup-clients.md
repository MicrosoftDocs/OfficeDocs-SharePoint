---
title: "Set up Migration Manager clients "
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
description: Set up multiple Migration Manager clients
---


# Setting up individual Migration clients

The Migration Manager centralizes the management of large file share migrations by configuring one or computers or VMs as migration “clients”.  A setup file is downloaded and installed each computer.  After each agent is successfully installed, it is referred to a migration "client" computer in the tool. The Migration Manager can then execute and monitor the migrations, automatically load balancing the task across the pool of clients have been configured.  

## Before you begin

- Check to make sure all system prerequisites have been installed on your local computer or VM before downloading and installing the Migration Manager client setup file

- Confirm that the Windows credentials you plan on using to configure the service has access to **all** the network file shares you plan to migrate.

- Confirm that your have SharePoint Admin credentials to access the “destination” of where you are migrating your content.

### Prerequisites
|**Component**|**Recommendation for best performance**|**Minimum - expect slow performance**|
|:-----|:------|:-----|
|CPU|64-bit quad core processor or better|64-bit 1.4 GHz 2-core processor or better|
|.Net version|V4.6.2 or higher. Learn more: [How to determine which versions are installed](https://docs.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|V4.6.2 or higher|
|RAM|16 GB|8GB|
|Local Storage|Solid state disk: 150 GB free space|Solid state disk: 150 GB free space|
|Network card|1 Gbps|High speed internet connection|
|Operating system|Windows Server 2012 R2 or Windows 10 client|Windows Server 2012 R2 or Windows 10 client|
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration|Required for OneNote migration|
|Anti-virus|Stop 3rd party anti-virus software on your computer prior to installation|Stop 3rd party anti-virus software on your computer prior to installation|</br>

### Required endpoints

|**Required endpoints**|**For**|
|:-----|:-----|
|https://secure.<spam><spam>aadcdn.microsoftonline-p<spam><spam>.com|Authentication|
|https://<spam><spam>api.office<spam><spam>.com|Office 365 APIs for content move and validation|
|https://<spam><spam>graph.windows<spam><spam>.net|Office 365 APIs for content move and validation|
|https://<spam><spam>spmtreleasescus.blob.core.windows<spam><spam>.net|Installation|
|https://*<spam><spam>.queue.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>blob.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>pipe.aria.microsoft<spam><spam>.com|Telemetry/update|
|https://*.<spam><spam>sharepoint<spam><spam>.com|Destination for migration|


## Setup your first client

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
2. In the left pane, under Admin centers, select SharePoint. (You might need to select Show all to see the list of admin centers.)
3. If the classic SharePoint admin center appears, select Open it now at the top of the page to open the new modern SharePoint admin center.
4. In the left pane select **Migration**.
5. Select **Download client setup file**.  
6. Click Run.
7. Enter your SharePoint Admin username and password.  These are to the SharePoint tenant where you will be migrating your content. Click **Next**.
8. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate.  Click Run configuration. 

On completion this computer will be added to the available clients that the Migration Manager can assign tasks.

