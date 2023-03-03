---
title: "New and improved features in SharePoint Server Subscription Edition Version 23H1"
ms.reviewer: 
ms.author: v-bshilpa
author: Benny-54
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
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 23H1."
---

# New and improved features in SharePoint Server Subscription Edition Version 23H1

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates introduced in the SharePoint Server Subscription Edition Version 23H1 feature update.

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features in SharePoint Server Subscription Edition.

|**Feature**|**Release rings**|**More information**|
|:-----|:-----|:-----|
|**Copy and move improvement in modern document library** <br/> |Standard release  <br/> |For more information, see [Copy and move improvement in modern document library](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#copy-and-move-improvement-in-modern-document-library).<br/> |
|**Bulk editing in modern lists** <br/> |Standard release <br/> |For more information, see [Bulk editing in modern lists](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#bulk-editing-in-modern-lists).  <br/> |
|**Column formatting enhancement** <br/> |Standard release <br/> |For more information, see [Column formatting enhancement](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#column-formatting-enhancement). <br/> |
|**Button web part** <br/> |Standard release  <br/> |For more information, see [Button web part](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#button-web-part). <br/> |
|**Choose the default site language in the modern self-service site creation pane** <br/> |Standard release  <br/> |For more information, see [Choose the default site language in the modern self-service site creation pane](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#choose-the-default-site-language-in-the-modern-self-service-site-creation-pane). <br/> |
|**New SharePoint RESTful ListData.svc implementation** <br/> |Standard release  <br/> |For more information, see [New SharePoint RESTful ListData.svc implementation](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release#new-sharepoint-restful-listdatasvc-implementation). <br/> |
|**Unified "uber" patches** <br/> |Standard release <br/> |For more information, see [Unified "uber" patches](#unified-uber-patches). <br/> |
|**Support for SharePoint Framework (SPFx) version 1.5.1** <br/> |Standard release <br/> |For more information, see [Support for SharePoint Framework (SPFx) version 1.5.1](#sfsf).  <br/> |
|**New PowerShell cmdlets for variations feature** <br/> |Standard release <br/> |For more information, see [New PowerShell cmdlets for variations feature](#new-powershell-cmdlets-for-variations-feature).  <br/> |
|**SharePoint Server recompiled with Visual C++ 2022** <br/> |Standard release <br/> |For more information, see [SharePoint Server recompiled with Visual C++ 2022](#ssrwv). <br/> |
|**Private key management in certificate management** <br/> |Early release <br/> |For more information, see [Private key management in certificate management](#private-key-management-in-certificate-management).  <br/> |
|**Support for wildcard host header bindings** <br/> |Early release <br/> |For more information, see [Support for wildcard host header bindings](#support-for-wildcard-host-header-bindings). <br/> |
|**Expanded usage of modern sharing dialog** <br/> |Early release <br/> |For more information, see [Expanded usage of modern sharing dialog](#expanded-usage-of-modern-sharing-dialog). <br/> |
|**Column totals in modern list views** <br/> |Early release <br/> |For more information, see [Column totals in modern list views](#column-totals-in-modern-list-views). <br/> |
|**Enhanced Quick Chart web part** <br/> |Early release <br/> |For more information, see [Enhanced Quick Chart web part](#enhanced-quick-chart-web-part). <br/> |
|**Improved file picker** <br/> |Early release <br/> |For more information, see [Improved file picker](#improved-file-picker). <br/> |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 23H1.

> [!NOTE]
> Features previously introduced in the SharePoint Server Subscription Edition Version 22H2 feature update will not be described here. See [New and improved features in SharePoint Server Subscription Edition Version 22H2](/sharepoint/what-s-new/new-and-improved-features-in-sharepoint-server-subscription-edition-22h2-release) for descriptions of those features.

### Unified "uber" patches

Up until now, Microsoft would release two separate public updates each month for SharePoint Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition. The first public update was called the **STS** or **core** update and contained all of the language-independent file updates. The second public update was called the **WSSLOC** or **language pack** update and contained all of the language-dependent file updates. Both public updates were required to be installed to fully update a SharePoint farm, although a new language-dependent WSSLOC public update may not have been released every month.

Some SharePoint customers were confused by the need to download and install two separate updates to fully update their SharePoint farm each month. They may mistakenly only download and install one of those updates, which could lead to unexpected behavior in their SharePoint farms due to mismatched updates.

To simplify the process of updating your SharePoint Server farm, Microsoft will now only release a single update each month for SharePoint Server Subscription Edition, starting with the March 2023 public update. This single "uber" update combines all of the fixes that would have previously been released in separate STS and WSSLOC updates.

The single uber updates are cumulative, so you only need to install the latest uber update to be fully up to date with all of the latest fixes for SharePoint Server Subscription Edition. It isn’t necessary to install any of the previous STS or WSSLOC updates before installing the uber update. No additional STS or WSSLOC updates will be released after the February 2023 public updates.

Customers should remember to run the SharePoint upgrade actions in their farm after installing a new update to complete the patching and upgrade process. For more information, see the [Upgrade to SharePoint Server Subscription Edition](/sharepoint/upgrade-and-update/upgrade-to-sharepoint-server-subscription-edition).

For more information, see [Software updates overview for SharePoint Server 2016, 2019, and Subscription Edition](/SharePoint/upgrade-and-update/software-updates-overview?branch=pr-en-us-4897) and [Install a software update for SharePoint Server](/SharePoint/upgrade-and-update/install-a-software-update?branch=pr-en-us-4897).

<a name="sfsf"> </a>
### Support for SharePoint Framework (SPFx) version 1.5.1

Previous versions of SharePoint Server Subscription Edition supported SharePoint Framework (SPFx) version 1.4.1. To expand the customization scenarios that SharePoint Server Subscription Edition supports, the 23H1 feature update adds support for SharePoint Framework (SPFx) version 1.5.1. 

This is one step on our long-term journey to improve and expand the capabilities of SharePoint Framework in SharePoint Server Subscription Edition.
For more information about SharePoint Framework version 1.5.1, see [SharePoint Framework v1.5.1 release notes](/sharepoint/dev/spfx/release-1.5.1).

### SharePoint Hybrid Configuration Wizard supports running on Windows Server Core

SharePoint Server Subscription added support for running on Windows Server Core, a leaner Windows Server deployment type that minimizes the number of OS features and services that are installed and running to only those that are essential for a server. However, the SharePoint Hybrid Configuration Wizard didn't support running on Windows Server Core due to some component dependencies that required Windows Server with Desktop Experience. Customers had to have at least one server in their SharePoint farm running on Windows Server with Desktop Experience if they wanted to use the SharePoint Hybrid Configuration Wizard to configure hybrid functionality within their farm.

Starting with the 23H1 feature update, the SharePoint Hybrid Configuration Wizard has been redesigned to no longer have a dependency on components that require Windows Server with Desktop Experience. As a result, customers can now run the SharePoint Hybrid Configuration Wizard on Windows Server Core. Customers will no longer need to keep at least one server in their farm running Windows Server with Desktop Experience to configure hybrid functionality within their farm.
Although the SharePoint Hybrid Configuration Wizard has now added support for Windows Server Core, it also remains compatible with Windows Server with Desktop Experience.

### New PowerShell cmdlets for variations feature

Previous versions of SharePoint Server included an `stsadm.exe -o variationsfixuptool` command to configure the variations feature of SharePoint. However, the `stsadm.exe` command line tool was removed in SharePoint Server Subscription Edition with no PowerShell cmdlets provided to replace this variations functionality.
SharePoint Server Subscription Edition Version 23H1 introduces four new PowerShell cmdlets that replaces the functionality of the `stsadm.exe -o variationsfixuptool` command. 

Those cmdlets are:

 - `Deploy-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`
 - `Repair-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`
 - `Test-SPVariation -Identity <SPWebPipeBind> [-Recurse] [-Label <String>]`
 - `Get-SPVariationJob -Identity <SPWebPipeBind>`

For more information, see [Cmdlet reference for SharePoint Server](/powershell/module/sharepoint-server/).  

<a name="ssrwv"> </a>
### SharePoint Server recompiled with Visual C++ 2022

Previous versions of SharePoint Server Subscription Edition were compiled with the Visual C++ 2019 compiler for unmanaged code. The SharePoint Prerequisite Installer that comes with the SharePoint Server Subscription Edition installed the Visual C++ Redistributable Package for Visual Studio 2015-2019 to support the binaries compiled with that compiler.

To ensure SharePoint Server can take advantage of the latest capabilities and fixes in the Visual C++ libraries, Microsoft has recompiled SharePoint Server Subscription Edition Version 23H1 with the Visual C++ 2022 compiler. The Version 23H1 feature update will automatically install the Visual C++ Redistributable Package for Visual Studio 2015-2022 to support the binaries recompiled with this compiler.
  
### Private key management in certificate management
  
SharePoint Server Subscription Edition introduced a new certificate management feature that allows SharePoint farm administrators to directly manage the deployment and lifecycle of SSL/TLS certificates in their SharePoint Server farms. The certificate management feature would apply a standard set of permissions to the private keys of these certificates regardless of their use cases.

To better support least privileges scenarios and minimize the permissions given to these private keys, SharePoint Server Subscription Edition Version 23H1 applies more granular and sophisticated permission management for these private keys. The permissions are based on the certificate assignments and will be dynamically updated when the certificate assignments change.

For example, if a certificate is assigned to perform client certificate authentication to an SMTP server, SharePoint ensures the process that’s connecting to the SMTP server has the necessary permissions to use the private key of that certificate. If a certificate is no longer assigned to perform client certificate authentication to an SMTP server, SharePoint removes permissions for that process so it no longer has access to the private key of that certificate.

APIs have been added to the *Microsoft.SharePoint.Administration.CertificateManagement.SPServerCertificate* class to allow third party integration with this functionality.
  
### Support for wildcard host header bindings
  
Previous versions of SharePoint Server Subscription Edition support host header bindings that would allow multiple SharePoint web applications to share the same TCP port. However, SharePoint Server only supported explicit host header bindings such as "sharepoint.example.com". Sometimes customers may want to support multiple host-named site collections across multiple web applications, all using the same TCP port.

SharePoint Server Subscription Edition Version 23H1 adds support for specifying a wildcard host header binding for a web application. This allows you to specify different wildcard bindings across multiple web applications that can share the same TCP port such as `*.external.example.com` and `*.internal.example.com`. You can then provision host-named site collections in the first web application using the `*.external.example.com` DNS naming scheme (such as `site1.external.example.com`, `site2.external.example.com`, etc.) and other host-named site collections in the second web application using the `*.internal.example.com` DNS naming scheme (such as `site1.internal.example.com`, `site2.internal.example.com`, etc.).
  
### Expanded usage of modern sharing dialog
  
In previous releases of SharePoint Server Subscription Edition, using sharing functionality in lists, document libraries, pages, or site contents would trigger the classic sharing dialog, even when using the modern view in a modern Team site or Communication site.

To provide a more intuitive sharing experience, these sharing entry points have been updated to use SharePoint’s modern sharing dialog. The modern sharing dialog is also a more accessible experience.

### Column totals in modern list views
  
SharePoint Server Subscription Edition Version 23H1 adds support for displaying column totals in modern list views just like in classic list views. This option can be enabled in the **save view** feature.
  
### Enhanced Quick Chart web part
  
Previous versions of SharePoint Server Subscription Edition allowed users to manually enter data in the Quick Chart modern web part to render charts on modern pages. However, users were unable to connect the Quick Chart web part to a list or library within the site to consume its data.

SharePoint Server Subscription Edition Version 23H1 enhances the Quick Chart modern web part by adding a **Get data from a list or library on this site** option. Users can now configure the Quick Chart web part to consume data from a list or library within the site.

For more information, see [Use the Quick Chart web part](https://support.microsoft.com/office/use-the-quick-chart-web-part-bcfee244-2408-400b-a9bd-4eca61aead51).
  
### Improved file picker
  
SharePoint Server Subscription Edition Version 23H1 improves the modern file picker (used by the Quick Links and File Viewer web parts) to support more file types: more productivity documents (pdf, Visio), text and code (txt), videos (mp4, mkv, m4v, etc.), audio (mp3, ogg, wav, etc.), models (st). 
