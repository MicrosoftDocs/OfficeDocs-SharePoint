---
title: "Integrate a Yammer network into SharePoint Server and Office 365"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 2b98f39e-649f-4b00-b025-0775ac996268
description: "Learn how to integrate a Yammer network together with your SharePoint Server environment and your Office 365 tenant."
---

# Integrate a Yammer network into SharePoint Server and Office 365

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with your SharePoint Server environment and your Office 365 for professionals and small businesses tenant.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You have an existing Office 365 tenant and a Yammer network.
    
- You have enabled Yammer as the Office 365 social experience on the SharePoint Online admin center.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You have already established directory synchronization with Office 365. 
    
> [!IMPORTANT]
> Planning your Office 365 user management is fundamental to deploying Office 365 and Yammer Enterprise. To understand how user management works, it's important to understand that Office 365 uses Microsoft Azure Active Directory to provide authentication to Office 365 services, includingYammer Enterprise. This means Office 365 uses the identity that is synchronized with Azure AD to provide authentication. 
  
## Step 1: Configure directory synchronization

You probably have already set up directory synchronization for Office 365 and your on-premises directory. If not, sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](https://go.microsoft.com/fwlink/?linkid=875044) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).

## Step 2: Use Yammer Embed

[Use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)

[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)

