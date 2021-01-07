---
title: "Sharing settings in the new SharePoint admin center"
ms.reviewer: srice
manager: serdars
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

This article covers all the features on the sharing page in the classic SharePoint admin center and where you can find them on the [Sharing page](https://admin.microsoft.com/sharepoint?page=sharing&modern=true) in the new SharePoint admin center. 

## Sharing outside your organization

|**Classic**|**New**|
|:-----|:-----|
|![Classic Sharing outside your organization settings](media/classic-external-sharing.png)|![New external sharing settings](media/new-external-sharing.png)|

|**Classic**|**New**|
|:-----|:-----|
|A. Don't allow sharing outside your organization <br/>B. Allow sharing only with the external users that already exist in your organization's directory <br/> C. Allow users to invite and share with authenticated external users <br/>D. Allow sharing to authenticated external users and using anonymous access links|Under **External sharing**, drag the SharePoint slider to the corresponding option:<br/>A. Only people in your organization<br/>B. Existing guests<br/>C. New and existing guests<br/>D. Anyone|
|Anonymous access links expire in this many days |In **File and folder links**, under **Choose expiration and permissions options for Anyone links**, select **These links must expire within this many days**.|
|Anonymous access links allow recipients to |  In **File and folder links**, under **Choose expiration and permissions options for Anyone links**, select **These links can give these permissions**.
|Let only users in selected security groups share with authenticated external users <br/> Let only users in selected security groups share with authenticated external users and using anonymous links <br/>|Expand **More external sharing settings** and select A**llow only users in specific security groups to share externally**. In the Manage security groups panel, under **Can share with**, select **Anyone** or **Authenticated guests only**. |

## Default links

|**Classic**|**New**|
|:-----|:-----|
|![Classic default link type settings](media/classic-default-link.png)|![New File and folder links settings](media/new-file-folder-links.png)|

|**Classic**|**New**|
|:-----|:-----|
|**Default link type** <br/> A. Direct - specific people <br/> C. Internal - only people in your organization <br/> C. Anonymous Access - anyone with the link |In **File and folder links**, under **Choose the type of link that's selected by default when users share files and folders in SharePoint and OneDrive**, select the corresponding option: <br/>A. Specific people (only the people the user specifies) <br/>B. Only people in your organization <br/> C. Anyone with the link  |
|Use shorter links when sharing files and folders | Under **Other settings**, select **Use short links for sharing files and folders**. |
|**Default link permission** <br/> View <br/> Edit <br/> |In **File and folder links**, under **Choose the permission that's selected by default for sharing links**, select an option. <br/> View <br/> Edit <br/>|

## Additional settings

|**Classic**|**New**|
|:-----|:-----|
|![Classic Additional settings](media/additional-sharing-settings.png)|![New More external sharing settings](media/new-more-external-sharing.png)|

|**Classic**|**New**|
|:-----|:-----|
|Limit external sharing using domains <br/>|Under **External sharing**, expand **More external sharing settings**, and then select **Limit external sharing by domain**.|
|Prevent external users from sharing files, folders, and sites that they don't own |Under **External sharing**, expand **More external sharing settings**, and then select **Allow guests to share items they don't own**.|
|External users must accept sharing invitations using the same account that the invitations were sent to |Under **External sharing**, expand **More external sharing settings**, and then select **Guests must sign in using the same account to which sharing invitations are sent**.|
|Require recipients to continually prove account ownership when they access shared items |Under **External sharing**, expand **More external sharing settings**, and then select **People who use a verification code must reauthenticate after this many days**.|
|**Notifications**<br/> E-mail OneDrive for Business owners when<br/> A. Other users invite additional external users to shared files<br/>B. External users accept invitations to access files <br/> C. An anonymous access link is created or changed| A. Use the PowerShell cmdlet `Set-SPOTenant -NotifyOwnersWhenItemsReshared`.<br/>B. This setting doesn't work in the new sharing experience that appears in most places. <br/> C. Use the PowerShell cmdlet `Set-SPOTenant -OwnerAnonymousNotification`. <br/> [More info about using Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant?view=sharepoint-ps)<br/> [Get started with the SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps) |


 
