---
title: "Block syncing of specific file types"
ms.reviewer: gacarini
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: 7d7168dd-9015-4245-a971-61b504f834d6
description: "In this article, you'll learn how to prevent users from uploading specific file types using the OneDrive admin center."
---

# Block syncing of specific file types

You can prevent users from uploading specific file types when they sync their OneDrive files.

> [!NOTE]
> This setting prevents file types from being uploaded but not downloaded. If users already have blocked file types in their OneDrive, the files will sync to their computer, but any changes they make on their computer won't be uploaded.

  
 **To block uploading of specific file types**
  
1. Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
 
   > [!NOTE]
   > If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Sharing page. 
   > 
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Select **Sync**.

    ![Sync settings in the SharePoint admin center](media/sp-sync-settings.png)
  
3. Select the **Block upload of specific file types** check box.

4. Enter the file name extensions you want to block, for example: **exe** or **mp3**.

    > [!IMPORTANT]
    > Do not include the periods with the extensions, or any other punctuation, spaces, or special characters.
  
5. Select **Save**.

   > [!NOTE]
   > When you configure this setting, it takes approximately 8 hours for the OneDrive sync app to detect it and apply the change.

For info about setting this sync app restriction by using PowerShell, see [Set-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/set-spotenantsyncclientrestriction). For info about using a policy to block upload of specific files, see [Exclude specific kinds of files from being uploaded](use-group-policy.md#exclude-specific-kinds-of-files-from-being-uploaded).


