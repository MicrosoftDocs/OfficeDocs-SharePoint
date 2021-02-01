---
title: Azure AD B2B integration for SharePoint & OneDrive
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
search.appverid:
- MET150
ms.collection: M365-collaboration
ms.custom:
 - Adm_O365
 - seo-marvel-apr2020
description: In this article, you'll learn about the SharePoint and OneDrive integration with Azure AD B2B (preview).
---

# SharePoint and OneDrive integration with Azure AD B2B 

This article describes how to enable Microsoft SharePoint and Microsoft OneDrive integration with Azure AD B2B.

Azure AD B2B provides authentication and management of guests. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account.

With SharePoint and OneDrive integration, the Azure B2B one-time passcode feature is used for external sharing of files, folders, list items, document libraries and sites. This feature provides an upgraded experience from the existing [secure external sharing recipient experience](what-s-new-in-sharing-in-targeted-release.md). 

Enabling this integration does not change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

Once the integration is enabled you and your users do not have to reshare or do any manual migration for guests previously shared with. Instead, when someone outside your organization clicks on a link that was created before the preview was enabled, SharePoint will automatically create a B2B guest account. This guest account is created on behalf of the user who originally created the sharing link. (If the user who created the link is no longer in the organization or no longer has permission to share, the guest will not be added to the directory and the file will need to be reshared.)

SharePoint and OneDrive integration with the Azure AD B2B one-time passcode feature is currently not enabled by default. Later, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today.

Advantages of Azure AD B2B include:
- Invited people outside your organization are each given an account in the directory and are subject to Azure AD access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Azure AD B2B and no longer require users to have or create a Microsoft account.
- If you have configured Google federation in Azure AD, federated users can now access SharePoint and OneDrive resources that you have shared with them.
- SharePoint and OneDrive sharing is subject to the Azure AD organizational relationships settings, such as **Members can invite** and **Guests can invite**.

This integration is not supported in the following Microsoft 365 services:
- Office 365 Germany
- Office 365 operated by 21Vianet
- GCC High and DoD

## Enabling the integration

To enable SharePoint and OneDrive integration with Azure AD B2B
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
3. Run the following cmdlets:
   ```PowerShell
   Set-SPOTenant -EnableAzureADB2BIntegration $true
   Set-SPOTenant -SyncAadB2BManagementPolicy $true
   ```

## Disabling the integration

You can disable the integration by running `Set-SPOTenant -EnableAzureADB2BIntegration $false`.
Content that was shared externally while the integration was enabled will need to be shared again with those people.

## See also

[Set-SPOTenant](https://docs.microsoft.com/powershell/module/sharepoint-online/set-spotenant)

[External sharing overview](https://docs.microsoft.com/sharepoint/external-sharing-overview)
