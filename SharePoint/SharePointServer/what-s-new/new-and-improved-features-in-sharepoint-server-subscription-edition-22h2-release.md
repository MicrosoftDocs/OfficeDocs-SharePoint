---
title: "New and improved features in SharePoint Server Subscription Edition Version 22H2"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.prod: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 22H2."
---

# New and improved features in SharePoint Server Subscription Edition Version 22H2

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates to existing features in SharePoint Server Subscription Edition Version 22H2.

## Summary of the features

The following table provides a summary of the new features introduced in the SharePoint Server Subscription Edition Version 22H2 feature update.

|**Feature**|**Description**|**More info**|
|:-----|:-----|:-----|
|**Feature release rings** <br/> |Standard release <br/> |For more information, see [Feature updates and feature releases](../administration/feature-updates-and-feature-releases.md)  <br/> |
|**AMSI integration** <br/> |Standard release <br/> |For more information, see [Configure AMSI integration with SharePoint Server](../security-for-sharepoint-server/configure-amsi-integration.md)  <br/> |
|**Copy and move improvement in modern document library** <br/> |Early release  <br/> |For more information, see [Copy and move improvement in modern document library](#copy-and-move-improvement-in-modern-document-library)<br/> |
|**Bulk editing in modern lists** <br/> |Early release <br/> |For more information, see [Bulk editing in modern lists](#bulk-editing-in-modern-lists)<br/> |
|**Column formatting enhancement** <br/> |Early release  <br/> |For more information, see [Column formatting enhancement](#column-formatting-enhancement) <br/> |
|**Button web part** <br/> |Early release  <br/> |For more information, see [Button web part](#button-web-part) <br/> |
|**Choose the default site language in the modern self-service site creation pane** <br/> |Early release  <br/> |For more information, see [Choose the default site language in the modern self-service site creation pane](#choose-the-default-site-language-in-the-modern-self-service-site-creation-pane) <br/> |
|**New SharePoint RESTful ListData.svc implementation** <br/> |Early release  <br/> |For more information, see [New SharePoint RESTful ListData.svc implementation](#new-sharepoint-restful-listdatasvc-implementation) <br/> |

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition Version 22H2.

### Feature release rings

As Microsoft delivers on its promise of an evergreen experience for SharePoint Server Subscription Edition, we recognize that organizations desire the ability to manage the introduction of new feature experiences into their environments. To meet this need, new feature experiences introduced in SharePoint Server Subscription Edition Version 22H2 will be grouped into feature release rings.

The two rings in this version are as follows: 

- Early release
- Standard release

In the **Early release** ring, new feature experiences will be enabled in your SharePoint farm as soon as they're ready. These experiences are supported for production use but may change before they're included in the Standard release ring. Enable **Early release** to:

- Use new feature experiences in a production environment as soon as possible.
- Perform compatibility testing and explore new feature experiences in a test environment and provide feedback to Microsoft.
- Prepare your internal help desk and user documentation for new feature experiences.

In the **Standard release** ring, new feature experiences are enabled in your SharePoint farm once they're ready for all customers to use by default. These feature experiences are supported for production use and have received additional validation during **Early release**. Enable Standard release if you prefer to minimize changes to your SharePoint experience and are willing to wait longer for new feature experiences. **Standard release** is the default feature release ring.

Customers can switch between these two feature release rings at any time. However, you must run the SharePoint Products Configuration Wizard on every server in your SharePoint farm after changing this setting. The Wizard will perform a repair operation to ensure all features recognize the new setting.

To learn more about this feature, see [Feature updates and feature releases](../administration/feature-updates-and-feature-releases.md)

### AMSI integration

The cybersecurity landscape has fundamentally changed, as evidenced by large-scale, complex attacks, and signals that  [human-operated ransomware](https://docs.microsoft.com/security/compass/human-operated-ransomware) are on the rise. More than ever, it's critical to keep your on-premises infrastructure secure and up to date, including SharePoint Servers. 

To help customers secure their environments and respond to associated threats from the attacks, we're introducing integration between SharePoint Server and the Windows [Antimalware Scan Interface](https://docs.microsoft.com/windows/win32/amsi/antimalware-scan-interface-portal) (AMSI). AMSI is a versatile standard that allows applications and services to integrate with any AMSI-capable anti-malware product present on a computer.  

When an AMSI-capable antivirus or anti-malware solution is integrated with SharePoint Server, it can examine the content of `HTTP` and `HTTPS` requests made to the server and prevent dangerous requests from being processed by SharePoint Server. Any AMSI-capable antivirus or anti-malware program that is installed on the server performs the scan as soon as the server starts to process the request. The purpose of AMSI isn't to replace current server-level antivirus/anti-malware defenses; it solely scans the `HTTP` and `HTTPS` protocols.

To learn more about this feature, see [Configure AMSI integration with SharePoint Server](../security-for-sharepoint-server/configure-amsi-integration.md)

### Copy and move improvement in modern document library

SharePoint Server Subscription Edition Version 22H2 enhances the modern document library experience by supporting copying and moving files across document libraries. In the new experience, when a user picks a file or multiple files and triggers a **copy** or **move** operation, the user will have the option to pick a destination outside the current document library. 
- **Copy** will allow users to pick a destination location in different subsites, in different site collections, and in different web applications. 
- **Move** will allow users to pick a destination location in different document libraries in the same site.

If the same term store is used in both the source and destination locations, the metadata of the file will be maintained rather than being copied or moved.

> [!NOTE]
> A document's version history will be preserved during move operations, but it won't be preserved during copy operations for the new copy of the document. 

To learn more about this feature, see [Move or copy files in SharePoint](https://support.microsoft.com/office/move-or-copy-files-in-sharepoint-00e2f483-4df3-46be-a861-1f5f0c1a87bc).

### Bulk editing in modern lists

SharePoint Server Subscription Edition Version 22H2 improves the bulk editing experience for list items in the modern lists. The users can now select multiple list items in a modern list and then click the new **Edit** button in the list toolbar. This will open an expanded editing pane where the user can update fields for all the selected list items at once.

To learn more about this feature, see [Bulk edit list item properties](https://support.microsoft.com/office/bulk-edit-list-item-properties-1521a373-b011-4a26-8fc9-016b491ee932)

### Column formatting enhancement

SharePoint Server Subscription Edition Version 22H2 allows you to customize how fields in SharePoint lists and libraries are displayed to the users. This feature gives you the capability to visualize data in various different ways to meet your needs, from applying color and other formatting to quickly understand the data at a glance, to powerful custom actions based on the state of the data. With a rich and flexible set of potential customizations, column formatting makes working with SharePoint lists and libraries much more engaging. This feature enhances the column formatting capabilities of the modern UX by adding support for Excel-style expressions and also supports Abstract Syntax Tree (AST) expressions. 

To learn more about this feature see, [Use column formatting to customize SharePoint](https://support.microsoft.com/office/column-formatting-1f927342-2bed-4745-b727-ff8b7ff96b22)

### Button web part

When you add a modern page to a site, you add and customize web parts, which are the building blocks of your page. The Button web part lets you easily add a button to your page with your own label and link. You can create an actionable button inside modern pages by adding it through the toolbox. 

To learn more about this feature, see [Use the Button web part](https://support.microsoft.com/office/use-the-button-web-part-d2e37c48-11e8-45b9-8d9e-abdaa97c2a7a)


### Choose the default site language in the modern self-service site creation pane

Previously, when creating a new site via the SharePoint start page, users couldn't select the default language of the site. The newly created site would use the default language of the web application. Starting in SharePoint Server Subscription Edition Version 22H2, a language selection control has been added to the modern site creation pane. Users can now create new sites with a specific language by selecting the desired language with that control.

### New SharePoint RESTful ListData.svc implementation

*ListData.svc* has been rebuilt so that it no longer depends on the listed WCF Data Services components while maintaining compatibility with the functionality of the prior design. When your farm is in the Early release ring, the new design is activated. You can go back to the original architecture if the *ListData.svc* web service exhibits unexpected behavior by switching the farm back to the Standard release ring.
