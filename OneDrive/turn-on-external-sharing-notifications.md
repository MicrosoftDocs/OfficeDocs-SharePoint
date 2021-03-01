---
title: "Control notifications"
ms.reviewer: shahna
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
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
- MET150
ms.assetid: b640c693-f170-4227-b8c1-b0a7e0fa876b
description: "Allow users to receive notifications about file activity in OneDrive and SharePoint."
---

# Control notifications

By default, users can receive notifications about file activity in OneDrive and SharePoint. These notifications can appear across apps and devices. For example, the service can send notifications through the Firebase Cloud Messaging service to the Office mobile app for Android or the Apple Push Notification service to the Office mobile app for iOS. It can also send notifications to the OneDrive sync app for Windows or Mac. As a global or SharePoint admin in Microsoft 365, you can turn off these notifications for all users for compliance purposes. If you allow these notifications, users can select to turn them off app by app where they don’t want them.

> [!NOTE]
> Currently, the service sends notifications to users when files are shared with them. Later, it will send notifications when people @mention the user in a comment. Other notifications might be added in the future. 
  
## Allow or block notifications

1. Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Settings page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Settings page.
    
2. Select the **Notifications** setting for OneDrive.
  
3. Select or clear **Allow notifications**.
  
This setting is the same as the setting on the Notifications page of the OneDrive admin center called "Display device notifications to users when OneDrive files are shared with them". You can also control this setting in PowerShell by using [Set-SPOTenant -NotificationsInOneDriveForBusinessEnabled](/powershell/module/sharepoint-online/set-spotenant).

The Notifications page of the OneDrive admin center includes three other settings under "Email OneDrive owners when":

- Other users invite additional external users to shared files. You can also control this by using [Set-SPOTenant -NotifyOwnersWhenItemsReshared](/powershell/module/sharepoint-online/set-spotenant). 
- External users accept invitations to access files. (This setting no longer works for the new sharing experience that appears in most places.)
- An anonymous access link is created or changed. You can also control this by using [Set-SPOTenant -OwnerAnonymousNotification](/powershell/module/sharepoint-online/set-spotenant).

## See also

For info about controlling SharePoint notifications, see [Control notifications](/sharepoint/notifications).
To control whether sharing emails include "At a glance" content, see [Set-SPOTenant -IncludeAtAGlanceInShareEmails](/powershell/module/sharepoint-online/set-spotenant).
