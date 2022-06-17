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