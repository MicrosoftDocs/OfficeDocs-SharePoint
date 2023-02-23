---
title: Block the download of Teams meeting recording files from SharePoint or OneDrive (preview)
ms.reviewer: samust
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
- BSA160
description: Learn how administrators can block the download of Teams meeting recording files from SharePoint and OneDrive.
---

# Block the download of Teams Meeting Recording files from SharePoint or OneDrive (preview)

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

As a SharePoint administrator or Global administrator in Microsoft 365, you can block the download of Teams meeting recording files from SharePoint or OneDrive. This feature can only be set at the organization level.

Blocking the download of Teams meeting recording files allows users to remain productive while addressing the risk of accidental data loss. Users have browser-only access to play the meeting recordings with no ability to download or sync files. They also won't be able to access content through apps. After this feature is turned on, any _new_ Teams meeting recording files created by the Teams service and saved in SharePoint and OneDrive are blocked. Note that this feature does not apply to manually uploaded meeting recording files. This feature will also not prevent the download of files that were uploaded by the Teams service prior to turning the feature on. If you would like to do so, you can open a support ticket.   

## Set this policy for a SharePoint site

1. To use PowerShell, [download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of SharePoint Online Management Shell, go to **Add or remove programs** and uninstall SharePoint Online Management Shell.
2. Connect to SharePoint as a [Global administrator or SharePoint administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3.  Run the following command:

    ```PowerShell
    Set-SPOTenant -BlockDownloadFileTypePolicy <$true/$false(default)>  -BlockDownloadFileTypeIds  TeamsMeetingRecording
    ```
    For example, to turn this feature on, run `Set-SPOTenant -BlockDownloadFileTypePolicy $true  -BlockDownloadFileTypeIds  TeamsMeetingRecording`.

## Exempting users in security groups from the policy

 The following parameter can be used with this cmdlet if required:

  `-ExcludedBlockDownloadGroupIds <comma separated security group ids>`
  
  This parameter exempts users from security groups from this policy so that they can fully download any meeting recording files of the organization.

## App impact

Blocking download may impact the user experience in some apps, including some Office apps. We recommend that you turn the policy on for some users and test the experience with the apps used in your organization. 

> [!NOTE]
> Apps that run in "app-only" mode in the service, like antivirus apps and search crawlers, are exempted from the policy.

## Need more help?

[SharePoint Q&A](/answers/topics/office-sharepoint-online.html)

## Related topics

[SharePoint and OneDrive unmanaged device access controls for administrators](/sharepoint/control-access-from-unmanaged-devices)

[Policy recommendations for securing SharePoint sites and files](/microsoft-365/enterprise/sharepoint-file-access-policies)

[Control access to SharePoint and OneDrive data based on defined network locations](control-access-based-on-network-location.md)
