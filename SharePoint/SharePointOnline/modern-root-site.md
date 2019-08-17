---
title: "Modernize your root site"
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

# Modernize your root site
  
Previously, when SharePoint was set up for an organization, a classic team site was created as the root (or top-level) SharePoint site. Now, a communication site is set up as the root site for new organizations. If your environment was set up before April 2019, you can change your root site to a modern site in one of three ways:

- Enable the modern site pages library experience and set a modern page as the home page of the root site. This gives users a modern team site experience with the left navigation. 
- If you have a different site that you want to use as your root site, you can replace (swap) the root site with it.
- To keep using the content on the site, you can convert the existing site to a communication site. 

## What's the root site?

The root site is one of the site collections provisioned automatically for an organization when they signup for any Office 365 or Microsft 365 products that include a SharePoint license. Typically that site's URL is of the format .sharepoint.com. 

## Swap your root site

Before you begin, make sure you:

1. Ensure that the source site that you want to swap to the root has followed the recommended guidance. [Building SharePoint Online portals](/sharepoint/dev/solution-guidance/portal-overview) 
2. Note any "Featured links" that have been added on the SharePoint start page. You'll need to add them again after the swap. [Learn how](change-links-list-on-sharepoint-home-page.md)
3. Review your source site to make sure it has the same policies, permissions, and external sharing settings as your current root site.

> [!NOTE]
> If you've enabled auditing, the following events can be recorded :
<br> Scheduled site swap: A site swap was scheduled at this time
<br> Swapped site: A site swap completed successfully at this time
<br> Failed site swap: A site swap failed at this time and will not retry
 
### Limitations

- Only sites within the same domain, for example, https://contoso.sharepoint.com can be swapped.
- The source site must be a modern team site (STS#3), a communication site (SITEPAGEPUBLISHING#0), or a classic team site (STS#0).
- The source and target sites can't be connected to an Office 365 group or associated with a hub. 
  
### Run the PowerShell cmdlet

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run Invoke-SPOSiteSwap.

```PowerShell
Invoke-SPOSiteSwap -SourceUrl https://contoso.sharepoint.com/sites/CommunicationSite -TargetUrl https://contoso.sharepoint.com -ArchiveUrl https://contoso.sharepoint.com/sites/Archive
```

(Where SourceUrl is the site you want to use, TargetUrl is the root site you want to replace, and ArchiveUrl is the location where you want to archive the current root site.)

For more info about this cmdlet, see [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap).

### Known issues with swapping sites

- The target site may return a "not found" (HTTP 404) error for a short period of time.
- Content will need to be recrawled to update the search index for the sites that have been swapped. This may take a period of time depending on various factors such as the amount of content in these sites. Anything dependent on the search index, may return incomplete results until the swapped sites have been recrawled.
- Anything dependent on "static" links (such as File Sync and OneNote files) will need to be manually corrected.
- If the source site was an organizational news site, update the URL. [Get a list of all organizational news sites](/powershell/module/sharepoint-online/get-spoorgnewssite?view=sharepoint-ps)
- Project Server sites may need to be validated to ensure that they are still associated correctly.

## Convert your root site to a communication site

When you convert your root site to a communication site:

- A new modern home page will be created for the root site (only the site at the root, not any subsites)
- Full-width pages with horizontal navigation will be available (the top navigation from classic view will be hidden, but can be seen on classic pages like the Site settings page)
- Custom script will be disabled
- Minor Versioning on the Site Pages library will be enabled
- Site Pages will be the default content type in the Site Pages library

The permissions and content of the root site won't be changed.

### Limitations

- The root site can be converted to a communication site only if the classic publishing feature was never turned on. 
- The root site must have quick launch site navigation enabled. [Learn how to do this](https://support.office.com/article/c040f014-acbb-4c98-8174-48428cf02b25)


### Run the PowerShell cmdlet

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run Enable-SPOCommSite.

```PowerShell
Enable-SPOCommSite -SiteUrl https://contoso.sharepoint.com
```

For more info about this cmdlet, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). 
