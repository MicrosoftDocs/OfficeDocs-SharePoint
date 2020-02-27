---
title: "Overview of My Sites in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f6663d4b-30e5-48d6-9bbc-aed8db1aae24
description: "Learn about the benefits and uses of My Sites in SharePoint Server."
---

# Overview of My Sites in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article provides an overview of My Sites end-user functionality and benefits for consideration by enterprise business decision makers or SharePoint administrators. It does not discuss the architecture of My Sites or information about planning and configuring My Sites.
  
If you are a SharePoint administrator who is responsible for configuring My Sites in your organization, use this article together with [Plan for My Sites in SharePoint Server](my-sites-planning.md) to understand and plan for My Sites. You can then use [Configure My Sites in SharePoint Server](configure-my-sites.md) to configure My Sites and [Plan user profiles in SharePoint Server](../administration/plan-user-profiles.md) to see how user profile setup can influence the information that is displayed in My Sites. 
  
## Uses and benefits of My Sites
<a name="section1"> </a>

In SharePoint Server, a My Site is a personal site for individual users in an organization. Although an organization can customize My Sites, by default users will be able to click on the app launcher at the top of every page to display tiles for: 
  
- **Newsfeed**
    
- **OneDrive**
    
- **Sites**
    
The default links on the left navigation bar that are visible to the owner of the My Site are as follows:
  
- **Newsfeed**
    
- **About me**
    
- **Blog**
    
- **Apps**
    
When a user views another user's profile, the links on the left navigation bar are similar, but also include a link to **Documents** and **People**. The **Documents** link lets other users view the My Site owner's public documents stored on the owner's OneDrive for Business, and the **People** link displays the people whom the My Site owner is following. 
  
My Sites give users rich social networking and collaboration features, which enable users to explore and share interests, projects, business relationships, content, and other data with people in the organization.
  
Because My Sites enable users to easily share information about themselves and their work, this sharing of information encourages collaboration, builds and promotes information about expertise, and targets relevant content to the people who want to see it. Once My Sites are deployed, a user can access his or her My Site by clicking his or her user name in the top-right corner of a SharePoint Server page and then clicking **About me**. A user can also click any photo or a name in a newsfeed to be directed to that user's My Site profile.
  
### Newsfeed

 **Newsfeed** is the user's social hub where he or she can see updates from the people, documents, sites, and tags that the user is following. **Newsfeed** is the default page that displays when a user accesses his or her My Site. This page displays the feed of recent activities related to a user's specified colleagues and interests. Users can customize their newsfeeds by adding or removing colleagues they are interested in, specifying interests, and configuring the kind of activities they want to follow, such as when a colleague tags a shared interest. 
  
When the system generates an activity related to a user's action, such as when the user follows a site or changes a document, the activity includes the URL of the related item and an activity is created with a link to the affected content. These activities are  *security trimmed*  , which means that users can only see activities with links to which they have permission. This differs from user-generated posts with URLs to site or content, which are not security trimmed. 
  
The **Newsfeed** page contains the information shown in the following table. 
  
|**Heading**|**Description**|
|:-----|:-----|
|**Start a conversation** <br/> |A text box in which the user can post to the newsfeed. The user can either choose to share with everyone, or with the members of a team site of which he or she is a member.  <br/> |
|**Following** <br/> |Lists all the conversations, tags, groups, and documents that the user is following.  <br/> |
|**Everyone** <br/> |Displays the recent conversations from everyone in the organization.  <br/> |
|**Mentions** <br/> |Displays all the mentions other users have made of the user, tasks assigned to the user, and so on.  <br/> |
|**Activities** <br/> |Displays all the activities by the user.  <br/> |
|**Likes** <br/> |Displays all the items that the user has liked.  <br/> |
|**I'm following** <br/> |Displays a number that indicates how many people, documents, sites, and tags the user is following. The user can click the numbers to get more details about any items that she or she is following.  <br/> |
|**Trending #tags** <br/> |Lists the top five tags.  <br/> |
   
### OneDrive

The **OneDrive** tab or tile links to the user's OneDrive for Business. OneDrive for Business is the user's personal file storage and synchronization service for business use. 
  
The user's OneDrive for Business usually includes a private folder and a folder that is shared with everyone, or with specific people. For more information, see [Overview of OneDrive for Business in SharePoint Server](../sites/onedrive-for-business-overview.md).
  
### Sites

The **Sites** tab lists the sites that the user is following and suggested sites that the user might find interesting. The user can use this to easily keep track of the sites he or she is most interested in. 
  
### About me

The **About me** is the default page that displays when a user accesses another user's My Site. This page displays the user's profile page to other people in the organization. The **About me** is also the default page that displays when a user accesses another user's My Site by clicking the user's name or profile picture. 
  
SharePoint Server provides user profile policies that specify how profile information is displayed and how it can be used. Although there are recommended default policies for features and properties exposed in user profiles and personal sites, you can configure custom policies to meet specific needs of the organization. For example, you can configure a property to be more or less visible by default, and allow a user to override default settings for properties that you want to give them control over. You configure these policies for the User Profile service in the SharePoint Central Administration website. For more information, see [Plan user profiles in SharePoint Server](../administration/plan-user-profiles.md).
  
The **About me** page includes a title that is typically "About <  _user's name_>" and it displays the user's profile data, such as the user's picture, title, group and telephone number. 
  
The **About me** page contains the information shown in the following table. 
  
|**Heading**|**Description**|
|:-----|:-----|
|**Activities** <br/> |Displays the user's recent activities on newsfeeds, who the user is following, colleagues the user has added, and so on.  <br/> |
|**edit your profile** <br/> |By clicking **edit your profile** link, a user can change or update their display photo and information, and privacy settings for their individual profile properties that you allow them to override in the profile policy. The privacy settings are assigned to one of the following two privacy groups: **Only Me** or **Everyone**. For example, a user might decide to display more information, such as a personal phone number.  <br/> |
|**In Common** <br/> |When a user views another user's profile, he or she can see the lowest level manager that they share.  <br/> |
|**Org Chart** <br/> |Displays an organization chart. The chart shows the user's position in the organization among management, peers, and direct reports. You can select other people from the chart to view their profiles.  <br/> |
   
### Blog

 **Blog** is a Web Part page that the My Site owner can use to publish a blog. By default, the **Blog** page displays a left navigation pane with links to the user's blog categories and archives that can be edited. 
  
The user can also customize the **Blog** page by editing the page, by adding apps to the page, or by changing the look of the page. 
  
### Apps

Displays the lists, libraries, and other apps for the user.
  
### Tasks

Displays tasks assigned to the user. This is only visible to the owner of the My Site page.
  
The tasks can be viewed based on importance, status (active), whether they are completed, recently added, or personal.
  
## See also
<a name="section1"> </a>

#### Concepts

[Configure My Sites in SharePoint Server](configure-my-sites.md)
  
[Plan for My Sites in SharePoint Server](my-sites-planning.md)
  
[Plan user profiles in SharePoint Server](../administration/plan-user-profiles.md)
  
[Overview of OneDrive for Business in SharePoint Server](../sites/onedrive-for-business-overview.md)

