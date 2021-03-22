---
title: "Lock and unlock sites"
ms.author: kaarins
author: kaarins
manager: serdars
recommendations: true
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
description: "This article contains information about how to use the lock state of a site to control the actions allowed on the site."
---

# Lock and unlock sites

As a global or SharePoint admin in Microsoft 365, you can block access to a site or make a site read-only by using Microsoft PowerShell to change the lock state of the site. 

> [!NOTE]
> You can't set the lock state on the root site.

## Change the lock state for a site

Follow these steps to change the lock state for a site by using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. At the PowerShell command prompt, type the following command, and then press ENTER.

 ```PowerShell
 Set-SPOSite -Identity "<SiteURL>" -LockState "<State>"
 ```

Where:
*SiteURL* is the URL of the site that you want to lock or unlock and *State* is one of the following values:

- **Unlock** to unlock the site and make it available to users.
- **ReadOnly** to prevent users from adding, updating, or deleting content. A message will appear on the site stating that the site is under maintenance and is read-only.
- **NoAccess** to prevent users from accessing the site and its content. If you've provided a NoAccessRedirectUrl value for your organization (below), traffic will be redirected to the URL you specified. If you haven't set this URL, a 403 error will be displayed.

 ```PowerShell
Set-SPOTenant -NoAccessRedirectUrl 'https://www.contoso.com'
 ```

For more info about the LockState parameter, see [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite). For more info about the NoAccessRedirectUrl parameter, see [Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant).