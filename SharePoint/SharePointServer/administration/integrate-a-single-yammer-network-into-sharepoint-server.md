---
title: "Integrate a single Yammer network into SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/11/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 58901f1a-dbc9-46ca-8b51-e683ea5f2ce3
description: "Learn how to integrate a single, active Yammer network together with your SharePoint Server environment."
---

# Integrate a single Yammer network into SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This scenario describes the prerequisites and recommended steps to integrate a single, active Yammer network together with your SharePoint Server environment.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2019, SharePoint Server 2016, or SharePoint Server 2013 SP1 or later installed.
    
- You don't use the SharePoint Server Newsfeed social feature.
    
- You use Active Directory Domain Services (AD DS) as your identity provider and Active Directory Federation Services (AD FS) 2.0 for identity federation.
    
- You have one single, established Yammer Basic or Enterprise network that has active users.
    
    For information about how users are managed in Yammer Enterprise, see [Manage Yammer users across their life cycle from Office 365](https://go.microsoft.com/fwlink/?linkid=875043).
    
## Scenario challenges

If you are using Yammer Basic, one of the top issues in this scenario is the inconsistency of users and their logon credentials between the user profile stores in Yammer and SharePoint Server. The following diagram shows the possible credentials mismatch situations between your AD DS user repository and the Yammer network user repository.
  
**Yammer user credential mismatch cases**

![Yammer diagram of credentials and mismatches](../media/YammerCredentialsMismatch.png)
  
**Table: Scenario 2 challenges: SharePoint Server and an active single Yammer network**

|**Challenge**|**Description**|
|:-----|:-----|
|Same user and email address in AD DS and Yammer  <br/> |The same user exists in both AD DS and Yammer with the same user name and email address. For this user, there is no change in the user name after you set up directory synchronization and Yammer Enterprise.  <br/> |
|Different user account  <br/> |User B used a different email address when they signed up for Yammer. For this user, there is a change after you set up Yammer Enterprise. For this scenario, you should let the affected users know about the changes to their logon credentials. The reason for the different logon credentials might be because the user joined the Basic network by using an alias, not their primary email address. It can also occur because the user changed their name. You can manage and make these email address changes by using the [Bulk Update Users](https://go.microsoft.com/fwlink/?LinkID=402146) page.  <br/> |
|Different domain  <br/> |In a scenario where you have multiple Yammer networks, you have disconnected users. This scenario is no longer supported after October 26, 2018. By merging networks, everyone in your organization can use a single Yammer network. This scenario is covered in more detail in [Integrate multiple Yammer networks into SharePoint Server](integrate-multiple-yammer-networks-into-sharepoint-server.md).  <br/> |
|Non-existent users  <br/> |When a user is removed or disabled in Office 365, if you have set up Yammer to [Enforce Office 365 identity for Yammer users](https://go.microsoft.com/fwlink/?linkid=875042), the user is removed from Yammer Enterprise.  <br/> |
   
## Step 1: Set up directory synchronization

Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to [Enforce Office 365 identity for Yammer users](https://go.microsoft.com/fwlink/?linkid=875042). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](https://go.microsoft.com/fwlink/?linkid=875044) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## Step 2: Disable default SharePoint Server social features

After you set up directory synchronization, [disable the default SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
## Step 3: Use Yammer Embed

After you disable the default SharePoint Server social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)
  
[Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md)
#### Other Resources

[Manage Yammer users across their life cycle from Office 365](https://go.microsoft.com/fwlink/?linkid=875043)

[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)

