---
title: "SharePoint Server to SharePoint Online and OneDrive Migration Guide"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- M365-collaboration
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
search.appverid: MET150
ms.custom: 
ms.assetid: 

---

# SharePoint Server OneDrive and SharePoint Migration Guide
This guide will help you prepare to migrate from SharePoint Server to OneDrive and SharePoint in Office 365.

Most migrations fall into regular phases as described below.  Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users. 

**Note:**</br>The SharePoint Migration Tool (SPMT) is a Microsoft developed migration tool available at no cost. To download: [SharePoint Migration Tool ](https://aka.ms/spmt-ga-page).

   ![Migration process](media/migrationprocess-fileshare.png)

|**Planning**|**Assess and remediate**|**Prepare your SharePoint OneDrive environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What to expect before and after|Run SMAT|User creation |Migration steps|Send regular emails to users|
|Migration and network performance considerations|Assess key areas|Site creation|Migration service providers|Provide training|
|Change management and communications|Remediate issues|Tenant settings| Let users know how they are impacted|
|Plan for Modernization: Modern team sites| Hubs| Workflow (Flow)"|Hybrid| Provide documentation for making the switch|




## Migration planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The mapping of content from your source My Sites to the destination OneDrive.

- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant. See this article for more info on speed [Best practices for improving SharePoint and OneDrive migration performance](https://docs.microsoft.com/en-us/sharepointmigration/sharepoint-online-and-onedrive-migration-speed) 

- Set permissions so IT can read/write from source to target destination

- We highly recommend that you consider setting up a hybrid environment at the beginning.
 Learn more at:   [SharePoint and OneDrive Configuration Roadmaps](https://docs.microsoft.com/en-us/sharepoint/hybrid/configuration-roadmaps).


### Planning for modernization
SharePoint Online, is continually being improved. New features are rolled out first in SharePoint Online and existing features revamped and improved.  As a result, features and their functionality that are available in SharePoint Server may be different in SharePoint Online. Here is a list of things to consider as you plan for your migration.

#### Modern team sites and modern pages
When moving your team site, we recommend that you create team sites in SharePoint Online that are "Modern", using template STS#3. This does not automatically make them group or Teams connected but you will be able to connect them in the future. Modern team sites come with a more user-friendly look and feel and a new home page. Migration tools such as the SharePoint Migration Tool (SPMT) can create these sites for you.
 

#### More guidance on modernization of sites

- [Modernize your classic SharePoint sites](https://aka.ms/sppnp-modernize) 

- [Transform classic pages to modern client-side pages](https://docs.microsoft.com/en-us/sharepoint/dev/transform/modernize-userinterface-site-pages):     How to use it from .Net, PowerShell and the SharePoint UI 

- [Transforming to modern site pages from inside the SharePoint UI](https://aka.ms/sppnp-pagetransformationui) How to setup and use the Page Transformation UI solution 

- [SharePoint Monthly Call Video](https://www.youtube.com/watch?v=NppqtPo4-bo&index=2&list=PLR9nK3mnD-OVC4_ut9bUi6ffRXLVuF0_g) Powershell usage shown at 34:27

- [Video: Preview of the page transformation UI integration](https://www.youtube.com/watch?v=y9SeZ9vBh7U&t=81s) 

### Moving to Microsoft hubs

As you plan your migration, there is another architectural change that can be applied relating to your site structure. In SharePoint online, **Hubs** is the best way to create relationships between sites. We highly recommend taking this opportunity to bring those subsites to be their own site collections in order to connect them through Hubs.

To learn more about Microsoft hubs:
- [What is a SharePoint hub site?](https://support.office.com/en-us/article/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f?ui=en-US&rs=en-US&ad=US)

- [Planning your SharePoint hub sites](https://docs.microsoft.com/en-us/sharepoint/planning-hub-sites)

### Transforming your Workflow
In Office 365, **Microsoft Flow** is the product that allows you to easily create and manage workflow. As you transition your content to OneDrive and SharePoint online, we highly recommend looking at the workflows you want to keep and recreate into Flows for better integration into the platform. 

For cases where Flow doesn’t accomplish your need, classic workflow will still be supported and available until 2026. We recommend taking this in considerations as you plan for your workflow lifetime.

To learn more:

- [Get started with Microsoft Flow](https://docs.microsoft.com/en-us/flow/getting-started)



### What content goes where
Include in your planning how to make this transition to Office 365 will make for a more collaborative experience for your users.
 
Review how you use the content stored in your file shares today. Does the file belong to a single user, even though they may share it with others? If so, save it in your OneDrive. Your OneDrive is private by default, but you can share files with others, which is particularly useful if you aren’t working as a team yet.

If you’re working on a file or folder intended for team consumption and collaboration, move it to a **shared library** where team members have access by default. OneDrive gives you access to all your shared libraries in Microsoft Teams, SharePoint or Outlook. When you need a new shared library for team files, you can create on right from OneDrive, add members, and start working together.



## Assess and remediate your content

Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. Think about how and what My Sites features you use in production.

An initial assessment can begin with working with your users in two main areas:

- Identify older content
- Determine if content is obsolete or redundant and can be deleted.



### Using the SharePoint Migration Assessment Tool (SMAT)
The SharePoint Migration Assessment Tool (SMAT) is a simple command line executable that scans the contents of your SharePoint Server 2013 farm to help identify any issues before you migrate your content.

After the scan is complete, SMAT generates summary and detailed reports showing the areas that could impact your migration. Not everything in the report needs to be remediated; but the important scans for your business needs should be looked at.

Also included is the SharePoint Migration Identity Management Tool, that does identity mapping by scanning SharePoint, Active Directory, and Azure Active Directory.






## Prepare your OneDrive environment

Before migrating your file share content, you must pre-provision your users in Office 365.  For guidance on pre-provisioning see: 
- [Prepare to provision users through directory synchronization to Office 365](/office365/enterprise/prepare-for-directory-synchronization)
- [Pre-provision OneDrive for users in your organization](/onedrive/pre-provision-accounts)




## Migration process

Below is a typical migration process that follows Microsoft’s best practices guidance.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.</br></br>
2.	Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which network file shares and local file shares are disabled and they are directed to use the SharePoint or OneDrive environment. This method is preferred as it reduces user impact.</br></br>
3.	Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.</br></br>
4.	Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to using their OneDrive accounts and SharePoint sites. This helps eliminate users from updating duplicate copies of content.</br></br>




### Migration offerings
Currently, there are a variety of migration offerings available to you. Which one is right for you?

|**Customer Self service**|**FastTrack driven**|**Partner driven**|
|:-----|:-----|:-----|
|No cost for Microsoft provided tool</br>[SharePoint Migration Tool ](https://aka.ms/spmt-ga-page)|No cost; included in your [Microsoft 365 subscription](https://docs.microsoft.com/en-us/fasttrack/o365-data-migration)|Price dependent on complexity|
|Process flexible, you set the pace|Highly structured process and schedule|Customized to your need|
|No need to configure complex infrastructure|Must set up infrastructure including external access rights, VPNs, test environment, admin environment, establish framework of contacts|Customized to your need|
|Less time required involved in scheduling process and restrictions|Scheduling templates and questionnaires provided as part of the organization process|Customized to your need|
|Customer controls the pace based on their needs|Schedule is driven in partnership with the FastTrack team|Customized to your need|
|May have to hire in expertise if you don’t have it in place already|Expertise provided by FastTrack|Expertise provided|
|Customer controls the schedule flexibility; off hours and blackout hours are defined by them|Must hold to a set schedule|Customized to your need|





**Self service**

The benefit for self-service migration is that you have full control over your process and timing, and you determine the pace of migration. Microsoft provides the [SharePoint Migration Tool](https://aka.ms/spmt-ga-page)  free of charge and you will be able to leverage your own IT resources rather than having to invest in outside expertise.  



**Microsoft FastTrack**

FastTrack is a Microsoft service included in your subscription cost that provides you with a set of best practices, tools, resources, and experts committed to making your experience with the Microsoft Cloud a great one. OneDrive onboarding guidance, migration benefits, and adoption guidance are included in the benefit offering. 

Onboarding guidance includes: help to discover what’s possible, creating a plan for success, and onboarding new users and capabilities at a flexible pace. The [Data Migration](/fasttrack/O365-data-migration) benefit covers guidance on migrating content from file share, Box, or Google Drive source environments. 

This guidance covers enablement of both OneDrive for Business and the source environment. FastTrack will also perform specific data migration activities on behalf of the customer for those with 500 or more licenses. See more details in the provided [FastTrack Center Benefit Overview](/fasttrack/O365-data-migration). Interested in getting started? Visit [FastTrack.microsoft.com](https://fasttrack.microsoft.com/), review resources, and submit a Request for Assistance.

**Migration service providers**

You may decide that your organization has specific business needs that require you to use third-party services or applications to help you execute your migration. Explore the professional services and applications available from partners in the Microsoft Partner Center. There you can find experts to help you in your enterprise content migration to Office 365.  For more information see: [Microsoft Partner Center](https://partnercenter.microsoft.com/en-us/partner/home). 

## User Onboarding
Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan: 
- **Evangelize the move.** Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training.**  Provide training to your users on the features in OneDrive.
- **Train your helpdesk.**  Before the cutover, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime** the migration may incur.
  
 Develop a plan for sending communications to your user base, providing clear statements of timing, expectations and impact to the individual. Include:

- The migration timeline and how it will impact them. Include any end user calls to action. 
- Assure them that if they have content already in OneDrive, that their content is safe and won’t be overwritten. 
- Let them know whether individuals can opt-out of the migration process

### Onboarding related resources
- [Microsoft 365 adoption guide](https://devfasttrackv4storage.blob.core.windows.net/marketing/en-us/resources/Microsoft%20365%20User%20Adoption%20Guide.pdf): Outlining methodology and resources for implementing proven adoption success factors
- [Posters, email templates](https://fasttrack.microsoft.com/microsoft365/resourcehub): customizable templates to generate internal awareness and excitement
- [Ways to work online with SharePoint](https://support.office.com/en-us/article/ways-to-work-with-sharepoint-11de936c-8fed-4474-ac58-583d0c38ac12)
- [OneDrive](https://support.office.com/en-us/article/onedrive-video-training-1f608184-b7e6-43ca-8753-2ff679203132?ocmsassetID=1f608184-b7e6-43ca-8753-2ff679203132&ui=en-US&rs=en-US&ad=US) and [team library](https://support.office.com/en-us/article/video-create-a-team-or-communication-site-551e190a-8fbe-47ae-a88a-798b443c46b1?ui=en-US&rs=en-US&ad=US) video training
- [OneDrive](https://support.office.com/en-us/article/upload-files-to-onedrive-for-business-a1397e56-61ec-4ed2-9dac-727bf8ac3357?ui=en-US&rs=en-US&ad=US) and [team library](https://support.office.com/en-us/article/sign-in-to-sharepoint-online-324a89ec-e77b-4475-b64a-13a0c14c45ec?ui=en-US&rs=en-US&ad=US) Quick start training guides: get up and running quickly with the basic info you need to be productive right away 
- [SharePoint Online video training](https://support.office.com/en-us/article/SharePoint-Online-video-training-cb8ef501-84db-4427-ac77-ec2009fb8e23)
- [Work together with OneDrive](https://support.office.com/en-us/article/work-together-with-onedrive-626cff9f-9a56-472b-a77d-b019d97eec8d?ui=en-US&rs=en-US&ad=US)
- [Learn more about OneDrive](https://support.office.com/en-us/article/learn-more-about-onedrive-38acc14b-fd86-466e-b802-baece8107c86?ui=en-US&rs=en-US&ad=US)


