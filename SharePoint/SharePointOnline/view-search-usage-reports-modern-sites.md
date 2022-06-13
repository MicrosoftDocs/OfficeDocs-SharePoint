---
title: "View search usage reports in modern sites"
ms.reviewer:
ms.author: v-lsaldanha
author: lovina-saldanha
manager: dansimp
recommendations: true
ms.date: 06/27/2021
audience: Admin
f1.keywords:
- CSH
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 479cfd6b-900b-46aa-b497-c13787771d3f
description: Learn how you can use search reports in the SharePoint admin center.
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
---

# View search usage reports in modern sites

If you're a SharePoint admin in your organization, you're probably asked questions about search usage, such as:

- What are the top queries on my site per day or per month?
- How many search queries are users performing on average?
- Which queries are getting low clicks as they're not showing up in any results?
- How often are query rules firing and how often are people clicking promoted results?

This article describes how you can use search reports in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> to find answers to these questions.

## To view a report

To view search usage reports in modern sites, navigate to **Site settings** > **Site collection administration** > **Microsoft Search** > **Configure search settings** > **Insights**.

Modern search usage reports with Microsoft Search provide a few graphs and tables generated from searches that are executed from search in modern sites. You can see data from the past 31 days (about one month), per day, or monthly for the previous year.

The first date picker lets you pick past 31 days (about one month) or past 12 months for the first two graphs. The second date picker lets you select a particular day or month for the bottom three tables (top, abandoned, no results). Downloading a report will allow you to see reports from a broader range of time. Click on the download arrow and select past 31 days (about one month) or past 12 months. The report is downloaded as an Excel spreadsheet. If you selected the past 31 days (about one month), the spreadsheet will have an individual tab for each day. The past 12 months download will have a tab for each month.

:::image type="content" source="media/view-search-usage-reports-1.png" alt-text="view usage reports." lightbox="media/view-search-usage-reports-1.png":::

## Overview of search reports

|Report|Description|
|---|---|
|Query Volume|This report shows the number of search queries performed. Use this report to identify search query volume trends and to determine periods of high and low search activity.|
|Top Queries|This report shows the most popular search queries. A query is added to this report when it's searched at least three times with a click on a result. Use this report to understand what types of information your users are searching for.|
|Abandoned Queries|This report shows popular search queries that receive low click-through. Use this report to identify search queries that might create user dissatisfaction and to improve the finding of content.|
|No Results Queries|This report shows popular search queries that returned no results. Use this report to identify search queries that might create user dissatisfaction and to improve the finding of content.|
|Impression distribution|This report shows impressions over various time frames. The timeline shows the daily number of impressions for a result type. Determine which result type is most frequently, or infrequently, used. Use this report to understand what result types users are using and any changes in user behavior over a period of time.|

## Related topics

[Microsoft 365 Reports in the Admin Center - SharePoint site usage](/microsoft-365/admin/activity-reports/sharepoint-site-usage-ww?view=o365-worldwide&preserve-view=true)

[Microsoft 365 Reports in the Admin Center - SharePoint activity](/microsoft-365/admin/activity-reports/sharepoint-activity-ww?view=o365-worldwide&preserve-view=true)
