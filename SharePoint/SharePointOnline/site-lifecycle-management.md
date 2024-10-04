---
ms.date: 10/04/2024
title: "Manage site lifecycle policies"
ms.reviewer: nvasudevan
manager: jtremper
recommendations: true 
ms.author: mactra
author: MachelleTranMSFT
audience: Admin
f1.keywords: 
- NOCSH 
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection: 
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- essentials-manage
search.appverid:
description: "Learn how to manage site lifecycle policies for SharePoint sites."
---

# Manage site lifecycle policies

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Site lifecycle management

SharePoint sites are growing rapidly, and one of the major challenges faced by IT administrators is managing the lifecycle of the large number of sites.

The site lifecycle management feature from Microsoft SharePoint Premium - SharePoint Advanced Management lets you manage inactive sites across your tenant from the [SharePoint admin center](get-started-new-admin-center.md).

:::image type="content" source="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png" alt-text="screenshot of site lifecycle management dashboard" lightbox="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png":::

You can set up an inactive site policy to automatically detect inactive sites and send notifications to site owners via email. The owners can then confirm whether the site is still active. When you're setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. The simulation policy runs once and generates a report based on the parameters you set. If the policy fails, you need to delete it and create a new simulation policy. You can also convert a simulation policy to an active policy.

The active policy runs monthly and generates reports, sending notifications to the respective owners to confirm the inactive site status. If the active policy fails during a particular month, it will run again on the next schedule. The active policy takes an enforcement action on those inactive sites that haven't been certified by the site owner or admin. However this enforcement takes place only if the tenant admin configures the policy in that manner.

> [!NOTE]
> This feature is currently rolling out and may not yet be fully available for all organizations.

## Prerequisites

To access and use site lifecycle management, your organization must have the [Microsoft SharePoint Premium - SharePoint Advanced Management subscription](advanced-management.md).

## Create an inactive site policy

1. To create an inactive site policy, go to the SharePoint admin center.

1. Expand **Policies** and select **Site lifecycle management**.

1. Select **+ Create policy** and select **Next**.

1. Enter your policy scope parameters and select **Next**.

    :::image type="content" source="media/site-lifecycle-management/3-inactive-site-policy-create-policy-set-scope.png" alt-text="screenshot of site lifecycle management set policy scope." lightbox="media/site-lifecycle-management/3-inactive-site-policy-create-policy-set-scope.png":::

1. Beginning August 2024, you can configure the policy in the following ways:

    :::image type="content" source="media/site-lifecycle-management/4-inactive-site-policy-create-policy-set-scope-filled.png" alt-text="Screenshot of site lifecycle management set policy scope filled out." lightbox="media/site-lifecycle-management/4-inactive-site-policy-create-policy-set-scope-filled.png":::

    - Choose to send emails to site owners/admins
    - Choose to take the following enforcement actions when there's no response from site owners or site admins after 3 notifications:
        - Mark the inactive site as read-only
        - Mark the inactive site as read-only for a configurable duration (3, 6, 9 or 12 months) before archival.

        > [!NOTE]
        > Microsoft 365 Archive must be enabled from the Microsoft Admin Center before archival is available. To learn more about Microsoft 365 Archive, see [Overview of Microsoft 365 Archive](/microsoft-365/archive/archive-overview).

1. Name your policy, add a description (optional) and select a policy mode. 

1. Select **Next**.

    :::image type="content" source="media/site-lifecycle-management/5-inactive-site-policy-name-policy.png" alt-text="Screenshot of site lifecycle management name policy." lightbox="media/site-lifecycle-management/5-inactive-site-policy-name-policy.png":::

1. Select **Done**. Your policy is now created and can be viewed and managed from the Site lifecycle management dashboard.

### Site owner notifications

The notifications inform SharePoint site owners that a site is inactive for X months. To keep the site, the owner should select the **Certify site** button in the notification email. Once the owner certifies the site as active, site lifecycle management doesn't check the activity of the confirmed site for one year.

Site owners are notified monthly for three months and then no notifications are sent for the next three months. After six months, monthly notifications resume if the site is inactive. The policy execution report lists the inactive site as unactioned by site owner. You can download the policy execution report and filter out sites that are marked as "no owner action."

#### Automated enforcement actions

You or the tenant admin can configure the policy to take an automated enforcement action for unresponsive notification recipients. If site owners don't respond to the notification emails, additional notifications are sent informing the site owners or admins.

If you configure the policy to take an automated enforcement action when there's no response from the notification recipients, then additional notifications are sent to inform the site owners or admins.

##### Read-only sites

Site owners receive notification when the site goes into read-only mode.

Once the site is in read-only mode, the policy applies the read-only banner to the site until the site owner contacts you for removal.

You're able to remove the read-only mode for the site from the SharePoint admin center by following the following steps:

1. Expand **Sites** and select **Active sites**.
1. Select the site you want to manage and then select **Unlock**.

##### Archived sites

When a site is archived, a notification is sent to site owners.

To unarchive the site, the site owner must reach out to you and request site unarchival.

You can unarchive a site from the SharePoint admin center by following these steps:

1. Expand **Sites** and select **Archived sites**.
1. Select the site you want to manage and select **Unarchive site**.

> [!TIP]
> Before creating an inactive site policy, check for any site access restriction policies that could disrupt site attestation by the respective site owner.

### Sites managed by multiple inactive site policies

If a site falls under multiple inactive site policies, notification emails aren't repeated. If a notification was sent within the last 30 days from any inactive site policy, the site remains inactive, and no more notifications are sent. The policy execution report shows the site's status as "Notified by another policy."

## Scope of inactive site policies

You can configure parameters for an inactive site policy like inactive time period, template type, site creation source, sensitivity labels, and exclusion of up to 100 sites.

### Site activities

Inactive site policies analyze activity across SharePoint and connected platforms like Teams, Viva Engage (formerly Yammer), and Exchange to detect a site's last activity.

|Platform type | Activities  |
|---------|---------|
|**SharePoint**     |Viewed files, edited files, shared files internally and externally, synced files, viewed pages, visited pages          |
|**Viva Engage (formerly Yammer)**     |Posted messages, read conversations, liked messages         |
|**Teams**     |Posted channel messages in a team across all channels, posted messages in Teams and all channels, replied to messages, mentioned in messages, reacted to messages, sent urgent messages, conducted meetings (recurring, ad hoc, one-time)          |
|**Exchange**     | Received emails in the Exchange mailbox       |

### Site templates

Site lifecycle management also reviews activity of communication sites, classic sites, Teams-connected sites, and group-connected sites with the following site template types:

|Site type|Template type|
|---|---|
|Communication site|SitePagePublishing#0|
|Classic sites|STS#0, STS#1, STS#2, WIKI#0, BLOG#0, SGS#0, SPS#0, SPSNEWS#0, ENTERWIKI#0, COMMUNITY#0, DEV#0, EXPRESS#0, EHS#1, EHS#2|
|Teams-connected site|STS#3 or Group#0|
|Group-connected site|STS#3 or Group#0|

### Excluded sites

The following sites are excluded from site activity detection:

- OneDrive sites
- Sites with other compliance policies applied
- Locked sites
- Sites created by system users
- App catalog sites
- Root sites
- Home sites
- Tenant admin sites

## Reporting

Sites that have been inactive for six months are listed in the policy execution report. The report is available for download as a .csv file and lets you filter out sites that are considered unactioned by site owners. 

:::image type="content" source="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png" alt-text="screenshot of inactive site policy downloaded csv report." lightbox="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png":::

The following table describes the information included in the policy execution report:

|Column  | Definition  |
|---------|---------|
|**Site name**     |Name of inactive site         |
|**URL**     |URL of inactive site         |
|**Template**     |Template of inactive site         |
|**Sensitivity label**     |Sensitivity label of inactive site       |
|**Site owner emails**     |Email addresses of site owners receiving inactive site activity email notifications           |
|**Last site activity**     |Date of last activity detected by inactive site policy across SharePoint site and connected workloads (Exchange, Viva Engage (formerly Yammer), or Teams)         |
|**Date created**     |Date when the inactive site was created         |
|**Storage used**     |Storage consumed by inactive site    |
|**Action status**     |Current stage site is in: First/second/third notification sent, site put in read-only mode, site archived|

## Related articles

[Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)

[Restore deleted sites](restore-deleted-site-collection.md)
