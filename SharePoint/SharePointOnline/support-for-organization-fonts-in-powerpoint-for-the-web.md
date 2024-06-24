---
title: "Support for organization fonts in PowerPoint and Word"
ms.reviewer:
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 06/24/2024
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
description: "Learn how to add organization fonts to the SharePoint as Organization Asset Libraries."
---

# Support for organization fonts in PowerPoint and Word

Organization fonts allow customers to create a brand for their organizations and encourage consistency in documents and presentations. Earlier, organization users could only see and use organization fonts when they were installed locally on their desktops. Now, customers with E3 or E5 licenses can take advantage of Organization Font Support in PowerPoint for the web to edit and display their fonts. When you upload your font as a SharePoint Organization Asset Library (OAL), you'll see that your organization font now renders properly on PowerPoint and Word.

> [!NOTE]
> Organization font support on PowerPoint and Word is not available for Office 365 Germany, Office 365 operated by 21Vianet (China), or Microsoft 365 US Government plans.
## How does this work?

The following diagram outlines the key steps in making our solution work (PPT is used as an example in this diagram):

   :::image type="content" source="media/companyadmin.png" alt-text="image of Admin user profiles":::

1. Organization administrator uploads their fonts to their organization's SharePoint site using the **SharePoint Online Management Shell.**
2. SharePoint stores the assets in a [public Office 365 Content Delivery Network.](/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo?view=o365-worldwide&preserve-view=true)
1. When a user opens a PowerPoint or Word file on the web platform, the web Application will access the Content Delivery Network (CDN) and fetch appropriate fonts.

## Adding organization fonts to SharePoint as an organization asset library

1. [Create a new SharePoint site](https://support.microsoft.com/office/create-a-site-in-sharepoint-4d1e11bf-8ddc-499d-b889-2b48d10b1ce8) or use your existing site for Organization Asset Libraries.

     > [!NOTE]
     > You cannot customize the permissions of font organization asset libraries as the fonts are hosted in a public CDN. When uploaded, font asset libraries are available across your entire tenant. Currently, sub-group permissioning of font asset libraries are not supported.

2. Ensure that your administrator account has **Full control** permissions to the SharePoint site you are using for your Organization Asset Libraries.

   :::image type="content" source="media/fullcontrol.png" alt-text="Full Control image":::

3. Ensure the site permissions for **Everyone except external user** are set to **Read** or **Edit.**

    :::image type="content" source="media/sitepermissions.png" alt-text="image of sitepermissions" lightbox="media/sitepermissions.png":::

    :::image type="content" source="media/userpermission.png" alt-text="image of userpermissions":::

4. Navigate to your site's home page. From the **New** dropdown menu, select **Create a Document Library** and name your new font library.

   :::image type="content" source="media/new-dropdown.png" alt-text="New drop-down option" lightbox="media/new-dropdown.png":::

   :::image type="content" source="media/createdocumentlibrary.png" alt-text="Create and name your font library" lightbox="media/createdocumentlibrary.png":::

5. [Download the latest version of the SharePoint Online Management Shell.](https://go.microsoft.com/fwlink/p/?LinkId=255251)
6. [Connect your SharePoint Management Shell with your administrator username and password.](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online)
7. Using the **SharePoint Online Management Shell**, run the following command as an administrator to designate the library as custom fonts asset library.

      `Add-SPOOrgAssetsLibrary -LibraryUrl <New Document Library SharePoint URL> -OrgAssetType OfficeFontLibrary -CdnType Public`

      For example:

     `Add-SPOOrgAssetsLibrary -LibraryUrl https://constosofonts.sharepoint.com/FontLibrary -OrgAssetType OfficeFontLibrary -CdnType Public`

    > [!NOTE]
    >
    > - Only include the direct path of your font library. The trailing `/AllItems.aspx` should not be included in your Library URL.
    > - Font asset libraries must be designated with `-CdnType Public`.

1. Using the **SharePoint Online Management Shell**, run the following command as an administrator to upload your custom font(s) to the document library location.

      ```powershell
   Set-SPOCustomFontCatalog -FontFolder <Local Font Folder Location> -LibraryUrl <Document Library SharePoint URL>
   ```

      For example:

      ```PowerShell
   Set-SPOCustomFontCatalog -FontFolder "C:\ProgramData\Fonts" -LibraryUrl https://contosofonts.sharepoint.com/FontLibrary
   ```

      > [!NOTE]
   >
   > - Your font folder should be the directory holding all your font files and should not include any non-font files.
   > - You may be re-prompted to enter your credentials at this step.

   Allow 24-hours for the SharePoint servers to update and for the users in your organization to see their organization fonts when using the **Font** dropdown menu in PowerPoint and Word for the web.
   
   :::image type="content" source="media/font_dropdown.png" alt-text="t":::

## Important notes on features and its release

### Feature notes

- Updates to organization font asset libraries can take up to 24 hours to propagate and become broadly available.
- If you need to change your font asset library, you will need to [remove the font asset library](/powershell/module/sharepoint-online/remove-spoorgassetslibrary) using the [```Remove-SPOOrgAssetsLibrary``` command](/powershell/module/sharepoint-online/remove-spoorgassetslibrary). Repeat the process above to upload your updates in the font files. Changes made to the Document Library on the SharePoint web platform may affect font availability and feature functionality.
- The uploaded organization fonts will only be usable and viewable within your organization. To share them externally, you need to [embed fonts into your PowerPoint presentations.](https://support.microsoft.com/office/benefits-of-embedding-custom-fonts-cb3982aa-ea76-4323-b008-86670f222dbc)

- This feature is only available on PowerPoint and Word on Web, Windows, Mac, and Mobile.

### Licensing considerations

> [!WARNING]
> By using this feature and publishing font files, a font catalog file will be created. The newly created font catalog files will be publicly stored, along with the fonts, in the cloud and will not respect the site classification guidelines if the Organization Asset Library is hosted in Restricted SharePoint Site. The font catalog files will contain font names and other font related metadata. Please note that the files will be accessible to anyone, including persons external to your organization, who are able to extract the URLs that point to them.
>
> These newly created files can be deleted by you. If deleted, the feature will not work as expected.
>
> Do not use this feature if your fonts contain proprietary information, or if they have license usage restrictions, such as restrictions on cloud hosting, or your organization isn't comfortable making the fonts publicly available.
