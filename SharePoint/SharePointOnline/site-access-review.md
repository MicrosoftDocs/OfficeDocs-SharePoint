---
ms.date: 21/06/2024
title: "Site access review from Data access governance reports"
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
description: "In this article, you learn about site access review as a remedial action available from Data access governance for SharePoint admins."
---

# Remedial actions from Data access governance reports

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

## Site Access Review

Once a DAG report is generated and sites are listed within the report, the SharePoint admin may not be able to decide the subsequent action by themselves, due to various reasons. The data in the report is aggregated at a site level. Detailed information at a file level isn't available to SharePoint admin due to compliance reasons. In such scenarios, the site owner who is usually the custodian of the data within the site, could be the best persona suited to review the oversharing scenario and take necessary action. Now, SharePoint admins can delegate the review to site owners using 'Site access review' and that provides detailed information at a file/item level allowing the site owner to take the necessary action

Few key points to be considered for 'Site access review'

- A 'Site access review' is available only within a DAG report. This review isn't a generic review but a review within the context of oversharing as specified in the DAG report. For for example: If the report is about Content shared with 'Everyone except external users', the access review to the site owner will be about that particular content only.
- 'Site access review' is available only via the SharePoint admin center portal/UI that is, a SharePoint admin can only select within the top 100 sites shown in the UI.

### Support matrix

Site access review (SAR) is available from the following DAG reports

- Content shared with 'Everyone except external users' reports

### Initiate site access review

From the DAG report, select one or more sites to initiate a review and select the 'Initiate site access review' button.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/initiate-site-access-review.png" alt-text="Initiate site access review for sites listed within DAG report":::

Use the comments section to set the right context and clarify on the expectations with the corresponding site owners. Click 'send' and the review request is sent as an email to all corresponding site owners.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/comments-site-access-review.png" alt-text="Provide comments for context setting for site owners":::

### Communication to site owner

All the site owners receive an email, for each site, with the relevant title and the comments from SharePoint admin requesting them to review permissions. The email also contains a link to the page where detailed information is provided to the site owner.

#### For content shared with 'Everyone except external users' reports

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/Email - EEEU files, folders and lists.jpg" alt-text="Email received by site owners for oversharing via EEEU":::

### Review by site owner

Clicking on the link in the email directs site owner to the access review detailed page. This page is specific for the scenario as specified in the DAG report.

#### Content shared with 'Everyone except external users' reports

This scenario provides details on 'public sites' or 'public files/items' created in the last 28 days.

##### For sites

Sites are 'public' when 'Everyone except external users' is part of the site membership,  that is, within site owners/members/visitors. This page provides details on which SharePoint groups have 'Everyone except external users', the date when it was added to the SharePoint group and by whom.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/site-owner-view-foreeeu-groups.png" alt-text="sharepoint groups to which eeeu was added":::

Clicking on the SharePoint group opens the group membership page that displays all members of this SharePoint group. Select 'Everyone except external users' and 'Actions' and choose to 'remove users from group'.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/Manage-sharepoint-group-membership.png" alt-text="Displays sharepoint group members":::

##### For items

The below page provides details on specific items (file/folder/list) shared with 'Everyone except external users' group, in the last 28 days, effectively making them 'public' items. Additional information on who shared the item and when are also provided.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/site-owner-view-foreeeu-files.png" alt-text="view for site owner regarding items shared with eeeu":::

Click on 'Manage access', locate the 'Everyone except external users' group in the 'Groups' tab beside 'people, click on the group and remove access, if necessary. More details are documented [here](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323).

### Completing the review

Once the site owner took the relevant actions and modified/removed relevant permissions, they can click on 'Complete review' and provide necessary comments. These comments are shared back to the SharePoint admin who raised the review request and the review is marked as 'Completed'.

### Managing multiple reviews for site owners

A site owner can receive review requests for multiple sites or multiple reviews for different scenario for the same site. A site owner can track all such requests from the 'site reviews' page.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/site-review-master-page.png" alt-text="Master pagr to track all site review for a site":::

There are multiple pathways to arrive at this page.

#### From email

The email provides link to the 'detailed' site review page. From within that page, a site owner can click on 'site reviews' in the breadcrumb present in the top left.

#### From site settings

If you lost the email, or closed the browser, you can still find the 'site reviews' page from the 'gear' icon in the site home page.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/site-review-from-gear-icon.png" alt-text="Path to site review page from site home page under gear icon":::

### Tracking all reviews by SharePoint admins

From a SharePoint admin perspective, they can track all reviews from a central page, present as a separate tab named as 'My review requests' in Data access governance landing page.

:::image type="content" source="../Documents/GitHub/OfficeDocs-SharePoint-pr/SharePoint/SharePointOnline/media/data-access-governance/my-review-requests.png" alt-text="Track all reviews initiated from a central page":::

Once SharePoint admin initiates a review, the review status is marked as 'pending'. A review can be marked as failed if the product couldn't determine a valid email ID for any site owner and hence there's no communication. Once a site owner completes the review, the status is updated as 'Completed' and comments given by the site owner are updated under the review details. To know more about the review details, click on a particular review.
