---
title: "Supporting Custom Organization Fonts in the PowerPoint for web"
ms.reviewer: 
ms.author: v-shesna
author: sheshachary
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
description: "Learn how to add customized fonts to the SharePoint as Organization Asset Libraries."
---

# Supporting Custom Organization Fonts in PowerPoint for web 
Custom fonts allow customers to create a brand for their organizations and encourage consistency in documents and presentations. Earlier, organization users could only see and use custom font when they were installed locally on their desktops. Now, customers with an E3 or E5 license can take advantage of **Custom Font Support** on PowerPoint for editing and displaying their fonts. When you upload your font as a SharePoint OAL, you will see that your custom font now renders properly on PowerPoint for the web. Seamless support for the desktop experiences is coming soon. 

## How does this work? 
The following diagram outlines the key steps in making our solution work: 

   :::image type="content" source="media/Company-admin.png" alt-text="Manage User Properties link under Admin user profiles.":::

1. Company administrator uploads their fonts to their company’s SharePoint site using the **SharePoint Online Management Shell.**
2. SharePoint stores the assets in a [public Office 365 Content Delivery Network.](/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo?view=o365-worldwide&preserve-view=true) 
3. When a user opens a PowerPoint file on the web platform, PowerPoint for the web will access the CDN and fetches appropriate fonts.

## Adding custom fonts to SharePoint as organization asset libraries 
1. [Create a new site](https://support.microsoft.com/office/create-a-site-in-sharepoint-4d1e11bf-8ddc-499d-b889-2b48d10b1ce8) or use your existing site for organization asset libraries and set permissions. 
2. Create a new document library for your custom font.
  
   :::image type="content" source="media/create-document-library.png" alt-text="Login to document library with your credentials":::
3.	To choose the library as font organization asset library, use the **SharePoint Online Management Shell,** and run the following command: 

      ```Add-SPOOrgAssetsLibrary -LibraryUrl <New Document Library SharePoint URL> -OrgAssetType OfficeFontLibary -CdnType Public```
 
     For example: 

      ```Add-SPOOrgAssetsLibary -LibraryUrl “https://constosofonts.sharepoint.com/FontLibrary” -OrgAssetType OfficeFontLibary -CdnType Public``` 
 
4.	To upload your custom font to the document library location you created, use the **SharePoint Online Management Shell,** and run the following command:

     ```Set-SPOCustomFontCatalog -FontFolder <Local Font Folder Location>  -LibraryUrl <Document Library SharePoint URL> ```
 
     For example: 

     ```Set-SPOCustomFontCatalog -FontFolder “C:\ProgramData\Fonts” -LibraryUrl “https://contosofonts.sharepoint.com/FontLibrary” ```

## Important notes on features and its release
- This feature or support will be available in PowerPoint for the web in the month of February 2022. Following endpoints are supporting this feature: 
  - Windows Desktop – March 2022 
  - Mac + mobile – June 2022 
- Updates to font organization asset libraries takes 24 hours to update across your organization. 
- This feature supports only TTF and OTF font filetypes. 
- Don't use the **Document Library SharePoint Web UI** for making changes to your font libraries, these changes won't reflect. Use only the **SharePoint Online Management Shell** commands to make changes.
  - Only use the `Remove-SPOOrgAssetsLibrary` command to remove an Office Font Library. 
- Your custom fonts will only be available internally, and external users can't render or use your custom font.

## Public CDNs and licensing 
In general, custom fonts for **public** will be stored in a cloud location, and it won't be accessible for public. In this scenario, **public** means - access to asset is anonymous and unauthenticated. Whenever a user requests the custom font, we don't check for company specific authentication. However, to gain access for your custom fonts, users outside of your company need to maliciously reconstruct or guess the URL location of your font. Later, spoof the request through an approved list of hosts (PPT, SharePoint, and Teams). If users can guess the URL of your custom fonts, they're unable to plug the URL into their browsers to download the custom fonts.