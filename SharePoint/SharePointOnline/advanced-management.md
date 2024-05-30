---
ms.date: 05/20/2024
title: "Microsoft SharePoint Premium - SharePoint Advanced Management overview"
ms.reviewer: daminasy
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- ContentEnagagementFY24
search.appverid:
- MET150
recommendations: false
description: "Learn about Microsoft SharePoint Premium - SharePoint Advanced Management and how you can use it in your organization."
---

# Microsoft SharePoint Premium - SharePoint Advanced Management overview

Microsoft SharePoint Premium - SharePoint Advanced Management is a Microsoft 365 add-on that provides a suite of features that can help you:

- Manage and govern SharePoint and OneDrive
- Enhance Microsoft 365 secure collaboration capabilities

SharePoint Advanced Management features are administered by SharePoint administrators in the SharePoint admin center. Some features can be used by site owners.

## Advanced access policies for secure content collaboration

**[Restrict SharePoint site access with Microsoft 365 groups and Entra security groups](restricted-access-control.md)** - You can restrict the access of a SharePoint site and its content only to the members of Microsoft 365 group (for group-connected sites) or a security group (for non-group connected sites). Users who aren't in the specified groups won't have access to site content even if they previously had site access permissions or a file sharing link.

**[Restrict OneDrive content access](onedrive-site-access-restriction.md)** - You can limit access to shared content in a user's OneDrive to people in a security group. The OneDrive access restriction policy prevents anyone who is not in the security group from accessing content in that OneDrive even if it's shared with them.

**[Restrict OneDrive service access](limit-access.md)** - You can limit OneDrive access to members of a specific security group if you want to allow only certain users to have access. Even if other users outside of these security groups are licensed for OneDrive, they won't have access to their own OneDrive or any shared OneDrive content.

**[Data access governance reports for SharePoint sites](data-access-governance-reports.md)** - These reports help you discover sites that contain potentially overshared or sensitive content. You can use these reports to assess and apply appropriate security and compliance policies.

**[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)** - With Microsoft Entra authentication context, you can enforce more stringent access conditions when users access SharePoint sites. Authentication contexts can be directly applied to sites or used with sensitivity labels to connect Microsoft Entra Conditional Access policies to labeled sites.

## Advanced sites content lifecycle management

**[Block download policy for SharePoint sites and OneDrive](block-download-from-sites.md)** - You can block download of files from SharePoint sites or OneDrive without needing to use Microsoft Entra Conditional Access policies. Users have browser-only access with no ability to download, print, or sync files. They also won't be able to access content through apps, including the Microsoft Office desktop apps.

**[Review your recent changes to SharePoint site properties](recent-actions-panel.md)** - The recent actions panel lets you review and monitor the last 30 changes you've made to a SharePoint site's properties (such as renaming a site, deleting a site, changing storage quota) within the last 30 days in the SharePoint admin center. This feature only shows changes made by you and not other administrators. Also, changes made to site properties at the organization-level will not show in the panel.

**[Manage site lifecycle policies](site-lifecycle-management.md)** - You can set up an inactive site policy to automatically detect inactive sites and send notifications to site owners via email. The owners can then confirm whether the site is still active. When you're setting up a site lifecycle policy, you can choose between a simulation policy and an active policy.

**[Create change history reports](change-history-report.md)** - You can create change history reports in the SharePoint admin center to review SharePoint site property changes made within the last 180 days. Create up to five reports for a given date range and filter by sites and users. You can download the report as a .csv file to view the site property changes.

## Licensing

SharePoint Advanced Management is a per-user license. To use SharePoint Advanced Management, you must have a license for each user in your organization. (It's not required for guests.) Users must also be licensed for SharePoint K, P1, or P2 via standalone or a Microsoft 365 suite.

You can purchase the *SharePoint Advanced Management Plan 1* add-on in the Microsoft 365 admin center, through a Cloud Solution Provider (CSP), or through volume licensing enrollment. Contact your Microsoft account manager for further information.

SharePoint Advanced Management is available for Commercial, WW Commercial Public Sector, Education, Charity, and US GCC, GCC-High, and DoD customers.

SharePoint Advanced Management is $3 per user per month for commercial customers.

Licensing details for each feature listed above are included in those articles.

## Related topics

[Microsoft Syntex documentation](/microsoft-365/syntex)

[Microsoft 365 Government - how to buy](/office365/servicedescriptions/office-365-platform-service-description/office-365-us-government/microsoft-365-government-how-to-buy)
