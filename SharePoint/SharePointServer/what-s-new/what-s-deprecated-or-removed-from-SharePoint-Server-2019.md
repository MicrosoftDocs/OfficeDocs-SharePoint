---
title: "What's deprecated or removed from SharePoint Server 2019"
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
description: "Learn about the features and functionality that are deprecated or removed in SharePoint Server 2019."
---

# What's deprecated or removed from SharePoint Server 2019

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)]

Learn about the features and functionality that are deprecated or removed in SharePoint Server 2019.

Deprecated features are included in SharePoint Server 2019 for compatibility with previous product versions. For information about new features in SharePoint Server 2019, see [New and improved features in SharePoint Server 2019](new-and-improved-features-in-sharepoint-server-2019.md).

## Definitions

Different customers may have different interpretations of terms such as “deprecated.” To ensure that customers fully understand what we mean by the terminology in this document, we’re including this brief definition of each term.

- **Deprecated**
 
  A deprecated feature is no longer being invested in by Microsoft and we discourage customers from taking a dependency on it if they haven’t used it before. Deprecated features are still supported by Microsoft in SharePoint Server 2019 for customers who are already using this feature in previous releases and need the feature for backward compatibility. Deprecated features may be removed in future major releases of SharePoint Server with no additional notice. Customers should begin to explore their options for migrating away from these features.

- **Removed**

  A removed feature is no longer supported by Microsoft in SharePoint Server 2019. In many cases the feature is actually removed from the product, but in some cases it may still be present. A feature labeled as “removed” is unsupported even if the feature is still present in the product.

## Features deprecated in SharePoint Server 2019

The following features and functionality have been deprecated in SharePoint Server 2019.

### Access Services 2010

Access Services 2010 will remain supported, but deprecated, for the SharePoint Server 2019 release. Customers are recommended to explore Microsoft [PowerApps](https://powerapps.microsoft.com/) and [Flows](http://flow.microsoft.com/) as potential alternatives to Access Services 2010.

### Access Services 2013

Access Services 2013 will remain supported, but deprecated, for the SharePoint Server 2019 release. Customers are recommended to explore Microsoft [PowerApps](https://powerapps.microsoft.com/) and [Flows](http://flow.microsoft.com/) as potential alternatives to Access Services 2013.

### Aggregated Newsfeed

The aggregated newsfeed feature (available at newsfeed.aspx and typically accessed via the Newsfeed tile on the app launcher), will be set to read-only in SharePoint Server 2019. Both the tile in the app launcher and the option to implement the newsfeed capability will also be removed from this version forward. For customers who are currently using the aggregated newsfeed, we recommend considering options such as Team News, Communication Sites, Yammer and/or Teams. Please note that the Site Feed feature on an individual site is not impacted and will continue to be supported across all versions of the product.

### Custom Help

To ensure that users receive highly relevant help content, Microsoft is moving from away from our legacy on-premises SharePoint help engine, which is based on help collections being installed in the on-prem farm. The new SharePoint help system is now rendered in the cloud and will have updated, synchronized content with Office 365. Custom help based on the legacy SharePoint help engine will remain supported, but deprecated, for the SharePoint Server 2019 release.

### Groove Sync Client

The Groove sync client is our client for syncing documents between your personal devices and SharePoint Server 2010, 2013, and 2016 Team sites. SharePoint Server 2019 introduces support for the new OneDrive Sync Client (a.k.a. the Next Generation Sync Client), which provides a more reliable and feature-rich syncing experience. If Groove detects that your existing sync relationships are to a site that has been upgraded to SharePoint Server 2019, it will attempt to migrate those sync relationships to the OneDrive Sync Client. Administrators can control this migration experience.

The Groove sync client will remain supported, but deprecated, for the SharePoint Server 2019 release.

### InfoPath Services

As we announced in the Microsoft 365 blog, InfoPath Services is a deprecated feature and customers are advised to explore alternatives for this feature. InfoPath Services will remain supported, but deprecated, for the SharePoint Server 2019 release.

There will not be a new InfoPath client shipped with this release. Microsoft will ensure that the InfoPath 2013 client will work with SharePoint Server 2019 for the remainder of the client support lifecycle (2026). InfoPath 2013 client will not be supported beyond that timeframe.

### Lists Web Service

The following SOAP endpoints in the Lists web service depend on the Microsoft Sync Framework, which was necessary to support the Groove sync client. Because the Groove sync client is now a deprecated feature, these SOAP endpoints are also being deprecated for the SharePoint Server 2019 release.

- [Lists.GetListItemChangesWithKnowledge](https://msdn.microsoft.com/library/websvclists.lists.getlistitemchangeswithknowledge.aspx)

- [Lists.UpdateListItemsWithKnowledge](https://msdn.microsoft.com/library/websvclists.lists.updatelistitemswithknowledge.aspx)
 
### Machine Translations

The Machine Translation Service will remain supported but deprecated for the SharePoint Server 2019 release.

### Variations

The Variations will remain supported but deprecated for the SharePoint Server 2019 release.

### PerformancePoint Services

PerformancePoint Services has a significant dependency on Microsoft Silverlight, which is a technology that will no longer be supported as of October 12, 2021. PerformancePoint Services will remain supported, but deprecated, for the SharePoint Server 2019 release. Customers are recommended to explore Microsoft [PowerBI](https://powerbi.microsoft.com/) as an alternative to PerformancePoint Services as we are making many new business intelligence investments in PowerBI.

### SharePoint Designer

There will not be a new SharePoint Designer client shipped with this release. Microsoft will ensure that SharePoint Designer 2013 will work with SharePoint Server 2019 for the remainder of the client support lifecycle (2026). SharePoint Designer 2013 will not be supported beyond that timeframe.

### Site Mailbox

As we announced in the SharePoint Community Blog, site mailboxes are being [deprecated](https://techcommunity.microsoft.com/t5/SharePoint-Blog/Deprecation-of-Site-Mailboxes/ba-p/93028) in SharePoint Online. Site mailboxes will remain supported, but deprecated, in the SharePoint Server 2019 release. Customers are recommend to explore shared mailboxes as an alternative to site mailboxes.

### Site Manager

The main functionality of Site Manager is now available in modern file move. The Site Manager feature will be supported, but it is deprecated in SharePoint Server 2019. Only site collection administrators will have permission to access the Site Manager page and the UI entry points to this page will be removed.

## Removed features in SharePoint Server 2019

The following features and functionality have been removed in SharePoint Server 2019. 

### Code-Based Sandbox Solutions

As announced in the Microsoft Office Dev Center and previous articles, code-based sandbox solutions were deprecated in SharePoint Server 2013 and have now been [removed](/sharepoint/what-s-new/what-s-new) in SharePoint Online. After careful consideration, we’ve decided to also remove support for code-based sandbox solutions in SharePoint Server 2019. Customers are recommended to explore [SharePoint add-ins](/sharepoint/dev/sp-add-ins/sharepoint-add-ins) as an alternative, which are fully supported for both SharePoint on-premises and SharePoint Online.

### Digest Authentication

As announced by the Windows Server team, Microsoft is [deprecating](/windows-server/get-started/removed-features-1709) the Digest authentication feature in Internet Information Services (IIS). This authentication mechanism isn’t very popular and there are many alternative authentication mechanisms available with better interoperability.

To ensure we remain compatible with potential future releases of Windows Server, we are removing support for Digest authentication in SharePoint Server 2019. The SharePoint prerequisite installer will no longer attempt to install this Windows feature. Customers using Digest authentication are recommended to explore alternatives such as Kerberos, NTLM, or SAML.

### Incoming email automatic mode

As announced by the Windows Server team, Microsoft is [deprecating](/windows-server/get-started/removed-features-1709) the IIS 6 Management compatibility features in Internet Information Services (IIS). The automatic mode of the SharePoint incoming email feature relies on IIS 6 APIs to manage the IIS SMTP service. Because no alternative APIs exist to manage the IIS SMTP service, we are removing support for automatic mode in the incoming email feature of SharePoint Server 2019. Customers using incoming email are recommended to use advanced mode instead, which allows you to manually manage the IIS SMTP service and drop folder.

### Multi-Tenancy

As Microsoft continues to innovate in SharePoint Online, an increasing amount of SharePoint multi-tenancy capabilities are taking dependencies on cloud technologies that aren’t available in on-premises environments. The cost and complexity of providing an on-premises alternative has become prohibitive, so we will no longer support multi-tenancy in the SharePoint Server 2019 release. Existing SharePoint Server customers who depend on multi-tenancy are recommended to explore migrating to SharePoint Online. Other options include migrating to a non-multi-tenancy farm configuration or remaining with SharePoint Server 2016.

### PDF Viewer (SharePoint Server 2019 Preview)

SharePoint Server 2019 Preview included a built-in PDF viewer which allowed SharePoint to render PDF documents. This feature was removed from the RTM release of SharePoint Server 2019. Customers can instead use the native PDF rendering capabilities available in most web browsers and client devices.

### PowerPivot Gallery and Refresh

Since the feature was first introduced in SharePoint, Microsoft BI strategy has shifted away from heavy integration to a standalone BI solution, Power BI, to give customers a flexible, optional integration with SharePoint along with standalone capabilities.  Both [PowerBI.com](https://powerbi.com/) and [Power BI Report Server](https://powerbi.microsoft.com/report-server/) offer the option to host and view Excel Workbooks with PowerPivot models today and is the preferred method for customers going forward to host and use their Excel Workbooks with PowerPivot models, or simply to migrate to PBIX files using the migration option in Power BI Desktop for Excel Workbooks.

### SharePoint Workflow Manager (SharePoint Server 2019 Preview)

Microsoft announced that SharePoint Server 2019 Preview would support a new workflow management application called SharePoint Workflow Manager to run SharePoint Server 2013 workflows. However, the SharePoint Workflow Manager application was canceled before its final release. The RTM release of SharePoint Server 2019 supports [Service Bus 1.1](https://support.microsoft.com/help/4077554/add-support-for-tls-1-1-and-tls-1-2-on-service-bus-for-windows-server) and [Microsoft Workflow Manager 1.0 CU5](https://support.microsoft.com/help/4055730/description-of-the-cumulative-update-5-for-workflow-manager-1-0) to run SharePoint Server 2013 workflows. For more information, see [Install and configure workflow in SharePoint Server](/sharepoint/governance/install-and-configure-workflow-for-sharepoint-server).

### Visio Services - Silverlight Based Rendering

Visio Services has 2 options for rendering Visio diagrams: Microsoft Silverlight-based and PNG-based. Microsoft Silverlight is a technology that will no longer be supported as of October 12, 2021. This means that, Silverlight-based rendering will no longer be supported in SharePoint Server 2019. Visio Services will only render Visio diagrams using the PNG-based technology.

## SharePoint Business Intelligence Scenarios

For more information on SharePoint BI scenarios, review the SQL Server Reporting Services Team blog post, [Simplifying our SharePoint integration story](https://blogs.msdn.microsoft.com/sqlrsteamblog/2016/11/17/simplifying-our-sharepoint-integration-story/).
