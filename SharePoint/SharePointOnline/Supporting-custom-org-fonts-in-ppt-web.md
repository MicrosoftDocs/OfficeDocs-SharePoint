---
title: "Supporting Custom Organization Fonts in the PowerPoint for web"
ms.reviewer: 
ms.author: Sheshachary
author: Sheshachary
manager: Clay Detels
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
ms.assetid: 187b73a8-02b5-4aa2-9db6-3b62cf2b8cd9
description: "Learn how to add customized fonts in to the SharePoint as Organization Asset Libraries."
---

# Supporting Custom Organization Fonts in PowerPoint for web 
Custom fonts allow customers to create a brand for their organizations to encourage consistency in the documents and presentations. Previously, users within organizations could only see and use their custom fonts on the Desktop experiences with fonts installed locally on organization machines. Now, customers with an E3 or E5 license can take advantage of <b>Custom Font Support</b> on PowerPoint for displaying new web fonts. Upload your font as a SharePoint OAL and observe your font has rendered properly on PowerPoint for the web. Seamless support for the desktop experiences is coming soon. 

## How does this work? 
The diagram below outlines the key steps in making our solution work: 

   ![Manage User Properties link under Admin user profiles.](media/Company-admin.png)

1. Company admin uploads their fonts to their company’s SharePoint site using the <b>SharePoint Online Management Shell.</b>
2. SharePoint stores the assets in a [public Office 365 Content Delivery Network.](https://docs.microsoft.com/en-us/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo?view=o365-worldwide) 
3. Users in the company will open a PowerPoint file on the web platform, PowerPoint for the web will fetch the appropriate fonts by accessing the CDN, when needed. 
4. PowerPoint for the web will render the fonts correctly on all web-based experiences. 

## Adding custom fonts to SharePoint as organization asset libraries 
1. [Create a new site](https://support.microsoft.com/en-us/office/create-a-site-in-sharepoint-4d1e11bf-8ddc-499d-b889-2b48d10b1ce8) or use your existing site for organization asset libraries and set permissions. 
2. Create a new document library for your custom font.
  
   ![Login to document library with your credentials](media/create-document-library.png)
3.	Using the <b>SharePoint Online Management Shell,</b> run the following commands to designate the library as a font organization asset library. 

      ```Add-SPOOrgAssetsLibary -LibraryUrl <New Document Library SharePoint URL> -OrgAssetType OfficeFontLibary -CdnType Public```
 
     For example: 

      ```Add-SPOOrgAssetsLibary -LibraryUrl “https://constosofonts.sharepoint.com/FontLibrary” -OrgAssetType OfficeFontLibary -CdnType Public``` 
 
4.	Using the <b>SharePoint Online Management Shell,</b> run the following command to upload your custom font to the document library location you just created. 

     ```Set-SPOCustomFontCatalog -FontFolder <Local Font Folder Location>  -LibraryUrl <Document Library SharePoint URL> ```
 
     For example: 

     ```Set-SPOCustomFontCatalog -FontFolder “C:\ProgramData\Fonts” -LibraryUrl “https://contosofonts.sharepoint.com/FontLibrary” ```

## Important notes on features and its release
- This feature/support will be available in the PowerPoint for the web in the month of February 2022. Subsequent endpoints supporting this feature are: 
  - Windows Desktop – March 2022 
  - Mac + mobile – June 2022 
- Updates to font organization asset libraries can take-up to 24 hours to update across your organization. 
- This feature supports only TTF and OTF font filetypes. 
- Do not use the <b>Document Library SharePoint Web UI</b> for making changes to your font libraries, these changes will not be reflecting. Use only the <b>SharePoint Online Management Shell</b> commands to make changes.
  - Only use the Remove-SPOOrgAssetsLibrary command to remove an Office Font Library. 
- Your custom fonts will only be available internally, and external users will not be able to render or use your custom font.

## Public CDNs and licensing 
In general, custom fonts for <b>public</b> will be stored in a cloud location, and it will not be accessible. In this scenario, public means - access to those assets is anonymous and unauthenticated. Whenever a user requests the custom font, we do not check for company specific authentication each time. However, to gain access to your fonts, those outside of your company would need to maliciously reconstruct or guess the URL location of your font and then spoof the request through an approved list of hosts (PPT, SharePoint, and Teams). Even, if they can guess the URL of your fonts, they are unable to simply plug the URL into their browsers to download the fonts. 
