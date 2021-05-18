---
title: Azure AD B2B integration for SharePoint & OneDrive
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
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
description: In this article, you'll learn about the SharePoint and OneDrive integration with Azure AD B2B.
---

# SharePoint and OneDrive integration with Azure AD B2B 

This article describes how to enable Microsoft SharePoint and Microsoft OneDrive integration with Azure AD B2B.

Azure AD B2B provides authentication and management of guests. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account.

With SharePoint and OneDrive integration with Azure B2B Invitation Manager enabled, Azure B2B Invitation Manager can be used for sharing of files, folders, list items, document libraries and sites with people outside your organization. This feature provides an upgraded experience from the existing secure external sharing recipient experience. Additionally, Azure B2B Invitation Manager one-time passcode feature allows users who do not have existing Work or School accounts or Microsoft Accounts to not have to create accounts in order to authenticate, but can instead use the one time passcode to verify their identity.

Enabling this integration does not change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

Once the integration is enabled you and your users do not have to reshare or do any manual migration for guests previously shared with. Instead, when someone outside your organization clicks on a link that was created before Azure AD B2B integration was enabled, SharePoint will automatically create a B2B guest account. This guest account is created on behalf of the user who originally created the sharing link. (If the user who created the link is no longer in the organization or no longer has permission to share, the guest will not be added to the directory and the file will need to be reshared.)

SharePoint and OneDrive integration with the Azure AD B2B one-time passcode feature is currently not enabled by default. Later, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today.

Advantages of Azure AD B2B include:
- Invited people outside your organization are each given an account in the directory and are subject to Azure AD access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Azure AD B2B and no longer require users to have or create a Microsoft account.
- If you have configured Google federation in Azure AD, federated users can now access SharePoint and OneDrive resources that you have shared with them.
- SharePoint and OneDrive sharing is subject to the Azure AD organizational relationships settings, such as **Members can invite** and **Guests can invite**. As with Microsoft 365 Groups and Teams, if an Azure AD organizational relationship setting is more restrictive than a SharePoint or OneDrive setting, the Azure AD setting will prevail.

This integration is not supported in the following Microsoft 365 services:
- Office 365 Germany
- Office 365 operated by 21Vianet
- GCC High and DoD

## Enabling the integration

This integration requires that your organization also enable [Azure AD email one-time passcode authentication](/azure/active-directory/b2b/one-time-passcode).

 > [!NOTE]
 > When the integration is enabled, people outside the organization will be invited via the Azure B2B platform when sharing from SharePoint. If the Azure B2B One Time Passcode option is enabled, recipients that do not have password-backed accounts will get a sign-in experience through Azure AD that uses One Time Passcodes. Otherwise, they will authenticate via their own Azure AD account or via an MSA account.
> When the integration is not enabled, people outside the organizaton will continue to use their existing accounts created when previously invited to the tenant. Any sharing to new people outside the organizaton may result in either Azure AD-backed accounts or SharePoint-only email auth guests that use a SharePoint One Time Passcode experience to sign in.

To enable Azure AD passcode authentication
1. Sign in to the [Azure portal](https://portal.azure.com) as an Azure AD global admin.
2. In the nav pane, select **Azure Active Directory**.
3. Under **Manage**, click **External identities**.
4. Click **External collaboration settings**.
5. Under **Email one-time passcode for guests**, choose **Enable email one-time passcode for guests effective now**.
6. Select **Save**.

To enable SharePoint and OneDrive integration with Azure AD B2B
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." <br>On the Download Center page, select your language and then click the Download button. You'll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you're running the 64-bit version of Windows or the x86 file if you're running the 32-bit version. If you don't know, see [Which version of Windows operating system am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
3. Run the following cmdlets:
   ```PowerShell
   Set-SPOTenant -EnableAzureADB2BIntegration $true
   Set-SPOTenant -SyncAadB2BManagementPolicy $true
   ```

## Disabling the integration

You can disable the integration by running `Set-SPOTenant -EnableAzureADB2BIntegration $false`.
Content that was shared externally while the integration was enabled will need to be shared again with those people.

## See also

[Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant)

[External sharing overview](./external-sharing-overview.md)
