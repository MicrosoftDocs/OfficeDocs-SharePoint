---
title: "Integrate a new Viva Engage network into SharePoint Server"
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
ms.assetid: 6485e76d-9c52-40eb-ae0f-4e00c321c7d8
description: "Learn how to integrate a new Viva Engage network into an existing SharePoint Server environment."
---

# Integrate a new Viva Engage network into SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
This scenario describes the prerequisites and recommended steps to integrate a new Viva Engage network together with your existing SharePoint Server environment.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You are ready to use a Viva Engage network.
    
## Step 1: Purchase Viva Engage Enterprise

Viva Engage is included in many Microsoft 365 subscriptions, which means that you might already have licenses for the service. 
  
## Step 2: Create your Viva Engage network

To set up a Viva Engage network, see [Viva Engage admin help](/viva/engage/eac-overview).
  
When you set up your network, [enforce Microsoft 365 identity for Viva Engage users](/viva/engage/configure-your-viva-engage-network/enforce-office-365-identity).
  
For information about how users are managed in Viva Engage Enterprise, see [Manage Viva Engage users across their life cycle from Microsoft 365](/viva/engage/manage-viva-engage-users/manage-users-across-their-lifecycle).
  
## Step 3: Set up directory synchronization

Microsoft 365 uses Microsoft Entra ID for identity management, and Viva Engage can be set up to enforce Microsoft 365 identity. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Microsoft Entra ID by using Microsoft Entra Connect. 
  
For more information, see [Plan for directory synchronization for Microsoft 365](/microsoft-365/enterprise/plan-for-directory-synchronization) and [Integrate your on-premises directories with Microsoft Entra ID](/azure/active-directory/hybrid/whatis-hybrid-identity).
  
## Step 4: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
    
## Step 5: Use Viva Engage Embed

After you disable the default SharePoint Server social features, you should [use the Viva Engage embed widget](add-the-viva-engage-embed-widget-to-a-sharepoint-page.md) to include Viva Engage feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Viva Engage with on-premises SharePoint Server environments](integrate-viva-engage-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Viva Engage and SharePoint Server](social-scenarios-with-viva-engage-and-sharepoint-server.md)
#### Other Resources

[Manage Viva Engage users across their life cycle from Microsoft 365](/viva/engage/manage-viva-engage-users/manage-users-across-their-lifecycle)

[Viva Engage - Admin Help](/viva/engage)
