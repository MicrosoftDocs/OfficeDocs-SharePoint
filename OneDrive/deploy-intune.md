---
title: "Deploy OneDrive apps using Intune"
ms.reviewer: 
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
ms.custom:
- seo-marvel-apr2020
search.appverid:
- MET150
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
ms.assetid: 3f3a511c-30c6-404a-98bf-76f95c519668
description: "In this article, you'll learn how you can use Intune to deploy the OneDrive mobile app to iOS and Android devices and the OneDrive sync app to Windows 10."
---

# Deploy OneDrive apps by using Intune

If you're a global admin or assigned [a role in Intune](/mem/intune/fundamentals/role-based-access-control) that gives you the necessary permissions, you can use Intune to deploy OneDrive apps. Before you begin deploying, make sure you review the planning information and deployment options in the [OneDrive guide for enterprises](plan-onedrive-enterprise.md).

## Deploy the OneDrive app for iOS or Android

To deploy apps in Intune, you use the [Microsoft Endpoint Manager admin center](https://endpoint.microsoft.com/?ref=AdminCenter#blade/Microsoft_Intune_DeviceSettings/AppsMenu/allApps). For the steps to deploy apps to iOS devices, see [Add iOS store apps to Microsoft Intune](/mem/intune/apps/store-apps-ios). For the steps to deploy apps to Android devices, see [Add Android store apps to Microsoft Intune](/mem/intune/apps/store-apps-android). Use **https://play.google.com/store/apps/details?id=com.microsoft.skydrive** as the Appstore URL. For info about assigning apps to groups, see [Assign apps to groups with Microsoft Intune](/mem/intune/apps/apps-deploy).

## Deploy the OneDrive sync app to Windows 10 devices 

Although the sync app comes with Windows 10, you might choose to switch to [per-machine installation](per-machine-installation.md).

For info about configuring sync app settings using Intune, see [Use administrative templates in Intune](configure-sync-intune.md).
