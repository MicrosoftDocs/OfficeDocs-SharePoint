---
title: "Overview of themes in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SharePoint_Online
ms.assetid: 7924fe8b-986c-44eb-8dd3-5724acecd529
description: "Learn about the themes in SharePoint Server and how to use them to customize the look and feel of sites."
---

# Overview of themes in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Themes give you a quick and easy way to change the look and feel of any site in SharePoint Server. They are pre-designed collections of web page elements, such as fonts, color schemes, layout, and background pictures that come with SharePoint Server. In SharePoint Server, you can apply a theme to a site, and then preview it before committing the change. You can change the theme of a site any number of times. For more information about themes, see [Themes overview for SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=306431). Note that this article still applies to SharePoint Server.
  
Using themes is one way to change the look and feel of a site. Themes are part of the larger, updated branding and design capabilities in SharePoint Servers 2016 and 2019. 

The SharePoint Server 2019 modern experience includes new Team and Communication sites. These modern sites contain visually compelling web parts that you can customize. For more information, see [What is a SharePoint team site?](https://support.office.com/en-us/article/What-is-a-SharePoint-team-site-75545757-36c3-46a7-beed-0aaa74f0401e) and [What is a SharePoint communication site?](https://support.office.com/en-us/article/What-is-a-SharePoint-communication-site-94A33429-E580-45C3-A090-5512A8070732)
  
This article includes an overview of themes and how they work. This article does not describe how to create custom themes, called composed looks, or how to upload and manage themes in a theme gallery. It also doesn't discuss how to plan for the overall branding of sites by using master pages or cascading style sheets.
  
## About themes
<a name="section1"> </a>

Themes enable lightweight branding of a SharePoint Server site by allowing a site owner or a user who has designer rights to make changes to the color palette, site layout, font scheme, and background of a site. Themes are applied and customized directly in the user interface, and do not require knowledge of cascading style sheets or master pages.
  
By default, a theme is only applied to the site for which it is selected. It is not inherited by any subsites unless you are working with a publishing site., Or, if the publishing feature was enabled for a site, you can choose to either inherit the theme from the parent site or specify a theme that will be used by the site. When working publishing sites and you want more control over your customizations than themes can provide, use Design Manager.
  
> [!NOTE]
> Themes were redesigned in SharePoint 2013 to simplify the process of customizing sites by changing the site layout, color palette, font scheme, and background image. The themes user interface has been redesigned and there is a set of new file formats related to themes. The themes remain the same in SharePoint Server 2016. Themes created in SharePoint 2010 Products cannot be used on SharePoint Server sites. However, they can still be used on site collections that have not been upgraded and are running in 2010 mode. 
  
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
    
- On the home page, click the **What's your style?** tile. This link isn't available in SharePoint Server 2019 modern team or communication sites.
    
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

You can create custom themes by creating additional color palettes and font schemes and uploading them to the theme gallery. The new color palettes and font schemes are then available to you when you choose to modify a design in the design gallery. Similarly, if you want to have additional site layouts to choose from, you can upload additional master pages, and corresponding preview files, to the master page gallery. For more information, see [SharePoint site theming](/sharepoint/dev/declarative-customization/site-theming/sharepoint-site-theming-overview).
  
You can create new designs by creating new list items in the composed looks list. Create a new list item and specify the master page, color palette, font scheme, and background image for the new design.
  
## See also
<a name="section2"> </a>

#### Other Resources

[Use composed looks to brand SharePoint sites](https://go.microsoft.com/fwlink/?linkid=845556)
  
[Branding SharePoint sites in the SharePoint add-in model](https://go.microsoft.com/fwlink/?linkid=845555)

[Change the look of your SharePoint site](https://support.office.com/en-us/article/Change-the-look-of-your-SharePoint-site-06bbadc3-6b04-4a60-9d14-894f6a170818)
