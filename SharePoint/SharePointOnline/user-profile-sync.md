---
title: "About user profile synchronization"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 5/21/2020
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 
description: "This article describes the user profile sync process for SharePoint in Microsoft 365, and the properties that are synced into user profiles."
---

# Overview

Microsoft SharePoint uses the Active Directory synchronization job to import user and group attribute information into the User Profile Application (UPA). When a new user is added to Azure Active Directory (Azure AD), the user account information is sent to the SharePoint directory store and the UPA sync process creates a profile in the User Profile Application based on a predetermined set of attributes. Once the profile has been created, any modifications to these attributes will be synced as part of regularly scheduled sync process.

> [!NOTE]
> The profile properties that are synced by the UPA sync process are not configurable. Synchronization times will vary based on workloads.

## Sync process

There are four steps in the sync process.

|Step|Description|
|:-------|:-------|
| 1. Azure on-premises to Azure AD | [Azure AD Connect](https://docs.microsoft.com/azure/active-directory/hybrid/how-to-connect-sync-whatis) syncs data from on-premises Active Directory to Azure AD. For more info, see [What is hybrid identity with Azure Active Directory?](https://docs.microsoft.com/azure/active-directory/hybrid/whatis-hybrid-identity) and [Attributes synchronized](https://docs.microsoft.com/azure/active-directory/hybrid/reference-connect-sync-attributes-synchronized#sharepoint-online).   |
| 2. Azure AD to SharePoint | Azure AD syncs data from Azure AD to the SharePoint directory store. |
| 3. SharePoint to UPA | The UPA sync process syncs user account information in SharePoint directory store to the User Profile Application (UPA). |
| 4. UPA to sites | User account information from the UPA is synced to SharePoint sites (previously called “site collections”). |

Typically, user profiles are created automatically for all accounts that are created in Microsoft 365. For organizations that have a Microsoft 365 Education subscription, user profiles are not created for new accounts by default. The user must access SharePoint once, at which time a basic stub profile will be created for the user account. The stub profile will be updated with all remaining data as part of the sync process.

If block sign-in is set on the user account in Azure AD or disabled accounts are synced from Active Directory on premises, those user accounts will not be processed as part of the UPA sync process. The user must be enabled and licensed for changes to be processed.

## Properties that are synced into SharePoint user profiles

The following Azure AD user attributes are synced to the UPA.

|Azure AD attribute|User profile property display names |Notes |Sync to sites|
|:-------|:-------|:-------|:-------|
|UserPrincipalName   | Account Name </br> User Name </br> User Principal Name | Example: </br> i:0#.f<|>membership<|>gherrera@contoso.com </br> gherrera@contoso.com | Yes |
|DisplayName |Name  | |Yes|
|GivenName |FirstName  | |Yes |
|sn  |LastName |  |Yes |
|telephoneNumber |Work phone |Example: (123) 456-7890 |Yes |
|proxyAddresses |Work Email </br> SIP Address |Work Email is set to the value prefixed with SMTP. (SMTP:gherrera@contoso.com) </br> Example: gherrera@contoso.com |Yes |
|PhysicalDeliveryOfficeName |Office | |Yes|
|Title |Title </br> Job Title |Job Title contains the same value as Title and is connected to a term set. |Yes |
|Department |Department |Department is connected to a term set. |Yes |
|WWWHomePage |Public site redirect | |No|
|PreferredLanguage |Language Preferences |Used by SharePoint to determine language for the user when the multilingual user interface (MUI) feature is enabled. |Yes |
|msExchHideFromAddressList |SPS-HideFromAddressLists | |No |
|Manager |Manager |User Manager for organization hierarchy |Yes |

> [!NOTE]
> To update additional or custom properties, see [Bulk update custom user profile properties](https://docs.microsoft.com/sharepoint/dev/solution-guidance/bulk-user-profile-update-api-for-sharepoint-online).

# Frequently asked questions (FAQs)

**How often are changes synced into the User Profile Application?**
</br>
User account attribute changes are collected in batches and processed for UPA synchronization. Times will vary based on the amount of changes requested in a single batch. The UPA synchronization is schedule to run at regular intervals.
</br></br>
**Will UPA synchronization overwrite existing properties in SharePoint user profiles?**
</br>
For the default properties that are synced by UPA synchronization, values will be overwritten to align with Azure AD.
</br></br>
**Does UPA synchronization update only properties that have changed?**
</br>
UPA synchronization is driven primarily by changes that are made Azure AD, including adding new users. A full import can occur under certain maintenance events.
</br></br>
**Why isn't it possible to map additional properties for UPA synchronization to sync from Azure AD to the User Profile Application?**
</br>
UPA synchronization is limited to a preconfigured set of properties to guarantee consistent performance across the service. 

