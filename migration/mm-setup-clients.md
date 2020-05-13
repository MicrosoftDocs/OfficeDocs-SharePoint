---
title: "Setup Migration Manager agents"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
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
description: Set up multiple Migration Manager agents
---

# Setup Migration Manager agents

>[!NOTE]
>Features noted in this topic are part of a preview release. The content and the functionality are subject to change and are not subject to the standard SLAs for support.


The Migration Manager centralizes the management of large file share migrations by configuring one or more computers or virtual machines (VMs) as migration "agents". To do this, you download and run a setup file on each computer.  

When you run the setup file, you are prompted for two sets of credentials: SharePoint Admin credentials to access your destination, and Windows credentials that have read access to any of the network file shares you plan to migrate. This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available "agent" to which it can automatically distribute migrations tasks.

After a agent is configured, anyone with the permission to go into the SharePoint Admin center can create tasks. The tasks will be automatically distributed to one of the configured agents.


## Before you begin
 
|**Check**|**Do**|
|:-----|:-----|
|[Prerequisites](#prerequisites)|Make sure all system prerequisites have been met on your local computer or VM before running the Migration Manager agent setup file.|
|[Government cloud support](#government-cloud-support)|If you are on the worldwide consumer cloud or GCC government cloud, confirm your configuration file is set correctly. |
|[Required Endpoints](#required-endpoints)|Review the required Endpoints|

>[!NOTE]
>Third party multi-factor authentication is not supported at this time.
</br></br></br>

### Recommended practices

- Determine how many VMs or computers you plan on using for your migration tasks. Identify these up front.

- Confirm that you have SharePoint Admin credentials to access the "destination" of where you are migrating your content.

- Confirm that the Windows credentials you plan on using to configure the service has access to **all** the network file shares you plan to migrate.  

- Create a Windows admin account specifically to use for your migration project. Make sure this admin account has access to any file share that you plan on migrating. Log into each VM or computer with this account before you run the setup file.
</br></br></br>

### Prerequisites

|**Component**|**Recommendation for best performance**|**Minimum - expect slow performance**|
|:-----|:------|:-----|
|CPU|64-bit quad core processor or better|64-bit 1.4 GHz 2-core processor or better|
|.Net version|V4.6.2 or higher. Learn more: [How to determine which versions are installed](https://docs.microsoft.com/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|V4.6.2 or higher|
|RAM|16 GB|8GB|
|Local Storage|Solid state disk: 150 GB free space|Solid state disk: 150 GB free space|
|Network card|1 Gbps|High speed internet connection|
|Operating system|Windows Server 2012 R2 or Windows 10 agent|Windows Server 2012 R2 or Windows 10 agent|
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration|Required for OneNote migration|
|Anti-virus|Anti-virus software on your computer can slow down the migration speed. Be aware of this, but consider the risk of turning off your organization's antivirus software. |


</br></br>

### Government cloud support

If you are on a **worldwide consumer cloud** or **GCC** government cloud, you must first take these steps:

1. Open microsoft.sharepoint.migration.common.dll.config.
2. Change the value of **SPOEnvironmentType** to **0** if you use the Worldwide consumer cloud or GCC.
3. Double-click "microsoft.sharepoint.migrationtool.advancedapp.exe" to start SPMT.
</br></br>

### Required endpoints




## Set up a single agent

1. Go to the [Desktop Tool (SPMT) page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationTool&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Select **Download agent setup file**.
3. Select **Run**.
4. Enter your SharePoint admin username and password. These are to the SharePoint environment where you will be migrating your content. Select **Next**.
5. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Run configuration**.

On completion this computer will be added to the available agents that the Migration Manager can assign tasks.

>[!Important]
> Passwords are not stored in the installer.

## Set up multiple agents

Based on the size of the content you want to migrate, you can setup as many agents as you need. If you are setting up multiple agents, we recommend that you download the agent setup file to a shared location. That way you can easily download the setup file on each of computer or VM.  

1. Go to the [Migration Manager page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Select **Download agent setup file**. If you previously downloaded the setup file, select the *agents* tab, and select **Add agent**. Save the file to file to a shared location.
3. Run the setup file on each VM or windows computer you plan on using to run migration tasks on.

>[!NOTE]
> Migration Manager automatically assigns tasks to a available agent, it does the load balancing for you. You cannot manually assign a task to a specific agent.
>
>Pausing a task does not release the agent to another task. An agent remains unavailable to accept a new task until the task is resumed and completed, or if the task is deleted.

>[!Note]
>The connection between the agent and Migration Manager stays active as long as the computer is still running and the SPO admin credentials that were used to sign into the agent are still valid. 
>
>If the agent does becomes disconnected, it still holds the token to the Migration Manager for up to 7 days. After that time, the agent will need to be reinstalled.

  
