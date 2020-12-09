---
Title: "Set up an intranet for a global organization"
ms.reviewer: 
ms.author: loreenl
author: loreenl
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- m365solution-spintranet
- m365solution-scenario

search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn about setting up a SharePoint intranet for a global 
organization
---
# Planning considerations for a global intranet

If your organization has team members in multiple locations around the world, you have additional considerations and options as you plan for your SharePoint intelligent intranet. For example, you may want different branding for individual regions, or have all regions access one home page. You may want to target content to team members  in certain regions or countries. You may want to provide sites in multiple languages. Or you may need to comply with data residency requirements in certain countries.
Here are options to consider which can be used independently or in combination to meet the needs of your global intranet and create the best experience for your users.

[Hub sites](#Hub-sites)

[Multilingual sites and pages](#Multilingual-sites-and-pages)

[Regional settings](#Regional-settings)

[Audience targeting](#Audience-targeting)

[Multi-Geo for data residency requirements](Microsoft-365-Multi-Geo)

## Hub sites
You can create individual sites for different departments and regions, and you can connect those sites to a hub. The advantage to using hub sites is that they provide a flat architecture that is flexible and carries branding and navigation across multiple sites connected to the hub. 

![Hub site concept](media\HubSiteExample.png)

For your global organization, consider whether you want to create individual hubs for each region, or a main hub site that staff in all regions access. If you want branding and navigation to carry across your entire organization, you could have a hub site that everyone enters through. If you have subsidiaries in different regions that have their own branding and navigation, you can create a hub site for each region.
[Learn how to plan for hub sites](https://docs.microsoft.com/en-us/sharepoint/planning-hub-sites).

## Multilingual sites and pages 
A separate consideration for a global or regional intranet is whether you want to set up sites on your intranet to be multilingual so that users can read and work with content in their preferred languages. 

User interface elements like site navigation, site title, and site description can be shown in the [user's preferred language](https://support.microsoft.com/en-us/office/change-your-personal-language-and-region-settings-caa1fccc-bcdb-42f3-9e5b-45957647ffd7). Additionally, you can provide pages and news posts on communication sites that you translate to users’ preferred languages. For example, you may have provisioned your site with a default language of English, but you have users who have set their language preference to Spanish, and users who have set their language preference to French. You can set up your site(s) to view in the site default language as well as in French and Spanish. 
>**Note** User interface elements and pages are not translated automatically. Each page created in your default language can have a corresponding page in a chosen target language that you, or someone you assign, manually translates. After you translate such a page and publish it, it will automatically be displayed to users who have set a preferred language in their Office personal profile. 

### Next steps 
* Site owners determine which [languages to support](https://support.microsoft.com/en-us/office/languages-supported-by-sharepoint-dfbf3652-2902-4809-be21-9080b6512fff) on their sites 

* Site owners [enable multilingual features and choose languages](https://support.microsoft.com/en-us/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c#bkmk_enable)

* [Create multilingual communication sites, pages, and news](https://support.microsoft.com/en-us/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c)

* [Set up a multilingual site name, navigation and footer](https://support.microsoft.com/en-us/office/create-multilingual-communication-sites-pages-and-news-2bb7d610-5453-41c6-a0e8-6f40b3ed750c#bkmk_muitranslations)

## Regional settings for sites
Site owners can change [regional settings](https://support.microsoft.com/en-us/office/change-regional-settings-for-a-site-e9e189c7-16e3-45d3-a090-770be6e83c1a) for a site to specify calendar settings and how numbers, dates, and times are shown for all users of a site. Individual users can choose to [specify their own personal settings](https://support.microsoft.com/en-us/office/change-your-personal-language-and-region-settings-caa1fccc-bcdb-42f3-9e5b-45957647ffd7).

## Audience targeting
Audience targeting helps the most relevant content get to the right audiences. By enabling audience targeting, specific content will be prioritized to specific audiences through SharePoint web parts, page libraries, and navigational links. 

For example, you might want to prominently display news about a sales meeting in Asia to users in that region rather than display it prominently to all regions. 

### Next steps
* Learn how to [set up audience targeting](https://support.microsoft.com/en-us/office/target-content-to-a-specific-audience-on-a-sharepoint-site-68113d1b-be99-4d4c-a61c-73b087f48a81)

* Learn more about [creating groups](https://support.microsoft.com/en-us/office/target-content-to-a-specific-audience-on-a-sharepoint-site-68113d1b-be99-4d4c-a61c-73b087f48a81?ui=en-us&rs=en-us&ad=us) for audience targeting.

## Microsoft 365 Multi-Geo 
Some countries have laws requiring that user data be stored within that country. To accommodate these requirements, you can set up a Microsoft 365 Multi-Geo tenant. With a Multi-Geo tenant, your tenant may be provisioned in one country, but user data for SharePoint, OneDrive, and Exchange can be stored in other countries. For example, you may have 5,000 employees in Europe and 8,000 employees in North America. All the users are working within the same tenant, but data for the 5,000 employees are stored in Europe while data for the 8,000 employees is stored in North America. This allows for seamless collaboration across your organization while still meeting data residency requirements.

The M365 administrator needs to enable Multi-Geo, and then SharePoint admins manage the Multi-Geo feature in the SharePoint admin center.

![SharePoint Multi-Geo Admin Center](media\sharepoint-multi-geo-admin-center.png)

>**Notes**  Due to the unique nature of data requirements in China, a differentiated version of Office 365 is available and operated by a partner from datacenters inside China. This service is not considered a Multi-Geo service. It is powered by technology that Microsoft has licensed to 21Vianet. For more information, see  [Office 365 operated by 21Vianet - Service Descriptions](https://docs.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-operated-by-21vianet).

>A differentiated service called Microsoft Cloud Germany is being migrated to Office 365 services in the new German datacenter. For more information see [Migration from Microsoft Cloud Deutschland to Office 365 services in the new German datacenter regions](https://docs.microsoft.com/en-us/microsoft-365/enterprise/ms-cloud-germany-transition?view=o365-worldwide).

### Next steps
* Microsoft 365 administrators [plan](https://docs.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-tenant-configuration?view=o365-worldwide) and [set up](https://docs.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-tenant-configuration?view=o365-worldwide) Multi-Geo for their organization.

* SharePoint administrators [set up Multi-Geo](https://techcommunity.microsoft.com/t5/office-365-blog/now-available-multi-geo-in-sharepoint-and-office-365-groups/ba-p/263302) in the SharePoint admin center to enable Multi-Geo features [across the user experience](https://docs.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-user-experience?view=o365-worldwide).


	

