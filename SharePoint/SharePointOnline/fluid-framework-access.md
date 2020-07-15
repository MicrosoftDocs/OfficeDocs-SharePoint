---
title: "Manage access to Fluid Framework"
ms.reviewer: kaarins
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ROBOTS: NOINDEX
search.appverid:
- SPO160
- MET150
- BSA160
ms.assetid: 
description: "Learn how to enable or disable Microsoft Fluid Framework preview for your organization."
---

# Manage access to Fluid Framework

Microsoft Fluid Framework preview improves team collaboration by helping users create files where they can add components such as action items and check lists. [Learn how to get started with Fluid](https://support.microsoft.com/office/d05278db-b82b-4d1f-8523-cf0c9c2fb2df). As a global or SharePoint admin in Microsoft 365, you can manage access to Fluid Framework preview in your organization.

> [!NOTE]
> This preview is rolling out. Some features are available only to organizations that have selected the [Targeted release option](/microsoft-365/admin/manage/release-options-in-office-365). You might not yet see this feature or it might look different than what is described.

### Disable Fluid Framework using PowerShell

Fluid Framework preview is enabled by default. Follow these steps to disable it for your organization.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."
    >
    > On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command.

   ```powershell
   Set-SPOTenant -IsFluidEnabled $false
   ```

   This change takes about 60 minutes to take effect across your organization.

To re-enable Fluid Framework, run the following command.

```powershell
Set-SPOTenant -IsFluidEnabled $true
```

This change takes about 60 minutes to take effect across your organization.

