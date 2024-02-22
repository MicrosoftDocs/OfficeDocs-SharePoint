---
title: "Tutorial: Run 'What-If' analysis on Version Storage Report File"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 01/31/2023
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
description: "This article provides guidance on how to run 'What-If' analysis on Version Storage Report File."

---

# Tutorial: Run ‘What-If’ analysis on Version Storage Report File (Preview)

In this tutorial, we discuss how to:

- Run impact analysis of Automatic setting.
- Run impact analysis of Manual Expiration.
- Run impact analysis of Manual Count limits.

Download the report file to your local computer and use the provided scripts to apply the desired setting to the file - Automatic, Manual Expiration Limits or Manual with Count Limits Only. If needed, you could use PowerShell and Excel examples to understand the impact of the selected setting on version storage or impacted users.

**Example: Apply Automatic Trim Setting**

- Here's an example of PowerShell script you could apply to generate a What-If Report file that applies the **Automatic Expiration**  policy on the report file `C:\Report.csv`.  

:::image type="content" source="media/version-history/expiration-automation.png" lightbox="media/version-history/expiration-automation.png" alt-text="expiration automation":::

**Example: Apply Manual Expiration**

- Here's an example of PowerShell script to generate a What-If Report file. It applies **Manual Expiration** with expire-after days set to **30** on the report file `C:\Report.csv`.  

:::image type="content" source="media/version-history/manual-expiration.png" lightbox="media/version-history/manual-expiration.png" alt-text="manual expiration":::

**Example: Apply Manual Count Limits**

- Here's an example of PowerShell script to generate a What-If Report file, It applies a **Manual with Count Limits** policy with major version limit set to **50** on the report file `C:\Report.csv`.

:::image type="content" source="media/version-history/manual-with-count-limits-a.png" lightbox="media/version-history/manual-with-count-limits-a.png alt-text="manual with count limits-a":::

:::image type="content" source="media/version-history/manual-with-count-limits-b.png" lightbox="media/version-history/manual-with-count-limits-a.png alt-text="manual with count limits-b":::