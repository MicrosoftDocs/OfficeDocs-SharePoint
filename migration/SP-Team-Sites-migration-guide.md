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

   ![Migration process](media/migrationprocess-fileshare.png)

|**Planning**|**Assess and remediate**|**Prepare your SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What to expect before and after|Run SMAT|User creation |Migration steps|Send regular emails to users|
|Migration and network performance considerations|Assess key areas|Site creation|Migration service providers|Provide training|
|Change management and communications|Remediate issues|Tenant settings| Let users know how they are impacted|
|Plan for Modernization: Modern team sites| Hubs| Workflow (Flow)"|Hybrid| Provide documentation for making the switch|




## Migration planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The mapping of content from your source site to the destination site.

- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant. See this article for more info on speed [Best practices for improving SharePoint and OneDrive migration performance](https://docs.microsoft.com/en-us/sharepointmigration/sharepoint-online-and-onedrive-migration-speed) 

- Set permissions so IT can read/write from source to target destination

- We highly recommend that you consider setting up a hybrid environment at the beginning.
 Learn more at:   [SharePoint Hybrid Configuration Roadmaps](https://docs.microsoft.com/en-us/sharepoint/hybrid/configuration-roadmaps).


### Planning for modernization
SharePoint Online is continually being improved. New features and improvements to existing features are rolled out in SharePoint Online before SharePoint Server.  As a result, features and functionality that are available in SharePoint Server may be different than those in SharePoint Online.

The modern experience in SharePoint is designed to not only be compelling but flexible, making it easier for anyone to create mobile-ready sites and pages. Improvements in navigation, branding, publishing, search, and sharing make it a


#### Modern team sites and modern pages

 
When moving your team site, we recommend that you create team sites in SharePoint Online that are "Modern".  While this does not automatically make them group or **Microsoft Teams** connected, you will be able to connect them in the future. You can either provision them using PowerShell using template #STS3, or use a migration tool such as the SharePoint Migration Tool (SPMT) that can create these sites for you.
 

#### More guidance on modernization of sites

- [Guide to the Modern experience in SharePoint](https://docs.microsoft.com/en-us/sharepoint/guide-to-sharepoint-modern-experience)

- [Modernize your classic SharePoint sites](https://aka.ms/sppnp-modernize) 

- [Transform classic pages to modern client-side pages](https://docs.microsoft.com/en-us/sharepoint/dev/transform/modernize-userinterface-site-pages):     How to use it from .Net, PowerShell and the SharePoint UI 

- [Transforming to modern site pages from inside the SharePoint UI](https://aka.ms/sppnp-pagetransformationui) How to setup and use the Page Transformation UI solution 

- [SharePoint Monthly Call Video](https://www.youtube.com/watch?v=NppqtPo4-bo&index=2&list=PLR9nK3mnD-OVC4_ut9bUi6ffRXLVuF0_g) Powershell usage shown at 34:27

- [Video: Preview of the page transformation UI integration](https://www.youtube.com/watch?v=y9SeZ9vBh7U&t=81s) 

### Moving to Microsoft hubs

Classic SharePoint architecture is typically built using a hierarchical system of site collections and sub-sites, with inherited navigation, permissions, and site designs. Once built, this structure can be inflexible and difficult to maintain. 

In the modern SharePoint experience, every site is a site collection, and all can be associated to a **hub** site which is a flat structure of sites that share navigation, branding, and other elements. This type of structure is far more flexible and adaptive to the changing needs of your organization. 

As you plan your migration, we recommend that **Hubs** is the best way to create relationships between sites. We highly recommend taking this opportunity to bring those subsites to be their own site collections in order to connect them through **Hubs**.



To learn more about Microsoft hubs:
- [What is a SharePoint hub site?](https://support.office.com/en-us/article/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f?ui=en-US&rs=en-US&ad=US)

- [Planning your SharePoint hub sites](https://docs.microsoft.com/en-us/sharepoint/planning-hub-sites)

### Transforming your Workflow
In Office 365, **Microsoft Flow** is the product that allows you to easily create and manage workflow. If you are currently using SharePoint workflows, we recommend that you consider "future-proofing" your environment by identifying the workflows you want to keep and recreate them using **Microsoft Flow** to allow for better platform integration. 


>[!Note]
>Classic workflow will still be supported and available until 2026. We recommend taking this in considerations as you plan for your workflow lifetime.


To learn more:

- [Get started with Microsoft Flow](https://docs.microsoft.com/en-us/flow/getting-started)


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

Before migrating your team site content, you must pre-provision your users in Office 365.  For guidance on pre-provisioning see: 
- [Prepare to provision users through directory synchronization to Office 365](/office365/enterprise/prepare-for-directory-synchronization)
- [Transform classic pages to modern client-side pages](https://docs.microsoft.com/en-us/sharepoint/dev/transform/modernize-userinterface-site-pages)




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



