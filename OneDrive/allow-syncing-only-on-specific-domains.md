---
title: "Allow syncing only on computers joined to specific domains"
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
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: a3b03efd-ccd0-4d3c-b9ae-7f8f3f9485bc
ms.custom: admindeeplinkSPO
description: "Learn how to restrict syncing to only devices on the domains you specify."
---

# Allow syncing only on computers joined to specific domains

To make sure that users sync OneDrive files only on managed computers, you can configure OneDrive to sync only on PCs that are joined to specific domains.
  
 **To allow syncing only on PCs joined to specific domains**
 
> [!NOTE]
> These settings apply to SharePoint sites as well as OneDrive.
> In a multi-geo environment, this setting can be configured separately for each geo location to apply to users with that preferred data location.

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">Settings in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
 
   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Select **Sync**.

    ![Sync settings in the SharePoint admin center](media/sp-sync-settings.png)
  
3. Select the **Allow syncing only on computers joined to specific domains** check box.

4. Add the [GUID of each domain](/powershell/module/activedirectory/get-addomain) for the member computers that you want to be able to sync.
 
   > [!NOTE]
   > Make sure to add the domain GUID of the computer domain membership. If users are in a separate domain, only the domain GUID that the computer account is joined to is required.

   > [!IMPORTANT]
   > This setting is only applicable to Active Directory domains. It does not apply to Azure AD domains. If you have devices which are only Azure AD joined, consider using a [Conditional Access Policy](/azure/active-directory/conditional-access/overview) instead.
    
7. Select **Save**.
    
For info about setting this sync app restriction by using PowerShell, see [Set-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/set-spotenantsyncclientrestriction).
