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



The Migration Manager centralizes the management of large file share migrations by configuring one or more computers or virtual machines (VMs) as migration "agents". To do this, you download and run a setup file on each computer.  

When you run the setup file, you are prompted for two sets of credentials: SharePoint Admin credentials to access your destination, and Windows credentials that have read access to any of the network file shares you plan to migrate. This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available "agent" to which it can automatically distribute migrations tasks.

After a agent is configured, anyone with the permission to go into the SharePoint Admin center can create tasks. The tasks will be automatically distributed to one of the configured agents.


## Before you begin
 
|**Check**|**Do**|
|:-----|:-----|
|[Prerequisites](#prerequisites)|Make sure all system prerequisites have been met on your local computer or VM before running the Migration Manager agent setup file.|
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
|Anti-virus|Anti-virus software on your computer can slow down the migration speed. Be aware of this, but consider the risk of turning off your organization's antivirus software. |


</br></br>

### Required endpoints

|**Required endpoints**|**For**|
|:-----|:-----|
|https://secure.<spam><spam>aadcdn.microsoftonline-p<spam><spam>.com|Authentication|
|https://<spam><spam>api.office<spam><spam>.com|Microsoft 365 APIs for content move and validation|
|https://<spam><spam>graph.windows<spam><spam>.net|Microsoft 365 APIs for content move and validation|
|https://<spam><spam>spmtreleasescus.blob.core.windows<spam><spam>.net|Installation|
|https://*<spam><spam>.queue.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>blob.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>pipe.aria.microsoft<spam><spam>.com|Telemetry/update|
|https://*.<spam><spam>sharepoint<spam><spam>.com|Destination for migration|
|https://<spam><spam>*.blob.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|
|https://<spam><spam>*.queue.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|

</br></br>

### Government Cloud

Settings for goverment cloud tenants are listed below.  The default setting is **0**.

|**Cloud**|**Setting value**|
|:-----|:-----|
|Consumer|0|
|GCC|0|
|GCC High|2|
|DoD|2|
</br>
If your are either a **GCC high** or **DoD** customer, you need to make a change to configuration file before you install the agent. To configure and install agent, do the following:

1. Download the agent setup file.
2. Open the setup file and remain on the **Welcome** page. 
3. Open  *%temp%\SPMigrationAgentSetup\SPMigrationAgentSetup\microsoft.sharepoint.migration.common.dll.config*.
4. Change the value of *SPOEnvironmentType* from 0 to 2.
5. On the Welcome page, click **Next**. Follow the prompts to enter your SharePoint admin username and password to your GCC High or DoD account.
6. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
7. Test agent access (optional) or click **Close**.
</br></br>
## Set up a single agent

1. Go to the [Desktop Tool (SPMT) page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationTool&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. Select **Download agent setup file**.
3. Open the setup file. On the Welcome page, select **Next**.
4. Enter your SharePoint admin username and password. These are to the SharePoint environment where you will be migrating your content. Select **Next**.
5. Enter your Windows credentials that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
6. Test agent access (optional) or click **Close**.

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

  
