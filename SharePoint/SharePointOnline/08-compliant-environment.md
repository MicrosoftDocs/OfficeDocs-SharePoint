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

o	Do you have data residency requirements?
o	Do you have info barriers requirements?
o	Retention
o	Labels, SITs, and DLP
o	Sync policies

- Specify how long you want to retain a user's OneDrive files when the user is deleted: [Set OneDrive retention for deleted users](set-retention.md)

- To prevent users from accessing OneDrive and SharePoint content on devices outside of specific domains, or from apps that don't use modern authentication: [Control access based on network authentication or app](control-access-based-on-network-location-or-app.md)


## Manage OneDrive by using the Microsoft Purview compliance portal

The [Microsoft Purview compliance portal](https://compliance.microsoft.com/) provides a centralized location to auditing, DLP, retention, eDiscovery, and alerting capabilities within Microsoft 365 that are applicable to OneDrive. You can create DLP policies from templates that protect certain types of data, such as Social Security numbers, banking information, and other financial and medical content. Some capabilities won't be available if you're using Intune (for example, device management). For a walkthrough of how to create DLP policies and apply them to OneDrive, see [Create a DLP policy from a template](/office365/securitycompliance/create-a-dlp-policy-from-a-template/).

## Data retention

When a user leaves your organization and you've deleted that user's account, what happens to the user's data? When considering data retention compliance, determine what needs to happen with the deleted user's data. For some organizations, retaining deleted user data could be important continuity and preventing critical data loss. The default retention policy for deleted OneDrive users is 30 days. You can configure the setting to a range between 0 days and 3,650 days (ten years).

For more info about OneDrive retention, see [OneDrive retention and deletion](retention-and-deletion.md) and [Learn about retention policies](/microsoft-365/compliance/retention-policies?view=o365-worldwide&preserve-view=true).

Key decision:

- What data retention time do you need for your organization?

-  **Retention** - On the <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">Settings page in the SharePoint admin center</a>, select **Retention** to configure data retention settings for users whose accounts have been deleted (the maximum value is 10 years). This organization-wide configuration setting is applicable to all organizations, regardless of the device management tool they use. Use this page to configure the data retention value based on the decisions you made in Part 2, [Plan for OneDrive for enterprises](plan-onedrive-enterprise.md).

### Multi-Geo data residency

Multi-Geo is Microsoft 365 feature that allows organizations to span their storage over multiple geo locations and specify where to store users' data. For multinational customers with data residency requirements, you can use this feature to ensure that each user's data is stored in the geo location necessary for compliance. For more info about this feature, see [Multi-Geo Capabilities in OneDrive and SharePoint](/office365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-office-365/).

If you have data residency requirements, consider OneDrive Multi-Geo. With OneDrive Multi-Geo, you can specify a preferred data location (PDL), from available locations around the world, for each user's OneDrive. For detailed info about OneDrive Multi-Geo, see [Multi-Geo Capabilities in OneDrive and SharePoint in Microsoft 365](/office365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-office-365/).

If you plan to deploy OneDrive Multi-Geo, there are two user scenarios:

- Users who start using OneDrive before you configure OneDrive Multi-Geo – their OneDrive will be located in the central location once you configure OneDrive Multi-Geo. If you need to move a user's OneDrive to a different geo location, follow the steps in [Move a OneDrive site to a different geo-location](/office365/enterprise/move-onedrive-between-geo-locations/).

- Users who start using OneDrive after you configure OneDrive Multi-Geo – you can configure their preferred data location as part of your general user onboarding process and their OneDrive will be created in the appropriate geo location.

Features such as file sync and mobile device management work normally in a multi-geo environment. There's no special configuration or management needed. The multi-geo experience for your users has minimal difference from a single-geo configuration. For details, see [User experience in a multi-geo environment](/office365/enterprise/multi-geo-user-experience/).

If you plan to configure OneDrive Multi-Geo prior to deploying OneDrive for your users, see [Plan for OneDrive Multi-Geo](/office365/enterprise/plan-for-multi-geo/), and follow the steps in [OneDrive Multi-Geo tenant configuration](/office365/enterprise/multi-geo-tenant-configuration/).

Key decisions:

- Do you plan to use OneDrive Multi-Geo?

- Will you have OneDrive Multi-Geo fully configured before your users start using OneDrive?

### Windows Information Protection

You can use Windows Information Protection (WIP) to help prevent data leakage by deploying application or device policies that restrict how your employees can store, access, and use your organization's data. For example, you can restrict users to synchronizing files that contain company data only to OneDrive and not to personal cloud storage providers like Dropbox. For info about how to use WIP, see [Protect your enterprise data using Windows Information Protection (WIP)](/windows/security/information-protection/windows-information-protection/protect-enterprise-data-using-wip).

If you've decided to use Windows Information Protection with OneDrive, see the following resources to set up your Windows Information Protection policies:

- [Create a Windows Information Protection (WIP) policy using Microsoft Intune](/windows/security/information-protection/windows-information-protection/overview-create-wip-policy/)

- [Create a Windows Information Protection (WIP) policy using Configuration Manager](/windows/security/information-protection/windows-information-protection/overview-create-wip-policy-configmgr)


[Microsoft Purview compliance documentation](/microsoft-365/compliance)

Learn

[Implement compliance in Microsoft 365](/learn/paths/implement-data-governance-microsoft-365-intelligence/)

[Manage compliance in Microsoft 365](/learn/paths/manage-compliance-microsoft-365/)

[Manage information protection and governance](/learn/paths/m365-compliance-information/)

[Explore data governance and compliance in Microsoft 365](/paths/introduction-to-data-governance-microsoft-365/)

[Manage data governance in Microsoft 365](/learn/paths/manage-data-governance-microsoft-365/)


## Data residency

[Microsoft 365 Multi-Geo](/microsoft-365/enterprise/microsoft-365-multi-geo)

[Multi-Geo Capabilities in OneDrive and SharePoint Online](/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365)

## Information barriers

Use information barriers to create policies that allow or prevent file collaboration between groups of people in your organization. The following table describes user segmentation capabilities of information barriers.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Information barriers](/microsoft-365/compliance/information-barriers) | Segment your SharePoint data and users to restrict unwanted communication and collaboration between groups and avoid conflicts of interest in your organization | [Use information barriers with SharePoint](/sharepoint/information-barriers)|

## Information protection

Microsoft Information Protection (MIP) capabilities included with Microsoft Purview help you discover, classify, and protect sensitive information in SharePoint. The follow sections describe the MIP capabilities included with Microsoft Purview and give you the tools to [know your data](#know-your-data), [protect your data](#protect-your-data), and [prevent data loss](#prevent-data-loss).

### Know your data

The following table describes capabilities to help you your SharePoint data landscape and identify sensitive data across your hybrid environment.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:--------------------|
|[Sensitive information types](/microsoft-365/compliance/sensitive-information-type-learn-about)| Identifies sensitive data by using built-in or custom regular expressions or a function. Corroborative evidence includes keywords, confidence levels, and proximity.| [Customize a built-in sensitive information type](/microsoft-365/compliance/customize-a-built-in-sensitive-information-type)|
|[Trainable classifiers](/microsoft-365/compliance/classifier-learn-about)| Identifies sensitive data by using examples of the data you're interested in rather than identifying elements in the item (pattern matching). You can use built-in classifiers or train a classifier with your own content.| [Get started with trainable classifiers](/microsoft-365/compliance/classifier-get-started-with) |
|[Data classification](/microsoft-365/compliance/data-classification-overview) | A graphical identification of items in your organization that have a sensitivity label, a retention label, or have been classified. You can also use this information to gain insights into the actions that your users are taking on these items. | [Get started with content explorer](/microsoft-365/compliance/data-classification-content-explorer) <p> [Get started with activity explorer](/microsoft-365/compliance/data-classification-activity-explorer) |

### Protect your data

The following table describes protection actions that include encryption, access restrictions, and visual markings to documents stored in SharePoint.

|Capability|What problems does it solve?|Get started|
|:------|:------------|---------------------|
|[Sensitivity labels](/microsoft-365/compliance/sensitivity-labels)| A single solution across apps, services, and devices to label and protect your data as it travels inside and outside your organization. <br /><br /> Example scenarios: <br />- [Manage sensitivity labels for Office apps](/microsoft-365/compliance/sensitivity-labels-office-apps) <br />- [Encrypt documents](/microsoft-365/compliance/encryption-sensitivity-labels)  <br />|[Get started with sensitivity labels](/microsoft-365/compliance/get-started-with-sensitivity-labels) |
|[Double Key Encryption](/microsoft-365/compliance/double-key-encryption)| Under all circumstances, only your organization can ever decrypt protected content or for regulatory requirements, you must hold encryption keys within a geographical boundary. | [Deploy Double Key Encryption](/microsoft-365/compliance/double-key-encryption#deploy-dke)|
|[Service encryption with Microsoft Purview Customer Key](/microsoft-365/compliance/customer-key-overview) | Protects against viewing of data by unauthorized systems or personnel, and complements BitLocker disk encryption in Microsoft datacenters. | [Set up Customer Key for Office 365](/microsoft-365/compliance/customer-key-set-up)|
|[SharePoint Information Rights Management (IRM)](/microsoft-365/compliance/set-up-irm-in-sp-admin-center#irm-enable-sharepoint-document-libraries-and-lists)|Protects SharePoint lists and libraries so that when a user checks out a document, the downloaded file is protected so that only authorized people can view and use the file according to policies that you specify. | [Set up Information Rights Management (IRM) in SharePoint admin center](/microsoft-365/compliance/set-up-irm-in-sp-admin-center)|
[Rights Management connector](/azure/information-protection/deploy-rms-connector) |Protection-only for existing on-premises deployments that use SharePoint Server, or file servers that run Windows Server and File Classification Infrastructure (FCI). | [Steps to deploy the RMS connector](/azure/information-protection/deploy-rms-connector#steps-to-deploy-the-rms-connector)
|[Microsoft Defender for Cloud Apps](/cloud-app-security/what-is-cloud-app-security)| Discovers, labels, and protects sensitive information that resides in data stores that are in the cloud. | [Discover, classify, label, and protect regulated and sensitive data stored in the cloud](/cloud-app-security/best-practices#discover-classify-label-and-protect-regulated-and-sensitive-data-stored-in-the-cloud)|

### Prevent data loss

The following table describes data loss prevention capabilities that help you prevent accidental oversharing of sensitive information in SharePoint.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:---------------------|
|[Data loss prevention](/microsoft-365/compliance/dlp-learn-about-dlp)| Helps prevent unintentional sharing of sensitive items. | [Get started with the default DLP policy](/microsoft-365/compliance/get-started-with-the-default-dlp-policy)|
|[Microsoft 365 data loss prevention on-premises scanner](/microsoft-365/compliance/dlp-on-premises-scanner-learn)|Extends DLP monitoring of file activities and protective actions for those files to on-premises file shares and SharePoint folders and document libraries.|[Get started with Microsoft 365 data loss prevention on-premises scanner (preview)](/microsoft-365/compliance/dlp-on-premises-scanner-get-started)|

## Information governance

Use Microsoft Information Governance capabilities in Microsoft 365 to govern your SharePoint content for compliance or regulatory requirements. The following table describes the capabilities to help you keep the content you need you and delete what you don't need.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Retention policies and retention labels](/microsoft-365/compliance/retention)<br /><br />[Learn about retention for SharePoint and OneDrive](/microsoft-365/compliance/retention-policies-sharepoint) | Retain or delete content with policy management for SharePoint documents | [Create and configure retention policies](/microsoft-365/compliance/create-retention-policies) <br /><br /> [Create retention labels for exceptions to your retention policies](/microsoft-365/compliance/create-retention-labels-information-governance)|