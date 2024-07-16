---
ms.date: 07/16/2024
title: "Site access review for data access governance reports"
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
description: "Learn about site access review as a remedial action available from Data access governance for SharePoint admins."
---

# Site access review for data access governance reports

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

Site access review in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) lets [IT administrators](/microsoft-365/admin/add-users/assign-admin-roles) delegate the review process of [data access governance reports](data-access-governance-reports.md) to site owners of overshared sites. This feature addresses limitations of data access governance reports, which generate lists of sites but lack detailed insights or solutions for oversharing scenarios.

## Prerequisites

To use the site access review feature, you must fulfill the following prerequisites:

- [Microsoft SharePoint Premium - SharePoint Advanced Management](advanced-management.md) subscription
- Admin credentials to access the SharePoint admin center

## Understanding site access review

Site access review addresses limitations in data access governance reports by involving site owners in the review process. This is crucial because:

- Data access reports provide site-level aggregation without file or item-level details due to compliance reasons.
- IT administrators can't view or investigate oversharing scenarios beyond site-level data.
- Site owners are best positioned to review and address oversharing issues in this scenario.

## How site access review works

- Site access review is accessible only for the top 100 data access governance reports.
- The review doesn't encompass the entire site context.
- Instead, a site access review specifically targets the oversharing scenario identified in the selected data access governance report.
- When you initiate a review, the system generates a context-specific email for the site owner.
- For instance, if you initiate a site access review for a report from the "Content shared with 'Everyone except external users'" category, the review email exclusively addresses sharing issues regarding that particular report.

> [!IMPORTANT]
> Currently, site access review is available only for "Content shared with 'Everyone except external users'" reports.

## Initiate a site access review for "Content shared with 'Everyone except external users'" reports

1. Sign in to SharePoint admin center with your admin credentials.
1. Expand the **Reports** section and select **Data access governance**.
1. Under "Content shared with 'Everyone except external users", select **View reports**.
1. Select a report and choose the sites you want to review.
    :::image type="content" source="./media/data-access-governance/initiate-site-access-review.png" alt-text="Initiate site access review for sites listed within DAG report":::
1. Select **Initiate site access review**.
1. Add comments in the provided section to give context to site owners.
    :::image type="content" source="./media/data-access-governance/comments-site-access-review.png" alt-text="Provide comments for context setting for site owners":::
1. Select **Send** to initiate the review request.

> [!TIP]
> You can track all initiated reviews in the "My review requests" tab on the data access governance landing page.

### Tracking initiated site access reviews

To see a list of all initiated site access reviews, select the **My review requests** tab from the data access governance landing page.

:::image type="content" source="./media/data-access-governance/my-review-requests.png" alt-text="Track all reviews initiated from a central page":::

When you initiate a site access review, it remains in a pending state until the site owner completes the review. Once the site owner completes the review, the status and comments are updated with the name of the reviewer and time and date of completion. A review can be marked as failed if site access review couldn't determine a valid email ID for the site owner to deliver the site access review.

### Site access review process (for site owners)

When you initiate a review, site owners receive an email for each site that requires attention. The email includes:

- Relevant title
- Your comments (if any)
- A request to review site permissions
- A link to a detailed access review page. This page is specific for the scenario as specified in the data access governance report.

:::image type="content" source="./media/data-access-governance/Email - EEEU files, folders and lists.png" alt-text="Email received by site owners for oversharing via EEEU":::

> [!NOTE]
> The link at the bottom of the email will change according to the type of data access governance report that site access review was initiated for. In the screenshot, the link says "View all EEEU claims" since the feature was initiated for a site from "Content shared with 'Everyone except external users' reporting.

#### Reviewing 'Everyone except external users' access (for site owners)

Site owners can review and manage access in two main areas:

- **SharePoint groups:**
  - View which groups contain 'Everyone except external users'
  - See when and by whom the group was added
  - Remove 'Everyone except external users' from groups if necessary:
    1. Selecting the SharePoint group opens the group membership page that displays all members of this SharePoint group.
    2. Select **Everyone except external users** and **Actions** and choose to **remove users from group**.

        :::image type="content" source="./media/data-access-governance/site-owner-view-foreeeu-files.png" alt-text="view for site owner regarding items shared with eeeu":::

- **Individual items (files/folders/lists):**
  - See items shared with 'Everyone except external users' in the last 28 days
  - View sharing details (who shared and when)
  - Manage access and remove permissions as needed:
    1. Select **Manage access**.
    1. Under the 'Everyone except external users' group in the **Groups** tab, select the group and select **remove access**. See [Stop sharing OneDrive or SharePoint files or folders, or change permissions](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323) for more information.

        :::image type="content" source="./media/data-access-governance/Manage-sharepoint-group-membership.png" alt-text="Displays sharepoint group members":::

#### Completing the review (for site owners)

Once the site owner takes the necessary actions like modifying or removing permissions, the site owner should:

1. Select **Complete review**.
2. Add any relevant comments
3. Submit the completed review

Comments are shared back to the IT administrator who raised the review request, and the review request is marked as Completed.

#### Managing multiple reviews (for site owners)

A site owner can receive review requests for multiple sites or multiple reviews for different scenarios at the same site. A site owner can track all requests by selecting the **Site reviews** page found in the left panel.

:::image type="content" source="./media/data-access-governance/site-review-master-page.png" alt-text="Master page to track all site review for a site":::

Here are the following ways a site owner can access the review page.

##### From email

The site review email provides a link to the detailed site review page. From the detailed site review page, the site owner can select **Site reviews** found in the left navigation panel.

##### From site settings

If the site owner lost the email, or closed the browser, they can return to the site review page by selecting the **Settings** or "gear" icon from the site's home page.

:::image type="content" source="./media/data-access-governance/site-review-from-gear-icon.png" alt-text="Path to site review page from site home page under gear icon":::

## Related topics

[Data access governance](data-access-governance-reports.md)

[Microsoft SharePoint Premium - SharePoint advanced management](advanced-management.md)
