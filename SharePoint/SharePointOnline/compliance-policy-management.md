---
title: "Compliance capabilities for SharePoint data in Microsoft 365"
f1.keywords:
- NOCSH
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
ms.topic: overview
ms.service: O365-seccomp
ms.collection: m365-security-compliance
ms.localizationpriority: high
search.appverid: 
- MOE150
- MET150
recommendations: false
description: "Learn about information governance, information protection, eDiscovery, and auditing capabilities in SharePoint in Microsoft 365."
---

# Learn about compliance for SharePoint

Microsoft 365 offers a full suite of tools and capabilities to maintain compliance for data stored in SharePoint and as your users collaborate in SharePoint. Review these capabilities and consider how they map to your business needs, the sensitivity of your data, and the scope of people that your users need to collaborate with.

This article provides a quick reference (and links to more information) for the compliance capabilities for SharePoint that are available in Microsoft 365.

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

## Records management

The following table describes the lifecycle management capabilities to manage high-value SharePoint items for legal, business, or regulatory obligations.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Records management](/microsoft-365/compliance/records-management)| A single solution for documents that incorporates flexible retention and deletion schedules and requirements to support the full lifecycle of your content with records declaration and defensible disposition when needed |[Get started with records management](/microsoft-365/compliance/get-started-with-records-management) |

## eDiscovery

Electronic discovery, or eDiscovery, is the process of identifying and delivering electronic information that can be used in internal and external investigations, and as evidence in legal cases. You can use eDiscovery tools in Microsoft 365 to search for content in SharePoint and OneDrive (as well as other Microsoft 365 services such as Exchange Online and Microsoft Teams). For more information, see [eDiscovery solutions in Microsoft 365](/microsoft-365/compliance/ediscovery).

The following table describes the eDiscovery tools to search for, preserve, review, and export content stored in SharePoint.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Content search](/microsoft-365/compliance/content-search)| Best used as a search tool to discover content in internal investigations and for responding to security incidents.|[Search for content using the Content search tool](/microsoft-365/compliance/search-for-content) |
|[eDiscovery (Standard)](/microsoft-365/compliance/get-started-core-ediscovery)|Lets you create eDiscovery cases and assign eDiscovery managers to specific cases. eDiscovery (Standard) also lets you associate searches and exports with a case and lets you preserve content that's relevant to the case.| [Create an eDiscovery hold](/microsoft-365/compliance/create-ediscovery-holds)<br /><br /> [Search for content in an case](/microsoft-365/compliance/search-for-content-in-core-ediscovery)<br /><br />[Export content from a case](/microsoft-365/compliance/export-content-in-core-ediscovery)|
|[eDiscovery (Permium)](/microsoft-365/compliance/overview-ediscovery-20)| Provides an end-to-end workflow to identify, preserve, collect, review, analyze, and export content that's responsive to your organization's internal and external investigations.  |[Set up eDiscovery (Permium)](/microsoft-365/compliance/get-started-with-advanced-ediscovery) |

## Auditing

Microsoft 365 auditing solutions provide an integrated solution to help organizations effectively respond to security events, forensic investigations, internal investigations, and compliance obligations. Hundreds of user and admin operations performed in SharePoint and OneDrive (as well as thousands of operations for other Microsoft 365 services) are captured, recorded, and retained in your organization's unified audit log. Audit records for these events are searchable by IT admins, compliance, and legal investigators in your organization. This capability provides visibility into SharePoint activities performed across your Microsoft 365 organization. For more information, see [Auditing solutions in Microsoft 365](/microsoft-365/compliance/auditing-solutions-overview).

The following table describes auditing capabilities in Microsoft 365.

|Capability|What problems does it solve?|Get started|
|:------|:------------|:----------------------------|
|[Audit (Standard)](/microsoft-365/compliance/set-up-basic-audit)|Provides the ability to log and search for audited activities in SharePoint and OneDrive.|[Search the audit log](/microsoft-365/compliance/search-the-audit-log-in-security-and-compliance)<br /><br /> [Audited activities](/microsoft-365/compliance/search-the-audit-log-in-security-and-compliance#audited-activities) <br /><br /> [Use sharing auditing in the audit log](/microsoft-365/compliance/use-sharing-auditing)|
|[Audit (Advanced)](/microsoft-365/compliance/advanced-audit)|Builds on the capabilities of Audit (Standard) by providing audit log retention policies, longer retention of audit records, and high-value crucial events, such as when a person searches for items in SharePoint. |[Set up Audit (Advanced)](/microsoft-365/compliance/set-up-advanced-audit)|