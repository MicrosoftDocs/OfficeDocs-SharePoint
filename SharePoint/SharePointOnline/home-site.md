---
title: "Set a site as your home site"
ms.reviewer: dipadur
ms.author: kaarins
author: kaarins
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
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
ROBOTS: NOINDEX, NOFOLLOW
description: "Learn how to use PowerShell to set a communication site as the home site for your organization."
---

# Set a site as your home site
  
A home site is a SharePoint [communication site](https://support.office.com/article/94A33429-E580-45C3-A090-5512A8070732) that you create and set as the main landing site for your intranet. It brings together news, events, embedded video and conversations, and other resources to deliver an engaging experience that reflects your organization's voice, priorities, and brand. Follow the instructions below to transform your communication site into a home site using Microsoft PowerShell.

Before you begin, make sure you've reviewed how to [plan, build, and launch a home site](./home-site-plan.md). 

> [!NOTE]
>- Targeted Release customer will have the option to [set a communication site as a home site in the SharePoint admin center](/SharePoint/home-site-admin-center) in September. This feature will become available to all customers on September 20 2021.
>- You can set only one site in your organization as a home site. The site can be registered as a hub site, but can't be associated with a hub. The first time you set up a home site, it might take up to several minutes for the changes to take effect. If you run the command again to switch your home site to a different site, it might take up to 2 hours.

## Set a site as your home site

After you create and customize the communication site that you want to use as your home site, you need to run a PowerShell cmdlet to set it as your home site. To run this cmdlet, you must be a site admin of the site.

> [!IMPORTANT] 
> - If the site you want to be your home site isn't currently your root site and you want it to be, first [replace your root site with the site](modern-root-site.md), and then make the site your home site. 

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run `Set-SPOHomeSite -HomeSiteUrl <siteUrl>`.

    (Where siteUrl is the site you want to use)
    
> [!TIP]
> After you set your home site, you might want to [enable and customize the global navigation](sharepoint-app-bar.md#customize-global-navigation-in-the-app-bar). 

## Remove a site as your home site

If you remove a site as your home site:

- The Home button will be removed from the Find tab of the SharePoint mobile app.
- If you enabled global navigation, the global navigation pane will be removed from the SharePoint app bar.
- Search will be scoped to the site only.

To remove the site as your home site, run `Remove-SPOHomeSite`.

The site will continue to be an organization news site. To remove it as an organization news site, see [Create an organization news site](organization-news-site.md).
