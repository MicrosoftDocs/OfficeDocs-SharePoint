---
title: "Set up multiple Migration Manager clients"
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
description: Set up multiple Migration Manager clients
---

# Set up multiple Migration Manager clients

The Migration Manager centralizes the management of large file share migrations by configuring one or computers or VMs as migration “clients”.  To do this, you download and run a setup file on each computer.  After each is successfully configured, it is recognized by Migration Manager as a migration "client". Migration Manager can then execute and monitor the migrations, automatically load balancing the task across the pool of clients have been configured. 

When you run the setup file, you will be prompted for two sets of credentials: Your SharePoint Admin credentials to access your destination, and your Windows credentials that have read access to any of the network file shares you plan to migrate. This pair of credentials creates a trust with Migration Manager.  Migration Manager now sees it as an available "client" to which it can automatically assign migrations tasks that you create. The more clients you configure, the more resources Migration Managerhas to load balance the tasks you create. 


## Before you begin

- Check to make sure all system prerequisites have been installed on your local computer or VM before downloading and installing the Migration Manager client setup file


### Recommended practices

- Determine how many VMs or computers you plan on using for your migration tasks. Identify these up front.

- Confirm that your have SharePoint Admin credentials to access the “destination” of where you are migrating your content.

- Confirm that the Windows credentials you plan on using to configure the service has access to **all** the network file shares you plan to migrate.  **Best practice** Create a Windows admin account specifically to use for your migration project. Make sure this admin account has access to any file share that you plan on migrating. Log into each VM or computer with this account before you run the setup file.

- Designate one person to run the setup file on the VMs or computers to ensure consistency

- After the "clients" are all configured, anyone with the permission to go into the SharePoint Admin center can create tasks.  The tasks will be automatically assigned to one of the clients which can be used interchangeably as the Windows credentials has access to any file share you plan on migrating.


 


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


## Setup a single client

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
2. In the left pane, under Admin centers, select SharePoint. (You might need to select Show all to see the list of admin centers.)
3. If the classic SharePoint admin center appears, select Open it now at the top of the page to open the new modern SharePoint admin center.
4. In the left pane select **Migration**.
5. Select **Download client setup file**.  
6. Click Run.
7. Enter your SharePoint Admin username and password.  These are to the SharePoint tenant where you will be migrating your content. Click **Next**.
8. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate.  Click Run configuration. 

On completion this computer will be added to the available clients that the Migration Manager can assign tasks.




## Set up multiple clients

Based on the size of the content you want to migrate, you can setup as many clients as you need. If you are setting up multiple clients, we recommend that you download the client setup file to a shared location. That way you can you can easily download the setup file on each of computer or VM.  

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin.
2. In the left pane, under Admin centers, select SharePoint.
3. In the left pane select **Migration solutions** and then **Migration Manager**.
4. Select **Download client setup file**.  If you previously downloaded the setup file, click the *Clients* tab and select **Add client**.  Save the file to file to a shared location.
5. Run the setup file on each VM or windows computer you plan on using to run migration tasks on.




