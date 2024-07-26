---
ms.date: 07/25/2024
title: Set up OneDrive in Omnissa Horizon Virtual Apps
ms.reviewer: 
ms.author: haroldw
author: haroldwongms
manager: tgrandison
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom:
- Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection:
- Strat_OD_admin
- M365-collaboration
description: In this article, you'll learn how to enable OneDrive in Omnissa Horizon Virtual Apps.
---

# Set up OneDrive in Omnissa Horizon Virtual Apps

You can enable OneDrive in Horizon Virtual Apps using the Omnissa Dynamic Environment Manager.

## Prerequisites

To set up and run OneDrive in Horizon Virtual Apps, you'll need to configure and install the Omnissa Dynamic Environment Manager (DEM), which you can learn more about on the [Omnissa website](https://docs.omnissa.com/bundle/DEMInstallConfigGuideV2312/page/IntroductiontoDynamicEnvironmentManager.html).

For more information on configuring published apps with Omnissa Horizon, see the [guidance articles on the Omnissa website](https://docs.omnissa.com/bundle/Desktops-and-Applications-in-HorizonV2312/page/ConfigureHorizon8forPublishedApplicationsDelivery.html).

## Configure Dynamic Environment Manager for OneDrive

1. Launch the Omnissa Dynamic Environment Manager management console, select **Create Config File** and select **Use an Application Template**.

1. Select the application template (Microsoft Office 2016 and 2019, or Microsoft 365), **Select OneDrive for Business** and click **Next**.

1. Provide the file name and description and select **Finish**.

1. Add the following **Import / Export** settings:

    `[IncludeRegistryTrees]` \
    `HKCU\Software\Microsoft\Office` \
    `HKCU\Software\Microsoft\Internet Explorer` \
    `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` \
    `HKCU\Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Cached` \
    `HKCU\Software\Microsoft\OneDrive`

    `[IncludeFolderTrees]` \
    `<Appdata>\Microsoft\Windows\Recent` \
    `<Appdata>\Microsoft\crypto` \
    `<Appdata>\SystemCertificates` \
    `<LocalAppdata>\Microsoft\IdentityCache` \
    `<LocalAppdata>\Microsoft\Internet Explorer` \
    `<LocalAppdata>\Microsoft\Windows\INetCache` \


## Validate OneDrive as default save location

Using the Omnissa Horizon client, launch any Microsoft Office or Microsoft 365 app.

1. Activate Microsoft Office or Microsoft 365.
2. After activation, save a document to verify the default save location is OneDrive.
