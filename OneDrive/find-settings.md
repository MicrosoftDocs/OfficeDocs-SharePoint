---
title: "Find OneDrive admin settings"
ms.reviewer: david.minasyan
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
description: "Learn where to find features from the OneDrive admin center. "
---

# Find OneDrive admin settings

This article covers all the features in the OneDrive admin center and where you can find them in other places.

## Sharing page

Go to the [**Sharing page** in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=sharing&modern=true)

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Sharing page in OneDrive admin center](media/sharing-page.png)|![Sharing page in SharePoint admin center](media/sp-sharing-page.png) |

## Sync page

Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and select **Sync**.

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Sync page in the OneDrive admin center](media/sync-page.png)|![Sync settings in the SharePoint admin center](media/sp-sync-settings.png) |

## Storage page

For the default storage setting, go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and select **Storage limit**.

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Storage page in the OneDrive admin center](media/storage-page.png)|![Classic other options](media/default-storage-limit.png) |

For the default storage setting, go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true), and select **Storage limit**.

| OneDrive admin center | SharePoint admin center |
|:-----|:-----|
|![Storage page in the OneDrive admin center](media/storage-page.png)|![Classic other options](media/default-storage-limit.png) |

## Device access page

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Allow access only from specific IP address locations <br/> |Yes  <br/> |
|Allow access from apps that don't use modern authentication <br/> |Yes  <br/> |
|Mobile application management <br/> |Map with Intune  <br/> |

## Compliance

This page contained links to other admin centers in Microsoft 365. Those places still exist. 

## Notifications

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Display device notifications to users when OneDrive files are shared with them <br/> |Yes  <br/> |
|Other users invite additional external users to shared files <br/> |Set-SPOTenant -NotifyOwnersWhenItemsReshared  <br/> |
|External users accept invitations to access files <br/> |Deprecated  <br/> |
|An anonymous access link is created or changed <br/> |Set-SPOTenant -OwnerAnonymousNotification  <br/> |

## Data migration

This page redirects to Migration Manager in the SharePoint admin center.

## Geo locations

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Switch location <br/> |Yes  <br/> |
|Add location  <br/> |Yes  <br/> |
|Delete satellite locations <br/> |Yes  <br/> |
