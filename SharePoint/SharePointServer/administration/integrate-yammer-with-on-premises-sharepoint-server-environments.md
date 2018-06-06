---
title: "Integrate Yammer with on-premises SharePoint Server environments"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/5/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 555e6de4-eece-440c-857b-9601c65df4fe
description: "Summary: Learn how to add Yammer functionality to a SharePoint Server environment and how to replace SharePoint Newsfeeds with Yammer."
---

# Integrate Yammer with on-premises SharePoint Server environments

 **Summary:** Learn how to add Yammer functionality to a SharePoint environment and how to replace SharePoint Newsfeeds with Yammer. 
  
Yammer comes in two varieties: Yammer Basic and Yammer Enterprise. 
- Yammer Basic is free and available to all users. It lets employees collaborate with other members of their organization.
-  Yammer Enterprise is a premium version that extends an organization's basic Yammer network and is integrated with Office 365. It's available as part of many SharePoint Online and Office 365 plans, and is the recommended version for integration. (See [Office 365 plans](https://go.microsoft.com/fwlink/p/?LinkId=394054).) 
  
Although SharePoint Server provides basic enterprise social features, Yammer provides a richer enterprise social experience. You can add Yammer functionality to SharePoint sites by adding it to the navigation bar, and embedding a Yammer feed into SharePoint pages. 
  
## Yammer networks, groups, and users

Before you integrate Yammer into your SharePoint Server  environment, you should learn about Yammer networks, groups, and users, and how they combine to create a foundation for providing you with a rich Yammer experience within SharePoint.
  
For more information, see [Yammer networks, groups, and users overview](yammer-networks-groups-and-users-overview.md).
  
## Use Yammer Enterprise with SharePoint Server 

You can choose whether to use the social features in SharePoint or Yammer. If you want to take advantage of the power of Yammer with SharePoint, you can use any of the following methods:
  
### Directory synchronization and single sign-on

By using directory synchronization, your organization can use existing on-premises user accounts. Your organization can also significantly reduce operational costs and give its employees safer and easier access to Yammer. 
  
Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to enforce Office 365 identity. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](https://go.microsoft.com/fwlink/?linkid=875044) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
### User interface integration

To take advantage of the features that are provided by Yammer, you should integrate the Yammer experience into SharePoint, and replace the default SharePoint Server enterprise social features. This is where users can take advantage of Yammer to drive increased collaboration and innovation across their organization.
  
To take advantage of the power of Yammer with SharePoint, you can use any of the following methods:
  
#### Add Yammer to the navigation for SharePoint 

In SharePoint 2016, you can add a Yammer tile to the 

In SharePoint 2013 Service Pack 1 (SP1) for SharePoint Server 2013, you can replace the Newsfeed link with a Yammer link on the top navigation bar.
  
![SharePoint navigation bar with Yammer](../media/Yammerinonpremnavbar.gif)
  
For more information, see [Add Yammer to the navigation bar for SharePoint Server](add-yammer-to-the-navigation-bar-for-sharepoint-Server.md).
  
#### Use Yammer instead of SharePoint Newsfeed features

To take advantage of the features that are provided by Yammer, it's a good idea to replace the default SharePoint Server 2013 enterprise social features with equivalent Yammer features. You can remove the SharePoint Server 2013 social web parts from My Sites and team sites, and you can hide the user interface controls that provide social functionality.
  
![Yammer home feed on a My Site page](../media/Yammerhomefeed.gif)
  
For more information, see [Hide SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
#### Use Yammer Embed to add feeds to SharePoint pages

You can use Yammer Embed to embed Yammer feeds into on-premises sites. Yammer Embed is a JavaScript widget that you can add to SharePoint Server 2013 pages to display different kinds of Yammer feeds.
  
For more information, see [Add the Yammer Embed widget to a SharePoint page](add-the-yammer-embed-widget-to-a-sharepoint-page.md).
  
## Social scenarios

We describe a set of scenarios common to most customers. For each scenario, we outline the steps that are required to integrate Yammer with your on-premises SharePoint Server 2013 environment. The steps for each scenario vary based on the state of your existing environment and your current Yammer deployment.
  
For more information, see [Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md).
  
## See also

#### Other Resources

[Yammer Customer Success Center](https://go.microsoft.com/fwlink/p/?LinkID=331300)
  
[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)

