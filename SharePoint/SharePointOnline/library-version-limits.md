---
title: "Set version limits for a document library"
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
description: "This article provides guidance on how admins can set version limits for a document library."

---


# Set version limits for individual document library

The default version history limits for new document libraries are set by either the organization-level limits or the site-level limits. If the site has its own version history limit, it means the site breaks inheritance from the organization. However, to meet specific content requirements, site admins can decide to [configure versioning for a library](https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37).

Here's a summary of the expected behavior when document libraries version expiration or count limits are updated:  

- **When library level version expiration setting is updated**, the new expiration limit is applied to newly created versions only. Take an example of a library with version expiration settings updated from **Never Expire** to **Expire after six months**. New version created is set to expire after six months with no impact on versions that is already created.  

- **When library level count limits are updated**, if existing versions exceed the new count limit, then those versions are gradually trimmed when the file is updated. Consider a library where the version count limit is initially set to 500 versions but is later reduced to 300 versions. In this scenario, if there's a file with 500 versions, each time a user updates the file, the system gradually purges the oldest 20 versions with each new version creation until the total number of versions aligns with the updated limit of 300. It's crucial to note that when count limits are lowered, the process of version deletion occurs gradually, with up to 20 versions being removed for every new version created.  

:::image type="content" source="media/version-history/overright-version-history-limits-document-library.png" lightbox="media/version-history/overright-version-history-limits-document-library.png" alt-text="Screenshot of overwrite version history.":::

## Manage version history limits for a library using PowerShell

Follow these steps to manage version history limits for a site by using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall **SharePoint Online Management Shell**.

1. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Run one of the following commands to manage version history limits on a library:

   | **Action** | **PowerShell Command** |
   | --- | --- |
   | View version history limits set on a library | `Get-SPOListVersionPolicy -Site $siteUrl -List $libName` |
   | Set Automatic version history limits on a library | `Set-SPOListVersionPolicy -Site $siteUrl -List $libName -EnableAutoExpirationVersionTrim $true` |
   | Set Manual limits with count and time parameters on a library | `Set-SPOListVersionPolicy -Site $siteUrl -List $libName`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersionLimit <delete major versions exceeding limit>`<br>`-MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>`<br>`-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>`|
   | Set Manual limits with count with no expiration limit on a library | `Set-SPOListVersionPolicy -Site $siteUrl -List $libName`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersionLimit <delete major versions exceeding limit>`<br>`-MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>`<br>`-ExpireVersionsAfterDays 0` |

## Learn More

For more information, check out the following resources:

- Manage version history limits for a library using [Set-SPOListVersionPolicy](/powershell/module/sharepoint-online/set-spolistversionpolicy)
