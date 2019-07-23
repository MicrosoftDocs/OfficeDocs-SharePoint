---
title: "Create a modern root site"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160

description: "Learn about modernizing the root site for your organization."
---

# Create a modern root site
  
Previously, when SharePoint was set up for an organization, a classic team site was created as the root (or top-level) SharePoint site. Now, a communication site is set up as the root site for new organizations. If your environment was set up before **DATE**, you can change your root site to a modern site in one of two ways:

- If you want to keep using the content on the site, you can convert the existing site to a communication site. For info, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). (You can do this only if you never turned on the classic publishing feature for the site.)
- If you have a different site that you want to use as your root site, you can replace (swap) the root site with it. For info, see [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap).
- 

## Before you swap your root site

1. Note any "Featured links" that have been added on the SharePoint start page. You'll need to add them again after the swap. [Learn how](change-links-list-on-sharepoint-home-page.md)
2. Review your source site to make sure it has the same policies, permissions, and external sharing settings as your current root site.

> [!NOTE]
> If you've enabled auditing, you can record the following events:
<br> SiteSwapScheduled: A site swap was scheduled at this time
<br> SiteSwapped: A site swap completed successfully at this time
<br> SiteSwapFailed: A site swap failed at this time and will not retry
 
## Limitations

- Only sites within the same domain, for example, https://<tenant-name>.sharepoint.com can be swapped.
- The source site must be either a Team Site (STS#0), a Modern Team Site (STS#3), or a Communication Site (SITEPAGEPUBLISHING#0).
- The source and target sites can't be connected to an Office 365 group or associated with a hub. 
  
## Run PowerShell commands to modernize the root site

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run either Enable-SPOCommSite or Invoke-SPOSiteSwap.

## Known issues with swapping sites

- The target site may return a "not found" (HTTP 404) error for a short period of time.
- Content will need to be recrawled to update the search index.
- Anything dependent on "static" links (such as File Sync and OneNote files) will need to be manually corrected.
- If the source site was an organizational news site, update the URL. [Get a list of all organizational news sites](/powershell/module/sharepoint-online/get-spoorgnewssite?view=sharepoint-ps)
- Project Server sites may need to be validated to ensure that they are still associated correctly.

