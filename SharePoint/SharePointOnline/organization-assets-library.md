---
title: "Create an organization assets library"
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Specify a library as a location for assets that are centrally stored and managed in your organization."
---

# Create an organization assets library

If your organization needs to store and manage images like photos or logos centrally for all your users to use, you can specify one or more document libraries as an "organization assets library." This makes it easier for users to add these assets when they create SharePoint sites and pages.

> [!NOTE]
> This feature is not available for Office 365 Germany, Office 365 operated by 21Vianet (China), or Office 365 US Government plans. <br>You can specify up to 30 organization asset libraries for a single organization, however all of these asset libraries must reside in the same site collection. You cannot add organization asset libraries from multiple site collections.

When a user adds a web part to any modern page in SharePoint and that web part opens the file picker, the user can select "Your organization" in the left pane to browse the libraries you've specified. 

## Use Microsoft PowerShell to specify a library as an organization assets library
  
1. Select an existing site or create a new site for the organization assets.

> [!NOTE]
> All organization asset libraries must be on the same site.

2. Upload the files you want to make available to all users to a document library.

3. [Download the latest SharePoint Online Management Shell version](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
4. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
5. Run the following command to designate the document library as an organization assets library:
  
    ```PowerShell
    Add-SPOOrgAssetsLibrary -LibraryURL <String> [-ThumbnailURL <String>] 
    ```

LibraryURL is the absolute URL of the library to be designated as a central location for organization assets. ThumbnailURL is the URL for the image file that you want to appear in the card's background in the file picker; this image must be on the same site as the library. The name publicly displayed for the library will be the name of the library on the SharePoint site. [Learn more about the Add-SPOOrgAssetsLibrary cmdlet](/powershell/module/sharepoint-online/add-spoorgassetslibrary)

Example: `Add-SPOOrgAssetsLibrary -LibraryURL https://contoso.sharepoint.com/sites/branding/Assets -ThumbnailURL https://contoso.sharepoint.com/sites/branding/Assets/contosologo.jpg`


> [!NOTE]
> Adding an organization assets library will enable a content delivery network (CDN) for your organization to provide fast and reliable performance for shared assets. You'll be prompted to enable CDN for each organization asset library you add. Vanity domains are currently not supported. [More info about CDNs](/office365/enterprise/content-delivery-networks)

 
## Related commands 

- See information about all organization asset libraries on the site: `Get-SPOOrgAssetsLibrary` [Learn more about this cmdlet](/powershell/module/sharepoint-online/get-spoorgassetslibrary) 
- Update thumbnail URL: `Set-SPOOrgAssetsLibrary -LibraryUrl <String> -ThumbnailUrl <String>` [Learn more about this cmdlet](/powershell/module/sharepoint-online/set-spoorgassetslibrary) 
- Remove a library: `Remove-SPOOrgAssetsLibrary -LibraryUrl <String>` [Learn more about this cmdlet](/powershell/module/sharepoint-online/remove-spoorgassetslibrary)
