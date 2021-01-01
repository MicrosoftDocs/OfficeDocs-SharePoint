---
title: "Migrate from My Sites to OneDrive in Office 365"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: "Learn how to evaluate the environment, prepare, and migrate content from My Sites to OneDrive in Microsoft 365."
---

# My Sites to OneDrive migration guide
This guide will help you prepare to migrate from My Sites to OneDrive in Microsoft 365.

Most migrations include these phases: planning, assessing and remediating, preparing the target environment, migrating and onboarding users.

![Migration process](media/migration-process.png)

|Migration planning|Assess and remediate|Prepare your OneDrive environment|Migrate|User onboarding|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs. sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Run SMAT<br><br>Assess key areas<br><br>Remediate issues|Pre-provision Microsoft 365 and users|Migration steps<br><br>Configure SharePoint hybrid<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Tell users how they're affected<br><br>Provide documentation for making the switch|

## Migration planning
Before you begin migration, assess your current source environment. What you discover will influence your overall strategy and timing, including:
- The mapping of content from your source My Sites to the destination OneDrive.
- The amount of content to migrate. Determine what content is redundant, out of date, or still relevant.
- Set permissions so IT can read/write from source to the target destination.
 
We strongly recommend that you consider setting up a hybrid environment. To learn more, see [SharePoint server hybrid configuration roadmaps](https://docs.microsoft.com/sharepoint/hybrid/configuration-roadmaps). 


### What migrates?

When you migrate to OneDrive by using the [SharePoint Migration Tool](https://docs.microsoft.com/sharepointmigration/introducing-the-sharepoint-migration-tool), you'll migrate content from your My Sites document library into OneDrive.

## Assess and remediate your content
Before you start your migration, it's important that you analyze your current environment. Only *you* know your data and how and who uses it. Think about how and what My Sites features you use in production.

An assessment can begin by working with your users in two main areas:
- Identify older content.
- Determine if content is obsolete or redundant and can be deleted.

## Using the SharePoint Migration Assessment Tool

The [SharePoint Migration Assessment Tool (SMAT)](https://docs.microsoft.com/sharepointmigration/overview-of-the-sharepoint-migration-assessment-tool) is a simple command-line executable that scans the contents of your SharePoint Server 2013 farm to help identify any issues before you migrate your content.
 
After the scan is complete, SMAT generates summary and detailed reports that identify areas that could affect your migration.

SMAT includes the SharePoint Migration Identity Management Tool, which does identity mapping by scanning SharePoint, Active Directory, and Azure Active Directory.  

SMAT scans many areas. Areas that are commonly of concern when migrating from My Sites are shown in the following table. Your environment isn't affected when SMAT performs its scan.

|Scan|Description|
|:-----|:-----|:-----|
|**File versions** |The more versions of a file you have, the longer it will take to migrate.<br/> Note: By default, versioning is enabled for all lists and libraries on the target platform. In the destination SharePoint site, there's no limit when versioning is enabled.</br></br>[See Migration assessment scan: File versions](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-file-versions)|
|**Large lists** |Lists of more than 20,000 items may cause     migration issues, making it more difficult to predict how long it takes to migrate sites. List data will still migrate, but the larger the list the more unpredictable the migration process. Extremely large lists can result in an extended migration.</br></br>[See Migration assessment scan: Large lists](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-large-lists)|
|**Long OneDrive URLs** |Content with long URLs that exceed a limit will be skipped.  They will not migrate.</br></br>[See Migration assessment scan: Long OneDrive URLs](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-long-onedrive-urls)|
|**Checked-out files** |Only checked-in content will be migrated. Make sure that users check in their files before migration to avoid data loss.</br></br>[See Migration assessment scan: Checked-out files](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-checked-out-files)|
|**Large Excel files** |If you try to open a file larger than 10 MB from OneDrive (online), you'll be prompted you to open the file in the Excel client.</br></br>[See Migration assessment scan: Large Excel files](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-large-excel-files)|
|**Large list views**|In your My Site, you can configure list-view throttling so the throttle on views is lifted during certain hours of the day. In OneDrive, the limit is in place around the clock. While your lists and data will still be migrated, some of your list views may be throttled.</br></br>[See Migration assessment scan: Large list views](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-large-list-views)|
|**Browser file handling**|SharePoint Server allows settings that range from "strict" to "permissive."  But in SharePoint and OneDrive in Microsoft 365, the "strict" setting is enforced and can't be modified. All data will be migrated, but the behavior with the HTM and HTML files will change from opening within the browser to prompting the user to download.</br></br>[See Migration assessment scan: Browser file handling](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-browser-file-handling)|
|**InfoPath** |InfoPath lets developers build custom forms to accept user input in various locations throughout SharePoint. Note that some features of custom InfoPath forms won't be migrated.</br></br>[See Migration assessment scan: InfoPath](https://docs.microsoft.com/sharepointmigration/migration-assessment-scan-infopath)|

## Prepare your OneDrive environment
Before you migrate your My Sites content, you must pre-provision your users in OneDrive:

- [Prepare to provision users through directory synchronization to Microsoft 365](https://support.office.com/article/prepare-to-provision-users-through-directory-synchronization-to-office-365-01920974-9e6f-4331-a370-13aea4e82b3e). Provisioning users with directory synchronization requires more planning and preparation than simply managing your work or school account directly in Microsoft 365. These additions ensure that your on-premises Active Directory synchronizes properly to Azure Active Directory.

- [Pre-provision OneDrive for users in your organization](https://support.office.com/article/ceef6623-f54f-404d-8ee3-3ce1e338db07).  
By default, the first time that a user browses to their OneDrive, it's automatically provisioned for them. In some cases, such as when your organization plans to migrate from your on-premises My Sites, you'll want your users' OneDrive locations ready beforehand (pre-provisioned).

- [Configure Microsoft 365 for SharePoint hybrid](https://docs.microsoft.com/sharepoint/hybrid/configure-office-365-for-sharepoint-hybrid) (optional). With SharePoint Server hybrid, productivity services in SharePoint in Microsoft 365 can be integrated with on-premises SharePoint Server to provide unified functionality and access to data. For enterprises that want to gradually move their existing on-premises SharePoint Server services to the cloud, SharePoint Server hybrid provides a staged migration path by extending high-impact SharePoint Server workloads to SharePoint.

A SharePoint Server hybrid environment enables trusted communication between SharePoint in Microsoft 365 and SharePoint Server. After you establish this trust framework, you can configure integrated functionality between services and features such as Search, Follow, and user profiles. You need to set up basic integration between Microsoft 365 for enterprises and SharePoint Server before you can configure a hybrid environment.

## Migrate

Use the [SharePoint Migration Tool](https://docs.microsoft.com/sharepointmigration/introducing-the-sharepoint-migration-tool) to easily migrate your existing My Sites to OneDrive.

1. **Install and launch the SharePoint Migration Tool.** You will select the bulk migration option using the .json or .csv file that you created. For details, see [Using the SharePoint Migration Tool](https://docs.microsoft.com/sharepointmigration/how-to-use-the-sharepoint-migration-tool).

2. **Create a mapping file.** Create a mapping file with source and target paths and save it as .csv. For details, see [How to format your JSON or CSV for data content migration](https://docs.microsoft.com/sharepointmigration/how-to-format-your-csv-file-for-data-content-migration).

## Migration best practices

The following information describes a typical migration process that follows Microsoft best-practices guidance.

1.  Select a small set of users for a pilot migration. The goals of the pilot are to validate the process, including performance and user communication, and to get a sample of user feedback.

1. Run the pilot migration. Use an incremental migration method that runs in the background with no user impact, followed by a cutover event in which users on-premises My Sites accounts are disabled. Direct users to the target OneDrive environment. This method is preferred, as it reduces user impact.

1. Assess the data from the pilot migration to determine the rest of your migration schedule, and make any changes. For example, you might update your user communication template to address questions you received from pilot users.

1. Do the rest of the migration. Use an incremental migration method, just like the pilot. We recommend a single cutover event for all users to switch to OneDrive and then disable their My Sites accounts. This approach helps eliminate any confusion resulting from users having to collaborate using both My Sites and OneDrive at the same time.

## User adoption

Develop a plan to prepare your users for the upcoming change. Consider these factors:

- **Evangelize the move:** Emphasize the benefits, collaborative capabilities, and reasons for the move.

- **End-user training:** Provide training to your users on the features in OneDrive.

- **Train your helpdesk:** Before the cutover, train your helpdesk in key features and common user questions.

- **Downtime:** Prepare for any possible downtime the migration may involve.

- **Communicate:** Develop a plan for sending communications to your users. Provide clear statements about timing, expectations, and impact to individuals.

- **Be public about the timeline:** Publish the migration timeline with details about user impacts. Include any user calls to action.

- **Reassure your users:** Assure users that content already in OneDrive is safe and won't be overwritten.

- **Opting out:** Tell users whether they can opt out of the migration process.

### Adoption-related resources

- [Microsoft 365 Adoption Guide](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE3cNVB): Outlines methodology and resources for implementing proven adoption success factors.
- [OneDrive Adoption](https://resources.techcommunity.microsoft.com/resources/onedrive-adoption/): This Resource Center will serve as your one stop shop for all adoption and change management-related content.


### Make the switch! 
The following articles can help your users "make the switch" from My Sites to OneDrive. They show how to do common tasks in OneDrive.

- [Upload and save files and folders to OneDrive](https://support.office.com/article/a5710114-6aeb-4bf5-a336-dffa7cc0b77a) 
- [Manage files and folders in OneDrive](https://support.office.com/article/20d7bb65-425a-4209-9b71-4cad046cfdc8)
- [Collaborate in OneDrive](https://support.office.com/article/d8a2a19a-e306-4ca5-9b00-19b0e96890d6)
- [Set up your mobile apps](https://support.office.com/article/51deb017-14c2-4f92-8b7a-f635aaa4eb3c)
- [Stay connected with OneDrive](https://support.office.com/article/829a8c87-713b-48ff-bfaa-54fa2c3b80d1)

## Advanced support

Your enterprise may have specific business needs that require you to use third-party services or applications to help with your migration to Microsoft 365. Explore the professional services and applications available from partners in the [Microsoft Partner Center](https://partnercenter.microsoft.com/partner/home).
