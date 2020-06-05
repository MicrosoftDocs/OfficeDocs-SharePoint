---
title: "Microsoft Fluid Framework – Admin Access Management"
ms.reviewer: kaarins
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160
ms.assetid: 
description: "Learn about managing admin access to the Fluid Network."
---

# Microsoft Fluid Framework – Admin Access Management

This article describes how admins of Microsoft 365 tenants can manage access to Microsoft Fluid framework preview by disabling Fluid Experiences across their tenant through SharePoint.

>[!NOTE]
>Name: Microsoft Fluid Framework Preview ID: Microsoft 365 Roadmap ID 56781

## Before you begin

Microsoft Fluid Framework preview releases across all targeted release tenants with default ON state. To enable or disable all Fluid Experiences across your Microsoft 365 tenant, you will need the SharePoint PowerShell https://docs.microsoft.com/office365/enterprise/powershell/manage-sharepoint-online-with-office-365-powershell module.

### Disabling Fluid Framework through SharePoint PowerShell cmdlet

1. Connect to SharePoint Online PowerShell by reviewing [Get started with SharePoint Online Management Shell](https://docs.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps).

2. Disable Fluid using the Set-SPOTenant cmdlet:
    - Set-SPOTenant -IsFluidEnabled $false

The change should take approximately 60 minutes to apply across your tenancy.

If you need to re-enable this capability, that can also be done through SharePoint PowerShell cmdlets.

### Enabling Fluid Framework through SharePoint Online PowerShell cmdlet

1. Connect to SharePoint PowerShell by reviewing [Get started with SharePoint Online Management Shell](https://docs.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps).

2. Enable Fluid using the Set-SPOTenant cmdlet:
    - Set-SPOTenant -IsFluidEnabled $true

The change should take approximately 60 minutes to apply across your tenancy.