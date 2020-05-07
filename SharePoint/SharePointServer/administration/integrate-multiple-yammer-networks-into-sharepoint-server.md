---
title: "Integrate multiple Yammer networks into SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 5a1b6cd9-358c-41af-8309-495640518eac
description: "Learn how to integrate multiple active Yammer networks together with your SharePoint Server environment."
---

# Integrate multiple Yammer networks into SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

This scenario describes the prerequisites and recommended steps to integrate multiple active Yammer networks together with your SharePoint Server environment.

    [!NOTE] Multiple active Yammer networks on one account are no longer supported after October 26, 2018. For more info, see [FAQ: Consolidating multiple Yammer networks](/yammer/configure-your-yammer-network/faq-consolidate-multiple-yammer-networks)
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You have one or more established Yammer networks (either Basic or Enterprise), with active users.
    
## Scenario challenges

When you integrate an email domain that has an existing Yammer network into a larger parent network, it's called a network merge. A network merge is a valid option when an organization has multiple business units or subsidiaries that want to take advantage of the collaboration and administrative features of Yammer Enterprise but that don't share a common email domain.
  
For example, say Contoso.com is an international company with subsidiaries in locations around the world. Each subsidiary has different product lines to serve the unique needs of customers in the area. Employee email addresses reflect the name of their subsidiary, like @contoso-europe.com and @contoso-asia.com. In a network merge, all subsidiary domains merge into the parent Yammer network, @contoso.com, and users who have subsidiary email addresses would be routed to the parent Yammer network when they sign in.
  
> [!CAUTION]
> When you do a network merge, the data in all subsidiary networks is permanently deleted. 
  
For more information about administering Yammer Enterprise, see [Yammer - Admin help](https://go.microsoft.com/fwlink/p/?LinkId=524338).
  
## Step 1: Merge multiple Yammer networks

Merging Yammer networks merges the users, but not the data. Before doing the merge, tell users whose networks will be merged with the parent network the date, time, and effects of the merge. Additionally, share the reasons for the merge, highlight the benefits, and provide instructions for archiving private message data, notes, files, and so on. Let users know that all data in the child networks will be permanently deleted.
  
When you are ready to merge networks:
  
- Follow the directions in [Combine multiple Yammer networks](/yammer/configure-your-yammer-network/consolidate-multiple-yammer-networks).
    
- Inform users in the parent network that new users are joining, and encourage current users to welcome the new ones.
    
> [!NOTE]
>  Consider exporting data before the merge, particularly if your organization adheres to specific data retention policies. You must be a Verified Administrator in Yammer (Enterprise feature only) to perform a data export. Yammer does not support any tool or support process to migrate data from one network to the other. 
  
## Step 2: Set up directory synchronization

Microsoft 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to [Enforce Microsoft 365 identity for Yammer users](https://go.microsoft.com/fwlink/?linkid=875042). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Microsoft 365](https://go.microsoft.com/fwlink/?linkid=875044) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## Step 3: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
## Step 4: Use Yammer Embed

After you disable the default SharePoint Server social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)
#### Other Resources

[Manage Yammer users across their life cycle from Microsoft 365](https://go.microsoft.com/fwlink/?linkid=875043)

[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)


