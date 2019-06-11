---
title: "SharePoint Server Team Sites Migration Guide"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
---

# SharePoint Server Team Sites Migration Guide
This guide will help you prepare to migrate from SharePoint Server teams sites to SharePoint Online in Office 365.

Most migrations fall into regular phases as described below.  Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating and onboarding your users. 

**Note:**</br>The SharePoint Migration Tool (SPMT) is a Microsoft developed migration tool available at no cost. To download: [SharePoint Migration Tool ](https://aka.ms/spmt-ga-page).

   ![Migration process](media/migration-process-SPonly.png)

|**Planning**|**Assess and remediate**|**Prepare your SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What to expect before and after</br></br></br></br>Migration and network performance considerations</br></br>Change management and communications</br></br>Plan for Modern team sites|Run SMAT</br></br>Assess key areas</br></br>Remediate issues</br></br>Workflows</br></br>|User creation</br></br>Site creation</br></br>Tenant settings</br></br>Hybrid</br></br>|Migration service providers</br></br>Let users know how they are impacted</br></br>|Send regular emails to users</br></br>Provide training</br></br>Provide documentation for making the switch</br></br>|




## Planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The mapping of content from your source site to the destination site.

- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant. See this article for more info on speed [Best practices for improving SharePoint and OneDrive migration performance](https://docs.microsoft.com/en-us/sharepointmigration/sharepoint-online-and-onedrive-migration-speed) 

- Set permissions so IT can read/write from source to target destination

- We highly recommend that you consider setting up a hybrid environment at the beginning.
 Learn more at:   [SharePoint Hybrid Configuration Roadmaps](https://docs.microsoft.com/en-us/sharepoint/hybrid/configuration-roadmaps).


### Understanding the modern architecture
New features and enhancements are continually being rolled in SharePoint Online before being included in SharePoint Server.  As a result, features and functionality that are available in SharePoint Server may be different than those in SharePoint Online.

As you plan your migration strategy, it is important to understand the modern architecture.
Begin by reading:

- **[Guide to the Modern experience in SharePoint](https://docs.microsoft.com/en-us/sharepoint/guide-to-sharepoint-modern-experience)**


### Planning a modern framework before you migrate

**Modern team sites, pages and hubs**

When moving your team site, we recommend that you create team sites in SharePoint Online that are "modern".  While this does not automatically make them group or **Microsoft Teams** connected, you will be able to connect them in the future. You can either create them using the user interface, PowerShell, or by using a migration tool such as the SharePoint Migration Tool (SPMT) that can create these sites for you.
 
As you plan your migration, we recommend that a **hub site** the best way to create relationships between sites. We highly recommend taking this opportunity to bring those subsites to be their own site collections in order to connect them through a hub.

- [What is a SharePoint hub site?](https://support.office.com/en-us/article/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f?ui=en-US&rs=en-US&ad=US)

- [Planning your SharePoint hub sites](https://docs.microsoft.com/en-us/sharepoint/planning-hub-sites)

Decide how your team sites map to a modern hub architecture. It isn't necessary to group connect every site you are moving, but strategize your site plan to optimize the structure to be flexible for continuous change.

#### More guidance on modernization

- [Modernize your classic SharePoint sites](https://aka.ms/sppnp-modernize) 

- [Transform classic pages to modern client-side pages](https://docs.microsoft.com/en-us/sharepoint/dev/transform/modernize-userinterface-site-pages)

- [Transforming to modern site pages from inside the SharePoint UI](https://aka.ms/sppnp-pagetransformationui)



### Workflows and planning for the future
In Office 365, **Microsoft Flow** is the product that allows you to easily create and manage workflow. If you are currently using SharePoint workflows, we recommend that you consider "future-proofing" your environment by identifying the workflows you want to keep and recreate them using **Microsoft Flow** to allow for better platform integration. 

To learn more:
- [Get started with Microsoft Flow](https://docs.microsoft.com/en-us/flow/getting-started)

>[!Note]
>Classic workflow will be supported and available until 2026. We recommend taking this into consideration as you plan for your workflow lifetime.



## Assess and remediate your content

Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. Think about how and what My Sites features you use in production.

An initial assessment can begin with working with your users in two main areas:

- Identify older content
- Determine if content is obsolete or redundant and can be deleted.



### Using the SharePoint Migration Assessment Tool (SMAT)
The SharePoint Migration Assessment Tool (SMAT) is a simple command line executable that scans the contents of your SharePoint Server 2013 farm to help identify any issues before you migrate your content.

After the scan is complete, SMAT generates summary and detailed reports showing the areas that could impact your migration. Not everything in the report needs to be remediated; but the important scans for your business needs should be looked at.

Also included is the SharePoint Migration Identity Management Tool, that does identity mapping by scanning SharePoint, Active Directory, and Azure Active Directory.





## Prepare your SharePoint environment

Before migrating your team site content, you must first pre-provision your users in Office 365.

  For guidance on pre-provisioning see: 
- [Prepare to provision users through directory synchronization to Office 365](/office365/enterprise/prepare-for-directory-synchronization)


Create modern hub sites based on how you have mapped your sites to a system of hub site. 

- [Create a hub site](https://docs.microsoft.com/en-us/sharepoint/create-hub-site)
- [Assocate a SharEPoint site with a hub site](https://support.office.com/en-us/article/associate-a-sharepoint-site-with-a-hub-site-ae0009fd-af04-4d3d-917d-88edb43efc05?ui=en-US&rs=en-US&ad=US)



## Migration process

Below is a typical migration process that follows Microsoft’s best practices guidance.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.</br></br>
2.	Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which SharePoint Server team sites are disabled and they are directed to use the SharePoint Online environment. This method is preferred as it reduces user impact.</br></br>
3.	Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.</br></br>
4.	Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to using their SharePoint sites. This helps eliminate users from updating duplicate copies of content.</br></br>



### Migration offerings
Currently, there are a variety of migration offerings available to you. Which one is right for you?


**Self service**

The benefit for self-service migration is that you have full control over your process and timing, and you determine the pace of migration. Microsoft provides the [SharePoint Migration Tool](https://aka.ms/spmt-ga-page)  free of charge and you will be able to leverage your own IT resources rather than having to invest in outside expertise.  


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

- [Ways to work online with SharePoint](https://support.office.com/en-us/article/ways-to-work-with-sharepoint-11de936c-8fed-4474-ac58-583d0c38ac12)
- [Team library video training](https://support.office.com/en-us/article/video-create-a-team-or-communication-site-551e190a-8fbe-47ae-a88a-798b443c46b1?ui=en-US&rs=en-US&ad=US)
- [Quick start training ](https://support.office.com/en-us/article/sign-in-to-sharepoint-online-324a89ec-e77b-4475-b64a-13a0c14c45ec?ui=en-US&rs=en-US&ad=US) 
- [SharePoint Online video training](https://support.office.com/en-us/article/SharePoint-Online-video-training-cb8ef501-84db-4427-ac77-ec2009fb8e23)



