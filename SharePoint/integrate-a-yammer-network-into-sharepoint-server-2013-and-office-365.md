---
title: Integrate a Yammer network into SharePoint Server 2013 and Office 365
ms.prod: SHAREPOINT
ms.assetid: 2b98f39e-649f-4b00-b025-0775ac996268
---


# Integrate a Yammer network into SharePoint Server 2013 and Office 365
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365, SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to integrate a Yammer network together with your SharePoint Server 2013 environment and your Office 365 tenant.This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with your SharePoint Server 2013 environment and your Office 365 for professionals and small businesses tenant.
## Scenario prerequisites

For this scenario, we assume that:
- You have UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1) or later installed.
    
  
- You have an existing Office 365 tenant and a Yammer network.
    
  
- You have enabled Yammer as the Office 365 social experience on the SharePoint Online admin center.
    
  
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
  
- You have already established single sign-on (SSO) with Office 365. 
    
    > [!NOTE:]
      

> [!IMPORTANT:]

  
    
    


## Configure single sign-on (SSO)

Set up Yammer for SSO with your SharePoint environment, as described in  [Integrate a new Yammer network into SharePoint Server 2013](html/integrate-a-new-yammer-network-into-sharepoint-server-2013.md). Because you already have Office 365 configured for SSO with your SharePoint environment, you can use the same federated identity solution for Yammer. If you don’t already have Office 365 configured for SSO with your SharePoint environment, you can configure it separately. For more information, see  [Overview of single sign-on for Office 365](https://go.microsoft.com/fwlink/p/?LinkId=507538).
> [!IMPORTANT:]

  
    
    


# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Social scenarios with Yammer and SharePoint Server 2013](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md)
  
    
    

  
    
    

