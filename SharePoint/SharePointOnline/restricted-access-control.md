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

Restricted Site Access lets you allow only users in specified Microsoft 365 group to access a SharePoint site. Even if other users outside of the Microsoft 365 group have received sharing links for the site or its content, they won’t have access to the content unless they are members of the Microsoft 365 group connected to the site

Changing user permissions from a group perspective reduces the risk of oversharing and protects sites containing sensitive information.

Enabling the Restricted Access Control feature enforces a label policy and provides newly-added flags, and grants access to members of the Microsoft 365 group associated with the site.

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
