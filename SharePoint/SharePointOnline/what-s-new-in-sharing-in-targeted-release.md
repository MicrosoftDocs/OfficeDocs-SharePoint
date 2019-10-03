---
title: "Secure external sharing in SharePoint Online"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: cc78357c-6d48-499c-9cc7-dae447d0d391
description: "In SharePoint Online, if you share with a user who is not in the directory, they are sent a one-time code that they can use to verify their identity."
---

# Secure external sharing recipient experience

A new method of securely sharing files and folders with external users is being implemented. Previously, when securely sharing with users who were not in the organization's directory, these users were sent an invitation and had to sign in using a Microsoft account or a work or school account in Azure AD. They were then added to the directory as guests and given permissions to the file or folder.
  
Going forward, recipients of secure external sharing who also use Office 365 in their organization will be able to sign in using their work or school account to access the document. After they have entered the one-time passcode for verification the first time, they will authenticate with their work or school account and have a full guest account created in the host's organization. This means that IT admins can manage them like any other guest account in their directory. 
  
The procedures for sharing files and folders remain the same. They can be found in [Share SharePoint files or folders in Office 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c). The procedures for [changing permissions and seeing who you've shared with](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323) also remain the same, though users who use the new external sharing experience appear underneath the link that was shared with them, not as a top-level user. 
  
Guest accounts are still used for sharing sites, and you can always add guest users to your directory if you need to give them access to more than just a file or folder. "Anyone" links remain available and are unchanged.
  
The following table shows the differences between sharing with external users with guest accounts and with ad-hoc external recipients.
  
||**Guest account**|**Ad-hoc external recipient**|
|:-----|:-----|:-----|
|Can access shared files and folders  <br/> |Yes  <br/> |Yes  <br/> |
|Verify access by…  <br/> |Signing in to Office 365  <br/> |Entering a time-sensitive and single-use code sent to the email address that the file or folder was share with  <br/> |
|Actions are audited  <br/> |Yes  <br/> |Yes  <br/> |
|Can have friendly name  <br/> |Yes  <br/> |Friendly name is the email address that the file or folder was shared with  <br/> |
|Can be Group members  <br/> |Yes  <br/> |No  <br/> |
|Can edit in Word, Excel, PowerPoint, or other Office 365 apps  <br/> |Yes  <br/> |No  <br/> |
|Access controlled by AAD conditional access policies  <br/> |Yes  <br/> |No  <br/> |
   
 This update also introduces some changes to the way that external sharing is audited. When using the share dialog to share with "specific people" and the recipients are all external users then a secure link will be created and the specified email addresses will be secured, or added, to the link. This appears in audit logs in the following ways: 
  
> [!NOTE]
> If the UserType property of a User object is "guest", the user is outside of your organization but may be an ad-hoc external recipient that does not have a Guest account 
  
> [!NOTE]
> Auditing operations related to sharing invitations can still appear in situations when SharePoint items other than files and folders are shared with external users (for example, when sharing a SharePoint site with external users). 
  
|**Operation**|**Description**|
|:-----|:-----|
|SecureLinkCreated  <br/> |A link that only works for specific people was created. It is usually followed by a series of AddedToSecureLink operations which signify the users who were secured to the link. The value in the **Detail** column for this activity identifies the UniqueSharingId for this link which can be used to match against future AddedToSecureLink and RemovedFromSecureLink operations. <br/> |
|SecureLinkDeleted  <br/> |A link that only works for specific people was deleted. It is usually preceded by a series of RemovedFromSecureLink operations which signify the users who used to be secured to the link. The value in the **Detail** column for this activity identifies the UniqueSharingId for this link which can be used to match against future AddedToSecureLink and RemovedFromSecureLink operations. <br/> |
|AddedToSecureLink  <br/> |A link that only works for specific people was secured to a user. The value in the **Detail** column for this activity identifies the name or email of the user the link was secured to and whether this user is an external user. The value also has a UniqueSharingId column that identifies the link they were secured to.  <br/> |
|RemovedFromSecureLink  <br/> |A user was removed from a link that only works for specific people. The value in the **Detail** column for this activity identifies the name or email of the user the link was previously secured to and whether this user is an external user. The value also has a UniqueSharingId column that identifies the link they were secured to.  <br/> |

> [!NOTE]
> Secure links is a default way to allow external recipients to access files and folders securely without requiring them to create or maintain a Microsoft account. Email-based verification codes are a simple and effective way to provide secure access, familiar to users who access secure internet sites that verify identity by sending a code by email or text message.

## See also
[External sharing overview](external-sharing-overview.md)

[Secure SharePoint Online sites and files](/office365/securitycompliance/secure-sharepoint-online-sites-and-files)

