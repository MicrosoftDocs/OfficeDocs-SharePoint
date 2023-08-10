---
ms.date: 04/27/2021
title: "OneDrive sync reports in the Apps Admin Center"
ms.reviewer: dmalayeri
ms.author: mikeplum
author: MikePlumleyMSFT
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
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
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

Use the OneDrive sync health dashboard in the Microsoft 365 [Apps Admin Center](https://config.office.com/) to get an executive summary of everything happening with OneDrive so that you can resolve common issues quickly and focus on other strategic tasks as an administrator.

Proactively keeping OneDrive healthy helps ensure that your organization's information is protected. The dashboard provides you with sync health reports for tracking relevant health issues and advisories, checking the sync status and app version of individual devices, and monitoring Known Folder Move roll out.

In this article, you'll learn how to set up and navigate the sync health dashboard to better manage your OneDrive users and increase OneDrive adoption.

## Requirements  

Before getting started, be sure that you're familiar with the requirements needed to access the dashboard:

- OneDrive sync app version 22.232 or later for Windows and macOS.

- OneDrive sync apps on the Insiders, Production, or Deferred ring. [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring).

- [Global Administrator](/microsoft-365/admin/add-users/about-admin-roles), Office Apps Administrator or Microsoft 365 Administrator role access is required to enable and set up the dashboard for your organization. After the feature is enabled by one of these roles, one can also view the dashboard using [Global reader](/microsoft-365/admin/add-users/about-admin-roles) or Reports reader access. To learn more about administrator roles and permissions in Microsoft 365, visit [About Admin Roles](/microsoft-365/admin/add-users/about-admin-roles).

- Devices in your organization should allow connections to `https://clients.config.office.net`.

> [!NOTE]
> This feature isn’t available to customers who have the following plans: Office 365 operated by 21Vianet, Office 365 GCC, or Office 365 GCC High and DoD.

## Set up the OneDrive sync health dashboard

In this section, you'll learn how to set up sync reports on Windows and macOS devices.

# [Windows](#tab/windows)

This tab provides how-to steps for enabling sync reports on Windows devices.

### Prerequisite

> [!NOTE]
> The previous Group Policy HKLM\SOFTWARE\Policies\Microsoft\OneDrive\SyncAdminReports and Intune "Sync Admin Reports" settings are no longer supported. We recommend that you update your Group Policy Object(s) or Intune OneDrive profile(s) to use the new "Enable sync health reporting for OneDrive" as soon as possible.

1. Ensure you have the required role and app versions listed in the [previous section](#requirements).

2. Go to [Microsoft 365 Apps admin center](https://config.office.com) and sign in as a global admin or Office apps admin.

3. From the left navigation menu, select **Health** > **OneDrive Sync**.

4. In the left navigation menu, select **Setup**.

5. Verify that a **Tenant Association Key** is present in the text field. If the field is empty, select **Generate new key**.

    > [!NOTE]
    > When you generate a new key for the first time, it can take up to 30 seconds for it to appear.

6. Enable the OneDrive EnableSyncAdminReports setting via Group Policy Object or Intune.

> [!IMPORTANT]
> **You must enable this setting on the devices from which you want to get reports using one of the below methods.** This setting does not affect users. We recommend a gradual rollout starting with a few test devices per day, then up to 100 devices per day, then gradually up to 10,000 devices per day until you finish.

### Group Policy

You can enable this setting in multiple ways:

- Edit the registry

    a. Go to HKLM\SOFTWARE\Policies\Microsoft\OneDrive

    b. Right-click > **New** > **DWORD (32-bit) Value**

    c. Name: EnableSyncAdminReports

    d. Type: REG_DWORD

    e. Data: 1

    :::image type="content" source="media/createregkey.png" alt-text="Screenshot image depicting the creation of a new key in the Registry Editor":::

- Run Command Prompt as an administrator, and then run the following command:

   ```PowerShell
    reg.exe add HKLM\Software\Policies\Microsoft\OneDrive /v EnableSyncAdminReports /t REG_DWORD /d 1
   ```

- Use [Group Policy](use-group-policy.md#manage-onedrive-using-group-policy).

To apply the setting on a single PC, follow these steps:

- Open Group Policy Editor (gpedit.msc).

- Go to Computer Configuration\Administrative Templates\OneDrive.

- Choose **Enable sync health reporting for OneDrive**.

- Select **Enabled** and then press **OK**.
  
### Intune

To apply the setting through Intune, we recommend that you use the "Settings Catalog" profile type:

-  Go to [Microsoft Intune Admin Center](https://intune.microsoft.com) and sign in as a global admin, Intune admin role, or an account with sufficient RBAC permissions.

-  Click on Devices, Windows, and then click on "Configuration profiles".

-  Edit or create a new OneDrive profile (Platform - "Windows 10 and later", Profile type - "Settings Catalog").

-  If creating a new profile, provide a name for the profile and go to the Configuration settings tab. If editing a profile, you will by default go direct to the Configuration settings tab.

-  Click on "Add setting" and the Settings picker will be displayed on the right side of the UI.

-  In the search bar, add "OneDrive". Alternatively you can scroll down to the OneDrive settings.

-  Click on the checkbox next to the "Enable sync health reporting for OneDrive" setting name.

-  Close the Settings picker from the "X" at the top right.

-  Click on the toggle switch to set "Enable sync health reporting for OneDrive" to "Enabled".

-  If creating a new profile, continue through the wizard, assing scope tags if required, and assigning the profile as required. If you are editing the profile, click on the "Review + save" button.

> [!IMPORTANT]
> When you enable the EnableSyncAdminReports setting on devices, it can take up to three days for reports to be available. Devices will appear in the report after this time. Forcing a specific device to report data is unsupported.

# [macOS](#tab/macos)

This tab provides how-to steps for enabling sync reports on macOS devices.

1. Ensure you have the required role and app versions listed in the [previous section](#requirements).

2. Go to the [Microsoft 365 Apps admin center](https://config.office.com) and sign in as a global admin or Office apps admin.

3. From the left navigation menu, select **Health** > **OneDrive Sync**.

4. In the left navigation menu, select **Setup**.

5. Confirm that a **Tenant Association Key** has been generated in the text field.

6. Before proceeding, ensure that the OneDrive application has been quit.

7. Create a.plist file with the key **EnableSyncAdminReports**. You can also use a script to set the key. The key is the same whether you run the standalone or Mac App Store edition of the sync app. However, the .plist file name and domain name will be different. When you apply the setting, ensure that you target the appropriate domain depending on the edition of the sync app.

|| Standalone | Mac App Store |
|:-----|:-----|:-----|
|**.plist location  <br/>**|~/Library/Preferences/com.microsoft.OneDrive.plist  <br/> |~/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  <br/> |
|**Domain <br/>**|com.microsoft.OneDrive  <br/> |com.microsoft.OneDrive-mac  <br/> |

9. Use the Terminal app to deploy the EnableSyncAdminReports setting onto your local computer.

    Enter the following preference key to enable the setting:
<br/>\<key\>EnableSyncAdminReports\</key\>
</br>\<integer\>1\</integer\>

10. Refresh the preferences cache.

11. On the next start of OneDrive, the new setting will be picked up.

> [!IMPORTANT]
> After you enable the EnableSyncAdminReports setting on devices, it takes up to three days for reports to be available.

---

## Navigate the OneDrive Sync health dashboard

In this section, you'l learn how to successfully navigate the OneDrive Sync health dashboard. Learn about the reporting insights available to you and how they can help you proactively manage OneDrive for your organization.  

Jump to:

- [Overview](#overview)
- [Devices](#devices)
- [Issues](#issues)

> [!NOTE]
> After you set up the dashboard as described in the previous section, the Global Reader admin role is sufficient to access and view reports.

### Overview

The **Overview** tab (the default view) shows a summary of devices that have at least one sync issue, a percentage of the devices in your organization using [Known folder move](redirect-known-folders.md), and the number of devices running on the current version of OneDrive.

| Card name         | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
|Sync errors | *Shows how many devices have sync errors or not.* <br> <br> Sorting through errors can help you proactively reach out to educate people while resolving common issues and improving user experience. Users may not report OneDrive issues to you immediately. Unreported issues could lead to unwanted problems while they're working on important tasks. With the **Sync errors** card, you won't have to wait to be notified by users to take action. |
| Known folders          | *Shows a snapshot of the number of known folders currently in use.* <br><br> **Known Folder Move** allows people to keep their Desktop, Documents, and Pictures folders protected by syncing them to the cloud with OneDrive. If you’re rolling out Known Folder Move for your organization, the **Known folders** card is a great way for you to monitor progress.                                   |
| Sync app version         | *Shows the number of devices running on the current version of OneDrive.* <br><br>  Running the current version of OneDrive helps users stay up to date with all the latest and greatest fixes and features from Microsoft. Hover over the **Sync app version** card for a filtered view of operating systems on the current version. Note: Mac App store devices are excluded from this section and will appear in the count as "devices excluded".                                                                                  |
||

### Devices

The **Devices** tab shows all users, their current health state, their known folders currently moved in OneDrive, their current app version and operating system version, a timestamp of the last time the app was fully up to date, and a timestamp of the last time the sync app reported health data to the dashboard. An icon and status in the **Errors** column indicate the state of each device.

This table provides a summary of the information found in each column of the **Devices** tab:

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

When someone in your organization reports a problem with syncing files to OneDrive, you can investigate quickly without having to ask for extra details of the error message via Microsoft Teams chat or Outlook email. Select a user to see more information on their device and sync status. This detailed view lets you see a user's essential OneDrive information including any errors they might be experiencing.

### Issues

The **Issues** tab shows you a list of OneDrive error messages found in the health report and the number of devices affected by them in your organization. Use this view to see if there are any common patterns between users and the errors present across your organization.

You can learn more about the error and devices affected by selecting an error message from the list. The **Issues** panel will appear with a summary of the devices affected, along with a list of users and their current app version and operating system. Partner with your users to fix common OneDrive sync issues.

To learn more about OneDrive error messages, see [What do the OneDrive error codes mean?](https://support.microsoft.com/office/what-do-the-onedrive-error-codes-mean-f7a68338-e540-4ebf-ad5d-56c5633acded).

## Data for the OneDrive sync health dashboard

The sync reports use health data that your OneDrive sync apps send to Microsoft. You have choices when it comes to the technology you use and the data you share. Use the EnableSyncAdminReports setting to manage which devices send data.

To learn more about the controls available to you, see [Overview of privacy controls for Microsoft 365 Apps](/deployoffice/privacy/overview-privacy-controls). To learn more about required service data, see [Required service data for Office](/deployoffice/privacy/required-diagnostic-data).

## Known limitations and considerations

This section describes known limitations and considerations in sync reporting.

**Limitations**

**Device Records:** By default, device records are kept in inventory for 30 days, after which they expire from the report.

**Folders in OneDrive:** Devices with folders in OneDrive will appear in reports as a device with 0-3 known folders. If a device has not enabled folders in OneDrive, it will appear in reports as a device that is **Not eligible** in the **Known Folders** section of the **Overview** tab. In the **Devices** tab, a hyphen ("-") will appear in the cell value of the **Known folders** table for devices that aren't applicable devices. This behavior is expected.

**Sync app version: Mac App Store edition** For devices using the Mac App Store edition of the sync app, the version installed on each device is displayed in the **Devices** tab. The dashboard doesn't currently track whether or not the Mac App Store edition is the latest version of the sync app available in the Mac App Store. If any devices use this edition, they'll be excluded from the **Sync app version** section of the **Overview** tab and the number of excluded devices is displayed. This is the expected result.

**Minimum time device is on for eligibility:** Devices need to be turned on for a minimum of five hours to be eligible for the report. Devices that are turned off frequently and not on for that amount of time might be missing from the dashboard, even if the group policy is set.

**Considerations:**

**Network Impact** *How is my network impacted when my organization enables Sync Reports?*

There is negligible impact to a network after enabling the sync reports setting on devices.

**Storage in the EU** *How is data stored in the EU geo?* 

Microsoft continues its commitment to meet and exceed the requirements of EU data protection laws. All data storage is EU Data Boundary compliant. 

**Microsoft Power BI** *Are there Power BI templates available?*

There are no Power BI templates available for sync reports.

## Troubleshooting

Use this section to troubleshoot if the OneDrive sync reports don't appear after three days.

> [!IMPORTANT]
> If you enable the EnableSyncAdminReports setting on devices that don't meet the [requirements](#requirements), it will have no effect. The app won't send reports.


Confirm that the EnableSyncAdminReports setting is applied to the device. Run Command Prompt as an administrator, and then run the following command:

   ```PowerShell
   reg.exe query HKLM\Software\Policies\Microsoft\OneDrive /v EnableSyncAdminReports
   ```

 The output should look like this:

:::image type="content" source="media/syncregkeyquery.png" alt-text="Screenshot of expected command prompt output.":::

If the EnableSyncAdminReports setting wasn't applied, go back and follow the steps under [Set up the OneDrive sync health dashboard](#set-up-the-onedrive-sync-health-dashboard).

If the setting was applied correctly, wait for 36 hours with the device turned on and signed in to OneDrive. If the device still doesn't appear on the dashboard, open a support ticket with Microsoft. For more information, see the next section, [Report a problem](#report-a-problem).

## Report a problem

If you encounter a problem with viewing the report dashboard, first verify that you've completed the steps in the troubleshooting section.

If problems persist after troubleshooting, [open a support ticket with Microsoft](/microsoft-365/admin/contact-support-for-business-products). Make sure that the device isn't powered off during this period so that the sync app can still run and send a health report.

For quick investigations, be sure to have the date and time when the EnableSyncAdminReports setting was enabled and either the user’s email or the OneDrive device ID available in your issue report.

To get the OneDrive device ID, select the OneDrive sync app in the notification area > **Help & Settings** > **Settings** > **About**.

## Send feedback

We value your feedback. To submit feature suggestions and report issues, you can use the Feedback button in the top-right corner of the dashboard page.

:::image type="content" source="media/sync-feedback.png" alt-text="Screenshot of Feedback form.":::

