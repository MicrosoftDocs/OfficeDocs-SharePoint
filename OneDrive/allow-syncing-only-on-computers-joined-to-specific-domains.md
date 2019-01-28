---
title: "Allow syncing only on computers joined to specific domains"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: a3b03efd-ccd0-4d3c-b9ae-7f8f3f9485bc
description: "Learn how to restrict syncing to only devices on the domains you specify in the OneDrive admin center. "
---

# Allow syncing only on computers joined to specific domains

To make sure that users sync OneDrive files only on managed computers, you can configure OneDrive to sync only on PCs that are joined to specific domains.
  
 **To allow syncing only on PCs joined to specific domains**
  
1. Open the [OneDrive admin center](https://admin.onedrive.com/?v=SyncSettings) and click **Sync** in the left pane. 
    
    ![The Sync tab of the OneDrive admin center](media/1c3bf6d6-7b82-4c73-9df7-c8551a0c2922.png)
  
2. Select the **Allow syncing only on PCs joined to specific domains** check box. 
    
3. Click **Add domains**.
    
4. Add the [GUID of each domain](/powershell/module/activedirectory/get-addomain) for the member computers that you want to be able to sync.
 
> [!NOTE]
> Make sure to add the domain GUID of the computer domain membership. If users are in a separate domain, only the domain GUID that the computer account is joined to is required.

> [!IMPORTANT]
> This setting is only applicable to Active Directory domains. It does not apply to Azure AD domains. If you have devices which are only Azure AD joined, consider using a [Conditional Access Policy](/azure/active-directory/conditional-access/overview) instead.
   
5. If you want to prevent Mac OS users from syncing entirely, select the **Block sync on Mac OS** check box. 
    
6. Click **Save** on the Sync page. 
    


