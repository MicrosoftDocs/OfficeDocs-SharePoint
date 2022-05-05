---
title: "Integrate a Yammer network into SharePoint Server with social features"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 9/7/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: e8baee59-a84d-4f56-bdeb-45de7d522b68
description: "Learn how to integrate a Yammer network together with the SharePoint Server environment where you already use SharePoint social features."
---

# Integrate a Yammer network into SharePoint Server with social features

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with the SharePoint Server environment where you already use SharePoint social features.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016 or SharePoint Server 2013 SP1 or later installed.
    
- Users already use the SharePoint Server Newsfeed social feature.
    
- You're ready to switch to your Yammer network.
    
## Scenario challenges

Many organizations already use social features in their SharePoint Server installation and have active and engaged communities that use these features. If you're ready to move towards Yammer, you have to manage both the technical implementation and the migration of users from one system to another.
  

  
> [!IMPORTANT]
> There are no tools or processes available to help you move content from a Community Site to a Yammer Group. Going forward, you can keep the data in a Community Site and put a link on the SharePoint Community Site that points to the Yammer group where future discussions will occur. 
  
Some communities might not want to immediately move to Yammer Groups. It's okay to let them continue to use the Community Site.
  
For new or old team sites, there's no option to automatically enable Yammer. Each site owner has to add Yammer using Yammer Embed or another custom integration. For information about how to use Yammer Embed to add a Yammer feed to a SharePoint page, see [Add the Yammer embed widget to a SharePoint page](add-the-yammer-embed-widget-to-a-sharepoint-page.md).
  
### SharePoint Server 2013

A common problem in SharePoint Server 2013 installations is that social features don't work across multiple farms. When you move to a single Yammer network, you eliminate this problem.
  
Many customers have active SharePoint Communities based on the Community Site Collection template. After you deploy SharePoint Server 2013 SP1, the Community Site Collection template is still available to use. A Community Site resembles a Yammer Group. We recommend that you have the users in these sites start conversations in new Yammer Groups. By using a Yammer Group, a community can share information, ask questions, and seek answers to problems.

## Step 1: Set up directory synchronization

Microsoft 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to [Enforce Microsoft 365 identity for Yammer users](/yammer/configure-your-yammer-network/enforce-office-365-identity). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Microsoft 365](/microsoft-365/enterprise/plan-for-directory-synchronization) and [Integrate your on-premises directories with Azure Active Directory](/azure/active-directory/hybrid/whatis-hybrid-identity).
  
## Step 2: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
## Step 3: Use Yammer Embed

After you disable the default SharePoint Server social features, [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)
#### Other Resources

[Integrate Yammer with other applications](/yammer/integrate-yammer-with-other-apps/integrate-with-other-applications)

[Yammer - Admin Help](/yammer/yammer-landing-page)