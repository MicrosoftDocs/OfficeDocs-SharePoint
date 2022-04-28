---
title: "OneDrive sync reports in the Apps Admin Center"
ms.reviewer: dmalayeri
ms.author: adjoseph
author: adeejoseph
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
- m365initiative-healthyonedrive
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: e1b3963c-7c6c-4694-9f2f-fb8005d9ef12
description: Learn how to proactively monitor OneDrive health, devices, and usage across an organization using the OneDrive sync reports.
---

# OneDrive sync reports in the Apps Admin Center

The OneDrive sync health dashboard in the Microsoft 365 [Apps Admin Center](https://config.office.com/) tracks the health of your sync app devices to provide you with actionable reporting insights on OneDrive usage across your organization. Using sync reports, you can proactively track relevant health errors and advisories, check the sync status and app version of individual devices, and monitor Known Folder Move roll out.

>[!IMPORTANT]
> This feature is in preview and isn't available to everyone. Review the requirements to determine eligibility.

The health insights range from a high-level executive summary to a comprehensive view of sync status per device, allowing you to quickly identify and resolve common issues while improving user experience.  

Having more visibility into what’s happening with sync can help you proactively educate users while increasing OneDrive adoption.

## Requirements  

- OneDrive sync apps on the Insiders or Production ring. Devices on the Deferred ring aren't eligible for the preview. [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring)

- OneDrive Sync app version 22.060 or later for Windows.

- [Global Administrator role](/microsoft-365/admin/add-users/about-admin-roles) or [Office apps admin role](/microsoft-365/admin/add-users/about-admin-roles) to set up the dashboard. After setup, only [Global reader role](/microsoft-365/admin/add-users/about-admin-roles) is required to view the dashboard.

- Devices in your organization should allow connections to `https://clients.config.office.net`.

>[!NOTE]
> This feature isn’t available to customers who have the following plans: Office 365 operated by 21Vianet, Office 365 GCC, or Office 365 GCC High and DoD.

## Set up the OneDrive sync health dashboard

This section guides you through the steps you need to take to enable sync reports on Windows devices.

>[!NOTE]
> The previous Group Policy HKLM\SOFTWARE\Policies\Microsoft\OneDrive\SyncAdminReports is still supported and will continue to be supported for 60 days after General Availability is announced. We recommend that admins deploy the GPO now, to ensure a smooth transition at that time.

1. Ensure you have the required role and app versions listed in the [previous section](#requirements).

2. Go to [Microsoft 365 Apps admin center](https://config.office.com) and sign in as a global admin or Office apps admin.

3. From the left navigation menu, select **Health** > **OneDrive Sync**

4. Select **Enable preview features** to accept the license terms.

    :::image type="content" source="media/enable-preview.png" alt-text="Screenshot of enable preview features button.":::

    The OneDrive sync health dashboard appears.

   :::image type="content" source="media/sync-home.png" alt-text="Screenshot of OneDrive sync health dashboard.":::

5. Enable the OneDrive EnableSyncAdminReports Group Policy Object (GPO).

    > [!IMPORTANT]
    > - You must enable this setting on the devices from which you want to get reports. This setting has no impact on users.
    > - We recommend a gradual rollout starting with a few test devices per day, then up to 100 devices per day, then gradually up to 10,000 devices per day until you finish.

    You can enable this setting in multiple ways:

    - Edit the registry

        a. Go to HKLM\SOFTWARE\Policies\Microsoft\OneDrive

        b. Right-click > **New** > **DWORD (32-bit) Value**

        c. Name: EnableSyncAdminReports

        d. Type: REG_DWORD

        e. Data: 1

        :::image type="content" source="media/createregkey.png" alt-text="Screenshot image depicting the creation of a new key in the Registry Editor":::

    - Run Command Prompt as an administrator, and then run the following command:

       `reg.exe add HKLM\Software\Policies\Microsoft\OneDrive /v EnableSyncAdminReports /t REG_DWORD /d 1`

    - Use [Group Policy](use-group-policy.md#manage-onedrive-using-group-policy)

    To apply the setting on a single PC, follow these steps:

    - Open Group Policy Editor (gpedit.exe)

    - Go to Computer Configuration\Administrative Templates\OneDrive.

    - Choose **Enable sync health reporting for OneDrive**.

       > [!IMPORTANT]
       > After you enable the EnableSyncAdminReports setting on devices, it takes up to three days for reports to be available.

    - Select **Enabled** and then press **OK**.

## OneDrive Sync health dashboard

> [!NOTE]
> After you set up the dashboard as described in the previous section, the Global Reader admin role is sufficient to access and view reports.

The **Overview** tab provides aggregated insights on devices that have sync errors, [Known Folder Move](redirect-known-folders.md) rollout status, and adoption of sync app versions and update ring.

:::image type="content" source="media/sync-dashboard.png" alt-text="Screenshot of Overview tab of OneDrive sync health dashboard.":::

The **Details** tab provides detailed info for each user and device to help you understand and troubleshoot sync errors.

:::image type="content" source="media/sync-health-ui.png" alt-text="Screenshot of OneDrive sync health details tab.":::

The tab reports on the following diagnostic data:

- User: The name of the user
- User email: The email address of the user
- Computer name: The name of the device
- Errors: Details including the counts, and error messages users are seeing
- Known folders: Details including enabled status for each folder (Desktop, Documents, Pictures)
- OneDrive app version: The currently installed OneDrive sync app version
- Operating system version: The current version of the OS running on the device
- Last synced timestamp (UTC): The last time sync app was fully up to date with the cloud
- Last status reported timestamp (UTC): The last time the sync app reported its diagnostic data to the dashboard

### Data for the OneDrive sync health dashboard

The sync reports use the required service data and diagnostic data that your OneDrive sync apps send to Microsoft. You are in control of which data and which devices send this data. Use the EnableSyncAdminReports setting to control which devices send data.

Diagnostic data is always under your control. To learn more about diagnostic data and the controls available to you, see [Overview of privacy controls for Microsoft 365 Apps](/deployoffice/privacy/overview-privacy-controls). To learn more about required service data, see [Required diagnostic data for Office](/deployoffice/privacy/required-diagnostic-data).

## Troubleshooting

Use this section to troubleshoot if the OneDrive sync reports don't appear after three days.

> [!IMPORTANT]
> If you enable the EnableSyncAdminReports setting on devices that don't meet the [requirements](#requirements), it will have no effect. The app won't send reports.

1. Confirm that the sync app is on the Insiders or Production ring. Run Command Prompt as an administrator, and then run the following command:  

    `reg.exe query HKLM\Software\Policies\Microsoft\OneDrive /v GPOSetUpdateRing`

    If the output from the script is **not** `dword:00000000`, your device is on the Insiders or Production ring.

2. Confirm that the SyncAdminReports setting is applied to the device. Run Command Prompt as an administrator, and then run the following command:

    `reg.exe query HKLM\Software\Policies\Microsoft\OneDrive /v EnableSyncAdminReports`

    The output should look like this:

    :::image type="content" source="media/syncregkeyquery.png" alt-text="Screenshot of expected command prompt output":::

    If the EnableSyncAdminReports setting wasn't applied, go back and follow the steps under [Set up the OneDrive sync health dashboard](#set-up-the-onedrive-sync-health-dashboard).

If the device is on the Insiders or Production ring and the setting was applied correctly, wait for 36 hours with the device turned on and signed in to OneDrive. If the device still doesn't appear on the dashboard, open a support ticket with Microsoft. For more information, see the next section, [Report a problem](#report-a-problem).

## Report a problem

If you encounter a problem with viewing the report dashboard, first verify that you've completed the steps in the troubleshooting section.

If problems persist after troubleshooting, [open a support ticket with Microsoft](/microsoft-365/admin/contact-support-for-business-products). Make sure that the device isn't powered off during this period so that the sync app can still run and send a health report.

For quick investigations, be sure to have the date and time when the SyncAdminReports setting was enabled and either the user’s email or the OneDrive device ID available in your issue report.

To get the OneDrive device ID, select the OneDrive sync app in the notification area > **Help & Settings** > **Settings** > **About**.

## Send feedback

To make a feature suggestion, use the Feedback button in the top, right corner of the dashboard page.

:::image type="content" source="media/sync-feedback.png" alt-text="Screenshot of Feedback form.":::
