---
title: "Overview of themes in SharePoint Server"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 9/8/2017
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SharePoint_Online
ms.assetid: 7924fe8b-986c-44eb-8dd3-5724acecd529
description: "Summary: Learn about the themes in SharePoint Server 2016 and SharePoint 2013 and how to use them to customize the look and feel of sites."
---

# Overview of themes in SharePoint Server

 **Summary:** Learn about the themes in SharePoint Server 2016 and SharePoint 2013 and how to use them to customize the look and feel of sites. 
  
Themes give you a quick and easy way to change the look and feel of any site in SharePoint Server. They are pre-designed collections of web page elements, such as fonts, color schemes, layout, and background pictures that come with SharePoint Server. In SharePoint Server, you can apply a theme to a site, and then preview it before committing the change. You can change the theme of a site any number of times. For more information about themes, see [Themes overview for SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=306431). Note that this article still applies to SharePoint Server,
  
Using themes is one way to change the look and feel of a site. Themes are part of the larger, updated branding and design capabilities in SharePoint Server 2016.
  
This article includes an overview of themes and how they work. This article does not describe how to create custom themes, called composed looks, or how to upload and manage themes in a theme gallery. It also does not discuss how to plan for the overall branding of sites by using master pages or cascading style sheets.
  
## About themes
<a name="section1"> </a>

Themes enable lightweight branding of a SharePoint Server site by allowing a site owner or a user who has designer rights to make changes to the color palette, site layout, font scheme, and background of a site. Themes are applied and customized directly in the user interface, and do not require knowledge of cascading style sheets or master pages.
  
By default, a theme is only applied to the site for which it is selected. It is not inherited by any subsites unless you are working with a publishing site., Or, if the publishing feature was enabled for a site, you can choose to either inherit the theme from the parent site or specify a theme that will be used by the site. When working publishing sites and you want more control over your customizations than themes can provide, use Design Manager.
  
> [!NOTE]
> Themes were redesigned in SharePoint 2013 to simplify the process of customizing sites by changing the site layout, color palette, font scheme, and background image. The themes user interface has been redesigned and there is a set of new file formats related to themes. The themes remain the same in SharePoint Server 2016. Themes created in SharePoint 2010 Products cannot be used on SharePoint Server 2016 and SharePoint 2013 sites. However, they can still be used on site collections that have not been upgraded and are running in 2010 mode. 
  
### Components of the themes experience

The following section provides an overview of the terminology and user interface components that comprise the themes experience in SharePoint Server.
  
The following list describes the themes terminology used in this article:
  
- **Design** A design, or composed look, is the color palette, font scheme, background image, and master page that determine the look and feel of a site. When used to discuss the overall look of a site, design and theme can be used interchangeably. 
    
- **Image** The background image used for the site. You can change this in any of the pre-configured themes. 
    
- **Color palette** A color palette, or color scheme, is the combination of colors that are used in a site. You can select from a number of predefined color combinations. 
    
- **Site layout** A master page defines how all the elements are structured on the page. There are two site layouts available for each of the pre-configured themes. 
    
- **Font scheme** Defines the fonts used in a site. You can select from a list of available fonts. 
    
### Theme gallery

You can access thumbnails of themes and apply them to a site through the **Change the look** gallery available in site settings. 
  
The theme gallery can be accessed in the following ways:
  
- Click **Settings**, and then click **Change the look**, or
    
- On the **Site Settings** page, under **Web Designer Galleries**, click **Themes**, or
    
- On the home page, click the **What's your style?** tile. 
    
### Master page gallery

The master page gallery lists the master page files, and their corresponding preview files (.preview), that are used by the themes user interface. The preview files are used to render the thumbnail images in the design gallery. If a master page does not have a corresponding preview file, it cannot be used in the design gallery.
  
To access the master page gallery, on the **Site Settings** page, under **Web Designer Galleries**, click **Master pages**.
  
### Composed looks list

The composed looks list shows the designs that are available to the design gallery. A design includes the design name, master page URL, color palette URL, image URL (optional), font scheme URL (optional), and display order number. 
  
To access the composed looks list, on the **Site Settings** page, under **Web Designer Galleries**, click **Composed looks**. 
  
## Ways to use themes
<a name="section2"> </a>

There are three ways to use themes on a site:
  
- Use a preinstalled theme.
    
- Modify a preinstalled theme.
    
- Upload a custom theme (composed look) to the gallery.
    
### Use a preinstalled theme
<a name="Section2a"> </a>

SharePoint Server comes with preinstalled themes, including the default SharePoint theme. When a new site is created, it will use the default SharePoint theme. 
  
### Modify a preinstalled theme
<a name="Section2b"> </a>

When a preinstalled theme is modified, a new theme called Current is created automatically after the theme changes have been applied. There can only be one Current theme for a site. SharePoint Server does not provide a way to save themes within the user interface. If you modify a preinstalled theme, apply the changes (thereby creating a new theme called Current), and then modify a second preinstalled theme. The second preinstalled theme becomes the Current theme when the settings are applied.
  
To save a modified theme, create a new list item in the composed looks list that contains the same master page, color palette, font scheme, and background image URLs of the modified theme (the modified theme is called Current in the composed looks list).
  
### Upload your own Composed Looks files to the theme gallery
<a name="Section2c"> </a>

You can create custom themes by creating additional color palettes and font schemes and uploading them to the theme gallery. The new color palettes and font schemes are then available to you when you choose to modify a design in the design gallery. Similarly, if you want to have additional site layouts to choose from, you can upload additional master pages, and corresponding preview files, to the master page gallery.
  
You can create new designs by creating new list items in the composed looks list. Create a new list item and specify the master page, color palette, font scheme, and background image for the new design.
  
## See also
<a name="section2"> </a>

#### Other Resources

[Use composed looks to brand SharePoint sites](https://go.microsoft.com/fwlink/?linkid=845556)
  
[Branding SharePoint sites in the SharePoint add-in model](https://go.microsoft.com/fwlink/?linkid=845555)

