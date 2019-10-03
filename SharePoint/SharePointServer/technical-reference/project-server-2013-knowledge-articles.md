---
title: "Project Server 2013 knowledge articles for Systems Center Operations Manager"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/20/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: adcaa180-eafe-4636-9547-6edadabd4fed
description: "Learn how to resolve alerts about Microsoft Project Server 2013 in the SharePoint Server 2013 management pack for Systems Center Operations Manager (SCOM)."
---

# Project Server 2013 knowledge articles for Systems Center Operations Manager

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
> [!NOTE]
> The Project Server 2013 knowledge articles for Systems Center Operations Manager only appear in the SharePoint Server 2013 and SharePoint Foundation 2013 Monitoring Pack for System Center Operations Manager 2012. 
  
The articles in this section are knowledge articles for Project Server 2013 that appear in the SharePoint Server 2013 management pack (MP). Typically, you would see these articles after clicking a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in Project Server 2013.
  
New SCOM alerts in Project Server 2013:
  
- [Project WFE to application server connection failed (SharePoint 2013 monitoring rule)](#ProjectApp)
    
- [Project WFE to application server connection failed](#ProjectApp2)
    
## Project WFE to application server connection failed (SharePoint 2013 monitoring rule)
<a name="ProjectApp"> </a>

 **Alert Name:**Project WFE to application server connection failed
  
 **Summary:** This alert occurs when a Project Server front-end server cannot connect to a back-end server. Requests are no longer transferred from the front-end to the back-end. 
  
### Cause

Potential root causes include: 
  
- Hardware issues
    
- Networking issues
    
- Permissions issues
    
### Resolution

Check standard connectivity on the faulty computers:
  
1. Ensure there are no hardware failures on any computer that reported the error.
    
2. Perform basic network connectivity checks between the front-end and back-end computers.
    
3. Check Project service accounts credentials and permissions.
    
## Project WFE to application server connection failed
<a name="ProjectApp2"> </a>

 **Alert Name:**Project WFE to application server connection failed
  
 **Summary:** This alert occurs when a Project Server front-end server cannot connect to a back-end server. Requests are no longer transferred from the front-end to the back-end. 
  
### Cause

Potential root causes include: 
  
- Hardware issues
    
- Networking issues
    
- Permissions issues
    
### Resolution

Check standard connectivity on the faulty computers:
  
1. Ensure there are no hardware failures on any computer that reported the error.
    
2. Perform basic network connectivity checks between the front-end and back-end computers.
    
3. Check Project service accounts credentials and permissions.
    
## See also
<a name="ProjectApp2"> </a>

#### Concepts

[System Center Operations Manager knowledge articles for SharePoint Server](system-center-operations-manager-knowledge-articles.md)

