---
title: "User Profile service overview"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 8198232e-8d49-46fa-b9f0-17b1d5ee6b62
description: "Learn about the User Profile service architecture and how SharePoint Server uses it to enable features such as audiences and My Sites."
---

# User Profile service overview

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]. 
  
The User Profile service stores information about users in a central location. It enables My Sites, social computing features such as social tagging and newsfeeds, and creating and distributing profiles across multiple sites and farms. It is also required by most [SharePoint hybrid scenarios](../hybrid/hybrid.md).
  
    
## The User Profile service application
<a name="benefit"> </a>

The User Profile service application in SharePoint Server provides a central location where service administrators configure and administer the following features:
  
- **User profiles** - contain detailed information about people in an organization. A user profile organizes and displays all of the properties related to each user, together with social tags, documents, and other items related to that user. 
    
- **Profile synchronization** - provides a reliable way to synchronize groups and user profile information that is stored in the SharePoint Server profile database together with information that is stored in Active Directory Directory Services. 
    
    In SharePoint Server 2013, you can synchronize directly with other directories across the enterprise.
    
    In SharePoint Server 2016, you can synchronize with other directories by using an external identity manager such as Microsoft Identity Manager 2016.
    
- **Audiences** - enables organizations to target content to users based on their job or task, as defined by their membership in a SharePoint Server group or distribution list, by the organizational reporting structure, or by the public properties in their user profiles. 
    
- **My Site Host** - a dedicated site for hosting My Sites. A My Site Host is needed in order to deploy the social features of SharePoint Server. 
    
- **My Site** - a personal site that gives users in your organization a central location to manage and store documents, links, and information about colleagues. 
    
- **Social tags and notes** - enables users to add social tags to documents, to other SharePoint Server items, and to other items, such as external web pages and blog posts. Users can also leave notes on profile pages of a My Site or any SharePoint Server page. Administrators can delete all tags for employees when they leave the company or remove a tag they do not want. 
    
These features make it possible for users in an organization to share information and to stay informed about what happens within the organization. Social tags, for example, enable users to tag and track the information in which they are most interested. Users can be alerted when people with which they work author new blog posts or when there is a change in organizational metadata.
  
Like other service applications in SharePoint Server, farm administrators can [delegate the administration of all or part of the User Profile service application](/previous-versions/office/sharepoint-server-2010/ee721057(v=office.14)) to one or more service application administrators. This enables the User Profile service application to be managed by the appropriate business group. One administrator can manage all areas of the User Profile service application or areas can be isolated and managed by different administrators. For example, one administrator can manage My Sites while a different administrator manages social tags and notes. The User Profile service application can be restricted and made available only to certain departments or sets of sites based on business need, security restrictions, and budgets. 
  
## User profile databases
<a name="architecture"> </a>

When you create a User Profile service application, SharePoint Server creates three databases for storing user profile information and associated data:
  
- **Profile database** - used to store user profile information. 
    
- **Synchronization database** - used to store configuration and staging information for synchronizing profile data from external sources such as the Active Directory Domain Services (AD DS). 
    
- **Social tagging database** - used to store social tags and notes created by users. Each social tag and note is associated with a profile ID. 
    
## Related service applications
<a name="related"> </a>

The User Profile service application relies on other service applications to implement the full range of social computing features in SharePoint Server. These related service applications include the following:
  
- **[Managed metadata service](../governance/managed-metadata-planning.md)** - makes it possible to use managed metadata and share content types across site collections and web applications. [Configure the managed metadata service](../governance/configure-the-managed-metadata-service.md) before you configure the User Profiles service application. 
    
- **Search Service application** - needed to enable the People Search feature. 
    
## See also
<a name="related"> </a>

#### Concepts

[Administer the User Profile service in SharePoint Server](../administration/user-profile-service-administration.md)

