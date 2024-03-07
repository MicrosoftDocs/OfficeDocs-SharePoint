---
ms.date: 03/07/2024
title: "Create change history reports for SharePoint sites"
ms.reviewer: daminasy
manager: jtremper
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

# Create change history reports for SharePoint sites

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can create custom change history reports in the [SharePoint admin center](get-started-new-admin-center.md) to review CSV reports of site actions or organization setting changes made within the last 180 days.

Change history reports can increase visibility and let you monitor changes made to the SharePoint configuration across various levels of your organization.

Create up to 10 reports that tracks what changed, when it happened, and who initiated the change across the site and organization settings.

:::image type="content" source="media/change-history/1-change-history-dashboard.png" alt-text="screenshot of change history report dashboard.":::

## Requirements

To access and use this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## Create a change history report

1. To create a change history report, go to the **Change history** page and select **New report**.

2. Choose the type of report you want to generate and select **Site settings/Organization settings**.

3. A panel appears where you can specify the type of information you want to include in your change history report. Select **Create report** to generate a new report.

4. The new report is listed on the change history page. Select the report to open the change history report panel and monitor its status.

5. Once the report is created, select **Download report** to export the data as a CSV file. The **Create a copy** button allows you to create more reports with similar parameters.

> [!NOTE]
> The report will take a few hours to generate depending on the search criteria selected when creating the report.

## View a change history report

To view change history reports, expand **Reports** and select **Change history**.

You can create new reports, delete, and refresh their statuses from the change history page. This page can only show 10 reports at a time. The best practice is to delete a previous report before creating a new one.

:::image type="content" source="media/change-history/2-change-history-dashboard-panel-expanded.png" alt-text="screenshot of change history dashboard with a prefilled new report panel":::

## Reporting

### Site settings report

Generate a site settings report for a given date range and filter by sites and users. You can download the report as a CSV file to view the site property changes. All site actions performed by Site administrators, Global administrators, and SharePoint administrators are captured in the report.

### Organization Settings Report (preview)

> [!NOTE]
> Organization settings reports are in public preview. A table listing trackable organization settings is included in this article.

You can also generate an organization settings report tracking changes made to organization settings from the SharePoint Admin Center. You can generate these reports for custom date ranges while filtering for specific users of interest. A best practice is to review the downloaded reports to ensure there are no deviations in settings from the desired state.

> [!TIP]
> You can export data for up to 180 days with a change history report depending on the user license. The report may contain data for users that go back 180 days as well as data for others that don’t. Since the type of user license isn’t shown on the report, it may appear as if data is missing for some users.

> [!NOTE]
> Admins assigned the [global reader role](/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide&preserve-view=true%3Do365-worldwide) do not have the permissions to create or delete a report, but can download to review the changes.

### Audited settings (preview)

Any changes made to the following tenant settings are reflected in the reports. We're continuously working to bring more settings under the ambit of these reports.

#### Organization settings

The table lists the latest set of supported settings found under the **Settings** node:

|Name|Description|
|---|---|
|**SharePoint Pages**|Allow commenting on modern pages|
|**SharePoint Site creation**|Users can create SharePoint site|
||Create teams sites under|
|| Default time zone|
|**OneDrive Sync**|Show Sync button on the OneDrive website|
|**SharePoint Version history limits**|Set version history limits|

#### Access control settings

The table lists the latest set of supported settings found in **Policies** under the **Access control** node:

|Name|Description|
|---|---|
|**Unmanaged devices**|Restrict access from devices that aren’t compliant or joined to a domain|
|**Idle session sign out**|Automatically sign out users from inactive browser sessions|
|**Network location**|Allow access only from specific IP addresses|
|**Apps that don't use modern authentication**|Block access from Office 2010 and other apps that can't enforce device-based restrictions|
|**OneDrive access restriction**|Restrict access to OneDrive content by security group|

#### Sharing settings

The table lists the latest set of supported settings found in **Policies** under the **Sharing** node:

|Name|Description|
|---|---|
|**External Sharing**|Content can be shared with, more external sharing settings|
|**File and folder settings**|Choose the type of link selected by default when users share files and folders in SharePoint and OneDrive|
||Choose the permission selected by default for sharing links|
||Choose who can access files with the URL to a file copied from the browser address bar|

## Related topics

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)
