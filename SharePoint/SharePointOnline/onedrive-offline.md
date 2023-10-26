---
ms.date: 10/25/2023
title: OneDrive webapp in offline mode
ms.reviewer:
ms.author: v-mathavale
author: v-mathavale
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
search.appverid:
- MET150
ms.collection:
- Strat_OD_admin
- M365-collaboration
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "Learn how to work with OneDrive web app when in offline mode."
---

# Work with OneDrive web app when offline

We know how important it is for you to access and work with your files on the web quickly and smoothly. That's why we built the next generation of OneDrive web app with performance as one of our main goals. We made sure that OneDrive delivers the best possible web experience for every user, regardless of their internet connection quality. In addition to that, you can now keep working with your files on OneDrive web app even when you are offline and have no internet access.

On Windows (Windows 10 and later) and macOS (macOS 12 Monterey or later) devices running the OneDrive sync app, you can now continue working with the OneDrive web app in your browser, OneDrive Progressive Web App (PWA), or Microsoft Teams even when you are offline or lose internet connection with the help of OneDrive offline mode. You can view, rename, move, copy all of your files, and create new folders. When your files are available for offline access, you can open them on your device in a native app directly from inside OneDrive web app. All the metadata changes you make offline to your files in the browser will be automatically synced back to OneDrive when your internet connection is restored.

To accomplish this, a copy of your file metadata that powers OneDrive web app is securely stored locally on your device. This data on your device is only available to you. If someone else were to sign in to your device, the local data on the device wouldn't be available to them. We adhere to privacy guidelines outlined in the [Microsoft Privacy Statement.](https://privacy.microsoft.com/privacystatement)

A secure local web server on your device handles the operations that you perform on your files, such as viewing, sorting, renaming, moving, and copying where traditionally these operations would need to be handled by the OneDrive cloud service. This results in fast and smooth interactions with your files like loading your files and folders, sorting, renaming, moving, renaming, and more. And all these operations continue to work even when you are offline, lose your internet connection, or run into a service disruption in the app.

To verify that OneDrive Offline mode is ready for you to use, follow the steps mentioned below:

> [!NOTE]
> Offline mode is per-device setting and needs to be configured on every device that you use to access OneDrive web app.

1. Open OneDrive for web.
2. In the upper right of the page, locate the ![](RackMultipart20231025-1-xzzjh5_html_1c15ffe384b3ad8a.png) icon that informs you that Offline mode is ready for you to use.

![](RackMultipart20231025-1-xzzjh5_html_f9be50f76b91403c.png)

When Offline mode is turned on, the changes you make are synced back to the cloud — either immediately (if you're online) or later when internet connection is restored (if you're offline at the time you make the changes).

## Resolve conflicting offline changes

When working offline, it's possible for a conflict to occur if two people change the same item at the same time in different ways. OneDrive tries to automatically resolve the conflict, but if it can't do that, it will notify you about the conflict so that you can resolve it in an appropriate way.

To resolve a conflict:

1. If a conflict exists, you will see a toast notification in OneDrive for web.

![](RackMultipart20231025-1-xzzjh5_html_17a4528e43435f8d.png)

2. Click the ![](RackMultipart20231025-1-xzzjh5_html_78a147a9a04bdbbe.png) icon on the toast to learn more about the reason for a conflict.

![](RackMultipart20231025-1-xzzjh5_html_3c15733871fe2370.png)

3. You resolve conflicts by dismissing them or by manually correcting them.

### Turn off Offline mode

> [!NOTE]
> Offline mode is per-device setting and needs to be configured on every device that you use to access OneDrive web app

1. To turn off Offline mode navigate to **My files** view.
2. Expand the info pane by clicking the **Info** button.

![](RackMultipart20231025-1-xzzjh5_html_d9c2ac16f528bc51.png)

3. Click **Turn off** to turn off Offline mode.
4. You will be presented with a confirmation dialog, at which point you can proceed with turning off offline mode or cancelling.

![](RackMultipart20231025-1-xzzjh5_html_f15993f71a5c3efd.png)

After you turn off Offline mode, next time you open OneDrive for web you will no longer see the Offline mode ![](RackMultipart20231025-1-xzzjh5_html_1c15ffe384b3ad8a.png) icon in the upper right of the page and when you're offline, you won't be able to access or edit your files from OneDrive.com or the Files app in Teams.

## Working with your OneDrive web app while offline

When you're working offline, you can still open and work with OneDrive for web. Features that aren't available while you're offline are grayed out to indicate that you can't use them at the moment, as illustrated below. When offline you will still be able to see, rename, move, and copy your files, as well as create new folders.

![](RackMultipart20231025-1-xzzjh5_html_5219a0c080d0351.png)

### Making files available offline

Offline file access and sync is fundamental to OneDrive and now you can leverage the power of OneDrive Files On-Demand in OneDrive web app. When you want files and folders available for offline access on your device, you can now select them to be always available locally directly from OneDrive web app. You can make files available offline on your device or even free up space by making offline files online-only. And you can do it directly from the OneDrive web app without having to navigate away to File Explorer or Finder to accomplish these tasks.

### Make file or folder available offline

1. Make sure you are syncing your OneDrive with OneDrive sync app.
2. Select the file or folder (you can select multiple) that you want to make available offline on your device.
3. Click "…" (select more actions for this item) and in the context menu that opens click ![](RackMultipart20231025-1-xzzjh5_html_5ec90527e71743c1.png)

![](RackMultipart20231025-1-xzzjh5_html_249bd5fa5fb817d1.png)

Alternatively, you can click ![](RackMultipart20231025-1-xzzjh5_html_5ec90527e71743c1.png) in the command bar.

![](RackMultipart20231025-1-xzzjh5_html_4c1f63d5c14d8328.png)

4. The file or folder will then be downloaded to your computer. Once completed, you will be notified with a toast that the file is available to you when you are offline. ![](RackMultipart20231025-1-xzzjh5_html_a32bb6f2904a5698.png)
5. You will see an "available offline" icon next to the files and folder that you marked to be available offline.

![](RackMultipart20231025-1-xzzjh5_html_b066ce9ec02093e8.png)

### Free up space on your device

You can also free up space on your computer by making offline files online-only. You will only be able to open these files when you are online, but you will still be able to rename, move, or copy these files when you are offline.

1. Select a file or folder (you can select multiple) that are marked as "available offline" that you no longer want to be available offline.
2. Click "…" (select more actions for this item) and in the context menu that opens select ![](RackMultipart20231025-1-xzzjh5_html_f844d6b6f657da6f.png) option.

![](RackMultipart20231025-1-xzzjh5_html_306e97844721ec1f.png)

 Alternatively, you can select ![](RackMultipart20231025-1-xzzjh5_html_69b891f49797edd1.png) in the command bar.

 ![](RackMultipart20231025-1-xzzjh5_html_cd9ff03c48b9eeca.png)

3. The file or folder will then be marked as online-only. Once completed, you will be notified with a toast that the file is no longer available to you when you are offline. ![](RackMultipart20231025-1-xzzjh5_html_4424faeb9da2879a.png)
4. You will no longer see "available offline" icon next to the file or folder that you chose not to be available offline on your computer.
 ![](RackMultipart20231025-1-xzzjh5_html_94646e52b157f85b.png)

> [!NOTE]
> - "Make available offline" action works across OneDrive for Web and OneDrive sync app on Windows and macOS.
> - You can make the file available offline in Windows File Explorer or macOS Finder and the file's offline availability state will be updated in OneDrive for Web as well.

 
### Current limitations of Offline mode

1. Offline mode is currently supported only on Windows (Windows 10 and later), macOS devices (macOS 12 Monterey or later), and Chromium-based browsers (Microsoft Edge, Google Chrome)
2. Currently, Offline mode is not supported in the following situations:
  - If you added a shortcut to shared folders in OneDrive
3. A _full_ offline experience in OneDrive for web — where you can perform all of the operations that are available online is not yet supported. The following features are not available when you are offline.
  - Sharing, copying links, downloading your files
  - Managing access to your files
  - Previewing your file in online previewer
  - Using **Search**
  - Creating and managing Power Automate flows
  - Copilot
  - Deleting files
  - Viewing file version history
  - Navigating to **Recycle bin**

### Bandwidth involved in using Offline mode

When compared to OneDrive sync app, bandwidth consumed by Offline mode is minimal, and largely depends on the size of your OneDrive and how frequently your OneDrive files are modified. When setting up Offline mode for the first time, a local copy of your file metadata will be downloaded and securely stored on your computer. The actual contents of your files will not be downloaded. After Offline mode is set up, only changes to your file metadata will result in upload or download activity over the network.

### Troubleshooting Offline mode issues

- For troubleshooting common Offline mode issues, check out Common issues when using Offline mode in OneDrive for Web