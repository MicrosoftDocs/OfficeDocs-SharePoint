---
ms.date: 10/02/2024
title: "Initiate site access reviews for data access governance reports"
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
description: "Learn about how to initiate site access reviews as a remedial action for data access governance for SharePoint sites."
---

# Initiate site access reviews for data access governance reports

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

Site access review in the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219) lets [IT administrators](/microsoft-365/admin/add-users/assign-admin-roles) delegate the review process of [data access governance reports](data-access-governance-reports.md) to the site owners of overshared sites.

Site access review involves site owners in the review process so they can address the concern of overshared sites identified in data access governance reports. This feature is crucial because:

- IT administrators can't have access to file-level or item-level details due to compliance reasons.
- Site owners are best positioned to review and address oversharing issues for their own sites.

## Prerequisites

To use the site access review feature, you must fulfill the following prerequisites:

- Have a [Microsoft SharePoint Premium - SharePoint Advanced Management](advanced-management.md) subscription
- Run a non-government cloud tenant environment. Site access review isn't supported in government cloud environments such as GCCH/GCC-Moderate/DoD/Gallatin
- Have admin credentials to access the SharePoint admin center to initiate an access review
- Have site owners respond to the review requests, take necessary actions and complete the review

## How site access review works

- Site access review is accessible only for the top 100 sites shown in the data access governance reports. Site access review specifically targets the oversharing scenario identified in the selected data access governance report.
- When you initiate a review, the system generates a context-specific email for the site owner.
- For example, if you initiate a site access review for a report from the "Content shared with 'Everyone except external users'" category, the review email exclusively addresses sharing issues regarding that particular report.

> [!IMPORTANT]
> Currently, site access review is available only for "Content shared with 'Everyone except external users'" reports.

## Initiate a site access review

1. Sign in to SharePoint admin center with your admin credentials.
1. Expand the **Reports** section and select **Data access governance**.
1. Under "Content shared with 'Everyone except external users", select **View reports**.
1. Select a report and choose the sites you want to review.

   :::image type="content" source="./media/data-access-governance/initiate-site-access-review.png" alt-text="Screenshot that shows Initiate site access review for sites listed within DAG report" lightbox="./media/data-access-governance/initiate-site-access-review.png":::

1. Select **Initiate site access review**.
1. Add comments in the provided section to give context to site owners.

    :::image type="content" source="./media/data-access-governance/comments-site-access-review.png" alt-text="Screenshot that shows provide comments for context setting for site owners":::

1. Select **Send** to initiate the review request.

### Track initiated site access reviews

To see a list of all initiated site access reviews, select the **My review requests** tab from the data access governance landing page.

:::image type="content" source="./media/data-access-governance/my-review-requests.png" alt-text="Screenshot that shows track all reviews initiated from a central page" lightbox="./media/data-access-governance/my-review-requests.png":::

When you initiate a site access review, it remains in a pending state until the site owner completes the review. Once the site owner completes the review, the status and comments are updated with the name of the reviewer and time and date of completion. A review can be marked as failed if site access review couldn't determine a valid email ID for the site owner to deliver the site access review.

### Site access review process (for site owners)

When you initiate a review, site owners receive an email for each site that requires attention. The email includes:

- Relevant title
- Your comments (if any)
- A request to review site permissions
- A link to a detailed access review page. This page is specific for the scenario as specified in the data access governance report.

    :::image type="content" source="./media/data-access-governance/email-eeeu-files-folders-lists.png" alt-text="Screenshot that shows Email received by site owners for oversharing via EEEU" lightbox="./media/data-access-governance/email-eeeu-files-folders-lists.png":::

#### Review 'Everyone except external users' site access review requests (for site owners)

Site owners can review and manage access in two main areas:

- **SharePoint groups:**
  - View which groups contain 'Everyone except external users'
  - See when and by whom the group was added
  - Remove 'Everyone except external users' from groups if necessary:
    1. Selecting the SharePoint group opens the group membership page that displays all members of this SharePoint group.
    2. Select **Everyone except external users** and **Actions** and choose to **remove users from group**.

        :::image type="content" source="./media/data-access-governance/manage-sharepoint-group-membership.png" alt-text="Screenshot that shows displays sharepoint group members" lightbox="./media/data-access-governance/manage-sharepoint-group-membership.png":::

- **Individual items (files/folders/lists):**
  - See items shared with 'Everyone except external users' in the last 28 days
  - View sharing details (who shared and when)
  - Manage access and remove permissions as needed:
    1. Select **Manage access**.
    1. Under the 'Everyone except external users' group in the **Groups** tab, select the group and select **remove access**. See [Stop sharing OneDrive or SharePoint files or folders, or change permissions](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323) for more information.

        :::image type="content" source="./media/data-access-governance/site-owner-view-foreeeu-files.png" alt-text="Screenshot that shows view for site owner regarding items shared with eeeu" lightbox="./media/data-access-governance/site-owner-view-foreeeu-files.png":::

#### Complete site access review requests (for site owners)

Once the site owner takes the necessary actions like modifying or removing permissions, the site owner should:

1. Select **Complete review**.
2. Add any relevant comments.
3. Submit the completed review.

Comments are shared back to the IT administrator who raised the review request. The review request is then marked as completed.

#### Manage multiple site access review requests (for site owners)

A site owner can receive review requests for multiple sites, or receive multiple reviews for different scenarios for the same site. A site owner can track all requests by selecting the **Site reviews** page found in the left panel.

:::image type="content" source="./media/data-access-governance/site-review-master-page.png" alt-text="Screenshot that shows Master page to track all site review for a site" lightbox="./media/data-access-governance/site-review-master-page.png":::

For site owners handling multiple reviews:

1. Access the 'site reviews' page via:
    - The link in the review email
    - The gear icon on the site home page:
        1. Select **Site settings**.
        1. Select **Site reviews**.
        :::image type="content" source="./media/data-access-governance/site-review-from-gear-icon.png" alt-text="Screenshot that shows path to site review page from site home page under gear icon" lightbox="./media/data-access-governance/site-review-from-gear-icon.png":::
1. View all pending site access reviews.
1. Complete reviews as necessary.

## Related topics

[Data access governance](data-access-governance-reports.md)

[Microsoft SharePoint Premium - SharePoint advanced management](advanced-management.md)
