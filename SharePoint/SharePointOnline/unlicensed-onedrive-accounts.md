---
ms.date: 08/28/2024
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
5. Starting January 2025, an interactive UI is available. You can select a username to view the details.

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

Microsoft 365 Archive charges for both storage and account reactivation. For more information about Microsoft 365 Archive pricing, see [Pricing model for Microsoft 365 Archive (Preview)](/microsoft-365/syntex/archive/archive-pricing).

## Frequently Asked Questions

**1. What is an unlicensed OneDrive account?**

**Answer:** When an employee leaves an organization or a license is removed, their OneDrive account becomes unlicensed after the admin takes one of two steps:

**License Removal:**

- Go to the Admin Center.
- Navigate to Billing > Your Products.
- Select the subscription and select on Remove licenses.

**User Deletion:**

- Go to the Admin Center.
- Navigate to Active users.
- Delete the user.

For additional information: [Delete a user from your organization](/microsoft-365/admin/add-users/delete-a-user).

**2. When will an unlicensed account get archived?**

**Answer:** For newly unlicensed OneDrive accounts, it will be after 93 days of the license removal or user deletion. For example, a OneDrive account that became unlicensed on August 1, 2025, will be inaccessible to users as of November 2, 2025. For unlicensed OneDrive accounts with license removal before October 26, 2024, the accounts will be archived sometime between late January 2025 to late March 2025.

**3. How does it impact eDiscovery in Microsoft Purview?**

**Answer:** Microsoft Purview eDiscovery and Content Search are still discoverable in archived content. Exporting the content that's supporting the search results will not require manual reactivation of the archived account, and it will take up to 24 hours to complete.

**4. How does it impact Retention Policy, Retention Setting, or Litigation Hold?**

**Answer:** Archived OneDrive accounts fully honor retention policies, settings, and litigation holds. For example, if your company has a five-year retention policy, it remains unchanged whether the OneDrive account is active or archived. Archiving doesn't reset the timeline of the retention policy or holds. 

>[!Note]
> If a OneDrive account is retained due to a Retention Policy, Retention Setting, or Litigation Hold and has been archived due to being unlicensed for 93 days or longer, then you will still pay for the monthly archive storage costs.

**5. Can I delete an unlicensed account without Archive reactivation?**

**Answer:** Yes. An archived unlicensed account can be deleted from the archive state. However, if the account is under retention policy, the unlicensed account can't be deleted, and the administrator receives an error message.

**6. When will I get charged?**

**Answer:** Once a payment method is provided, billing follows the routine cycle for archived content. If there's no retention policy and billing stops, your content is deleted within a 93-day period. If a retention policy is still active, the policy is honored regardless of billing status. If the account has no retention and billing, the 93-day content deletion lifecycle begins.

As an example, if the billing is put down to reactivate one particular unlicensed account, the reactivation fee will be applied for $0.60/GB for that account, and from that month onward, the storing fee of $0.05/GB/Month will also be applied for all unlicensed accounts within the organization that's longer than 90 days.

**7. Can unlicensed ODB leverage unused SPO storage quota?**

**Answer:** No. They're independent. Unlicensed OneDrive accounts can't use unused SharePoint storage quota, even though there's Microsoft 365 Archive set up in the SharePoint tenant.

**8. What's the guidance on 'duplicate accounts'?**

**Answer:** A duplicate account is created when an employee switches to a different country/region or a different firm within the organization. If the duplicate accounts aren't desired, we recommend using the downloadable CSV in the SharePoint Admin Center to identify the accounts and delete them. For already-archived unlicensed OneDrive accounts, it can be deleted from the archived state without the need of reactivation.

**9. What is the outcome if an Unlicensed OneDrive account is restored from the Recycle Bin, 90 days after its license removal? Does the account get automatically archived?**

**Answer:** Yes. If 90 days have past since the license removal, bringing back an unlicensed OneDrive account from the recycle bin can lead to automatic archival.

**10. Once I initiate the reactivation of an account from Microsoft 365 Archive, how long do I have to wait until the data is available?**

**Answer:** It takes up to 24 hours for the account to be accessible. Once the account is reactivated, it remains active for a total of 30 days before it gets automatically archived again.

**11. Is there any charge to use the eDiscovery Hold feature?**
**Answer:** We honor eDiscovery hold and charge accordingly. eDiscovery Hold works the same way as retention policy and legal hold.

**12. What's the process to relicense an account once it's archived?**

**Answer:** If the archived account has an associated user, the IT admin can simply give the user a valid license and the account will automatically get reactivated within 24 hours. If the archived account does not have an associated user (for example, if the identity was deleted), then we recommend admins move any actively needed content to a SharePoint site or an active and licensed OneDrive account.

**13. If a change is made to retention policies, will that change sync down to the archived sites?** 

**Answer:** Yes. As an example, if the company retention policy is shortened from 5 years to 3 years, this change will be synced with all archived accounts, and the recycle bin process will start for accounts that have completed the retention policy.

## Related topics

- [OneDrive retention and deletion](retention-and-deletion.md)
- [Pricing model for Microsoft 365 Archive](/microsoft-365/archive/archive-pricing)
- [Learn about retention for SharePoint and OneDrive](/purview/retention-policies-sharepoint#how-retention-works-with-microsoft-365-archive)
- [Set the OneDrive retention for deleted users](set-retention.md)
- [Create retention labels for exceptions](/purview/create-retention-labels-data-lifecycle-management)
- [Delete a user from your organization](/microsoft-365/admin/add-users/delete-a-user)
- [Assign or unassign licenses for users in the Microsoft 365 admin center](/microsoft-365/admin/manage/assign-licenses-to-users)
