---
title: Integrate a new Yammer network into SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: 6485e76d-9c52-40eb-ae0f-4e00c321c7d8
---


# Integrate a new Yammer network into SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to integrate a new Yammer network into an existing SharePoint Server 2013 environment.This scenario describes the prerequisites and recommended steps to integrate a new Yammer network together with your existing SharePoint Server 2013 environment.
## Scenario prerequisites

For this scenario, we assume that:
- You have UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1) or later installed.
    
  
- You don’t use the SharePoint Server 2013 Newsfeed social feature.
    
  
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
  
- You are ready to use a Yammer Enterprise network.
    
  

## Step 1: License and activate Yammer

Before you start, determine whether you have a Yammer license. Remember that Yammer Enterprise is included in all versions of Office 365 for professionals and small businesses, which means that you might already have a license for the service.If you have a Yammer license but have not yet activated it, you can  [activate it now](https://go.microsoft.com/fwlink/p/?LinkId=524338).
## Step 2: Create your Yammer network

We recommend that you  [create one single, central Yammer network](https://go.microsoft.com/fwlink/p/?LinkId=524341). This makes collaboration among all employees easier, and you can invite users from other domains to the primary domain as guests. A single network also provides centralized administration, which guarantees consistency across things like policy implementation and management, feature rollout, and scheduled maintenance. If all employees are in one location or are dispersed but share a common email address, use a single Yammer network.
## Step 3: Configure single sign-on (SSO)

In a scenario like this, where you don’t have an established Yammer network, we strongly recommend that you **configure single sign-on (SSO)** for Yammer first, and then configure Yammer Directory Sync. By doing this, you can give users a quality experience from the start, with a logon and user experience that looks and feels familiar. You’ll have a fresh network on which you can configure SSO and then invite users by using Yammer Directory Sync and a custom email message invitation.
> [!IMPORTANT:]

  
    
    


## Step 4: Configure Yammer Directory Sync

When you have a new network, you can **configure Yammer Directory Sync** to use custom email messages when you invite users to the network. These custom email messages can provide your organization’s established social guidelines or any other information for new Yammer users.
## Step 5: Disable default SharePoint Server 2013 social features

After you enable SSO and configure Yammer Directory Sync, you should  [disable the default SharePoint Server 2013 social features](html/hide-sharepoint-server-2013-social-features.md).If your organization wants to upgrade and migrate to SharePoint Server 2013, see the following articles:
-  [Overview of the upgrade process to SharePoint Server 2016](html/overview-of-the-upgrade-process-to-sharepoint-server-2016.md)
    
  
-  [Upgrade to SharePoint Server 2016](html/upgrade-to-sharepoint-server-2016.md)
    
  

> [!NOTE:]

  
    
    


## Step 6: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should  [use the Yammer embed widget](html/add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages.
# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Social scenarios with Yammer and SharePoint Server 2013](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md)
  
    
    

#### 

 [Yammer single sign-on integration](https://go.microsoft.com/fwlink/p/?LinkId=402150)
  
    
    

  
    
    

