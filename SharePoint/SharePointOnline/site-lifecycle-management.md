---
ms.date: 06/22/2023
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

The notifications inform SharePoint site owners a site has been inactive for an X number of months. If they want to keep the site, they should select the **Certify site** button found in the notification email.

If a site owner doesn't act after three consecutive email notifications, site lifecycle management withholds sending notifications for the next three instances (90 days) known as the **cool off period**. The site is then labeled as **unactioned**.

To summarize the possible outcomes, if a site owner:

- confirms a site is **active** via the notification email, the policy withholds further site inactivity notifications unless the site becomes inactive again.
- takes no action after three consecutive email notifications, the cool off period begins and the site is considered **unactioned**.

#### Cool off period

Notifications are withheld for 90 days during the cool off period. Once the period ends, notifications restart if the site is still inactive.

#### Unactioned sites

Unactioned sites appear in the policy execution report as **Unactioned by Site Owner** during the cool off period. You can download the policy execution report and filter out sites marked **Unactioned by Site Owner**.

## Types of inactive site policies

When configuring a site lifecycle policy, you can choose to create either a **simulation policy** or an **active policy**.

- A simulation policy runs once and generates a report based on configured parameters. A simulation policy can be converted to an active policy.

- An active policy runs monthly, generates reports and sends notifications to respective owners asking them to attest their detected inactive site.

### Configurable parameters for inactive site policies

Site lifecycle management lets you configure several key parameters for an inactive site policy like:

- period of inactivity
- types of site templates
- site creation source
- sensitivity labels
- and exclusion of up to 100 sites

### Out-of-scope sites

The following sites are considered out-of-scope and excluded from an inactive site policy:

- ownerless sites
- OneDrive sites
- sites with retention policies applied

## Create an inactive site policy

1. To create an inactive site policy, go to the **SharePoint admin center**.

2. Expand **Policies** and select **Site lifecycle management**.

3. Select **+ Create policy** and select **Next**.:::image type="content" source="media/Site lifecycle management/2-inactive-site-policy-create-policy.png" alt-text="screenshot of site lifecycle management create a new policy" lightbox="media/Site lifecycle management/2-inactive-site-policy-create-policy.png":::

4. Enter your policy scope parameters and select **Next**. During this step, you can:

- set how long since the last site activity before a site is considered inactive
- filter by site creation source
- filter by sensitivity label
- exclude specific sites from the policy :::image type="content" source="media/Site lifecycle management/4-inactive-site-policy-create-policy-set-scope-filled.png" alt-text="screenshot of site lifecycle management set policy scope" lightbox="media/Site lifecycle management/4-inactive-site-policy-create-policy-set-scope-filled.png":::

5. Name your policy, add a description (optional) and select a policy mode. Select **Next**.:::image type="content" source="media/Site lifecycle management/5-inactive-site-policy-name-policy.png" alt-text="screenshot of site lifecycle management name policy" lightbox="media/Site lifecycle management/5-inactive-site-policy-name-policy.png":::

6. Select **Done**. Your policy is now created and can be viewed and managed from the **Site lifecycle management** dashboard.:::image type="content" source="media/Site lifecycle management/6-inactive-site-policy-finish.png" alt-text="screenshot of site lifecycle management create scope finished" lightbox="media/Site lifecycle management/6-inactive-site-policy-finish.png":::

## Reporting

Inactive sites detected during the cool off period are shown in the policy execution report. The report is available for download as a .csv file. and also lets you filter out sites that are considered unactioned by site owners. :::image type="content" source="media/Site lifecycle management/8-inactive-site-policy-downloaded-csv-report.png" alt-text="screenshot of inactive site policy downloaded csv report" lightbox="media/Site lifecycle management/8-inactive-site-policy-downloaded-csv-report.png":::

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)

[Restore deleted sites](restore-deleted-site-collection.md)
