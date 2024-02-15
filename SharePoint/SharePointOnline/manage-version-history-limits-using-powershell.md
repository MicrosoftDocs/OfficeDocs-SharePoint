---
title: "Manage Version history limits for a site using PowerShell"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/22/2023
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
description: "This article provides guidance on how to manage version history limits for a site using PowerShell."

---

# Manage Version history limits for a Site using PowerShell

## Environment Setup

To manage **Version history limits** for a Site using PowerShell, install the latest PnP PowerShell. For details, see [Installing PnP PowerShell | PnP PowerShell](https://pnp.github.io/powershell/articles/installation.html).

## Set Site Level Version Limits for both new and existing document libraries

### Apply Automatic settings

:::image type="content" source="media/version-history/automatic-setting-pnp-site.PNG" alt-text="automatic set pnp":::

### Apply Manual Setting with versions count and Time limits

:::image type="content" source="media/version-history/manual-setting-pnp-site-time-limit.PNG" alt-text="manual set pnp time limit":::

### Apply Manual Setting with versions count and No Time limits

:::image type="content" source="media/version-history/manual-setting-pnp-site-no-time-limit.PNG" alt-text="manual set pnp no time limit":::

## Set site version policy for new document libraries only

### Apply Automatic settings 

:::image type="content" source="media/version-history/automatic-setting-new-libs.PNG" alt-text="automatic set for new libs":::

### Apply Manual Setting with Major Version Count and Time limits

:::image type="content" source="media/version-history/automatic-setting-new-libs-time-limit.PNG" alt-text="automatic setting new libs with time limit":::

### Apply Manual Setting with Major Version Count and No Time limits  

:::image type="content" source="media/version-history/automatic-setting-new-libs-no-time-limit.PNG" alt-text="automatic setting new libs with no time limit":::

### Clear Site Level Version history limits  

If the setting on the site is cleared, the new document libraries use the tenant level settings.  
> [!NOTE]
> Clearing a setting on a Site will only apply to New Document Libraries created on the site and will not impact the settings on existing doc libraries.  

:::image type="content" source="media/version-history/inherit-tenant-new-doc-libs.PNG" alt-text="inherit tenant new doc libs":::

## Set site version policy for existing document libraries only

### Apply Automatic settings

:::image type="content" source="media/version-history/automatic-setting-existing-libs.PNG" alt-text="automatic setting existing libs":::

### Apply Manual Setting with Versions count and Time limits

:::image type="content" source="media/version-history/manual-setting-existing-libs-time-limit.PNG" alt-text="manual setting existing libs time limit":::

### Apply Manual Setting with Versions count and NO Time limits

:::image type="content" source="media/version-history/manual-setting-existing-libs-no-time-limit.PNG" alt-text="manual setting existing libs no time limit":::

### Cancel the request  

Cancels the settings update request on libraries that isn't processed. This won't revert the change for document libraries where the settings update was already processed.

:::image type="content" source="media/version-history/cancel-existing-libs.PNG" alt-text="cancel existing libs":::

## Get progress for Set site version policy

It is for setting version policy for **existing** document libraries on the site.  

`Get-PnPSiteVersionPolicyProgress`

Here's the description of the status in response:

| **Status:** | **Description** |
|:-----|:-----|
| `NoRequestFound` | There's no request on the site to set version policy for existing document libraries. |
| `New`   | It's a new request and never processed. |
| `InProgress`  | The request was processed but not completed yet. |
| `CompleteSuccess` | The request was processed and completed successfully. |
| `CompleteWithFailure`  | It was processed and completed, but some document libraries failed to set the version policy. |

- `NoRequestFound`

:::image type="content" source="media/version-history/norequest.PNG" alt-text="no request":::

- `New`request

:::image type="content" source="media/version-history/newrequest.PNG" alt-text="new request":::

- `InProgress` request

:::image type="content" source="media/version-history/inprogress.PNG" alt-text="in progress":::

- `Complete` request

:::image type="content" source="media/version-history/completedrequest.PNG" alt-text="completed request":::

