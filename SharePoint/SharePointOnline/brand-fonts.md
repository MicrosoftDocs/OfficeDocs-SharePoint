---
ms.date: 04/18/2024
title: Brand fonts  
ms.reviewer:
ms.author: ruihu
author: maggierui
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- MET150
ms.collection:
- M365-collaboration
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "Learn what Brand fonts are, how to add brand fonts to the brand center, how to locate custom fonts on the web, how to install and manage custom fonts, supported font file types and font licensing."
---
# Brand Fonts

The choice of font can have a significant impact on the look and feel of your content. A font can convey your brand personality, tone, and style, as well as enhance the readability and aesthetics of your text. Whether you want to create a professional, elegant, playful, or creative impression, using a font that matches your brand identity can help you stand out from the crowd and connect with your audience.

<img src="c:\GitHub\OfficeDocs-SharePoint-pr\SharePoint\SharePointOnline/media/image1.png" style="width:4.55151in;height:2.28096in" alt="A screenshot of a brand Description automatically generated" />

Brand fonts are your organization’s fonts that are uploaded and managed within the SharePoint brand center. In this article we’ll talk about how to manage your brand fonts so you can use them in Microsoft 365.

NOTE: \<font licensing note to link to the font licensing page\>

There are different types of font format types and font file types. The way a font is used, digital or printed, can change the font file type needed.

### Web-safe fonts

Web-safe fonts are a set of fonts that are widely used and available on most devices by default. They are designed to be compatible with different browsers and operating systems, and to reduce the risk of font substitution or distortion.

## Adding brand fonts to the brand center

SharePoint and Viva Connections include a set of font options that are available for use within Microsoft web products.

However, sometimes you may want to use a custom font that you’ve created, purchased or downloaded from somewhere else. These custom fonts might be more accurate to how you would like to represent your brand within Microsoft 365 applications like SharePoint and Viva Connections.

### Locate custom fonts on the Web

You can also get and use fonts that are installed with other applications, or download fonts from the Internet. Some fonts on the Internet are sold commercially, some are shareware, and some are free. The [Microsoft Typography site](https://www.microsoft.com/en-us/Typography/default.aspx) site provides links to other font foundries (the people or businesses outside of Microsoft who make and offer fonts) where you can find more fonts.

## Install a custom brand font

After choosing your custom brand font, you will need to upload it into the SharePoint brand center so that it can be part of your font packages. You will go to the Brand Fonts library from the Brand center app.

1.  Download or locate your custom brand font files. These often come in .zip folders.

2.  If the font files are zipped, unzip them by right-clicking the .zip folder and then clicking **Extract**.

3.  Navigate to the Brand fonts library in the SharePoint brand center app. Using the upload button

After the brand font files are uploaded our system will extract the needed metadata from the font files for use in the Brand center.

NOTE: There is a slight delay in the time from upload until this metadata is populated into the library and the font is available for use.

### Supported font file types: 

| Font file type       | File extension |
|----------------------|----------------|
| True Type fonts      | .ttf           |
| Open Type fonts      | .otf           |
| Web Open Format Font | .woff          |
| Web Open Format Font | .woff2         |

The Web Open Format file is a web-only font format that compresses the fonts to make them load faster on websites. This format cannot be used for other purposes, such as installing the fonts on your computer. WOFF 2.0 is the ideal format for web fonts being used on SharePoint and Viva Connections. These fonts work well on the web but not in graphics software.

Font file Size Limit: 10MB

## Manage your custom brand fonts

To manage your custom brand fonts, you will need to navigate to the Brand Fonts library in the Brand center app.

1.  Select your custom font file from the library.

2.  Edit the Visible property on your font file to control the availability of the font for experiences.  
    \<Screenshot plus note\>

> NOTE: Deletion of custom brand fonts is not allowed from the Brand center app at this time.

SEPARATE ARTICLE

# Font Licensing for the brand center

Fonts are a kind of software. Like many other kinds of software, you get a license to use font files instead of buying them. Different vendors have different licenses for their fonts, but generally most licenses, including the ones for the fonts Microsoft provides with applications and Windows, do not let you put the fonts in applications or share them with others.

Any font used in Microsoft 365 applications requires a font license that covers the conditions of font usage for the intended product. This could include a webfont license, application license, desktop license, server license, or several other license types.

** Warning**

By using this feature and publishing font files, a font catalog will be created. The newly created font catalog files will be publicly stored, along with the fonts, in the cloud and will not respect the site classification guidelines if the Organization Asset Library is hosted in Restricted SharePoint Site. The font catalog files will contain font names and other font related metadata. Be aware that the files will be accessible to anyone, even people outside of your organization, who can get the URLs that link to them.

Do not use this feature if your fonts contain proprietary information, or if they have license usage restrictions, such as restrictions on cloud hosting, or your organization isn't comfortable making the fonts publicly available.

### Microsoft provided fonts

Microsoft provides a set of fonts for usage in Microsoft 365 applications. A Microsoft 365 application can use the fonts to render content to a screen, allow that content to be edited, and allow that content to be output to a device, like a printer.   
  
Some of the fonts supplied with the Brand center were created specifically for Microsoft by leading type designers and type design companies (known as font foundries). Other fonts were licensed to Microsoft from font foundries for inclusion with Microsoft 365 applications.  
  
Reference: [Cloud fonts in Office - Microsoft Support](https://support.microsoft.com/en-us/office/cloud-fonts-in-office-f7b009fe-037f-45ed-a556-b5fe6ede6adb?ui=en-us&rs=en-us&ad=us)

NOTE:  
Microsoft provided fonts are available to Microsoft 365 subscribers

### Custom brand fonts

For fonts obtained elsewhere or supplied with other apps, you will need to review the license agreements that accompany those applications.

**Why must I dig up and read those agreements?**

We're sorry, but Microsoft can’t provide guidance to fonts that we didn’t supply.

The rights we provide you for Windows supplied fonts are considered quite broad, and it’s possible that other font licenses, even some free ones, may be more restrictive.

Some font foundries may give away “free” versions of fonts with limited licenses and make their money selling extended rights.

Some font licenses may restrict commercial use, require attribution, and restrict redistribution or commercial redistribution of documents that include embedded versions of the font.
