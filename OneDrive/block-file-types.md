---
title: "Block syncing of specific file types"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: 7d7168dd-9015-4245-a971-61b504f834d6
description: "Learn how to prevent users from uploading specific file types using the OneDrive admin center. "
---

# Block syncing of specific file types

You can prevent users from uploading specific file types when they sync their OneDrive for Business files.

   > [!NOTE]
   > This setting prevents file types from being uploaded but not downloaded. If users already have blocked file types in their OneDrive, the files will sync to their computer, but any changes they make on their computer won't be uploaded. 
  
 **To block uploading of specific file types**
  
1. Open the [OneDrive admin center](https://admin.onedrive.com/?v=SyncSettings), and click **Sync** in the left pane. 
    
    ![The Sync page of the OneDrive admin center](media/1c3bf6d6-7b82-4c73-9df7-c8551a0c2922.png)
  
2. Select the **Block syncing of specific file types** check box. 
    
3. Click **Edit**.
    
4. Type the file name extensions you want to block, for example: **exe** or **mp3**. 
    
    > [!IMPORTANT]
    > Do not include the periods with the extensions, or any other punctuation, spaces, or special characters. 
  
5. Click **Save** on the Sync page. 
    
For info about setting this sync app restriction by using PowerShell, see [Set-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/set-spotenantsyncclientrestriction)

