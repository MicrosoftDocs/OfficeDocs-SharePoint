---
title: "Plan for My Sites in SharePoint Server"
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
ms.assetid: 4edf74cf-8808-4277-ba10-b1f925d7c440
description: "Learn about the process and considerations for planning a My Sites deployment in SharePoint Server."
---

# Plan for My Sites in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In SharePoint Server, a My Site is a personal site for a user in an organization. Although a My Site appears as a single site to a user, the My Sites architecture in SharePoint Server consists of a web application, a My Site host site collection, an individual site collection, and several SharePoint service applications and features. Except for the individual site collection, all other parts of this infrastructure are configured once and shared among all the users who are part of the My Sites deployment.
  
This article contains information about My Sites architecture, related services, and other considerations when planning to deploy My Sites.
  
    
## My Sites architecture
<a name="mysitesarch"> </a>

The My Sites architecture consists of a web application that hosts My Sites, a My Site host site collection, and individual site collections for users.
  
Each user's My Site uses two site collections: the farm's My Site host site collection and the user's individual site collection. Although you can use an existing web application to host these site collections, we recommend that you use a dedicated web application to improve performance and manageability.
  
When you create the My Site host site collection and users create their individual site collections, the data is maintained in one or more content databases that are associated with the web application that hosts My Sites. Like other web applications in SharePoint Server, you can add content databases to this web application if you must have multiple databases for storage. For more information, see [Planning for storage requirements](my-sites-planning.md#storage) later in this article. 
  
The My Site host site collection and the configuration that enables individual My Sites site collections to be created are required before users can create My Sites. For more information, see [Configure My Sites in SharePoint Server](configure-my-sites.md).
  
The My Site host site collection and individual site collections are described more fully in the following sections. 
  
### My Site host site collection

The My Site host site collection is a special site collection that displays the newsfeed and profile pages of all users' My Sites. The site collection's site template must be the My Site host site template, available from the **Enterprise** tab of the **Create Site Collection** page. The My Site host site template can be used only once per User Profile service application, which is discussed later in this article. 
  
My Sites require that a site collection exist at the web application root (which is displayed as **/** in the user interface). Without this, you will receive a message that states that there is no site collection at the root when you try to enable self-service site creation for the web application. Because we recommend that you use a dedicated web application to host My Sites, you should use the root path for the My Site host collection unless you have a specific requirement to create the site collection deeper in the uniform resource locator (URL) path. 
  
Although not recommended, if you create the My Site host deeper in the path, it must be under an explicit inclusion managed path. Additionally, you must create a separate site collection at the web application root, although this site collection can be empty and created without a template.
  
The URL for a My Site host site collection is shared by all users of the same User Profile service application. The URL for **Newsfeed** is http://  _hostname_/default.aspx, and the URL for **About Me** is http://  _hostname_/person.aspx, where  _hostname_ is the address of the site collection. For example, if you configure your My Site host site collection at http://contoso.com/my, users access their newsfeeds and profiles at http://contoso.com/my/default.aspx and http://contoso.com/my/person.aspx, respectively. 
  
Although these URLs are the same for all users of a User Profile service application, the information displayed for each user is different. SharePoint Server determines the information to display based on the user's logon account. The information is targeted to that specific user and is provided by the SharePoint service applications referred to in this article.
  
When a visitor views another user's My Site, the visitor can see only the user's profile page. This URL is http:// _hostname_/person.aspx?accountname= _account_, where  _hostname_ is the address of the site collection and  _account_ is the user name (and, if it is configured, the user's domain name). For example, http://contoso.com/my/person.aspx?accountname=sidney. 
  
### Individual site collections

A user's individual site collection hosts the document library of the user's individual My Site. An individual site collection is created the first time that a user accesses the My Site. This ability to create an individual site collection requires the following configuration in SharePoint Server:
  
- The web application that hosts My Sites has a wildcard inclusion managed path, such as sites or personal. This is the path under which the individual site collections will be created when users access their My Sites for the first time. 
    
- The **Setup My Sites** settings for the User Profile service application are configured to use the URL of the My Site host site collection and the wildcard inclusion managed path for individual site collections. 
    
- The web application is enabled for self-service site creation. This functionality enables the individual site collections to be created under the specified wildcard inclusion managed path. The self-service site creation feature has special security considerations for cross-site scripting. This strengthens the recommendation to host My Sites in a dedicated web application to isolate any scripts running in a My Site from affecting other sites in your environment. 
    
- Users must have **Create Personal Site** permissions to create a My Site. By default, this permission is enabled for all authenticated users. For more information, see [Plan users and user permissions](my-sites-planning.md#planusers) later in this article. 
    
The URL to a user's document library section of a My Site is in the format of http:// _hostname_/ _managed_path_/ _account_/documents, where  _hostname_ is the address of the My Site host site collection,  _managed_path_ is the managed path for the My Site host, and  _account_ is the account of the user logged on. For example, if you configure your My Site host site collection and managed path at http://contoso.com/my, users access their documents at http://contoso.com/my/  _account_/documents.
  
With the  _account_ part of the URL, when you set up My Sites, you have three options to specify how to name an individual user's site collection, as shown in the following table. 
  
**Table: Naming options for an individual user's site collection**

|**Option**|**Description**|
|:-----|:-----|
|**User name (do not resolve conflicts)** <br/> |By using this option, the My Site name is the user name of the account. This is not a user's display name. For example, if a user's friendly name is Sidney Higa and the user's account is sidney, the site collection is named sidney. Only choose the first option if you are sure that all user names in your organization are unique. Otherwise users will encounter conflicts when they provision their My Sites. If a conflict occurs, the first user who creates a My Site with a user name is successful. However, the next user who tries to use the same user name cannot create a My Site.  <br/> |
|**User name (resolve conflicts by using domain_username)** <br/> |By using this option, the first user who has a duplicate user name will have a My Site created by using the user name only, and a second user who has that same user name will have a My Site created by using both the domain name and user name. For example, the first user will have a My Site created under http://contoso.com/my/sidney/default.aspx while the second user will have a My Site created under http://contoso.com/my/CONTOSO_sidney/default.aspx. Choose this option when it is possible for a user name to exist multiple times in an organization, such as when you have multiple domains. Because a user name is guaranteed to be unique only within its own directory source, this option prevents two users who have the same user name but different domains from encountering issues when they create their My Sites.  <br/> |
|**Domain and user name (will not have conflicts)** <br/> |By using this option, all My Site names are created by using both the domain name and user name. For example, http://contoso.com/my/CONTOSO_sidney/default.aspx. Choose this option when you want My Sites to be consistently named with the domain name and user name, regardless of whether conflicts with user names exist or not.  <br/> |
   
## Related service applications
<a name="relsvcapps"> </a>

My Sites rely on several SharePoint service applications and their related databases. These related service applications are discussed in this section, although you should also refer to the linked articles to fully plan and implement them to support My Sites in your enterprise.
  
### User Profile service application
<a name="upsvcapp"> </a>

The User Profile service application has three databases: profile database, a social database, and a synchronization database. The profile database stores information about users, such as a profile picture, the organization the users belong to, and so on. The social database stores pointers to social tags and notes created by the users when they use the **Notes and Tags** feature. The synchronization database stores connection information for profile import. SharePoint Server uses the information in the profile database to personalize the data displayed on the **About Me** page of a user's My Site. Additionally, the User Profile service application enables social computing features, such as tagging, mentions, and newsfeeds for My Sites, which affect the **About Me** and **Newsfeed** sections of a user's My Site. 
  
The User Profile service application is required for My Sites. 
  
#### Plan for profile synchronization

Although configuring the User Profile service application is required for My Sites, synchronizing profiles between SharePoint Server and directory services or business applications is optional but highly recommended. Profile synchronization provides rich functionality for My Sites by enabling the User Profile service application to collect information about users in an organization from directory services and business applications. As a result, consistent and timely information is always available on a user's My Site. Information about users can also be synchronized across the deployment among all site collections that use the same User Profile service application. User information can also be used by personalization features to increase the value of collaboration and relationships in an organization.
  
#### Plan policies and privacy

SharePoint Server provides a default set of policies that you can configure to make the appropriate information available to meet the needs of an organization. You can also create and deploy custom policy features to meet specific needs. When planning for My Sites, you should define which information is needed for key business processes in an organization and which information might be unsuitable for sharing across an organization. Between these extremes is the information that should be shared only among some users. In the case of information that might be unsuitable for sharing across an organization, you must create policies to address these specific situations. 
  
Additionally, My Site features might store or use personally identifiable information. When planning to deploy My Sites, make sure that you carefully plan how to control the behavior of these features — or turn off the features — to help protect the privacy of this information. These decisions are affected by several factors, such as corporate privacy practices, and regional or national/regional privacy laws.
  
#### Plan users and user permissions
<a name="planusers"> </a>

For users to create My Sites, maintain their profiles, follow people and content, and use tags and notes, there are user permissions to configure in the User Profile service application. Determine which of the following permissions to grant to users or groups of users:
  
1. **Create Personal Site** This permission enables users to create a personal site to store their documents, newsfeed, and followed content. 
    
2. **Follow People and Edit Profile** This permission enables users to follow people from their My Site and to edit their personal profile. 
    
3. **Use Tags and Notes** This permission enables users to use the Tags and Notes feature. 
    
By default, all authenticated users are granted all these permissions, but you can configure specific permissions depending on your needs. For example, you could allow only full-time employees to create My Sites, instead of all workers in your organization. There are seven different combinations of user permissions available to grant to users. However, not all of these permission combinations provide the expected results. As a best practice, simplify administration by granting permissions to security groups instead of specific users.
  
> [!NOTE]
> Changing user permissions in the User Profile service application is not recommended. Any changes that you make will not impact the user experience in a meaningful way. For example, if you remove the **Follow People and Edit Profile** permission the user will still be able to edit profiles and other users will still be able to follow people they choose. Additionally, if you remove the **Follow People and Edit Profile** permission for a My Site user the Tags and Notes feature is disabled. We do not recommend removing any social features. 
  
### Managed metadata service application
<a name="mmsapp"> </a>

The managed metadata service application enables web applications to store and access keywords from a managed metadata term database. For My Sites, this functionality is required for users to specify keywords as their areas of expertise in the **Ask Me About** section, to use hash tags in posts in newsfeeds, and for social tagging by using the **Tags and Notes** feature of a My Site. 
  
A managed metadata service application is highly recommended for My Sites. It must be configured as the default keyword term store for the web application. 
  
### Search service application
<a name="searchapp"> </a>

Although not required for My Sites, the SharePoint Server Search service application is highly recommended to enable users to search from their My Sites for people in the organization based on names or areas of expertise. Additionally, when you add a hash tag to microblog posts, users are directed to search results for that tag when they click it. This search functionality is part of enterprise search planning and configuration.
  
### People search
<a name="searchapp"> </a>

When a user searches for people, results contain links to the public profiles of users and links to contact them by email or messaging programs. When planning for My Sites, you might want to consider supplementing the default people search scope, and supplementing the **Search Center** tab with customized search scopes and tabs for more specific groups of users. 
  
If the administrator of the User Profile service application differs from the administrator of the Search service application, the User Profile service application administrator should review the information architecture and site hierarchy to determine the key business concepts that might relate to specific groups of users for whom other users might search across sites. Then the User Profile service application administrator can work with the Search service application administrator to develop search scopes and people search tabs for those specific groups. User Profile service application administrators can also use their knowledge of the user profiles they manage to determine other useful groups of users, and to create additional specific search scopes and search tabs for those groups.
  
Site collection administrators can also create site-level search scopes for users who are members of their site collections.
  
People search planning also feeds back into user profile planning. Initial planning might reveal people or groups of users whom you want to make it easier to find. However, additional user profile properties might have to be created to allow for those users to be found easily. 
  
### Expertise search
<a name="searchapp"> </a>

When planning My Sites, you should determine whether you want to enable users to locate colleagues within the organization based on the colleagues' expertise. People search and expertise tagging help users locate people inside an organization who have identified themselves as having significant experience with a particular subject. Users in your organization can add terms to their profile that describe areas in which they have experience. These terms are used by people search when a user searches for someone in the organization who has experience in a particular area.
  
If email analysis is enabled, users can also find people by using email analysis in Outlook. Colleague suggestions are imported from Outlook if you are using Outlook email. If you are using Outlook, SharePoint Server analyzes sent email messages and then makes colleague and keyword suggestions based on this analysis. Users can then see these suggestions when they edit their profiles. 
  
Although you can enable email analysis for all users in Outlook or only for specific groups by using Group Policy, users can opt out of this feature. If email analysis is disabled for all users, individual users can still opt in.
  
## Planning for jobs and schedules
<a name="jobs"> </a>

The timer jobs in the following table are related to My Sites functionality.
  
**Table: Timer jobs related to My Sites**

|**Services**|**Jobs**|
|:-----|:-----|
|Microsoft SharePoint Foundation Web Application  <br/> |My Site Cleanup Job  <br/> |
|Microsoft SharePoint Foundation Timer  <br/> | _User Profile service application name_ - **User Profile to SharePoint Full Synchronization** <br/>  _User Profile service application name_ - **User Profile to SharePoint Quick Synchronization** <br/> |
|User Profile Service  <br/> | _User Profile service application name_ - **Feed Cache Repopulation** <br/>  _User Profile service application name_ - **Activity Feed Job** <br/>  _User Profile service application name_ - **Activity Feed Cleanup Job** <br/>  _User Profile service application name_ - **My Site Suggestions Email Job** <br/> |
   
You can enable or disable these jobs, and configure their schedules to meet the needs of your organization. These jobs are located in the SharePoint Central Administration website, under **Monitoring**, in the **Review job definitions** section. In the **View** list, select **Service** and then, from the **Service** menu, select **Change Service** to select different services and view the related timer jobs. 
  
## Planning for geographically distributed deployments
<a name="geodist"> </a>

When planning for My Sites, you must consider the location of the users in the organization and the number of farms or User Profile service applications that will host My Sites. If you have more than one farm or User Profile service application, you will likely have to configure trusted My Site host locations.
  
### User Profile service deployment considerations for My Sites

My Sites depend on the User Profile service application. In SharePoint Server, My Sites should be configured by using one User Profile service application. Server farm architectures using a single User Profile service application include the following:
  
- A single server farm with a single User Profile service application.
    
- An enterprise services farm sharing a single User Profile service application together with one or more consuming farms. The My Sites Host is located on one of the consuming farms. In SharePoint Server, the consuming farm must be physically located in the same datacenter as the enterprise services farm when you share the User Profile service application. Consuming the User Profile service application from another farm over a WAN connection is not supported. This means that both the User Profile service application and the My Site Host must be located in the same datacenter. 
    
### Trusted My Site host locations

The **Trusted My Site Host Locations** feature prevents a user from creating more than one My Site in an organization with multiple User Profile service applications. 
  
For example, in a server farm deployment that spans geographic regions, you might have separate User Profile service applications for each region or regional server farms in the environment. By default, a user can create a different My Site in each User Profile service application or server farm, which could cause unwanted results from both an administration perspective and a user perspective. When you have multiple My Sites for an individual user in an organization, server resource needs increase. Additionally, users might not understand or want multiple My Sites.
  
To prevent individual users from creating multiple My Sites, configure trusted My Site host locations. When specified, users are redirected to the single My Site host location that is intended for their accounts regardless of where they are browsing when they attempt to create or access their My Sites. This feature ensures that each user can create only one My Site in an organization.
  
Configuring trusted My Site host locations is optional.
  
## Planning for the multilingual user interface
<a name="mui"> </a>

When enabled, users can use the multilingual user interface feature for their My Sites. This feature is used to display the site's user interface in a secondary language that the user prefers instead of the default, primary language that was selected when the site was created. By default, when a new site is created, it is created in the default, primary language of the SharePoint Server installation on the server. A farm administrator must install language packs on the server before sites can be created in languages other than the default, primary language.
  
For My Sites, the multilingual user interface feature is controlled by the **Language Options** setting when you configure My Site settings. The languages that are available to users correspond to the language packs installed in the server farm. For more information about language packs, see [Install or uninstall language packs for SharePoint Server 2016](install-or-uninstall-language-packs-0.md). 
  
## Planning for storage requirements
<a name="storage"> </a>

Because My Site users can edit their profiles, generate newsfeed activities, upload and download documents, and so on, plan carefully for the storage and capacity needs of your environment. Take into consideration the content databases for My Sites and the databases for the related services of My Sites.
  
Additionally, SharePoint Server includes a default Personal Site quota template, which has a storage limit of 100 MB and no user limit. This quota template is used for each user's individual site collection in the user's My Site. Because feed activity is now stored in lists in the user's My Site, and those lists are not archived, storage needs will continue to grow. Therefore, consider increasing the personal site quota to 500 MB or more depending on the activity that you expect in the feeds.
  
Configuring quota templates is optional, but recommended. 
  
## Planning for file types
<a name="files"> </a>

Like other web applications in SharePoint Server, you can configure the file types that users can upload to or download from the web application that hosts My Sites. This is useful if you want to prevent users from uploading or downloading file types that can be large, such as media file types, or file types that can be run on the client computer, such as executable files.
  
By default, SharePoint Server blocks certain file types. However, you can configure My Sites to allow these file types, or add other file types to block depending on the needs in your organization. 
  

