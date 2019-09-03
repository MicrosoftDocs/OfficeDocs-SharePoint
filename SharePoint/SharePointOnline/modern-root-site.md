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
  
When SharePoint is set up for an organization, a root (or top-level) site is created. Before April 2019, the site was created as a classic team site. Now, a communication site is set up as the root site for new organizations. If your environment was set up before April 2019, you can modernize your root site three ways:

- If you have a different site that you want to use as your root site, or if you want to use a modern team site, [replace (swap) the root site](#swap-your-root-site) with it.
- If you want the content on your classic team site to be displayed with the layout of a communication site, [apply the communication site experience](#apply-the-communication-site-experience-to-the-root-site-coming-soon) to the root site. This feature isn't available yet, but is coming soon.
- If you want to continue using the classic team site, [enable the modern site pages library experience](/sharepoint/dev/transform/modernize-userinterface-lists-and-libraries) and [set a modern page as the home page](/sharepoint/dev/transform/modernize-userinterface-site-pages) of the root site. This gives users a modern team site experience with the left navigation.

> [!IMPORTANT]
> Before you launch an intranet landing page at your root site location, we strongly encourage you to [review the guidance about optimizing SharePoint performance](/office365/enterprise/tune-sharepoint-online-performance).

## What's the root site?

The root site for your organization is one of the sites that's provisioned automatically when you purchase and set up an Office 365 or Microsoft 365 plan that includes SharePoint. The URL of this site is typically *contoso*.sharepoint.com, and the owner is Company Administrator (all global admins in the organization). The root site can't be connected to an Office 365 group. 

> [!WARNING]
> Do not delete the root site for your organization. If you do, users won't be able to access any SharePoint sites until you restore the root site. 

## Swap your root site

Before you begin, make sure you:

1. Note any "Featured links" that have been added on the SharePoint start page. You'll need to add them again after the swap. [Learn how](change-links-list-on-sharepoint-home-page.md)
2. In the new SharePoint admin center, review your source site to make sure it has the same policies, permissions, and external sharing settings as your current root site.

If you've [turned on audit log search](/office365/securitycompliance/turn-audit-log-search-on-or-off), the following events can be recorded:

- Scheduled site swap: A site swap was scheduled at this time
- Swapped site: A site swap completed successfully at this time
- Failed site swap: A site swap failed at this time and won't be tried again
 
### Limitations

- Only sites within the same domain, for example, https://contoso.sharepoint.com can be swapped.
- The source site must be a modern team site (STS#3), a communication site (SITEPAGEPUBLISHING#0), or a classic team site (STS#0).
- All subsites contained with the source and target sites will be swapped.
- The source and target sites can't be connected to an Office 365 group. They also can't be hub sites or associated with a hub.<br>If a site is a hub site, unregister it as a hub site, swap the root site, and then register the site as a hub site. If a site is associated with a hub, disassociate the site, swap the root site, and then reassociate the site. [Learn how to manage hubs in the new SharePoint admin center](manage-sites-in-new-admin-center.md#change-a-sites-hub-site-association)
- Any sharing links or bookmarks will need to be recreated after the site swap.
  
### Run the PowerShell cmdlet

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run Invoke-SPOSiteSwap.

```PowerShell
Invoke-SPOSiteSwap -SourceUrl https://contoso.sharepoint.com/sites/CommunicationSite -TargetUrl https://contoso.sharepoint.com -ArchiveUrl https://contoso.sharepoint.com/sites/Archive
```

(Where SourceUrl is the site you want to use, TargetUrl is the root site you want to replace, and ArchiveUrl is the location where you want to archive the current root site.)

For more info about using this cmdlet and what happens with the previous root site, see [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap).

### Known issues with swapping sites

- The target site might return a "not found" (HTTP 404) error for a short time.
- Content must be recrawled to update the search index for the sites that have been swapped. This might take some time depending on factors such as the amount of content in these sites. Anything dependent on the search index might return incomplete results until the swapped sites have been recrawled.
- Anything dependent on "static" links (such as File Sync and OneNote files) will need to be manually updated.
- If the source site was an organizational news site, update the URL. [Get a list of all organizational news sites](/powershell/module/sharepoint-online/get-spoorgnewssite?view=sharepoint-ps)
- Project Server sites might need to be validated to make sure they're still associated correctly.

## Apply the communication site experience to the root site (coming soon)

When you apply the communication site experience to the root site:

- A new modern home page is created for the root site (only the site at the root, not any subsites)
- Full-width pages with horizontal navigation become available (the top navigation from classic view is hidden, but can be seen on classic pages like the Site settings page)
- [Custom script](allow-or-prevent-custom-script.md) is disabled
- Minor Versioning on the Site Pages library is enabled
- Site Pages are the default content type in the Site Pages library

The permissions and content of the root site aren't changed, and the root site still appears as having the template "team site (classic experience)" or STS#0.

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
