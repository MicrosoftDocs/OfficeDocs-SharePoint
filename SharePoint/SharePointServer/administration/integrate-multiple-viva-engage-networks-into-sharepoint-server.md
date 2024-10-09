---
title: "Integrate multiple Viva Engage networks into SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 9/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: 5a1b6cd9-358c-41af-8309-495640518eac
description: "Learn how to integrate multiple active Viva Engage networks together with your SharePoint Server environment."
---

# Integrate multiple Viva Engage networks into SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

This scenario describes the prerequisites and recommended steps to integrate multiple active Viva Engage networks together with your SharePoint Server environment.

> [!NOTE]
> Multiple active Viva Engage networks on one account are no longer supported after October 26, 2018. For more info, see [FAQ: Consolidating multiple Viva Engage networks](/viva/engage/configure-your-viva-engage-network/faq-consolidate-multiple-viva-engage-networks).
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You have one or more established Viva Engage networks (either Basic or Enterprise), with active users.
    
## Scenario challenges

When you integrate an email domain that has an existing Viva Engage network into a larger parent network, it's called a network merge. A network merge is a valid option when an organization has multiple business units or subsidiaries that want to take advantage of the collaboration and administrative features of Viva Engage but that don't share a common email domain.
  
For example, say Contoso.com is an international company with subsidiaries in locations around the world. Each subsidiary has different product lines to serve the unique needs of customers in the area. Employee email addresses reflect the name of their subsidiary, like @contoso-europe.com and @contoso-asia.com. In a network merge, all subsidiary domains merge into the parent Viva Engage network, @contoso.com, and users who have subsidiary email addresses would be routed to the parent Viva Engage network when they sign in.
  
> [!CAUTION]
> When you do a network merge, the data in all subsidiary networks is permanently deleted. 
  
For more information about administering Viva Engage, see [Viva Engage - Admin help](/viva/engage/eac-overview?formCode=MG0AV3).
  
## Step 1: Merge multiple Viva Engage networks

Merging Viva Engage networks merges the users, but not the data. Before doing the merge, tell users whose networks will be merged with the parent network the date, time, and effects of the merge. Additionally, share the reasons for the merge, highlight the benefits, and provide instructions for archiving private message data, notes, files, and so on. Let users know that all data in the child networks will be permanently deleted.
  
When you are ready to merge networks:
  
- Follow the directions in [Combine multiple Viva Engage networks](/viva/engage/configure-your-viva-engage-network/consolidate-multiple-viva-engage-networks).
    
- Inform users in the parent network that new users are joining, and encourage current users to welcome the new ones.
    
> [!NOTE]
>  Consider exporting data before the merge, particularly if your organization adheres to specific data retention policies. You must be a Verified Administrator in Viva Engage (Enterprise feature only) to perform a data export. Viva Engage does not support any tool or support process to migrate data from one network to the other. 
  
## Step 2: Set up directory synchronization

Microsoft 365 uses Microsoft Entra ID for identity management, and Viva Engage can be set up to [Enforce Microsoft 365 identity for Viva Engage users](/viva/engage/configure-your-viva-engage-network/enforce-office-365-identity). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Microsoft Entra ID by using Microsoft Entra Connect. 
  
For more information, see [Plan for directory synchronization for Microsoft 365](/microsoft-365/enterprise/plan-for-directory-synchronization) and [Integrate your on-premises directories with Microsoft Entra ID](/azure/active-directory/hybrid/whatis-hybrid-identity).
  
## Step 3: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
## Step 4: Use Viva Engage Embed

After you disable the default SharePoint Server social features, you should [use the Viva Engage embed widget](add-the-viva-engage-embed-widget-to-a-sharepoint-page.md) to include Viva Engage feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Viva Engage with on-premises SharePoint Server environments](integrate-viva-engage-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Viva Engage and SharePoint Server](social-scenarios-with-viva-engage-and-sharepoint-server.md)
#### Other Resources

[Manage Viva Engage users across their life cycle from Microsoft 365](/viva/engage/manage-viva-engage-users/manage-users-across-their-lifecycle)

[Viva Engage - Admin Help](/viva/engage/)
