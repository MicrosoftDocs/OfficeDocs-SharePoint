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

# Find OneDrive settings in the new SharePoint admin center

This article covers all the features in the OneDrive admin center and where you can find them in the new SharePoint admin center.

## Sharing page

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Default link type  <br/> |Yes  <br/> |
|Advanced settings for shareable links <br/> |Yes  <br/> |
|External sharing for SharePoint and OneDrive  <br/> |Yes  <br/> |
|Advanced settings for external sharing   <br/> |Yes   <br/> |
|Other: Display to owners the names of people who viewed their files   <br/> |???   <br/> |

## Sync page

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Show the Sync button on the OneDrive website  <br/> |Yes  <br/> |
|Allow syncing only on PCs joined to specific domains <br/> |Yes  <br/> |
|Block syncing of specific file types  <br/> |Yes  <br/> |

## Storage page

| Classic | New |
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png) |

<br/>

| Classic | New |
|:-----|:-----|
|Default storage in GB <br/> |Yes  <br/> |
|Days to retain files in OneDrive after a user account is marked for deletion <br/> |Yes  <br/> |

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
