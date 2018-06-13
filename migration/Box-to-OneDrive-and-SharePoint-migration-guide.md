---
title: "Box to OneDrive and SharePoint Migration Guide"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 6/15/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom: 
ms.assetid: 

---

# Box to OneDrive and SharePoint Online Migration Guide
The purpose of this guide is to assist you in preparing for your Box to OneDrive and SharePoint migration.

Most migrations fall into regular phases as described below.  Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users. 

Insert graphic

|**Migration Planning**|**Assess and remediate**|**Prepare you OneDrive and SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What goes where|Analyze Box admin reports|Pre-provision Office 365 and users|Review migration offerings|Send regular emails to users|
|Understanding permissions vs Sharing|Assess key areas||Microsoft FastTrack services|Provide training|
|What to expect before and after|Remediate issues||Migration service providers|Let uesrs know how they are impacted|
|Migration and network performance considerations||||Provide documentation for making the switch|
|Change management and communications|

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

Knowing the capabilities of OneDrive and SharePoint, look at the following table to help you determine what content goes where:


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

We’ve touched on Microsoft’s recommendation to not migrate external sharing permissions. However many organizations have a hard requirement to retain external permissions on their content. This sub-section overviews Microsoft’s best practices as follows: 
- Audit external permissions on the Box content source
- Determine whether that content is worthy to remain externally shared
- If so, determine whether that content is suited for OneDrive or SharePoint based on the What content goes where above guidance
- - If OneDrive – reshare files externally with the appropriate external users after the migration  
- If SharePoint<br>
- Where possible, leverage the collaboration and security benefits of grouping external partner specific content per SharePoint Team site. Read more details in the business to business extranet solution article.  <br> If content cannot be grouped as such, then externally reshare on the file or folder level in the target SharePoint Team site. 




## Prepare your OneDrive and SharePoint Online environment

Before migrating your Box content, you must pre-provision your users in OneDrive and SharePoint Online For guidance on pre-provisioning see: 
- Prepare to provision users through directory synchronization to Office 365
- Pre-provision OneDrive for users in your organization.
- •	Configure the firewall and proxy for SharePoint and OneDrive access: Office 365 URLs and IP address ranges. 


## Assess and remediate your content
Before beginning your migration, it is important that you perform an analysis of your current environment.  Only you know your data and how and who uses it.  Think about how and what Box features you use in production.
 
The following are recommended assessments.  All can be performed using Box’s Folders and Files admin report. Run this report and use its results to perform these assessments. Remediate your content on the source before beginning your migration to save time and effort later.


### File Extensions
|**Assess**|**Remediate**|
|:-----|:-----|
|Find all files in the Folders and Files report whose Path ends in one of the extensions defined here: Types of files that cannot be added to a list or library.|Turn scripting capability on in OD/SP as described here: Allow or prevent custom script. Make sure you understand why these files are blocked by default as described here: Security considerations of allowing custom script.|

### File and Folder Name Characters
|**Assess**|**Remediate**|
|:-----|:-----|
|Find all items in the Folders and Files report whose name contains any of the characters detailed here: Restrictions and limitations when you sync SharePoint libraries to your computer through OneDrive.|Work with your migration vendor to substitute these characters in all file and folder names.<br><br>**Note:** The # and % characters are supported but not enabled by default. Follow these steps to enable them: New support for # and % in SharePoint Online and OneDrive.|

### File and Folder Path Length
|**Assess**|**Remediate**|
|:-----|:-----|
|Find all items in the *Folders and Files* report whose Path exceeds the file path length described here: SharePoint Online limits.|Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|

### Large drives and complex sharing
|**Assess**|**Remediate**|
|:-----|:-----|
|Scan for any drives that have a very large amount of content, or many different unique sharing permissions – this is usually a sign that the drive should be broken down into smaller, more focused sites. <br><br>Specifically, any drive that has more than 50,000 documents shared with different users must be broken up. Use Box’s Folders and Files report and Shared Links report to identify such drives.|Identify sets of content within these drives that are conceptually similar (same project area, all shared with the same users, etc). Move these sets of content out and into new drives before starting migration.|
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

Onboarding guidance includes: help to discover what’s possible, creating a plan for success, and onboarding new users and capabilities at a flexible pace. The Data Migration benefit covers guidance on migrating content from file share, Box, or Google Drive source environments. 

This guidance covers enablement of both OneDrive for Business and the source environment. FastTrack will also perform specific data migration activities on behalf of the customer for those with 500 or more licenses. See more details in the provided FastTrack Center Benefit Overview. Interested in getting started? Visit FastTrack.Microsoft.Com, review resources, and submit a Request for Assistance.

**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Office 365.  For more information see: Microsoft Partner Center. 
 
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
- Microsoft 365 adoption guide: outlining methodology and resources for implementing proven adoption success factors
- Posters, email templates: customizable templates to generate internal awareness and excitement
- OneDrive and SharePoint video training
- OneDrive and SharePoint Quick start training guides: get up and running quickly with the basic info you need to be productive right away 

### Make the Switch! 
The following articles will help your users “make the switch” from Box to OneDrive. The topics show how you used to do common tasks in Box and how you do the same in OneDrive.

- Switch to OneDrive from Box 
- Open with OneDrive
- Store with OneDrive
- Work together with OneDrive
- Learn more about OneDrive

