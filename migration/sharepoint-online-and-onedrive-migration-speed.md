---
ms.date: 08/22/2023
title: "Migration performance guide for SharePoint & OneDrive"
ms.reviewer:
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-mar2020
search.appverid: MET150
description: "This article explains the factors that influence migration speed at each phase while using the SharePoint Migration API."
---

# General migration performance guidance

> [!IMPORTANT]
> Many Microsoft SharePoint and Microsoft OneDrive customers run business-critical applications against the service that run in the background. These include content migration, data loss prevention (DLP), and backup solutions.  
>
>We have implemented tighter throttling limits on background apps (migration, DLP and backup solutions) during weekday daytime hours. You should expect that these apps will achieve very limited throughput during these times.  However, **during evening and weekend hours** for the region, the service will be ready to process a significantly higher volume of requests from background apps.
>
> **Can Microsoft turn off the throttle to help me with migration?**  **No.** Throttling is in place to protect the reliability and availability of the service. Throttling rules cannot be disabled or suspended. Opening a support ticket will not lift throttle. See the [FAQ and Troubleshooting](#faq-and-troubleshooting) section for additional information.

## Performance guidance for Migration Manager and SPMT

When using either the SharePoint Migration Tool (SPMT) or running a Migration Manager agent, follow these guidelines to help improve your migration performance.

- [Improving the speed at which the source can be read](./spmt-performance-guidance.md#improving-the-speed-at-which-the-source-can-be-read)
- [Improving the migration computer speed](./spmt-performance-guidance.md#improving-the-migration-computer-speed)
- [Improving your connectivity to Office 365 and Azure](./spmt-performance-guidance.md#improving-your-connectivity-to-microsoft-365-and-azure)

## Performance guidance for the SharePoint Migration API

Migration performance can be impacted by network infrastructure, file size, migration time, and throttling. Understanding these will help you plan and maximize the efficiency of your migration. This guidance may also be applied to SPMT.

Currently, [SPMT](./introducing-the-sharepoint-migration-tool.md) and other third party vendor tools use the SharePoint API for migration. It leverages Azure and uses channels for large content transfer. Whatever migration tool you use, these factors apply. Follow the recommendations listed below for each phase of your migration process.

### Before migration

Planning is the key to optimizing your migration.  Determine what content you need to migrate, prioritize when the content needs to be migrated, and decide on what the optimal migration infrastructure should be.

#### I. Scan the source

The first rule of a good migration is to know your source; evaluate and triage your content before you migrate. What content really needs to be migrated? What can be left behind? How many file versions should be included? The amount of content you migrate will determine the overall size of your project.

#### II. Package the content

This step is where the tool creates a proper package for the content to be imported into the cloud. This step is automated in SPMT and in most third-party tools.

**Package size.** To improve migration throughput, we recommend that you package at least 250 files per transfer. For the transfer size, we recommend a minimum of 100 MB and less than 250 MB per package. Keeping within these guidelines result in a faster upload speed to Azure and leverages the scale capabilities of the migration API.

The following table provides estimates of the type of speed you may achieve based on the types of content you're migrating.

| Type of metadata | Examples | Maximum |
|:-----|:-----|:-----|
|Light|ISO files, video files |10 TB/day|
|Medium |List items, Office files (~1.5 MB)|1 TB/day|
|Heavy|List items with custom columns, small files (~50 kb)|250 GB /day|

- Large file size migrates faster than smaller ones. Small file size can result in larger overhead and processing time which directly impacts the performance.

- Files migrate faster than objects and list items.

The speed of this step depends on the efficiency of the tool you're using and the type of content that you package. Splitting your packages in a smart way is something that will greatly improve this step. In addition, ensure that your permissions, sharing, or other limits are set up properly for migration and are within [SharePoint limits and boundaries](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).

> [!NOTE]
> If you are planning to migrate over 100TB, review the following section, **Large Migration**.

### During migration

#### I. Upload to Azure

SPMT or your third-party tool will migrate your content into SharePoint using the Migration API, leveraging Azure as a temporary holding place.

If you have a good connection and can configure your datacenter, choose the same datacenter location closest geographically to you for your Azure and your Microsoft 365 account.
Migration data throughput is highest during off-peak hours, which are typically nights and weekends in your region's time zone. Your region's time zone is determined by where your SharePoint tenant is set up.

#### II. The Migration API

The final step of the migration process is when the data is moved from Azure to SharePoint. This action is transparent to the user when using SPMT or a third- party tool.

To improve throughput, users are encouraged to run parallel tasks against different site collections if possible. We recommend that you don't submit more than 5,000 migration jobs/requests at one time. Over-queuing the network creates an extra load on the database and slow migration down. Make sure your task has completed before you upload a new migration request. Some tools may already be doing this for you.

> [!IMPORTANT]
> We recommend that you do not have more than 5,000 migration jobs/requests **in the queue**. This number *does not* refer to the number of jobs *processing*.
>
> To learn more about processing performance, see [Avoid getting throttled or blocked in SharePoint Online](/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

During migration, it isn't uncommon for your migration task to be throttled. Throttling is implemented to ensure the best user experience and reliability of SharePoint. It's primarily used to load balance the database and can occur if you misconfigure migration settings, such as migrating all your content in a single task or attempting to migrate during peak hours.

For more technical background and information, please see:

- [Migration API Overview](/sharepoint/dev/apis/migration-api-overview)
- [Avoid getting throttled or blocked in SharePoint](/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)

### After migration

After the migration is completed, verify that your content has been successfully moved to SharePoint or OneDrive.

### Large migrations over 100 TB

> [!NOTE]
>
> This process should only be followed if you meet the following requirements:
>
> - The migration is occurring within the next 30 days.
> - The migration is over 100 TB of data.

If you're planning to migrate over 100 TB, submit a support request following the steps listed below. Make sure to include all requested information.

Follow these steps:

1. As an administrator, select the following link, which will populate a help query in the admin center: [SharePoint Migration over 100 TB](https://admin.microsoft.com/AdminPortal/?searchSolutions=SharePoint%20Migration%20over%20100TB)

2. At the bottom of the pane, select **Contact Support**, and then select **New Service Request**.

3. Leave **Description** blank.

4. Fill out the remaining info, and select **Contact me**.

5. After the ticket has been created, ensure you provide the support agent with the following information:
    - Estimated size of your migration.
    - An estimate of when you would like to start and complete your migration.
    - Where you're migrating your content from, such as SharePoint Server, Box, Google Workspace Drive, File shares, and so on.

## File share migration performance factors

Throughput for file share migration is impacted by multiple factors. The chart below shows the relationship between the number of agents and throughput. Data thus far indicates no obvious throughput drop when agent count increases.

Each user account has a certain quota for API call rate and bandwidth. Using multiple credentials mitigates throttling.

:::image type="content" source="media/mm-file-share-gb-hour-agent-performance.png" alt-text="file share gb performance":::

- Number of files in task - the more files, the higher the speed
- File size  - the larger the file size, the higher the speed
- The task count (Task count more than 10 times that of the agent count gains the maximum agent performance)
- The source computer disk performance
- The agent computer disk performance
- The RAM size of agent computer
- The number of consumers of the source computer
- Anti-virus competes the CPU and disk with agent
- Network speed
- Throttling - Decided by multiple factors including client side factors and server side factors. The throttling can be mitigated by using multiple SharePoint Online migration accounts.

According to our telemetry and support tickets, the typical bottleneck is from source reading. Primary reasons are:

- The source computer disk performance
- The agent computer disk performance
- The RAM size of agent computer
- The number of consumers of the source
- Anti-virus competes with the CPU and disk with agent
- Network speed


### FAQ and Troubleshooting

**Question: I am experiencing poor performance during migration.**

Answer: Check this article to help identify where the performance bottleneck is:  [Improve migration performance when using SPMT or Migration Manager.](./spmt-performance-guidance.md)

**Question:  I am experiencing throttling during migration.**

Answer:  First check the guidance in this document. Learn more at: [Avoid getting throttled or blocked in SharePoint.](/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)</br>For specific tools configuration or questions, please contact your third party tools vendor for more information.

**Question: I'm continually getting throttled while I am attempting to migrate. Can Microsoft turn off the throttle to help me with migration?**

Answer: Throttling is in place to protect the reliability and availability of the service. Throttling rules can't be disabled or suspended and **opening a support ticket will not lift throttle**. Refer to [Avoid getting throttled or blocked in SharePoint](/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online) for more information.

**Question: If you cannot turn off the throttle, what can I do if I am being throttled or experience poor performance?**

Answer:  Here are some quick self-help checks to consider:

- Try to migrate during off-peak business hours
- If you're experiencing slowness, make sure you aren't running any unnecessary software that may compete with migration resources.
- Check with your software provider to ensure you're migrating to SPO/OneDrive using *app-based authentication*.  Migration is a background task and shouldn't be run in user mode. If attempted to migrate in user mode, it can trigger larger than normal throttling.

**Question: My migration is blocked with consistent high volume of Http 503 errors ("Server Too Busy")?**

Answer: If you're experiencing a high volume of HTTP 503 responses blocking your migration **during evening and weekend hours**, follow the steps to create a support ticket.

Follow these steps:

1. As an administrator, select the following link, which will populate a help query in the admin center: [SharePoint Migration Throttle with 503](https://aka.ms/503MigrationThrottle).

2. At the bottom of the pane, select **Contact Support**, and then select **New Service Request**.

3. Leave **Description** blank.

4. After the ticket has been created, ensure you provide the support agent with the following information:
    - How much is left of your migration (x TB?).
    - Migration start and end date.
    - Describe where you're migrating your content from, such as SharePoint Server, Box, Google Workspace Drive, File shares, etc.
    - Estimate the number of throttles (for example, x throttle per hour?) and when (specific time and date) did the throttling happened.
    - Which migration tool you're using. For example, SPMT, ShareGate, Mover, etc.

**Question: When migrating OneNote notebooks that contain attachments from SharePoint 2010 to SharePoint Online, all attachments greater than 100 KB are missing.**

Answer: In SharePoint 2010, OneNote notebooks with attachments greater than 100 KB are put into a folder with a special content type that the SharePoint Migration Tool can't read.
As a workaround, you can migrate your SharePoint 2010 data to SharePoint 2016, then use the SharePoint Migration Tool to migrate the data from SharePoint 2016 to SharePoint Online.

### How to open a Microsoft support ticket for other migration issues

If you want to file a Microsoft support ticket, follow these steps and include the following information for any migration reason:


1. As an administrator, select the [SharePoint Migration Issue](https://admin.microsoft.com/AdminPortal/?searchSolutions=SharePoint%20Migration%20Issue) link, which will populate a help query in the admin center. 

2. At the bottom of the pane, select **Contact Support**, and then select **New Service Request**.

3. Leave **Description** blank.

4. Fill out the remaining info, and select **Contact me**.

5. After the ticket has been created, make sure to include the following information:

    - Your organization URL.
    - How much is left of your migration (x TB?).
    - Migration start and end date.
    - A description of where you're migrating your content from, such as SharePoint Server, Box, Google Workspace Drive, File shares, etc.
    - If it's a throttling related escalation, provide information such as the number of throttles, how many throttles per hour, and the specific time and date the throttling happened. If you're experiencing poor performance, please describe the nature of the poor performance.
    - Indicate which migration tool you're using (for example, SPMT, ShareGate, Mover, and so on).
    - State if you're logging in using *user login* or *app-based authentication*.


## Related articles

[Avoid getting throttled or blocked in SharePoint](/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)
