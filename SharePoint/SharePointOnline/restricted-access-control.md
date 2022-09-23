---
title: "Restricted Access Control"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 09/30/2022
audience: Admin
f1.keywords:
- NOCSH 
ms.topic: conceptual
ms.service: sharepoint-online
ms.localizationpriority: 
ms.collection:  
search.appverid:
ms.assetid: TBD
description: "Enable restricted access control for SharePoint sites through Microsoft 365 Group Membership"
---
# Restricted Site Access for SharePoint sites

Use Restricted Site Access to let only users in a specified Microsoft 365 group to access a SharePoint site. This setting enforces a label policy and provides newly-added flags to reduce the risk of oversharing sites throughout your organization. Even if other users outside of the Microsoft 365 group have received sharing links for the site or its content, they won’t have access to the content unless they are members of the Microsoft 365 group connected to the site.

## Prerequisites

Two important things to keep in mind are:

1. To use this feature, your organization must first have the following subscription:

    - SharePoint Advanced Management

2. Restricted Site Access can only be applied to SharePoint sites connected to Microsoft 365 groups.

The Restricted Access Control policy can be enabled at the tenant-level or a site-level with PowerShell depending on your needs.

## How to enable restricted site access in your organization

SharePoint Administrators or Global Administrators can enable restricted access control feature in your organization by following these steps:

1. Download and install the latest version of SharePoint Online Management Shell.

2. Connect to SharePoint Online as a Global Administrator or SharePoint Administrator in Microsoft 365. To learn how, see Getting started with SharePoint Online Management Shell.

3. To enable restricted access control in SharePoint, run the following command:

    ```PowerShell
    Set-SPOTenant -EnableRestrictedAccessControl $true
    ```

4. After you've enabled restricted access control for SharePoint in your organization, wait for approximately 1 hour before managing restricted access control for a specific Microsoft 365 group connected site.

 Note: If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.
