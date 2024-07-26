---
ms.date: 07/26/2024
title: "Manage unlicensed OneDrive user accounts"
ms.reviewer: rebecca.gee
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
- M365-collaboration
- Highpri
- Tier2
description: "Learn how to manage unlicensed OneDrive user accounts."
---

# Manage unlicensed OneDrive user accounts

As an [IT administrator](/microsoft-365/admin/add-users/about-admin-roles), you might encounter situations where some of your users have unmanaged and unlicensed OneDrive accounts within your organization. Unlicensed OneDrive accounts can pose security and compliance risks, as well as create confusion and duplication of files.

In this article, you learn how to identify, monitor, and manage unlicensed OneDrive accounts in your organization.

## Changes to storage policies for unlicensed OneDrive accounts

> [!IMPORTANT]
> Beginning January 27, 2025, any OneDrive user account that has been unlicensed for longer than 90 days becomes inaccessible to admins and end users. The unlicensed account is automatically archived, viewable via admin tools, but remains inaccessible until administrators take action on them."

## Prerequisites

If you want to access the data of the now inaccessible unlicensed OneDrive account, you must do the following prerequisites to set up [Microsoft 365 Archive](/microsoft-365/syntex/archive/archive-setup):

1. Set up and link Azure subscription in [Syntex pay-as-you-go](/microsoft-365/syntex/syntex-azure-billing).
2. Must have Global admin or SharePoint admin permissions.
3. [Enable Microsoft 365 Archive](/microsoft-365/syntex/syntex-azure-billing) Unlicensed Account billing (billing is available starting April 2025).

If a OneDrive account stays unlicensed for longer than 90 days, the account becomes inaccessible until you fulfill the prerequisites.

> [!NOTE]
> These changes do not apply to EDU, GCC, or DoD customers.

## Get reports on unlicensed OneDrive user accounts

Unlicensed OneDrive accounts aren't associated with a Microsoft 365 or Office 365 subscription in your organization. A OneDrive account can become unlicensed when the licensing isn't activated or is expired.

You can also encounter unlicensed OneDrive accounts when accounts are created, but aren't assigned a license. Monitoring unlicensed accounts can help you determine the risk of these accounts, and plan for migration or [deletion of user accounts](/microsoft-365/admin/add-users/delete-a-user).

You can identify unlicensed OneDrive accounts using the SharePoint admin center to generate reports on unlicensed accounts. The following steps show how to use the SharePoint admin center to generate a report of unlicensed OneDrive accounts:

1. Sign in to the SharePoint admin center with your work or school account.
2. Go to **Reports** and select **User reports**.
3. Under **OneDrive usage**, select **Unlicensed users**.
4. You can download the report as a CSV file.
5. Starting January 2025, an interactive UI will be available. You can select a username to view the details.

The report shows the username, email address, account type, and last activity date of each unlicensed OneDrive account.

## Unlicensed OneDrive account management options

After you identify the unlicensed OneDrive account, you can choose to license or delete the account. If no action is taken, the account remains archived.

### Assign license to unlicensed OneDrive account

To assign a license to an unlicensed OneDrive account, you need to assign a Microsoft 365 or Office 365 subscription to the user that includes OneDrive. Assigning a license allows the user to access their OneDrive files with their work or school account, and lets you manage their settings and policies.

You can also bulk assign licenses using either of the following methods:

- [Assign licenses to user accounts in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users)
- [Assign licenses to user accounts with PowerShell](/microsoft-365/enterprise/assign-licenses-to-user-accounts-with-microsoft-365-powershell)

### Delete unlicensed OneDrive account

To delete an unlicensed OneDrive account, you need to [remove the user from your organization and delete their data](/microsoft-365/admin/add-users/delete-a-user). You can use the Microsoft 365 admin center, PowerShell, or the Microsoft Graph API to permanently delete the user.  

Once you delete the unlicensed account, both the OneDrive account and its files are permanently deleted, and the user is no longer able to sign in to their work or school account.

### Archive unlicensed OneDrive account

If no action is taken, the account remains archived through [Microsoft 365 Archive](/microsoft-365/syntex/archive/archive-overview). Archiving the account lets you keep the OneDrive account and its data for long periods of time in case you need to retrieve it later.

Microsoft 365 Archive charges for both storage and file reactivation. For more information about Microsoft 365 Archive pricing, see [Pricing model for Microsoft 365 Archive (Preview)](/microsoft-365/syntex/archive/archive-pricing).

## Related topics

- [OneDrive retention and deletion](retention-and-deletion.md)
- [Pricing model for Microsoft 365 Archive (Preview)](/microsoft-365/archive/archive-pricing)
- [Learn about retention for SharePoint and OneDrive](/purview/retention-policies-sharepoint#how-retention-works-with-microsoft-365-archive)
- [Set the OneDrive retention for deleted users](set-retention.md)
- [Create retention labels for exceptions](/purview/create-retention-labels-data-lifecycle-management)
- [Delete a user from your organization](/microsoft-365/admin/add-users/delete-a-user)
- [Assign or unassign licenses for users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users)
