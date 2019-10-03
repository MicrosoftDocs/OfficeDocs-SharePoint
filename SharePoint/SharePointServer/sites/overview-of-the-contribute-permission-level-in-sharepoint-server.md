---
title: "Overview of the Contribute permission level in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 3d6fb9be-5773-40a1-9b31-352994ef4740
description: "Learn about the Contribute permission level in SharePoint Server."
---

# Overview of the Contribute permission level in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
## About updating web files
<a name="section1"> </a>

Web files enable you to implement various customization options for a web page. Web files can contain scripts (for example, JavaScript) that can call web services and interoperate with data on a site. Web files are stored as a modifiable list, based on their file name extensions. 
  
A member of the Farm Administrators group can use Microsoft PowerShell cmdlets to configure web files that have the following file name extensions:
  
- .ascx
    
- .aspx
    
- .asmx
    
- .master
    
- .jar
    
- .swf
    
- .xap
    
- .xsf
    
- .xsn
    
The tasks that require the Add and Customize Pages permission in SharePoint Server include the following:
  
- Update the content of a web file
    
- Move a web file
    
- Upload a web file
    
- Rename a web file
    
- Publish, migrate, import and export a web file
    
Users with the default Contribute permission level in SharePoint Server can perform the following tasks:
  
- Check in, check out, or revert a web file
    
- Revert a version from version history for a web file
    
- Delete a web file
    
- Recycle a deleted web file
    
## About editing Web Parts
<a name="section2"> </a>

To add or edit Web Parts that developers have marked as unsafe for editing, SharePoint Server users must have the Add and Customize Pages permission.
  
By default, the following Web Parts are marked as safe for editing and can be added or edited by users who have the default Contribute permission level:
  
- Basic Chart Web Part
    
- Image Web Part
    
- Page Viewer Web Part
    
- Picture Slideshow Web Part
    
- Relevant Documents Web Part
    
- Site Users Web Part
    
- Title Bar Web Part
    
- User Tasks Web Part
    
## See also
<a name="section2"> </a>

#### Concepts

[User permissions and permission levels in SharePoint 2013](user-permissions-and-permission-levels.md)

