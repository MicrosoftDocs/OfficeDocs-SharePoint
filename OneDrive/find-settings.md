---
title: "Find OneDrive admin settings"
ms.reviewer: david.minasyan
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
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
description: "Learn where to find features from the OneDrive admin center. "
---

# Find OneDrive admin settings

This article covers all the features in the OneDrive admin center and where you can find them in other places.

## Sharing page

Go to the [Sharing page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=sharing&modern=true)

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Sharing page in OneDrive admin center](media/sharing-page.png)|![Sharing page in SharePoint admin center](media/sp-sharing-page.png) |

## Sync page

Go to the [Settings page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and select **Sync**.

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Sync page in the OneDrive admin center](media/sync-page.png)|![Sync settings in the SharePoint admin center](media/sp-sync-settings.png) |

## Storage page

Go to the [Settings page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true). To change the default storage setting, select **Storage limit**. To change the retention setting for deleted users, select **Retention**. 

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Storage page in the OneDrive admin center](media/storage-page.png)|![OneDrive settings on the Settings page in the SharePoint admin center](media/settings-page.png) |

## Device access page

Go to the [Access control page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=accessControl&modern=true). To control access based on network location, select **Network location**. To control access from apps that can't enforce device-based restrictions, select **Apps that don't use modern authentication**.

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Device access page in the OneDrive admin center](media/device-access.png)|![Access control page in the SharePoint admin center](media/access-control.png) |

The policy settings under "Mobile application management" are no longer being updated. We recommend [creating app protection policies](https://endpoint.microsoft.com/?ref=AdminCenter#blade/Microsoft_Intune_DeviceSettings/AppsMenu/appProtection) in the Microsoft Endpoint Manager admin center. [Learn how](/mem/intune/apps/app-protection-policies). Refer to the following table to identify the Intune settings that correspond with the settings in the OneDrive admin center. 

| OneDrive | Intune |
|:-----|:-----|
|Block downloading files in the apps |Save copies of org data  <br/> |
|Block taking screenshots in the Android apps <br/> |Screen capture and Google Assistant  <br/> |
|Block copying files and content within files <br/> |Restrict cut, copy, and paste between other apps  <br/> |
|Block printing files in the apps <br/> |Printing org data  <br/> |
|Block backing up app data <br/> |Prevent backups  <br/> |
|Require an app passcode <br/>Number of attempts before app is reset <br/>Passcode length <br/>Require complex passcode <br/>Allow fingerprint instead of passcode (iOS only) <br/> |PIN for access  <br/> MAX PIN attempts<br/>Select minimum PIN length<br/>Simple PIN<br/>Allow fingerprint instead of PIN<br/>|
|Block opening OneDrive and SharePoint files in other apps <br/> |Send org data to other apps  <br/> |
|Encrypt app data when the device is locked <br/> |Encrypt org data  <br/> |
|Require Office 365 sign-in every 7 days <br/> |Recheck the access requirements after (minutes of inactivity)  <br/> |
|When a device is offline: Minutes to verify user access after <br/> |Offline grace period (for "Block access")  <br/> |
|When a device is offline: Days to wipe app data after <br/> |Offline grace period (for "Wipe data")  <br/> |

## Compliance

This page contains links to Office 365 Security & Compliance. [View the compliance and risk management solutions available in Microsoft 365](https://compliance.microsoft.com/solutioncatalog)

- [Search the audit log](https://compliance.microsoft.com/auditlogsearch?viewid=Search)
- [Create a DLP policy](https://compliance.microsoft.com/datalossprevention?viewid=policiesn)
- [View DLP policy match reports](https://compliance.microsoft.com/reports/dlppolicymatchesreport)
- [Create a retention policy](https://compliance.microsoft.com/informationgovernance?viewid=retention)
- [Create an eDiscovery case](https://compliance.microsoft.com/classicediscovery)
- [Create an alert](https://compliance.microsoft.com/compliancealerts)

## Notifications

For the "Display device notifications to users when OneDrive files are shared with them" setting, Go to the [Settings page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and select the OneDrive **Notifications** setting.

| Classic | New |
|:-----|:-----|
|![Notifications page in the OneDrive admin center](media/notifications-od.png)|![NOtifications setting in the SharePoint admin center](media/notifications.png) |

For info about the "E-mail OneDrive owners when" settings, refer to the following table.

| Classic | New |
|:-----|:-----|
|Other users invite additional external users to shared files <br/> |This setting is available in PowerShell (`Set-SPOTenant -NotifyOwnersWhenItemsReshared`).  <br/> |
|External users accept invitations to access files <br/> |This setting no longer works for the new sharing experience that appears in most places.  <br/> |
|An anonymous access link is created or changed <br/> |This setting is available in PowerShell (`Set-SPOTenant -OwnerAnonymousNotification`).  <br/> |

## Data migration

This page redirects to the [Migration page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migration&modern=true).

## Geo locations

Go to the [Geo locations page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=geoLocationsg&modern=true).

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Geo locations page in the OneDrive admin center](media/geo-locations.png)|![New geo locations](media/new-geo-locations.png)|

