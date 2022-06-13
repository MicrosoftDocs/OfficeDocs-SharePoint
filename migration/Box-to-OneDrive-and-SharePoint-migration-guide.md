---
title: "Box to OneDrive Migration Guide"
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
description: "Learn how to evaluate the environment, prepare, and migrate content from Box to OneDrive work or school accounts in Microsoft 365."
---

# Box to OneDrive Migration Guide

This guide helps you prepare to migrate from Box to OneDrive in Microsoft 365.

Most migrations fall into regular phases. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users.

![Migration process](media/migration-process.png)

|Migration planning|Assess and remediate|Prepare your OneDrive environment|Migrate|User onboarding|
|---|---|---|---|---|
|What content goes where<br><br>Understanding permissions vs Sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Analyze Box admin reports<br><br>Assess key areas<br><br>Remediate issues|Pre-provision Microsoft 365 and users|Review migration offerings<br><br>Microsoft FastTrack services<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted<br><br>Provide documentation for making the switch|

## Migration planning

Before beginning your migration, it's important to plan your outcome. To do this, perform an assessment of your current source environment. What you discover influences your overall strategy and timing, including:

- The design of the target environment and the mapping between source and target systems.
- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
- Build your user onboarding into your upfront planning. Communicate early and often with your users about the migration and how it will impact them. Don't wait until the very end to start preparing them for the change.

### What content goes where

Consider how you use the content in your Box accounts today and plan how to transition to Microsoft 365 for a more collaborative experience.

Does the file belong to me alone, even though I might share it with others? If so, save it in your OneDrive personal library. Your personal library is private by default, but you can share files with others, which is particularly useful if you aren't working as a team yet.

If you're working on a file intended for team consumption and collaboration, use OneDrive to save it to a **shared library** where team members have access by default. OneDrive gives you access to all your shared libraries in Microsoft Teams, SharePoint or Outlook. When you need a new shared library for team files, you can create one right from OneDrive, add members, and start working together.

![Sharing](media/Migration-WhatGoesWhere-Box-to-ODSP-520x.png)

### Understanding permissions vs sharing

How you share your files dictates how they appear in the **Shared with Me** view in OneDrive. **Shared with Me** includes:

- Files and folders that someone shared with you via OneDrive (they selected **Share**, and entered your name or email address).
- Files and folders that you have opened from a shared location.

The following table maps your current Box sharing experience with OneDrive.

|Box|OneDrive|
|---|---|
|Folders or file with only one owner, but more than one contributor|As the owner, content should be migrated to the user's OneDrive personal library.<br><br>For any user who has access to a user's folder, that folder automatically appears in their **Shared with Me** list.|
|Only one owner, but shared with a Box group|As the owner, content is migrated to the user's OneDrive personal library. <br><br>The Box group should be converted to a security group. <br><br>Email should then be sent to the new security group, where each user can accept the invitation link. Content then appears in those users' **Shared with Me** lists.|
|Folders or file with multiple owners (co-admin in Box)|Content should be migrated to the appropriate shared library.<br><br>For any user who has access to the shared library and follows the associated SharePoint team site, the SharePoint team site appears on the left side navigation of OneDrive on the web.|
|Box folders with contributors who are external to your organization|For prescriptive guidance, see the specific External Permission Best Practice section in this document. <br><br>**Note:** Content that's shared with a user from another company's Box instance won't be migrated. If the user still wants to retain that content, their Box account needs to remain active.|
|**Shared with** Box end user experience|Only content that's been explicitly shared with a user appears in their **Shared with Me** view in OneDrive. <br><br>For content that's stored in shared libraries, the team site appears on the left side of the OneDrive view for users who have access to the team site.|

## Assess and remediate your content

Before you start your migration, it's important to perform an analysis of your current environment. Only you know your data and how and who uses it. Think about how and what Box features you use in production.

All of the following recommended assessments can be performed using Box's Folders and Files admin report. Run this report and use its results to perform these assessments. Remediate your content on the source before beginning your migration to save time and effort later.

|&nbsp;|Assess|Remediate|
|---|---|---|
|**File extensions**|Find all files in the Folders and Files report whose Path ends in one of the extensions defined here: [Types of files that cannot be added to a list or library](https://support.office.com/article/30BE234D-E551-4C2A-8DE8-F8546FFBF5B3)|If the blocked file types are scripting files, they're blocked because scripting capabilities are turned off by default in OneDrive. <br><br>If you want to allow these file types, turn on scripting capabilities as described here: [Allow or prevent custom script](/sharepoint/allow-or-prevent-custom-script). <br><br>Make sure you understand why these files are blocked by default as described here: [Security considerations of allowing custom script](/sharepoint/security-considerations-of-allowing-custom-script)|
|**File and folder name characters**|Find all items in the Folders and Files report whose name contains any of the characters detailed here: [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)|Work with your migration vendor to substitute these characters in all file and folder names.<br><br>**Note:** The # and % characters are supported but not enabled by default. Follow these steps to enable them: [New support for # and % in SharePoint and OneDrive](https://techcommunity.microsoft.com/t5/Microsoft-SharePoint-Blog/New-support-for-and-in-SharePoint-Online-and-OneDrive-for/ba-p/60357)|
|**File and folder path length**|Find all items in the Folders and Files report whose path exceeds the file path length described here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)|Work with your migration vendor to reorganize your file and folder structure such that it doesn't exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives might help here.|
|**Large drives and complex sharing**|Scan for any drives that have a very large amount of content, or many different unique sharing permissions – this is usually a sign that the drive should be broken down into smaller, more focused sites. <br><br>Specifically, any drive that has more than 50,000 documents shared with different users must be broken up. Use Box's Folders and Files report and Shared Links report to identify such drives.|Identify sets of content within these drives that are conceptually similar (like same project area or all shared with the same users). Move these sets of content out and into new drives before you start the migration.|

## Prepare your OneDrive environment

Before you migrate your Box content, you must pre-provision your users in OneDrive. For guidance on pre-provisioning, see:

- [Prepare to provision users through directory synchronization to Microsoft 365](/office365/enterprise/prepare-for-directory-synchronization)
- [Pre-provision OneDrive for users in your organization](/onedrive/pre-provision-accounts)

## Migrate

### Migration process

The following is a typical migration process that follows Microsoft's best practices guidance:

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.

2. Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cut-over event in which users' Box accounts are disabled and the users are directed to use the target OneDrive environment. This method is preferred because it reduces user impact.

3. Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you might update your user communication template to address a question that you received from a pilot user.

4. Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cut-over event for all users to switch to OneDrive and disable their Box accounts. This approach helps to eliminate any confusion that results from users collaborating using both Box and OneDrive at the same time.

   > [!NOTE]
   > Box has rate limiting in effect, which might impact the scheduling of your migration. Work with your migration provider to understand how these limits affect your migration.

### Migration offerings

Currently, there are a variety of migration offerings available to you. They include:

#### Microsoft FastTrack

FastTrack is a Microsoft service that's included in your subscription cost. It provides a set of best practices, tools, resources, and experts committed to making your experience with the Microsoft Cloud a great one. OneDrive onboarding guidance, migration benefits, and adoption guidance are included in the benefit offering.

Onboarding guidance includes help to:

- Discover what's possible.
- Create a plan for success.
- Onboard new users and capabilities at a flexible pace.

The [Data Migration](/fasttrack/O365-data-migration) benefit covers guidance on migrating content from file share, Box, or Google Drive source environments.

This guidance covers enablement of both OneDrive and the source environment. FastTrack also performs specific data migration activities on behalf of the customer for those with 500 or more licenses. For more info, see [FastTrack Center Benefit Overview](/fasttrack/O365-data-migration). Interested in getting started? Visit [FastTrack.microsoft.com](https://fasttrack.microsoft.com/), review resources, and submit a Request for Assistance.

#### Migration service providers

You might decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications that are available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Microsoft 365. For more info, see [Microsoft Partner Center](https://partnercenter.microsoft.com/partner/home).

## User onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:

- **Evangelize the move**. Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End-user training**. Provide training to your users on the features in OneDrive.
- **Train your helpdesk**. Before the cut-over event, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime**. Have a plan for possible downtime that might occur during the migration.

 Develop a plan for sending communications to your user base. Provide clear statements of timing, expectations, and impact to individuals. Consideration factors:

- The migration timeline and how it will impact them. Include any user calls to action.
- Assure them that if they already have content in OneDrive, their content is safe and won't be overwritten.
- Let them know whether individuals can opt out of the migration process.

### Onboarding related resources

- [Microsoft 365 adoption guide](https://go.microsoft.com/fwlink/p/?LinkID=2003460): Outlining methodology and resources for implementing proven adoption success factors
- [Posters, email templates](https://www.microsoft.com/fasttrack/resources): Customizable templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1): Video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec): Quick start training guides; get up and running quickly with the basic info you need to be productive right away.

### Make the switch!

The following articles will help your users "make the switch" from Box to OneDrive. The topics show how you used to do common tasks in Box and how you do the same in OneDrive.

- [Switch to OneDrive from Box](https://support.office.com/article/b7f3c899-edb7-44ab-bc3f-0a37e9f1a7fa)
- [Open with OneDrive](https://support.office.com/article/c24d1cef-dddb-43b9-929b-45b571b84990)
- [Store with OneDrive](https://support.office.com/article/7be433cd-d95b-46d8-9e8e-a1e32ecc4724)
- [Work together with OneDrive](https://support.office.com/article/626cff9f-9a56-472b-a77d-b019d97eec8d)
- [Learn more about OneDrive](https://support.office.com/article/38acc14b-fd86-466e-b802-baece8107c86)

## Advanced

### Permissions and roles

There's an important distinction between permissions and sharing.

**Permissions** determine the level of access a user has to content – whether they can view, edit, or have no access at all. Generally, users have *permissions* to a lot of content (your company portals, for example), but have had much less content explicitly *shared* with them. Permissions for both services are defined by assigned roles.  The following table maps your current Box roles with OneDrive:

| Box roles | OneDrive roles |
|:-----|:-----|
|Co-owner|Contributor|
|Editor|Contributor|
|Viewer Uploader|Viewer|
|Previewer Uploader|None|
|Viewer|Viewer|
|Previewer|None|
|Uploader|None|

### External permission best practices

We recommend *not* handling external sharing during the act of migration. Instead, assess existing external sharing content, and then re-share post migration per the following guidelines:

- Audit external permissions on the Box content source using the Collaborations report (generated through the Box Admin Console).

- Determine whether that content is worthy to remain externally shared.

- If you decide the content is to remain externally shared, determine whether that content is suited for OneDrive personal libraries or shared libraries based on the *"What content goes where"* previous guidance.

- For **OneDrive** personal libraries: re-share files externally with the appropriate external users after the migration.

- For **Shared libraries**:

  - Where possible, leverage the collaboration and security benefits of grouping content that's specific to external partners in a dedicated SharePoint team site. For more info, see [Use SharePoint as a business-to-business (B2B) extranet solution](/sharepoint/create-b2b-extranet).

  - If content can't be grouped as such, externally re-share on the file or folder level in the target team library.
