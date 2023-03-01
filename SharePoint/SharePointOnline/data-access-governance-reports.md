---
ms.date: 03/01/2023
title: "Data access governance insights for SharePoint sites"
ms.reviewer: karthig
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: "In this article, you'll learn about reports that can help you govern access to data in SharePoint."
---

# Data access governance insights for SharePoint sites

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

As security and compliance requirements increase across industries and the amount of business data grows exponentially, organizations need tools to help govern their data. Data access governance reports provide info that helps you govern access to SharePoint data. The reports help you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply appropriate security and compliance policies.

## Access the reports in the SharePoint admin center

1. Go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.
2. In the left pane, select **Reports** > **Data access governance**. The following reports are currently available:

   - Sharing links
   - Sensitivity labels applied to files
     :::image type="content" source="media/data-access-governance-screen.png" alt-text="Data access governance page":::
     
## Sharing links reports

The Sharing links reports help you identify potential oversharing by seeing the sites where users created the most new sharing links. A report is available for the following links:

- **"Anyone" links**: This report gives you a list of sites in which the highest number of Anyone links were created. These links let anyone access files and folders without signing in.
- **"People in the organization" links**: This report gives you a list of sites in which the highest number of “People in the organization” links were created. These links can be forwarded internally and let anyone in the organization access files and folders.
- **"Specific people" links shared externally**: This report gives you a list of sites in which the highest number of “specific people” links were created for people outside the organization.
:::image type="content" source="media/sharing-links-screen.png" alt-text="Sharing links page":::

### Run the reports

To get the latest data for a report, run the report. You can run all reports or select individual reports to run. It might take a few hours for reports to run. To check if a report is ready or when it was last updated, see the **Status** column.

> [!NOTE]
> Each report can be run only once in 24 hours.

### View the reports

When a report is ready, select it to view the data. Each sharing link report includes:

- Up to 100 sites with highest number of [sharing links](modern-experience-sharing-permissions.md) created in the last 30 days.
- The policies applied to these sites – [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).
- The primary admin for each site.
  :::image type="content" source="media/anyone-links-screen.png" alt-text="Report for Anyone links":::

### Download the reports

You can download a .csv file to get the same information for up to 10,000 sites. 

## Sensitivity labels for files reports

The "Sensitivity labels for files" reports help you control access to sensitive content by finding sites storing [Office files that have sensitivity labels applied](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files). You can review these sites to ensure the correct policies are applied.

### Add the reports

You can add a report for each sensitivity label you want to track. Adding a report runs it for the first time.  

> [!NOTE]
> You can add reports only for sensitivity labels with a scope that includes "File".

:::image type="content" source="media/sensitivity-labels-screen.png" alt-text="Add sensitivity label reports panel":::

### Run reports

To get the latest data for a report, run the report. You can run all reports or select individual reports to run. It might take a few hours for reports to run. To check if a report is ready or when it was last updated, see the **Status** column.

> [!NOTE]
> Each report can be run only once in 24 hours.

:::image type="content" source="media/sensitivity-labels-reports-link.png" alt-text="Reports for sites with files labeled Confidential and Highly confidential":::

### Download reports

After you run a report, select it to download the data. The report includes:

- Up to 10,000 sites with the highest number of [Office files that have sensitivity labels applied](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files).
- The policies applied on these sites - [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).
:::image type="content" source="media/details-screen.png" alt-text="Downloaded .csv file":::

## Limitations or known issues

- These reports work only if you have non-pseudonymized report data selected for your organization. To change this setting, you must be Global Administrator. Go to the [Reports setting in the Microsoft 365 admin center](https://admin.microsoft.com/#/Settings/Services/:/Settings/L1/Reports) and clear **Display concealed user, group, and site names in all reports**.
- Data in these reports might be delayed by up to 48 hours. In new tenants, it might take a few days for data to be available and for these reports to be generated successfully.
