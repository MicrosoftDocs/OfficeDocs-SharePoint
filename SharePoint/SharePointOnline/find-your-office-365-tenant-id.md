---
ms.date: 07/17/2023
title: "Find your Microsoft 365 tenant ID"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom:
  - Adm_O365
  - onedrive-toc
  - has-azure-ad-ps-ref
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn how to find the Microsoft 365 tenant ID."
---

# Find your Microsoft 365 tenant ID

Your Microsoft 365 tenant ID is a globally unique identifier (GUID) that is different than your organization name or domain. You may need this identifier when you configure OneDrive policies.
  
**To find your Microsoft 365 tenant ID in the Azure AD admin center**

Your tenant ID can be found in the **Tenant ID** box on the [Overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView).

![The Directory Properties pane in the Azure Admin Center dashboard](media/tenant-id-image.png)
  
> [!NOTE]
> For info about finding your tenant ID by using PowerShell instead, first read [Microsoft Graph PowerShell](/powershell/microsoftgraph/installation?view=graph-powershell-1.0&preserve-view=true) and then use [Get-MgOrganization](/powershell/module/microsoft.graph.identity.directorymanagement/get-mgorganization?view=graph-powershell-1.0&preserve-view=true).
