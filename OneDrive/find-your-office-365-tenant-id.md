---
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

Your tenant ID can be found in the **Tenant ID** box on the [Properties page](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Properties).

![The Directory Properties pane in the Azure Admin Center dashboard](media/tenant-id-image.png)
  
> [!NOTE]
> For info about finding your tenant ID by using PowerShell instead, first read [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2?view=azureadps-2.0&preserve-view=true) and then use [Get-AzureADTenantDetail](/powershell/module/azuread/Get-AzureADTenantDetail).
