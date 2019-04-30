---
title: "MySites to OneDrive and SharePoint Migration Guide"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.custom: 
ms.assetid: 

---

# MySites to OneDrive Migration Guide
This guide will help you prepare to migrate from My Sites to OneDrive in Office 365.

Most migrations fall into regular phases as described below. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users.



![Migration process](media/migration-process.png)

|**Migration planning**|**Assess and remediate**|**Prepare your OneDrive environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs Sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Run SMAT<br><br>Assess key areas<br><br>Remediate issues|Pre-provision Office 365 and users|Migration steps<br><br>Configure SharePoint Hybrid<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted<br><br>Provide documentation for making the switch|

## Migration planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:
- The mapping of content from your source My Sites to the destination OneDrive.
- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
- Set permissions so IT can read/write from source to target destination
- We highly recommend that you consider setting up a hybrid environment.  Learn more:  [SharePoint and OneDrive Configuration Roadmaps](https://docs.microsoft.com/en-us/sharepoint/hybrid/configuration-roadmaps). 



### What migrates?

When you migrate to OneDrive using the [SharePoint Migration Tool (SPMT)](https://docs.microsoft.com/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool), you will be migrating your content stored in your MySites document library into OneDrive.




## Assess and remediate your content
Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. Think about how and what My Sites features you use in production.

An initial assessment can begin with working with your users in two main areas:
- Identify older content
- Determine if content is obsolete or redundant and can be deleted.


## Using the SharePoint Migration Assessment Tool (SMAT)

The [SharePoint Migration Assessment Tool (SMAT)](https://docs.microsoft.com/en-us/sharepointmigration/overview-of-the-sharepoint-migration-assessment-tool) is a simple command line executable that scans the contents of your SharePoint Server 2013 farm to help identify any issues before you migrate your content.
 
After the scan is complete, SMAT generates summary and detailed reports showing the areas that could impact your migration.

Also included is the  SharePoint Migration Identity Management Tool, that does identity mapping by scanning SharePoint, Active Directory, and Azure Active Directory.  

Your environment will not be impacted while SMAT performs a scan of your environment. SMAT scans many areas, but those commonly of concern when migrating from My Sites are:

|**Scan**|**Description**|
|:-----|:-----|:-----|
|**File Versions** |The more versions of a file you have, the longer it will take to migrate. Note: By default, versioning is enabled for all lists and libraries on the target platform. In the destination SPO site, there is no limit when versioning is enabled.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-file-versions)|
|**Large Lists** |Lists over 20,000 items have caused issues with migration, making it more difficult to predict how long it takes to migrate sites. List data is migrated, but the larger the list the more unpredictable the migration process has proven. Extremely large lists can result in an extended migration.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-large-list)|
|**Long OneDrive URLs** |Content with long URLs exceeding the limit will be skipped.  They will not migrate.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-long-onedrive-urls)|
|**Checked out files** |Only checked-in content will be migrated. Have users check in their files prior to migration to avoid data loss.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-checked-out-files)|
|**Large Excel Files** |If you attempt to open a file larger than 10MB from OneDrive (online), it will prompt you to open the file in the Excel client application.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-large-excel-files)|
|**Large List Views**|In your My Site, you can configure list view throttling so there are a set number of hours per day where the throttle on views is lifted. In OneDrive, the limit is in place continuously (24x7). While your lists and data will be migrated, some of your list views be throttled.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-large-list-views)|
|**Browser File Handling**|SharePoint Server allows you to set it from “strict” to “permissive”.  However, in SharePoint Online and OneDrive, the “strict” setting is enforced and can’t be modified.  Data will be migrated, but the behavior with the HTM and HTML files will change from opening within the browser to prompting the user to download.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-browser-file-handling)|
|**InfoPath** |InfoPath lets developers build custom forms for accepting user input in a variety of locations throughout SharePoint. However,certain features of custom InfoPath forms will not be migrated.</br></br>[Learn more](https://docs.microsoft.com/en-us/sharepointmigration/migration-assessment-scan-infopath)|




## Prepare your OneDrive environment
Before migrating your My Sites content, you must pre-provision your users in OneDrive: 

1. [Prepare to provision users through directory synchronization to Office 365](https://support.office.com/en-us/article/prepare-to-provision-users-through-directory-synchronization-to-office-365-01920974-9e6f-4331-a370-13aea4e82b3e).  Provisioning users with directory synchronization requires more planning and preparation than simply managing your work or school account directly in Office 365. The additional planning and preparation tasks are required to ensure that your on-premises Active Directory synchronizes properly to Azure Active Directory. 

2. [Pre-provision OneDrive for users in your organization](https://support.office.com/en-us/article/Pre-provision-OneDrive-for-users-in-your-organization-ceef6623-f54f-404d-8ee3-3ce1e338db07).  
By default, the first time that a user browses to their OneDrive it's automatically provisioned for them. In some cases, such as when your organization plans to migrate from your on-premises MySites, you want your users' OneDrive locations to be ready beforehand -- pre-provisioned.

3. [Configure Office 365 for SharePoint Hybrid](https://docs.microsoft.com/en-us/sharepoint/hybrid/configure-office-365-for-sharepoint-hybrid) (optional). With SharePoint Server hybrid, productivity services in SharePoint Online can be integrated with on-premises SharePoint Server to provide unified functionality and access to data. For enterprises that want to gradually move their existing on-premises SharePoint Server services to the cloud, SharePoint Server hybrid provides a staged migration path by extending high-impact SharePoint Server workloads to SharePoint Online. </br></br>A SharePoint Server hybrid environment enables trusted communications between SharePoint Online and SharePoint Server. When you have established this trust framework, you can configure integrated functionality between services and features such as Search, Follow, and user profiles. You will need to set up some basic integration between Office 365 for enterprises and SharePoint Server before you can configure a hybrid environment.




## Migrate

Use the [SharePoint Migration Tool (SPMT)](https://docs.microsoft.com/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool) as an easy way to migrate your existing My Sites to OneDrive. 

1. **Install and launch the SharePoint Migration Tool.** You will be selecting the bulk migration option using either the JSON or .CSV file you created. For detailed information on the SPMT and bulk migration see [How to use the SharePoint Migration Tool](https://docs.microsoft.com/en-us/sharepointmigration/how-to-use-the-sharepoint-migration-tool).

2. **Create a mapping file.** Create a mapping file with source and target paths and save it as a .csv file.  For detailed information see,  [How to format your JSON or CSV for data content migration](https://docs.microsoft.com/en-us/sharepointmigration/how-to-format-your-csv-file-for-data-content-migration).




## Migration best practices
Below is a typical migration process that follows Microsoft’s best practices guidance.
- Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.</br></br>

- Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which users on-premises My Sites accounts are disabled and they are directed to use the target OneDrive  environment. This method is preferred as it reduces user impact.</br></br>

- Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.</br></br>

- Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to OneDrive and disable their My Sites accounts. This approach helps to eliminate any confusion resulting from users having to collaborate using both My Sites and OneDrive at the same time.</br></br>

## User Adoption
Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:
- **Evangelize the move.** Underscore the benefits, the collaborative capabilities, and the reasons for making the move.</br></br>

- **End user training.** Provide training to your users on the features in OneDrive.</br></br>

- **Train your helpdesk.** Before the cutover, train your helpdesk in key features and common user questions.</br></br>

- **Downtime".** Prepare for any possible downtime the migration may incur.</br></br>

- **Communicate.** Develop a plan for sending communications to your user base, providing clear statements of timing, expectations and impact to the individual. </br></br>

- **Be public about the timeline.** Publish the migration timeline and how it will impact them. Include any end user calls to action.</br></br>

- **Reassure your users.** Assure them that if they have content already in OneDrive, that their content is safe and won’t be overwritten.</br></br>

- **Opting out**. Let them know whether individuals can opt-out of the migration process.</br></br>


### Adoption related resources
- [Microsoft 365 adoption guide](https://devfasttrackv4storage.blob.core.windows.net/marketing/en-us/resources/Microsoft%20365%20User%20Adoption%20Guide.pdf): Outlining methodology and resources for implementing proven adoption success factors
- [OneDrive Adoption resources](https://resources.techcommunity.microsoft.com/resources/onedrive-adoption/): This Resource Center will serve as your one stop shop for all adoption and change management related content.


### Make the switch! 
The following articles will help your users “make the switch” from My Sites to OneDrive. The topics show how you used to do common tasks in OneDrive.
- [Upload files to OneDrive](https://support.office.com/en-us/article/upload-files-to-onedrive-a5710114-6aeb-4bf5-a336-dffa7cc0b77a?ui=en-US&rs=en-US&ad=US) 
- [Manage folders in OneDrive](https://support.office.com/en-us/article/manage-folders-in-onedrive-20d7bb65-425a-4209-9b71-4cad046cfdc8?ui=en-US&rs=en-US&ad=US)
- [Collaborate in OneDrive](https://support.office.com/en-us/article/collaborate-in-onedrive-d8a2a19a-e306-4ca5-9b00-19b0e96890d6?ui=en-US&rs=en-US&ad=US)
- [Set up your mobile apps for OneDrive](https://support.office.com/en-us/article/set-up-your-mobile-apps-51deb017-14c2-4f92-8b7a-f635aaa4eb3c?ui=en-US&rs=en-US&ad=US)
- [Stay connect with OneDrive](https://support.office.com/en-us/article/stay-connected-with-onedrive-829a8c87-713b-48ff-bfaa-54fa2c3b80d1?ui=en-US&rs=en-US&ad=US)


## Advanced

### Migration offerings
Currently, migration offerings available to you include:


**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Office 365.  For more information see: [Microsoft Partner Center](https://partnercenter.microsoft.com/en-us/partner/home). 




