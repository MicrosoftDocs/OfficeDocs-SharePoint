---
title: "Integrate a Yammer network into SharePoint Server 2013 with social features"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: e8baee59-a84d-4f56-bdeb-45de7d522b68
description: "Summary: Learn how to integrate a Yammer network together with the SharePoint Server 2013 environment where you already use SharePoint social features."
---

# Integrate a Yammer network into SharePoint Server 2013 with social features

 **Summary:** Learn how to integrate a Yammer network together with the SharePoint Server 2013 environment where you already use SharePoint social features. 
  
This scenario describes the prerequisites and recommended steps to integrate a Yammer network together with the SharePoint Server 2013 environment where you already use SharePoint social features.
  
## Scenario prerequisites

For this scenario, we assume that:
  
- You have SharePoint Server 2013 SP1 or later installed.
    
- Users already use the SharePoint Server 2013 Newsfeed social feature.
    
- You're ready to switch to your Yammer network.
    
## Scenario challenges

Many organizations already use social features in their SharePoint Server 2013 installation and have active and engaged communities that use these features. If you're ready to move towards Yammer, you have to manage both the technical implementation and the migration of users from one system to another.
  
A common problem in SharePoint Server 2013 installations is that social features don't work across multiple farms. When you move to a single Yammer network, you eliminate this problem.
  
Many customers have active SharePoint Communities based on the Community Site Collection template. After you deploy UNRESOLVED_TOKEN_VAL(SharePointServer2013_SP1), the Community Site Collection template is still available to use. A Community Site resembles a Yammer Group. We recommend that you have the users in these sites start conversations in new Yammer Groups. By using a Yammer Group, a community can share information, ask questions, and seek answers to problems.
  
> [!IMPORTANT]
> There are no tools or processes available to help you move content from a Community Site to a Yammer Group. Going forward, you can keep the data in a Community Site and put a link on the SharePoint Community Site that points to the Yammer group where future discussions will occur. 
  
Some communities might not want to immediately move to Yammer Groups. It's okay to let them continue to use the Community Site.
  
For new or old team sites, there's no option to automatically enable Yammer. Each site owner has to add Yammer using the Yammer app for SharePoint, Yammer Embed, or another custom integration. For information about how to add the Yammer app for SharePoint to a SharePoint site, see [Get and install the Yammer app onto SharePoint Server 2013 sites](get-and-install-the-yammer-app-onto-sharepoint-server-2013-sites.md).
  
## Step 1: Set up directory synchronization

Office 365 uses Azure Active Directory for identity management, and Yammer Enterprise can be set up to [Enforce Office 365 identity for Yammer users](http://technet.microsoft.com/library/008f940b-6bec-47fc-bcc6-9c6133467562%28Office.14%29.aspx). If you're using an on-premises directory, in order to manage users in one place, you need to sync your on-premises directory with Azure Active Directory by using Azure Active Directory Connect. 
  
For more information, see [Plan for directory synchronization for Office 365](http://technet.microsoft.com/library/d3577c90-dda5-45ca-afb0-370d2889b10f%28Office.14%29.aspx) and [Integrate your on-premises directories with Azure Active Directory](https://go.microsoft.com/fwlink/p/?LinkId=869669).
  
## Step 2: Disable default SharePoint Server 2013 social features

After you set up directory synchronization, [disable the default SharePoint Server 2013 social features](hide-sharepoint-server-2013-social-features.md).
  
## Step 3: Use Yammer Embed

After you disable the default SharePoint Server 2013 social features, you should [use the Yammer embed widget](add-the-yammer-embed-widget-to-a-sharepoint-page.md) to include Yammer feeds on SharePoint pages. 
  
## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint 2013 environments](integrate-yammer-with-on-premises-sharepoint-2013-environments.md)
  
[Social scenarios with Yammer and SharePoint Server 2013](social-scenarios-with-yammer-and-sharepoint-server-2013.md)
#### Other Resources

[Yammer single sign-on integration](https://go.microsoft.com/fwlink/p/?LinkId=402150)

