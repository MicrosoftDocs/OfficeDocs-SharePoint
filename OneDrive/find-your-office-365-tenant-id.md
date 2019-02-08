---
title: "Find your Office 365 tenant ID"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- MET150
- BCS160
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn how to find the Office 365 tenant ID for your organization."
---

# Find your Office 365 tenant ID

Your Office 365 tenant ID is a globally unique identifier (GUID) that is different than your tenant name or domain. On rare occasions, you might need this identifier, such as when configuring Group Policy objects for OneDrive.
  
If you do need to find your Office 365 tenant ID, it's pretty easy. Choose one of the following procedures.
  
## Use the Azure AD admin center
  
Office 365 uses Azure AD to manage user accounts.
  
You can find your tenant ID in the Azure AD admin center. You'll need to be an Azure AD administrator.
  
 **To find your Office 365 tenant ID in the Azure AD admin center**
  
1. Sign in to the [Azure Active Directory admin center](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview) as a global or user management admin.
    
2. Under **Manage**, select **Properties**. The tenant ID is shown in the **Directory ID** box. 
    
## Use PowerShell
  
You can use Microsoft PowerShell to find the tenant ID. You'll need the [Microsoft Azure PowerShell Az module](/powershell/azure/overview).
  
Run the below cmdlet, signing in with the code provided by the cmdlet.
  
```PowerShell
Connect-AzAccount
```

Your tenant ID is listed in the output.
  

