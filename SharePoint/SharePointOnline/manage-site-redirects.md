---
title: "Manage site redirects"
ms.reviewer: adwood
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- MET150
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
description: "This article contains information on how to manage site redirects in SharePoint. You'll learn how to view and delete site redirects."
---

# Manage site redirects 

As part of [changing a SharePoint site address](change-site-address.md), [moving a site to a different geo location](/office365/enterprise/move-sharepoint-between-geo-locations), or [swapping a site](modern-root-site.md#replace-your-root-site), we automatically create redirects to ensure that links pointing to the prior URL continue to work. These redirects are sites that use a special site template at the prior site URL.

For example, if you changed a site address from https://<i></i>contoso.sharepoint.<i></i>com/sites/*OldSiteName* to https://<i></i>contoso.sharepoint.<i></i>com/sites/*NewSiteName* or moved a site from https://<i></i>*contoso*.sharepoint.<i></i>com/sites/SiteName to https://<i></i>*contosoEUR*.sharepoint.<i></i>com/sites/SiteName, we'll place a redirect (Template type REDIRECTSITE#0) at the old URL, which contains special headers and logic to redirect your browser requests to the new site.

In some cases, you might want to free up the old URL to use it for a new site. To do this, you need to delete the redirect.

> [!NOTE]
> After you delete a redirect, any request to that URL won't get redirected. This means that any bookmarks, links, or Shared With Me references will not be routed to the new URL.

## To remove a redirect 

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

    ```PowerShell
    Remove-SPOSite -Identity https://contoso.sharepoint.com/sites/OldSiteName
    ```

4. When prompted, confirm that you want to delete the redirect. 

To confirm that the redirect has been deleted, browse to the URL. It should return a 404 error. You can also run `Get-SPOSite -Identity https://contoso.sharepoint.com/sites/OldSiteName`. It will return that we cannot get the site.

> [!NOTE]
> You might need to clear the history in your browser before browsing to the URL.

## To get a list of all redirect sites

Run the following command.
 
 ```PowerShell
 Get-SPOSite -Template REDIRECTSITE#0
 ```


