---
ms.date: 07/02/2021
title: "What's deprecated or removed from SharePoint Server Subscription Edition?"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the features and functionalities that are deprecated or removed in SharePoint Server Subscription Edition."
---

# What's deprecated or removed from SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the features and functionalities that are deprecated or removed in SharePoint Server Subscription Edition.

## Definitions

Different customers may have different interpretations of terms such as "deprecated." To ensure that customers fully understand what we mean by the terminology in this document, we're including this brief definition of each term. For more information on Microsoft's lifecycle terms and definitions, see [Lifecycle Terms and Definitions](/lifecycle/definitions).

- **Deprecated**
 
  A feature is deprecated when Microsoft decides to no longer invest in its enhancements or further development. Customers are discouraged from having a dependency on a deprecated feature if they haven't used it before. Deprecated features are still supported by Microsoft in SharePoint Server Subscription Edition for customers who are already using this feature in previous releases and need the feature for backward compatibility. Deprecated features may be removed in future updates to SharePoint Server Subscription Edition. Unless there are exceptional circumstances, Microsoft will provide advance notice before a deprecated feature is removed by a future update. Customers should begin to explore their options for migrating away from these features.

  Deprecated features are included in SharePoint Server Subscription Edition for compatibility with previous product versions. For information about new features in SharePoint Server Subscription Edition, see [New and improved features in SharePoint Server Subscription Edition](new-and-improved-features-in-sharepoint-server-subscription-edition.md).

- **Removed**

  A removed feature is no longer supported by Microsoft in SharePoint Server Subscription Edition. In many cases, the feature is removed from the product, but in some cases it may still be present. A feature labeled as "removed" is unsupported even if the feature is still present in the product.
 
## Deprecated features

 - InfoPath Forms Services
 
 - Microsoft Workflow Manager
 
 - SharePoint 2010 workflows
 
 - SharePoint Designer 2013
 
 - Internet Explorer 11

## Removed features

 - Access Services 2010 
 
 - Access Services 2013 
 
 - Classic authentication mode for content web applications
 
 - Groove sync app support 
 
 - Lists web service APIs for Groove sync app 

 - PerformancePoint Services 
 
 - Stsadm.exe command-line tool 
 
 - Update-SPHelp PowerShell cmdlet
 
## Detailed description of features deprecated or removed in SharePoint Server Subscription Edition

The following features and functionality have been deprecated or removed in SharePoint Server Subscription Edition.

### InfoPath Forms Services

InfoPath Forms Services are deprecated but will remain supported for the SharePoint Server Subscription Edition release until July 14, 2026. After that date, InfoPath Forms Services will no longer be supported. Microsoft recommends exploring Power Apps as a potential alternative to InfoPath forms.

### Microsoft Workflow Manager
Microsoft has released SharePoint Workflow Manager as the new workflow engine to power the SharePoint 2013 Workflow platform for SharePoint Server and replace Microsoft Workflow Manager.  We recommend that all customers using SharePoint 2013 workflows upgrade to SharePoint Workflow Manager as soon as they’re able to.  Microsoft will focus all future investments and maintenance on SharePoint Workflow Manger rather than Microsoft Workflow Manager, including providing support beyond the year 2026. For more information, see [Install and configure workflow for SharePoint Server](/sharepoint/governance/install-and-configure-workflow-for-sharepoint-server).

### SharePoint 2010 workflows

SharePoint 2010 workflows are deprecated but will remain supported for the SharePoint Server Subscription Edition release until July 14, 2026. After that date, SharePoint 2010 workflows will no longer be supported. Microsoft recommends exploring [SharePoint 2013 workflows](/sharepoint/dev/general-development/creating-a-workflow-by-using-sharepoint-designer-and-the-sharepoint-wo#:~:text=%20Creating%20a%20workflow%20by%20using%20SharePoint%20Designer,for%20many...%204%20See%20also.%20%20More%20) or [Power Automate](https://flow.microsoft.com/) as potential alternatives to SharePoint 2010 workflows.

### SharePoint Designer 2013

SharePoint Designer 2013 is deprecated but will remain supported with SharePoint Server Subscription Edition until July 14, 2026. After that date, SharePoint Designer 2013 will no longer be supported. Customers will be able to continue using Visual Studio to create and edit their SharePoint 2013 workflows after that date.

### Internet Explorer 11

Internet Explorer 11 is only supported in the SharePoint Central Administration site. Internet Explorer 11 isn't supported in Team sites, OneDrive personal sites, or any other types of SharePoint content sites. Microsoft recommends exploring Microsoft Edge as the replacement for Internet Explorer 11.

### Access Services 2010

Access Services 2010 has been removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2010.

### Access Services 2013

Access Services 2013 has been removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2013.  

### Classic authentication mode for content web applications

Classic authentication mode has been removed and is no longer supported by Microsoft for content web applications in SharePoint Server Subscription Edition. Content web applications will now only support claims authentication mode. The Central Administration web application continues to use and support classic authentication mode.  

### Groove sync app support

Groove sync app support has been removed and is no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring the Microsoft [OneDrive sync app](https://support.microsoft.com/office/sync-files-with-onedrive-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49#bkmk_install) as the replacement for the Groove sync app.

### Lists web service APIs for Groove sync app 

The Lists web service APIs for Groove sync app have been removed and are no longer supported by Microsoft in SharePoint Server Subscription Edition. We recommend exploring the Microsoft [OneDrive sync app](https://support.microsoft.com/office/sync-files-with-onedrive-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49#bkmk_install) as the replacement for the Groove sync app.

### PerformancePoint Services

PerformancePoint Services had a significant dependency on Microsoft Silverlight, which is a technology that is no longer be supported as of October 12, 2021. PerformancePoint Services has been removed from SharePoint Server Subscription Edition. We recommend exploring Microsoft [Power BI](https://powerbi.microsoft.com/) as an alternative to PerformancePoint Services as we're making many new business intelligence investments in Power BI.

### Stsadm.exe command-line tool 

The stsadm.exe command-line administration tool has been removed from SharePoint Server Subscription Edition. SharePoint PowerShell cmdlets can be used to administer SharePoint from the command line or through scripting.

### Update-SPHelp PowerShell cmdlet

As SharePoint PowerShell cmdlets have been converted from snap-ins to modules in SharePoint Server Subscription Edition, the Update-SPHelp cmdlet is no longer necessary to download the latest cmdlet help content. The Update-Help cmdlet will now be able to download the latest help content for SharePoint PowerShell cmdlets.



