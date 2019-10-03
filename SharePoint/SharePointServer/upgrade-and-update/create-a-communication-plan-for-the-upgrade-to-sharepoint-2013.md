---
title: "Create a communication plan for the upgrade to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6633015d-3938-4d83-b814-f3af85101f49
description: "Communicate timelines, requirements, and how to obtain help with site owners and users during upgrade to SharePoint 2013."
---

# Create a communication plan for the upgrade to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
It is important that you communicate with users during the upgrade process from SharePoint 2010 Products to SharePoint 2013. Site users have to know what to expect when they visit their sites again after you have upgraded the environment. Site owners have to know how they can help prepare for upgrade and what they have to do to upgrade their site collections in SharePoint 2013 and My Sites in SharePoint 2013. Both site users and site owners have to know when the upgrade will occur. As part of the planning process, determine the following:
  
- Who are the members of the upgrade team, what other stakeholders are involved, and who will be affected by the upgrade?
    
- What information must the upgrade team have, and when?
    
- What information must site users and other stakeholders have, and when?
    
This article describes how to create a communication plan so that the upgrade team, stakeholders, and users know what to expect before, during, and after the upgrade.
  
## Who is a member of the upgrade team?
<a name="UpgradeTeam"> </a>

For small deployments in which sites were not customized extensively, the upgrade team might consist of only one person. For larger deployments, on the other hand, several people with different roles can be required, as described in the following list: 
  
- **Server administrators** Server administrators perform most of the upgrade tasks. There must be at least one server administrator on the upgrade team because running the Setup wizard requires someone who is a member of the Administrators group on each front-end web server. 
    
    > [!NOTE]
    > Farm administrators might not be local administrators for the server. 
  
- **Database administrators** If you have a separate database administration team, you must coordinate with them to schedule the upgrade and perform the upgrade. 
    
- **Server security teams** You must coordinate with your security teams, such as the Active Directory Domain Services (AD DS) team, to verify accounts and permissions or to take advantage of the new policy settings that you can apply for SharePoint 2013. 
    
- **Network teams** You must coordinate with the network teams, especially if you must switch DNS to point to your new farm, or add the new servers to the network infrastructure. 
    
- **Client deployment team** Communicate with client deployment teams to coordinate deployments of new client and server applications. Client deployment might have to occur before you upgrade, or it might be an option for users after their sites are upgraded. 
    
- **Services administrators** You must communicate with the administrators for service applications, such as the Business Data Connectivity service, to make sure that they are ready for the upgrade and they can review or reconfigure the appropriate settings in the new version. 
    
- **IT or application Helpdesk leadership and personnel** If you have a helpdesk for your company, make sure that they know about the timing for the upgrade and are prepared for questions after upgrade. Helpdesk should be a key stakeholder for planning and testing so that they can be understand the potential changes from an upgrade and the effect that it will have on users. 
    
- **Site collection owners** You must notify site collection owners when the upgrade process is about to occur. Warn them about any issues that you find when you run the pre-upgrade checker or when you upgrade their sites. You must also communicate with site collection owners about their role in upgrade. Site collection owners can upgrade their own sites in SharePoint 2013. Site collection owners can run health checks and review upgrade evaluation sites before they upgrade their sites. 
    
- **Site designers and developers and third-party solution providers** If you have custom templates, Web Parts, Web services, or other custom elements that are associated with your sites, you must work with the associated site designers and developers or third-party solution providers. Because custom elements can fail or perform differently in an upgraded environment, you have to make sure that designers or developers can create new versions of these custom elements or verify that these elements were upgraded correctly. Because their work can have a big influence on the upgrade schedule, work with these stakeholders early in the process. For more information about potential issues with custom elements, see [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)).
    
- **Site users** Although you do not have to include site users in making decisions about the upgrade process, you must tell site users when it will occur and what they should expect. 
    
- **Sponsors and other stakeholders** Other people in your organization might be involved in the upgrade planning process. Make sure that you include them in your communication plan appropriately. 
    
    > [!NOTE]
    > An upgrade team can include one or more members in each role, depending on your organization. 
  
## When and what to communicate to the upgrade team
<a name="CommtoUpgradeTeam"> </a>

In general, the server administrators and service application administrators set the timeline for upgrade, and site owners are notified only when the process is about to begin. However, because team members have their own tasks to perform at particular points in the overall upgrade process, it is very important that you have a solid plan to communicate the progress of the upgrade to all team members so that everyone knows when it is time to perform their particular tasks. 
  
The whole upgrade team must work together to determine the dates and times to perform the upgrade. We recommend that you choose an upgrade window to occur when site usage is lowest. For small single-server deployments, upgrade may be completed in less than a day. Larger deployments can take more time, up to a weekend. There is no way to determine the precise length of time that will be required to upgrade any particular site collection. Because of this, it is very important to communicate with other team members involved in the upgrade process in addition to users. The day or days that you choose for upgrading should be far enough in the future that the upgrade team has enough time to complete all of the preliminary steps. When you plan the timeline, make sure that you schedule time to validate the upgraded sites and time to implement any changes or do any work to re-brand sites.
  
It is important to communicate with site owners, designers, and developers at the following points during the upgrade process:
  
- Before the trial upgrade so that they know the general timeline and their roles in the process.
    
- After you perform a trial upgrade to find issues. For example, issues such as customized site templates or custom Web Parts should be reported to the appropriate site owner, designer, or developer before you schedule the upgrade, to give them time to investigate the issues and take preliminary steps. Or a developer might decide that it would be prudent to rebuild a Web Part before the upgrade occurs. And site owners might want to note any customizations that were done to their sites, such as site templates and changes to core Active Server Page Extension (ASPX) files. 
    
- After the environment is upgraded so that they can review the sites and make any changes that are needed.
    
- When you are ready for them to upgrade their site collections.
    
## When and what to communicate to site users
<a name="CommtoSiteUsers"> </a>

It is equally important to communicate with the users of the sites to tell them about the following issues: 
  
- **When the environment will be upgraded** In particular, you must also inform them if their sites will be unavailable during the upgrade. 
    
- **When their sites will upgraded** Site collection owners should communicate to their site users about the timeline for upgrading the site collection. If you, as a server farm administrator, are upgrading a site, you should communicate when that will occur. 
    
- **How the upgrade might affect them and what they should know about the new environment** For example, the site will look different and function slightly differently in the new user interface. You can also point them to available content, such as What's New article. For more information about feature changes, see [What's new](../what-s-new/what-s-new.md). 
    
- **How to obtain help** If they find an issue with their site after upgrade, how can they obtain help in addressing it? 
    
You can use the new system status bar in the site collections to notify users of these items. For more information about how to set notifications for the status bar, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#Notifications) in the article [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)).
  
## See also
<a name="CommtoSiteUsers"> </a>

#### Other Resources

[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)

