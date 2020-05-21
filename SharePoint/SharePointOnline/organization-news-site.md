---
title: "Create an organization news site"
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
- SPO160
- MET150
ms.collection:  
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
description: "In this article, you'll learn how to specify a site as an official or authoritative organization news site."
---

# Create an organization news site

To specify sites as "official" or "authoritative" for news in your organization, mark them as organization news sites. These posts get special visual treatment (see the "NEWS @ CONTOSO" color block below), and appear on the SharePoint start page. 

![A post from an organization news site on the SharePoint start page](media/c9335bc4-6be2-41e8-bd53-bf32a946d179.png)

SharePoint admins can specify any number of organization news sites. For multi-geo tenants, organization news sites would have to be set up for each geo location. Each geo location could use the same central organization news site, and/or have its own unique site that shows organization news specific to that region.

> [!NOTE]
> When SharePoint home sites are released, they will be automatically configured as organization news sites.

For more info about working with news, see [Use the News web part on a SharePoint page](https://support.office.com/article/C2DCEE50-F5D7-434B-8CB9-A7FEEFD9F165) and [Add news posts](https://support.office.com/article/495f8f1a-3bef-4045-b33a-55e5abe7aed7). 

## Use Microsoft PowerShell to specify a site as an organization news site
  
1. [Download the latest SharePoint Management Shell version](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Management Shell, go to Add or remove programs and uninstall "SharePoint Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 
    
2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365.

    To learn how, see [Getting started with SharePoint Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command to designate the site as an organization news site:
  
    ```PowerShell
    Set-SPOOrgNewsSite -OrgNewsSiteUrl <site URL> 
    ```

Example: `Set-SPOOrgNewsSite -OrgNewsSiteUrl https://contoso.sharepoint.com/sites/Marketing`

## Related commands 

- View a list of all your organization news sites: [Get-SPOOrgNewsSite](/powershell/module/sharepoint-online/get-spoorgnewssite) 
- Remove a site from the list of organization news sites: [Remove-SPOOrgNewsSite](/powershell/module/sharepoint-online/remove-spoorgnewssite)
