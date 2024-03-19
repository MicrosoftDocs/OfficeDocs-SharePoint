---
ms.date: 1/19/2024
title: Block download policy for SharePoint sites and OneDrive
ms.reviewer: samust
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Strat_SP_admin
- Highpri
- Tier1
- M365-sam
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160
description: Learn how administrators can block download of files from a SharePoint and OneDrive without using conditional access policies.
---

# Block download policy for SharePoint sites and OneDrive

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

As a SharePoint Administrator or Global Administrator in Microsoft 365, you can block download of files from SharePoint sites or OneDrive. This feature does not need  Microsoft Entra Conditional Access policies. This feature can be set for individual sites and cannot be set at the organization level.

Blocking download of files allows users to remain productive while addressing the risk of accidental data loss. Users have browser-only access with no ability to download, print, or sync files. They also won't be able to access content through apps, including the Microsoft Office desktop apps. When web access is limited, users will see this message at the top of sites, "Your organization doesn't allow you to download, print, or sync from this site. For help contact your It department."

Note that you can block the download of Teams meeting recording files specifically if you need to. For more information, see [Block the download of Teams meeting recording files from SharePoint or OneDrive](/microsoftteams/block-download-meeting-recording).

## Requirements

This feature requires [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md).

## How to set this policy for a SharePoint site

1. To use PowerShell: [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3.  Run the following command.

    ```PowerShell
    Set-SPOSite -Identity <SiteURL> -BlockDownloadPolicy $true
    ```
    For example, `Set-SPOSite -Identity https://contoso.sharepoint.com/sites/research -BlockDownloadPolicy $true`. You can apply this cmdlet to OneDrive as well by changing the URL to `https://contoso-my.sharepoint.com/personal/John`. 

The following parameters can be used with this cmdlet to fine-tune it:

- `-ExcludeBlockDownloadPolicySiteOwners $true`<br/>Exempts site owners from this policy and they can fully download any content for the site.

- `-ExcludedBlockDownloadGroupIds <comma separated group IDs>`<br/>Exempts users from the mentioned groups from this policy and they can fully download any content for the site.

- `-ExcludeBlockDownloadSharePointGroups <comma separated group IDs>`<br/>Exempts users from the mentioned SharePoint groups from this policy and they can fully download any content for the site.

- `-ReadOnlyForBlockDownloadPolicy $true`<br/>Marks the site as read-only in addition to preventing downloads. 

You also can attach a block download policy to a site sensitivity label.
  
```PowerShell
Set-Label -Identity 'Internal' -AdvancedSettings @{BlockDownloadPolicy="true" | “false” }
Set-Label -Identity 'Internal' -AdvancedSettings @{ExcludedBlockDownloadGroupIds="<list of security or M365 groups>"}
```

## App impact

Blocking download might impact the user experience in some apps, including some Office apps. We recommend that you turn the policy on for some users and test the experience with the apps used in your organization. In Office, make sure to check the behavior in Power Apps and Power Automate when your policy is on.

> [!NOTE]
> Apps that run in "app-only" mode in the service, like antivirus apps and search crawlers, are exempted from the policy.
>
> If you're using classic SharePoint site templates, site images might not render correctly. This is because the policy prevents the original image files from being downloaded to the browser.

## Need more help?

[SharePoint Q&A](/answers/topics/office-sharepoint-online.html)

## Related topics

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Restrict OneDrive access by security group](limit-access.md)

[Configure a default sensitivity label for a SharePoint document library](/microsoft-365/compliance/sensitivity-labels-sharepoint-default-label)
