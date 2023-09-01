---
ms.date: 10/11/2019
title: "Setup Migration Manager agents"
ms.reviewer: jhendr
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Set up multiple Migration Manager agents
---

# Step 1: Set up Migration Manager agents

When migrating file shares with Migration Manager, you first set up one or more "migration agents", by running a setup file on each computer or VM you choose to configure. Grouping provides agent flexibility, such as only assigning particular migrations to a particular set of agents, or separating out agents in groups based on geographical location to optimize performance.

When you run the setup file, you are prompted for two sets of credentials.  You need SharePoint or OneDrive Admin credentials depending on your destination, and Windows credentials with read access to the source. Best practice is to not use global admin accounts, but to create service accounts for the agents to utilize. Those Windows credentials must have read access to all file shares you plan to migrate. This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available "agent" to which it can automatically distribute migrations tasks.

After an agent is configured, anyone with the permission to go into the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> can create tasks. The tasks will be automatically distributed to one of the available configured agents.

> [!Important]
> Make sure to download the latest version of the agent setup file.
> Passwords **are not** stored in the installer.

## Planning checklist

|Category|Guidance|
|:-----|:-----|
|Determine how many agents you need|[How many agents to create](#agents-and-performance-considerations)|
|Have the right credentials to use|SharePoint or OneDrive admin for migration destination and an on-premises account for source that has access to ALL network file shares you plan to migrate. Confirm that you have SharePoint or OneDrive Admin credentials to access the "destination" of where you are migrating your content. Verify that the on-premises credentials you plan on using to configure the agent has access to **all** the network file shares you plan to migrate.  |
|Virtual machines or computers to use:|Determine how many VMs or computers you plan on using for your migration project. List the computers or VMs before you start.|
|[Verify prerequisites](mm-prerequisites.md)|Make sure your computer meets the requirements.|
|[Check required endpoints](mm-prerequisites.md)|Verify that you have the required endpoints configured.|
|[Multi-geo tenant](#multi-geo-agent-setup)|If you have a multi-geo tenant, make sure to understand where the agent will be installed.|
|[Pre-provision OneDrive accounts](/onedrive/pre-provision-accounts)|If you are migrating to OneDrive accounts, make sure the accounts are pre-provisioned before you migrate. The migration account must also be give site collection administrator rights to each OneDrive site. Pre-provisioning can be done by using a script as described here: [Pre-provision OneDrive for users in your organization](/onedrive/pre-provision-accounts).|
|[Government Cloud](mm-gov-cloud.md)|If your tenant resides in a government cloud, you may have extra steps to perform before using Migration Manager.|

>[!Tip]
>Create a service account with admin rights for your agent to run on the server or VM, with read access to the sources you migrate, and SharePoint or OneDrive Administrator access to the destination specifically to use for your migration project. Log into each VM or computer with this account before you run the setup file to ensure the agent installs as a service.

>[!NOTE]
>Third party multi-factor authentication is not supported at this time.

## Agents and performance considerations

One factor to achieving the best performance in your migration is using the **fewest number of agents needed** to complete the migration within your timeframe. Using more agents than needed can increase the throttling rate when reports are uploaded.

**Example:** If your migration can be done within the desired time slot using 10 agents and at an acceptable speed, don't use 20 agents. Using more agents means higher traffic and a higher API request rate. 

### Determine how many agents you need

To calculate the minimum required number of agents to use for your migration:

1. Run a test migration with 20 to 30 tasks using 1 agent to test the throughput per agent. Record the time.
2. Estimate the number of tasks for your entire migration. Take the length of time it took 1 test agent to process, and calculate the number of agents for the migration. Factor in the overall length of time you have to complete your migration project.
3. If you have already created more agents than you need, they can be disabled by selecting the agent within Migration Manager.

## Set up an agent

1. Log into the computer or VM you choose to set up an agent with credentials that have read access to all file shares you plan to migrate.
2. From the new SharePoint admin center, select <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">**Migration center**</a>.You need to sign in with an account that has [SharePoint Administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
3. Under "For file shares", select **Get started**.
4. Select the **Agents** tab, and then select **Add**.
5. Select **Download agent setup file**.
6. Open the setup file. On the Welcome page, select **Next**.
7. Enter the SharePoint admin username and password of the environment where you will be migrating your content. Select **Next**.
8. Enter the password of the Windows account that will provide access to **all** the file shares that contain the content you want to migrate. Select **Install**.
9. Test agent access (optional) or select **Close**.  After the setup is completed, the new agent will be added to the available agents that can be assigned tasks.

>[!Note]
>**Multiple agents**.  If you have a large migration project and to set up multiple agents, we recommend that you download the agent setup file to a shared location. That way you can easily download the setup file on each computer or VM.  Multiple agents allow you to batch certain migrations jobs to particular groups depending on need. An example would be grouping agents by datacenter to achieve better performance based on geographical location. 

Example: You are migrating 10,000 users from on-premises shares in two datacenters to OneDrive. 2,000 users have data stored in a California datacenter and 8,000 users have data stored in a Vermont datacenter. You installed two agents at the California datacenter and six agents at the Vermont datacenter. By grouping the agents geographically, you could batch migrations where the source data is in California to the California agent group and for Vermont data to the Vermont agent group. Geographical grouping will provide performance benefits. Without grouping, all datacenters would be in a default group, and you would not have control over which agents are used. This could cause the California agents to migrate Vermont data and Vermont agents to migrate California data. While this technically will migrate files, performance could be affected.


### Working folder

A working folder named **%appdata%\Microsoft\SPMigration** is created for each agent. This folder is where logs, reports, and any temporary folders are saved. Make sure that your working folder has a minimum of 150 GB of free space. It may need more depending on the size of the data you plan to migrate.

## Multi-geo agent setup

If you have a Multi-Geo SharePoint tenant, the agent will be installed in <a href="https://go.microsoft.com/fwlink/?linkid=2185076" target="_blank">Geo locations</a> set in the SharePoint admin center. Before installing the agent, make sure the desired geo-location is the one set in the admin center. To change an agent's geo-location, delete and reinstall the agent. 

Learn more: [Multi-Geo Capabilities in OneDrive and SharePoint Online](/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365)

To install an agent to a different Geo location:

1. **Download** the agent setup file.
2. **Launch** the setup file and remain on the *Welcome page*.
3. **Open** this file:  %temp%\SPMigrationAgentSetup\SPMigrationAgentSetup\Microsoft.SharePoint.Migration.ClientShared.dll.config
4. Under appSettings, add an entry as shown in the following **example** for the desired country/region or data center. (Note: this is an example for Canada.) </br>

```powershell 
 
<add key="GeoLocation" value="CAN" />

```

The country or regional GEO code can be found here [Microsoft 365 Multi-Geo availability](/microsoft-365/enterprise/microsoft-365-multi-geo)

>[!Important]
> **Migration to Teams:** If you are migrating to Teams, the destination Teams site must be in the same GEO as your tenant admin.  If they are different, the Teams channel won't load when you select destination.  

## Installing the agent as an app

 If the system detects you are not joined to a domain when installing the agent, you can install the agent as a Windows app.  If you still wish to install it as a service, exit and sign in with a domain-joined account.

>[!Important]
> If you install the agent as an app, it will not run if the computer is asleep, effectively pausing your migration.  

1. Select **Install as an app**. 

![Install agent as an app](media/mm-agent-app.png)

2. After the agent installs, sign in with your SharePoint Admin credentials.
3. Test if your agent has access to the file shares you want to migrate (optional).

![Install as an app settings](media/mm-agent-app-settings.png)

4. The settings screen will display if and to what tenant you are connected.  Select **unlink tenant** if you wish to sign in to a different tenant.

5. Microsoft 365 will automatically renew authorization to access your tenant as long as the migration agent is active.  If the agent has been inactive for longer than seven days, you may need to sign in again.



## Agent task assignment

Migration Manager automatically assigns tasks to an available agent. You cannot manually assign a task to a specific agent. Each agent can have up to 10 tasks in its queue. You can, however, assign tasks to agent groups.

Pausing a task does not release the agent to another task. An agent remains unavailable to accept a new task until the task is resumed and completed, or if the task is deleted.


## How long will the connection stay active?
The connection between the agent (as a service) and Migration Manager stays active as long as the computer is still running and the SharePoint admin credentials that were used to sign into the agent are still valid. 

If the agent does becomes disconnected, it still holds the token to the Migration Manager for up to 7 days. After that time, the agent will need to be reinstalled.


