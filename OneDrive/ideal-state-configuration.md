---
title: "Ideal state configuration"
ms.reviewer: kaarins
ms.author: kaarins
author: jackwi-alt
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
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
- GOB150
- GOB160
- MET150
ms.assetid: b664e743-ae8b-4a93-aefd-1b20c584a93a
description: "Learn how IT admins can use a checklist to have an ideal state configuration in realizing the full potential of OneDrive both from admin and user perspectives."
---

# Ideal state configuration

For the Sync *ideal state* configuration, use this checklist:

- **Update & Ring**:
  - Allows traffic to oneclient.sfx.ms and g.live.com.
  - Some users are in Insiders; the rest are in Production.
  For more info, see [Sync app update process](sync-client-update-process.md).

- **Windows Notification Service**:
  - Allows traffic to *.wns.windows.com.
  For more info, see [Configure sync on Windows]().

- **Files On-Demand & Storage Sense**:
  - Ensure it's enabled.
  - Enable Storage Sense policies.
  For more info, see [Set Files On-Demand states](files-on-demand-windows.md) and [Set Files On-Demand states](files-on-demand-mac.md).

- **Office integration**:
  - Ensure it's enabled.
  For more info, see [Transition from previous sync app](transition-from-previous-sync-client.md).

- **Silent account configuration**:
  - Enable policy.
  For more info, see [Use silent account configuration](use-silent-account-configuration.md).

- **Known Folder Move (KFM)**:
  - Enable silent policy onm all new devices.
  - Enable policy gradually on existing devices.
  For more info, see [Redirect known folders](redirect-known-folders.md).

To realize the full potential of OneDrive both from admin and user perspectives, make sure you implement these six items.

To provide a seamless transition for your users, we encourage admins to plan data migration and adoption well in advance. For planning purposes, use the following resources.

## OneDrive deployment quick reference

The OneDrive deployment quick reference includes:

- **Planning**:
  - How much content does your organization have?
  - Where do users put files today?

- **Data migration**:
  - Use SharePoint Migration Tool (SPMT) or engage with FastTrack.
  - Migrate existing enterprise content directly top the cloud.

- **Prep and deploy OneDrive Sync**:
  - Apply OneDrive GPOs.
  - Configure OneDrive Sync.
  - Use Known Folder Move (KFM) for documents, desktop, and pictures known folders.
  - Deploy Onedrive to PCs and Macs.
  - Enable SharePoint site Sync and automount relevant Teams sites.

- **User engagement**:
  - Deploy OneDrive mobile.
  - Known Folder Move (KFM) and Files On-Demand.
  - Help users engage and discover the power of OneDrive.

- **Operate**:
  - Automatic Updates or self-managed *Enterprise* ring?
  - Remove Groove.exe from your Office install.

For more info, see [OneDrive documentation](https://docs.microsoft.com/OneDrive).

## OneDrive user adoption resources

The OneDrive resource center serves as your one-stop shop for all adoption and change management-related content. Use it to:

- Recruit stakeholders and empower champions.

- Prioritize your scenarios and measure success.

- Implement a communications campaign and execute launch events.

- Train users and ready your Help desk.

For more info, see [OneDrive Adoption Resources](https://aka.ms/OnedriveAdoption).