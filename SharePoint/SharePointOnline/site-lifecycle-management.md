---
ms.date: 07/31/2023
title: "Manage site lifecycle policies"
ms.reviewer: nvasudevan
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
search.appverid:
description: "Learn how to manage site lifecycle policies for SharePoint sites."
---

# Manage site lifecycle policies

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

> [!NOTE]
> This feature is currently rolling out and may not yet be fully available for all organizations.

SharePoint sites are growing rapidly, and one of the major challenges faced by [SharePoint administrators](sharepoint-admin-role.md) is managing the lifecycle of the large number of sites.

The site lifecycle management feature from Microsoft Syntex- SharePoint Advanced Management lets you manage inactive sites across your tenant from the [SharePoint admin center](get-started-new-admin-center.md). :::image type="content" source="media/Site lifecycle management/1-inactive-site-policy-dashboard.png" alt-text="screenshot of site lifecycle management dashboard" lightbox="media/Site lifecycle management/1-inactive-site-policy-dashboard.png":::

## Requirements

To access and use this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## Site lifecycle management policies

You can create a policy that automates the detection of inactive sites and initiates a workflow that notifies site owners via email. Site owners can then confirm the active status of a site.

### Site owner notifications

The notifications inform SharePoint site owners a site has been inactive for an X number of months. If they want to keep the site, they should select the **Certify site** button found in the notification email. Once a site owner certifies a site as active, the site lifecycle management system wouldn't consider it inactive for one year.

> [!NOTE]
> When certifying a site, site owners may get a 403 error if tenant-level restricted access control settings are active, blocking site access. Before creating an inactive site policy, check for any such settings that could disrupt site attestation by the respective site owner.

If a site owner doesn't act after three consecutive email notifications, site lifecycle management withholds sending notifications for the next three instances (90 days) known as the **cool off period**. The site is then labeled as **unactioned**.

To summarize the possible outcomes, if a site owner:

- confirms a site is **active** via the notification email, the policy withholds further site inactivity notifications unless the site becomes inactive again after one year.
- takes no action after three consecutive email notifications, the cool off period begins and the site is considered **unactioned**.

#### Cool off period

Notifications are withheld for 90 days during the cool off period. Once the period ends, notifications restart if the site is still inactive.

#### Unactioned sites

Unactioned sites appear in the policy execution report as **Unactioned by Site Owner** during the cool off period. You can download the policy execution report and filter out sites marked **Unactioned by Site Owner**.

#### Sites managed by multiple inactive site policies

Admins can create up to five inactive site policies using site lifecycle management. Depending on the configured parameters, a site may come under the scope of multiple policies. In such cases, the system checks to avoid spamming site owners. If at least 30 days have passed since the last notification sent by any other policy, the site is still identified as inactive, but no additional notification is sent to the owner. The site's status in the policy execution report will be **Notified by another policy**.

## Create an inactive site policy

1. To create an inactive site policy, go to the **SharePoint admin center**.

2. Expand **Policies** and select **Site lifecycle management**.

3. Select **+ Create policy** and select **Next**.:::image type="content" source="media/Site lifecycle management/2-inactive-site-policy-create-policy.png" alt-text="screenshot of site lifecycle management create a new policy" lightbox="media/Site lifecycle management/2-inactive-site-policy-create-policy.png":::

4. Enter your policy scope parameters and select **Next**. :::image type="content" source="media/Site lifecycle management/4-inactive-site-policy-create-policy-set-scope-filled.png" alt-text="screenshot of site lifecycle management set policy scope" lightbox="media/Site lifecycle management/4-inactive-site-policy-create-policy-set-scope-filled.png":::

5. Name your policy, add a description (optional) and select a policy mode. Select **Next**.:::image type="content" source="media/Site lifecycle management/5-inactive-site-policy-name-policy.png" alt-text="screenshot of site lifecycle management name policy" lightbox="media/Site lifecycle management/5-inactive-site-policy-name-policy.png":::

6. Select **Done**. Your policy is now created and can be viewed and managed from the **Site lifecycle management** dashboard.:::image type="content" source="media/Site lifecycle management/6-inactive-site-policy-finish.png" alt-text="screenshot of site lifecycle management create scope finished" lightbox="media/Site lifecycle management/6-inactive-site-policy-finish.png":::

## Types of inactive site policies

When configuring a site lifecycle policy, you can choose between a **simulation policy** or an **active policy**.

- The **simulation policy** runs once and generates a report based on the configured parameters. If the policy fails, the admin should delete it and create a new simulation policy. A simulation policy can be converted to an active policy.

- The **active policy** runs monthly, generating reports and sending notifications to respective owners to attest their detected inactive site. If an active policy fails during a particular month, it will run again on the next schedule.

### Scope of inactive site policies

Site lifecycle management lets you configure several key parameters for an inactive site policy like:

- period of inactivity
- types of site templates
- site creation source
- sensitivity labels
- exclusion of up to 100 sites

#### In-scope site activity

Inactive site policies then analyzes activity across SharePoint, Teams, Viva Engage (formerly Yammer), and Exchange to determine when a site was last active:

**SharePoint**:

- files viewed
- files edited
- files shared internally and externally
- files synced
- pages viewed and visited
  
**Viva Engage (formerly Yammer)**:

- messages posted
- conversations read
- messages liked

**Teams** (all actions across shared, private, and public channels are analyzed):

- channel messages posted in a team across all channels
- posts in Teams and all channels
- replies to messages
- mentions in messages
- reactions to messages
- urgent messages sent
- meetings (recurring, ad hoc, one-time)

**Exchange**:

- emails received in the Exchange mailbox

> [!NOTE]
> Communication sites, classic sites, and Teams

### Out-of-scope site activity

The following sites are considered out-of-scope and excluded from an inactive site policy:

- ownerless site
- OneDrive site
- site with retention policies applied
- site with any other compliance policies applied
- locked site
- site created by system users
- app catalog site
- root site
- home site
- tenant admin site

## Reporting

Inactive sites detected during the cool off period are shown in the policy execution report. The report is available for download as a .csv file and also lets you filter out sites that are considered unactioned by site owners. :::image type="content" source="media/Site lifecycle management/8-inactive-site-policy-downloaded-csv-report.png" alt-text="screenshot of inactive site policy downloaded csv report" lightbox="media/Site lifecycle management/8-inactive-site-policy-downloaded-csv-report.png":::

See the following table which explains the reporting categories found in the policy execution report:

|Reporting category  | Meaning  |
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
| |**No owner action**: No action was taken by the site owner after three consecutive notifications.|
|**Action status**     |Status of the notification to the site owner:         |
| |**Success** denotes the notification was delivered to the site owner.|
| |**Failure** denotes the notification to the site owner has failed.|

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)

[Restore deleted sites](restore-deleted-site-collection.md)
