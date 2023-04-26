---
ms.date: 03/01/2023
title: "Restrict OneDrive access by security group"
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- Highpri
- Tier1
search.appverid:
ms.assetid: 
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "In this article, you'll learn how to allow only users in specified security groups to access OneDrive."
---

# Restrict OneDrive access by security group

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can use the restricted access control policy for OneDrive to allow only users in specified security groups to access OneDrive. Even if other users outside of these security groups are licensed for OneDrive, they won’t have access to their own OneDrive or any shared OneDrive content.

You can use this to prevent oversharing of OneDrive content. For example, you can restrict OneDrive access to your users, preventing guests from accessing any OneDrive content even if it's shared with them.

## Requirements

To access and use this feature, your organization must have one of the following subscriptions:

- Microsoft Syntex - SharePoint Advanced Management
- Office 365 E5/A5
- Microsoft 365 E5/A5

## Enablement

To enable this feature:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185071" target="_blank">Access control in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](sharepoint-admin-role.md) for your organization.

2. Select **Restrict OneDrive access**.

3. Select **Restrict OneDrive access to only users in specified security groups**.

    :::image type="content" source="media/restrictonedriveaccess.png" alt-text="Restrict OneDrive access on the Access control page in the SharePoint admin center":::

4. Add the security groups (maximum of 10) you want to be able to use OneDrive.

5. Select **Save**.

> [!NOTE]
> Users who aren't included in the security groups you added will lose access to their own OneDrive and any shared OneDrive content.

## Audit events

[Audit events](/microsoft-365/compliance/audit-log-activities) are available in Microsoft Purview compliance portal to help you monitor restricted access control activities. Audit events are logged for the following activities:

- Enabled Restricted OneDrive access and sharing
- Disabled Restricted OneDrive access and sharing

## Related topics

[Restrict access control for SharePoint sites](restricted-access-control.md)

[Data access governance insights for SharePoint sites](data-access-governance-reports.md)
