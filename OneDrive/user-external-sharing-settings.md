---
title: "Change the external sharing setting for a user's OneDrive"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODB160
- MET150
ms.assetid: 64aa1f56-d7f6-4500-a408-1fde8fe6db36
description: "Learn how to change the OneDrive external sharing setting for a user in the Microsoft 365 admin center."
---

# Change the external sharing setting for a user's OneDrive

After you set the organization-wide sharing settings for SharePoint and OneDrive, you can further restrict the external sharing for a specific OneDrive user. 

> [!NOTE]
> Instead of changing the external sharing setting for an individual user's OneDrive, you might want to block external sharing of sensitive information for all users. To learn how, see [Overview of data loss prevention policies](/office365/securitycompliance/data-loss-prevention-policies).

  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, select **Users** > **Active users**.

4. Select the user.

5. Under **OneDrive Settings**, next to **External sharing**, click **Edit**.

6. Select a new external sharing level, and then click **Save**.

> [!NOTE]
> You can also change the external sharing setting for a specific OneDrive user by using Microsoft PowerShell and running the cmdlet Set-SPOSite with the parameter -SharingCapability. For more info, see [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite).
    

