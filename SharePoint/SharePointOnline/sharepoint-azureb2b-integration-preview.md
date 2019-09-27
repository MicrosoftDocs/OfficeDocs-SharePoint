---
title: "SharePoint and OneDrive integration with Azure AD B2B (Preview)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.custom: Adm_O365
ms.collection: M365-collaboration
description: "Learn about the SharePoint and OneDrive integration with Azure AD B2B (preview)."
---

# SharePoint and OneDrive integration with Azure AD B2B (Preview)

This article describes how to enable SharePoint and OneDrive integration with Azure AD B2B.

Azure AD B2B provides authentication and management of guest users. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account (MSA).

With SharePoint and OneDrive integration, the Azure B2B one-time passcode feature is used for external sharing of files, folders, list items, document libraries and sites. This feature provides an upgraded experience from the existing [secure external sharing recipient experience](what-s-new-in-sharing-in-targeted-release.md). 

Enabling the preview does not change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

SharePoint and OneDrive integration with the Azure AD B2B one-time passcode feature is currently in preview. After preview, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today for all tenants.

Advantages of Azure AD B2B include:
- Invited external users are each given an account in the directory and are subject to Azure AD access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Azure AD B2B and no longer require users to have or create a Microsoft account.
- If you have configured Google federation in Azure AD, federated users can now access SharePoint and OneDrive resources that you have shared with them.
- SharePoint and OneDrive sharing is subject to the Azure AD organizational relationships settings, such as **Members can invite** and **Guests can invite**.

This preview is not supported in the following Office 365 services:
- Office 365 Germany
- Office 365 operated by 21Vianet
- GCC High and DoD

## Opting in to the preview

This preview requires that your organization also be opted into the [Azure AD email one-time passcode authentication preview](https://docs.microsoft.com/azure/active-directory/b2b/one-time-passcode).

To opt in to the Azure AD passcode authentication preview
1. Sign in to the [Azure portal](https://portal.azure.com) as an Azure AD global administrator.
2. In the navigation pane, select **Azure Active Directory**.
3. Under **Manage**, select **Organizational Relationships**.
4. Select **Settings**.
5. Under **Enable Email One-Time Passcode for guests (Preview)**, select **Yes**.
6. Click **Save**.

To opt in to the SharePoint and OneDrive integration with Azure AD B2B
1. Install the latest version of the [SharePoint Online Services Module for Windows PowerShell](https://www.powershellgallery.com/packages/Microsoft.Online.SharePoint.PowerShell) (minimum version 8924.1200).
2. Connect to your tenant by using [Connect-SPOService](https://docs.microsoft.com/en-us/powershell/module/sharepoint-online/connect-sposervice).
3. Run the following cmdlets:
   ```PowerShell
   Set-SPOTenant -EnableAzureADB2BIntegration $true
   Set-SPOTenant -SyncAadB2BManagementPolicy $true
   ```

## Opting out of the preview

You can disable the preview by running `Set-SPOTenant -EnableAzureADB2BIntegration $false`. (You can also [opt out of the Azure AD passcode authentication preview](https://docs.microsoft.com/en-us/azure/active-directory/b2b/one-time-passcode#opting-out-of-the-preview-after-opting-in).)
Content that was shared externally while the preview was enabled will need to be shared again with the specific external users.

Note that after preview, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today for all tenants and you will not be able to opt out.

## Feedback

We're interested in your feedback about this preview. Please fill out the [Feedback on SharePoint integration with Azure AD B2B Preview](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR2JklDeWHptFqoV2KEW0bYxUQTMxTzYxV1NST0VQSEFLSUY4NVZIVlk0OC4u) survey.

## See also

[Set-SPOTenant](https://docs.microsoft.com/en-us/powershell/module/sharepoint-online/set-spotenant)

[External sharing overview](https://docs.microsoft.com/sharepoint/external-sharing-overview)
