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
ms.service: sharepoint-online
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
description: "Allow users to receive notifications about SharePoint site activity."
---

# Control notifications

By default, SharePoint mobile app users can receive notifications about site activity. The service sends these notifications through the Firebase Cloud Messaging service for Android or the Apple Push Notification service for iOS. As a global or SharePoint admin in Microsoft 365, you can turn off these notifications for all users for compliance purposes. If you allow these notifications, users can select to turn them off.

Currently, notifications are sent for the following activities:

- SharePoint news published (users receive these based on relevancy)
- Page comment (sent to the page author)
- Page comment reply (sent to the page author and the author of the comment that is being replied to)
- Page comment mention (sent to person @ mentioned)
- Page like (sent to the page author)

Other notifications might be added in the future.

>[!NOTE]
>Notifications aren't available for the US government environments, Office 365 Germany, or Office 365 operated by 21Vianet (China).

## Allow or block notifications

1. Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
    
2. Select the **Notifications** setting for SharePoint.
  
3. Select or clear **Allow notifications**.
  
You can also control this setting in PowerShell by using [Set-SPOTenant -NotificationsInSharePointEnabled](/powershell/module/sharepoint-online/set-spotenant).

## See also

For info about controlling OneDrive notifications, see [Control notifications](/onedrive/turn-on-external-sharing-notifications).

To control whether sharing emails include "At a glance" content, see [Set-SPOTenant -IncludeAtAGlanceInShareEmails](/powershell/module/sharepoint-online/set-spotenant).
