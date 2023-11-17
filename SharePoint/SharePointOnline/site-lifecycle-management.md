---
ms.date: 08/30/2023
title: "Manage site lifecycle policies"
ms.reviewer: nvasudevan
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
- Highpri
- Tier1
- M365-sam
- M365-collaboration
search.appverid:
description: "Learn how to manage site lifecycle policies for SharePoint sites."
---

# Manage site lifecycle policies

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

> [!NOTE]
> This feature is currently rolling out and may not yet be fully available for all organizations.

## Site lifecycle management

The site lifecycle management feature from Microsoft Syntex- SharePoint Advanced Management lets you manage inactive sites across your tenant from the [SharePoint admin center](get-started-new-admin-center.md).

You can set up an inactive site policy to automatically detect inactive sites and send notifications to site owners via email. The owners can then confirm whether the site is still active. When you're setting up a site lifecycle policy, you can choose between a simulation policy and an active policy. The simulation policy runs once and generates a report based on the parameters you've set. If the policy fails, you need to delete it and create a new simulation policy. You can also convert a simulation policy to an active policy.

The active policy runs monthly and generates reports, sending notifications to the respective site owners to confirm the inactive site's status. If the active policy fails during a particular month, it will run again on the next schedule.

:::image type="content" source="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png" alt-text="screenshot of site lifecycle management dashboard" lightbox="media/site-lifecycle-management/1-inactive-site-policy-dashboard.png":::

### Site owner notifications

The notifications inform SharePoint site owners that a site has been inactive for X months. To keep the site, the owner should select the **Certify site** button in the notification email. Once the owner certifies the site as active, site lifecycle management doesn't check the activity of the confirmed site for one year.

Site owners are notified monthly for thee months and then no notifications are sent for the next three months. After six months, monthly notifications resume if the site is inactive. The policy execution report lists the inactive site as unactioned by site owner. You can download the policy execution report and filter out sites that are marked as "no owner action."

> [!TIP]
> Before creating an inactive site policy, check for any site access restriction policies that could disrupt site attestation by the respective site owner.

### Sites managed by multiple inactive site policies

If a site falls under multiple inactive site policies, notification emails aren't repeated. If a notification was sent within the last 30 days from any inactive site policy, the site remains inactive, and no more notifications are sent. The policy execution report shows the site's status as "Notified by another policy."

## Requirements

Site lifecycle management requires [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md).

## Create an inactive site policy

1. To create an inactive site policy, go to the SharePoint admin center.

1. Expand **Policies** and select **Site lifecycle management**.

1. Select **+ Create policy** and select **Next**.

1. Enter your policy scope parameters and select **Next**. :::image type="content" source="media/site-lifecycle-management/4-inactive-site-policy-create-policy-set-scope-filled.png" alt-text="screenshot of site lifecycle management set policy scope." lightbox="media/site-lifecycle-management/4-inactive-site-policy-create-policy-set-scope-filled.png":::

1. Name your policy, add a description (optional) and select a policy mode. Select **Next**.:::image type="content" source="media/site-lifecycle-management/5-inactive-site-policy-name-policy.png" alt-text="screenshot of site lifecycle management name policy." lightbox="media/site-lifecycle-management/5-inactive-site-policy-name-policy.png":::

1. Select **Done**. Your policy is now created and can be viewed and managed from the **Site lifecycle management** dashboard.

## Scope of inactive site policies

You can configure parameters for an inactive site policy like inactive time period, template type, site creation source, sensitivity labels and exclusion of up to 100 sites.

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

- Ownerless sites
- OneDrive sites
- Sites with retention policies applied
- Sites with other compliance policies applied
- Locked sites
- Sites created by system users
- App catalog sites
- Root sites
- Home sites
- Tenant admin sites

## Reporting

Sites that have been inactive for six months are listed in the policy execution report. The report is available for download as a .csv file and lets you filter out sites that are considered unactioned by site owners. :::image type="content" source="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png" alt-text="screenshot of inactive site policy downloaded csv report." lightbox="media/site-lifecycle-management/8-inactive-site-policy-downloaded-csv-report.png":::

The following describes the information included in the policy execution report:

|Column  | Definition  |
|---------|---------|
|**Site name**     |Name of inactive site         |
|**URL**     |URL of inactive site         |
|**Template**     |Template of inactive site         |
|**Sensitivity label**     |Sensitivity label of inactive site       |
|**Site owner emails**     |Email addresses of site owners who have received inactive site activity email notifications           |
|**Last site activity**     |Date of last activity detected by inactive site policy across SharePoint site and connected workloads (Exchange, Viva Engage (formerly Yammer), or Teams)         |
|**Date created**     |Date when the inactive site was created         |
|**Storage used**     |Storage consumed by inactive site    |
**Inactive site status**     |Stage of the policy with the inactive site. There are four possible stages:|
| |**First notification**: The first notification has been shared with the site owner of the inactive site.|
| |**30 days since first notification**: The second notification has been shared with the site owner of the inactive site.|
| |**60 days since first notification**: The third notification has been shared with the site owner of the inactive site.|
| |**No owner action**: No action the site owner after three consecutive notifications.|
|**Action status**     |Status of the notification to the site owner:         |
| |**Success** denotes the notification was delivered to the site owner.|
| |**Failure** denotes the notification to the site owner has failed.|

## Related articles

[Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)

[Restore deleted sites](restore-deleted-site-collection.md)
