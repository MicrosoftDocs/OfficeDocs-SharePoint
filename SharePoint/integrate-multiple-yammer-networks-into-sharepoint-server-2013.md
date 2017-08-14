---
title: Integrate multiple Yammer networks into SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: 5a1b6cd9-358c-41af-8309-495640518eac
---


# Integrate multiple Yammer networks into SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, Yammer Enterprise*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn how to integrate multiple active Yammer networks together with your SharePoint Server 2013 environment.This scenario describes the prerequisites and recommended steps to integrate multiple active Yammer networks together with your SharePoint Server 2013 environment.
## Scenario prerequisites

For this scenario, we assume that:
- You have UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1) or later installed.
    
  
- You don’t use the SharePoint Server 2013 Newsfeed social feature.
    
  
- You have one or more established Yammer networks (either Basic or Enterprise), with active users.
    
  

## Scenario challenges

When you integrate an email domain that has an existing Yammer network into a larger parent network, it’s called a  *network merge*  . A network merge is a valid option when an organization has multiple business units or subsidiaries that want to take advantage of the collaboration and administrative features of Yammer Enterprise but that don’t share a common email domain.For example, say Contoso.com is an international company with subsidiaries in locations around the world. Each subsidiary has different product lines to serve the unique needs of customers in the area. Employee email addresses reflect the name of their subsidiary, like @contoso-europe.com and @contoso-asia.com. In a network merge, all subsidiary domains merge into the parent Yammer network, @contoso.com, and users who have subsidiary email addresses would be routed to the parent Yammer network when they sign in.
> [!CAUTION:]

  
    
    

For more information about how to upgrade a network to Yammer Enterprise and how to merge networks, see  [Upgrade your network to Yammer Enterprise](https://go.microsoft.com/fwlink/p/?LinkId=507537).
## Step 1: Merge multiple Yammer networks

Before doing the merge, tell users whose networks will be merged with the parent network the date, time, and effects of the merge. Additionally, share the reasons for the merge, highlight the benefits, and provide instructions for archiving private message data, notes, files, and so on. Let users know that all data in the child networks will be permanently deleted.When you are ready to merge networks:
- Follow the directions in **Combine multiple Yammer networks**.
    
  
- Inform users in the parent network that new users are joining, and encourage current users to welcome the new ones.
    
  

> [!NOTE:]
>  Consider exporting data before the merge, particularly if your organization adheres to specific data retention policies. You must be a Verified Administrator in Yammer (Enterprise feature only) to perform a data export.>  Yammer does not support any tool or support process to migrate data from one network to the other.
  
    
    


## Step 2: Configure single sign-on (SSO)

To configure SSO, follow the directions in **Set up single sign-on in a Yammer network**.
### 

![Idea icon](images/) <br/>  Look for and fix email mismatches between Yammer and the SAML assertion before they happen. <br/>  Verify that your identity provider supports high availability. <br/>  Involve a range of users in testing. <br/>  Test that you can sign in to Yammer by using the federated identity solution from both inside and outside the network. <br/>  Prepare appropriate communications for users. <br/> 
## Step 3: Configure Yammer Directory Sync

To configure Yammer Directory Sync:
- Follow the directions in **Plan for Yammer Directory Sync**.
    
  
- When you first implement Yammer Directory Sync, do so in suspend mode. For information about Yammer Directory Sync setting parameters, see  [Change Yammer Directory Sync settings](https://go.microsoft.com/fwlink/p/?LinkId=516977).
    
  
- Enable the  *EnableAdds*  and *EnableUpdates*  parameters later. For more information, see [Change Yammer Directory Sync settings](https://go.microsoft.com/fwlink/p/?LinkId=516977).
    
  

### 

![Idea icon](images/) <br/>  Make sure that you understand attribute mappings and preferences and how they will affect your Yammer network. <br/>  Customize the activation and welcome email messages. <br/>  Understand and review the validation report. <br/>  Include only users who have email addresses that match your domains. <br/>  Prepare for disaster recovery with a standby instance. <br/>  Document the configuration and discuss it with business and communications stakeholders. <br/> 
## Step 4: Disable default SharePoint Server 2013 social features

After you enable SSO and configure Yammer Directory Sync, you should  [disable the default SharePoint Server 2013 social features](html/hide-sharepoint-server-2013-social-features.md).
## Step 5: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should  [use the Yammer embed widget](html/add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages.
# See also

#### 

 [Integrate Yammer with on-premises SharePoint 2013 environments](html/integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
    
    
 [Social scenarios with Yammer and SharePoint Server 2013](html/social-scenarios-with-yammer-and-sharepoint-server-2013.md)
  
    
    

  
    
    

