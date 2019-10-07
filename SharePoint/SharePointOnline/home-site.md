---
title: "Create a home site"
ms.reviewer: dipadur
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

description: "Create a home site for your organization."
---

# Create a home site
  
A home site is designed to be the landing page for your intranet portal. It's typically used as the [root site](modern-root-site.md) in your organization and is often a [hub site](create-hub-site.md). When you set a site as your home site:

- A link to it will appear from the SharePoint start page for any user that has access to the site.
- Users can easily navigate to the site from the SharePoint mobile app
- The search for the site is scoped to all sites within the organization.
- The site is automatically set up as an [organization news site](organization-news-site.md).

> [!IMPORTANT]
> Before you launch an intranet landing page, we strongly encourage you to [review the guidance about optimizing SharePoint performance](/office365/enterprise/tune-sharepoint-online-performance).

## Limitations

- The site you select must be a communication site that is not associated with a hub. It can't be a subsite. 
- This feature doesn't work if your organization has configured [Office 365 Multi-Geo](/office365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-office-365)
- SharePoint framework extensions will work on the home site, but not the SharePoint start page. 

## Run the PowerShell cmdlet

Before you begin, make you're a site admin of the site you want to set as your home site.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run Set-SPOHomeSite - HomeSiteUrl <siteUrl>.

    (Where siteUrl is the site you want to use)

> [!NOTE]
> The first time you set up a home site, it might take several minutes. If you're [changing the site address](change-site-address.md) of a home site, it might take up to 8 hours.


