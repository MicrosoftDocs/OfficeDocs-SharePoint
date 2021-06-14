---
title: "Plan, create, and manage a home site for your organization"
ms.reviewer: 
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- m365solution-scenario
- m365solution-spintranet
ms.custom:
- seo-marvel-apr2020
search.appverid:
- SPO160
- MET150
- BSA160
description: "Learn how to plan and create the top landing page for your organization, and then set it as your home site."
---

# Plan, build, and maintain a home site for your organization
  
A SharePoint home site provide a personalized landing experience that reflects the organization’s brand, voice, and priorities. A home site also serves as the gateway to other portals in your organization’s intranet. Your organization needs a home site not only to provide the best intranet experience for viewers but to also take advantage of features like SharePoint global navigation and the many ways to integrate your intranet with Microsoft Teams by using [Viva Connections](https://www.microsoft.com/microsoft-viva/?ef_id=5acddca3e3be1730e131bc646cab7344:G:s&OCID=AID2101053_SEM_5acddca3e3be1730e131bc646cab7344:G:s&msclkid=5acddca3e3be1730e131bc646cab7344).
<br>
If you’ve already created your home site and are ready to set it now, learn how to [transform your communication site into a home site](/sharepoint/home-site#:~:text=Set%20a%20site%20as%20your%20home%20site%201,365.%20...%203%20Run%20Set-SPOHomeSite%20-HomeSiteUrl%20%3CsiteUrl%3E.%20).

**Use a SharePoint home site to:**

-	Provide a gateway to other high-traffic portals
-	Connect people with an intranet-wide search experience
-	Showcase targeted news and content
-	Take advantage of the new people engagement tool, Viva Connections 

    ![Link to the home site in the SharePoint mobile app](media/home-site-example.png)


## What is a SharePoint home site?

Home sites are SharePoint communication sites that have special capabilities such as the ability to prioritize news posted from the home site across the rest of the intranet. Review key differences between standard SharePoint communication sites and home sites:

| Feature                  | Communication site                 | Home site          |
| :------------------- | :------------------: |:---------------:|
| Engage and inform broad audiences  | X | X |
| Customizable branding opportunities                 | X                | X            |
| Can be turned into a hub site                | X                  | X             |
| Automatically marked as the official source of organizational news                 |                   | X              |
| Priority access in the mobile app home button                |                   | X              |
| Option to enable and customize global navogation in the SharePoint app bar                 |                   | X              |
| Option to set up Viva Connections              |                    | X              |

## Home site super powers explained

Home sites are unlike any other site in SharePoint. When you transform a SharePoint communication site into a home site, you’ll automatically apply special capabilities that make the home site an ideal landing destination for your intelligent intranet.

### Search for content across the entire intranet
Home sites allow users to search for content (such as sites, news, and files) across the entire intranet rather than searching just the site like typical SharePoint sites.

### Official source of organizational news  
By default, a home site is set as the organizational news source. News post that are created from the home site automatically become official organizational news and will take priority on the [SharePoint start page](https://support.microsoft.com/office/discover-content-with-the-sharepoint-start-page-6b85097a-87e0-4611-a29a-dfd49b1a1220) and in the home section of the SharePoint mobile app. Administrators can [set sites as official organizations news sources in the admin center](/sharepoint/organization-news-site).

### Enable and customize global navigation in the SharePoint app bar
The SharePoint app bar features a global navigation option that displays intranet navigational nodes and resources no matter where users are in SharePoint. To take full advantage of this feature, you must have a home site. Learn more about how to [enable and customize global navigation in the SharePoint app bar](/SharePoint/sharepoint-app-bar). 

### Use Viva Connections to integrate your intranet into Microsoft teams
Viva connections was designed to drive engagement, build community, and enable your organization to stay connected. To take advantage if this solution, you’ll need a home site. Then, you can integrate the home site into Microsoft Teams. [Learn more about Viva connections](/SharePoint/viva-connections).


## Before getting started

Before you get started planning and building your home site, review best practices and considerations. 

#### Best practices for creating home sites:
-	Since home sites will be used by the entire organization, the site needs to be [inclusive and easily accessible on all devices](https://support.microsoft.com/topic/get-ready-build-an-accessible-sharepoint-site-3a1df3ad-f093-450c-85a6-b3bf70fd6abb)
-	For the same reason above, [consider other languages that might be needed](https://support.microsoft.com/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c)
- Since the home site will be viewed by high volumn of users, ensure you are [managing site performance](/sharepoint/portal-health) through the planning and building phases
-	Links in the home site navigation can direct users to content on the home site and global navigation can be used to lead users to universally used resources and portals
-	After creating your home site, [replace the site with the current root site](/sharepoint/modern-root-site#replace-your-root-site)
-	Make sure the home site is discoverable by [adding an entry point to the Microsoft 365 app launcher](/microsoft-365/admin/manage/customize-the-app-launcher?view=o365-worldwide) and a [featured link on the SharePoint start page](/sharepoint/change-links-list-on-sharepoint-home-page)
-	[News published from the home site](https://support.microsoft.com/office/create-and-share-news-on-your-sharepoint-sites-495f8f1a-3bef-4045-b33a-55e5abe7aed7) should be relevant to the entire organization


#### Considerations:
-	Align the branding on the home site to the overall intranet brand 
-	For organizations with many portals and resources, consider [making your home site a hub site](/sharepoint/planning-hub-sites) to expand navigational options and easily sync permissions and branding across many sites
-	Use a home site template from the SharePoint look book called [The Landing](https://lookbook.microsoft.com/details/c9300e94-6e83-471a-b767-b7878689e97e) to jump start the design process


## Summary of how to get a home site for your organization

Since home sites are the gateway to your intranet, you’ll want to prioritize content and resources that are relevant to most employees. Work with business owners and stakeholders to organize and align the flow of information and the navigational design. Then, use [SharePoint PowerShell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell?view=sharepoint-ps) to create a home site and use the [Page diagnostics for SharePoint tool](/microsoft-365/Enterprise/page-diagnostics-for-spo?view=o365-worldwide) to ensure to best viewing experience. Finally, use the [Portal launch scheduler](/microsoft-365/enterprise/portallaunchscheduler?view=o365-worldwide) to plan the launch of your new site and make the site discoverable by adding links to key entry-points in the Microsoft 365 experience.
<br>
Before you get started planning your home site, [hear from the Microsoft product team on how to think](https://techcommunity.microsoft.com/t5/video-hub/build-and-launch-a-sharepoint-home-site-tips-and-tricks-from-the/m-p/1696758) about and approach the design of your organization’s home site. 


| Plan                  | Build                | Manage          |
| :------------------- | :------------------- |:----------------|
| -	Align objectives with partners and business owners
-	Organize priority content and resources 
-	Design wayfinding for the home site and global navigation
-	Think about branding
-	Use audience targeting on navigational links, news, and web parts
  | -	Upload and organize site assets and content like logos and files 
-	Customize the site to align with the rest of the intranet
-	Apply audience targeting
-	Turn on a content approval flow
-	Use PowerShell to turn the communication site into a home site
-	Replace the home site with the root site
-	Measure site health and performance
- Test on all devices
 | -	Share the site with your organization
-	Use the Portal launch scheduler to manage the launch
-	Make the home site discoverable
-	Announce the launch of the home site in an all-hands meeting and in communication channels
-	Monitor usage and page analytics
 |

## Plan your home site
A great home site starts with a plan. Since the home site is essentially the gateway to the intranet, you will want to collaborate with other business owners such as human resources, leadership teams, and even your legal team to ensure the most important and universal resources are accessible for everyone in the organization. 







## Build your home site
Once you’ve got a plan, you are ready to start creating the home site in SharePoint. Start with a communication site, and after you’ve got the general layout finalized, use SharePoint PowerShell to transform it into a home site. 








## Launch your home site
Once you’ve got your home site created it’s time to plan the launch and make sure the rest of the organization can find and use the home site.








## Home site capabilities

When you set a site as your home site:

- It's easily accessible from the SharePoint mobile app for Android and iOS. All users that have access to the home site will see a home button on the Find tab of the mobile app. Being communication sites, home sites are designed to be mobile friendly from the start.

    ![Link to the home site in the SharePoint mobile app](media/home-site-fre.png)

- Search for the site is scoped to all sites within the organization. Having a great search experience is critical for the success of the home site. [Learn more about Microsoft Search](/microsoftsearch/overview-microsoft-search)

- The site is automatically set up as an [organization news site](organization-news-site.md). (Although you can have only one home site, you can have multiple organization news sites.)
- The site is enabled for [configuring the global navigation in the SharePoint app bar](sharepoint-app-bar.md#get-started-customizing-the-global-navigation-tab).

- Having a home site enables you to use [Viva Connections](https://docs.microsoft.com/SharePoint/viva-connections).

> [!NOTE]
> Integration between the home site and [SharePoint start page](https://support.office.com/article/6b85097a-87e0-4611-a29a-dfd49b1a1220) (where the branding, theming, header, navigation, and footer elements from the home site are applied to the start page and users can easily navigate between the pages) is not available at this time. Please watch for updates in the [Microsoft 365 roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=SharePoint).

## Plan and create your home site

To set a site as your organization's home site, you first need to create and customize the site you want to use.

1. When you design your organization's top landing page, consider the goals from the perspective of your IT department, your organization's communications team, and end users of the experience.
2. Create a communication site to use for the home site, and customize it using built-in features as much as possible:




| Fun                  | With                 | Tables          |
| :------------------- | -------------------: |:---------------:|
| left-aligned column  | right-aligned column | centered column |
| $100                 | $100                 | $100            |
| $10                  | $10                  | $10             |
| $1                   | $1                   | $1              |


| Fun                  | With                 | 
| :------------------- | -------------------: |
| left-aligned column  | right-aligned column | 
| $100                 | $100                 | 
| $10                  | $10                  | 
| $1                   | $1                   | 


|                   |                | 
| :------------------: | :------------------- |
| ![image of a clipboard](media/icon-plan.png) | Start by aligning objectives with stakeholders and organizing priority content and resources. Consider details specific to your organization like if the home page will need to be available in more than one language. Use modern SharePoint sites for the home site. Learn more about how [modern SharePoint sites](https://support.microsoft.com/office/sharepoint-classic-and-modern-experiences-5725c103-505d-4a6e-9350-300d3ec7d73f) and how to [create a multi-lingual site and pages](https://support.microsoft.com/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c). | 
| $100                 | $100                 | 
| $10                  | $10                  | 
| $1                   | $1                   | 



## Plan your home site


|                   | Action        | Get started          |
| :------------------: | :------------------: |:----------------|
|  ![image of a clipboard](media/icon-plan.png)   | **Get organized** | Start by aligning objectives with stakeholders and organizing priority content and resources. Consider details specific to your organization like if the home page will need to be available in more than one language. Use modern SharePoint sites for the home site. Learn more about how [modern SharePoint sites](https://support.microsoft.com/office/sharepoint-classic-and-modern-experiences-5725c103-505d-4a6e-9350-300d3ec7d73f) and how to [create a multi-lingual site and pages](https://support.microsoft.com/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c). |
| $100                 | $100                 | $100            |
| $10                  | $10                  | $10             |
| $1                   | $1                   | $1              |
| $1                   | $1                   | $1              |
