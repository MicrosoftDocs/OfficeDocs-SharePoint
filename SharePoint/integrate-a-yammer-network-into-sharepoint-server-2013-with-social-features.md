---
title: Integrate a Yammer network into SharePoint Server 2013 with social features
ms.prod: SHAREPOINT
ms.assetid: e8baee59-a84d-4f56-bdeb-45de7d522b68
---


# Integrate a Yammer network into SharePoint Server 2013 with social features
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to integrate a Yammer network together with the SharePoint Server 2013 environment where you already use SharePoint social features.This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with the SharePoint Server 2013 environment where you already use SharePoint social features.
## Scenario prerequisites

For this scenario, we assume that:
- You have UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1) or later installed.
    
  
- Users already use the SharePoint Server 2013 Newsfeed social feature.
    
  
- You’re ready to switch to your Yammer network.
    
  

## Scenario challenges

Many organizations already use social features in their SharePoint Server 2013 installation and have active and engaged communities that use these features. If you’re ready to move towards Yammer, you have to manage both the technical implementation and the migration of users from one system to another.A common problem in SharePoint Server 2013 installations is that social features don’t work across multiple farms. When you move to a single Yammer network, you eliminate this problem.Many customers have active SharePoint Communities based on the Community Site Collection template. After you deploy UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1), the Community Site Collection template is still available to use. A Community Site resembles a Yammer Group. We recommend that you have the users in these sites start conversations in new Yammer Groups. By using a Yammer Group, a community can share information, ask questions, and seek answers to problems.
> [!IMPORTANT:]

  
    
    

Some communities might not want to immediately move to Yammer Groups. It’s okay to let them continue to use the Community Site.For new or old team sites, there’s no option to automatically enable Yammer. Each site owner has to add Yammer using the Yammer app for SharePoint, Yammer Embed, or another custom integration. For information about how to add the Yammer app for SharePoint to a SharePoint site, see  [Get and install the Yammer app onto SharePoint Server 2013 sites](html/get-and-install-the-yammer-app-onto-sharepoint-server-2013-sites.md).
## Step 1: Configure single sign-on (SSO)

To configure SSO, follow the directions in **Set up single sign-on in a Yammer network**.
### 

![Idea icon](images/) <br/>  Look for and fix email mismatches between Yammer and the SAML assertion before they happen. <br/>  Verify that your identity provider supports high availability. <br/>  Involve a range of users in testing. <br/>  Test that you can sign in to Yammer by using the federated identity solution from both inside and outside the network. <br/>  Prepare appropriate communications for users. <br/> 
## Step 2: Configure Yammer Directory Sync

To configure Yammer Directory Sync:
- Follow the directions in **Plan for Yammer Directory Sync**. For more information, see [Yammer Integrations](https://go.microsoft.com/fwlink/p/?LinkId=402150).
    
  
- When you first implement Yammer Directory Sync, do so in suspend mode. For information about Yammer Directory Sync setting parameters, see  [Change Yammer Directory Sync settings](https://go.microsoft.com/fwlink/p/?LinkId=516977).
    
  
- Enable the  *EnableAdds*  and *EnableUpdates*  parameters later. For more information, see [Change Yammer Directory Sync settings](https://go.microsoft.com/fwlink/p/?LinkId=516977).
    
  

### 

![Idea icon](images/) <br/>  Make sure that you understand attribute mappings and preferences and how they will affect your Yammer network. <br/>  Customize the activation and welcome email messages. <br/>  Understand and review the validation report. <br/>  Include only users who have email addresses that match your domains. <br/>  Prepare for disaster recovery with a standby instance. <br/>  Document the configuration and discuss it with business and communications stakeholders. <br/> 
## Step 3: Disable default SharePoint Server 2013 social features

After you enable SSO and configure Yammer Directory Sync, you should  [disable the default SharePoint Server 2013 social features](html/hide-sharepoint-server-2013-social-features.md).
## Step 4: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should  [use the Yammer embed widget](html/add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages.
# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Social scenarios with Yammer and SharePoint Server 2013](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md)
  
    
    

#### 

 [Yammer single sign-on integration](https://go.microsoft.com/fwlink/p/?LinkId=402150)
  
    
    

  
    
    

