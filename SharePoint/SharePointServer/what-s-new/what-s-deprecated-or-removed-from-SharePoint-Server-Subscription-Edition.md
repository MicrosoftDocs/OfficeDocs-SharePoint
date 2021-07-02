---
title: "What's deprecated or removed from SharePoint Server Subscription Edition"
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
description: "Learn about the features and functionality that are deprecated or removed in SharePoint Server Subscription Edition."
---

# What's deprecated or removed from SharePoint Server 2016

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the features and functionality that are deprecated or removed in SharePoint Server Subscription Edition.

Deprecated features are included in SharePoint Server Subscription Edition for compatibility with previous product versions. For information about new features in SharePoint Server Subscription Edition, see [New and improved features in SharePoint Server Subscription Edition](new-and-improved-features-in-sharepoint-server-subscription-edition.md).

## Definitions

Different customers may have different interpretations of terms such as "deprecated." To ensure that customers fully understand what we mean by the terminology in this document, we're including this brief definition of each term.

- **Deprecated**
 
  A deprecated feature is no longer being invested in by Microsoft and we discourage customers from taking a dependency on it if they haven't used it before. Deprecated features are still supported by Microsoft in SharePoint Server 2019 for customers who are already using this feature in previous releases and need the feature for backward compatibility. Deprecated features may be removed in future major releases of SharePoint Server with no additional notice. Customers should begin to explore their options for migrating away from these features.

- **Removed**

  A removed feature is no longer supported by Microsoft in SharePoint Server 2019. In many cases, the feature is actually removed from the product, but in some cases it may still be present. A feature labeled as "removed" is unsupported even if the feature is still present in the product.
 
## Deprecated Features

 - SharePoint 2010 workflows (Alternative: SharePoint 2013 workflows or Power Automate)

## Removed Features

 - Access Services 2010 (Alternative: Power Apps)
 
 - Access Services 2013 (Alternative: Power Apps)
 
 - Groove sync app support (Alternative: OneDrive sync app)
 
 - Lists web service APIs for Groove sync app (Alternative: OneDrive sync app)

 - PerformancePoint Services (Alternative: PowerBI)
 
 - Stsadm.exe command line tool (Alternative: PowerShell cmdlets)

 
## Features deprecated in SharePoint Server Subscription Edition

The following features and functionality have been deprecated in SharePoint Server Subscription Edition.

### Access Services 2010

Access Services 2010 will remain supported, but deprecated, for the SharePoint Server Subscription Edition release. Customers are recommended to explore Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2010.

### Access Services 2013

Access Services 2013 will remain supported, but deprecated, for the SharePoint Server 2019 release. Customers are recommended to explore Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2013.  

### PerformancePoint Services is removed

PerformancePoint Services had a significant dependency on Microsoft Silverlight, which is a technology that will no longer be supported as of October 12, 2021. PerformancePoint Services has been removed from SharePoint Server vNext. Customers are recommended to explore Microsoft [PowerBI](https://powerbi.microsoft.com/)as an alternative to PerformancePoint Services as we are making many new business intelligence investments in PowerBI.

### Stsadm.exe command line tool 

The stsadm.exe command line administration tool has been removed from SharePoint Server Subscription Edition. SharePoint PowerShell cmdlets should be used to administer SharePoint from the command line or through scripting. TAP customers should open bugs (feedback) in the MS Collaborate portal if any important functionality in stsadm.exe is not available in the SharePoint PowerShell cmdlets.

### Update-SPHelp PowerShell cmdlet 

Because the SharePoint PowerShell cmdlets have been converted from snap-ins to modules in SharePoint Server vNext, the Update-SPHelp cmdlet is no longer necessary to download the latest cmdlet help content. This cmdlet has been removed.






  
