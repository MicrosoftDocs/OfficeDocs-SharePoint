---
title: "Find your Office 365 tenant ID"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn how to find the Office 365 tenant ID for your organization."
---

# Find your Office 365 tenant ID

Your Office 365 tenant ID is a globally unique identifier (GUID) that is different than your organization name or domain. You might need this identifier when you configure Group Policy objects for OneDrive.
  
**To find your Office 365 tenant ID in the Azure AD admin center**
  
1. Sign in to the [Azure Active Directory admin center](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview) as a global or user management admin.
    
2. Under **Manage**, select **Properties**. The tenant ID is shown in the **Directory ID** box. 
    
> [!NOTE]
> For info about finding your tenant ID by using PowerShell instead, first read [Azure Active Directory PowerShell for Graph](/powershell/azure/active-directory/install-adv2?view=azureadps-2.0) and then use [Get-AzureADTenantDetail](/powershell/module/azuread/Get-AzureADTenantDetail).

  

