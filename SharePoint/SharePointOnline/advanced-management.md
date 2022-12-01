---
title: "Microsoft Syntex Advanced Management (Preview) overview"
ms.reviewer: daminasy
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection:  
search.appverid:
- MET150
description: "Learn about Microsoft Syntex Advanced Management and how you can use it in your organization."
---

# Microsoft Syntex Advanced Management (Preview) overview

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

Microsoft Syntex Advanced Management is a Microsoft 365 add-on that provides a suite of features that can help you:

- Govern SharePoint and OneDrive
- Enhance Microsoft 365 secure collaboration capabilities

Articles that cover features that use Syntex Advanced Management are designated with  [!INCLUDE[Advanced Management](includes/advanced-management.md)] at the top.

## Management

Data access governance reports help you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply appropriate security and compliance policies. For details, see [Data access governance reports](/sharepoint/data-access-governance-reports).

You can limit OneDrive access to members of a specific security group if you want to allow only certain users to have access. Even if other users outside of these security groups are licensed for OneDrive, they won't have access to their own OneDrive or any shared OneDrive content. For details, see [Limit OneDrive access by security group](/onedrive/limit-access).

You can review and export the most recent site-related actions you made in the SharePoint admin center in the last 30 days by using the recent actions panel. Site property changes like site name, site creation and deletion, site URL, sharing settings, and storage quota are listed as actions in the panel. Note that changes made to organization-level settings, and changes made by other admins are not shown in the panel. For details, see [Recent Actions Panel in SharePoint admin center](/SharePoint/recent-actions-panel).

## Secure collaboration

With Azure Active Directory authentication context, you can enforce more stringent access conditions when users access SharePoint sites that have a sensitivity label applied. Authentication contexts are used with sensitivity labels to connect Azure AD conditional access policies to labeled sites. For details, see [Manage site access based on sensitivity label](/sharepoint/authentication-context-example).

When SharePoint is enabled for sensitivity labels, you can configure a default label for document libraries. Then, any new files uploaded to that library, or existing files edited in the library will have that label applied if they don't already have a sensitivity label, or they have a sensitivity label but with lower priority. For details, see [Configure a default sensitivity label for a SharePoint document library](/microsoft-365/compliance/sensitivity-labels-sharepoint-default-label).

You can restrict the access of a SharePoint site and its content only to the members of Microsoft 365 group connected to the site. Users who are not added in the Microsoft 365 group won't have access even if they previously had site access permissions to a file. For details, see [Restricted Access Control for SharePoint sites](/sharepoint/restricted-access-control).

