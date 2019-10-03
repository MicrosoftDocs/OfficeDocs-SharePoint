---
title: "Alternate access URLs have not been configured (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/22/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 7f65b235-8e0d-48d8-acca-e2e0295e6522
description: "Learn how to resolve the SharePoint Health Analyzer rule: Alternate access URLs have not been configured, for SharePoint Server."
---

# Alternate access URLs have not been configured (SharePoint Server)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
>[!IMPORTANT]
>This health analyzer rule only applies to SharePoint 2010 as this was removed in [KB4011601](https://support.microsoft.com/help/4011601) for SharePoint Server 2013 and [KB4011576](https://support.microsoft.com/help/4011576) for SharePoint Server 2016.

 **Rule Name:** Alternate access URLs have not been configured. 
  
 **Summary:** A default zone URL must not point to the computer name of a front-end Web server. Because this installation has more than one front-end Web server, an incorrectly configured default zone URL can result in a variety of errors, including incorrect links and failed operations. 
  
 **Cause:** A default zone URL is pointing to the computer name of a front-end Web server. 
  
 **Resolution: Change the default zone URL to a URL that differs from the computer name of any front-end Web server.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the the SharePoint Central Administration website home page, in the **System Settings** section, click **Configure alternate access mappings**.
    
3. On the Alternate Access Mappings page, on the **Alternate Access Mapping Collection** menu, click **Change Alternate Access Mapping Collection**.
    
4. In the **Select An Alternate Access Mapping Collection** dialog box, click the alternate access mapping collection for which you want to change the default zone URL. 
    
5. On the Alternate Access Mappings page, click **Edit Public URLs**.
    
6. On the Edit Public Zone URLs page, in the **Default** text box, type a new default zone URL that differs from the computer name of any front-end Web server, and then click **Save**.
    

