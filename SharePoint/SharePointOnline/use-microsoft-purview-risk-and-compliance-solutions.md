---
title: "Use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint and OneDrive"
f1.keywords:
- NOCSH
ms.author: kyrachurney
author: kyracatwork
manager: roygles
ms.date: 5/16/2014
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
description: Learn how to use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint and OneDrive.
---

# Use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint and OneDrive


> [!IMPORTANT]
> Read the [overview](#overview) to get a summary of the plan. See the [migration strategies](migration-strategies.md) page for more details and links to important articles and pages. 
>
>Review the older information management and records management features in SharePoint and OneDrive for business [retirement timeline](#retirement-timeline) for dates that have been announced and for updates on new retirement announcements.

## Overview

If you need to proactively retain or delete content in Microsoft 365 for data lifecycle management or records management, we recommend using Microsoft 365 Purview Data Lifecycle Management and Microsoft Purview Records Management features instead of older features in SharePoint and OneDrive for Business. 

We're planning a long-term retirement plan for these older features and will share updates including dates in the [retirement timeline](#retirement-timeline). Feature retirements will be communicated in advance to give customers time to prepare and perform any applicable migration activities. 

The following features are under consideration for retirement: 

- Record Center 
    - [Create a record center site ](https://support.microsoft.com/en-us/office/create-a-records-center-6bf1488b-62a8-486c-90dd-54b6bcce4b3a#:~:text=You%20need%20to%20take%20the%20following%20steps%20to,on%20the%20Records%20Center%20site.%20...%20See%20More.)
    - [Submit records to the record center](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) 
    - [Content Organizer](https://support.microsoft.com/en-us/office/configure-the-content-organizer-to-route-documents-b0875658-69bc-4f48-addb-e3c5f01f2d9a#:~:text=Each%20time%20that%20a%20document,in%20a%20different%20site%20collection.) 
    - [Vault abilities](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c)
- [Information Management Policies](intro-to-info-mgmt-policies.md) 
- [In-Place Records Management](https://support.microsoft.com/en-us/office/configuring-in-place-records-management-7707a878-780c-4be6-9cb0-9718ecde050a?ui=en-us&rs=en-us&ad=us) 
- [Document deletion policies (deletion only) ](https://support.microsoft.com/en-us/office/create-a-document-deletion-policy-in-sharepoint-server-2016-4fe26e19-4849-4eb9-a044-840ab47458ff?ui=en-us&rs=en-us&ad=us)
- [Use policies for site closure and deletion (deletion only)](https://support.microsoft.com/en-us/office/use-policies-for-site-closure-and-deletion-a8280d82-27fd-48c5-9adf-8a5431208ba5)

## Retirement summary

The following key points summarize how migration and retirement work: 

- Microsoft won't automatically force a migration of your older information management and records management features in SharePoint and OneDrive for Business. If you choose not to migrate to supported features, the older features may no longer function when the feature is retired and will no longer be supported.  
- Between now and the retirement date of the feature, you have the flexibility to migrate your data lifecycle and record management scenarios on your own schedule. 
- If you have configured SharePoint sites for content type policies or information management policies to retain content for a list or library, those policies are ignored while a retention policy or retention label policy is in effect. 
- Retirement activities for features may include some or all of the following: 
    - Feature may no longer supported by Microsoft support. 
    - It may not function as expected or may not function at all. 
    - In the solution UI, it may no longer be visible. 
    - Configurations may not be available from the solution UI or programmatically, including enable and disable actions. 
    - Back-end services supporting behaviors for feature may no longer function, resulting in the cessation of feature behavior within the tenant, even if the older feature behavior was still enabled. 
    
## Retirement timeline 
> [!NOTE]
> Any future dates and timelines are approximate and may change as we develop our plans further. see [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=) for the most current information.

### Worldwide (standard multitenant) 

#### Upcoming 

N – Announcement of first set of features in the retirement plan and timelines 

### Special (GCC, GCC-H, DoD) 

#### Upcoming 

N  – Announcement of first set of features in the retirement plan and timelines

## Migrating from older features to modern features

The modern purview features can be used in several different ways to meet your data lifecycle and record management needs. The approach or combination of approaches that work best for you and your organization will depend on your organization’s governance strategy and applicable requirements. 

To identify what works best for your scenarios and understand options for migrating your organization's older features to modern Purview solutions, see [migration strategies](migration-strategies.md). 

