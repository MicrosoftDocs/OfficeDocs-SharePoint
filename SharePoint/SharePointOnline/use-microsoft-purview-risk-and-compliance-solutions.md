---
title: "Use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint for Microsoft 365"
f1.keywords:
- NOCSH
ms.author: kyrachurney
author: kyracatwork
manager: roygles
ms.date: 10/25/2023
audience: Admin
ms.topic: overview
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- WSU150
- SPO160
- OSU150
- MET150
ms.assetid: 63a0b501-ba59-44b7-a35c-999f3be057b2
ms.collection:
- purview-compliance
- Tier3
ms.custom:
- seo-marvel-apr2020
description: Learn how to use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint for Microsoft 365.
---

# Use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint for Microsoft 365


> [!IMPORTANT]
> Read the [overview](#overview) to get a summary of the plan to deprecate the applicable older features from SharePoint for Microsoft 365 records management. For more information and links to important articles and pages, see [migration strategies](migration-strategies.md).
>
>Review the older information management and records management features in SharePoint for Microsoft 365 [deprecation timeline](#deprecation-timeline) for dates that have been announced and for updates on new deprecation announcements.

## Overview

If you need to retain or delete content in Microsoft 365, we recommend using Microsoft Purview Data Lifecycle Management and Microsoft Purview Records Management features instead of older information management and records management features in SharePoint for Microsoft 365

We have a long-term deprecation plan for these older features. More information, including dates, is in the [deprecation timeline.](#deprecation-timeline) Feature deprecations are communicated in advance to give customers time to prepare and perform any applicable migration activities. 

The following older information management and records management features in SharePoint for Microsoft 365 are under consideration for deprecation: 

- Record Center 
    - [Create a record center site ](https://support.microsoft.com/en-us/office/create-a-records-center-6bf1488b-62a8-486c-90dd-54b6bcce4b3a#:~:text=You%20need%20to%20take%20the%20following%20steps%20to,on%20the%20Records%20Center%20site.%20...%20See%20More.)
    - [Submit records to the record center](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) (commonly referred to as “send to” location) 
    - [Content Organizer](https://support.microsoft.com/en-us/office/configure-the-content-organizer-to-route-documents-b0875658-69bc-4f48-addb-e3c5f01f2d9a#:~:text=Each%20time%20that%20a%20document,in%20a%20different%20site%20collection.) 
   
- [Information management policies](intro-to-info-mgmt-policies.md) 
- [In-place records management,](https://support.microsoft.com/en-us/office/configuring-in-place-records-management-7707a878-780c-4be6-9cb0-9718ecde050a?ui=en-us&rs=en-us&ad=us) including [vault abilities.](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c)
- [Document deletion policies (deletion only) ](https://support.microsoft.com/en-us/office/create-a-document-deletion-policy-in-sharepoint-server-2016-4fe26e19-4849-4eb9-a044-840ab47458ff?ui=en-us&rs=en-us&ad=us)
- [Policies for site closure and deletion (deletion only)](https://support.microsoft.com/en-us/office/use-policies-for-site-closure-and-deletion-a8280d82-27fd-48c5-9adf-8a5431208ba5)

## Deprecation summary

The following key points summarize how deprecation works:  

- Microsoft won't automatically migrate your older information management and records management features in SharePoint for Microsoft 365. If you choose not to migrate to supported features, the older features might no longer be supported.   
- Between now and the deprecation date of the feature, you have the flexibility to migrate your scenarios on your own schedule.  
- If you have configured SharePoint sites for content type policies or information management policies, those policies continue to be ignored while a retention policy or retention label policy is in effect. 
- Deprecation for features might include some or all the following outcomes:  
    - Microsoft might not support the feature.
    - It might no longer be visible in the user interface.  
    - Configurations might not be available through the user interface or programmatically, including enable and disable actions.  
    - When fully deprecated, backend services supporting behaviors for the feature might no longer function as expected.
    
## Deprecation timeline 
 
> [!NOTE]
> Any future dates and timelines are approximate and might change as we develop our plans further.

### Worldwide service

#### Upcoming 

November 2023 – Announcement of the first set of features in the deprecation plan and timelines. 

January 2025 - The following features will no longer be supported by Microsoft and configurations will no longer be available:
• Record Center site template, used to create a new Record Center site.
• Configure systems to submit files to a site using the Record Center programmable interface (commonly referred to as “send to” location). ​
• Content Organizer. 

### Government clouds (GCC, GCC-H, DoD) 

#### Upcoming 

November 2023 – Announcement of the first set of features in the deprecation plan and timelines.

January 2025 - The following features will no longer be supported by Microsoft and configurations will no longer be available:
• Record Center site template, used to create a new Record Center site.​
• Configure systems to submit files to a site using the Record Center programmable interface (commonly referred to as “send to” location). ​
• Content Organizer. 

## Migrating from older features to modern features

Modern Microsoft Purview features have flexible configuration options to help meet your data lifecycle and records management needs. The specific configuration that works best for your organization depends on your organization’s governance strategy and applicable requirements.  

To identify what works best for your scenarios and understand options for migrating your organization's older features to modern Purview solutions, see [migration strategies](migration-strategies.md). 

