---
ms.date: 06/04/2024
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
description: "In this article, you'll learn about reports that can help you govern access to data in SharePoint."
---

# Data access governance reports for SharePoint sites

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

As sprawl and oversharing of SharePoint sites increase with exponential data growth, organizations need help to govern their data. Data access governance reports provide info that helps you govern access to SharePoint data. The reports let you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply appropriate security and compliance policies.

## Requirements

This feature requires either Microsoft 365 E5 or Microsoft SharePoint Premium - SharePoint Advanced Management.

While admins with Microsoft 365 E5 licensing can access Data access governance reporting, they are not able to view or utilize the other [SharePoint Advanced Management features](advanced-management.md).


## Access the reports in the SharePoint admin center

1. Go to the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.
2. In the left pane, select **Reports** > **Data access governance**. The following reports are currently available:

   - Sharing links
   - Sensitivity labels applied to files
   - Content shared with 'Everyone except external users'

      :::image type="content" source="media/data-access-governance/dag-landing-page.jpeg" alt-text="dag reports landing page":::

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

Note that the reports don't include OneDrive data.

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

## Content shared with 'Everyone except external users' reports

Everyone except external users (EEEU) is a built-in group that represents the entire organization without any external guests. It's used in following scenarios where content needs to be visible to the entire organization.

1. 'Public sites' - When a site should be publicly visible to the entire organization - 'Everyone except external users' (EEEU) group is part of the site membership,  i.e., site owners/visitors/members.
2. 'Public items' - You can pick EEEU in the people picker to share a particular item (file/folder) and then that item is visible to the entire organization.

Now organizations can discover potential oversharing occurring via EEEU using the new Data access Governance (DAG) report that captures the above mentioned events in the last 28 days.

### Create eeeu reports

When creating a report, you can choose various options, to create focused reports or filter later within the report.

:::image type="content" source="media/data-access-governance/eeeu-addreport.png" alt-text="create an everyone except external users report":::

- Report name: Provide a unique name for the report.
- Template: Lists categories of SharePoint site templates (Classic sites, Communication sites, Team sites, others). You can choose multiple values or 'All sites'.
- Privacy: Applicable for Team sites in the scope. You can select 'Private', 'Public' or 'All'.
- Site sensitivity: Lists all sensitivity labels. Select one or many labels if you want to report to run within the scope of labeled sites. For eg: 'Identify files within sites labeled as 'Confidential', that were shared with EEEU in the last 28 days.
- Report type: Use this to select the scenario to be considered for this report, as discussed above,  i.e., whether you want a report for recent 'public sites' or for recent 'public items'.

### Run eeeu reports

To get the latest data for a report, run the report. You can run all reports or select individual reports to run. It might take a few hours for reports to run. To check if a report is ready or when it was last updated, see the **Status** column.

> [!NOTE]
> Each report can be run only once in 24 hours.

### View eeeu reports

Each EEEU report includes data as shown in the screenshot below

:::image type="content" source="media/data-access-governance/dag-eeeu-report.jpeg" alt-text="eeeu report details":::

- Up to 100 sites with highest number of items/groups shared with EEEU in the last 28 days.
- Policies applied to these sites – [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), site privacy and [site external sharing policy](external-sharing-overview.md).
- Primary admin for each site.

The reports don't include OneDrive data.

### Download eeeu reports

After you run a report, select it to download the data. In the report:

- The site with the most number of items/groups shared with EEEU appears first and the report includes up to 1 million such sites.
- Other site related information such as the primary admin, admin's email address, site template, privacy, sensitivity label etc.

## Limitations or known issues

- These reports work only if you have non-pseudonymized report data selected for your organization. To change this setting, you must be Global Administrator. Go to the [Reports setting in the Microsoft 365 admin center](https://admin.microsoft.com/#/Settings/Services/:/Settings/L1/Reports) and clear **Display concealed user, group, and site names in all reports**.
- Data in these reports might be delayed by up to 48 hours. In new tenants, it might take a few days for data to be available and for these reports to be generated successfully.

## Remedial actions from Data access governance reports

Once SharePoint admins run the Data access governance reports to discover potential oversharing, the next step is to take actions to remediate such risks. The decision should consider factors such as sensitivity of the content, how much is the exposure and disruption to existing status.

If immediate action needs to be taken, the SharePoint admin can configure [Restricted access control (RAC)](../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/restricted-access-control.md) and restrict access to a specified group (currently in preview). They can leverage the ['Change history' report](../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/change-history-report.md) to identify any recent changes by admins that could have lead to oversharing.

The SharePoint admin may also want to consult the site owner(s), whose sites are listed in DAG reports, and ask them to review the permissions and take necessary actions. This is possible with 'Site access review' feature, from within DAG reports. Site owners can also view detailed information about the relevant oversharing scenario, as per the DAG report, and take necessary action and update the SharePoint admin.
