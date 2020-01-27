---
title: "Plan hybrid SharePoint taxonomy and hybrid content types"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: f14dddb4-ee1a-4471-95bc-2ce41613442a
description: "SharePoint hybrid taxonomy enables you to have a single taxonomy that spans SharePoint Server and SharePoint Online. This gives you a single, consistent taxonomy no matter where your sites are located."
---

# Plan hybrid SharePoint taxonomy and hybrid content types

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

SharePoint hybrid taxonomy enables you to have a single taxonomy that spans SharePoint Server and SharePoint Online. This gives you a single, consistent taxonomy no matter where your sites are located.
  
You can choose which term groups are shared between SharePoint Server and SharePoint Online and which are on-premises only or online only.
  
The shared taxonomy is mastered in SharePoint Online and a read-only copy is kept updated in SharePoint Server. Shared terms, term sets, and groups are available in both locations.

>[!IMPORTANT] 
> Farm Administrators can modify Term Groups on-premises. These changes will not replicate to SharePoint Online. It is important that Farm Administrators be notified to not make changes on-premises.
  
You also have the option of installing hybrid content types. This feature propagates updates made to your SharePoint Online content types to your SharePoint Server site collections.
  
## Prerequisites

Hybrid SharePoint taxonomy and hybrid content types are available in SharePoint Server 2013 and SharePoint Server 2016 with the following [SharePoint updates](/officeupdates/sharepoint-updates):
  
- Hybrid taxonomy requires the November 2016 public update or later.
    
- Hybrid content types requires the June 2017 public update or later.
    
Configuration of both features uses the Hybrid Picker in the SharePoint Online admin center, which also has a number of prerequisites. Be sure to read [Hybrid picker in the SharePoint Online admin center](hybrid-picker-in-the-sharepoint-online-admin-center.md) as you plan your hybrid SharePoint taxonomy rollout. 
  
The functionality and configuration procedures are the same for both versions of SharePoint Server.
  
As with all hybrid scenarios, hybrid SharePoint taxonomy and hybrid content types both rely on your [user accounts being synchronized between SharePoint Server and SharePoint Online](/office365/enterprise/office-365-integration), though users whose accounts are not synchronized can still use the replicated and local term sets on-premises.
  
## How hybrid SharePoint taxonomy works

Hybrid SharePoint taxonomy works by replicating changes that you make to your taxonomy in SharePoint Online to your term store in SharePoint Server. Replication is done at the term group level. Groups that are replicated via hybrid SharePoint taxonomy are set to read-only in SharePoint Server and can only be updated in SharePoint Online. (A term store administrator can still update the SharePoint Server groups, but such updates will be overwritten during the next replication.)
  
You choose the groups that you want to share across SharePoint Server and SharePoint Online. System and special groups (the System, Search, SearchDirectories, and People groups) cannot be replicated, but any other groups that you create can be. (Be sure you're not reusing terms between groups that you replicate and groups that you don't replicate.)
  
The Taxonomy Groups Replication SharePoint Server timer job polls SharePoint Online for taxonomy changes on a daily basis and replicates them to the SharePoint Server taxonomy store. This timer job performs a daily update of changes and a weekly full replication. You can reschedule the timer job to meet your needs or run it manually when you want to force an update.
  
 **On-premises taxonomy**
  
If you already have a taxonomy in SharePoint Server, you can copy it to SharePoint Online by using PowerShell. This allows you to create your master taxonomy from your existing SharePoint Server and SharePoint Online taxonomies, while maintaining the IDs of the terms, term sets, and term groups in those taxonomies.
  
We recommend that you copy your taxonomy to SharePoint Online before you set up hybrid SharePoint taxonomy. You can do so at a later time, but you'll have to rerun the Hybrid Picker configuration wizard in order to turn on replication for those groups.
  
 **Local term sets**
  
You can continue to work with local term sets in both locations. They remain local and are not affected by hybrid SharePoint taxonomy. These local site-specific terms cannot be replicated.
  
## How hybrid content types work

If you already have content types in SharePoint Server, you can copy them to SharePoint Online by using PowerShell. This allows you to create your master content types list from your existing SharePoint Server and SharePoint Online content types. You control which content types are shared across SharePoint Online and SharePoint Server.
  
We recommend that you copy your content types to SharePoint Online before you set up hybrid content types.
  
## Get set up

To get started configuring hybrid SharePoint taxonomy and hybrid content types, be sure you've reviewed the [prerequisites for the Hybrid Picker](hybrid-picker-in-the-sharepoint-online-admin-center.md), and then read [Configure hybrid SharePoint taxonomy and hybrid content types](configure-hybrid-sharepoint-taxonomy-and-hybrid-content-types.md).
  
## See also

#### Other Resources

[TechNet Forums - Hybrid Taxonomy](https://social.technet.microsoft.com/Forums/office/home?forum=hybridtaxonomy)

