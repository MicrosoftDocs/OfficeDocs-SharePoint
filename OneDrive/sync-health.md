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
#Customer intent: As an IT administrator, I want to proactively monitor sync health in OneDrive, so that I can mitigate user error while increasing sync consumption across the organization. .
---

# OneDrive sync reports in the Apps Admin Center

Use the OneDrive sync health dashboard in the Microsoft 365 [Apps Admin Center](https://config.office.com/) to get an executive summary of everything happening with OneDrive so that you can resolve common issues quickly and focus on other strategic tasks as an administrator.

:::image type="content" source="media/sync-dashboard.png" alt-text="Image of the overview page of the sync reports dashboard":::

Proactively keeping OneDrive healthy helps ensure that your organization's information is protected. The dashboard provides you with sync health reports for tracking relevant health issues and advisories, checking the sync status and app version of individual devices, and monitoring Known Folder Move roll out.

In this article, you'll learn how to set up and navigate the sync health dashboard to better manage your OneDrive users and increase OneDrive adoption.

## Requirements  

Before getting started, be sure that you're familiar with the requirements needed to access the dashboard:

- OneDrive sync apps on the Insiders or Production ring. Devices on the Deferred ring aren't eligible for the preview. [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring).

- OneDrive sync app version 22.087 or later for Windows and macOS.

- [Global Administrator role](/microsoft-365/admin/add-users/about-admin-roles) or [Office apps admin role](/microsoft-365/admin/add-users/about-admin-roles) to set up the dashboard. After setup, only [Global reader role](/microsoft-365/admin/add-users/about-admin-roles) is required to view the dashboard.

- Devices in your organization should allow connections to `https://clients.config.office.net`.

>[!NOTE]
> This feature isn’t available to customers who have the following plans: Office 365 operated by 21Vianet, Office 365 GCC, or Office 365 GCC High and DoD.

## Set up the OneDrive sync health dashboard

In this section, you'll learn how to set up sync reports on Windows and macOS devices.

# [Windows](#tab/windows)

This tab provides how-to steps for enabling sync reports on Windows devices.

>[!NOTE]
> The previous Group Policy HKLM\SOFTWARE\Policies\Microsoft\OneDrive\SyncAdminReports is still supported and will continue to be supported for 60 days after General Availability is announced. We recommend that admins deploy the GPO now, to ensure a smooth transition at that time.

1. Ensure you have the required role and app versions listed in the [previous section](#requirements).

2. Go to [Microsoft 365 Apps admin center](https://config.office.com) and sign in as a global admin or Office apps admin.

3. From the left navigation menu, select **Health** > **OneDrive Sync**

4. Select **Enable preview features** to accept the license terms.

    :::image type="content" source="media/enable-preview.png" alt-text="Screenshot of enable preview features button.":::

5. Enable the OneDrive EnableSyncAdminReports Group Policy Object (GPO).

    > [!IMPORTANT]
    > **You must enable this setting on the devices from which you want to get reports.** This setting has does not affect  users. We recommend a gradual rollout starting with a few test devices per day, then up to 100 devices per day, then gradually up to 10,000 devices per day until you finish.

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

    - Select **Enabled** and then press **OK**.

> [!IMPORTANT]
> After you enable the EnableSyncAdminReports setting on devices, it takes up to three days for reports to be available.

# [macOS](#tab/macos)

This tab provides how-to steps for enabling sync reports on macOS devices.

1. Ensure you have the required role and app versions listed in the [previous section](#requirements).

2. Go to the [Microsoft 365 Apps admin center](https://config.office.com) and sign in as a global admin or Office apps admin.

3. From the left navigation menu, select **Health** > **OneDrive Sync**

4. Select **Enable preview features** to accept the license terms.

    :::image type="content" source="media/enable-preview.png" alt-text="Screenshot of enable preview features button.":::

5. In the left navigation menu, select **Settings**.

6. Confirm that a **Tenant Association Key** has been generated in the text field.

7. Before proceeding, ensure that the OneDrive application has been quit.

8. Create a.plist file with the key **EnableSyncAdminReports**. You can also use a script to set the key. The key is the same whether you run the standalone or Mac App Store edition of the sync app. However, the .plist file name and domain name will be different. When you apply the setting, ensure that you target the appropriate domain depending on the edition of the sync app.

|| Standalone | Mac App Store |
|:-----|:-----|:-----|
|**.plist location  <br/>**|~/Library/Managed Preferences/com.microsoft.OneDrive.plist  <br/> |~/Library/Managed Preferences/com.microsoft.OneDrive-mac.plist  <br/> |
|**Domain <br/>**|com.microsoft.OneDrive  <br/> |com.microsoft.OneDrive-mac  <br/> |

9. Use the Terminal app to deploy the EnableSyncAdminReports setting onto your local computer.

    The example for this setting in the .plist file is:
<br/>\<key\>EnableSyncAdminReports\</key\><br/>\<(Bool)/\>

10. Refresh the preferences cache.

11. On the next start of OneDrive, the new setting will be picked up.

> [!IMPORTANT]
> After you enable the EnableSyncAdminReports setting on devices, it takes up to three days for reports to be available.

---

## Navigate the OneDrive Sync health dashboard

In this section, you'l learn how to successfully navigate the OneDrive Sync health dashboard. Learn about the reporting insights available to you and how they can help you proactively manage OneDrive for your organization.  

Jump to:

- [Overview](#overview)
- [Details](#details)
- [Issues](#issues)

> [!NOTE]
> After you set up the dashboard as described in the previous section, the Global Reader admin role is sufficient to access and view reports.

### Overview

The **Overview** tab (the default view) shows a summary of devices that have at least one sync issue, a percentage of the devices in your organization using [Known folder move](redirect-known-folders.md), and the number of devices running on the current version of OneDrive.

:::image type="content" source="media/sync-dashboard.png" alt-text="Screenshot of Overview tab of OneDrive sync health dashboard.":::

| Card name         | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
|Sync errors | *Shows how many devices have sync errors or not.* <br> <br> Sorting through errors can help you proactively reach out to educate people while resolving common issues and improving user experience. Users may not report OneDrive issues to you immediately. Unreported issues could lead to unwanted problems while they're working on important tasks. With the **Sync errors** card, you won't have to wait to be notified by users to take action. |
| Known folders          | *Shows a snapshot of the number of known folders currently in use.* <br><br> **Known Folder Move** allows people to keep their Desktop, Documents, and Pictures folders protected by syncing them to the cloud with OneDrive. If you’re rolling out Known Folder Move for your organization, the **Known folders** card is a great way for you to monitor progress.                                   |
| Sync app version         | *Shows the number of devices running on the current version of OneDrive.* <br><br>  Running the current version of OneDrive helps users stay up to date with all the latest and greatest fixes and features from Microsoft. Hover over the **Sync app version** card for a filtered view of operating systems on the current version. Note: Mac App store devices are excluded from this section and will appear in the count as "devices excluded".                                                                                  |
||

### Details

The **Details** tab shows all users, their current health state, their known folders currently moved in OneDrive, their current app version and operating system version, a timestamp of the last time the app was fully up to date, and a timestamp of the last time the sync app reported health data to the dashboard. An icon and status in the **Errors** column indicate the state of each device.

:::image type="content" source="media/sync-health-ui.png" alt-text="Screenshot of OneDrive sync health details tab.":::

This table provides a summary of the information found in each column of the **Details** tab:

| Column name       | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
|User | The name of the user |
| User email         | The user's email address                                   |
| Device name         | The device name |
| Errors         | The health status of a device   |
| Known folders        | The name of folders moved to OneDrive  |
| App version         | The current version of OneDrive running on the device |
| Operating system        | The current version of the OS running on the device  |
| Last synced timestamp (UTC)       | The last time that the sync app was fully up to date with the cloud  |
| Last status reported timestamp (UTC)        |  The last time that the sync app reported health data to the dashboard  |
||

Customize your view of which devices show up on the dashboard by using the filter option in the command bar. Standard filters include "all devices" where you can see every device and "devices with errors" where you'll only see devices with errors.

You can easily create a custom filter with your own conditions. From the command bar, select **Filter** > **New filter** to open the **Custom filter** panel. Name your filter and select your desired conditions. If you'd like to filter by app version, be sure that you enter the complete sync app version number including periods. Afterwards, select **Create** to use your new filter.

[![Screenshot of the custom filter panel.](media/custom-filter-inline.png) ](media/custom-filter-pane.png#lightbox)

When someone in your organization reports a problem with syncing files to OneDrive, you can investigate quickly without having to ask for extra details of the error message via Microsoft Teams chat or Outlook email. Select a user to see more information on their device and sync status. This detailed view lets you see a user's essential OneDrive information including any errors they might be experiencing.

:::image type="content" source="media/detail-panel-dashboard.png" alt-text="Image depicting Details panel with individual OneDrive user and device information":::

### Issues

The **Issues** tab shows you a list of OneDrive error messages found in the health report and the number of devices affected by them in your organization. Use this view to see if there are any common patterns between users and the errors present across your organization.

:::image type="content" source="media/issues-dashboard.png" alt-text="The Issues tab showing a list of errors present in devices.":::

You can learn more about the error and devices affected by selecting an error message from the list. The **Issues** panel will appear with a summary of the devices affected, along with a list of users and their current app version and operating system. Partner with your users to fix common OneDrive sync issues.

:::image type="content" source="media/error-message-panel.png" alt-text="Image depicting issues panel ":::

To learn more about OneDrive error messages, see [What do the OneDrive error codes mean?](https://support.microsoft.com/office/what-do-the-onedrive-error-codes-mean-f7a68338-e540-4ebf-ad5d-56c5633acded).

## Data for the OneDrive sync health dashboard

The sync reports use health data that your OneDrive sync apps send to Microsoft. You have choices when it comes to the technology you use and the data you share. Use the EnableSyncAdminReports setting to manage which devices send data.

To learn more about the controls available to you, see [Overview of privacy controls for Microsoft 365 Apps](/deployoffice/privacy/overview-privacy-controls). To learn more about required service data, see [Required service data for Office](/deployoffice/privacy/required-diagnostic-data).

## Known limitations and considerations

This section describes known limitations and considerations in sync reporting.

By default, device records are kept in inventory for 30 days, after which they expire from the report.

**Known folders:** Devices enabled for Known Folder Move will report as a device with 0-3 known folders. If a device isn't enabled for Known Folder Move, it will report as a device that is **Not applicable** in the **Known Folders** section of the **Overview** tab. In the **Details** tab, a hyphen ("-") will appear in the cell value of the **Known folders** table for devices that aren't applicable devices. This behavior is expected.

**Sync app version:** For devices using the Mac App Store edition of the sync app, the version installed on each device is displayed in the **Details** tab. However, the dashboard doesn't currently track whether or not the edition is the latest version of the sync app available in the Mac App Store. If any devices use this edition, they'll be excluded from the **Sync app version** section of the **Overview** tab and the number of excluded devices is displayed. This is the expected result.

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

We value your feedback. To submit feature suggestions and report issues, you can use the Feedback button in the top-right corner of the dashboard page.

:::image type="content" source="media/sync-feedback.png" alt-text="Screenshot of Feedback form.":::
