---
title: "Block unmanaged device access controls for administrators"
ms.reviewer: samust
ms.author: samust
author: SanjoyanM
manager: sesham
recommendations: true
audience: Admin
f1.keywords: CSH
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
ms.assetid: 5ae550c4-bd20-4257-847b-5c20fb053622
description: Learn how administrators can block download of files from a SharePoint site and OneDrive. Needs no conditional access policies.
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
---

# Block download of files from a SharePoint site and OneDrive

As a SharePoint Administrator or Global Administrator in Microsoft 365, you can block download of files from a SharePoint sites and OneDrive. This feature do not need  Azure active directory conditional access policy. This feature can be set for individual sites and cannot be set at tenant level. [If you want to prevent download of SharePoint content from unmanaged devices then check this feature](https://learn.microsoft.com/en-us/sharepoint/control-access-from-unmanaged-devices).

Blocking download of files allows users to remain productive while addressing the risk of accidental data loss. Users will have browser-only access with no ability to download, print, or sync files. They also won't be able to access content through apps, including the Microsoft Office desktop apps. When web access is limited, users will see the this message at the top of sites, "Your organization doesn't allow you to download, print, or sync from this site. For help contact your It department."

## How to set this policy for a SharePoint site

1. To use PowerShell: [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3.  Run the following command.

    ```PowerShell
    Set-SPOSite -Identity https://<SharePoint online URL>/sites/<name of site or OneDrive account> -BlockDownloadPolicy $true
    ```
 
 ## Advanced configurations
 
 The following parameters can be used with this cmdlet to fine tune it.
 
 `-ExcludeBlockDownloadPolicySiteOwners $true` Exempts site owners from this policy and they can fully download any content for the site.
 
 `-ExcludedBlockDownloadGroupIds <comma separated group ids>` Exempts users from the mentioned groups from this policy and they can fully download any content for the site.
 
 ## App impact

Blocking download may impact the user experience in some apps, including some Office apps. We recommend that you turn on the policy for some users and test the experience with the apps used in your organization. In Office, make sure to check the behavior in Power Apps and Power Automate when your policy is on.

> [!NOTE]
> Apps that run in "app-only" mode in the service, like antivirus apps and search crawlers, are exempted from the policy.
>
> If you're using classic SharePoint site templates, site images may not render correctly. This is because the policy prevents the original image files from being downloaded to the browser.
>

## Need more help?

[SharePoint Q&A](/answers/topics/office-sharepoint-online.html)

## See also

[Policy recommendations for securing SharePoint sites and files](/microsoft-365/enterprise/sharepoint-file-access-policies)

[Control access to SharePoint and OneDrive data based on defined network locations](control-access-based-on-network-location.md)
