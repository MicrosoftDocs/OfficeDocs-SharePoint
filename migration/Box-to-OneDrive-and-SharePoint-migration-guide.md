---
title: "Box to OneDrive and SharePoint Migration Guide"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 6/18/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ROBOTS: NOINDEX
ROBOTS: NOFOLLOW
ms.custom: 
ms.assetid: 

---

# Box to OneDrive and SharePoint Migration Guide
This guide will help you prepare to migrate from Box to OneDrive and SharePoint in Office 365.

Most migrations fall into regular phases as described below.  Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users. 

![SharePoint Migration Tool](media/Migration-process.png)

|**Migration Planning**|**Assess and remediate**|**Prepare your OneDrive and SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs Sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Analyze Box admin reports<br><br>Assess key areas<br><br>Remediate issues|Pre-provision Office 365 and users|Review migration offerings<br><br>Microsoft FastTrack services<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted<br><br>Provide documentation for making the switch|

## Planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:
- The design of the target OneDrive and SharePoint environment and the mapping between source and target systems. 
- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.


## What content goes where
Consider how you use the content in your Box accounts today and plan how to transition to the improved Office 365 collaborative experience. 

Let’s first review the benefits that OneDrive and SharePoint provide to understand how each can best serve your needs. 

- **OneDrive** is personal online storage space in the cloud.  Use it to store and protect your work files while accessing them across multiple devices with ease.  OneDrive files are private by default, but you do have the ability to share files and folders inside and outside your organization.

- A **SharePoint team site** is a place that users can collaborate on files, documents, and ideas. It is set up to facilitate two-way communication between team members and offers a full range of features to help a team communicate and collaborate.


Storing your content in OneDrive and SharePoint allows you to easily share files inside and outside your organization and collaborate on Office documents together in real time with the latest Office desktop, web, and mobile apps.

Additionally, you can use OneDrive on the web, mobile or desktop sync client on PC and Mac to access all your files in Office 365.

Knowing the capabilities of OneDrive and SharePoint, look at the following table to help you determine what content goes where:<br><br>


|**Ask...**|**OneDrive**|**SharePoint**|
|:-----|:-----|:-----|
|Does the file belong to me alone, even though I might share it with others?|X||
|Is this a file you want to keep private for the time being?|X||
|Does this file/content belong to a larger group, such as project team, department, or division?||X|
|Does this content need to be managed by a workflow?||X|
|Do you need to manage metadata on this content?||X|
|Is this a set of like content that regularly needs to be shared outside your organization?||X|
|Do you have governance policies (records management, etc) that control this content?||X|

## Permissions and sharing

There is an important distinction between permissions and sharing. 

**Permissions** determine the level of access a user has to content – whether they can view, edit, or have no access at all. 

Generally, users have *permissions* to a lot of content (your company portals, for example), but have had much less content explicitly *shared* with them. 

Permissions for both services are defined by assigned roles.  The following table maps your current Box roles with OneDrive and SharePoint:

|**Box Roles**|**OneDrive or SharePoint Roles**|
|:-----|:-----|
|Co-owner|Contributor|
|Editor|Contributor|
|Viewer Uploader|Viewer|
|Previewer Uploader|None|
|Viewer|Viewer|
|Previewer|None|
|Uploader|None|


**Sharing** is an explicit action a user takes to invite another user to collaborate on content. Sharing content implicitly gives that user permission to edit the content as well. Only content that has been explicitly shared with a user (or a group to which they belong) will appear in their **Shared with Me** view in OneDrive.
The following table maps your current Box sharing experience with OneDrive or SharePoint.

|**Box**|**OneDrive and SharePoint**|
|:-----|:-----|
|Folders or file with only one owner, but more than one contributor|As the owner, content should be migrated to the user's OneDrive folder.<br><br>Any user who has access to a user's folder will have that folder automatically appear in their **Shared with Me** list.|
|Only one owner, but shared with a Box group|As the owner, content will be migrated to the user's OneDrive folder. <br><br>The Box group should be converted to a security group.  <br><br>Email should then be sent to the new security group, where each user can accept the invitation link. Content will then appear in those users **Shared with Me** list.|
|Folders or file with multiple owners (co-admin in Box)|Content should be migrated to the appropriate SharePoint team site.<br><br>Any user who has access to the team site and follows the team site, will have the team site appear on the left side of their OneDrive view.| 
|Box folders with contributors who are external to your organization|For prescriptive guidance see the specific External Permission Best Practice section in this document. <br><br>**Note:**  Any content that is shared with a user from another company’s Box instance won’t be migrated.  If the user still wants to retain that content – their Box account will need to remain active.|
|**Shared with** Box end user experience|Only content that has been explicitly shared with a user will appear in their **Shared with Me** view in OneDrive. <br><br>For content stored in SharePoint: any user who has access to the team site and follows the team site, will have the team site appear on the left side of their OneDrive view.|

## External permission Best Practices

Microsoft’s recommendation is to not handle external sharing during the act of migration. Rather, assess existing external sharing content and then reshare post migration per the following guidelines: 
 
- Audit external permissions on the Box content source using the Collaborations report (generated through the Box Admin Console)
- Determine whether that content is worthy to remain externally shared
- If you decide the content is to remain externally shared, determine whether that content is suited for OneDrive or SharePoint based on the What content goes where above guidance
- For **OneDrive**: reshare files externally with the appropriate external users after the migration  
- For **SharePoint**:<br> 
    - Where possible, leverage the collaboration and security benefits of grouping external partner specific content in a dedicated SharePoint team site. Read more details here: [Use Office 365 SharePoint Online as a business-to-business (B2B) extranet solution](https://support.office.com/en-us/article/Use-Office-365-SharePoint-Online-as-a-business-to-business-B2B-extranet-solution-7b087413-165a-4e94-8871-4393e0b9c037).<br>
    - If content cannot be grouped as such, then externally reshare on the file or folder level in the target SharePoint team site. 





## Prepare your OneDrive and SharePoint Online environment

Before migrating your Box content, you must pre-provision your users in OneDrive and SharePoint Online For guidance on pre-provisioning see: 
- [Prepare to provision users through directory synchronization to Office 365](https://support.office.com/en-us/article/prepare-to-provision-users-through-directory-synchronization-to-office-365-01920974-9e6f-4331-a370-13aea4e82b3e)
- [Pre-provision OneDrive for users in your organization](https://support.office.com/en-us/article/Pre-provision-OneDrive-for-users-in-your-organization-ceef6623-f54f-404d-8ee3-3ce1e338db07)



## Assess and remediate your content
Before beginning your migration, it is important that you perform an analysis of your current environment.  Only you know your data and how and who uses it.  Think about how and what Box features you use in production.
 
All of following recommended assessments can be performed using Box’s Folders and Files admin report. Run this report and use its results to perform these assessments. Remediate your content on the source before beginning your migration to save time and effort later.

| |**Assess**|**Remediate**|
|:-----|:-----|:-----|
|**File extensions**|Find all files in the Folders and Files report whose Path ends in one of the extensions defined here: [Types of files that cannot be added to a list or library](https://support.office.com/en-us/article/Types-of-files-that-cannot-be-added-to-a-list-or-library-30BE234D-E551-4C2A-8DE8-F8546FFBF5B3)|If the blocked file types are scripting files, they are blocked because scripting capabilities are turned off by default in OneDrive and SharePoint. <br><br>If you want to allow these file types, turn on scripting capabilities as described here: [Allow or prevent custom script](https://support.office.com/en-us/article/allow-or-prevent-custom-script-1f2c515f-5d7e-448a-9fd7-835da935584f?ui=en-US&rs=en-001&ad=US). <br><br>Make sure you understand why these files are blocked by default as described here: [Security considerations of allowing custom script](https://support.office.com/en-us/article/security-considerations-of-allowing-custom-script-b0420ab0-aff2-4bbc-bf5e-03de9719627c)|
|**File and folder name characters**|Find all items in the Folders and Files report whose name contains any of the characters detailed here: [Restrictions and limitations when you sync SharePoint libraries to your computer through OneDrive](https://support.microsoft.com/en-us/help/2933738/restrictions-and-limitations-when-you-sync-sharepoint-libraries-to-you)|Work with your migration vendor to substitute these characters in all file and folder names.<br><br>**Note:** The # and % characters are supported but not enabled by default. Follow these steps to enable them: [New support for # and % in SharePoint Online and OneDrive](https://techcommunity.microsoft.com/t5/Microsoft-SharePoint-Blog/New-support-for-and-in-SharePoint-Online-and-OneDrive-for/ba-p/60357)|
|**File and folder path length**|Find all items in the *Folders and Files* report whose Path exceeds the file path length described here: [SharePoint Online limits](https://support.office.com/en-us/article/SharePoint-Online-limits-8f34ff47-b749-408b-abc0-b605e1f6d498)|Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|
|**Large drives and complex sharing**|Scan for any drives that have a very large amount of content, or many different unique sharing permissions – this is usually a sign that the drive should be broken down into smaller, more focused sites. <br><br>Specifically, any drive that has more than 50,000 documents shared with different users must be broken up. Use Box’s Folders and Files report and Shared Links report to identify such drives.|Identify sets of content within these drives that are conceptually similar (same project area, all shared with the same users, etc). Move these sets of content out and into new drives before starting migration.|
## Migrate

### Migration process
Below is a typical migration process that follows Microsoft’s best practices guidance.
1.	Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.<br><br>
2.	Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which users Box accounts are disabled and they are directed to use the target OneDrive and SharePoint environment. This method is preferred as it reduces user impact.<br><br>
3.	Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.<br><br>
4.	Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to OneDrive and disable their Box accounts. This approach helps to eliminate any confusion resulting from users having to collaborate using both Box and OneDrive and SharePoint at the same time.<br><br>
>[!NOTE]
>Box has rate limiting in effect, which may impact the scheduling of your migration. Work with your migration provider to understand how these limits affect your migration.


### Migration offerings
Currently, there are a variety of migration offerings available to you. They include:

**Microsoft FastTrack**

FastTrack is a Microsoft service included in your subscription cost that provides you with a set of best practices, tools, resources, and experts committed to making your experience with the Microsoft Cloud a great one. OneDrive onboarding guidance, migration benefits, and adoption guidance are included in the benefit offering. 

Onboarding guidance includes: help to discover what’s possible, creating a plan for success, and onboarding new users and capabilities at a flexible pace. The [Data Migration](https://technet.microsoft.com/library/mt651702.aspx) benefit covers guidance on migrating content from file share, Box, or Google Drive source environments. 

This guidance covers enablement of both OneDrive for Business and the source environment. FastTrack will also perform specific data migration activities on behalf of the customer for those with 500 or more licenses. See more details in the provided [FastTrack Center Benefit Overview](https://technet.microsoft.com/library/mt651702.aspx). Interested in getting started? Visit [FastTrack.microsoft.com](https://fasttrack.microsoft.com/), review resources, and submit a Request for Assistance.

**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Office 365.  For more information see: [Microsoft Partner Center](https://partnercenter.microsoft.com/en-us/partner/home). 
 
## User Adoption
Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan: 
- **Evangelize the move.** Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training.**  Provide training to your users on the features in OneDrive and SharePoint Online.
- **Train your helpdesk.**  Before the cutover, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime** the migration may incur.
  
 Develop a plan for sending communications to your user base, providing clear statements of timing, expectations and impact to the individual. Consideration factors:

- The migration timeline and how it will impact them. Include any end user calls to action. 
- Assure them that if they have content already in OneDrive or SharePoint, that their content is safe and won’t be overwritten. 
- Let them know whether individuals can opt-out of the migration process

### Adoption related resources
- [Microsoft 365 adoption guide](https://devfasttrackv4storage.blob.core.windows.net/marketing/en-us/resources/Microsoft%20365%20User%20Adoption%20Guide.pdf): Outlining methodology and resources for implementing proven adoption success factors
- [Posters, email templates](https://fasttrack.microsoft.com/microsoft365/resourcehub): customizable templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/en-us/article/onedrive-video-training-1f608184-b7e6-43ca-8753-2ff679203132?ocmsassetID=1f608184-b7e6-43ca-8753-2ff679203132&ui=en-US&rs=en-US&ad=US) and [SharePoint](https://support.office.com/en-us/article/sharepoint-online-video-training-cb8ef501-84db-4427-ac77-ec2009fb8e23?ui=en-US&rs=en-US&ad=US) video training
- [OneDrive](https://support.office.com/en-us/article/upload-files-to-onedrive-for-business-a1397e56-61ec-4ed2-9dac-727bf8ac3357?ui=en-US&rs=en-US&ad=US) and [SharePoint](https://support.office.com/en-us/article/sign-in-to-sharepoint-online-324a89ec-e77b-4475-b64a-13a0c14c45ec?ui=en-US&rs=en-US&ad=US) Quick start training guides: get up and running quickly with the basic info you need to be productive right away 

### Make the Switch! 
The following articles will help your users “make the switch” from Box to OneDrive. The topics show how you used to do common tasks in Box and how you do the same in OneDrive.

- [Switch to OneDrive from Box](https://support.office.com/en-us/article/Switch-to-OneDrive-from-Box-b7f3c899-edb7-44ab-bc3f-0a37e9f1a7fa)
- [Open with OneDrive](https://support.office.com/en-us/article/open-with-onedrive-c24d1cef-dddb-43b9-929b-45b571b84990?ui=en-US&rs=en-US&ad=US)
- [Store with OneDrive](https://support.office.com/en-us/article/store-with-onedrive-7be433cd-d95b-46d8-9e8e-a1e32ecc4724?ui=en-US&rs=en-US&ad=US)
- [Work together with OneDrive](https://support.office.com/en-us/article/work-together-with-onedrive-626cff9f-9a56-472b-a77d-b019d97eec8d?ui=en-US&rs=en-US&ad=US)
- [Learn more about OneDrive](https://support.office.com/en-us/article/learn-more-about-onedrive-38acc14b-fd86-466e-b802-baece8107c86?ui=en-US&rs=en-US&ad=US)

