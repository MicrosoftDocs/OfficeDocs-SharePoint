---
ms.date: 10/30/2020
title: "Managed migration guide for use with Mover"
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
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: A guide to managing a migration project with the Mover migration tool.
---
# Managed migration guide using Mover


>[!Important]
>We have retired the legacy [Mover](https://app.mover.io) tool's ability for admin-led migrations from [Google Drive](mm-google-overview.md), [Dropbox](mm-dropbox-overview.md), [Box](mm-box-overview.md), and [Egnyte](mm-egnyte-overview.md). Please use [Migration Manager](https://aka.ms/ODSP-MM), located in the SharePoint admin center.
>
>*Ongoing migrations are not impacted by this change. However, you cannot create new connectors.* If you are currently in the middle of a Mover migration, you may continue using Mover until you finish your migration using your existing connectors. FastTrack led migrations are not impacted at this time.
>
>[**Individuals or students**: You may continue to use Mover, learn how!](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)
>
>[Learn more about the Mover.io retirement timeline](mover-retirement-timeline.md)

The Mover Migration tool is a Microsoft owned migration tool available at no cost to subscribers of Microsoft 365 with qualifying licenses. This guide was created to share the process and best practices of managing a cloud-to-cloud migration project using the Mover migration tool.

Most migrations fall into incremental phases. Proven success factors for migration include the following stages:

- Assessment & Planning
- Remediating
- Preparing your destination environment
- Migration
- Onboarding your users

> [!TIP]
> We highly recommend reading and reviewing the current Mover documentation. This content provides valuable knowledge on how to understand the Mover tool for running migrations from various cloud storage platforms.
> See [Mover migration content](./mover-plan-migration.md)

## Assess & Plan
Before beginning your migration, it's important you plan your outcome by doing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The design of the target environment and the mapping between source and destination.
  - Ensuring that all OneDrive users and SharePoint sites are provisioned.
  - Determine where to migrate your content. Content that is shared among many users is best migrated to SharePoint.  Content primarily owned and consumed by one user is best migrated to that user's OneDrive account
- Address large data owners and make informed decisions to split up this data and migrate into SharePoint sites.
- Ensure that you have provisioned adequate storage in the destination before migrating, especially when moving a large amount of data.

- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
- Understand the scope of your project, time restrictions, or deadlines
- Build your user onboarding into your upfront planning. Communicate early and often with your users about the migration and how it will impact them. Don't wait until the very end to start preparing them for the change.

Before beginning your migration, it is important that you perform an analysis of your current environment.

### Inventory scan

You or your customer might have a relative idea of how many users and files are in the source environment and which might be migrated. However, it is important to get an accurate count of the user base and files (including the size) by running an **Inventory Scan**. This scan will let you know how many users and files are in the source environment and help determine who owns the data. To learn more, see [Running a migration inventory scan with Mover.](mover-scan.md)

Using the results from your inventory scan, assess and remediate in the following areas:

|Scan result area|Assess|Remediate|
|---|---|---|
|**Data ownership**|How many users are in the domain and who owns the data|Most data will be shared data.  Only owned folders and the root files for each user is copied. If a user does not own any data, then consider excluding them from the migration.  Content that was shared with them will be migrated by the data owner then reshared to those users in the Destination during the migration process. Content can be automatically reshared after it is migrated so that each user has access to their content exactly as before. |
|**Data distribution**|Find all accounts that exceed 100,000 files or with items greater than 1 TB.|Split these accounts into smaller service accounts. Users with large data sets must be broken into smaller accounts to facilitate faster transfers. To learn more, see [Migration performance optimizations](#migration-performance-optimization). |
|**File and folder path length**|Find all items whose path exceeds the file path length described here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)|Work with your customer to reorganize the file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|
|**Size and number of files/data**|Get an accurate count of the number of files and data size.|This number will be the most accurate, as it will not include items in the trash, or externally shared data. Do not rely on your cloud provider's reporting to give you an accurate picture. Use this information to more clearly define migration timeline and length of time required for the migration.|

> [!IMPORTANT]
> The Mover tool only copies files/folders/data owned by users within the source tenant. The tool does NOT migrate external shared data, email or items residing in the trash.
>
> **External Shared data** - The external owner of that data will need to re-share that data.
>
> **Email** - The Mover tool does not migrate email. For help finding a service that migrates email, see [FastTrack migrations](/fasttrack/data-migration#migration-to-exchange-online)
>
> **Trash** - Customer should communicate to their user base that items in the trash can not be moved and to ensure they check items in trash and if needed reclaim from trash for migration.

### Interpreting Scan Results for Final Delta/Cutover Events

 You or your customer might have a relative idea of how many items and users are in their source domain and how many they might want to migrate. However, it is essential to get an accurate count of your total items/number of users by running an Inventory Scan. This scan will let you know how many items/users are in the domain and help determine who owns the data. To learn more, see [Running a migration inventory scan with Mover](/sharepointmigration/mover-scan).

 Another critical fundamental of running the Inventory Scan is determining the viability of completing a Final Delta or Cutover pass before letting your users start using their OneDrive accounts and SharePoint sites when they switch over to using Microsoft 365.

For migrations, there are two key stages to consider.

- **Migration Sync**. This is where you run the migration, and most of your content is migrated on the first or subsequent passes.  These passes can vary from 1 to many, depending on the amount of content migrated, remediation of failed users, failed files, or new users added during the migration.
- **Final Delta/Cutover**. Once the Migration Sync passes are complete, it is prudent to run a Final Delta/Cutover event.  A final delta cutover event ensures that any new or modified Source content is migrated and that all current content is available for Microsoft 365 users.
Final Delta/Cutover events are typically run over a weekend when your tenant tends to be quieter than the standard working week. It allows time to prepare for users starting to use Microsoft 365 on the Monday after the cutover.

You can use the Scan Results for large migrations to evaluate how many items/users you have to migrate and determine if a single weekend cutover event will complete in the required timeframe.

Currently, the estimated upper limits for completing a Final Delta/Cutover event from Friday to Monday is approximately 100 to 150 million files or 12,000 - 15,000 users.

If your file or user count exceeds these limits, planning should be set early in the migration to address how best to perform the Final Delta/Cutover.

Our recommendation is to split your users by either GEO Region (APAC, EMEA, AMER) or even by Department (HR, IT, Sales etc.) and schedule multiple cutover events to ensure that each Region or Department is completed before the Monday deadline.

You can use the Tagging feature on the Migration tools to help identify by Region or Department and use the Filtering options to help plan, run, and monitor their progress.

### Scope and timeline

The most common question from customers is "How long will the migration take?". While the Mover tool is one of the fastest ways to migrate data, the migration speed can be impacted by many factors, including:

- Number of files and folders being moved
- File size
- Total amount of data being moved
- Server connections with the source or destination
- Both source and destination connectors have rate limits. We are constrained to how fast they allow us to download, upload, and process data between the two.
- Complexity of permissions or sharing of data: Applying permissions as part of the migration is another factor that can influence speed. When permissions are applied, we are again making numerous API calls that will increase the time it takes to migrate the data.

Mapping out timelines and setting expectations of what can be achieved with those timelines is essential to managing a successful migration project.

Budgeting for ample time for planning and assessing will ensure a smoother migration. One of the benefits of migrating via the Mover tool is that we only take a copy of the source data and upload that to the Destination. This allows the users to continue to work in their source files while we copy their data for them, allowing the migration to run in parallel with minimal distribution of the customers' daily activities.

The only time users need to refrain from creating new content is during the final delta.

### Communication

A migration is a significant undertaking for any customer. Trying to grasp the entire extent of all data and communicating with the users within the organization is complicated.

Before, during, and after a migration, it is critical to communicate clearly and effectively with your user base.

**Management**. Management needs concise information about the how's and why's of the migration, including the benefits and expectations. Communicate what a successful migration looks like.
**Users**. They need to know when changes are taking place, and who to go to with questions or issues.
**IT Helpdesk/Support staff**. If your organization is large enough to have specific support staff for other employees, they must understand each step of the migration and be able to troubleshoot questions that arise.

## Prepare your environment

We recommend the following best practices as you prepare your environment.

|What|Action notes|
|---|---|
|**Source connectors**|Each source has a specific process and caveats to be aware of when authoring and creating your connector. Learn more about your source connector here: [Setup your source](./mover-box.md) |
|**Account setup** |As manager of the project, retain ownership of the migration account.  This ensures that only those running the migration have control of the migration, including running, monitoring, and maintaining the migration. |
|**Disable mail notifications**|Disable all migration notification emails to avoid getting spammed.  Otherwise, you and your customers will receive test emails regarding transfers, failures, progress, etc.  Learn more: [Disable email notifications](./mover-disable-emails.md)|
|**Destination upload folder**|Map an upload/destination folder for uploading the migrated data.|
|**Review important general considerations**|Make sure to review how the tool handles what gets transferred, synced, permissions, and other best practices here: [Mover Migration FAQ](./mover-migration-faq.md)

## Migration performance optimization

Many factors determine how long a migration might take. It is not an exact science, but one of the basic rules of thumb is that it moves one file per second on average. If a customer has 1 million files, it will take 1 million seconds to migrate, which equates to roughly 12 days.

The tool will migrate as fast as possible, but performance can be impacted by:

- The distribution of the data - If you have many users who own a large number of files, the migration will take longer to complete.
- The state of both the source and destination servers; how fast they can download and upload the data.
- The size of the files. Large files will migrate quicker than large number of small files, as fewer files make less API calls.
- Time of day. Schedule migrations outside of standard office hours to allow more data to migrate quicker.  Source and Destination tenants tend to be quieter when there is less daily user usage.

The more users simultaneously being transferred, the higher our throughput for your migration. Users with large data sets should be broken into smaller accounts to facilitate faster transfers.

> [!IMPORTANT]
> To maximize throughput, **users should not own greater than 100,000 items or 1 TB of data**. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds.

**Examples**:

|Size|Action|
|---|---|
|If a user owns more than 400,000 items|Divide the items between four users each with 100,000 items.|
|If a user owns more than 5 TB of data|Divide between five users so that each user owns 1 TB.|

To create Service Accounts, you can work with your Source Cloud Storage Admin to carry out the following steps:

1. Once you have identified a large user determine how many Service Accounts will be required (see example above).
2. Create the Service Accounts and assign them a license.
3. From the original large user, identify the folder(s) you would like to assign to the Service Account.
4. Change the ownership of said folder(s) to the new Service Account. This may require that the original owner first share it with the new owner, and the new owner accept. The original owner will then have the option to select them as owner.
5. When it comes to migrating the Service Account, create a corresponding OneDrive user/SharePoint site to migrate the new Service Account content to.

When mapping please ensure that each Service Account has its own unique matching Destination account to optimize performance.

|Source Path|Destination Path|
|---|---|
|originaluser@contoso.com |originaluser@contoso.com/[upload folder]\*|
|serviceaccount1@contoso.com |serviceaccount1@contoso.com/[upload folder]\*|
|serviceaccount2@contoso.com | serviceaccount2@contoso.com/[upload folder]\*|
|serviceaccount3@contoso.com |serviceaccount3@contoso.com/[upload folder]\*|

Asterisk (\*) = optional folder

## Migration process

Below is a typical migration process that follows Microsoft's best practices guidance.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.

   Best practices for Pilot migrations:

   - Select a small subset of users (between 10 –50)
   - Selected users own a small amount of total data (max of about 2 TB). This ensures that the Pilot Migration won't take too long to complete.
   - Include a mix of users migrating into both OneDrive and SharePoint to demonstrate how the data will appear in both locations after migration.

2. Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which network file shares and local file shares are disabled and they are directed to use the Microsoft 365 environment. This method is preferred as it reduces user impact.

3. Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.

4. Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to using their OneDrive accounts and SharePoint sites. This helps eliminate users from updating duplicate copies of content.

5. Provide regular (daily) reporting to key stakeholders with a migration report that captures all transfers and their current status.

6. Once your migration completes, have a team ready to help with user adoption and onboarding for a smooth transition into Microsoft 365.

## User Onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:

- **Evangelize the move.** Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training.**  Provide training to your users on the features in OneDrive.
- **Train your helpdesk.**  Before the cutover, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime** the migration may incur.

Develop a plan for sending communications to your user base, providing clear statements of timing, and expectations and impact to the individual, including:

- The migration timeline and how it will impact them. Include any user calls to action.
- Assure them that their content is safe and won't be overwritten.
- Let them know whether individuals can opt out of the migration process.

### Onboarding related resources

- [Microsoft 365 end user adoption guide](https://adoption.microsoft.com/): Outlining methodology and resources for implementing proven adoption success factors
- [Microsoft 365 adoption resources](https://www.microsoft.com/fasttrack/resources): including customizable posters and templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1) video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec) Quick start training guides: get up and running quickly with the basic info you need to be productive right away
- [Microsoft 365 Learning Pathways:](/office365/customlearning/) customizable product training experience for end user readiness

