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
description: "Learn how you can work with OneDrive web app in offline mode."
---

# Work with OneDrive web app when offline

We know how important it is for you to access and work with your files on the web quickly and smoothly. That's why we built the next generation of OneDrive web app with performance as one of our main goals. We made sure that OneDrive delivers the best possible web experience for every user, regardless of the internet connection quality. In addition to that, you can now keep working with your files on OneDrive web app even when you're offline and have no internet access.

On Windows 10 or later and macOS 12 Monterey or later for devices running the OneDrive sync app, you can now continue working with the OneDrive web app in your browser, OneDrive Progressive Web App (PWA), or Microsoft Teams even when you're offline or lose internet connection with the help of OneDrive offline mode. You can view, rename, move, copy all of your files, and create new folders. When your files are available for offline access, you can open them on your device in a native app directly from inside OneDrive web app. All the metadata changes you make offline to your files in the browser are automatically synced back to OneDrive when your internet connection is restored.

To accomplish this, a copy of your file metadata that powers OneDrive web app is securely stored locally on your device. This data on your device is only available to you. If someone else was to sign in to your device, the local data on the device wouldn't be available to them. We adhere to privacy guidelines outlined in the [Microsoft Privacy Statement.](https://privacy.microsoft.com/privacystatement)

A secure local web server on your device handles the operations that you perform on your files, such as viewing, sorting, renaming, moving, and copying. Traditionally, these operations would need to be handled by the OneDrive cloud service. This results in fast and smooth interactions with your files like loading your files and folders, sorting, renaming, moving, and more. And all these operations continue to work even when you're offline, lose your internet connection, or run into a service disruption in the app.

## Verify that OneDrive Offline mode is ready for use

> [!NOTE]
> Offline mode is per-device setting and needs to be configured on every device that you use to access OneDrive web app.

1. Open **OneDrive** for web.

1. In the upper right of the page, locate the :::image type="icon" source="media/onedrive-offline/onedrive-offline1.png" border="false"::: that informs you that Offline mode is ready for you to use.
:::image type="content" source="media/onedrive-offline/onedrive-offline2.png" alt-text="Screenshot of OneDrive offline mode ready.":::

When Offline mode is turned on, the changes you make are synced back to the cloud—either immediately (if you're online) or later when internet connection is restored (if you're offline at the time you make the changes).

## Resolve conflicting offline changes

When working offline, it's possible for a conflict to occur if two people change the same item at the same time in different ways. OneDrive tries to resolve the conflict automatically. But if it can't do that, it notifies you about the conflict so that you can resolve it in an appropriate way.

To resolve a conflict:

1. If a conflict exists, you'll see a toast notification in OneDrive for web.

    :::image type="content" source="media/onedrive-offline/onedrive-offline3.png" alt-text="Screenshot of notification to resolve conflict.":::

2. Select the :::image type="icon" source="media/onedrive-offline/onedrive-offline4b.png" border="false":::  icon on the toast to learn more about the reason for a conflict.

    :::image type="content" source="media/onedrive-offline/onedrive-offline5.png" alt-text="Screenshot of reason for the conflict.":::

3. You resolve conflicts by dismissing them or by manually correcting them.

### Turn off Offline mode

> [!NOTE]
> Offline mode is per-device setting and needs to be configured on every device that you use to access OneDrive web app.

1. To turn off Offline mode, navigate to **My files** view.

1. Expand the info pane by clicking the **Info** button.
    :::image type="content" source="media/onedrive-offline/onedrive-offline6.png" alt-text="Screenshot of My files view.":::

3. Select **Turn off** to turn off Offline mode.

1. In the confirmation dialog that appears, you can proceed with turning off offline mode or canceling.
    :::image type="content" source="media/onedrive-offline/onedrive-offline7.png" alt-text="Screenshot of confirmation dialog.":::

After you turn off Offline mode, next time you open OneDrive for web, you'll no longer see the Offline mode :::image type="icon" source="media/onedrive-offline/onedrive-offline1.png" border="false"::: icon in the upper right of the page and when you're offline, you won't be able to access or edit your files from OneDrive.com or the Files app in Teams.

## Work with OneDrive web app while offline

When you're working offline, you can still open and work with OneDrive for web. Features that aren't available while you're offline are grayed out to indicate that you can't use them at the moment, as illustrated below. When offline, you'll still be able to see, rename, move, copy your files, and create new folders.
:::image type="content" source="media/onedrive-offline/onedrive-offline8.png" alt-text="Screenshot of command bar.":::


### Make files available offline

Offline file access and sync are fundamental to OneDrive and now you can leverage the power of OneDrive files on-demand in OneDrive web app. When you want files and folders available for offline access on your device, you can select them to be always available locally directly from OneDrive web app. You can make files available offline on your device or even free up space by making offline files online-only. And you can do it directly from the OneDrive web app without having to navigate away to File Explorer or Finder to accomplish these tasks.

To make file or folder available offline:

1. Make sure you're syncing your OneDrive with OneDrive sync app.
2. Select the file or folder (you can select multiple) that you want to make available offline on your device.
3. Select "…" (select more actions for this item) and in the context menu that opens select :::image type="icon" source="media/onedrive-offline/icon-3b.png" border="false":::

    :::image type="content" source="media/onedrive-offline/onedrive-offline10.png" alt-text="Screenshot of making file available offline.":::

Alternatively, you can select :::image type="icon" source="media/onedrive-offline/icon-3b.png" border="false":::  in the command bar.

:::image type="content" source="media/onedrive-offline/onedrive-offline11.png" alt-text="Screenshot of command bar to make file offline." lightbox="media/onedrive-offline/onedrive-offline11.png":::


4. The file or folder is then downloaded to your computer. Once completed, you'll be notified with a toast that the file is available to you when you're offline. 
:::image type="content" source="media/onedrive-offline/onedrive-offline12.png" alt-text="Screenshot of file available when offline.":::
1. You'll see an "available offline" icon next to the files and folder that you marked to be available offline.

    :::image type="content" source="media/onedrive-offline/onedrive-offline-13b.png" alt-text="Screenshot of available offline icon.":::

### Free up space on your device

You can also free up space on your computer by making offline files online-only. You'll only be able to open these files when you're online, but you'll still be able to rename, move, or copy these files when you're offline.

1. Select a file or folder (you can select multiple) that are marked as "available offline" that you no longer want to be available offline.

1. Select "…" (select more actions for this item) and in the context menu that opens select :::image type="icon" source="media/onedrive-offline/icon-4b.png" border="false"::: option.

:::image type="content" source="media/onedrive-offline/onedrive-offline-15.png" alt-text="Screenshot of making file online.":::

 Alternatively, you can select :::image type="icon" source="media/onedrive-offline/icon5b.png" border="false"::: in the command bar.

:::image type="content" source="media/onedrive-offline/onedrive-offline-17.png" alt-text="Screenshot of make available online." lightbox="media/onedrive-offline/onedrive-offline-17.png":::

3. The file or folder is marked as online-only. Once completed, you'll be notified with a toast that the file is no longer available to you when you're offline. 
:::image type="content" source="media/onedrive-offline/onedrive-offline-18.png" alt-text="Screenshot of toast that file is not available online.":::

1. You'll no longer see "available offline" icon next to the file or folder that you chose not to be available offline on your computer.

    :::image type="content" source="media/onedrive-offline/onedrive-offline-19b.png" alt-text="Screenshot of file not available offline.":::
 
    > [!NOTE]
    > - "Make available offline" action works across OneDrive for Web and OneDrive sync app on Windows and macOS.
    > - You can make the file available offline in Windows File Explorer or macOS Finder and the file's offline availability state will be updated in OneDrive for Web as well.

### Current limitations of Offline mode

1. Offline mode is currently supported only on Windows (Windows 10 and later), macOS devices (macOS 12 Monterey or later), and Chromium-based browsers (Microsoft Edge, Google Chrome)
2. Currently, Offline mode isn't supported in the following situations:
      - If you added a shortcut to shared folders in OneDrive
3. A _full_ offline experience in OneDrive for web—where you can perform all the operations that are available online isn't yet supported. The following features aren't available when you're offline.
      - Sharing, copying links, adding new files, downloading your files
      - Managing access to your files
      - Previewing your file in online previewer
      - Using **Search**
      - Creating and managing Power Automate flows
      - Copilot
      - Deleting files
      - Viewing file version history
      - Navigating to **Recycle bin**

### Bandwidth involved in using Offline mode

When compared to OneDrive sync app, bandwidth consumed by Offline mode is minimal, and largely depends on the size of your OneDrive and how frequently your OneDrive files are modified. When setting up Offline mode for the first time, a local copy of your file metadata is downloaded and securely stored on your computer. The actual contents of your files won't be downloaded. After Offline mode is set up, only changes to your file metadata will result in upload or download activity over the network.

### Troubleshooting Offline mode issues

- For troubleshooting common Offline mode issues, check out Common issues when using Offline mode in OneDrive for Web.