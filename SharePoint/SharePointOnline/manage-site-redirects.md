---
title: "Manage site redirects in SharePoint Online"
ms.reviewer: adwood
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
description: "Learn how to remove a site redirect in SharePoint Online."
---

# Manage site redirects in SharePoint Online

As part of changing your [SharePoint Online site address](change-site-address.md) and [moving a SharePoint Online site to a different geo location for Multi-Geo tenants](https://docs.microsoft.com/en-us/office365/enterprise/move-sharepoint-between-geo-locations), we automatically create redirect sites to ensure that links pointing to the prior site address continue to work. These redirect sites are a special site template in the prior site URL.

For example, if you renamed a site https<i></i>://contoso<i></i>.sharepoint.i></i>com/sites/*OldSiteName* to https<i></i>://contoso.sharepoint.i></i>com/sites/*NewSiteName* or cross-geo moved a site https<i></i>://contoso.sharepoint.i></i>com/sites/SiteName to https<i></i>://contoso*EUR*.sharepoint.i></i>com/sites/SiteName, we will place a redirector site (Template type REDIRECTSITE#0) associated to the old namespace, which contains special headers and logic to redirect your browser requests to the new renamed site.

In some cases, you may want to free up the old namespace to place another site in that address; to do that, you may delete the redirect site.

> [!NOTE]
> Once you delete a redirect site, any request to that site address will not get redirected. This means that bookmarks, links, or Shared With Me references from prior to the rename or move will not be routed to the new address.

## To Remove a Redirect Site

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
1. `Remove-SPOSite -Identity https://contoso.sharepoint.com/sites/OldSiteName`
1. At the confirmation prompt, select **Y**.
4. After you have removed the site, you may `Get-SPOSite -Identity https://contoso.sharepoint.com/sites/OldSiteName` to confirm that the site was removed. This will return that we cannot get the site. Also, if you try to navigate to the site, you will get a 404 response.

> [!NOTE]
> Some browsers may cache the site; thus, you should manually clear your cache before seeking to access the redirect.

## To get a list of redirect sites

1. Connect to the SharePoint Admin Center in the location where the site is hosted.
2. `Get-SPOSite -Template REDIRECTSITE#0`

This will return a list of all redirect sites.
