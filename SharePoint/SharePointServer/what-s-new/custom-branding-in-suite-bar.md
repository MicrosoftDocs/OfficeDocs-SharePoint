---
title: "New and improved features in SharePoint Server Subscription Edition Version 23H2"
ms.reviewer: 
ms.author: v-smandalika
author: v-smandalika
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.date: 08/31/2023
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

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features in SharePoint Server Subscription Edition:


|Feature  |Release Ring  |More information  |
|---------|---------|---------|
|**Private key management in certificate management** <br/>     |   Standard release      |    Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.     |
|**Support for wildcard host header bindings** <br/>    |  Standard release       |  Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.       |
|**Expanded usage of modern sharing dialog** <br/>    | Standard release        |    Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.     |
|**Column totals in modern list views**  <br/>   |  Standard release       |     Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.    |
|**Enhanced Quick Chart web part** <br/>    |    Standard release     |     Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.    |
|**Improved file picker** <br/>    |   Standard release      |  Early release feature in 23H1 feature update; promoted to Standard release in 23H2 feature update.       |
|**AMSI integration enabled by default** <br/>    |  Standard release       |   New in 23H2 feature update.      |
|**AMSI health analyzer rule** <br/>    |  Standard release       |  New in 23H2 feature update.       |
|**People Picker supports LDAPS (TLS connection encryption)** <br/>    |   Standard release      |   New in 23H2 feature update.      |
|**Search crawler uses HTTP 1.1 by default** <br/>    |  Standard release       |   New in 23H2 feature update.      |
|**SharePoint Framework (SPFx) component upgrades** <br/>    |   Standard release      |   New in 23H2 feature update.      |
|**New PowerShell cmdlets to manage feature release rings** <br/>    | Standard release        |     New in 23H2 feature update.    |
|**Custom branding in the Suite Bar** <br/>    |    Early release     |     New in 23H2 feature update.    |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 23H2.

> [!NOTE]
> Features previously introduced in the Version 23H1 feature update won't be described here. See [New and improved features in SharePoint Server Subscription Edition Version 22H2](new-and-improved-features-in-sharepoint-server-subscription-edition-23h1-release.md) for descriptions of those features.

### AMSI integration enabled by default

Antimalware Scan Interface (AMSI) integration allows AMSI-capable antimalware solutions to scan HTTP and HTTPS requests that are sent to SharePoint Server. If a request is deemed to be dangerous by that antimalware solution, AMSI can block the request from being processed by SharePoint Server, providing an extra layer of protection from cybersecurity attacks.

Although the AMSI integration feature was first introduced in SharePoint Server Subscription Edition Version 22H2, it wasn't enabled by default. Customers had to enable the feature on each web application that they wanted to protect in the farm. Since that time, we've seen security attacks continue to become more sophisticated, and the potential impact to customers has grown.

To help prevent successful security attacks and to improve the overall security of customer environments, AMSI integration will be enabled by default for all web applications starting with the Version 23H2 feature update. Customers won't need to take any further steps beyond installing the update and running the SharePoint Productions Configuration Wizard to trigger the upgrade action. If customers skip installing the September 2023 Public Update (PU), this change will be triggered when they install the next public update that contains the Version 23H2 feature update.
If customers don't want AMSI integration to be enabled in their SharePoint Server farms, they can install the Version 23H1 feature update, run the SharePoint Products Configuration Wizard, and then follow the standard steps to disable the feature in their web applications. If you follow these steps, SharePoint won't attempt to re-enable the feature when installing future PUs.

For more information, see [Configure AMSI integration with SharePoint Server](../security-for-sharepoint-server/configure-amsi-integration.md).

### AMSI health analyzer rule

SharePoint Server Subscription Edition Version 22H2 further improves AMSI protection with the introduction of a SharePoint health analyzer rule. This health rule is designed to confirm that AMSI protection is functioning as expected and to notify SharePoint farm administrators when it isn’t.

Once an hour, this health analyzer rule will check to see if AMSI integration is enabled on any web applications in the farm. If it's enabled, the health analyzer rule will send simulated web requests through the AMSI API on every server in the farm that hosts a web application. It checks to see if the API returns the expected status code, showing that the request has been successfully scanned. If AMSI API calls don’t return a successful result code (meaning AMSI didn’t successfully scan the simulated web request), then this health analyzer rule will record a failure. The health analyzer rule report in Central Administration will list which servers in the farm experienced a failure, and will recommend steps to fix it.

The administrator can see the failure message in the health analyzer rule report, as shown in the following screenshot:

:::image type="content" source="../media/health-analyzer-rule-report.png" alt-text="Screenshot showing the Health analyzer rule report page." lightbox="../media/health-analyzer-rule-report.png":::

To troubleshoot the issue of AMSI protection not working, see [Antimalware Scan Interface (AMSI) protection may not be working](../technical-reference/amsi-protection-may-not-be-working.md).

### People Picker supports LDAPS (TLS connection encryption)

As organizations become more aware of the risks of unencrypted communication over a network, some are choosing to implement policies that require encryption for all network connections. HTTP is one of the most common protocols that organizations want to protect, but there are other network communication protocols as well. One of those protocols is the Lightweight Directory Access Protocol (LDAP), which is used by applications to access directory services. The SharePoint People Picker feature uses LDAP to look up users and groups in Active Directory forests and domains. LDAP isn't an encrypted protocol by default, although there are several options to enable encryption with it.

To better support organizations that want to require encryption for LDAP traffic, the SharePoint People Picker feature has added support for Secure LDAP (LDAPS) in SharePoint Server Subscription Edition Version 23H2. This feature allows the People Picker to use TLS connection encryption to protect LDAP traffic through encrypted communication with Active Directory over TCP ports 636 and 3269.

To enable Secure LDAP (LDAPS) in the SharePoint People Picker, use the `SecureSocketsLayer switch` parameter with the **Set-SPPeoplePickerConfig** and **Add-SPPeoplePickerSearchADDomain** PowerShell cmdlets.

For more information, see [Plan for People Picker in SharePoint](../administration/plan-for-people-picker.md).

### Search crawler uses HTTP 1.1 by default

Previously, a SharePoint Search Service Application would crawl HTTP or HTTPS-based content sources using the HTTP 1.0 protocol. Although this version is a valid version of the HTTP protocol, some network and security infrastructure may choose to block requests that use this protocol version.

To ensure better compatibility with modern network and security infrastructure, SharePoint Search Service Applications will now crawl HTTP and HTTPS-based content sources using the HTTP 1.1 protocol by default. HTTP 1.1 is a well-supported protocol across the ecosystem and we don't anticipate any negative impact as a result of this change in our default behavior.

Customers who wish to directly control which HTTP protocol version is used for each of their content sources can do so by specifying the `HttpProtocol` parameter with the **New-SPEnterpriseSearchCrawlContentSource** and **Set-SPEnterpriseSearchCrawlContentSource** PowerShell cmdlets.

You can specify either of the following options of the `HttpProtocol` parameter, with which you can use the **New-SPEnterpriseSearchCrawlContentSource** and **Set-SPEnterpriseSearchCrawlContentSource** PowerShell cmdlets:

- **Default**: This option refers to the system default one, currently HTTP 1.1.
- **Http_1_0**: This option refers to the HTTP 1.0 protocol.
- **Http_1_1**: This option refers to the HTTP 1.1 protocol that you can revert to once you came out of the default mode to try using other options.

For more information, see [Add, edit, or delete a content source in SharePoint Server](../search/add-edit-or-delete-a-content-source.md).

### SharePoint Framework (SPFx) component upgrades

SharePoint Server Subscription Edition Version 23H2 adds support for React version 16 and Office UI Fabric React 7, allowing developers to utilize these newer component versions in their SharePoint Framework solutions. 

> [!NOTE]
> Because the support for React version 16 and Office UI Fabric React 7 were not made as part of a broader update to the SharePoint Framework (SPFx), some manual configuration of the development environment must be completed in order to utilize them.

Microsoft will continue to improve and expand the capabilities of SharePoint Framework in SharePoint Server Subscription Edition in future feature updates.

For more information about improvements in SharePoint Server Subscription Edition, see.

### New PowerShell cmdlets to manage feature release rings

When Microsoft released the Version 22H2 feature update for SharePoint Server Subscription Edition, it included the concept of feature release rings to support its new evergreen experience. Feature release rings allow Microsoft to introduce new feature experiences in stages. New feature experiences that are ready for production use are typically first introduced in the Early release ring. Once the new feature experiences are ready for all customers to use by default, they’re moved into the Standard release ring.

SharePoint Server Subscription Edition farms are in the Standard release ring by default, but organizations can choose to move their SharePoint farms to Early release or Standard release at any time. Up until now, organizations could only make this choice through the **Feature Release Preference** page in SharePoint Central Administration, making it challenging to configure this preference in scripted deployments.

Microsoft now adds new PowerShell cmdlets to manage the feature release preference in the farm. Those cmdlets are:

- Get-SPFeatureReleasePreference
- Set-SPFeatureReleasePreference -FeatureReleaseRing {Early | Standard}

For more information, see [Feature release rings](../administration/feature-release-rings.md).

### Custom branding in the Suite Navigation Bar

The SharePoint Server modern UX provides a powerful yet intuitive user interface that scales from desktop to mobile devices. However, the architecture of the modern UX limited the opportunities for organizations to apply custom branding to the Suite Navigation Bar, which is the global navigation bar that provides access to the App Launcher, contextual settings menu, and user welcome control in SharePoint sites.

SharePoint Server Subscription Edition Version 23H2 introduces the ability for organizations to apply custom branding in the Suite Bar to better align with their branding standards. SharePoint farm administrators will be able to specify and make updates the following attributes of the Suite Navigation Bar: 

- **SuiteNavAllowOverwrite**: Determines whether the Suite Navigation Bar settings of the web application can be overridden at the site-collection level. The default value is **false**, meaning any attempt to customize the Suite Navigation Bar at the site collection-level will be ignored. When this attribute's value is set to **true**, the web application-level Suite Navigation Bar settings apply to all site collections, except those collections to which explicit customizations have been made.

- **SuiteNavBrandingText**: Specifies the branding text of the Suite Navigation Bar.

- **SuiteNavBrandingLogoUrl**: Specifies a URL location that points to your logo. Ensure that the logo is from within the web application. The logo can be in the BMP, JPG, JPE, JPEG, PNG, GIF, or SVG format.

- **SuiteNavBrandingLogoTitle**: Specifies the title of your logo.

- **SuiteNavBrandingLogoNavigationUrl**: Specifies the URL to which users will navigate when they select the branding text or the logo.

- **SuiteBarBackground**: Sets a color to use for the background of the Suite Navigation Bar. The Suite Navigation Bar appears at the top on every page of your web application. The color value should be in the form #AARRGGBB, #RRGGBB, or #RGB as hex values.

- **SuiteBarText**: Sets a color to use for the text and icons on the Suite Navigation Bar.

- **SuiteNavAccentColor**: Sets a color to use for the background color of buttons on the Suite Navigation Bar when you hover on them.


