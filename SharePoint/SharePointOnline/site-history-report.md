---
ms.date: 05/01/2023
title: "Create and view SharePoint site change history reports"
ms.reviewer: cvelaga
manager: serdars
recommendations: true
ms.author: mactra
author: MachelleTranMSFT
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- M365-collaboration
- Highpri
- Tier1
description: "Learn how to create and view SharePoint site change history reports in SharePoint admin center."
---

# Create and view SharePoint site change history reports

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can create change history reports in the SharePoint admin center to review SharePoint site property changes made within the last 180 days.

Create up to five reports for a given date range and filter by sites and users. You can download the report as a .csv file to view the site property changes.

> [!TIP]
> You can export data for up to 180 days with a change history report depending on the user license. The report may contain data for users that go back 180 days as well as data for others that don’t. Since the type of user license isn’t shown on the report, it may appear as if data is missing for some users.

> [!NOTE]
> Admins assigned the global reader role do not have the permissions to create or delete a report but can download to review the changes.

## Requirements

To access and use this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## Create a change history report

1. To create a change history report, go to the **Change history** page and select **Create new report**.  

2. A panel appears on the right where you can specify the type of information you want to include in your change history report. Select **Create report** to generate a new report.

3. The new report is listed on the Change history page. Select the report to open the change history report panel and monitor its status.

4. Once the report is created, select **Download report** to export the data as a .csv file. The **Create a copy** button allows you to create more reports with similar parameters.

> [!NOTE]
> The report will take hours to generate depending on the search criteria selected when creating the report.

## View a change history report

To view change history reports, expand **Reports** and select **Change history**.

You can create new reports, delete, and refresh their statuses from the change history page. This page will only show five reports at a time. The best practice is to delete a previous report before creating a new one.

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)
