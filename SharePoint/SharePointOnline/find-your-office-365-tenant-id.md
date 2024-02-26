---
ms.date: 02/25/2024
title: "Find your Microsoft 365 tenant ID"
ms.reviewer: 
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
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
  - azure-ad-ref-level-one-done
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn how to find the Microsoft 365 tenant ID using the Microsoft Entra admin center."
---

# Find your Microsoft 365 tenant ID

Your Microsoft 365 tenant ID is a globally unique identifier (GUID) that is different than your organization name or domain. You can use this identifier when you configure OneDrive policies.
  
## Find your Microsoft 365 tenant ID in the Microsoft Entra admin center

Your tenant ID can be found in the **Tenant ID** box on the [Overview page](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView).

![Screenshot that shows the Directory Properties pane in the Entra Admin Center dashboard](media/find-m365-tenant-id-dashboard.png)
  
> [!NOTE]
> For info about finding your tenant ID by using PowerShell instead, first read [Microsoft Graph PowerShell](/powershell/microsoftgraph/installation?view=graph-powershell-1.0&preserve-view=true) and then use [Get-MgOrganization](/powershell/module/microsoft.graph.identity.directorymanagement/get-mgorganization?view=graph-powershell-1.0&preserve-view=true).
