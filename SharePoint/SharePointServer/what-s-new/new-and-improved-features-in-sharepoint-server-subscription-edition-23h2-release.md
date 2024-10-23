---
ms.date: 09/06/2023
title: "New and improved features in SharePoint Server Subscription Edition Version 23H2"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 23H2."
---

# New and improved features in SharePoint Server Subscription Edition Version 23H2

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 23H2 feature update.

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 23H2 feature update.

|**Feature**|**Release ring**|**More information**|
|:-----|:-----|:-----|
|  **Private key management in certificate management**  |  Standard release  |  For more information, see [Private key management in certificate management](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#private-key-management-in-certificate-management). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update.   |
|  **Support for wildcard host header bindings**  |  Standard release  | For more information, see [Support for wildcard host header bindings](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#support-for-wildcard-host-header-bindings). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update. |
|  **Expanded usage of modern sharing dialog**  |  Standard release  | For more information, see [Expanded usage of modern sharing dialog](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#expanded-usage-of-modern-sharing-dialog). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update. |
|  **Column totals in modern list views**  |  Standard release  | For more information, see [Column totals in modern list views](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#column-totals-in-modern-list-views). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update.   |
|  **Enhanced Quick Chart web part**  |  Standard release  | For more information, see [Enhanced Quick Chart web part](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#enhanced-quick-chart-web-part). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update. |
|  **Improved file picker**  |  Standard release  | For more information, see [Improved file picker](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release#improved-file-picker). <br/> <br/> This was part of *Early release* in the Version 23H1 feature update.   |
|  **AMSI integration enabled by default**  |  Standard release  | For more information, see [AMSI integration enabled by default](#amsi-integration-enabled-by-default). |
|  **AMSI health analyzer rule**  |  Standard release  | For more information, see [AMSI health analyzer rule](#amsi-health-analyzer-rule). |
|  **People Picker supports LDAPS (TLS connection encryption)**  |  Standard release  |  For more information, see [People Picker supports LDAPS (TLS connection encryption)](#people-picker-supports-ldaps-tls-connection-encryption). |
|  **Search crawler uses HTTP 1.1 by default**  |  Standard release  | For more information, see [Search crawler uses HTTP 1.1 by default](#search-crawler-uses-http-11-by-default). |
|  **SharePoint Framework (SPFx) component upgrades**  |  Standard release  |  For more information, see  [SharePoint Framework (SPFx) component upgrades](#sharepoint-framework-spfx-component-upgrades). |
|  **New PowerShell cmdlets to manage feature release rings** |  Standard release  |  For more information, see [New PowerShell cmdlets to manage feature release rings](#new-powershell-cmdlets-to-manage-feature-release-rings). |
|  **Custom branding in the Suite Bar**  |  Early release   |  For more information, see [Custom branding in the Suite Bar](#custom-branding-in-the-suite-bar). |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 23H2.

> [!NOTE]
> Features previously introduced in the Version 23H1 feature update will not be described here. For more information on Version 23H1, see [New and improved features in SharePoint Server Subscription Edition Version 23H1](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release). 

### AMSI integration enabled by default

Antimalware Scan Interface (AMSI) integration allows AMSI-capable antimalware solutions to scan `HTTP` and `HTTPS` requests that are sent to SharePoint Server. If a request is deemed to be dangerous by that antimalware solution, AMSI can block the request from being processed by SharePoint Server, providing an additional layer of protection from cybersecurity attacks.

Although the AMSI integration feature was first introduced in SharePoint Server Subscription Edition Version 22H2, it wasn't enabled by default. Customers had to enable the feature on each web application that they wanted to protect in the farm. Since then, we've seen security attacks continue to become more sophisticated and the potential impact to customers has grown.

To help prevent successful security attacks and improve the overall security of customer environments, AMSI integration will be enabled by default for all web applications starting with the Version 23H2 feature update. Customers only need to install the update and run the SharePoint Products Configuration Wizard to trigger the upgrade action. If customers skip installing the September 2023 Public Update, this change will be triggered by the next public update they install that contains the Version 23H2 feature update.

If customers don't want AMSI integration to be enabled in their SharePoint Server farms, they can install the Version 23H2 feature update, run the SharePoint Products Configuration Wizard, and then follow the standard steps to disable the feature in their web applications. If you follow these steps, SharePoint won't attempt to re-enable the feature when installing future public updates.

For more information, see [Configure AMSI integration with SharePoint Server](/sharepoint/security-for-sharepoint-server/configure-amsi-integration).

### AMSI health analyzer rule

SharePoint Server Subscription Edition Version 23H2 further improves AMSI protection with the introduction of a SharePoint health analyzer rule. This health rule is designed to confirm that AMSI protection is functioning as expected and notify SharePoint farm administrators when it isn't.

Once an hour, this health analyzer rule will check to see if AMSI integration is enabled on any web applications in the farm. If it is, the health analyzer rule will send simulated web requests through AMSI on every server in the farm that hosts a web application. It checks to see if AMSI returns the expected status code showing that the request has been successfully scanned. If any of the simulated web requests don't result in a successful status code (meaning AMSI didn't successfully scan the simulated web request), then this health analyzer rule will record a failure. The health analyzer rule report in Central Administration will list which servers in the farm experienced a failure and recommended steps to fix it.

For more information, see [Antimalware Scan Interface (AMSI) protection may not be working](/sharepoint/technical-reference/amsi-protection-may-not-be-working).

### People Picker supports LDAPS (TLS connection encryption)

As organizations become more aware of the risks of unencrypted communication over a network, some are choosing to implement policies that require encryption for all network connections. `HTTP` is one of the most common protocols that organizations want to protect, but there are other network communication protocols as well. One of those is the Lightweight Directory Access Protocol (LDAP), which is used by applications to access directory services. The SharePoint People Picker feature uses LDAP to look up users and groups in Active Directory forests and domains. LDAP is not an encrypted protocol by default, although there are several options to enable encryption with it.

To better support organizations that want to require encryption for LDAP traffic, the SharePoint People Picker feature has added support for Secure LDAP (LDAPS) in SharePoint Server Subscription Edition Version 23H2. This allows the People Picker to use TLS connection encryption to protect LDAP traffic to TCP ports 636 and 3269.

To enable Secure LDAP (LDAPS) in the SharePoint People Picker, use the SecureSocketsLayer switch parameter with the *Set-SPPeoplePickerConfig* and *Add-SPPeoplePickerSearchADDomain* PowerShell cmdlets.

For more information, see [Configure People Picker in SharePoint Server Subscription Edition](/sharepoint/administration/configure-people-picker-subscription-edition).

### Search crawler uses HTTP 1.1 by default

Previously, a SharePoint Search Service Application would crawl `HTTP` or `HTTPS`-based content sources using the `HTTP` 1.0 protocol. Although this is a valid version of the `HTTP` protocol, some network and security infrastructure may choose to block requests that use this protocol version.

To ensure better compatibility with modern network and security infrastructure, SharePoint Search Service Applications will now crawl `HTTP` and `HTTPS`-based content sources using the `HTTP` 1.1 protocol by default. `HTTP` 1.1 is a well-supported protocol across the ecosystem and we don't anticipate any negative impact as a result of this change in our default behavior.

Customers who wish to directly control which `HTTP` protocol version is used for each of their content sources can do so by specifying the HttpProtocol parameter with the *New-SPEnterpriseSearchCrawlContentSource* and *Set-SPEnterpriseSearchCrawlContentSource* PowerShell cmdlets.

For more information, see [Add, edit, or delete a content source in SharePoint Server](/sharepoint/search/add-edit-or-delete-a-content-source).

### SharePoint Framework (SPFx) component upgrades

SharePoint Server Subscription Edition Version 23H2 adds support for React version 16 and Office UI Fabric React 7, allowing developers to utilize these newer component versions in their SharePoint Framework solutions. Microsoft will continue to improve and expand the capabilities of SharePoint Framework in SharePoint Server Subscription Edition in future feature updates.

For more information, see [SharePoint Framework development with SharePoint Server 2019 and Subscription Edition](/sharepoint/dev/spfx/sharepoint-2019-and-subscription-edition-support) and [Upgrade components in SharePoint Framework development with SharePoint Server Subscription Edition](/sharepoint/dev/spfx/sharepoint-2019-and-subscription-edition-support?formCode=MG0AV3).

### New PowerShell cmdlets to manage feature release rings

When Microsoft released the Version 22H2 feature update for SharePoint Server Subscription Edition, it included the concept of feature release rings to support its new evergreen experience. Feature release rings allow Microsoft to introduce new feature experiences in stages. New feature experiences that are ready for production use are typically first introduced in the **Early release** ring. Once the new feature experiences are ready for all customers to use by default, they're moved into the **Standard release** ring.

SharePoint Server Subscription Edition farms are in the Standard release ring by default, but organizations can choose to move their SharePoint farms to Early release or Standard release at any time. Up until now, organizations could only make this choice through the Feature Release Preference page in SharePoint Central Administration. This made it challenging to configure this preference in scripted deployments.

Microsoft now adds new PowerShell cmdlets to manage the feature release preference in the farm. Those cmdlets are:

- Get-SPFeatureReleasePreference
- Set-SPFeatureReleasePreference -FeatureReleaseRing {Early | Standard}

For more information, see [Feature release rings](/sharepoint/administration/feature-release-rings).

### Custom branding in the Suite Bar

The SharePoint Server modern UX provides a powerful yet intuitive user interface that scales from desktop to mobile devices. However, the architecture of the modern UX limited the opportunities for organizations to apply custom branding to the Suite Bar, which is the global navigation bar that provides access to the App Launcher, contextual settings menu, and user welcome control in SharePoint sites.

SharePoint Server Subscription Edition Version 23H2 introduces the ability for organizations to apply custom branding in the Suite Bar to better align with their branding standards. SharePoint farm administrators will be able to specify custom text, logos, hyperlinks, and color schemes in the Suite Bar that apply to all sites within a web application.

For more information, see [Custom branding in Suite Navigation Bar](/sharepoint/sites/custom-branding-in-suite-bar).
