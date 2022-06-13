---
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

> [!NOTE]
> Instead of changing the external sharing setting for an individual user's OneDrive, you might want to block external sharing of sensitive information for all users. To learn how, see [Learn about Microsoft Purview data loss prevention](/compliance/dlp-learn-about-dlp).

  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center. 
    
2. In the left pane, select **Users** \> **Active users**.

3. Select the user.

4. Select the **OneDrive** tab, and under **Sharing**, select **Manage external sharing**.

5. Select a new external sharing level, and then select **Save**.

> [!NOTE]
> You can also change the external sharing setting for a specific OneDrive user by using Microsoft PowerShell and running the cmdlet Set-SPOSite with the parameter -SharingCapability. For more info, see [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite).
    

