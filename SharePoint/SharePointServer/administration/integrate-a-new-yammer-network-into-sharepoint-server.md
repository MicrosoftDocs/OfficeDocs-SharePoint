---
title: "Integrate a new Yammer network into SharePoint Server"
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
ms.assetid: 6485e76d-9c52-40eb-ae0f-4e00c321c7d8
description: "Learn how to integrate a new Yammer Enterprise network into an existing SharePoint Server environment."
---

# Integrate a new Yammer network into SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
This scenario describes the prerequisites and recommended steps to integrate a new Yammer Enterprise network together with your existing SharePoint Server environment.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You are ready to use a Yammer Enterprise network.
    
## Step 1: Purchase Yammer Enterprise

Yammer Enterprise is included in many Microsoft 365 subscriptions, which means that you might already have licenses for the service. 
  
## Step 2: Create your Yammer network

To set up a Yammer network, see [Yammer admin help](/yammer/yammer-landing-page).
  
When you set up your network, [enforce Microsoft 365 identity for Yammer users](/yammer/configure-your-yammer-network/enforce-office-365-identity).
  
For information about how users are managed in Yammer Enterprise, see [Manage Yammer users across their life cycle from Microsoft 365](/yammer/manage-yammer-users/manage-users-across-their-lifecycle).
  
## Step 3: Set up directory synchronization

Microsoft 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to enforce Microsoft 365 identity. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Microsoft 365](/microsoft-365/enterprise/plan-for-directory-synchronization) and [Integrate your on-premises directories with Azure Active Directory](/azure/active-directory/hybrid/whatis-hybrid-identity).
  
## Step 4: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
    
## Step 5: Use Yammer Embed

After you disable the default SharePoint Server social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)
#### Other Resources

[Manage Yammer users across their life cycle from Microsoft 365](/yammer/manage-yammer-users/manage-users-across-their-lifecycle)

[Yammer - Admin Help](/yammer/)