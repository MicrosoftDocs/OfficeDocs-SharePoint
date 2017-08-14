---
title: Integrate a single Yammer network into SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: 58901f1a-dbc9-46ca-8b51-e683ea5f2ce3
---


# Integrate a single Yammer network into SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to integrate a single, active Yammer network together with your SharePoint Server 2013 environment.This scenario describes the prerequisites and recommended steps to integrate a single, active Yammer network together with your SharePoint Server 2013 environment.
## Scenario prerequisites

For this scenario, we assume that:
- You have UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1) or later installed.
    
  
- You don’t use the SharePoint Server 2013 Newsfeed social feature.
    
  
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
  
- You have one single, established Yammer Basic or Enterprise network that has active users.
    
  

## Scenario challenges

One of the top issues in this scenario is the inconsistency of users and their logon credentials between the user profile stores in Yammer and SharePoint Server 2013. The following diagram shows the possible credentials mismatch situations between your AD DS user repository and the Yammer network user repository. **Yammer user credential mismatch cases**
  
    
    
![Yammer diagram of credentials and mismatches](images/)
  
    
    

### Table: Scenario 2 challenges: SharePoint Server 2013 and a single active Yammer network

ChallengeDescriptionSame user and email address in AD DS and Yammer  <br/> The same user exists in both AD DS and Yammer with the same user name and email address. For this user, there is no change in the user name after you set up Yammer Directory Sync and single sign-on (SSO).  <br/> Different user account  <br/> User B used a different email address when they signed up for Yammer. For this user, there is a change after you set up SSO. For this scenario, you should let the affected users know about the changes to their logon credentials. The reason for the different logon credentials might be because the user joined the Basic network by using an alias, not their primary email address. It can also occur because the user changed their name. You can manage and make these email address changes by using the  [Bulk Update Users](http://go.microsoft.com/fwlink/?LinkID=402146&amp;clcid=0x409) page. <br/> Different domain  <br/> In a scenario where you have multiple Yammer networks, you have disconnected users. In this case, we recommend that you merge Yammer networks. By merging networks, everyone in your organization can use a single Yammer network. This scenario is covered in more detail in  [Integrate multiple Yammer networks into SharePoint Server 2013](html/integrate-multiple-yammer-networks-into-sharepoint-server-2013.md).  <br/> Non-existent users  <br/> When a user is removed or disabled in AD DS, the Yammer Directory Sync process also automatically removes that user from Yammer. Also, before the Yammer Directory Sync process, unauthenticated users won’t be able to log on to Yammer because authentication is routed through AD DS, where the account is no longer active.  <br/> 
## Step 1: Configure single sign-on (SSO)

To configure SSO, follow the directions in **Set up single sign-on in a Yammer network**.
### 

![Idea icon](images/) <br/>  Look for and fix email mismatches between Yammer and the SAML assertion before they happen. <br/>  Verify that your identity provider supports high availability. <br/>  Involve a range of users in testing. <br/>  Test that you can sign in to Yammer by using the federated identity solution from both inside and outside the network. <br/>  Prepare appropriate communications for users. <br/> 
## Step 2: Configure Yammer Directory Sync

To configure Yammer Directory Sync:
- Follow the directions in **Plan for Yammer Directory Sync**.
    
  
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
  
    
    

  
    
    

