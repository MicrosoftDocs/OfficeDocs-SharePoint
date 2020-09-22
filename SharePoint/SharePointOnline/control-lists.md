---
title: "Control Microsoft Lists"
ms.reviewer: hasaladi
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Control settings in the Lists app."
---

# Control settings for Microsoft Lists

As a global or SharePoint admin in Microsoft 365, you can control settings for Microsoft Lists. You can:

- Disable the creation of personal lists (prevent users from saving new lists to "My lists")
- Disable built-in list templates

You control both of these settings by using Microsoft PowerShell.

## Disable creation of personal lists

If you change this setting, when users create a list, they must select a SharePoint site for saving the list. The "Save to" setting doesn't include the "My lists" option. 
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -DisablePersonalListCreation $true​ 
    ```

To re-enable the creation of personal lists, set the parameter to `$false`.

## Disable built-in list templates

Disabling these templates removes them from all places users create lists (the Lists app, Microsoft Teams, and SharePoint sites).
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -DisableModernListTemplateIds 'c3a96423-13f5-4201-a83e-fbbbca5bd4e7'   ​
    ```

To re-enable a built-in template, use the parameter `EnableModernListTemplateIds`.
