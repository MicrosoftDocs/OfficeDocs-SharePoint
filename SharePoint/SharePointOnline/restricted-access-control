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
# Restrict access to SharePoint sites based on Microsoft 365 Group Membership

Protect SharePoint site content with Restricted Access Control (RAC).

Restricted Access Control is a new feature from the SharePoint Advanced Management (SAM) add-on that provides premium features to assist IT administrator
 with overseeing site management policies, data access governance, and collaboration insights.

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
