---
title: "Branding issues that may occur when upgrading to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f6a5ef4c-e49b-4f5e-bcfe-4df4c59b445f
description: "Learn how to address issues with branding, such as custom CSS, custom themes, and custom master pages, and custom page layouts in an upgraded site."
---

# Branding issues that may occur when upgrading to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
SharePoint 2013 introduces a new user interface that is lightweight, fast, and fluid. This UI is built by using new CSS styles, themes, and master pages. To get this new experience, you must upgrade to the new UI. But the significant changes that were made to support the new UI may break the upgrade story for some scenarios where you use custom branding.
  
In SharePoint 2010 Products, you may have branded your site in one of several different ways:
  
- Applying a custom style sheet to your site that overrides the SharePoint default styles.
    
- Applying a custom theme (THMX file) to your site.
    
- Copying and changing a master page that is included with SharePoint 2013.
    
- Creating a completely new custom master page in a publishing site, where the custom master page uses custom styles and is referenced by custom page layouts.
    
When you upgrade your site collection to SharePoint 2013, these types of customizations will not work as is because the default CSS styles, themes, and master pages have changed. Instead, you must create your custom branding again. This requires you to use the new styles, themes, or master pages available in SharePoint 2013, and then apply the newly re-created design to the upgraded site collection.
  
Changes to the default SharePoint styles, themes, and master pages were necessary to create a faster and more fluid user interface, and to make subsequent upgrades more predictable.
  
For this reason, if your site collection contains custom branding, we recommend that, before you upgrade, you first create an evaluation site collection where you can test and re-create your custom branding in a SharePoint 2013 environment. For more information about an evaluation site collection, see [Upgrade a site collection](upgrade-a-site-collection.md).
  
The following sections list branding issues that may occur when you upgrade to SharePoint 2013.
  
## Custom CSS

The most common way to apply custom branding to a SharePoint 2010 Products site is to create a CSS file that contains styles that override the default SharePoint styles.
  
To make the new UI faster and more fluid, SharePoint 2013 introduced fundamental changes in how CSS is implemented:
  
- CSS file sizes are reduced.
    
- Nesting of CSS selectors is limited.
    
- CSS inheritance is used whenever possible.
    
- Classes are defined in only one place.
    
- Related classes are grouped in the CSS file.
    
- Inline styles and the !mportant declaration are not used because they cannot be overridden.
    
- Styles use a consistent structure and naming convention.
    
In SharePoint 2013, styles use a consistent structure and naming convention.
  
|**NAMING PART**|**MS-**|**\<FEATURE\>-**|**\<NAME\>**|
|:-----|:-----|:-----|:-----|
|**Explanation** <br/> |Indicates this is a Microsoft class.  <br/> |The name of the feature with which this item is associated, or "core" if it's used as part of the core UI.  <br/> |A descriptive name of the item, such as title, link, and so on  <br/> |
   
Because of these changes in how SharePoint 2013 implements CSS, when you upgrade, custom CSS styles will not be applied to your site. To resolve this, you should first create an evaluation site collection and then use that site as the environment where you can identify the new SharePoint 2013 styles that you have to override. Create a CSS file for these styles, and then apply that CSS to your upgraded site.
  
## Custom theme

In SharePoint 2010 Products, you can use an Office program such as PowerPoint 2010 to create a THMX file. Then you can upload that theme file to SharePoint 2010 Products and apply the theme to your site. 
  
In SharePoint 2013, the theming engine was improved so that theming is faster and more flexible, and so that themes can be more easily upgraded moving forward. The theming model uses comment-style markup in the CSS and then replaces parts of the CSS based on parameters such as fonts and color schemes that users select. Themes in SharePoint 2013 are defined by XML files:
  
- SPColor.xml defines the color palette, in which slots now have semantic names so that it's more clear what UI elements will be affected when you change a color value. Also, themes now support setting opacity.
    
- SPFont.xml defines the font scheme and supports multiple languages, web-safe fonts, and web fonts.
    
But there is no support to upgrade a THMX file from SharePoint 2010 Products to SharePoint 2013. If you applied a custom theme to the SharePoint 2010 Products site, when you upgrade to SharePoint 2013, the theme files remain in place. But the theme is no longer applied to the site, and the site reverts to the default theme.
  
To resolve this, you should first create an evaluation site collection and then use the new theming features in SharePoint 2013 to create the theme again. For more information about the new themes, see the following articles on MSDN:
  
- [Themes overview in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=301983)
    
- [How to: Deploy a custom theme in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=301984)
    
- [Color palettes and fonts in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=301985)
    
- [How to: Create a master page preview file in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=301987)
    
> [!IMPORTANT]
> Moving forward, if you want to use custom branding, and if you want that branding to work after future upgrades, we recommend that you use themes to implement your design. Themes will have upgrade support when future updates are available. If themes don't work for your scenario or you must have more extensive branding, we recommend that you use a publishing site together with Design Manager. But understand that if you invest in building custom master pages and page layouts, you may have to rework or update your design files during and after each SharePoint upgrade. 
  
## Copy and change a master page that ships with SharePoint 2013

In SharePoint 2010 Products, a common way to make minor customizations to the UI is to copy and change a master page that ships with SharePoint 2010 Products. For example, you might change the master page to remove or hide capabilities from users.
  
When you upgrade a SharePoint 2010 Products site to SharePoint 2013, the master page is reset to use the default master page in SharePoint 2013. Therefore, after upgrade, your site will display its custom branding. The custom master page that was created in SharePoint 2010 Products still lives in the site, but you should not apply the old master page to the new site because the new site will not display as expected.
  
To support the new UI in SharePoint 2013, changes were made to the default master pages. For this reason, you cannot apply a master page that was created in SharePoint 2010 Products to a site in SharePoint 2013.
  
To resolve this, you should first create an evaluation site collection, and then create the master page again in the SharePoint 2013 site. After you verify that the new master page works as expected, move the master page to the new site collection and apply it to the site. If the sites are publishing sites, you can use Design Manager to export and then import the master page as part of a design package. Otherwise, you can move the master page as part of a sandboxed solution or by uploading the file to the master page gallery.
  
> [!IMPORTANT]
> SharePoint Foundation 2013 does not support publishing sites. You'll need SharePoint 2013 to use publishing sites. 
  
## Custom master page in a publishing site

If you want a fully branded site such as a corporate communications intranet site, you use a publishing site that has a fully custom master page and custom page layouts that are attached to the custom master page.
  
When you upgrade a SharePoint 2010 Products site to SharePoint 2013, the master page is reset to use the default master page in SharePoint 2013. Therefore, after upgrade, your site will not display its custom branding. The custom master page and page layouts created in SharePoint 2010 Products still live in the site, but you should not apply the old master page to the new site because the new site will not display as expected. 
  
To resolve this issue, you should first create an evaluation site collection that is a publishing site, and then create the master page again in the SharePoint 2013 site. After you verify that the new master page works as expected, complete the following steps: 
  
1. Export the master page as part of a design package.
    
2. Import the design package into the new site collection,
    
3. Apply the new master page to the site.
    
## Custom content placeholders on a custom master page

> [!IMPORTANT]
> If your custom master page contains a custom content placeholder, and if custom page layouts also contain this custom content placeholder, an error may prevent the home page of your site from rendering at all after upgrade. Instead, after upgrade, you may see the error message: "An unexpected error has occurred." 
  
To determine whether you have this issue, you can create an evaluation site collection that is also a publishing site, and then set the master page to the master page that ships with SharePoint 2013. If the site still displays, you don't have this issue. If the site doesn't display and you get an "unexpected error" with a correlation ID, you likely have this issue. 
  
To resolve this issue, do the following:
  
1. Create an evaluation site collection that is a publishing site collection.
    
2. Create a SharePoint 2013 master page.
    
3. Add the custom content placeholder to the 2013 master page.
    
4. Apply the new master page to the site.
    
5. Create a page layout that does not contain the custom content placeholder.
    
    The page layout will be associated with the new master page that was applied to the site.
    
6. Change all the pages that use the old page layout to use the new page layout. 
    
    You can manually edit each page individually in the browser and use the option on the Ribbon, or you can use the client-side object model for SharePoint to update pages programmatically.
    
7. Delete the old page layout that contains the custom content placeholder.
    
We recommend that you do not add custom content placeholders to your custom master page or page layouts.
  
## See also

#### Other Resources

[Troubleshoot site collection upgrade issues in SharePoint 2013](troubleshoot-site-collection-upgrade-issues-in-sharepoint-2013.md)
  
[Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md)
  
[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Run site collection health checks in SharePoint 2013](/SharePoint/sharepoint-server)
  
[Overview of Design Manager in SharePoint 2013](https://go.microsoft.com/fwlink/?LinkId=403875)

