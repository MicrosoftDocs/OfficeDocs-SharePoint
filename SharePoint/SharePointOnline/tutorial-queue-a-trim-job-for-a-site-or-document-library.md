---
title: "Tutorial: Queue a Trim Job for a Site or Document Library"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 02/22/2024
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
description: "This article provides guidance on how to queue a Trim Job for a Site or Document Library."

---

# Tutorial: Queue a Trim Job for a Site or Document Library (Preview)

In this tutorial we discuss:

- Schedule a batch trim job from a site or library.
- Stop an in-progress batch deletion job.
- Check progress of your batch deletion job.

## Prerequisites

1. Determine the **Scope [Site, Library]** for version deletion - You can delete old file versions for all document libraries in a site or for a specific document library.
1. Determine the minimum **age (in days)** for the file versions you want to delete. For example, on May 1, 2023, if you choose to delete file versions that are at least 30 days old, then the versions snapshotted before April 1, 2023 (your target date), will be deleted.

## Queue Trim Job

Follow the PowerShell examples to start deleting old file versions. Make sure you're a site administrator.

**Example 1. Queue trim job to delete versions on all libraries on a Site.**

To delete versions that are older than 180 days old for all document libraries in the site collection `https://contoso.sharepoint.com`.

:::image type="content" source="media/version-history/batch-trim-all-lib.png" lightbox="media/version-history/batch-trim-all-lib.png" alt-text="batch trim all library":::

**Example 2. Batch trim versions on a single library on a site.**

To delete versions that are older than 30 days in document library 'Documents' in the site collection `https://contoso.sharepoint.com`.

:::image type="content" source="media/version-history/batch-trim-single-lib.png" lightbox="media/version-history/batch-trim-single-lib.png" alt-text="batch trim single library":::

Once the cmdlet executes successfully, versions that match your criteria are deleted asynchronously in batches in the upcoming days.

## Cancel an in-progress Batch Trim Job

If needed, you can cancel an in-progress batch trim job. Once the cmdlet executes successfully, asynchronous version deletion is stopped, but versions that are already deleted stay removed.

**Example 1. Stop additional batch deletion on site scoped trim job.**

To stop the more batch deletion for the site collection `https://contoso.sharepoint.com`.

:::image type="content" source="media/version-history/batch-deletion-site-scoped.png" lightbox="media/version-history/batch-deletion-site-scoped.png" alt-text="batch deletion site scoped":::

**Example 2. Stop additional batch deletion on library scoped trim job.**

To stop the more batch deletion for the document library Documents in site collection `https://contoso.sharepoint.com`.

:::image type="content" source="media/version-history/batch-deletion-lib-scoped.png" lightbox="media/version-history/batch-deletion-lib-scoped.png" alt-text="batch trim library scoped":::

