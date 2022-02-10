---
title: "Supporting Custom Organization Fonts in the PowerPoint for web"
ms.reviewer: 
ms.author: v-shesna
author: sheshachary
manager: serdars
recommendations: true
ms.date: 01/31/2022
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
description: "Learn how to add organization fonts to the SharePoint as Organization Asset Libraries."
---

# Support for Organization Fonts in PowerPoint for web 
Organization fonts allow customers to create a brand for their organizations and encourage consistency in documents and presentations. Earlier, organization users could only see and use organization fonts when they were installed locally on their desktops. Now, customers with E3 or E5 licenses can take advantage of Organization Font Support in PowerPoint for the web to edit and display their fonts. When you upload your font as a SharePoint Organization Asset Library (OAL), you'll see that your organization font now renders properly on PowerPoint for the web. Seamless support for the desktop experiences is coming soon.

> [!NOTE]
>- Organization font support on PowerPoint for the web is not available for Office 365 Germany, Office 365 operated by 21Vianet (China), or Microsoft 365 US Government plans.


## How does this work? 
The following diagram outlines the key steps in making our solution work: 

   :::image type="content" source="media/Company-admin.png" alt-text="Manage User Properties link under Admin user profiles.":::

1. Organization administrator uploads their fonts to their organization's SharePoint site using the **SharePoint Online Management Shell.**
2. SharePoint stores the assets in a [public Office 365 Content Delivery Network.](/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo?view=o365-worldwide&preserve-view=true) 
3. When a user opens a PowerPoint file on the web platform, PowerPoint for the web will access the Content Delivery Network (CDN) and fetch appropriate fonts.

## Adding organization fonts to SharePoint as organization asset library 
1. [Create a new site](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.microsoft.com%2Foffice%2Fcreate-a-site-in-sharepoint-4d1e11bf-8ddc-499d-b889-2b48d10b1ce8&data=04%7C01%7Cv-shesna%40microsoft.com%7C469dfcba67174de505e308d9e01e0779%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637787241955790760%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=IIR6K8%2F9ZBRVrOD%2B2ZuYwMdBybeufNE3sI22zSCfCJE%3D&reserved=0) or use your existing site for Organization Asset Libraries.

     > [!NOTE]
     > You cannot customize the permissions of font organization asset libraries as the fonts are hosted in a public CDN. When uploaded, font asset libraries are available across your entire tenant. Currently, sub-group permissioning of font asset libraries are not supported.

2. Navigate to your site’s home page. From the **New** dropdown menu, select **Create a Document Library** and name your new font library.

   :::image type="content" source="media/new-drop-down.png" alt-text="New drop-down option":::

   :::image type="content" source="media/create-document-library.png" alt-text="Create and name your font library":::

3. [Download the latest version of the SharePoint Online Management Shell.](https://go.microsoft.com/fwlink/p/?LinkId=255251)
4. Using the **SharePoint Online Management Shell**, run the following command to designate the library as custom fonts asset library.

      `Add-SPOOrgAssetsLibrary -LibraryUrl <New Document Library SharePoint URL> -OrgAssetType OfficeFontLibary -CdnType Public`

      For example:
     
     `Add-SPOOrgAssetsLibary -LibraryUrl https://constosofonts.sharepoint.com/FontLibrary -OrgAssetType OfficeFontLibary -CdnType Public`.
5. Using the **SharePoint Online Management Shell**, run the following command to upload your custom font(s) to the document library location.

    `Set-SPOCustomFontCatalog -FontFolder <Local Font Folder Location> -LibraryUrl <Document Library SharePoint URL>`

      For example:

    `Set-SPOCustomFontCatalog -FontFolder “C:\ProgramData\Fonts" -LibraryUrl https://contosofonts.sharepoint.com/FontLibrary`

     Allow 24 hours for Sharepoint servers to update and for users in your organization to see their organization fonts when using the **Font** dropdown menu in PowerPoint for the web.

## Important notes on features and its release

### Feature notes
- Updates to organization font asset libraries can take up to 24 hours to propagate and become broadly available.
- You should only use the **SharePoint Online Management Shell** commands to make changes. Any changes made using the **Document Library SharePoint Web** won't reflect in your font libraries.
- The uploaded organization fonts will only be usable and viewable within your organization. To share them externally, you need to [embed fonts into your PowerPoint presentations.](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.microsoft.com%2Fen-us%2Foffice%2Fembed-fonts-in-documents-or-presentations-cb3982aa-ea76-4323-b008-86670f222dbc&data=04%7C01%7Cv-shesna%40microsoft.com%7C9cf273bbf9c14d337ec208d9df961a78%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637786658092612309%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=idoG67fR3e7njA8RslxUn71i7Yfqq4q%2F7eH%2FJzScVdk%3D&reserved=0)
- This feature is only available on PowerPoint for the web. Support for Windows, Mac, and Mobile are coming soon. In the meantime, continue to [download and install custom fonts to use with Office.](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.microsoft.com%2Fen-us%2Ftopic%2Fdownload-and-install-custom-fonts-to-use-with-office-0ee09e74-edc1-480c-81c2-5cf9537c70ce&data=04%7C01%7Cv-shesna%40microsoft.com%7C9cf273bbf9c14d337ec208d9df961a78%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637786658092612309%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=EvcPAJtCguowz%2Ff7MF29rXEdN8MWMYwrD1c%2BQIcR3lM%3D&reserved=0)

### Licensing considerations 

> [!WARNING]
> By using this feature and publishing font files, a font catalog file will be created. The newly created font catalog files will be publicly stored, along with the fonts, in the cloud and will not respect the site classification guidelines if the Organization Asset Library is hosted in Restricted SharePoint Site. The font catalog files will contain font names and other font related metadata. Please note that the files will be accessible to anyone, including persons external to your organization, who are able to extract the URLs that point to them.

These newly created files can be deleted by you. If deleted, the feature will not work as expected.

Do not use this feature if your fonts contain proprietary information, or if they have license usage restrictions, such as restrictions on cloud hosting, or your organization isn't comfortable making the fonts publicly available.

