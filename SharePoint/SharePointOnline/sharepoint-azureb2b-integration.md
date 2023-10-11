---
ms.date: 06/11/2019
title: Microsoft Entra B2B integration for SharePoint & OneDrive
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
ms.localizationpriority: medium
search.appverid:
- MET150
ms.collection: M365-collaboration
ms.custom:
 - Adm_O365
 - seo-marvel-apr2020
description: In this article, you'll learn about the SharePoint and OneDrive integration with Microsoft Entra B2B.
---

# SharePoint and OneDrive integration with Microsoft Entra B2B 

This article describes how to enable Microsoft SharePoint and Microsoft OneDrive integration with Microsoft Entra B2B.

Microsoft Entra B2B provides authentication and management of guests. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account.

With SharePoint and OneDrive integration with Azure B2B Invitation Manager enabled, Azure B2B Invitation Manager can be used for sharing of files, folders, list items, document libraries and sites with people outside your organization. This feature provides an upgraded experience from the existing secure external sharing recipient experience. Additionally, Azure B2B Invitation Manager one-time passcode feature allows users who don't have existing Work or School accounts or Microsoft Accounts to not have to create accounts to authenticate, but can instead use the one time passcode to verify their identity.

Enabling this integration doesn't change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

Once the integration is enabled you and your users don't have to reshare or do any manual migration for guests previously shared with. Instead, when someone outside your organization clicks on a link that was created before Microsoft Entra B2B integration was enabled, SharePoint will automatically create a B2B guest account. This guest account is created for the user who originally created the sharing link. (If the user who created the link is no longer in the organization or no longer has permission to share, the guest won't be added to the directory and the file will need to be reshared.)

SharePoint and OneDrive integration with the Microsoft Entra B2B one-time passcode feature is enabled by default for new tenants.

Advantages of Microsoft Entra B2B include:
- Invited people outside your organization are each given an account in the directory and are subject to Microsoft Entra ID access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Microsoft Entra B2B and no longer require users to have or create a Microsoft account.
- If you've configured Google federation in Microsoft Entra ID, federated users can now access SharePoint and OneDrive resources that you've shared with them.
- SharePoint and OneDrive sharing is subject to the Microsoft Entra organizational relationships settings, such as **Members can invite** and **Guests can invite**. As with Microsoft 365 Groups and Teams, if a Microsoft Entra organizational relationship setting is more restrictive than a SharePoint or OneDrive setting, the Microsoft Entra setting will prevail.

> [!NOTE]
> Microsoft Entra B2B doesn’t support Microsoft accounts in Microsoft 365 operated by 21Vianet.

## Enabling the integration

 > [!NOTE]
 > When the integration is enabled, people outside the organization will be invited via the Azure B2B platform when sharing from SharePoint. They will sign in based on the [Microsoft Entra B2B redemption policy](/azure/active-directory/external-identities/redemption-experience#invitation-redemption-flow).
> When the integration isn't enabled, people outside the organization will continue to use their existing accounts created when previously invited to the tenant. Any sharing to new people outside the organizaton may result in either Microsoft Entra ID-backed accounts or SharePoint-only email auth guests that use a SharePoint One Time Passcode experience to sign in.

 >[!NOTE]
 > Review any custom [domain sharing restrictions in SharePoint and OneDrive](/sharepoint/restricted-domains-sharing) and decide if they should be moved to the [Microsoft Entra B2B Allow/Deny list](/azure/active-directory/external-identities/allow-deny-list). The Microsoft Entra ID Allow/Deny list also affects other Microsoft 365 services like Teams and Microsoft 365 Groups.

To enable SharePoint and OneDrive integration with Microsoft Entra B2B

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following cmdlets:

   ```PowerShell
   Set-SPOTenant -EnableAzureADB2BIntegration $true
   ```

## Disabling the integration

You can disable the integration by running '[Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant) -EnableAzureADB2BIntegration $false'. 

> [!Important]
> Once disabled, users who were shared to while the integration was enabled will always be a Microsoft Entra Guest User for future shares. To convert a user from a Microsoft Entra Guest User back to a SharePoint OTP user, you will need to [delete the guest](/sharepoint/remove-users#delete-a-guest-from-the-microsoft-365-admin-center) in Microsoft Entra ID and remove all SPUser objects in your organization that reference that guest user.  

## See also

[Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant)

[External sharing overview](./external-sharing-overview.md)
