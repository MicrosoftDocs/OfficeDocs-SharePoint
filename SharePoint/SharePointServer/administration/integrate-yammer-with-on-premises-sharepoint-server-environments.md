---
title: "Integrate Yammer with on-premises SharePoint Server environments"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 555e6de4-eece-440c-857b-9601c65df4fe
description: "Learn how to add Yammer functionality to a SharePoint Server environment and how to replace SharePoint Newsfeeds with Yammer."
---

# Integrate Yammer with on-premises SharePoint Server environments

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
 
Although SharePoint Server provides basic enterprise social features, Yammer Enterprise provides a richer enterprise social experience to drive increased collaboration and innovation across your organization. You can add Yammer functionality to SharePoint sites by adding it to the navigation bar, replacing SharePoint Server social features with Yammer, and embedding a Yammer feed into SharePoint pages. 

Before you integrate Yammer into your SharePoint Server  environment, you should learn about:
- Yammer networks, groups, and users, and how they combine to create a foundation for providing you with a rich Yammer experience within SharePoint. For more information, see [Yammer networks, groups, and users overview](yammer-networks-groups-and-users-overview.md).
- Directory synchronization and enforcing Office 365 identity in Yammer. By using directory synchronization, your organization can use existing on-premises user accounts. Your organization can also significantly reduce operational costs and give its employees safer and easier access to Yammer. 
  
    Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to enforce Office 365 identity so that users only have to sign on once to access both SharePoint and Yammer content. If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
    For more information, see [Plan for directory synchronization for Office 365](https://go.microsoft.com/fwlink/?linkid=875044), [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669), and [Enforce Office 365 identity for Yammer users](https://go.microsoft.com/fwlink/?linkid=875249)
    
## Add Yammer to the navigation for SharePoint 

In SharePoint Server 2019 and SharePoint Server 2016, you can add a Yammer tile to the navigation. For instructions, see [Add Yammer to the navigation bar for SharePoint Server](add-yammer-to-the-navigation-bar-for-sharepoint-Server.md).

Here's what it looks like in SharePoint Server 2019:

![SharePoint Server 2019 Office 365 navigation showing the Yammer app](../media/yammer_spserver_apps2019.png)

Here's what it looks like in SharePoint Server 2016: 

![SharePoint Server 2016 navigation showing the Yammer app](../media/yammer-tile-sharepoint.png)
 
In SharePoint 2013 Service Pack 1 (SP1) for SharePoint Server 2013, you can replace the Newsfeed link with a Yammer link on the top navigation bar.

![SharePoint Server 2013 navigation bar with Yammer](../media/Yammerinonpremnavbar.gif)
  
  
## Use Yammer instead of SharePoint Newsfeed features

To take advantage of the features that are provided by Yammer, it's a good idea to replace the default SharePoint Server enterprise social features with equivalent Yammer features. You can remove the SharePoint Server social web parts from My Sites and team sites, and you can hide the user interface controls that provide social functionality.
  
![Yammer home feed on a My Site page](../media/Yammerhomefeed.gif)
  
For more information, see [Hide SharePoint Server social features](hide-sharepoint-server-social-features.md).
  
## Use Yammer Embed to add feeds to SharePoint pages

You can use Yammer Embed to embed Yammer feeds into on-premises sites. Yammer Embed is a JavaScript widget that you can add to a SharePoint page to display different kinds of Yammer feeds.
  
For more information, see [Add the Yammer Embed widget to a SharePoint page](add-the-yammer-embed-widget-to-a-sharepoint-page.md).
  
## Social scenarios

Take a look at the most common social scenarios, and learn the steps required to integrate Yammer with your on-premises SharePoint Server environment. The steps for each scenario depend on the state of your existing environment and your current Yammer deployment.
  
For more information, see [Social scenarios with Yammer and SharePoint Server](social-scenarios-with-yammer-and-sharepoint-server.md).
  
## See also

#### Other Resources

[Yammer - Admin Help](https://go.microsoft.com/fwlink/?linkid=525575)

[Yammer Customer Success Center](https://go.microsoft.com/fwlink/p/?LinkID=331300)


