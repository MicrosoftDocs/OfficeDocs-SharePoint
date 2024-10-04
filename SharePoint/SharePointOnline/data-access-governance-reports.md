---
ms.date: 10/02/2024
title: "Data access governance reports for SharePoint sites"
ms.reviewer: samust
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: "In this article, you learn about reports that can help you govern access to data in SharePoint."
---

# Data access governance reports for SharePoint sites

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

As sprawl and oversharing of SharePoint sites increase with exponential data growth, organizations need help with governing their data. Data access governance reports can help you govern access to SharePoint data. The reports let you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply the appropriate security and compliance policies.

## Requirements

This feature requires either Microsoft 365 E5 or Microsoft SharePoint Premium - SharePoint Advanced Management.

> [!NOTE]
> IT administrators with Microsoft 365 E5 licensing can access Data access governance reporting, but are unable to view or utilize the other [SharePoint Advanced Management features](advanced-management.md).

## Access the reports in the SharePoint admin center

1. As an [administrator](sharepoint-admin-role.md), sign in to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) for your organization.
2. In the left pane, select **Reports** and then select **Data access governance**.

    The following reports are currently available from the Data access governance landing page:

   - Sharing links
   - Sensitivity labels applied to files
   - Shared with 'Everyone except external users'
     :::image type="content" source="media/data-access-governance/dag-landing-page.png" alt-text="Screenshot that shows data access governance dashboard." lightbox="media/data-access-governance/dag-landing-page.png":::

## Sharing links reports

Sharing links reports lets you identify potential sources of oversharing by showing the sites where users created the most new sharing links. A report is available for the following links:

|Name of report|Description|
|---|---|
|**"Anyone" links**| This report provides a list of sites in which the highest number of "Anyone" links were created. "Anyone" links allow anyone to access files and folders without signing in.|
|**"People in the organization" links**| This report provides a list of sites in which the highest number of "People in the organization" links were created. These links can be forwarded internally and allow anyone in the organization to access files and folders.|
|**"Specific people" links shared externally**| This report provides a list of sites in which the highest number of "Specific people" links were created for people outside the organization.|

:::image type="content" source="media/sharing-links-screen.png" alt-text="Sharing links page":::

### Run the reports

To get the latest data for each report, manually run the Data access governance report. You can run all reports or select individual reports to run. It can take a few hours for reports to fully generate. To check if a report is ready or to see when it was last updated, see the **Status** column.

> [!NOTE]
> Each report can be run only once in 24 hours.

### View the reports

When a report is ready, select the name of the report to view the data. Each sharing link report includes:

- Up to 100 sites with highest number of [sharing links](modern-experience-sharing-permissions.md) created in the last 30 days.
- The types of policies applied to the sites – [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).
- The name of the primary administrator for each site.

> [!NOTE]
> The reports don't include OneDrive data.

### Download the reports

You can also download the reporting as a .csv file for up to 10,000 sites.

> [!IMPORTANT]
> You can download reporting for up to 1 million sites if you have a SharePoint SharePoint Premium - SharePoint Advanced Management license and your tenant is a non-government cloud environment.

## Sensitivity labels for files reports

The sensitivity labels for files report feature lets you control access to sensitive content by finding sites storing [Office files that have sensitivity labels applied](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files). You can review these sites to ensure the correct policies are applied.

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

After you run a report, select the report to download the data. The report includes:

- Up to 10,000 sites with the highest number of [Office files that have sensitivity labels applied](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files).
- The policies applied on the following sites - [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).

:::image type="content" source="media/details-screen.png" alt-text="Downloaded .csv file":::

## Content shared with 'Everyone except external users' (EEEU) reports

> [!IMPORTANT]
> This report is only available if you have a SharePoint Premium - SharePoint Advanced Management license and the tenant is a non-government cloud environment. The report is currently unavailable for government cloud environments such as GCCH/GCC-Moderate/DoD/Gallatin, even if you have a SharePoint Premium - SharePoint Advanced Management license.

Everyone except external users (EEEU) is part of a built-in group that represents the entire organization without any external guests. It's used in following scenarios where content needs to be visible to the entire organization:

- Public sites - The site is publicly visible to users within your entire organization - Everyone except external users (EEEU) group is part of the site membership,  that is, site owners/visitors/members.
- Public items - You can select EEEU in the people picker to share a particular item (file/folder) and then that item is visible to the entire organization.

Now organizations can discover potential oversharing occurring via EEEU using the new Data access governance (DAG) report that captures the above mentioned events in the last 28 days.

### Create Everyone except external users reports

When creating a report, you can select various options like create focused reports or filter later within the report.

:::image type="content" source="media/data-access-governance/eeeu-addreport.png" alt-text="Screenshot that shows create an everyone except external users report":::

- Report name: Provide a unique name for the report.
- Template: Lists categories of SharePoint site templates (Classic sites, Communication sites, Team sites, others). You can choose multiple values or 'All sites'.
- Privacy: Applicable for Team sites in the scope. You can select 'Private', 'Public' or 'All'.
- Site sensitivity: Lists all sensitivity labels. Select one or many labels if you want to report to run within the scope of labeled sites. For for example: 'Identify files within sites labeled as 'Confidential', that were shared with EEEU in the last 28 days.
- Report type: To select the scenario as discussed earlier, whether you want a report for recent 'public sites' or for recent 'public items'.

### Run Everyone except external users reports

To get the latest data for a report, run the report. You can run all reports or select individual reports to run. It might take a few hours for reports to run. To check if a report is ready or when it was last updated, see the **Status** column.

> [!NOTE]
> Each report can be run only once in 24 hours.

### View EEEU reports

Each EEEU report includes data as shown in the following screenshot:

:::image type="content" source="media/data-access-governance/dag-eeeu-report.png" alt-text="Screenshot that shows eeeu report details" lightbox="media/data-access-governance/dag-eeeu-report.png":::

- Up to 100 sites with highest number of items/groups shared with EEEU in the last 28 days.
- Policies applied to these sites – [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), site privacy, and [site external sharing policy](external-sharing-overview.md).
- Primary admin for each site.

> [!NOTE]
> The reports don't include OneDrive data

### Download Everyone except external users reports

After running the report, select the report to download the data. In the report:

- The site with the most number of items/groups shared with EEEU appears first and the report includes up to 1 million such sites.
- Other site related information such as the primary admin, admin's email address, site template, privacy, sensitivity label etc.

## Limitations or known issues

- Reports work if you have nonpseudonymized report data selected for your organization. To change this setting, you must be a Global Administrator. Go to the [Reports setting in the Microsoft 365 admin center](https://admin.microsoft.com/#/Settings/Services/:/Settings/L1/Reports) and clear **Display concealed user, group, and site names in all reports**.
- Report data can be delayed for up to 48 hours. In new tenants, it can take a few days for data to be generated successfully and available for viewing.

## Remedial actions from Data access governance reports

> [!IMPORTANT]
> Remedial actions from  Data access governance reports are only available for SharePoint Premium - SharePoint Advanced Management subscribers running non-government cloud environments. The feature is currently unavailable for government cloud environments such as GCCH/GCC-Moderate/DoD/Gallatin, even if you have a SharePoint Premium - SharePoint Advanced Management license.

Once you run the Data access governance reports to discover potential oversharing, the next step is to take actions to remediate such risks. We recommend considering factors like sensitivity of the content, amount of content exposed and disruption to existing status.

If immediate action needs to be taken, you can configure [Restricted access control (RAC)](./restricted-access-control.md) and restrict access to a specified group (currently in preview). You can also use the ['Change history' report](./change-history-report.md) to identify recent changes to site properties that could lead to oversharing.

You can also request the site owner review the permissions before taking necessary actions via [the Site access review feature](site-access-review.md) that is available within the Data access governance reports.
