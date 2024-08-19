---
ms.date: 04/12/2024
title: "Configure settings with Intune"
ms.reviewer: kafeaver
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- onedrive-toc
search.appverid:
- MET150
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
description: "In this article, you learn how to configure the Microsoft OneDrive sync app by using settings catalog in Microsoft Intune."
---

# Configure settings with Intune

Profiles in Microsoft Intune let you configure settings and push them to devices in your organization. Settings catalog built in to Microsoft Intune make configuring the Microsoft OneDrive sync app easier than ever.

## Create a profile

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
1. Select **Devices** > **Configuration** > **Create**.
1. Enter the following properties:

    - **Platform**: Select **Windows 10 and later**.
    - **Profile type**: Select **Settings catalog**.

1. Select **Create**.
1. In **Basics**, enter the following properties:

    - **Name**: Enter a descriptive name for the profile. Name your profiles so you can easily identify them later. For example, a good profile name is **Windows: OneDrive**.
    - **Description**: Enter a description for the profile. This setting is optional, but recommended.

1. Select **Next**.

1. In **Configuration settings**, select **Add settings**.

1. In the settings picker, select **OneDrive** to see all the available settings.

1. Select any setting you want to configure. Or, choose **Select all these settings**. After you add your settings, close the settings picker.
    For info about these settings, see [Use OneDrive policies](use-group-policy.md). For info about the recommended settings, see [Recommended sync app configuration](ideal-state-configuration.md).

    :::image type="content" source="media/intune-settings-catalog.png" alt-text="A screenshot showing the configuration of the Intune settings catalog policy for OneDrive." lightbox="media/intune-settings-catalog.png":::

1. Configure the settings the way you want, and then select **OK**.
    > [!NOTE]
    > Some settings require entering your tenant ID. [Learn how to find it](find-your-office-365-tenant-id.md). When you're done, select **Next**.

1. Select scope tags, and then select **Next**. For information about scope tags, see [Use RBAC and scope tags for distributed IT](/mem/intune/fundamentals/scope-tags).

1. In **Assignments**, include or exclude the profile from selected groups. For info about assigning profiles, see [Assign user and device profiles](/mem/intune/configuration/device-profile-assign).

    > [!NOTE]
    > If the profile is assigned to user groups, then configured ADMX settings apply to any device that the user enrolls, and signs in to. If the profile is assigned to device groups, then configured ADMX settings apply to any user that signs into that device. This assignment happens if the ADMX setting is a computer configuration (`HKEY_LOCAL_MACHINE`), or a user configuration (`HKEY_CURRENT_USER`). With some settings, a computer setting assigned to a user may also impact the experience of other users on that device.
    >
    > For more info, see [User groups vs. device groups](/mem/intune/configuration/device-profile-assign#user-groups-vs-device-groups).

    When you're done, select **Next**.

1. In **Review + create**, review your settings. When you select **Create**, your changes are saved, and the profile is assigned. The policy is also shown in the profiles list.

## See also

- [Use the settings catalog to configure settings on Windows](/mem/intune/configuration/settings-catalog)
- [Understanding ADMX-backed policies](/windows/client-management/mdm/understanding-admx-backed-policies)
- [Monitor device profiles in Microsoft Intune](/mem/intune/configuration/device-profile-monitor)
