---
ms.date: 11/08/2023
title: "Change the external sharing setting for a user's OneDrive"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom: onedrive-toc
search.appverid:
- ODB160
- MET150
ms.assetid: 64aa1f56-d7f6-4500-a408-1fde8fe6db36
description: "Learn how to change the OneDrive external sharing setting for a user in the Microsoft 365 admin center."
---

# Change the external sharing setting for a user's OneDrive

After you set the organization-wide sharing settings for Microsoft SharePoint and Microsoft OneDrive, you can further restrict the external sharing for a specific OneDrive user. 

> [!TIP]
> Instead of changing the external sharing setting for an individual user's OneDrive, you might want to block external sharing of sensitive information with [Microsoft Purview data loss prevention](/purview/dlp-learn-about-dlp).
  
1. Sign in to https://admin.microsoft.com as a Global Administrator.
    
2. In the left pane, select **Users** \> **Active users**.

3. Select the user.

4. Select the **OneDrive** tab, and under **Sharing**, select **Manage external sharing**.

5. Select a new external sharing level, and then select **Save**.

> [!NOTE]
> You can also change the external sharing setting for a specific OneDrive user by using PowerShell and running the Set-SPOSite cmdlet with the parameter -SharingCapability. For more info, see [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite).
    


