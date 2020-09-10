---
title: "Manage the lock status for sites in SharePoint Online"
ms.reviewer: adwood
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
- MET150
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
description: "This article contains information on how to use the lock status of a site to control the actions allowed on a site collection."
---

# Manage the lock status for sites in SharePoint Online

The following table describes the locking options that are available in SharePoint Server.


|Option  |Description  |
|---------|---------|
|Unlock |Unlocks the site collection and makes it available to users.  |
|Read-only (blocks additions, updates, and deletions)    |Prevents users from adding, updating, or deleting content. A message will appear on the site stating that the site is under maintenance and it is read-only.   |
|No access    |Prevents users from accessing the site collection and its content. Users who attempt to access the site receive an error page that informs the user that the website declined to show the webpage.    |
|NoAcccessRedirectURL   |Traffic to sites that have a lock state NoAccess will be redirected to that URL. If parameter NoAccessRedirectUrl is not set, a 403 error will be returned.    |

> [!NOTE]
> It isn't possible to set the lock state on the root site collection.

## Manage the lock status for a site

Follow this procedure to set the lock state of a site by using the SharePoint Online Management shell.

**To manage the lock status for a site**

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. At the PowerShell command prompt, type the following command, and then press ENTER.
 
PowerShellCopy

 ```PowerShell
 Set-SPOSite -Identity "<SiteCollection>" -LockState "<State>"
 ```
Where:
- *SiteCollection* is the URL of the site collection that you want to lock or unlock.
- *State* is one of the following values:
  - **Unlock** to unlock the site collection and make it available to users.
  - **ReadOnly** to prevent users from adding, updating, or deleting content.
  - **NoAccess** to prevent users from accessing the site collection and its content. Users who attempt to access the site receive an error message.
  - **NoAccessRedirectURL** Traffic to sites that have a lock state NoAccess will be redirected to that URL. If parameter NoAccessRedirectUrl is not set, a 403 error will be returned.

For more information, see [Set-SPOSite](https://docs.microsoft.com/powershell/module/sharepoint-online/set-sposite).