---
title: "Integrate a new Yammer network into SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/11/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 6485e76d-9c52-40eb-ae0f-4e00c321c7d8
description: "Summary: Learn how to integrate a new Yammer Enterprise network into an existing SharePoint Server  environment."
---

# Integrate a new Yammer network into SharePoint Server

 **Summary:** Learn how to integrate a new Yammer Enterprise network into an existing SharePoint Server environment. 
  
This scenario describes the prerequisites and recommended steps to integrate a new Yammer Enterprise network together with your existing SharePoint Server environment.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You are ready to use a Yammer Enterprise network.
    
## Step 1: Purchase Yammer Enterprise

Yammer Enterprise is included in many Office 365 plans, which means that you might already have licenses for the service. 
  
## Step 2: Create your Yammer network

We recommend that you create one single, central Yammer network. This makes collaboration among all employees easier, and you can invite users from other domains to the primary domain as guests. A single network provides centralized administration, which guarantees consistency across things like policy implementation and management, feature rollout, and scheduled maintenance. If all employees are in one location or are dispersed but share a common email address, use a single Yammer network.
  
When you set up your network, [Enforce Office 365 identity for Yammer users](https://go.microsoft.com/fwlink/?linkid=875042).
  
For information about how users are managed in Yammer Enterprise, see [Manage Yammer users across their life cycle from Office 365](https://go.microsoft.com/fwlink/?linkid=875043).
  
## Step 3: Set up directory synchronization

Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to enforce Office 365 identity. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](https://go.microsoft.com/fwlink/?linkid=875044) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## Step 4: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
    
## Step 5: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)
#### Other Resources

[Manage Yammer users across their life cycle from Office 365](https://go.microsoft.com/fwlink/?linkid=875043)

[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)

