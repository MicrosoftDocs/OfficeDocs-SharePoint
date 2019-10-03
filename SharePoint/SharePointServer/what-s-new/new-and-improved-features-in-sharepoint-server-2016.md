---
title: "New and improved features in SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: e81557fb-5046-4a67-8ec8-fdfda648af68
description: "Learn about the new features and updates to existing features in SharePoint Server 2016."
---

# New and improved features in SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]

Learn about the new features and updates to existing features in SharePoint Server 2016.
  
For a comparison of SharePoint on-premises features between SharePoint 2013 and SharePoint Server 2016 editions, see [SharePoint feature availability across on-premises solutions](http://go.microsoft.com/fwlink/p/?LinkID=760410&amp;clcid=0x409). For new features in SharePoint Server 2016 for end users, see [What's new in SharePoint Server 2016](https://support.office.com/en-us/article/What-s-new-in-SharePoint-Server-2016-089369b5-c3d4-4551-8bed-22b2548abd3b).
  
## Summary of features

The following table provides a summary of the new features that you can try out in this SharePoint Server 2016 release.
  
|**Feature**|**Description**|**More information**|
|:-----|:-----|:-----|
|**Access Services** <br/> |New Access features are available when you deploy Access Services in SharePoint Server 2016 .  <br/> |For more information, see [Access Services plus Access client and server](#access).  <br/> |
|**Compliance features** <br/> |New compliance features for SharePoint Server 2016 include the document deletion and in-place hold policies.  <br/> |For more information, see [Compliance features](#compliance).  <br/> |
|**Customized web parts** <br/> |The compile time for customized XSLT files used for Content Query, Summary Links, and Table of Contents Web Parts is improved.  <br/> |NA  <br/> |
|**Document Library accessibility** <br/> |SharePoint Server 2016 includes new document library accessibility features.  <br/> |For more information, see [Document Library accessibility](#doclib).  <br/> |
|**Durable links** <br/> |Resource-based URLs now retain links when documents are renamed or moved in SharePoint.  <br/> |NA  <br/> |
|**Encrypted Connections** <br/> |SharePoint Server 2016 supports TLS 1.2 connection encryption by default.  <br/> |For more information, see [Encrypted connections](#encrypted).  <br/> |
|**Fast Site Collection Creation** <br/> |The Fast Site Collection Creation feature is a rapid method to create site collections and sites in SharePoint.  <br/> |For more information, see [Fast Site Collection Creation](#FSCC).  <br/> |
|**Filenames - expanded support for special characters** <br/> |SharePoint Server 2016 now supports using some special characters in file names that were blocked in previous versions.  <br/> |For more information, see [File names - expanded support for special characters](#file).  <br/> |
|**Hybrid in SharePoint 2016** <br/> |Hybrid in SharePoint Server 2016 enables you to integrate your on-premises farm with Office 365 productivity experiences, allowing you to adopt the cloud at your own pace.  <br/> |For more information, see [Hybrid in SharePoint Server 2016](#hybrid).  <br/> |
|**Identify and search for sensitive content** <br/> |SharePoint Server 2016 now provides the same data loss prevention capabilities as Office 365.  <br/> |For more information, see [Identify and search for sensitive content in both SharePoint Server 2016 and OneDrive documents](#sensitive).  <br/> |
|**Image and video previews** <br/> |You can now preview images and videos in SharePoint Server 2016 document libraries.  <br/> |For more information, see [Image and video previews](#preview).  <br/> |
|**Information Rights Management** <br/> |SharePoint Server 2016 provides Information Rights Management (IRM) capabilities to secure information by encrypting and securing information on SharePoint libraries with OneDrive for Business.  <br/> |For more information, see [Information Rights Management](#InfoRights).  <br/> |
|**Large file support** <br/> |SharePoint Server 2016 now supports uploading and downloading files larger than 2,047 MB.  <br/> |For more information, see [Large file support](#largefile).  <br/> |
|**MinRole** <br/> |MinRole is a new feature in SharePoint Server 2016 that allows a SharePoint farm administrator to define each server's role in a farm topology.  <br/> |For more information, see [MinRole farm topology](#minrole).  <br/> |
|**Mobile experience** <br/> |SharePoint Server 2016 offers an improved mobile navigation experience.  <br/> |For more information, see [Mobile experience](#mobile).  <br/> |
|**New features in November 2016 PU for SharePoint Server 2016 (Feature Pack 1)** <br/> |The November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) offers seven new features for SharePoint Server 2016.  <br/> |For more information, see [New features in November 2016 PU for SharePoint Server 2016 (Feature Pack 1)](new-features-in-feature-pack-1.md).  <br/> |
|**New controls for working with OneDrive for Business** <br/> |SharePoint Server 2016 provides controls at the top of your personal document folders that make common tasks in OneDrive for Business more accessible.  <br/> |For more information, see [New controls for working with OneDrive for Business](#newcontrols).  <br/> |
|**New Recycle Bin in OneDrive and Team sites** <br/> |SharePoint Server 2016 adds a link for the Recycle Bin in the left navigation area of the OneDrive and Team sites.  <br/> |NA  <br/> |
|**Open Document Format (ODF)** <br/> |SharePoint Server 2016 adds support for Open Document Format (ODF) files to use in document library templates.  <br/> |For more information, see [Open Document Format (ODF) available for document libraries](#ODF).  <br/> |
|**Project Server** <br/> |New Project Server features are available in SharePoint Server 2016.  <br/> |For more information, see [Project Server 2016 ](#project).  <br/> |
|**ReFS file system support** <br/> |SharePoint Server 2016 now supports drives that are formatted with the ReFS file system.  <br/> |For more information about the ReFS file system, see [Resilient File System Overview](http://go.microsoft.com/fwlink/?LinkID=620210&amp;clcid=0x409) and [Resilient file system](http://go.microsoft.com/fwlink/?LinkID=620212&amp;clcid=0x409).  <br/> |
|**SharePoint business intelligence** <br/> |SharePoint Server 2016 now supports SQL Server 2016 CTP 3.1 and the Power Pivot add-in and Power View.  <br/> |For more information about SharePoint business intelligence, see [Power Pivot add-in and Power View are now available to use with SharePoint Server 2016](new-and-improved-features-in-sharepoint-server-2016.md#BI).  <br/> |
|**SharePoint Search** <br/> |SharePoint Search Server Application has significant changes to its deployment.  <br/> |For more information, see [SharePoint Search Service application](#search).  <br/> |
|**Sharing improvements** <br/> |SharePoint Server 2016 has many new sharing improvements available.  <br/> |For more information, see [Sharing](#share).  <br/> |
|**Site Folders view** <br/> |SharePoint Server 2016 provides a new Site Folders view that lets you access the document libraries in sites that you're following.  <br/> |For more information, see [Site folders view](#folders).  <br/> |
|**Sites page pinning** <br/> |This new feature helps you see and follow sites.  <br/> |For more information, see [Sites page pinning](#pin).  <br/> |
|**SMTP Connection Encryption** <br/> |SharePoint Server 2016 supports sending email to SMTP servers that use **STARTTLS** connection encryption.  <br/> |For more information, see [SMTP connection encryption](#smtpcon).  <br/> |
|**SMTP ports (non-default)** <br/> |SharePoint Server 2016 adds support for SMTP servers that use TCP ports other than the default port (25).  <br/> |For more information, see [Use SMTP ports other than the default (25)](#smtpport).  <br/> |
|**Web Application Open Platform Interface Protocol (WOPI)** <br/> |You can now rename files, create new files, and share files from within the WOPI iframe on the browser page.  <br/> |NA  <br/> |
   
## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server 2016.
  
### Access Services plus Access client and server
<a name="access"> </a>

The following new Access features are available when you deploy Access Services in SharePoint Server 2016:
  
- Support apps for Office. For more information, see [Spice up your Access app with add-ins for Office](http://go.microsoft.com/fwlink/p/?LinkID=620215&amp;clcid=0x409).
    
- Access App Upgrade. For more information, see [Upgrade an Access app](http://go.microsoft.com/fwlink/p/?LinkID=620216&amp;clcid=0x4809).
    
- Download in Excel feature available for users to pivot Access tables. For more information, see [Introducing a new feature in Access 2013 web apps-Download in Excel](http://go.microsoft.com/fwlink/p/?LinkID=620218&amp;clcid=0x4809).
    
- With the improved Related Item Control, you can do the following:
    
  - Choose from any existing view for the dialog box on the Related Item Control.
    
  - Add a new item on the Related Item Control when the parent record isn't saved.
    
  - Turn off the **Add link** at the bottom of the Related Item Control. 
    
- The Cascading Combo box is now available in Access. For more information, see [Introducing a new user experience feature in Access web apps: Cascading Controls](http://go.microsoft.com/fwlink/p/?LinkID=620219&amp;clcid=0x4809).
    
### Central Administration is no longer provisioned on all servers by default
<a name="access"> </a>

SharePoint Server 2016 Central Administration is now provisioned on the first server in a farm by default when using the SharePoint Products Configuration Wizard. Central Administration is not provisioned on additional servers in a farm by default.
  
You can provision or unprovision Central Administration on individual servers in a farm, no matter what the server role is by using the following methods:
  
- The **Services on Server** page on **Central Administration \> System Settings**
    
- Microsoft PowerShell cmdlets:
    
  - [New-SPCentralAdministration](/powershell/module/sharepoint-server/New-SPCentralAdministration?view=sharepoint-ps)
    
  - [Remove-SPCentralAdministration](/powershell/module/sharepoint-server/Remove-SPCentralAdministration?view=sharepoint-ps)
    
- The  `psconfig.exe -cmd adminvs` operation 
    
- The **SharePoint Products Configuration Wizard**
    
> [!NOTE]
> The state of Central Administration does not affect whether a server is considered compliant with MinRole. The MinRole health rule will not attempt to provision or unprovision Central Administration. 
  
### Compliance features
<a name="compliance"> </a>

The document deletion policy allows you to delete documents in users' OneDrive for Business sites after specific periods of time. The In-Place Hold policy allows administrators to preserve documents, email, and other files.
  
For more information, see [Overview of document deletion policies](http://go.microsoft.com/fwlink/p/?LinkID=620220&amp;clcid=0x4809).
  
### Document Library accessibility
<a name="doclib"> </a>

The following features are now available for working in SharePoint Server 2016 document libraries:
  
- Landmarks to a page make it easier to navigate, and there are alt text improvements for all major navigation links.
    
- Keyboard shortcuts are provided for the following document tasks:
    
  - Alt + **N** - **N** ew 
    
  - Alt + **E** - **E** dit 
    
  - Alt + **U** - **U** pload 
    
  - Alt + **M** - **M** anage 
    
  - Alt + **S** - **S** hare 
    
  - Alt + **Y** - S **y** nchronization 
    
- Focus improvements, such as keeping focus on prior elements and focus trapping.
    
- Announcements for upload progress.
    
- Announcements for file name and file types when browsing folder and file lists.
    
- Improved callout reading.
    
- Fixed use of color issues for views switcher.
    
- Updates to the Help documentation.
    
### Encrypted connections
<a name="encrypted"> </a>

When you set up an SSL binding in Internet Information Services (IIS) Manager to host your web application, SharePoint uses TLS 1.2 connection encryption if your client application supports it. SharePoint also supports TLS 1.2 connection encryption when connecting to other systems, for example when crawling websites.
  
> [!NOTE]
> A security vulnerability was identified in the SSL 3.0 protocol that can allow an attacker to decrypt data. For enhanced security, some SharePoint features now disable SSL 3.0 connection encryption by default, as well as certain encryption algorithms (for example RC4) with known weaknesses. SharePoint disables SSL 3.0 connection encryption by default for some, but not all features. To ensure that SSL 3.0 is disabled for all features, you should disable it in Windows by editing the Windows Registry. For more information, see the "Disable SSL 3.0 in Windows For Server Software", and "For Client Software", workarounds in [Microsoft Security Advisory 3009008](/security-updates/SecurityAdvisories/2015/3009008). 
  
### Fast Site Collection Creation
<a name="FSCC"> </a>

This new feature provides templates that work at same level as SQL Server, which reduces the round trips required between the SharePoint and SQL servers. Use the **SPSiteMaster** Microsoft PowerShell cmdlets to create sites and site collections quickly. 
  
### File names - expanded support for special characters
<a name="file"> </a>

SharePoint has historically blocked file names that included the **&amp;**, **~**, **{**, and **}** characters, file names that contained a **GUID**, file names with leading dots, and file names longer than 128 characters. These restrictions are removed in SharePoint Server 2016 and are now available to use. 
  
> [!IMPORTANT]
> Restricted characters such as **%** and **#** are still not allowed in file names. Page file names, such as wiki pages, may not contain the following characters: " # % * : < > ? \ / | nor can they begin with a leading dot (period) character.
  
### Hybrid in SharePoint Server 2016
<a name="hybrid"> </a>

In SharePoint Server 2016, new hybrid features are available to enable hybrid solutions.
  
 **Hybrid sites**
  
 **Hybrid sites features** allows your users to have an integrated experience while using SharePoint Server and SharePoint Online sites: 
  
- Users can follow SharePoint Server and SharePoint Online sites, and see them consolidated in a single list.
    
- Users have a single profile in Office 365, where all of their profile information is stored.
    
For more information, see [SharePoint hybrid sites and search](../hybrid/sharepoint-hybrid-sites-and-search.md).
  
 **Hybrid OneDrive for Business**
  
Hybrid sites features are used in concert with **Hybrid OneDrive for Business** (introduced in SharePoint Server 2013 with Service Pack 1 (SP1)): 
  
- Users can sync files with Office 365 and share them with others.
    
- Users can access their files directly through Office 365 from any device.
    
 **Cloud hybrid search**
  
Cloud hybrid search is a new hybrid search solution alternative. With cloud hybrid search:
  
- You index all of your crawled content, including on-premises content, to your search index in Office 365. You can set up the crawler in SharePoint Server 2016 to crawl the same content sources and use the same search connectors in Office SharePoint Server 2007, SharePoint Server 2010, and SharePoint Server 2013.
    
- When users query your search index in Office 365, they get unified search results from both on-premises and Office 365 content.
    
For more information about cloud hybrid search, see the public Microsoft cloud hybrid search program on [Microsoft Office connection](http://go.microsoft.com/fwlink/p/?LinkID=624235&amp;clcid=0x409).
  
For more information, see [Plan for hybrid OneDrive for Business](/sharepoint/hybrid/plan-hybrid-onedrive-for-business).
  
For more information about the hybrid solutions available today, please visit the [SharePoint Hybrid Solutions Center](https://go.microsoft.com/fwlink/p/?LinkID=613711).
  
### Identify and search for sensitive content in both SharePoint Server 2016 and OneDrive documents
<a name="sensitive"> </a>

With this new capability, you can:
  
- **Search for sensitive content** across SharePoint Server 2016, SharePoint Online, and OneDrive for Business. 
    
- **Leverage 51 built-in sensitive information types** (credit cards, passport numbers, Social Security numbers, and more). 
    
- Use **DLP Queries** from the eDiscovery site collection to discover sensitive content relating to common industry regulations from the SharePoint eDiscovery Center, identify offending documents, and export a report. 
    
- Turn on **DLP Policies** from the Compliance Policy Center site collection to notify end users and administrators when documents with sensitive information are stored in SharePoint and automatically protect the documents from improper sharing. 
    
Information on configuring and using this feature is documented in SharePoint Online and Office 365. For more information, see:
  
- [Search for sensitive content in SharePoint and OneDrive documents](http://go.microsoft.com/fwlink/p/?LinkID=620221&amp;clcid=0x4809)
    
- [Use DLP in SharePoint Online to identify sensitive data stored on sites](http://go.microsoft.com/fwlink/p/?LinkID=620288&amp;clcid=0x4809)
    
### Image and video previews
<a name="preview"> </a>

In SharePoint Server 2016 when you post images and videos to a document library, you can see a preview by hovering the mouse over the image or video, or by clicking on them.
  
### Information Rights Management
<a name="InfoRights"> </a>

For more information, see [Secure and sync with Information Rights Management on OneDrive for Business](http://go.microsoft.com/fwlink/p/?LinkID=620223&amp;clcid=0x4809) and [Apply Information Rights Management to a list or library](https://support.office.com/en-us/article/Apply-Information-Rights-Management-to-a-list-or-library-3bdb5c4e-94fc-4741-b02f-4e7cc3c54aa1).
  
### Large file support
<a name="largefile"> </a>

Previous versions of SharePoint did not support uploading or downloading files larger than 2,047 MB. SharePoint Server 2016 now allows you to upload or download larger files. You can configure the desired maximum file-size limit on a per-web application basis in your SharePoint farm.
  
### MinRole farm topology
<a name="minrole"> </a>

The role of a server is specified when you create a new farm or join a server to an existing farm. SharePoint automatically configures the services on each server based on the server role, optimizing the performance of the farm based on that topology. There are eight predefined server roles that are available, as shown in the following table.
  
|**Server role**|**Description**|
|:-----|:-----|
|**Front-end** <br/> |Service applications, services, and components that serve user requests belong on front-end web servers. These servers are optimized for low latency.  <br/> |
|**Application** <br/> |Service applications, services, and components that serve back-end requests, such as background jobs or search crawl requests, belong on Application servers. These servers are optimized for high throughput.  <br/> |
|**Distributed Cache** <br/> |Service applications, services, and components that are required for a distributed cache belong on Distributed Cache servers.  <br/> |
|**Search** <br/> |Service applications, services, and components that are required for search belong on Search servers.  <br/> |
|**Custom** <br/> |Custom service applications, services, and components that do not integrate with MinRole belong on Custom servers. The farm administrator has full control over which service instances can run on servers assigned to the Custom role. MinRole does not control which service instances are provisioned on this role.  <br/> |
|**Single-Server Farm** <br/> |Service applications, services, and components required for a single-machine farm belong on a Single-Server Farm. A Single-Server Farm is meant for development, testing, and very limited production use. A SharePoint farm with the Single-Server Farm role cannot have more than one SharePoint server in the farm.  <br/> **Important:** <br/> The Standalone Install mode is no longer available in SharePoint Server 2016. The Single-Server Farm role replaces the Standalone Install mode available in previous SharePoint Server releases. Unlike Standalone Install, the SharePoint administrator must separately install and prepare Microsoft SQL Server for SharePoint. The SharePoint administrator must also configure the SharePoint farm services and web applications, either manually or by running the Farm Configuration Wizard.  <br/> |
|**Front-end with Distributed Cache** <br/> |Shared role that combines the Front-end and Distributed Cache roles on the same server.  <br/> **Note:** <br/> This shared role was introduced in the November Public Update for SharePoint Server 2016 (Feature Pack 1).  <br/> |
|**Application with Search** <br/> |Shared role that combines the Application and Search roles on the same server.  <br/> **Note:** <br/> This shared role was introduced in the November Public Update for SharePoint Server 2016 (Feature Pack 1).  <br/> |
   
For more information about the MinRole feature, see [Overview of MinRole Server Roles in SharePoint Server 2016](../install/overview-of-minrole-server-roles-in-sharepoint-server.md) and [Planning for a MinRole server deployment in SharePoint Server 2016](../install/planning-for-a-minrole-server-deployment-in-sharepoint-server.md).
  
### Mobile experience
<a name="mobile"> </a>

When you use a mobile device to access the home page for a SharePoint Server 2016 team site, you can tap tiles or links on the screen to navigate the site. You can also switch from the mobile view to PC view, which displays site pages as they are seen on a client computer. This view is also touch enabled.
  
### New controls for working with OneDrive for Business
<a name="newcontrols"> </a>

You can click a control to create new Office documents, upload files, synchronize your files for offline use, and share your files. For more information, see "Simple controls" on [The OneDrive Blog](http://go.microsoft.com/fwlink/?LinkID=620285&amp;clcid=0x4809).
  
### Open Document Format (ODF) available for document libraries
<a name="ODF"> </a>

The Open Document Format (ODF) enables you to create new files in a document library and save as ODF files so that users can edit the new file with a program they choose. For more information, see [Set Open Document Format (ODF) as the default file template for a library](http://go.microsoft.com/fwlink/?LinkID=620286&amp;clcid=0x4809).
  
### Project Server 2016
<a name="project"> </a>

Project Server 2016 for SharePoint Server 2016 has many new capabilities and features, including:
  
- **Resource Engagements:** Now project managers can request needed resources from resource managers to complete their projects. Also, resource managers can use the new heat map functionality to see where resources are spending their time. 
    
- **Multiple Timelines:** Project and Portfolio managers can now create richer timelines that display multiple timelines in a single view. 
    
- **Simpler administration:** Project Server now has multi-tenant storage capabilities and has combined data storage with SharePoint. This greatly reduces IT overhead by eliminating the dedicated Project Server database and improves backup and restore capabilities. 
    
- **Cloud grade performance and scale:** Many performance and scalability improvements that have been added to Project Online have also been added to Project Server 2016. 
    
For more information, see [What's new for IT pros in Project Server 2016 Preview](/project/what-s-new-for-it-pros-in-project-server-2016).
  
> [!IMPORTANT]
> Project Server 2016 is installed with SharePoint Server 2016 Enterprise, though is licensed separately. For more information about Project Server licensing, see [Licensing Project](http://go.microsoft.com/fwlink/p/?LinkID=761107&amp;clcid=0x409). 
  
### Power Pivot add-in and Power View are now available to use with SharePoint Server 2016
<a name="BI"> </a>

SQL Server 2016 CTP 3.1 is now available. You can now download SQL Server 2016 CTP 3.1 to use the Power Pivot for SharePoint add-in. You can also use Power View by installing SQL Server Reporting Services (SSRS) in SharePoint-integrated mode and the SSRS front-end add-in from the SQL Server installation media.
  
Download SQL Server 2016 CTP 3.1 from [Microsoft Download Center](https://go.microsoft.com/fwlink/p/?LinkID=716860).
  
The following SharePoint Server 2016 business intelligence features are available when you upgrade to SQL Server 2016 CTP 3.1:
  
- Power Pivot Gallery
    
- Scheduled Data Refresh
    
- Workbooks as a Data Source
    
- Power Pivot Management Dashboard
    
- Power View reports
    
- Power View Subscriptions
    
- Report Alerting
    
For more information, download the new [Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016](http://go.microsoft.com/fwlink/p/?LinkID=717977&amp;clcid=0x409) white paper. For details about configuring and deploying business intelligence in a multiple server SharePoint Server 2016 farm, download [Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm](http://go.microsoft.com/fwlink/p/?LinkID=723106&amp;clcid=0x409).
  
### Request Manager service improvements
<a name="BI"> </a>

SharePoint Request Manager now provisions on the server roles shown in the following list, to support both throttling and routing scenarios:
  
- Application
    
- Distributed Cache
    
- Front-End
    
Additionally, the Request Manager service will no longer prevent sites from rendering when the service is enabled while you have no routing rules defined.
  
### Sharing
<a name="share"> </a>

The following list shows the sharing improvements that are available for SharePoint Server 2016:
  
- Create and Share folder
    
- Sharing Hint
    
- See who the folder is shared with when viewing a folder
    
- Members can share
    
- Improved invitation mail
    
- One-click email to approve or deny a request for access
    
- Recently Shared Items cache, see [Enable the Recently Shared Items (RSI) cache to quickly populate the Shared with Me view](../sites/set-up-onedrive-for-business.md#EnableRSIcache).
    
### SharePoint Search Service application
<a name="search"> </a>

SharePoint Search supports indexing of up to 500 million items per Search Server application. For more information, see [Overview of search architecture in SharePoint Server](../search/search-architecture-overview.md). For information about SharePoint cloud hybrid search, see [Learn about cloud hybrid search for SharePoint](https://support.office.com/en-us/article/Learn-about-cloud-hybrid-search-for-SharePoint-af830951-8ddf-48b2-8340-179c1cc4d291?ui=en-US&amp;rs=en-US&amp;ad=US).
  
### Simplified SSL configuration for Central Administration site
<a name="search"> </a>

We've simplified the process for configuring Central Administration to use SSL bindings. The following command parameters are now available to use:
  
-  `New-SPCentralAdministration -Port <number> -SecureSocketsLayer`
    
-  `Set-SPCentralAdministration -Port <number> -SecureSocketsLayer`
    
-  `Psconfig.exe -cmd adminvs -port <number> -ssl`
    
You must assign a server certificate to the Central Administration IIS web site by using the IIS administration tools. The Central Administration web application won't be accessible until you do this.
  
If you specify port 443, it will automatically create an SSL binding instead of an HTTP binding even if you don't include the **SecureSocketsLayer** or **SSL** parameters. 
  
The Central Administration public AAM URL will be automatically updated to use the appropriate protocol scheme, server name, and port number.
  
### Site collection upgrades
<a name="search"> </a>

There are three options available for upgrading site collections. For more information, see [Upgrade a site collection to SharePoint Server 2016](../upgrade-and-update/upgrade-a-site-collection.md).
  
### SMTP connection encryption
<a name="smtpcon"> </a>

The following list shows the SharePoint 2016 requirements that are needed to negotiate connection encryption with an SMTP server:
  
1. STARTTLS must be enabled on the SMTP server.
    
2. The SMTP server must support the TLS 1.0, TLS 1.1, or TLS 1.2 protocol.
    
    > [!IMPORTANT]
    > SSL 2.0 and SSL 3.0 protocols are not supported. 
  
3. The SMTP server must have a server certificate installed.
    
4. The server certificate must be valid. Typically, this means that the name of the server certificate must match the name of the SMTP server provided to SharePoint. The server certificate must also be issued by a certificate authority that is trusted by the SharePoint server.
    
5. SharePoint must be configured to use SMTP connection encryption.
    
To configure SharePoint to always use SMTP connection encryption, open the SharePoint Central Administration website and browse to **System Settings** > **Configure outgoing e-mail settings** and set the **Use TLS connection encryption** drop-down menu to **Yes**. To configure SharePoint to always use SMTP connection encryption in Microsoft PowerShell, use the  `Set-SPWebApplication` cmdlet without the **DisableSMTPEncryption** parameter. For example: 
  
```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress sharepoint@contoso.com
```

To configure SharePoint to never use SMTP connection encryption in SharePoint Central Administration, browse to **System Settings** > **Configure outgoing email settings** and set the **Use TLS connection encryption** drop-down menu to **No**. To configure SharePoint to never use SMTP connection encryption in PowerShell, use the  `Set-SPWebApplication` cmdlet with the **DisableSMTPEncryption** parameter. For example: 
  
```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -DisableSMTPEncryption -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress 
sharepoint@contoso.com
```

> [!NOTE]
> If SharePoint is configured to use SMTP connection encryption, it will only send email messages if it successfully negotiates connection encryption with the SMTP server. It will not fall back and send email messages unencrypted if connection encryption negotiation fails. If SharePoint is not configured to use SMTP connection encryption, it will always send email messages unencrypted, even if the SMTP server supports connection encryption. > Using SMTP connection encryption does not enable SMTP authentication. SMTP requests are always sent anonymously. 
  
### Site folders view
<a name="folders"> </a>

For more information, see "Site folders" in [The OneDrive Blog](http://go.microsoft.com/fwlink/?LinkID=620285&amp;clcid=0x4809).
  
### Sites page pinning
<a name="pin"> </a>

You can now pin sites that you see on the sites page. A pinned site shows at the top of the list of sites that you're following.
  
### Suite Navigation is themable
<a name="pin"> </a>

You can now apply themes to your Suite Navigation.
  
### Use SMTP ports other than the default (25)
<a name="smtpport"> </a>

To configure SharePoint to use a non-default SMTP port open SharePoint Central Administration, browse to **System Settings** > **Configure outgoing email settings**, and set the **SMTP server port** to the port number of your SMTP server. To configure SharePoint to use a non-default SMTP port in PowerShell, use the  `Set-SPWebApplication` cmdlet with the **SMTPServerPort** <port number> parameter. For example: 
  
```
$WebApp = Get-SPWebApplication -IncludeCentralAdministration | ? { $_.IsAdministrationWebApplication -eq $true }
Set-SPWebApplication -Identity $WebApp -SMTPServer smtp.internal.contoso.com -SMTPServerPort 587 -OutgoingEmailAddress sharepoint@contoso.com -ReplyToEmailAddress 
sh  arepoint@contoso.com
```

## Related Topics

[What is SharePoint?](https://support.office.com/en-us/article/What-is-SharePoint-97b915e6-651b-43b2-827d-fb25777f446f?ui=en-US&amp;rs=en-US&amp;ad=US)
  

