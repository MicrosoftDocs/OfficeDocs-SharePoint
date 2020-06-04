---
title: "Plan hybrid OneDrive"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: seo-marvel-apr2020
ms.assetid: 080d0fb6-3182-4233-abe7-e0f60799c0e5
description: "In SharePoint Server, you can redirect users to OneDrive in Microsoft 365 when they select OneDrive in the nav bar (SharePoint Server 2010 and SharePoint Server 2013) or in the app launcher (SharePoint Server 2016). This is known as hybrid OneDrive."
---

# Plan hybrid OneDrive

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

In SharePoint Server, you can redirect users to Microsoft OneDrive when they select **OneDrive** in the nav bar (SharePoint Server 2010 and SharePoint Server 2013) or in the app launcher (SharePoint Server 2016). This is known as hybrid OneDrive.
  
With this feature, you can continue to use your on-premises SharePoint farm while providing your users with an easy way to store, share, and collaborate in the cloud with OneDrive. This best-of-both-worlds approach lets you keep your key business information in your own environment while allowing users the flexibility to access their documents from anywhere.
  
## How it works

With hybrid OneDrive your users can:
  
- Store personal files they are working on in the cloud, and access these files even when they aren't signed in to your corporate network.
    
- Access these files on devices such as iPhones, Windows Phones, tablets, and so on.
    
- Share and collaborate on documents with others in your organization or with external users by using guest links.
    
As an IT pro, you can:
  
- Provide cloud storage for your users.
    
- Add storage for your users in the cloud in 25-100 gigabytes (GB) increments, as needed.
    
- Continue to provide SharePoint features as usual in your on-premises farm.
    
 **Things to keep in mind**
  
To avoid user confusion, keep the following in mind when you turn on hybrid OneDrive:
  
- When you turn on this feature, your users will be directed to OneDrive when they select OneDrive in SharePoint Server. Be sure to plan to migrate your users' content from their old SharePoint Server OneDrive to the new one in Office 365.
    
- Because there's no direct link between OneDrive in SharePoint Server and OneDrive, users' **Shared with me** lists in Office 365 won't display documents that have been shared with them from on-premises SharePoint Server.

- In SharePoint Server 2016 and SharePoint Server 2019, the custom company logo set in the Microsoft 365 Admin center appears in the SuiteNav menu bar. For more info about how to set the company logo, see [Customize the Microsoft 365 theme for your organization](https://docs.microsoft.com/office365/admin/setup/customize-your-organization-theme).
    
## Getting started

In SharePoint Server 2013 and SharePoint Server 2016, hybrid OneDrive is available as part of several hybrid option bundles. For details, see [Hybrid sites features and OneDrive](sharepoint-hybrid-sites-and-search.md#SitesFeatures).
  
Hybrid OneDrive is also available with SharePoint Server 2010. For details, see [Configure hybrid OneDrive in SharePoint Server 2010](https://go.microsoft.com/fwlink/?LinkId=691695) . 
  

