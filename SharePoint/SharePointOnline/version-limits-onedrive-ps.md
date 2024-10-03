---
title: "Set version limits on OneDrive using PowerShell"
ms.reviewer: rekamath
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 10/03/2024
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- SPO160
- SPS150
- MET150
description: "This article provides guidance on how an admin can set the version limits on OneDrive for a specific user using PowerShell."

---


# Change version limits on OneDrive using PowerShell

By default, organization version history settings are applied to all new OneDrive accounts. As a SharePoint admin in Microsoft 365, you can set the version limits on OneDrive storage for a specific user.

Follow these steps to manage Version history limits for a site by using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall **SharePoint Online Management Shell**.

1. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Run one of the following commands to manage Version history limits for a specific user:

| **Action** | **PowerShell Command** |
| --- | --- |
| View the version history limits set for a user | Get-SPOSite -Identity $siteUrl \| fl Url, EnableAutoExpirationVersionTrim, ExpireVersionsAfterDays, MajorVersionLimit |
| Set automatic Version history limits for a user | `Set-SPOSite -Identity $siteUrl -EnableAutoExpirationVersionTrim $true` |
| Set manual limits with count and time parameters for a user | `Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersionLimit <delete major versions exceeding limit>`<br>`-MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>`<br>`-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>` |
| Set manual limits with count with no expiration limit for a user | To set manual limits with count limits set the `-ExpireVersionsAfterDays parameter` to 0:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersionLimit  <delete major versions exceeding limit>`<br>`-MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>`<br>`-ExpireVersionsAfterDays 0` |
| Clear the existing Version history limits for a user<br><br>**Note:** Clearing a setting for a user applies to new versions created on files stored on the user’s OneDrive account and doesn't trim existing versions. | `Remove-SPOSiteVersionPolicyJob -Identity $siteUrl` |

## Learn More

[Change a specific user's OneDrive storage space](change-user-storage.md)
