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

# What's deprecated or removed from SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the features and functionality that are deprecated or removed in SharePoint Server Subscription Edition.

Deprecated features are included in SharePoint Server Subscription Edition for compatibility with previous product versions. For information about new features in SharePoint Server Subscription Edition, see [New and improved features in SharePoint Server Subscription Edition](new-and-improved-features-in-sharepoint-server-subscription-edition.md).

## Definitions

Different customers may have different interpretations of terms such as "deprecated." To ensure that customers fully understand what we mean by the terminology in this document, we're including this brief definition of each term.

- **Deprecated**
 
A deprecated feature is no longer being invested in by Microsoft and we discourage customers from taking a dependency on it if they haven't used it before. Deprecated features are still supported by Microsoft in SharePoint Server Subscription Edition for customers who are already using this feature in previous releases and need the feature for backward compatibility. Deprecated features may be removed in future major releases of SharePoint Server with no additional notice. Customers should begin to explore their options for migrating away from these features.

- **Removed**

A removed feature is no longer supported by Microsoft in SharePoint Server Subscription Edition. In many cases, the feature is actually removed from the product, but in some cases it may still be present. A feature labeled as "removed" is unsupported even if the feature is still present in the product.
 
## Deprecated Features

 - SharePoint 2010 workflows 
 
 - Update-SPHelp PowerShell cmdlet

## Removed Features

 - Access Services 2010 
 
 - Access Services 2013 
 
 - Groove sync app support 
 
 - Lists web service APIs for Groove sync app 

 - PerformancePoint Services 
 
 - Stsadm.exe command line tool 
 
 - Infopath form service
 
 - Sharepoint designer support
 
## Detailed description of features deprecated or removed in SharePoint Server Subscription Edition

The following features and functionality have been deprecated or removed in SharePoint Server Subscription Edition.

### SharePoint 2010 workflows

SharePoint 2010 workflows will remain supported, but deprecated, for the SharePoint Server Subscription Edition release. Customers are recommended to explore [SharePoint 2013 workflows](/sharepoint/dev/general-development/creating-a-workflow-by-using-sharepoint-designer-and-the-sharepoint-wo#:~:text=%20Creating%20a%20workflow%20by%20using%20SharePoint%20Designer,for%20many...%204%20See%20also.%20%20More%20) or [Power Automate](https://flow.microsoft.com/) as potential alternatives to SharePoint 2010 workflows.

### Update-SPHelp PowerShell cmdlet

As SharePoint PowerShell cmdlets have been converted from snap-ins to modules in SharePoint Server Subscription Edition, the Update-SPHelp cmdlet is removed and no longer necessary to download the latest cmdlet help content.

### Access Services 2010

Access Services 2010 will remain supported, but has been removed from SharePoint Server Subscription Edition. Customers are recommended to explore Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2010.

### Access Services 2013

Access Services 2013 will remain supported, but has been removed from SharePoint Server Subscription Edition. Customers are recommended to explore Microsoft [Power Apps](https://powerapps.microsoft.com/) and [Power Automate](https://flow.microsoft.com/) as potential alternatives to Access Services 2013.  

### Groove sync app support

Groove sync app support will remain supported, but has been removed from SharePoint Server Subscription Edition. Customers are recommended to explore Microsoft [OneDrive sync app](https://support.microsoft.com/office/sync-files-with-onedrive-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49#bkmk_install) as a potential alternative to Groove sync app support.

### Lists web service APIs for Groove sync app 

Lists web service APIs for Groove sync app will remain supported, but has been removed from SharePoint Server Subscription Edition. Customers are recommended to explore Microsoft [OneDrive sync app](https://support.microsoft.com/office/sync-files-with-onedrive-in-windows-615391c4-2bd3-4aae-a42a-858262e42a49#bkmk_install) as a potential alternative to lists web service APIs.

### PerformancePoint Services

PerformancePoint Services had a significant dependency on Microsoft Silverlight, which is a technology that will no longer be supported as of October 12, 2021. PerformancePoint Services has been removed from SharePoint Server Subscription Edition. Customers are recommended to explore Microsoft [PowerBI](https://powerbi.microsoft.com/)as an alternative to PerformancePoint Services as we are making many new business intelligence investments in PowerBI.

### Stsadm.exe command line tool 

The stsadm.exe command line administration tool has been removed from SharePoint Server Subscription Edition. SharePoint PowerShell cmdlets must be used to administer SharePoint from the command line or through scripting. TAP customers can open bugs (feedback) in the Microsoft Collaborate portal if any important functionality in stsadm.exe is not available in the SharePoint PowerShell cmdlets.

> [!NOTE]
> As SharePoint PowerShell cmdlets have been converted from snap-ins to modules in SharePoint Server Subscription Edition, the Update-SPHelp cmdlet is no longer necessary to download the latest cmdlet help content. This cmdlet has been removed.

### Microsoft Information Protection and Control Client 2.1 (MSIPC)

This feature has been replaced by an internal version that will be installed through SharePoint setup and serviced through SharePoint public updates.

### Windows Server AppFabric 1.1

This featuer has been replaced by an internal version that will be installed through SharePoint setup and serviced through SharePoint public updates.
