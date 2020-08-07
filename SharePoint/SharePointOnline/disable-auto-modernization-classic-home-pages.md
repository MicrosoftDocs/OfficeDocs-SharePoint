---
title: Automatic modernization of classic home pages
ms.reviewer: metorres
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.custom: 
- Adm_O365
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn about the automatic modernization of classic home pages, and how to disable this if you want."

---
# Classic home page modernization

Modernizing the home page of a classic SharePoint team site makes the page look great on any device and makes it easier for users to customize the layout and see news and activity. This article covers all the details on how automatic modernization works and the controls you have as an administrator. 

## How it works 

If a classic team site meets the following criteria for being updated, the home page will automatically modernize the next time a user visits. When users first experience the change, they’ll see a walkthrough that highlights the new capabilities and includes a link to a help article with more details. 

We encourage users to adopt the change in order to benefit from the power of modernized pages. However, if site admins or site owners want to revert to the classic home page, they can. Instructions are available in the [support article](https://support.office.com/article/77cbbd3c-2a23-4a76-bfd7-c5bf95afe1c6). 

### Update criteria 

- Classic team site (STS#0) only.

- Home page name in any language is ‘Home.aspx’.

- Contains default web parts only: getting started (GettingStartedWebPart), Newsfeed (SiteFeedWebPart), and document library (XsltListViewWebPart). 

- No text is present (wiki HTML is not customized).

- DisplayFormTemplateName = "WikiEditForm".

- ModernizeHomepageOptOut feature is not activated.

- No custom master pages are detected.

- The classic publishing feature is turned off.

>[!NOTE]
>All update criteria must be met for a team site home page to qualify for the automatic upgrade.

### The technical details 

- Applies to both STS#0 site collections and all corresponding subsites.

- The update applies only to the home page. No other classic pages will be changed. We recommend using the [SharePoint PnP modernization framework](/sharepoint/dev/transform/modernize-userinterface-site-pages) for all other site pages. 

- The new modern home page is named ‘Home.aspx’ and the classic page gets renamed to ‘Home(old).aspx’.

- This update does not create a [Microsoft 365 Group](https://docs.microsoft.com/sharepoint/dev/transform/modernize-connect-to-office365-group) for the team site.

- Classic site themes may not be identical once your page is updated to modern. [Learn how to apply custom styles and color to your site](/sharepoint/dev/declarative-customization/site-theming/sharepoint-site-theming-overview).

- Only site admins can revert to the classic home page through the link appearing in the left navigation. Site owners can revert to the classic page by visiting site pages and marking the classic page as their home page. 

- Update happens on demand based on next site access. If a subsite is accessed, it will trigger the update for its root site collection and its other subsites. Remember, the update only applies to the root site collection and subsites if the criteria are met. 

- We do not check the state of [custom actions](/sharepoint/dev/sp-add-ins/create-custom-actions-to-deploy-with-sharepoint-add-ins), therefore they will not transfer to your new modern page.

- We do not check the state of modern SharePoint lists and libraries for classic sites.


## Why update classic team site home pages to modern? 

Over the years, SharePoint modern pages have become powerful tools for collaboration and productivity at work and we want more users to take advantage of these capabilities. Automatically modernizing team site home pages that are not customized is the first step to helping classic site users get more out of SharePoint. 

## What to expect after a classic team site home page is updated to modern

When users first experience the change, they’ll see a walkthrough that highlights the new capabilities and includes a link to a help article with more details like this:

![Classic-to-modern upgrade experience](media/classictomodernnewGIF.gif)

For more training, download the [classic to modern walkthrough](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/raw/live/SharePoint/SharePointOnline/media/modernize-classic-home-page-walkthrough.pdf).


## How to prevent specific sites from being updated 

To disable the update on specific sites, use one of the following options: 

**Option 1**: Use [PnP PowerShell](/powershell/sharepoint/sharepoint-pnp/sharepoint-pnp-cmdlets?view=sharepoint-ps) to prevent a specific site from being upgraded by enabling a web scoped feature on each site and sub site that’s being impacted.

Connect to the site using Connect-PnPOnline. For example,

`Connect-PnPOnline -Url https://[tenant].sharepoint.com/sites/siteurl -Credentials $cred`

To prevent modernization of an uncustomized home page, run:

`Enable-PnPFeature -Identity F478D140-B148-4038-9CB0-84A8F1E4BE09 -Scope Web`

If you later want to re-enable modernization of that page, run:

`Disable-PnPFeature -Identity F478D140-B148-4038-9CB0-84A8F1E4BE09 -Scope Web`

**Option 2**: Don’t know what sites will be impacted by this change? You can use the [SharePoint Modernization Scanner](/sharepoint/dev/transform/modernize-scanner) and run the scanner in “HomePageOnly” mode. The output of the modernization scanner run contains a file called SitesWithUncustomizedHomePages.csv. Use this file to get a list of sites and sub sites that will get a modern homepage. This tool will enable you to message users impacted if desired. If needed, use the PowerShell cmdlet above, or the following sample script to opt multiple sites out of the update: https://github.com/SharePoint/sp-dev-modernization/tree/dev/Scripts/HomePageModernizationOptOut  
 

**Option 3**:
Add an out-of-the-box SharePoint [web part](https://support.office.com/article/3fdae6c3-8fc1-49ab-8708-8c104b882e64), a custom web part, or text to your team site home page.


>[!NOTE]
>It's highly recommended that you modernize home pages to benefit from the latest SharePoint features and to improve the viewing experience for users on desktop and mobile. Another option for modernizing classic sites is to enable the communication site experience on a specific classic site. For info, see [Enable the communication site experience on classic team sites](modernize-classic-team-site.md).


## What about new classic team sites STS#0 created after this change? 

Classic team sites (STS#0) created after **May 1, 2020** will not get updated.  

 
## Can I also modernize the other pages in my sites? 

For a more consistent user experience, we recommend that you modernize all pages on classic team sites. This can be self-service done via the open-source [SharePoint PnP Page Transformation solution](/sharepoint/dev/transform/modernize-userinterface-site-pages). 


## Getting excited about modern? 

For more help in transitioning to modern, refer to the following resources: 

- [Guide to modern experience in SharePoint](guide-to-sharepoint-modern-experience.md)

- [SharePoint modern inspiration](https://lookbook.microsoft.com/)  

- [Modernizing your classic sites](/sharepoint/dev/transform/modernize-classic-sites)  

- [Transform classic pages to modern pages](/sharepoint/dev/transform/modernize-userinterface-site-pages) 

- [Enable the communication site experience on classic team sites](modernize-classic-team-site.md)
