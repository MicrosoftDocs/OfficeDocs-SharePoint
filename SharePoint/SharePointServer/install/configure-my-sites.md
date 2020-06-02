---
title: "Configure My Sites in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e6600dfa-7f96-4c6f-a1be-b7ad348ac30f
description: "Learn how to set up and configure My Sites in SharePoint Server."
---

# Configure My Sites in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to set up My Sites in SharePoint Server. Like other tasks in SharePoint Server, there are multiple ways to complete a task. This article provides ordered tasks with prerequisites and procedures to help you set up My Sites in your enterprise.
  
Before you set up My Sites, ensure that you understand the concepts and terminology in [Overview of My Sites in SharePoint Server](my-sites-overview.md) and [Plan for My Sites in SharePoint Server](my-sites-planning.md).
  
We recommend that you perform all of the procedures in the order listed for best results, although not all of them are required.
  
    
## Prerequisites
<a name="prereq"> </a>

Because My Sites have dependencies on other service applications and features in SharePoint Server, ensure that you meet the prerequisites in this section before you perform the procedures in this task.
  
> [!NOTE]
> My Sites are hosted by a web application and rely on a User Profile service application. Both are described in this section. My Sites also requires a managed metadata service application. We recommend that you also have a Search service application to use with My Sites, but this is not required. Without the Search service application, some My Sites functionality is affected. For more information, see [Plan for My Sites in SharePoint Server](my-sites-planning.md). 
  
### Web application
<a name="webapp"> </a>

Although you can use an existing web application, for optimal performance and security, we recommend that you create the My Site host site collection in a dedicated web application. For more information, see [Create a web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261875(v=office.14)).
  
> [!IMPORTANT]
> If a My Site host site collection was created during initial deployment and configuration, we recommend that you do not use it because it was created in the default web application. Delete this site collection, and create a new web application that is dedicated to hosting My Sites. Then create a new My Site host site collection in the dedicated web application. 
  
### User Profile service application and profile synchronization
<a name="upsapp"> </a>

Ensure you have a User Profile service application that you want to use for My Sites. 
  
> [!IMPORTANT]
> Although the **Create New User Profile service application** dialog requests information in the **My Site Host URL** and **Personal Site Location** sections, for this task, remove any default values and leave those fields blank when you create the User Profile service application. Additionally, you can select any of the options in **Site Naming Format**. These settings will be configured separately later in this task. 
  
> [!NOTE]
> This section only applies to SharePoint Server 2013. Optionally, configure profile synchronization if you want to synchronize user and group profile information that is stored in the SharePoint Server 2013 profile database with profile information that is stored in a directory service or business system. 
  
## Create a My Site host site collection
<a name="mysitehost"> </a>

The My Site host site collection is a site collection that uses the Enterprise site template named **My Site Host**. This site collection must be created in the web application that you want to host My Sites. Generally, this site collection can be created at the root path of the web application, although it can be created as an explicit inclusion managed path deeper in the URL as long as there is a site collection created at the web application root. For more information about how to select the path for the My Site host collection, see [Plan for My Sites in SharePoint Server](my-sites-planning.md).
  
 **To create a My Site host site collection**
  
1. Verify that you have the following administrative credentials:
    
  - To create a My Site host site collection, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website or a service application administrator for the services related to My Sites. If you are a service application administrator, you must also have permission to create site collections in the web application that you dedicate to host My Sites.
    
2. In Central Administration, click **Application Management**, and then click **Create site collections**.
    
3. On the **Create Site Collection** page, in the **Web Application** section, ensure that the selected web application is the web application that you want to host My Sites. If it is not, expand the list, and then click **Change Web Application**. In the **Select Web Application** dialog, select a different web application. 
    
4. In the **Title and Description** section, type a title and description for the site collection. 
    
5. In the **Web Site Address** section, select the URL where you want this site collection created. Generally, you should use the default path (which is displayed as **/** in the user interface), which is the root of the web application. For more information about this path, see [My Sites architecture](my-sites-planning.md#mysitesarch) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
    
6. In the **Template Selection** section, on the **Enterprise** tab, click **My Site Host**.
    
7. In the **Primary Site Collection Administrator** section, and optionally in the **Secondary Site Collection Administrator** section, type an account in the format  _domain\username_ to specify an administrator for the site collection. 
    
8. Optionally, in the **Quota Template** section, select a quota template for the My Site host site collection. This quota template does not affect the individual site collections that users create for their My Sites. For more information, see [Planning for storage requirements](my-sites-planning.md#storage) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
    
9. Click **OK**. Copy this site collection URL for later reference.
    
## Add a wildcard inclusion managed path to the web application
<a name="wildcardpath"> </a>

The wildcard inclusion managed path is the path under which separate site collections are created for a user's My Site. Creation of the site collection occurs the first time that a user views the user's My Site. This functionality is available only when self-service site creation is also enabled. Enabling self-service site creation is discussed later in this article. 
  
 **To add a wildcard inclusion managed path to the web application**
  
1. Verify that you have the following administrative credentials:
    
  - To add managed paths, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website. 
    
2. In Central Administration, click **Application Management**, and then click **Manage Web applications**. 
    
3. On the **Web Applications Management** page, select the web application that you created to host My Sites. 
    
4. On the **Web Applications** tab, in the **Manage** group, click **Managed Paths**. 
    
5. In the **Define Managed Paths** dialog, in the **Add a New Path** section, in the **Path** box, type the path that you want to append to the URL namespace, and then select **Wildcard inclusion**. For example, if your web application URL is http://mysites.contoso.com/ and you want users' individual site collections created under a path named "personal", type personal in the **Path** box. Separate My Sites site collections will be created for each user under http://mysites.contoso.com/personal/. 
    
6. Click **Add Path**, and then click **OK**.
    
7. Copy this managed path for later reference.
    
## Connect the web application to service applications
<a name="connectapps"> </a>

The web application that hosts My Sites must be connected to service applications in SharePoint Server. The User Profile service application is required for My Sites. The managed metadata service application and Search service application are highly recommended. For more information, see [My Sites architecture](my-sites-planning.md#mysitesarch) in [Plan for My Sites in SharePoint Server](my-sites-planning.md). 
  
Additionally, if you have other SharePoint sites from which you want users to be able to access their My Site and **About Me** links from the upper-right corner menu, connect the web applications of those sites to the User Profile service application. 
  
 **To connect the web application to service applications**
  
1. Verify that you have the following administrative credentials:
    
  - To connect a web application to a service application, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website.
    
2. In Central Administration, in the **Application Management** section, click **Manage Web applications**. 
    
3. On the **Web Applications Management** page, select the web application that you created to host My Sites. 
    
4. On the **Web Applications** tab, in the **Manage** group, click **Service Connections**. 
    
5. In the **Configure Service Application Associations** dialog, in the **Edit the following group of connections** list, select **default** if the default group contains the service applications that you want to connect to the web application. 
    
  - If you choose **[Custom]**, select any service applications to which you want to connect the web application, including the User Profile service application, the managed metadata service application, and the Search service application.
    
6. Click **OK**.
    
## Enable self-service site creation for the web application
<a name="enableselfsvc"> </a>

Self-service site creation enables the automatic creation of a separate site collection for users when they first view their My Site. 
  
 **To enable self-service site creation for the web application**
  
1. Verify that you have the following administrative credentials:
    
  - To enable self-service site creation, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website.
    
2. In Central Administration, in the **Application Management** section, click **Manage Web applications**. 
    
3. On the **Web Applications** page, select the web application that you created to host My Sites. 
    
4. On the **Web Applications** tab, in the **Security** group, click **Self-Service Site Creation**. 
    
5. In the **Self-Service Site Creation Management** dialog, in **Site Collections**, select **On**. Optionally, in **Quota template to apply**, select a quota template.
    
6. In **Start a Site** for SharePoint Server 2013 and 2016 or **Site Creation** in SharePoint Server 2019, any option may be selected, including hiding the Self-Service Site Creation process from the user.
    
7. Click **OK** to finish. 
    
Perform these additional steps to configure permissions for users to create team sites from their My Sites to use site feeds.
  
1. In the **Policy** group, click **Permission Policy.**
    
2. On **Manage Permission Policy Levels** dialog, click **Add Permission Policy Level.**
    
3. Type a name for the permission policy.
    
4. Under **Permissions**, in **Site Permissions**, select the **Grant** option for **Create Subsites - Create subsites such as team sites, Meeting Workspace sites, and Document Workspace sites**. 
    
5. Click **Save**.
    
6. In the **Policy** group, click **User Policy**.
    
7. On **Policy for Web Application** dialog, click **Add Users**.
    
8. On **Add Users**, in **Zones** select **(All Zones)**, then click **Next**.
    
9. In **Choose Users**, enter the user names of the users that you want to create team sites from their My Site to use site feeds. If all users can create team sites from their My Site to use site feeds, click the **Browse** icon. In **Select People and Groups**, click **All Users**, then click **Everyone**. Click **Add**, and then click **OK**.
    
10. In the **Choose Permissions** section, select the name of the **Permission Policy** created previously. 
    
11. Click **Finish**, and then click **OK**.
    
## Configure My Site settings for the User Profile service application
<a name="configsettings"> </a>

After you have a My Site host site collection and wildcard inclusion managed path configured for My Sites, you can update the My Sites settings in the User Profile service application. Most of these settings are configured during initial deployment and only change infrequently during maintenance operations afterward.
  
 **To configure My Site settings for the User Profile service application**
  
1. Verify that you have the following administrative credentials:
    
  - To configure My Site settings for the User Profile service application, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website or a service application administrator for the User Profile service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the User Profile service application that you connected to the web application hosting My Sites earlier in this task. 
    
4. On the **Manage Profile Service** page, in the **My Site Settings** section, click **Setup My Sites**.
    
5. On the **My Sites Settings** page, in the **Preferred Search Center** section, specify settings for the search center to direct users to when they search for people or documents from their **About Me** profile page. If you do not have a search center set up yet, you can skip this step and complete it later. For more information, see [Search service application](my-sites-planning.md#searchapp) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
    
6. In the **My Site Host** section, type the URL of the My Site host site collection that you created earlier in this task. 
    
7. The **My Site Host URL in Active Directory** section uses Exchange Autodiscover to allow client and mobile phone applications to find a user's SharePoint Server 2016 My Site. 
    
8. In the **Personal Site Location** section, type the wildcard inclusion managed path you configured earlier in this task. By default, **personal** is prepopulated in the box. However, if you chose a different path for your wildcard inclusion managed path, replace **personal** with your path. 
    
9. In the **Site Naming Format** section, select a naming format for the My Sites site collections that will be created when users view their My Sites for the first time. For more information about these formats, see [My Sites architecture](my-sites-planning.md#mysitesarch) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
    
10. In the **Language Options** section, there is an option to specify whether users can select a preferred language for their My Site. However, the current behavior is to default to the installation language for SharePoint. [My Sites architecture](my-sites-planning.md#mysitesarch) in [Plan for My Sites in SharePoint Server](my-sites-planning.md)

  > [!NOTE]
  > This section is not present in SharePoint Server 2019.
    
11. In the **Read Permission Level** section, specify the users or groups that can view other users' My Sites when they are created. By default, this includes all authenticated users. However, you can select a more specific group or users depending on the needs of your deployment. 
    
12. In the **Security Trimming Options** section, specify how system generated posts are checked for permissions before they are displayed in feeds and on the **Tags and Notes** page. 
    
13. In the **Newsfeed** section, enable system generated posts to the feed on My Sites by selecting **Enable activities in My Site newsfeeds**. This option is selected by default. This is important in hosted environments where tenants can share the same User Profile service but have different requirements on whether they can enable newsfeeds for their users. 
    
14. In the **E-mail Notifications** section, specify an email address to use as the sender email address for My Site email notifications. This account does not have to be a real monitored email address. If you want to receive notifications for newsfeed activities, such as replies to your posts or when someone follows you, select **Enable newsfeed email notifications**.
    
    > [!IMPORTANT]
    > You must add the IP address of the farm's outbound SMTP server to the safe list in Exchange Server 2013 to prevent My Site email notifications from being sent to the Junk folder. 
  
15. In the **My Site Cleanup** section, specify a new owner of a My Site if the existing My Site user is removed from the profile database. For example, if a user leaves the company and is no longer in the profile database, the user's My Site will be deleted together with any content. However, before it is deleted, a new owner can recover any important content. Select **Enable access delegation** for the My Site cleanup job to first attempt to assign ownership of the My Site to the user's manager. If no manager is found, the My Site is assigned to the user specified in **Secondary Owner**. The new owner has two weeks to retrieve content from the My Site before it is deleted.
    
16. In the **Privacy Settings** section, select **Make My Sites Public** to make all users' My Sites public. This option is not selected by default. 
    
    > [!NOTE]
    > When a user's My Site is public, the user's list of followers, the user's list of people they are following, and all activities (including new follow notifications, social tagging and rating of content, birthdays, job title changes, workplace anniversary, updating Ask Me About, posting on a note board, and new blog posts) will be public. Any policies set within **People and Privacy** on the **Manage Policies** page is overridden. 
  
17. Click **OK**.
    
For more information about additional timer jobs for My Sites, see [Planning for jobs and schedules](my-sites-planning.md#jobs) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
  
## Enable the User Profile Service Application - Activity Feed Job
<a name="timerjobs"> </a>

The **User Profile Service Application - Activity Feed Job** creates system generated posts in the feeds for the following events: 
  
- Following a tag
    
- Tagging an item
    
- Birthday celebration
    
- Job title change
    
- Workplace anniversary
    
- Updates to Ask Me About
    
- Posting on a note board
    
After you configure My Sites, enable the **User Profile Service Application - Activity Feed Job** so that users receive system generated posts in the **Newsfeed** on their My Sites. 
  
There are other timer jobs related to My Sites that you might want to review and change default settings for. For more information about jobs related to My Sites functionality, see [Planning for jobs and schedules](my-sites-planning.md#jobs) in [Plan for My Sites in SharePoint Server](my-sites-planning.md).
  
 **To enable the User Profile Service Application - Activity Feed Job**
  
1. Verify that you have the following administrative credentials:
    
  - To configure timer jobs, you must be a member of the Farm Administrators group on the computer running the SharePoint Central Administration website.
    
2. In Central Administration, click **Monitoring**, and then click **Review job definitions**. 
    
3. On the **Job Definitions** page, in the **View** list, select **Service**. The **Service** list appears. 
    
  - If the **Service** list does not display **User Profile Service**, in **Service**, click **No selection**, then click **Change Service**. On the **Select Service** page, use the arrows in the upper-right corner to locate **User Profile Service**, and then click it. The **Job Definitions** page updates with the User Profile service jobs. 
    
4. Click the activity feed job for the User Profile service application that you created in [Prerequisites](configure-my-sites.md#prereq) earlier in this article. The job name is in the format  _User_Profile_service_name_ - **Activity Feed Job**, where  _User_Profile_service_name_ is the name that you specified for your User Profile service application. 
    
5. On the **Edit Timer Job** page, in the **Recurring Schedule** section, select the interval that you want the job to run. Available intervals are **Minutes**, **Hourly**, **Daily**, **Weekly**, and **Monthly**. Selecting a shorter interval, such as **Minutes** or **Hourly**, ensures that activities appear on users' My Site newsfeeds more frequently. However, it increases load on the system depending on how many activities are available. Selecting a longer interval, such as **Daily**, **Weekly**, or **Monthly**, reduces the number of times the job runs and processes feeds. However, it also means that users receive less frequent updates to activities in their newsfeeds.
    
6. Click **Enable**.
    
7. Optionally, click **Run Now** to run the job immediately without waiting for the next scheduled interval. 
    
## Next steps
<a name="nextsteps"> </a>

After you configure My Sites by using the procedures in this article, consider whether you require the following optional procedures:
  
- [Configure trusted My Site host locations](#trustedmysitehost)
    
- [Configure links to Office client applications](#officelinks)
    
- [Promote site links on My Sites](configure-my-sites.md#personalizationsitelink)
    
- [Start related services](configure-my-sites.md#startsvcs)
    
### Configure trusted My Site host locations
<a name="trustedmysitehost"> </a>

 **Trusted My Site Host Locations** is an optional feature that prevents a user from creating more than one My Site in an organization with multiple User Profile service applications. 
  
User Profile service application administrators can add links to trusted My Site host locations when they want to give users access to My Sites on multiple User Profile service applications. In most cases, links to trusted My Site host locations will be targeted to individual users or groups of users based on an identified business need. The links can be maintained and changed over time as business and user needs change. User Profile service application administrators can delete a link to a trusted My Site host locations when the users targeted by the link no longer require access to My Sites in multiple locations.
  
 **To add a trusted My Site host location by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
  - To use Central Administration to add a trusted My Site host location, you must be a member of the Farm Administrators group or a Service Application Administrator for the User Profile service application.
    
2. On the Central Administration Web site, under **Application Management**, click **Manage service applications**.
    
3. On the Manage Service Applications page, select the User Profile service application from the list of service applications.
    
4. On the ribbon, click **Manage**.
    
5. On the Manage Profile Service page, under **My Site Settings**, click **Configure Trusted Host Locations**.
    
6. On the Trusted My Site Host Locations page, click **New Link** to add a trusted My Site host location. 
    
7. On the Add Trusted Host Location page, enter the URL of the trusted personal site location in the URL box. 
    
8. In the **Description** box, enter a description for the trusted personal site location. 
    
9. Optionally, in the **Target Audiences** box, either type the user names or group names in the corresponding box or click **Browse** to select audiences by browsing, and then click **OK**. 
    
### Configure links to Office client applications
<a name="officelinks"> </a>

Users' My Sites are convenient locations for users to save files that they work on in Office client applications, such as Word, Excel, and PowerPoint. After you configure an environment for My Sites, you can add a link to the **Favorite Links** section that users see when they save documents in the **Save As** dialog in Office client applications. Users can then select their My Site and save files to the **Documents** library available on their My Site. 
  
 **To add a link to Office client applications**
  
1. Verify that you have the following administrative credentials:
    
  - To add a link to Office client applications, you must be a member of the Administrators group on the computer that is running the SharePoint Central Administration Web site.
    
2. On the Central Administration Web site, under **Application Management**, click **Manage service applications**.
    
3. On the Manage Service Applications page, select the User Profile service application from the list of service applications.
    
4. On the ribbon, click **Manage**.
    
5. On the Manage Profile Service page, under **My Site Settings**, click **Publish Links to Office Client Applications**.
    
6. On the Published links to Office client applications page, click **New Link**. 
    
7. On the Add Published Link page, in the **URL** box, type the URL of the location where users will be able to publish links. 
    
8. In the **Description** box, type a brief name for this location. 
    
    This is the name that will appear in the Favorite Links section of the Save As dialog.
    
9. Select the type of the location that this link represents. For example, if the target location is a SharePoint document library, select **Document Library**.
    
10. In the **Target Audiences** box, either type the name of the user or group to add or using the address book to find a user or group to add. Separate multiple user names or group names with a semicolon (;). You may also type All site users to select all users. 
    
    > [!NOTE]
    > To use the address book, click the book icon. In the dialog that appears, type all or part of a user's name, and then press ENTER. Scroll through the search results, and double-click the name of the user or users whom you want to add. Then click **OK**. 
  
11. Click **OK**. 
    
    The new link is displayed in the list of links on the Published links to Office client applications page.
    
### Promote site links on My Sites
<a name="personalizationsitelink"> </a>

If your organization wants to provide important information to users, it can do so by promoting a site link to a user's My Site. When you promote a site link, it appears on all the My Sites in the site collection. They can be used to display important company information. For instance, your organization might want to give users quick access to a timesheet. The destination of the link can be a site within the company intranet or an external site on the Internet. 
  
 **Add promote a site link to My Sites**
  
1. Verify that you have the following administrative credentials:
    
  - To use Central Administration to add a trusted My Site host location, you must be a member of the Farm Administrators group or a Service Application Administrator for the User Profile service application.
    
2. On the Central Administration Web site, under **Application Management**, click **Manage service applications**.
    
3. On the Manage Service Applications page, select the User Profile service application from the list of service applications.
    
4. On the ribbon, click **Manage**.
    
5. On the Manage Profile Service page, under **My Site Settings**, click **Manage promoted sites**.
    
6. On the Promoted Sites page, click **New Link**. 
    
7. On the Promoted a Site page, in the **Properties** section, do the following: 
    
1. In the **URL** box, type the URL of the site to which you want to link. 
    
2. In the **Description** box, type a description of the site. 
    
3. In the **Owner** box, type the name of an owner for this link, or click Browse to select an owner from the People Picker. 
    
4. Leave **Target Audiences** blank. 
    
    When you leave this box blank, the link that you specified in the URL box appears on the My Sites top link bar for all users.
    
    > [!NOTE]
    > If you want to specify target audiences for the site, either type the audience names in the **Target Audiences** box or click **Browse** to use the **Select Audiences** page. This option requires that you define an audience, set up rules for this audience, and compile the audience. 
  
8. Click **OK**. 
    
### Start related services
<a name="startsvcs"> </a>

If the related services for My Sites have not been started yet, start them so that My Sites functionality is available in your environment. For more information, see [Start or stop a service in SharePoint Server](../administration/start-or-stop-a-service.md).
  

