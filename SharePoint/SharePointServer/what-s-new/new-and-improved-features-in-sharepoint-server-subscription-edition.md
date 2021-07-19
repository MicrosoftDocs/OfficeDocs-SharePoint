---
title: "New and improved features in SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-bshilpa
author: Benny-54
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition."
---

# New and improved features in SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates to existing features in SharePoint Server Subscription Edition.

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features in SharePoint Server Subscription Edition.

|**Feature Group**|**Features**|**More info**|
|:-----|:-----|:-----|
|Authentication and Identity Management <br/> | <ul><li>Adds support for OpenID Connect (OIDC) 1.0</li><li>Enhanced People Picker for modern authentication</li></ul> | <ul><li>For more information, see [OpenID Connect (OIDC) 1.0 authentication](#OIDCa).</li><li>For more information, see [People Picker improvement for modern authentication](#people).</li></ul> | 
|Deployment and Upgrade <br/> | <ul><li>Adds support for Windows Server 2022</li><li>Adds support for Windows Server Core</li><li>Supports "N - 2" upgrading from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)</li></ul> | <ul><li>For more information, see [Windows Server 2022](#server).</li><li>For more information, see [Windows Server Core](#core).</li><li>For more information, see [Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)](#upgrade).</li></ul> |
|Farm Administration <br/> | <ul><li>Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)</li></ul> | <ul><li>For more information, see [Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)](#fedral).</li></ul> | 
|PowerShell <br/> | <ul><li>SharePoint PowerShell cmdlets converted from snap-in to module</li></ul> | <ul><li>For more information, see [SharePoint PowerShell cmdlets converted from snap-in to module](#snap).</li></ul> |
|Search <br/> | <ul><li>Support for returning list content in modern results page</li></ul> | <ul><li>For more information, see [Support for returning list content in modern results page](#listmrp).</li></ul> |
|Security <br/> | <ul><li>Adds support for TLS 1.3</li><li>Strong TLS encryption by default</li></ul> | <ul><li>For more information, see [TLS 1.3](#tlss).</li><li>For more information, see [Strong TLS encryption by default](#tlsed).</li></ul> |
|Sites, Lists, and Libraries <br/> | <ul><li>Accessibility improvements</li><li>Image and document thumbnails in document libraries and picture libraries</li></ul> | <ul><li>For more information, see [Accessibility improvements across modern UX](#aiamu).</li><li>For more information, see [Image and document thumbnails in document libraries and picture libraries](#idt).</li></ul> |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition.

## Authentication and Identity Management

<a name="OIDCa"> </a>
### OpenID Connect (OIDC) 1.0 authentication

SharePoint Server Subscription Edition adds support for the OpenID Connect (OIDC) 1.0 authentication protocol. OIDC is a modern authentication protocol that makes it easy to integrate applications and devices with your organization's identity and authentication management solutions to better meet your evolving security and compliance needs. For example, customers can enforce authentication policies such as multifactor authentication (MFA), conditional access policies based on device compliance, and more.

SharePoint Server Subscription Edition supports OIDC authentication with identity providers such as Azure Active Directory (AAD), Active Directory Federation Services (AD FS) 2016 or higher, and third-party identity providers that implement the OIDC 1.0 protocol.

To set up OIDC authentication in SharePoint Server, see [OpenID Connect 1.0 authentication](../security-for-sharepoint-server/oidc-1.0-authentication.md).

<a name="people"> </a>
### People Picker improvement for modern authentication

When modern authentication (trusted identity provider) such as SAML 1.1 or OIDC 1.0 is used, the People Picker control can’t search, resolve, and validate users and groups without writing a custom claim provider through C#.

In SharePoint Server Subscription Edition, the People Picker has been enhanced to allow resolving users and groups based on their profiles in the User Profile Application (UPA). UPA must be configured to synchronize users and groups from the trusted identity provider membership store. This allows the People Picker to only resolve valid users and groups without requiring a custom claims provider.

To configure People Picker, see [Enhanced People Picker for modern authentication](../administration/enhanced-people-picker-for-trusted-authentication-method.md).

## Deployment and Upgrade

<a name="server"> </a>
### Windows Server 2022

Windows Server 2022 includes various new features and improvements in virtualization, networking, security, and more, such as:

 - Performance improvements in the Hyper-V virtual switch to reduce the CPU load of virtual machine network communication.
 
 - Performance improvements in both TCP and UDP networking to maximize bandwidth, minimizing packet loss, and reduce CPU load.
 
 - Support for TLS 1.3, the latest and strongest connection encryption standard.
 
 - Support for AES-256-GCM encryption in SMB file sharing, along with compressed file transfers over the network when using the `robocopy.exe` and `xcopy.exe` tools with the `/compress` parameter.
 
SharePoint Server Subscription Edition supports additional security features when deployed with Windows Server 2022 or higher such as support for TLS 1.3 and strong TLS encryption by default. 

> [!NOTE]
> These security features are not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

<a name="core"> </a>
### Windows Server Core

Windows Server Core is a leaner Windows Server deployment type compared to the classic Windows Server with Desktop Experience. Server Core minimizes the number of OS features and services that are installed and running to only those that are truly needed for a server. This reduces the demand on system resources (CPU, RAM, and disk space) and the potential attack surface for security vulnerabilities.

SharePoint Server Subscription Edition adds support for the Windows Server Core deployment type with both Windows Server 2019 and Windows Server 2022. The Windows Server Desktop Experience deployment type remains supported with both Windows Server 2019 and Windows Server 2022.

For more information, see [Installing SharePoint Server Subscription Edition on Windows Server Core](../install/installing-sharepoint-server-subscription-edition-on-windows-server-core.md)

<a name="upgrade"> </a>
### Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)

SharePoint Server Subscription Edition supports both **N - 1** and **N - 2** version-to-version upgrade. You can upgrade directly from the following SharePoint products using the standard database attach upgrade procedure:

 - SharePoint Server 2019 (including Project Server 2019)
 
 - SharePoint Server 2016 (including Project Server 2016)

> [!NOTE]
> Directly upgrading from versions of SharePoint earlier than SharePoint Server 2016 via database attach is not supported. SharePoint 2013, SharePoint 2010, and so on must first be upgraded to either SharePoint Server 2016 or SharePoint Server 2019 via database attach before upgrading to SharePoint Server Subscription Edition.

For more information:

 - To install SharePoint Server Subscription Edition, see [Installation overview for SharePoint Server Subscription Edition](../install/install-overview-spserver-se.md).
 
 - To upgrade to SharePoint Server Subscription Edition, see [Upgrade to SharePoint Server Subscription Edition](../upgrade-and-update/upgrade-to-sharepoint-server-subscription-edition.md).
 
## Farm Administration
  
<a name="fedral"> </a>  
### Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)
  
In SharePoint Server, some service applications can be shared across server farms. Microsoft supports service applications published by a SharePoint Server Subscription Edition farm being consumed by the following versions of SharePoint Server:

 - SharePoint Server Subscription Edition (N)

 - SharePoint Server 2019 (N - 1)

 - SharePoint Server 2016 (N - 2)

For more information, see [Share service applications across farms in SharePoint Server](/sharepoint/administration/share-service-applications-across-farms).

## PowerShell

<a name="snap"> </a>
### SharePoint PowerShell cmdlets converted from snap-in to module

SharePoint Server PowerShell cmdlets are now installed via a PowerShell module instead of a PowerShell snap-in. This follows the recommended packaging approach from PowerShell and allows us to better support the PowerShell experience.  
  
It includes the following benefits:
  
  - SharePoint Server cmdlets are now automatically available in all Windows PowerShell consoles.  You don't have to launch the SharePoint Management Shell or use the `Add-PSSnapin` cmdlet to access the SharePoint Server cmdlets.
  
  - PowerShell will be able to download updated SharePoint Server cmdlet help content over the Internet.
  
> [!NOTE]
> The SharePoint Management Shell will continue to be included in the product to provide a familiar PowerShell UI for managing SharePoint Server. The SharePoint Server PowerShell cmdlets will continue to require Windows PowerShell. These cmdlets will not be compatible with PowerShell Core 6.x or PowerShell 7.x.

## Search

<a name="listmrp"> </a>
### Support for returning list content in modern results page
  
Lists and list items are now searchable in the modern UX. List item results will be included in the **All** category of the modern search result page.

## Security

<a name="tlss"> </a>
### TLS 1.3 

Transport Layer Security (TLS) is a cryptographic protocol that encrypts communication between two endpoints, such as between a web browser and an HTTPS web site. TLS 1.3 is the latest and most secure version of the TLS protocol.

SharePoint Server Subscription Edition supports TLS 1.3 by default when deployed with Windows Server 2022 or higher. 

> [!NOTE]
> TLS 1.3 is not available and is not supported when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.
  
> [!NOTE]
> Not all applications in your software ecosystem may support TLS 1.3. Check with your software vendors to determine if your other applications support TLS 1.3. SharePoint Server Subscription Edition can fall back to earlier TLS protocol versions when connecting with systems that don't support TLS 1.3 unless the customer has disabled earlier TLS protocol versions.

For more information, see [TLS 1.3 Support](../security-for-sharepoint-server/tls-support-1.3.md).
 
<a name="tlsed"> </a> 
### Strong TLS encryption by default

SharePoint Server Subscription Edition will use the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to SharePoint sites only use the strongest encryption by default. SharePoint Server will configure itself to enforce the minimum TLS version and cipher suite requirements of HTTP/2 on its SSL bindings regardless of whether the connection uses HTTP/2. 

Specifically:

 - The SSL/TLS protocol version negotiated must be TLS 1.2 or higher.

 - The TLS cipher suite negotiated must support forward secrecy and AEAD encryption modes such as GCM.

Customers can allow legacy encryption to be used if needed for backward compatibility with older software that doesn't support strong TLS protocol versions and cipher suites.

> [!NOTE]
> Strong TLS encryption by default is not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

For more information, see [Strong TLS Encryption](../security-for-sharepoint-server/strong-tls-encryption.md).

## Sites, Lists, and Libraries

<a name="aiamu"> </a>
### Accessibility improvements across modern UX
  
SharePoint Server Subscription Edition includes numerous accessibility improvements across the modern UX to ensure that all users can be productive with SharePoint.

<a name="idt"> </a>
### Image and document thumbnails in document libraries and picture libraries

SharePoint Server Subscription Edition can render thumbnails of files in the Tiles view of document libraries and picture libraries. SharePoint will render thumbnails of popular image file formats such as PNG, JPEG, GIF, and more. And if you've linked your SharePoint Server farm to an Office Online Server farm, SharePoint will also be able to render thumbnails of popular document formats such as PDFs, Word documents, PowerPoint documents, and Rich Text Files.

## Related articles

[Installation overview for SharePoint Server Subscription Edition](../install/install-overview-spserver-se.md)

[System requirements for SharePoint Server Subscription Edition](../install/system-requirements-for-sharepoint-subscription-edition.md)

[Upgrade to SharePoint Server Subscription Edition](../upgrade-and-update/upgrade-to-sharepoint-server-subscription-edition.md)



