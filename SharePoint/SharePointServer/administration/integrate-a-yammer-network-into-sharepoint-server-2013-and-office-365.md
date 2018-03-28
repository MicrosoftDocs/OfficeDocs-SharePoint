---
title: "Integrate a Yammer network into SharePoint Server 2013 and Office 365"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 2b98f39e-649f-4b00-b025-0775ac996268
description: "Summary: Learn how to integrate a Yammer network together with your SharePoint Server 2013 environment and your Office 365 tenant."
---

# Integrate a Yammer network into SharePoint Server 2013 and Office 365

 **Summary:** Learn how to integrate a Yammer network together with your SharePoint Server 2013 environment and your Office 365 tenant. 
  
This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with your SharePoint Server 2013 environment and your Office 365 for professionals and small businesses tenant.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2013 SP1 or later installed.
    
- You have an existing Office 365 tenant and a Yammer network.
    
- You have enabled Yammer as the Office 365 social experience on the SharePoint Online admin center.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You have already established directory synchronization with Office 365. 
    
> [!IMPORTANT]
> Planning your Office 365 user management is fundamental to deploying Office 365 and Yammer Enterprise. To understand how user management works, it's important to understand that Office 365 uses Microsoft Azure Active Directory to provide authentication to Office 365 services, includingYammer Enterprise. This means Office 365 uses the identity that is synchronized with Azure AD to provide authentication. 
  
## Configure directory synchronization

You probably have already set up directory synchronization for Office 365 and your on-premises directory. If not, sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](http://technet.microsoft.com/library/d3577c90-dda5-45ca-afb0-370d2889b10f%28Office.14%29.aspx) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint 2013 environments](integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
[Social scenarios with Yammer and SharePoint Server 2013](social-scenarios-with-yammer-and-sharepoint-server-2013.md)

