---
title: "Integrate a Viva Engage network into SharePoint Server and Microsoft 365"
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
ms.assetid: 2b98f39e-649f-4b00-b025-0775ac996268
description: "Learn how to integrate a Viva Engage network together with your SharePoint Server environment and your Microsoft 365 organization."
---

# Integrate a Viva Engage network into SharePoint Server and Microsoft 365

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
This scenario describes the prerequisites and recommended steps to integrate a Viva Engage network together with your SharePoint Server environment and your Microsoft 365 Apps for enterprise or Microsoft 365 Apps for business.
  
## Scenario prerequisites

For this scenario, we assume that you have:
  
- SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- An existing Microsoft 365 organization and a Viva Engage network.
    
- Enabled Viva Engage as the Microsoft 365 social experience in the classic SharePoint admin center.
    
- Active Directory Domain Services (AD DS) as your identity provider, and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- Already established directory synchronization with Microsoft 365. 
    
> [!IMPORTANT]
> Planning your user management is fundamental to deploying Microsoft 365 and Viva Engage. To understand how user management works, it's important to understand that Microsoft 365 uses Microsoft Entra ID to provide authentication to Microsoft 365 services, including Viva Engage. This means Microsoft 365 uses the identity that is synchronized with Microsoft Entra ID to provide authentication. 
  
## Step 1: Configure directory synchronization

You probably have already set up directory synchronization for Microsoft 365 and your on-premises directory. If not, sync your on-premises directory with Microsoft Entra ID by using Microsoft Entra Connect. 
  
For more info, see [Plan for directory synchronization for Microsoft 365](/microsoft-365/enterprise/plan-for-directory-synchronization) and [Integrate your on-premises directories with Microsoft Entra ID](/azure/active-directory/hybrid/whatis-hybrid-identity).

## Step 2: Use Viva Engage Embed

[Use the Viva Engage embed widget](add-the-viva-engage-embed-widget-to-a-sharepoint-page.md) to include Viva Engage feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Viva Engage with on-premises SharePoint Server environments](integrate-viva-engage-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Viva Engage and SharePoint Server](social-scenarios-with-viva-engage-and-sharepoint-server.md)

[Viva Engage - Admin Help](/viva/engage/)
