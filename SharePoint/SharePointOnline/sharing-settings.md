---
title: "Sharing settings in the new SharePoint admin center"
ms.reviewer: srice
manager: pamgreen
ms.author: kaarins
author: kaarins
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- SPO160
- MET150
ms.assetid: 
description: "In this article, you'll learn where to find sharing settings in the new SharePoint admin center."
---

# Find sharing settings in the new SharePoint admin center

This article covers all the features on the sharing page of the classic SharePoint admin center and where you can find them in the new SharePoint admin center.

## Sharing outside your organization

|**Classic**|**New**|
|:-----|:-----|
|![Classic Sharing outside your organization settings](media/classic-external-sharing.png)|![New external sharing settings](media/new-external-sharing.png)|

|**Classic**|**New**|
|:-----|:-----|
|Don't allow sharing outside your organization <br/> Allow sharing only with the external users that already exist in your organization's directory <br/> Allow users to invite and share with authenticated external users <br/> Allow sharing to authenticated external users and using anonymous access links|**External sharing, SharePoint slider**<br/>Only people in your organization<br/>Existing guests<br/>New and existing guests<br/>Anyone|
|Anonymous access links expire in this many days: |**File and folder links**, under **Choose expiration and permissions options for Anyone links.** <br/>These links must expire within this many days|
|Anonymous access links allow recipients to: <br/> Files <br/> Folders <br/> |  **File and folder links**, under **Choose expiration and permissions options for Anyone links.** <br/>These links can give these permissions:
|Let only users in selected security groups share with authenticated external users <br/> Let only users in selected security groups share with authenticated external users and using anonymous links <br/>|**More external sharing settings**  <br/> Allow only users in specific security groups to share externally <br/> In the Manage security groups panel, under **Can share with**, select **Anyone** or **Authenticated guests only**. |

## Default links

|**Classic**|**New**|
|:-----|:-----|
|![Classic default link type settings](media/classic-default-link.png)|![New File and folder links settings](media/new-file-folder-links.png)|

|**Classic**|**New**|
|:-----|:-----|
|**Default link type** <br/> Direct - specific people <br/> Internal - only people in your organization <br/> Anonymous Access - anyone with the link |**File and folder links**  <br/> **Choose the type of link that's selected by default when users share files and folders in SharePoint and OneDrive.** <br/> Specific people (only the people the user specifies) <br/> Only people in your organization <br/> Anyone with the link  |
|Use shorter links when sharing files and folders | **Other settings**<br/>Use short links for sharing files and folders |
|**Default link permission** <br/> View <br/> Edit <br/> |**Choose the permission that's selected by default for sharing links.** <br/> View <br/> Edit <br/>|

## Additional settings

|**Classic**|**New**|
|:-----|:-----|
|![Classic Additional settings](media/additional-sharing-settings.png)|![New More external sharing settings](media/new-more-external-sharing.png)|

|**Classic**|**New**|
|:-----|:-----|
|Limit external sharing using domains <br/>|**External sharing**, **More external sharing settings**<br/>Limit external sharing by domain|
|Prevent external users from sharing files, folders, and sites that they don't own |**External sharing**, **More external sharing settings**<br/>Allow guests to share items they don't own|
|External users must accept sharing invitations using the same account that the invitations were sent to |**External sharing**, **More external sharing settings**<br/>Guests must sign in using the same account to which sharing invitations are sent|
|Require recipients to continually prove account ownership when they access shared items |**External sharing**, **More external sharing settings**<br/>People who use a verification code must reauthenticate after this many days|
|**Notifications**<br/> E-mail OneDrive for Business owners when<br/> Other users invite additional external users to shared files<br/>External users accept invitations to access files <br/> An anonymous access link is created or changed||


 
