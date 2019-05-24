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

If your organization needs to store and manage files like templates, photos, or logos centrally for all your users to use, you can specify one or more document libraries as an "organization assets library."

> [!NOTE]
> Currently, all organization asset libraries must be on the same site.  

When a user adds a web part to any modern page in SharePoint and that web part opens the file picker, the user can select "Your organization" in the left pane to browse the libraries you've specified. 

## Use Microsoft PowerShell to specify a library as an organization assets library
  
1. Select an existing site or create a new site for the organization assets.

2. Upload the files you want to make available to all users to the document library.

3. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
4. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
5. Run the following command:
  
    ```PowerShell
    Add-SPOOrgAssetsLibrary [[-LibraryURL] <Object>] [[-ThumbnailURL] <Object>] 
    ```

> [!NOTE]
> We use a content delivery network (CDN) for organization assets to provide improved performance. Assets are stored on servers closer to the browsers requesting them, which helps speed up downloads and reduce latency. This won't affect other aspects of your organization unless you explicitly opt in. When you specify your first organization assets library, you'll see two confirmations - one to allow CDN in your organization, and another to specifically enable CDN for that library. For every new library you add, you'll see a confirmation to specifically enable CDN for that library. 
Example: `Add-SPOOrgAssetsLibrary -LibraryURL https://contoso.sharepoint.com/sites/branding/Products -ThumbnailURL https://contoso.sharepoint.com/sites/branding/Products/surfacestudio.jpg`    
 
Other useful commands: 

- See existing associated libraries, if any: `Get-SPOOrgAssetsLibrary` 
- Update thumbnail URL: `Set-SPOOrgAssetsLibrary [[-LibraryURL] <Object>] [[-ThumbnailURL] <Object>]` 
- Remove a library: `Remove-SPOOrgAssetsLibrary [[-LibraryURL] <Object>]` 
 
## Known issues

- After you specify the first organization assets library, it may take some time for the “Your organization” option to appear in the file picker. 
- If you change the thumbnail, it may take about 15 minutes for the change to appear in the file picker. 
- When you specify an organization assets library, you may see the error, “Value cannot be longer than 5000.” This means you have specified the maximum number of organization assets libraries. To add a new library, remove an existing one.   

