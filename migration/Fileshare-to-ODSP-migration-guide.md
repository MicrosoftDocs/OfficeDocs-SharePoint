---
ms.date: 06/05/2018
title: "Migrate file shares to SharePoint and OneDrive"
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
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-mar2020
search.appverid: MET150
ms.assetid: 
description: "Learn how to evaluate the environment, prepare, and migrate content from file shares to OneDrive and SharePoint in Microsoft 365."
---

# Guide to migrating file shares to OneDrive, Teams, and SharePoint

This guide helps you prepare to migrate from file shares to OneDrive, Teams, and SharePoint in Microsoft 365.

Most migrations fall into regular phases as follows. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating, and onboarding your users.

> [!NOTE]
> Migrating your file shares with Migration Manager lets you have a centralized way of connecting servers, creating tasks, and automatically load balancing your migration tasks. You are guided through the steps of migrating your file shares, from the setup of agents, the creation of tasks, and the migration to Microsoft 365. 
>
> **Get started:**  [Migrate file shares to Microsoft 365 with Migration Manager](/sharepointmigration/mm-get-started)


   ![Migration process](media/migrationprocess-fileshare.png)

|Migration planning|Assess and remediate|Prepare your OneDrive and SharePoint environment|Migrate|User onboarding|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Assess key areas<br><br>Remediate issues|Pre-provision Microsoft 365 and users|Review migration offerings<br><br>Microsoft FastTrack services<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted|

## File shares

File shares include centralized file hosting on a network server or a network drive or shared files or disks on a local computer. Often referred to as a "Z drive" on networked computers, it's a shared drive somewhere on the network.

## Migration planning

Before you start your migration, it's important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The design of the target environment and the mapping between source and target systems.
- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
- Build your user onboarding into your upfront planning. Communicate early and often with your users about the migration and how it will impact them. Don't wait until the very end to start preparing them for the change.

### What's migrated

When preparing for your file share migration, it's important to know what's being migrated when you use the SharePoint Migration Tool and what's not.

|Migrated|Not migrated|
|:-----|:-----|
|Documents|Conversion of embedded URLs in content|
|File and folder structure|Windows hidden attributes on file and folder|
|User level file and folder permissions|Explicit deny permissions|
|Files under 15 GB|Inaccessible or corrupted documents|
|Site, document, and folder metadata|Files or folders exceeding current SharePoint restrictions and limitations|

### What content goes where

In your planning, include how this transition to Microsoft 365 will make for a more collaborative experience for your users.

Review how you use the content stored in your file shares today. Does the file belong to a single user, even though they might share it with others? If so, save it in your OneDrive. Your OneDrive is private by default, but you can share files with others, which is particularly useful if you aren't working as a team yet.

If you're working on a file or folder intended for team consumption and collaboration, move it to a **shared library** where team members have access by default. OneDrive gives you access to all your shared libraries in Microsoft Teams, SharePoint, or Outlook. When you need a new shared library for team files, you can create one right from OneDrive, add members, and start working together.

![Sharing](media/SP-Migration-WhatGoesWhere_filesharetoODSP.png)

### Permissions vs sharing

How you have shared your files dictates how they appear in the **Shared with me** view in OneDrive.

Files and folders that you have opened from a shared location:

- After migration, the final permission level is determined by a mapping of the most restrictive share or NTFS permission level.
- A user's **Shared with me** folder in OneDrive won't be updated for source files shared with a group the user is a part of.
- After migration, all advanced NTFS permissions are removed. For explicit deny permissions, this means the content is subject to parallel permissions or permission on the folder and parent level and may become accessible.

|Windows file share permissions|SharePoint item access|SharePoint role|
|:-----|:-----|:-----|
|Full control|Full control|Full control|
|Modify|Modify|Contribute|
|Read and execute|Read and execute|Read|
|List folder contents|List folder contents|Read|
|Read|Read|Read|
|Write|Write|Contribute|

## Assess and remediate your content

Before your migration starts, it's important to perform an analysis of your current environment. Only you know your data and how and who uses it.

The SharePoint Migration Tool (SPMT) provides the ability to scan your files and provide assessment reports. To find any issues with your file before migration, turn on the setting **Only perform scanning**.

If you have multiple sources that you want to assess, consider using the bulk process by creating a .json or .csv file.

Here are some of the more common issues that arise when preparing for migration:

| |Assess|Remediate|
|:-----|:-----|:-----|
|**File extensions**|Find all files in the Folders and Files report whose path ends in one of the extensions defined here: [Types of files that cannot be added to a list or library](https://support.office.com/article/30BE234D-E551-4C2A-8DE8-F8546FFBF5B3)|If the blocked file types are scripting files, they are blocked because scripting capabilities are turned off by default in OneDrive. <br><br>If you want to allow these file types, turn on scripting capabilities as described here: [Allow or prevent custom script](/sharepoint/allow-or-prevent-custom-script). <br><br>Make sure you understand why these files are blocked by default as described here: [Security considerations of allowing custom script](/sharepoint/security-considerations-of-allowing-custom-script).|
|**File and folder name characters**|Find all items in the Folders and Files report whose name contains any of the characters detailed here: [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)|Work with your migration vendor to substitute these characters in all file and folder names.<br><br>**Note:** The # and % characters are supported but not enabled by default. Follow these steps to enable them: [New support for # and % in SharePoint and OneDrive](https://techcommunity.microsoft.com/t5/Microsoft-SharePoint-Blog/New-support-for-and-in-SharePoint-Online-and-OneDrive-for/ba-p/60357).|
|**File and folder path length**|Find all items in the *Folders and Files* report whose Path exceeds the file path length described here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)|Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|

## Prepare your OneDrive environment

Before you migrate your file share content, you must pre-provision your users in Microsoft 365. For guidance on pre-provisioning, see
- [Prepare to provision users through directory synchronization to Microsoft 365](/office365/enterprise/prepare-for-directory-synchronization)
- [Pre-provision OneDrive for users in your organization](/onedrive/pre-provision-accounts)

## Migrate

### Migration process

The following is a typical migration process that follows Microsoft's best practices guidance.

> [!IMPORTANT]
> Make sure that the account used to migrate content has permissions on the destination OneDrive.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.</br></br>
2. Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cut-over event in which network file shares and local file shares are disabled and they are directed to use the SharePoint or OneDrive environment. This method is preferred as it reduces user impact.
3. Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you might update your user communication template to address a question you received from a pilot user.</br></br>
4. Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cut-over event for all users to switch to using their OneDrive accounts and SharePoint sites. This helps eliminate users from updating duplicate copies of content.

### Migration offerings

Currently, there are a variety of migration offerings available to you. Which one is right for you?

| Offering | Pricing | Process | Infrastructure | Scheduling | Pace | Expertise | Schedule flexibility |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| Customer Self service | [Migration Manager](/sharepointmigration/mm-get-started) | Flexible, you set the pace | No need to configure complex infrastructure | Less time required involved in scheduling process and restrictions | Customer controls the pace based on their needs | Might have to hire in expertise if you don't have it in place already | Customer controls the schedule flexibility; off hours and blackout hours are defined by them |
| FastTrack driven | Included in your [Microsoft 365 subscription](/fasttrack/o365-data-migration) | Highly structured process and schedule | 	Must set up infrastructure including external access rights, VPNs, test environment, admin environment, establish framework of contacts | Scheduling templates and questionnaires provided as part of the organization process | Schedule is driven in partnership with the FastTrack team | Expertise provided by FastTrack | Must hold to a set schedule |
| Partner driven | Price dependent on complexity | 	Customized to your need | Customized to your need | Customized to your need | Customized to your need | Expertise provided | Customized to your need |

**Self service**

The benefit for self-service migration is that you have full control over your process and timing, and you determine the pace of migration. Using [Migration Manager](/sharepointmigration/mm-get-started), you will be able to leverage your own IT resources rather than having to invest in outside expertise.

**Microsoft FastTrack**

FastTrack is a Microsoft service included in your subscription cost providing you with a set of best practices, tools, resources, and experts committed to making your experience with the Microsoft cloud a great one. OneDrive onboarding guidance, migration benefits, and adoption guidance are included in the benefit offering.

Onboarding guidance includes: help to discover what's possible, creating a plan for success, and onboarding new users and capabilities at a flexible pace. The [Data Migration](/fasttrack/O365-data-migration) benefit covers guidance on migrating content from file share, Box, or Google Drive source environments.

This guidance covers enablement of both OneDrive and the source environment. FastTrack will also perform specific data migration activities on behalf of the customer for those with 500 or more licenses. For more details, see [FastTrack Center Benefit Overview](/fasttrack/O365-data-migration). Interested in getting started? Visit [FastTrack.microsoft.com](https://fasttrack.microsoft.com/), review resources, and submit a Request for Assistance.

**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or apps to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Microsoft 365. For more info, see [Microsoft Partner Center](https://partnercenter.microsoft.com/partner/home).

## User Onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:

- **Evangelize the move**. Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training**.  Provide training to your users on the features in OneDrive.
- **Train your helpdesk**.  Before the cut-over event, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime**. Plan for possible downtime during the migration.

Develop a plan for sending communications to your user base, providing clear statements of timing, and expectations and impact to the individual, including:

- The migration timeline and how it will impact them. Include any user calls to action.
- Assure them that if they already have content in OneDrive, their content is safe and won't be overwritten.
- Let them know whether individuals can opt out of the migration process.

### Onboarding related resources

- [Microsoft 365 end user adoption guide](/office365/customlearning/champ_o365guide): Outlining methodology and resources for implementing proven adoption success factors
- [Posters, email templates](https://www.microsoft.com/fasttrack/resources): Customizable templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1): Video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec): Quick start training guides; get up and running quickly with the basic info you need to be productive right away
- [SharePoint video training](https://support.office.com/article/cb8ef501-84db-4427-ac77-ec2009fb8e23)
- [Work together with OneDrive](https://support.office.com/article/626cff9f-9a56-472b-a77d-b019d97eec8d)
- [Learn more about OneDrive](https://support.office.com/article/38acc14b-fd86-466e-b802-baece8107c86)

