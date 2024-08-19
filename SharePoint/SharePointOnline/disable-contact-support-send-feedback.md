---
ms.date: 4/12/2024
title: "Prevent users from contacting Microsoft directly"
ms.reviewer: pramod.balasu
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.custom: onedrive-toc
ms.collection: M365-collaboration
ms.localizationpriority: medium
description: "This article describes how SharePoint Administrators in Microsoft 365 can disable the 'Contact support' and 'Send feedback' features in the OneDrive sync app."
---

# Prevent users from contacting Microsoft directly

> [!NOTE]
>
> - The ability of OneDrive users to contact Microsoft directly in the form of support requests will be disabled before end of calendar year 2022. </br>
    Only an administrator will be able to open a support request with Microsoft.</br>
> - Users can still send feedback as usual on the OneDrive app on Windows, Mac, iOS, and Android devices. </br>
> - For **Windows and Mac**: 'Contact support' will be disabled in future updates and for existing or old versions it will not work to create a service request. </br>
> - For **Android**: 'Report a Problem' will create a feedback item instead of a service request.</br>
> - For **iOS**: 'Ask for help' will be disabled in future updates and for existing or old versions it will not work to create a service request. 'Report a Problem' will create a feedback item instead of a service request.

The OneDrive sync app (OneDrive.exe) allows users to contact Microsoft directly from within the app. Users can:

- Create a support ticket by selecting **Get help** and then selecting the **Contact support** link in the help pane.
- Send positive or negative feedback directly to Microsoft by selecting **Send feedback**.

![The Get help and Send feedback commands](media/Img1-4717638.png)

As a SharePoint Administrator, you can disable these support features to prevent people in your organization from contacting Microsoft directly.

If you disable these features, users can still select Get help to view help articles, but the Contact support link will no longer appear.

The following screenshots show the changes after you disable the support features.

![The Get help and Feedback commands](media/Img2-4717638.png)

![The help pane](media/Img3-4717638.png)

> [!NOTE]
> If you disable "Contact support" and "Send feedback" but allow users to sync personal accounts, they can still contact support and send feedback directly to Microsoft from the OneDrive sync app when they're signed in with their personal account.

## Disable "Contact support" and "Send feedback" in Windows

To disable these features in Windows, you can:

- Use the [Set-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/set-spotenantsyncclientrestriction) in Microsoft PowerShell
- Edit the registry

### Use PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

      ```PowerShell
      Set-SPOTenantSyncClientRestriction -DisableReportProblemDialog $true
      ```

### Edit the registry

Follow these steps to disable the features on a PC by editing the registry.

> [!IMPORTANT]
> Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, [back up the registry for restoration](https://support.microsoft.com/help/322756/how-to-back-up-and-restore-the-registry-in-windows) in case problems occur.

1. In Registry Editor, locate the following subkey: **HKEY_CURRENT_USER\Software\Microsoft\OneDrive**

2. Right-click **OneDrive**, select **New**, and then select **DWORD (32-bit) Value**.

3. Enter **DisableReportProblemDialog** for the name.

4. Right-click the new registry key, enter **1** for **Value data**, and then select **OK**.

## Disable "Contact support" and "Send feedback" on Mac

To disable the features in the OneDrive sync app for Mac, add a preference to defaults.

For the standalone Mac sync app:
**defaults write com.microsoft.OneDrive DisableReportProblemDialog 1**

For the Mac sync app installed through the Mac App Store:

**defaults write com.microsoft.OneDrive-mac DisableReportProblemDialog 1**
