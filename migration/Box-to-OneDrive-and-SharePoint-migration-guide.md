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
The purpose of this guide is to assist you in preparing for your Box to Office 365 migration.  
Most migrations fall into regular phases as described below.  Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users. 

INSERT GRAPHIC

## Planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:
- The design of the target OneDrive and SharePoint Online environment and the mapping between source and target systems. 
- The amount of content you eventually migrate. Determine if content is redundant, out of date, or still relevant.

## What content goes where
Consider how you use the content in your Box accounts today and plan how to transition to the improved Office 365 collaborative experience. 

Let’s first review the benefits that OneDrive and SharePoint provides to understand how each area can best serve your needs. 

- **OneDrive** is a place where you can store files from your computer into the cloud, and access them from any device, or share them with others. As part of Office 365, OneDrive lets you update and share your files from anywhere and work on Office documents with others at the same time.
- **SharePoint Online team site**  is a place that users can collaborate on files, documents, and ideas. It is set up to facilitate two-way communication between team members and offers a full range of features to help a team communicate and collaborate.

Knowing the capabilities of OneDrive and SharePoint, look at the following table to help you determine what content goes where:

|**Ask...**|**OneDrive**|**SharePoint Online site**|
|:-----|:-----|:-----|
|Does the file belong to me alone?|X||
|Is this a file you want to keep private for the time being?|X||
|Is this a file you want to share with a very limited set of people?|X|X|
|Does this file/content belong to a larger group, such as Sales or HR?|X|
|Is there a policy on any of the content|X|
|Does this content need to be managed by a workflow?|X|
|Do you need to manage metadata on this content?|X|
|Will this file need to be shared with someone outside of your company?|X|X|
|Is there a group of like content that needs to be shared outside your company?|X|
|Do you have governance policies that control this content?|X|
|Do you want to leverage the collaborating features in Office 365?|X|X|

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

**Sharing** is an explicit action a user takes to invite another user to collaborate on content. Sharing content implicitly gives that user permission to edit the content as well. Only content that has been explicitly shared with a user (or a group to which they belong) will appear in their *Shared with Me* view in OneDrive.
The following table maps your current Box sharing experience with OneDrive or SharePoint.

|**Box**|**OneDrive or SharePoint Online**|
|:-----|:-----|
|Folders or file with only one owner, but more than one contributor|As the owner, content should be migrated to the user's OneDrive folder. Any user who has access to a user's folder will have that folder automatically appear in their **Shared with Me** list.|
|Only one owner, but shared with a Box group|As the owner, content will be migrated to the user's OneDrive folder. <br>The Box group should be converted to a security group.  <br>Email should then be sent to the new security group, where each user can accept the invitation link. Content will then appear in those users **Shared with Me** list.|
|Box folders with contributors who are external to your organization|Microsoft's recommendation is to not migrate external sharing permissions. <br>**Note:**  Any content that is shared with a user from another company?s Box instance won?t be migrated.  If the user still wants to retain that content, their Box account will need to remain active.|
|**Shared with** Box end user experience|Only content that has been explicitly shared with a user will appear in their **Shared with Me** view in OneDrive. For group content, Office 365 Groups will appear in users **Shared with Me** view in OneDrive.|

## External permission Best Practices

We’ve touched on Microsoft’s recommendation to not migrate external sharing permissions. However many organizations have a hard requirement to retain external permissions on their content. This sub-section overviews Microsoft’s best practices as follows: 
- Audit external permissions on the Box content source
- Determine whether that content is worthy to remain externally shared
- If so, determine whether that content is suited for OneDrive or SharePoint based on the What content goes where above guidance
- - If OneDrive – reshare files externally with the appropriate external users after the migration  
- If SharePoint<br>
- Where possible, leverage the collaboration and security benefits of grouping external partner specific content per SharePoint Team site. Read more details in the business to business extranet solution article.  <br> If content cannot be grouped as such, then externally reshare on the file or folder level in the target SharePoint Team site. 

## Change management and communications plan

### Change management

Develop a plan to prepare your users for the upcoming change. Include in your plan: 
•	Evangelize the move. Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
•	End user training.  Provide training to your users on the features in OneDrive and SharePoint Online.
•	Train your helpdesk.  Before the cutover, train your helpdesk in key features and common user questions.
•	Prepare for any possible downtime the migration may incur.  

### Communication plan

Develop a plan for sending communications to your user base, providing clear statements of timing, expectations and impact to the individual.  See the Onboarding your users section below for messaging suggestions.


## Prepare your OneDrive and SharePoint Online environment

Before migrating your Box content, you must pre-provision your users in OneDrive and SharePoint Online For guidance on pre-provisioning see: 
- Prepare to provision users through directory synchronization to Office 365
- Pre-provision OneDrive for users in your organization .

### Admin settings and policies
After provisioning your users, plan how you want to what your SharePoint sites and OneDrive accounts to be configured.  This includes your mobile device settings and access, default sharing settings, and site ownership. 

In addition
- Set permissions so a 3rd party tool can migrate
- Change default settings to allow special characters (those not enabled by default)
- For your migration it is necessary to have connectivity between corpnet and Office 365.
- Configure the firewall and proxy for SharePoint Online and OneDrive access: Office 365 URLs and IP address ranges. 


## Assess and remediate your content
Before beginning your migration, it is important that you perform an analysis of your current environment.  Only you know your data and how and who uses it.  Think about how and what Box features you use in production. 

The following are recommended assessments can all be performed using Box’s Folders and Files admin report. Run this report and use its results to perform these assessments. Remediate your content on the source before beginning your migration to save time and effort later.

### File Extensions
#### Assess
Find all files in the Folders and Files report whose Path ends in one of the extensions defined here: Types of files that cannot be added to a list or library.
#### Remediate
Turn scripting capability on in OD/SP as described here: Allow or prevent custom script. Make sure you understand why these files are blocked by default as described here: Security considerations of allowing custom script.
### File and Folder Name Characters
#### Assess
Find all items in the Folders and Files report whose name contains any of the characters detailed here: Restrictions and limitations when you sync SharePoint libraries to your computer through OneDrive.
#### Remediate
Work with your migration vendor to substitute these characters in all file and folder names.
Note that the # and % characters are supported but not enabled by default. Follow these steps to enable them: New support for # and % in SharePoint Online and OneDrive .
### File and Folder Path Length
#### Assess
Find all items in the Folders and Files report whose Path exceeds the file path length described here: SharePoint Online limits. 
#### Remediate
Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.

## Migrate

### Migration offerings
Currently, there are a variety of migration offerings available to you. They include
- Microsoft FastTrack Benefit
- 3rd Party vendors
- API’s

### Microsoft migration Best Practices

•	Define your migration plan with your vendor.  We recommend that you have completed your assessment and remediation of your content before you migrate; not after.  
•	We recommend that you choose an incremental migration plan with a single cutover day.
•	Convert existing Box groups to security groups.
•	Schedule users with dependencies in the same batch. Shared content is only migrated if it’s owned by the Box account currently being migrated. 
•	Build time into the schedule for User Acceptance testing
•	Be aware of your Box plan and any restrictions you may encounter regarding the number of actions you can perform in any given month. Box has different throttling limits based on your contract ( see Box pricing plans ).  
o	Starter: 25K Actions/Month
o	Business: 50K Actions/Month
o	Enterprise: 100K Actions/Month
•	Migration speed can be impacted by many factors. Understanding these will help you plan and maximize the efficiency of your migration as you work with your migration vendor.  For more info see:  SharePoint Online and OneDrive Migration Speed 

 
## Common migration errors and recommended remediation actions

|**Issue**|**Description**|**Remediation**|
|:-----|:-----|:-----|
|Blocked files|"Files with certain extensions (ASPX| MASTER| XAP| SWF| JAR| ASMX| ASCX| XSF| HTC) fail to migrate."|"If you want these files migrated| a SharePoint Online admin can change this default setting prior to migration."|
||This happens because scripting files are blocked by SharePoint Online by default.|"For more information| see Turn scripting capabilities on or off."|
|Unsupported characters in folder and file names|Certain special characters and file and folder names can be used in Box but not in OneDrive and SharePoint Online.|Specify in the migration questionnaire which invalid characters and invalid file and folder names should be remediated through character substitution during migration.|
||"For more information| see Restrictions and limitations when you sync SharePoint libraries to your computer through OneDrive."||
|Long URL path|"Files and folders with a long path (for example| deeply nested folders and long names) fail to migrate."|Folders and files like these are identified by our Inventory Manager (assuming 50 characters for the tenant name by default).|
||The entire combined path of folder name and file name in the target can have up to 400 characters.|Customers can refer to the assessment report and reorganize folders and files.|
||"For more information| see Restrictions and limitations when you sync SharePoint libraries to your computer through OneDrive."|"If not remediated| these failures are captured during migration and are reported in the migration report."|
|Files already exist|"If the end user is already using OneDrive and there’s a file with same name in Box| the file won’t migrate due to the name conflict."|We recommend you back up the existing OneDrive content and provide empty OneDrive accounts for migration.|
||End users should rename these files if they’re aware of them.|
||These files are reported in the final error report as “Already Exists”.|
|External content and permissions|"Content and permissions external to your organization aren’t migrated. For example| permissions on personal Gmail accounts and content owned by Outlook.com accounts"|Most organizations choose not to share content with external users due to corporate security guidelines.|
||"To remediate this issue| customers should use the Collaborations report (generated through the Box Admin Console) to identify the external accounts and then notify end users so they can reshare with external users after migration."|
|Migration tool not authorized to connect to  Box|When using valid co-admin credentials a message displays that the migration tool is not authorized to connect to Box.|The client ID of the migration tool may have been removed from the Unpublished Applications exceptions list in Box.|
||"Customers should validate if their Box environment disables published and unpublished applications by default. If applicable| the client ID may need to be re-added to the exception list."|
||"To view the exception list| log on to Box with a co-admin account| navigate to the Admin Console| open Enterprise Settings| and then access the Apps tab."|
|Content in Box may have a different owner than the account used for creation|"When a user creates a document in a location shared by a different internal Box user| the content won’t migrate with the Box drive of the creator. Instead| it’s migrated with the Box drive of the user who is sharing."|"Box file and folder ownership is determined by the top parent folder in the hierarchy| regardless of how child folders are created or shared."|


