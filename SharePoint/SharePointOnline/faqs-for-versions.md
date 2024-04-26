---
title: "FAQs for versions history limits"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 04/30/2024
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

# FAQs 

## What happens to versions that are deleted, have expired, or exceeded the count limits?

When a user [deletes a previous version of an item or a file in SharePoint (microsoft.com)](https://support.microsoft.com/en-us/office/delete-a-previous-version-of-an-item-or-file-in-sharepoint-45edfb0d-8b43-4f07-ac6a-ab4ac169d5aa#__bkmkrecycle), SharePoint moves versions into the recycle bin. Users are able to [restore deleted versions from the site collection recycle bin (microsoft.com)](https://support.microsoft.com/en-us/office/restore-deleted-items-from-the-site-collection-recycle-bin-5fa924ee-16d7-487b-9a0a-021b9062d14b).

Versions trimmed by the Automatic setting or when a version's age exceeds the manual time limits, are tagged for permanent deletion. They aren't available for restoration from the recycle bin once purged.  

> [!NOTE]
> Background timer jobs permanently purge expired versions and this process may take a couple of days from the actual expiration date.  

Versions that exceed count limits are gradually trimmed when the file is updated. Each file update triggers approximately 20 version deletions until the count limits are met.  

## How do legal holds or retention policies impact version deletions or expirations?

When a site is on hold or a document with versions is subject to retention settings, the configured retention setting determines the retention of versions. In other words, the retention setting always wins, whether it's a deletion or hold policy. [Learn about retention for SharePoint and OneDrive](/microsoft-365/compliance/retention-policies-sharepoint?view=o365-worldwide#how-retention-works-with-document-versions&preserve-view=true).

## What happens when organization level or library level version settings are updated?

When **organization-level version settings are updated**, the new settings are applied to all new libraries created since the change was made. The new settings don't apply to existing libraries or versions already created.

When **library-level version expiration setting is updated**, the new expiration limit is applied to newly created versions only. Take an example of a library with version expiration settings updated from **Never Expire** to **Expire after six months**. The newly created versions are set to expire after six months with no impact on previously created versions.  

When **library-level count limits are updated**, if existing versions exceed the new count limit, then those versions are gradually trimmed when the file is updated. Take an example of a library with count limits set to 500 versions, was reduced to 300 versions. If you had a file with 500 versions, every time a user updates the file, the oldest 20 versions are purged until you are at the right number of versions.

## How will automatic setting impact ability to restore a library or OneDrive?

When **Automatic setting** is selected, users have access to a maximum of 500 versions created within the last 30 days enabling the user to [Restore a shared library](https://support.microsoft.com/en-us/office/restore-a-shared-library-317791c3-8bd0-4dfd-8254-3ca90883d39a) or [Restore your OneDrive](https://support.microsoft.com/en-us/office/restore-your-onedrive-fa231298-759d-41cf-bcd0-25ac53eb8a15).
