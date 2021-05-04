---
title: "Overview of OneDrive Sync admin reports in the Microsoft 365 Apps admin center"
ms.reviewer: cheyang
ms.author: adjoseph
author: adeejoseph
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
description: Learn how to use OneDrive Sync admin reports to get insights and take action on sync client adoption and health.
---

# Overview of OneDrive Sync admin reports in the Microsoft 365 Apps Admin center

>[!IMPORTANT]
> This is pre-release documentation for a preview program that isn't available to everyone and is subject to change. This pre-released feature will be gradually rolling out to customers on the Insider and Production rings on 05/04/2021 and the roll out will be completed by the end of 06/04/2021.

This article is for IT admins managing the OneDrive sync app.

OneDrive Sync admin reports provide you with unified actionable insights to simplify the IT workflow. From small businesses to large enterprises, OneDrive Sync admin reports will be the single place to get insights and take action on both sync client adoption and health.

From their dashboard, admins can check the sync status and client version of individual devices, monitor Known Folder Move roll out, and track sync errors. The insights range from a high-level executive summary to a drill-down of sync status per-device, to be used in a variety of administrative scenarios.

**Requirements**:  
- This feature is available for OneDrive Sync clients on Insiders or Production Update Rings only. Deferred Ring devices are not eligible for the preview.

- Deploy the OneDrive Sync client version 21.078 or newer (Windows only, Mac support underway).

- Ensure that your organization’s IT admin has the appropriate administrative access – Global administrator role, Office Apps administrator role, or Global reader role.

- Verify with your network team that client devices can reach the following endpoint: 
[https://clients.config.office.net](https://clients.config.office.net)

## Set up the OneDrive Sync admin reports dashboard

Before you can begin to set up the dashboard, ensure that appropriate administrative access is in place.

1. **Get access to the [Microsoft 365 Apps Admin Center](https://config.office.com/).**
    * To complete Step 2 below, you must have the [Global Administrator role](/microsoft-365/admin/add-users/about-admin-roles?WT.mc_id=365AdminCSH&view=o365-worldwide) or [Office Apps Administrator role](/microsoft-365/admin/add-users/about-admin-roles?WT.mc_id=365AdminCSH&view=o365-worldwide) (either one of the two).

    * Once you've completed the step below, you can view the report with [Global Reader role](/microsoft-365/admin/add-users/about-admin-roles?WT.mc_id=365AdminCSH&view=o365-worldwide).

    To learn more about Microsoft 365 admin roles, see [here](/microsoft-365/admin/add-users/about-admin-roles?WT.mc_id=365AdminCSH&view=o365-worldwide).

2. **Onboard Sync clients in your organization**

    1. Confirm Sync client build is on supported versions
    
       Supported Sync client versions are:

       * Windows, build number 21.078 or newer.
       * Mac is currently not supported.

    2. Obtain a **Tenant Association Key** from the [Microsoft 365 Apps Admin Center](https://config.office.com/).

        1. From your web browser, go to https://config.office.com and sign in with an Office 365 account using either *Global Admin or Office Apps admin privileges.*

        1. From the left navigation, under **“Health,”** click on **OneDrive Sync** tab, you will see a “PREVIEW” tag associated with the tab

           :::image type="content" source="media/preview-button.png" alt-text="Image of OneDrive Sync Preview Tab in Microsoft 365 Apps Admin Center":::

        1. Select the **“Enable preview features”** button to accept the End User Licensing Agreement. 
        
           :::image type="content" source="media/enable-preview.png" alt-text="Image of enable preview features button":::
        
           :::image type="content" source="media/license-terms.png" alt-text="Image of licensing terms in admin center":::

           Once accepted, you will see this visual on your screen:

           :::image type="content" source="media/sync-home.png" alt-text="Image of OneDrive Sync Admin dashboard":::

        1. After you have seen the visual above, navigate to **Settings** page. Here you will see the **Tenant Association Key.**
          
           If the key field is empty, you will need to create a new key by selecting “Generate new key”.

           Next, copy this key for the following step.

           :::image type="content" source="media/tenant-key-image.png" alt-text="Image of tenant association key generator":::

           > [!NOTE] 
           > It can take up to 30 seconds for the Tenant Association Key to show up on the screen when generated for the first time.

    3. **Enable OneDrive SyncAdminReports GPO using the Tenant Association Key.**

       > [!IMPORTANT]
       > -  You must enable this GPO on the sync clients you want to get reports from, the GPO has no impact on the end user.
       > -	When a new Tenant Association Key is generated, update the registry setting as well.
       > -	We recommend a gradual rollout starting with a few test devices per day, then onto within 100 devices per day, then gradually ramp up to no more than 10,000 devices per day until you finish.
      
       There are multiple options for deploying for Windows platform.

       1. **Enable group policy via registry.** 
        
          Navigate to HKLM\SOFTWARE\Policies\Microsoft\OneDrive

          a. Right click > New > String Value.

          b. Name: SyncAdminReports
            
          c. Type: REG_SZ

          d. Data: Paste your Tenant Association Key here.

             :::image type="content" source="media/registry-editor.png" alt-text="Image of  the Registry Key setting":::

        2. **Enable via Command Line** (running in Administrator Mode):
        
            reg.exe add HKLM\Software\Policies\Microsoft\OneDrive /v SyncAdminReports /t REG_SZ /d **"Paste your Tenant Association Key here"** /f

        3. **The SyncAdminReports GPO is available in the OneDrive administrative template files (ADMX/ADML).** The instructions below apply to an individual machine, but the template can applied more broadly via Intune. For more information on deploying broadly,  see [Use OneDrive policies to control sync settings](use-group-policy.md).

            a. Open Group Policy Editor (gpedit.exe).

            b. Navigate to Computer Configuration\Policies\Administrative Templates\OneDrive

            c. Select “Sync Admin Reports”, either double-clicking or selecting “Edit policy setting”

            d. Select “Enable” and paste your Tenant Association Key in the respective text field in the Options menu. Press OK.

       > [!IMPORTANT]
       > It takes up to 3 days from when the GPO has been enabled on the devices to see the reports, and that is expected.

## Troubleshooting steps

This section will help you troubleshoot if the OneDrive sync admin reports do not appear after 3 days.

**The sync client must be (1) running build 21.078.0412.0001 or newer and (2) in the Insiders or Production Update Ring (not Enterprise/Deferred). Enabling the GPO on ineligible devices will not have any effect – these clients will not upload health reports.**

Use the script below to confirm that:

1.	The sync client is on Production or Insider Ring. 

2.	The SyncAdminReports GPO has been applied to the device

    In Command Prompt (running in Administrator mode), run the following commands:

    - Check to confirm the sync client is on Production or Insider ring:

      `reg.exe query HKLM\Software\Policies\Microsoft\OneDrive /v GPOSetUpdateRing`

      If the output from the script **is not** dword:00000000, then your device is on Production or Insider ring.

    - Check to confirm the sync client has SyncAdminReports GPO enabled:

      `reg.exe query HKLM\Software\Policies\Microsoft\OneDrive /v SyncAdminReports`

      The output should look like this:

      :::image type="content" source="media/command-prompt.png" alt-text="Image of command prompt output":::

If the GPO was not applied, complete step C (Enable OneDrive SyncAdminReports GPO using the Tenant Association Key) [above](#set-up-the-onedrive-sync-admin-reports-dashboard) again.

If the Sync client is not on Production or Insider ring, opt into those rings using the steps in [Use OneDrive policies to control sync settings](use-group-policy.md#set-the-sync-app-update-ring).

If the GPO was applied correctly and device is on Production or Insiders ring, wait for 24 hours with the device on and signed-into OneDrive. Then, if the device is still not on the dashboard, open a support ticket with Microsoft. For more information, visit the section [**Report issues**](#report-issues) below.

## OneDrive Sync admin report dashboard 

> [!NOTE]
> Once you reach this step, the Global Reader admin role is sufficient to access and view the report.

The Overview page provides aggregated insights on devices that have sync errors, [Known Folder Move](redirect-known-folders.md) rollout status, and adoption of Sync client versions and update ring.

:::image type="content" source="media/sync-dashboard.png" alt-text="Image of Sync admin reports dashboard":::

The Details page provides aggregated insights to help admins understand and trouble shoot Sync errors.

It reports on the following diagnostic data:
-	User: The name of the user
-	User email: The email address of the user
-	Computer name: The name of the device
-	Errors: Details including the counts, and error messages end users are seeing
-	Known folders: Details including enabled status for each folder (Desktop, Documents, Pictures)
-	OneDrive app version: The currently installed OneDrive version 
-	Operating system version: The current version of the OS running on the device
-	Last synced timestamp (UTC): The last time Sync client was fully up to date with the cloud
-	Last status reported timestamp (UTC): The last time Sync client reported its diagnostic data to the dashboard. 

:::image type="content" source="media/sync-health-ui.png" alt-text="Image of Sync admin health reports details pane":::

### Data for the OneDrive sync health dashboard

The Sync admin reports uses the required service data and diagnostic data that your OneDrive clients send to Microsoft. You are in control of which data and which devices send this data. Control over the devices that send this data can be achieved using the GPO options listed above.

Diagnostic data is always under your control.  To learn more about diagnostic data and the controls available to you, see [Overview of privacy controls for Microsoft 365 Apps](/deployoffice/privacy/overview-privacy-controls). To learn more about required service data, see [Required diagnostic data for Office](/deployoffice/privacy/required-diagnostic-data).

## Report issues

If you are encountering an issue with viewing the report dashboard, first verify that you've completed the troubleshooting steps above.

If issues persist after troubleshooting, please [open a support ticket with Microsoft](/microsoft-365/admin/contact-support-for-business-products?view=o365-worldwide&tabs=phone). Ensure that the device is not powered off during this period so that the sync client can still run and upload a health report.

For quick investigations, be sure to have the date and time range in which the GPO was applied and either the user’s email or the OneDriveDeviceId available in your issue report.

To obtain OneDrive DeviceID, go to OneDrive app in the notification area > **Help & Settings** > **Settings** > **About**.


## Provide Feedback

If you'd like to make a feature suggestion, please use the Feedback button on the bottom right of the dashboard page to submit suggestions.

:::image type="content" source="media/sync-feedback.png" alt-text="Image of sync admin dashboard feedback submission box.":::
