---
title: "Integrate multiple Yammer networks into SharePoint Server 2013"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 5a1b6cd9-358c-41af-8309-495640518eac
description: "Summary: Learn how to integrate multiple active Yammer networks together with your SharePoint Server 2013 environment."
---

# Integrate multiple Yammer networks into SharePoint Server 2013

 **Summary:** Learn how to integrate multiple active Yammer networks together with your SharePoint Server 2013 environment. 
  
This scenario describes the prerequisites and recommended steps to integrate multiple active Yammer networks together with your SharePoint Server 2013 environment.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server 2013 Newsfeed social feature.
    
- You have one or more established Yammer networks (either Basic or Enterprise), with active users.
    
## Scenario challenges

When you integrate an email domain that has an existing Yammer network into a larger parent network, it's called a network merge. A network merge is a valid option when an organization has multiple business units or subsidiaries that want to take advantage of the collaboration and administrative features of Yammer Enterprise but that don't share a common email domain.
  
For example, say Contoso.com is an international company with subsidiaries in locations around the world. Each subsidiary has different product lines to serve the unique needs of customers in the area. Employee email addresses reflect the name of their subsidiary, like @contoso-europe.com and @contoso-asia.com. In a network merge, all subsidiary domains merge into the parent Yammer network, @contoso.com, and users who have subsidiary email addresses would be routed to the parent Yammer network when they sign in.
  
> [!CAUTION]
> When you do a network merge, the data in all subsidiary networks is permanently deleted. 
  
For more information about administering Yammer Enterprise, see [Yammer admin center](https://go.microsoft.com/fwlink/p/?LinkId=524338).
  
## Step 1: Merge multiple Yammer networks

Merging Yammer networks merges the users, but not the data. Before doing the merge, tell users whose networks will be merged with the parent network the date, time, and effects of the merge. Additionally, share the reasons for the merge, highlight the benefits, and provide instructions for archiving private message data, notes, files, and so on. Let users know that all data in the child networks will be permanently deleted.
  
When you are ready to merge networks:
  
- Follow the directions in [Combine multiple Yammer networks](http://technet.microsoft.com/library/218e799e-0e88-4883-95aa-a2ffb744f101.aspx).
    
- Inform users in the parent network that new users are joining, and encourage current users to welcome the new ones.
    
> [!NOTE]
>  Consider exporting data before the merge, particularly if your organization adheres to specific data retention policies. You must be a Verified Administrator in Yammer (Enterprise feature only) to perform a data export. >  Yammer does not support any tool or support process to migrate data from one network to the other. 
  
## Step 2: Set up directory synchronization

Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to [Enforce Office 365 identity for Yammer users](http://technet.microsoft.com/library/008f940b-6bec-47fc-bcc6-9c6133467562%28Office.14%29.aspx). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](http://technet.microsoft.com/library/d3577c90-dda5-45ca-afb0-370d2889b10f%28Office.14%29.aspx) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## Step 3: Disable default SharePoint Server 2013 social features

After you set up directory synchronization, [disable the default SharePoint Server 2013 social features](hide-sharepoint-server-2013-social-features.md).
  
## Step 4: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint 2013 environments](integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
[Social scenarios with Yammer and SharePoint Server 2013](social-scenarios-with-yammer-and-sharepoint-server-2013.md)
#### Other Resources

[Manage Yammer users across their life cycle from Office 365](http://technet.microsoft.com/library/6c4c8fff-6444-404a-bffc-f9da0bcc3039%28Office.14%29.aspx)

