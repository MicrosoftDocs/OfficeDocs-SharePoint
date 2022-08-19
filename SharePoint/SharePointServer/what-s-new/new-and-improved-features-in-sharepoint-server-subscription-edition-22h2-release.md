---
title: "New and improved features in SharePoint Server Subscription Edition 22H2"
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
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition 22H2."
---

# New and improved features in SharePoint Server Subscription Edition 22H2

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates to existing features in SharePoint Server Subscription Edition 22H2.

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition 22H2.

### Feature release rings

As Microsoft delivers on its promise of an evergreen experience for SharePoint Server Subscription Edition, we recognize how important it is that customers have control over how new feature experiences and capabilities become available in their environments. To support this, we're introducing feature release rings in SharePoint Server Subscription Edition Version 22H2. 
The two rings in this version are as follows: 

- Early release

- Standard release

In the **Early release** ring, new feature experiences will be enabled in your SharePoint farm as soon as they're ready. These feature experiences are supported for production use, but may continue to evolve based on customer feedback and validation before they reach Standard release. Enable early release to:

- Use new feature experiences in a production environment as soon as they're available.
- Explore new feature experiences in a test environment and provide feedback to Microsoft before they reach Standard release.
- Perform compatibility testing in a test environment before they reach Standard release.
- Prepare your internal help desk and user documentation for the new feature experiences before they reach Standard release.

In the **Standard release** ring, new feature experiences are enabled in your SharePoint farm once they're ready for all customers to use by default. These feature experiences are supported for production use and have received additional validation during Early release. Enable standard release if you prioritize minimal disruption to your SharePoint experience and you're willing to wait longer for new feature experiences. Standard release is the default feature release ring.

Customers can switch between these two feature release rings at any time. However, you must run the SharePoint Products Configuration Wizard on every server in your SharePoint farm after changing this setting. The Wizard will perform a repair operation to ensure all features recognize the new setting.

### Copy and move improvement in modern document library

SharePoint Server Subscription Edition Version 22H2 enhances the modern document library experience by supporting copying and moving files across document libraries. In the new experience, when a user picks a file or multiple files and triggers a **copy** or **move** operation, the user will have the option to pick a destination outside the current document library. 
- **Copy** will allow users to pick a destination location in different subsites, in different site collections, and in different web applications. 
- **Move** will allow users to pick a destination location in different document libraries in the same site.

For more information on the copy and move enhancement, see [Move or copy files in SharePoint.](https://support.microsoft.com/en-us/office/move-or-copy-files-in-sharepoint-00e2f483-4df3-46be-a861-1f5f0c1a87bc). 

If the same term store is used in both the source and destination locations, the metadata of the file will be maintained rather than being copied or moved.

> [!NOTE]
> A document's version history will be preserved during move operations, but it won't be preserved during copy operations for the new copy of the document. 

### Bulk editing in modern lists

SharePoint Server Subscription Edition Version 22H2 improves the bulk editing experience for list items in the modern lists. The users can now select multiple list items in a modern list and then click the new **Edit** button in the list toolbar. This will open an expanded editing pane where the user can update fields for all the selected list items at once.

### Column formatting enhancement

SharePoint Server Subscription Edition Version 22H2 allows you to customize how fields in SharePoint lists and libraries are displayed to the users. This enhances the column formatting capabilities of the modern UX by adding suppport for Excel-style expressions and also supports Abstract Syntax Tree (AST) expressions. Column formatting. This feature gives you the capability to visualize data in a variety of different ways to meet your needs, from applying color and other formatting to quickly understand the data at a glance, to powerful custom actions based on the state of the data. With a rich and flexible set of potential customizations, column formatting makes working with SharePoint lists and libraries much more engaging. 

To learn more about this feature see, [Use column formatting to customize SharePoint](/sharepoint/dev/declarative-customization/column-formatting).

### Button web part

When you add a modern page to a site, you add and customize web parts, which are the building blocks of your page. The Button web part lets you easily add a button to your page with your own label and link.You can create an actionable button inside modern pages by adding it through the toolbox. 

To learn more about this feature, see 


### New language picker in modern self-site creation pane

SharePoint Server Subscription Edition Version 22H2 allows to choose the default site language in the modern self-service site creation pane.

Before, the users couldn't choose the site's default language when creating a new site through the SharePoint start page. The web application's default language would be used on the newly formed website. Starting in SharePoint Server Subscription Edition Version 22H2, a language selection control has been added to the modern site creation pane. The users can now create new sites with a specific language by selecting the desired language with that control.

### New SharePoint RESTful ListData.svc implementation

ListData.svc has been rebuilt so that it no longer depends on the listed WCF Data Services components while maintaining compatibility with the functionality of the prior design. When your farm is in the Early release ring, the new design is activated. You can go back to the original architecture if the ListData.svc web service exhibits unexpected behaviour by switching the farm back to the Standard release ring.
