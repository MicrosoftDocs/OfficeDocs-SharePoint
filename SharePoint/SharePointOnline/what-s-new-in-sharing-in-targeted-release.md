---
ms.date: 07/11/2018
title: "Secure external sharing in SharePoint"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: cc78357c-6d48-499c-9cc7-dae447d0d391
description: "In SharePoint, if you share with a user who is not in the directory, they are sent a one-time code that they can use to verify their identity."
---

# Secure external sharing recipient experience

In SharePoint, if you share with a person who is not in the directory, they're sent a one-time code that they can use to verify their identity.

This article describes the current default one-time-passcode experience. However, we recommend that you enable [SharePoint and OneDrive integration with Microsoft Entra B2B](sharepoint-azureb2b-integration.md), which will replace this experience.

Recipients of secure external sharing who also use Microsoft 365 in their organization can sign in using their work or school account to access the document. After they have entered the one-time passcode for verification the first time, they will authenticate with their work or school account and have a guest account created in the host's organization. IT admins can manage them like any other guest account in their directory.

Guest accounts are used for sharing sites, and you can always add guests to your directory if you need to give them access to more than just a file or folder.

The following table shows the differences between sharing with people who have guest accounts and with ad hoc external recipients.

|&nbsp;|Guest account|Ad hoc external recipient|
|---|---|---|
|Can access shared files and folders|Yes|Yes|
|Verify access by...|Signing in to Microsoft 365|Entering a time-sensitive and single-use code sent to the email address that the file or folder was share with|
|Actions are audited|Yes|Yes|
|Can have friendly name|Yes|Friendly name is the email address that the file or folder was shared with|
|Can be Group members|Yes|No|
|Can edit in Word, Excel, PowerPoint, or other Microsoft 365 apps|Yes|No|
|Access controlled by Microsoft Entra Conditional Access policies|Yes|No|

 When you use the Share dialog box to share with "specific people" and the recipients are all outside the organization, then a secure link will be created and the specified email addresses will be secured, or added, to the link. This appears in audit logs in the following ways.

> [!NOTE]
> If the UserType property of a User object is "guest", the user is outside of your organization but may be an ad hoc external recipient that does not have a guest account.

> [!NOTE]
> Auditing operations related to sharing invitations can still appear in situations when SharePoint items other than files and folders are shared with guests (for example, when you share a SharePoint site with guests).

|Operation|Description|
|---|---|
|SecureLinkCreated|A link that only works for specific people was created. It's usually followed by a series of AddedToSecureLink operations, which signify the users who were secured to the link. The value in the **Detail** column for this activity identifies the UniqueSharingId for this link, which can be used to match against future AddedToSecureLink and RemovedFromSecureLink operations.|
|SecureLinkDeleted|A link that only works for specific people was deleted. It's usually preceded by a series of RemovedFromSecureLink operations, which signify the users who used to be secured to the link. The value in the **Detail** column for this activity identifies the UniqueSharingId for this link, which can be used to match against future AddedToSecureLink and RemovedFromSecureLink operations.|
|AddedToSecureLink|A link that only works for specific people was secured to a user. The value in the **Detail** column for this activity identifies the name or email of the user the link was secured to and whether this user is a guest. The value also has a UniqueSharingId column that identifies the link they were secured to.|
|RemovedFromSecureLink|A user was removed from a link that only works for specific people. The value in the **Detail** column for this activity identifies the name or email of the user the link was previously secured to and whether this user is a guest. The value also has a UniqueSharingId column that identifies the link they were secured to.|

## See also

[External sharing overview](external-sharing-overview.md)

[Share SharePoint files or folders in Microsoft 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c)

[Change permissions and seeing who you've shared with](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
