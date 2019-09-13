---
title: Sharing and permissions in the SharePoint modern experience
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
localization_priority: Priority
description: "Learn about sharing and permissions in the SharePoint modern experience"
---

# Sharing and permissions in the SharePoint modern experience



## Hub site permissions

Hub site owner defines the shared experiences for hub navigation and theme. Hub site members create content on the hub site as with any other SharePoint site. Owners and members of the sites associated with the parent hub create content on individual sites.

admin must specify users who can add sites to hub

connected site perms are managed separately

perms to hub site depend on whether group-connected or not



## Communication site permissions

## Team site permissions and Office 365 Groups

## Sharable links

## Using team sites with Teams

## Guest sharing

## Managing permissions with security groups

## SharePoint and OneDrive integration with Azure AD B2B (Preview)


Azure AD B2B provides authentication and management of guest users. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account (MSA).

With SharePoint and OneDrive integration, the Azure B2B one-time passcode feature is used for external sharing of files, folders, list items, document libraries and sites. This feature provides an upgraded experience from the existing [secure external sharing recipient experience](https://docs.microsoft.com/sharepoint/what-s-new-in-sharing-in-targeted-release). 

Enabling the preview does not change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

SharePoint and OneDrive integration with the Azure AD B2B one-time passcode feature is currently in preview. After preview, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today for all tenants.

Advantages of Azure AD B2B include:
- Invited external users are each given an account in the directory and are subject to Azure AD access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Azure AD B2B and no longer require users to have or create a Microsoft account.
- If you have configured Google federation in Azure AD, federated users can now access SharePoint and OneDrive resources that you have shared with them.
- SharePoint and OneDrive sharing is subject to the Azure AD organizational relationships settings, such as **Members can invite** and **Guests can invite**.


[SharePoint and OneDrive integration with Azure AD B2B (Preview)](sharepoint-azureb2b-integration-preview.md)

## See also

[External sharing overview](external-sharing-overview.md)

[Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)

[Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c)
