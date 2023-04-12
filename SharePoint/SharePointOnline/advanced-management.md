---
ms.date: 03/28/2023
title: "Microsoft Syntex - SharePoint Advanced Management overview"
ms.reviewer: daminasy
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: normal
ms.collection:
- Highpri
- Tier1
search.appverid:
- MET150
recommendations: false
description: "Learn about Microsoft Syntex - SharePoint Advanced Management and how you can use it in your organization."
---

# Microsoft Syntex - SharePoint Advanced Management overview

Microsoft Syntex - SharePoint Advanced Management is a Microsoft 365 add-on that provides a suite of features that can help you:

- Manage and govern SharePoint and OneDrive
- Enhance Microsoft 365 secure collaboration capabilities

SharePoint Advanced Management features are administered by SharePoint administrators in the SharePoint admin center. Some features can be used by site owners.

> [!IMPORTANT]
> SharePoint Advanced Management is currently rolling out. Licenses and functionality will become available to organizations throughout March and early April.

## Advanced access policies for secure content collaboration

**[Restricted access control for SharePoint sites](restricted-access-control.md)** - You can restrict the access of a SharePoint site and its content only to the members of Microsoft 365 group connected to the site. Users who are not in the Microsoft 365 group won't have access even if they previously had site access permissions to a file.

**[Restricted access control policy for OneDrive](limit-access.md)** - You can limit OneDrive access to members of a specific security group if you want to allow only certain users to have access. Even if other users outside of these security groups are licensed for OneDrive, they won't have access to their own OneDrive or any shared OneDrive content.

**[Data access governance reports for SharePoint sites](data-access-governance-reports.md)** - These reports help you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply appropriate security and compliance policies.

**[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)** - With Azure Active Directory authentication context, you can enforce more stringent access conditions when users access SharePoint sites. Authentication contexts can be directly applied to sites or used with sensitivity labels to connect Azure AD conditional access policies to labeled sites.

**[Secure SharePoint document libraries](/microsoft-365/compliance/sensitivity-labels-sharepoint-default-label)** - When SharePoint is enabled for sensitivity labels, you can configure a default label for document libraries. Then, any new files uploaded to that library, or existing files edited in the library will have that label applied if they don't already have a sensitivity label, or they have a sensitivity label but with lower priority.

## Advanced sites content lifecycle management

**[Block download policy for SharePoint sites and OneDrive](block-download-from-sites.md)** - You can block download of files from SharePoint sites or OneDrive without needing to use Azure Active Directory conditional access policies. Users have browser-only access with no ability to download, print, or sync files. They also won't be able to access content through apps, including the Microsoft Office desktop apps.

**[Recent SharePoint admin actions](recent-actions-panel.md)** - You can review and export the most recent site-related actions you made in the SharePoint admin center in the last 30 days by using the recent actions panel. Site property changes like site name, site creation and deletion, site URL, sharing settings, and storage quota are listed as actions in the panel. Note that changes made to organization-level settings, and changes made by other admins are not shown in the panel.

## Licensing

SharePoint Advanced Management is a per-user license. To use SharePoint Advanced Management, you must have a license for each user in your organization. (It's not required for guests.) Users must also be licensed for SharePoint K, P1, or P2 via standalone or a Microsoft 365 suite.

You can purchase the *SharePoint Advanced Management Plan 1* add-on in the Microsoft 365 admin center, through a Cloud Solution Provider (CSP), or through volume licensing enrollment. Contact your Microsoft account manager for further information.

SharePoint Advanced Management is available for Commercial, WW Commercial Public Sector, Education, Charity, and US GCC, GCC-High, and DoD customers.

SharePoint Advanced Management is $3 per user per month for commercial customers.

Licensing details for each feature listed above are included in those articles.

## Related topics

[Microsoft Syntex documentation](/microsoft-365/syntex)
