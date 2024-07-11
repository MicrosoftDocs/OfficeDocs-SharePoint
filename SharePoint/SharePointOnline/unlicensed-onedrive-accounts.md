---
ms.date: 07/11/2024
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

As an [IT administrator](/microsoft-365/admin/add-users/about-admin-roles), you might encounter situations where some of your users have unlicensed OneDrive accounts that aren't managed by your organization. This can pose security and compliance risks, as well as create confusion and duplication of files.

In this article, you'll learn how to identify, monitor, and manage unlicensed OneDrive accounts in your organization.

## Changes to storage policies for unlicensed OneDrive accounts

> [!IMPORTANT]
> Beginning August 1, 2025, OneDrive user accounts that have been unlicensed for more than 90 days will enter a frozen state where the data is inaccessible and blocked from read and/or write access. However, the data will not be deleted.

## Prerequisites

If you want to access the data from the now frozen unlicensed OneDrive account, you must do the following prerequisites for setting up [Microsoft 365 Archive](/microsoft-365/syntex/archive/archive-setup):

1. Set up and link Azure subscription in [Syntex pay-as-you-go](/microsoft-365/syntex/syntex-azure-billing).
2. Must have Global admin or SharePoint admin permissions.
3. [Enable Microsoft 365 Archive](/microsoft-365/syntex/syntex-azure-billing).

If no action is taken on unlicensed OneDrive accounts that have been frozen for more than 90 days, the accounts continue to remain frozen and inaccessible by users.

> [!IMPORTANT]
> After August 1, 2025, you won’t be able to remove OneDrive user licenses until you choose how all future unlicensed accounts will be managed. You can choose to delete all future unlicensed accounts or set up billing to keep the OneDrive accounts accessible in Microsoft 365 Archive.

> [!NOTE]
> These changes do not apply to EDU, GCC, or DoD customers.

## Get reports on unlicensed OneDrive user accounts

Unlicensed OneDrive accounts aren't associated with a Microsoft 365 or Office 365 subscription in your organization. A OneDrive account can become unlicensed when the licensing hasn’t been activated or is expired. You might also encounter unlicensed user accounts when user accounts are created, but haven’t been assigned a license. Monitoring unlicensed accounts can help you determine the impact and risk of these accounts, and plan for migration or [deletion of user accounts](/microsoft-365/admin/add-users/delete-a-user).

You can identify unlicensed OneDrive accounts using the SharePoint admin center to generate reports on unlicensed accounts. The following steps show how to use the SharePoint admin center to generate a report of unlicensed OneDrive accounts:

1. Sign in to the SharePoint admin center with your work or school account.
2. Go to **Reports** and select **User reports**.
3. Under **OneDrive usage**, select **Unlicensed users**.
4. Select a username to view the details of the OneDrive account like storage, file count, sharing activity, and sync status.
5. You can also download the report as a CSV file.

The report shows the username, email address, account type, and last activity date of each unlicensed OneDrive account.

## Unlicensed OneDrive account management options

After you have identified and monitored the unlicensed OneDrive accounts in your organization, you can decide how to manage them. You have three options: license, archive, or delete.

### Assign license to unlicensed OneDrive account

To assign a license to an unlicensed OneDrive account, you need to assign a Microsoft 365 or Office 365 subscription to the user that includes OneDrive. This allows the user to access their OneDrive files with their work or school account, and enable you to manage their settings and policies.

You can also bulk assign licenses using either of the following methods:

- [Assign a license to users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users)
- [Assign a license to users with PowerShell](/microsoft-365/enterprise/assign-licenses-to-user-accounts-with-microsoft-365-powershell)

### Archive unlicensed OneDrive account

You can archive the unlicensed OneDrive account using [Microsoft 365 Archive](/microsoft-365/syntex/archive/archive-overview) which lets you keep the OneDrive account and its data for long periods of time in case you need to retrieve it later. Microsoft 365 Archive charges for both storage and file reactivation. See [Pricing model for Microsoft 365 Archive (Preview)](/microsoft-365/syntex/archive/archive-pricing) for more information on Microsoft 365 Archive pricing.

### Delete unlicensed OneDrive account

To delete an unlicensed OneDrive account, you need to [remove the user from your organization and delete their data](/microsoft-365/admin/add-users/delete-a-user). You can use the Microsoft 365 admin center, PowerShell, or the Microsoft Graph API to delete the user. This will permanently delete the user's OneDrive account and files, and prevent them from signing in with their work or school account.

## Related topics

[OneDrive retention and deletion](retention-and-deletion.md)
[Pricing model for Microsoft 365 Archive (Preview)](/microsoft-365/archive/archive-pricing)
[Learn about retention for SharePoint and OneDrive](/purview/retention-policies-sharepoint#how-retention-works-with-microsoft-365-archive)
[Set the OneDrive retention for deleted users](set-retention.md)
[Create retention labels for exceptions](/purview/create-retention-labels-data-lifecycle-management)
[Delete a user from your organization](/microsoft-365/admin/add-users/delete-a-user)
[Assign or unassign licenses for users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users)
