---
title: Create a compliant SharePoint and OneDrive environment
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: 
---

# Create a compliant SharePoint and OneDrive environment

Most organizations have business or legal requirements that govern how data is used, shared, and retained. Some organizations also have data residency requirements or regulatory requirements that restrict communication between certain users and groups.

Microsoft 365 has a wide range of governance and compliance features to address these needs. This article provides an overview of features you may want to consider as part of your OneDrive and SharePoint rollout.

## Information governance

Use Microsoft Information Governance capabilities in Microsoft 365 to govern your OneDrive and SharePoint content for compliance or regulatory requirements. The following table describes the capabilities to help you keep the content you need you and delete what you don't need.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Retention policies and retention labels](/microsoft-365/compliance/retention)<br /><br />[Learn about retention for SharePoint and OneDrive](/microsoft-365/compliance/retention-policies-sharepoint) | Retain or delete content with policy management for SharePoint documents | [Create and configure retention policies](/microsoft-365/compliance/create-retention-policies) <br /><br /> [Create retention labels for exceptions to your retention policies](/microsoft-365/compliance/create-retention-labels-information-governance)|

### Deleted users' data

When a user leaves your organization and you've deleted that user's account, what happens to the user's data? When considering data retention compliance, determine what needs to happen with the deleted user's data. For some organizations, retaining deleted user data could be important continuity and preventing critical data loss. 

If a user's Microsoft 365 account is deleted, their OneDrive files are preserved for 30 days. To change this setting, [Set the OneDrive retention for deleted users](set-retention.md).

By default, when a user is deleted, the user's manager is automatically given access to the user's OneDrive. To change this, see [OneDrive retention and deletion](retention-and-deletion.md).

## Information protection

Microsoft Information Protection (MIP) capabilities included with Microsoft Purview help you discover, classify, and protect sensitive information in OneDrive and SharePoint. The following table describes these capabilities. Consider if you want to implement any of these capabilities as part of your OneDrive and SharePoint rollout.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:--------------------|
|[Sensitive information types](/microsoft-365/compliance/sensitive-information-type-learn-about)| Identifies sensitive data by using built-in or custom regular expressions or a function. Corroborative evidence includes keywords, confidence levels, and proximity.| [Customize a built-in sensitive information type](/microsoft-365/compliance/customize-a-built-in-sensitive-information-type)|
|[Trainable classifiers](/microsoft-365/compliance/classifier-learn-about)| Identifies sensitive data by using examples of the data you're interested in rather than identifying elements in the item (pattern matching). You can use built-in classifiers or train a classifier with your own content.| [Get started with trainable classifiers](/microsoft-365/compliance/classifier-get-started-with) |
|[Sensitivity labels](/microsoft-365/compliance/sensitivity-labels)| A single solution across apps, services, and devices to label and protect your data as it travels inside and outside your organization. <br /><br /> Example scenarios: <br />- [Manage sensitivity labels for Office apps](/microsoft-365/compliance/sensitivity-labels-office-apps) <br />- [Encrypt documents](/microsoft-365/compliance/encryption-sensitivity-labels)  <br />|[Get started with sensitivity labels](/microsoft-365/compliance/get-started-with-sensitivity-labels) |
|[SharePoint Information Rights Management (IRM)](/microsoft-365/compliance/set-up-irm-in-sp-admin-center#irm-enable-sharepoint-document-libraries-and-lists)|Protects SharePoint lists and libraries so that when a user checks out a document, the downloaded file is protected so that only authorized people can view and use the file according to policies that you specify. | [Set up Information Rights Management (IRM) in SharePoint admin center](/microsoft-365/compliance/set-up-irm-in-sp-admin-center)|
|[Data loss prevention](/microsoft-365/compliance/dlp-learn-about-dlp)| Helps prevent unintentional sharing of sensitive items. | [Get started with the default DLP policy](/microsoft-365/compliance/get-started-with-the-default-dlp-policy)|

## File sync

The OneDrive sync app has policies that you can use to help you maintain a compliant environment. Consider configuring these policies before you roll out SharePoint and OneDrive.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Allow syncing OneDrive accounts for only specific organizations|[AllowTenantList](use-group-policy.md#allow-syncing-onedrive-accounts-for-only-specific-organizations)|[AllowTenantList](deploy-and-configure-on-macos.md#allowtenantlist)|
|Block syncing OneDrive accounts for specific organizations|[BlockTenantList](use-group-policy.md#block-syncing-onedrive-accounts-for-specific-organizations)|[BlockTenantList](deploy-and-configure-on-macos.md#blocktenantlist)|
|Prevent users from syncing libraries and folders shared from other organizations|[BlockExternalSync](use-group-policy.md#prevent-users-from-syncing-libraries-and-folders-shared-from-other-organizations)|[BlockExternalSync](deploy-and-configure-on-macos.md#blockexternalsync)|
|Prevent users from syncing personal OneDrive accounts|[DisablePersonalSync](use-group-policy.md#prevent-users-from-syncing-personal-onedrive-accounts)|[DisablePersonalSync](deploy-and-configure-on-macos.md#disablepersonalsync)|
|Exclude specific kinds of files from being uploaded|[EnableODIgnoreListFromGPO](use-group-policy.md#exclude-specific-kinds-of-files-from-being-uploaded)|[EnableODIgnore](deploy-and-configure-on-macos.md#enableodignore)|

## Data residency

Multi-Geo is Microsoft 365 feature that allows organizations to span their storage over multiple geo locations and specify where to store users' data. For multinational customers with data residency requirements, you can use this feature to ensure that each user's data is stored in the geo location necessary for compliance. For more info about this feature, see [Multi-Geo Capabilities in OneDrive and SharePoint](/office365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-office-365/).

Features such as file sync and mobile device management work normally in a multi-geo environment. There's no special configuration or management needed. The multi-geo experience for your users has minimal difference from a single-geo configuration. For details, see [User experience in a multi-geo environment](/office365/enterprise/multi-geo-user-experience/).

For more information about Microsoft 365 Multi-Geo, see [Microsoft 365 Multi-Geo](/microsoft-365/enterprise/microsoft-365-multi-geo).

## Information barriers

Microsoft Purview Information Barriers (IB) is a compliance solution that allows you to restrict two-way communication and collaboration between groups and users in Microsoft Teams, SharePoint, and OneDrive. Often used in highly regulated industries, IB can help to avoid conflicts of interest and safeguard internal information between users and organizational areas.

When IB policies are in place, users who shouldn't communicate or share files with other specific users won't be able to find, select, chat, or call those users. IB policies automatically put checks in place to detect and prevent unauthorized communication and collaboration among defined groups and users.

If your business requires information barriers, see [Learn about information barriers](/microsoft-365/compliance/information-barriers) and [Use information barriers with SharePoint](/sharepoint/information-barriers) to get started.

## Next steps

> [!div class="nextstepaction"]
> [Plan sharing and collaboration options](collaboration-options.md)

## Related topics

[Plan for SharePoint and OneDrive in Microsoft 365](plan-for-sharepoint-onedrive.md)

[B2B Sync](b2b-sync.md)

[Implement compliance in Microsoft 365](/learn/paths/implement-data-governance-microsoft-365-intelligence/)

[Protect your enterprise data using Windows Information Protection (WIP)](/windows/security/information-protection/windows-information-protection/protect-enterprise-data-using-wip)

[Control OneDrive and SharePoint access based on network authentication or app](control-access-based-on-network-location-or-app.md)