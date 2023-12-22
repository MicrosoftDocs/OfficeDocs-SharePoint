---
title: "FAQs for Versions"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/14/2023
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
description: "Learn frequently asked questions for versions."
---

# Frequently asked questions for Version history limits

**What happens to versions that have expired or exceeded the count limits?**

When a user [deletes a previous version of an item or file in SharePoint (microsoft.com)](https://support.microsoft.com/en-us/office/delete-a-previous-version-of-an-item-or-file-in-sharepoint-45edfb0d-8b43-4f07-ac6a-ab4ac169d5aa#__bkmkrecycle), SharePoint moves versions into the recycle bin. Users are able to [restore deleted versions from the site collection recycle bin (microsoft.com)](https://support.microsoft.com/en-us/office/restore-deleted-items-from-the-site-collection-recycle-bin-5fa924ee-16d7-487b-9a0a-021b9062d14b).

Versions trimmed under the automatic setting or because the version’s age or count exceeded the limits set by the admin are marked for permanent deletion. These are available to restore from the recycle bin.

**How do legal holds or retention policies impact version deletions or expirations?**

When a document with versions is subject to retention settings, the retention of versions is determined by the configured retention setting. In other words, the retention setting always wins, whether that be a deletion or hold policy. [Learn about retention for SharePoint and OneDrive - Microsoft 365 Compliance | Microsoft Docs](/microsoft-365/compliance/retention-policies-sharepoint?view=o365-worldwide#how-retention-works-with-document-versions&preserve-view=true).

**What happens when organization-level or library-level version settings are updated?**

When **Organization-level version settings are updated**, the new settings are applied to all new libraries created since the change was made. The new settings won't be applied to existing libraries or to versions that have already been created.  

When **Library-level version expiration setting is updated**, the new expiration limit is applied to newly created versions only. For example, if the version expiration settings of a library are updated from "Never expire" to "Expire after six months", only the newer versions will be set to expire after six months with no impact on the older versions.  

When **Library-level count limits are updated**, if existing versions exceed the new count limit, then those versions will be gradually trimmed when the file is updated. For example, if a library having count limits set to 500 versions were reduced to 300 versions - and you had a file with 500 versions, every time a user updated the file, the oldest 20 versions are purged until you are at the right number of versions.
