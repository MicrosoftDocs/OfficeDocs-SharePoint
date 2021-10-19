---
title: "Data access governance reports"
ms.reviewer: 
ms.author: v-smandalika
author: v-smandalika
manager: dansimp
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
search.appverid: MET150
description: "In this article, you'll learn about governing data access in SharePoint and OneDrive."
---

# Data Access Governance in SharePoint and OneDrive

**Overview**

With growing security- and compliance-related implications across industries and with faster growth of business data, organizations must have the right tools to govern data stored in OneDrive and SharePoint. Data Access Governance reports give insights into how you can govern data access in SharePoint sites.
The reports help you discover sites containing heavily shared content and sensitive content. You can use these reports to govern these sites for right security and compliance policies.

> [!NOTE]
> 1. This feature is defined and governed by Microsoft online services terms.
> 2. This feature will be available with E5 licenses when we announce general availability.

## Access Data Access Governance Reports feature

You can access the Data Access Governance Reports feature from the SharePoint admin center portal.

Perform the following steps:

1. Log in to the SharePoint admin center portal.
1. On the left navigation pane of the home screen, choose **Reports > Data access governance**.
   The **Data access governance** screen appears, and it displays the following reports:

    - Sharing links
    - Sensitivity labels applied to files

1. Click **View reports** under the **Sharing links** pane or the **Sensitivity labels applied to files** pane.

For more information, see [Sharing links reports](#sharing-links-reports) and Sensitivity labels for files reports.

## Sharing links reports

The "Sharing links" reports help identify potential oversharing by reviewing sites at which users created new sharing links. You have three different reports, each mapped to three different types of links the users can generate to share a file or folder in SharePoint.

- **"Anyone" links**: This report gives you a list of sites in which the highest number of “Anyone” links were created. These links let anyone access files and folders without signing in.
- **"People in the organization" links**: This report gives you a list of sites in which the highest number of “People in the organization” links were created. These links can be forwarded internally and let anyone in the organization access files and folders.
- **"Specific people" links (shared externally)**: This report gives you a list of sites in which the highest number of “specific people” links were created for people outside the organization.

### Run the reports

To get the latest data for a report, run the report. You can choose to run all reports or select individual reports and run them. Once a report-run process starts, it might take a few hours for it to complete. You can track the status of the report to see if it is running or check when it was last updated.

> [!NOTE]
> Each report can be made to run only once in 24 hours.

### View the reports

Once a report is run and updated, you can click the report's link to view the data.
The resultant screen provides you:

1. The top 100 sites with highest number of [sharing links](modern-experience-sharing-permissions.md) created in the last 30 days as of report updated date.
1. Information on the policies applied on these sites – [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).
1. Details of the administrators for these sites.

### Download the reports

You can further download a detailed CSV report to get the same view of top 10,000 sites, sorted in decreasing order of the number of sharing links created in the last 30 days.

## Sensitivity labels for files reports

The "Sensitivity labels for files" reports help you control access to sensitive content by finding sites in which [sensitivity labelled files](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files) are stored. You can review these sites for verify for the right policies applied.

### Add and run the reports

You can add one report for every sensitivity label you want to track. Once a report is added, the run-process might take a few hours to complete.

> [!NOTE]
> You can add and run the reports on only those sensitivity labels whose scope includes "File".

### Run reports

To get the latest data for an added report, run the added report. You can choose to run all reports or select individual reports and run them. Once the report-run process starts, it might take a few hours for it to complete. You can track the status of the report to see if it is running or check when it was last updated.

> [!NOTE]
> Each report can be made to run only once in 24 hours.

### Download reports

Once a report is run and updated, you can click the report's link to download it.
The resultant screen provides you:

1. Top 10,000 sites, sorted in decreasing order of the number of specific [sensitivity labelled files](/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files) present in the sites.
1. Information on the policies applied on these sites - [site sensitivity](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites), [site unmanaged device policy](control-access-from-unmanaged-devices.md), and [site external sharing policy](external-sharing-overview.md).

## Limitations or known issues

1. **Issue**: Site ID, Site URL, and primary administrators' details are hidden or pseudonymized by default.
    - Microsoft has made a privacy change, as part of privacy commitment, to pseudonymize user-level information by default in all our reports. For you to get non- pseudonymized data in DAG reports, review this policy change and update this setting as per your organization’s needs.
        - **Policy change**: [Privacy changes to Microsoft 365 Usage Analytics - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-365-blog/privacy-changes-to-microsoft-365-usage-analytics/ba-p/2694137)
        - **Settings to be reviewed and updated**: Global administrators can revert this change for their tenant and show identifiable user information if their organization’s privacy practices allow. This data rollback can be achieved in the Microsoft 365 admin center in the path **Settings > Org Settings > Services and selecting Reports**. Under **Choose how to show user information**, select **Show identifiable user information** in **Reports**. Showing identifiable user information is a logged event in the Microsoft 365 compliance center audit log.
        
1. Data in these reports could be delayed by 48 hours (maximum).

## Support

If you are facing any issues or have any feedback, please reach out to **dag_feedback@microsoft.com**.




