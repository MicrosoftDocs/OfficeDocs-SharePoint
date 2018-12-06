---
title: "Find your Office 365 tenant ID"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 06/29/2018
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- MET150
- BCS160
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Your Office 365 tenant ID is a globally unique identifier (GUID) that is different than your tenant name or domain. On rare occasions, you might need this identifier, such as when configuring Windows group policy for OneDrive for Business."
---

# Find your Office 365 tenant ID

Your Office 365 tenant ID is a globally unique identifier (GUID) that is different than your tenant name or domain. On rare occasions, you might need this identifier, such as when configuring Windows group policy for OneDrive for Business.
  
If you do need to find your Office 365 tenant ID, it's pretty easy. Choose one of the following procedures.
  
## Use the Azure AD portal
  
Office 365 uses Azure AD to manage user accounts.
  
You can find your tenant ID in the Azure AD portal. You'll need to be an Azure AD administrator.
  
 **To find your Office 365 tenant ID in the Azure AD portal**
  
1. Log in to Microsoft Azure as an administrator.
    
2. In the Microsoft Azure portal, click **Azure Active Directory**.
    
3. Under **Manage**, click **Properties**. The tenant ID is shown in the **Directory ID** box. 
    
## Use Windows PowerShell
  
You can use Windows PowerShell to find the tenant ID. You'll need the [Microsoft Azure PowerShell module](https://go.microsoft.com/fwlink/p/?LinkId=717444).
  
Open a Microsoft Azure PowerShell command window and run the following script, entering your Office 365 credentials when prompted.
  
```
Login-AzureRmAccount
```

Your tenant ID is listed in the output.
  

