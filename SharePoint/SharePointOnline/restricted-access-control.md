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

Two important things to keep in mind are:

1. To use this feature, your organization must first have the following subscription:

- SharePoint Advanced Management

2. Restricted Site Access can only be applied to SharePoint sites connected to Microsoft 365 groups.

The Restricted Access Control policy can be enabled at the tenant-level or a site-level with PowerShell depending on your needs.

## How to enable policy on the tenant using PowerShell

Run the following command:

```PowerShell
    Set-SPOTenant -EnableRestrictedAccessControl $true
```

## How to enable policy at the site level using PowerShell

Run the following command:

```PowerShell
    Set-SPOSite -Identity <> -RestrictedAccessControl $true
```
