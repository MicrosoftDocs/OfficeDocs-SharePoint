---
title: "Plan for site maintenance and management in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/8/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4fdf96bd-813f-4499-b7d2-958b7bce002c
description: "Learn how to control resource utilization through management of sites and site collections in SharePoint Server."
---

# Plan for site maintenance and management in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Every site and site collection in your SharePoint Server farm uses system resources, such as storage, processing, and network. If sites are unused or abandoned they use resources but don't deliver any business value, and so they are using storage space that could be used somewhere else. Out-of-control sites use system resources beyond what your original plan may have allocated to them. In both cases, access to system resources is being denied and performance will suffer, overhead increases, and manageability decreases. To help you avoid these issues, you need to plan for managing your sites and site collections. This article tells you about the tools you can use to manage sites and site collections in SharePoint Server.
  
    
## Quotas
<a name="section1"> </a>

The first step in controlling the amount of resources that your sites and site collections use is to establish and apply quota templates. Quotas let you control how much data a site collection can hold and then lock the site to further content when site storage reaches a maximum size. With quotas you can also control the amount of resources, such as processor and memory, that a site or site collection can use. Quotas let you set storage limit values and warning limit values as well as resource utilization limits which applications cannot exceed. Once you configure and apply quotas, you reduce the impact of issues caused by out-of-control site collections. For more information on working with quotas and how to configure them, see [Create, edit, and delete quota templates in SharePoint Server](create-edit-and-delete-quota-templates.md).
  
When you perform your database and server capacity planning, determine what size limits (if any) you want to enforce. The following list describes how to take the best advantage of quotas:
  
- Create different quota templates for different site types. For example, you might want different quotas for different divisions, or for different customer types, or for different paths (perhaps sites under the /sites path only get 100 MB per site collection, whereas sites under the /VIP path can take up to 300 MB per site collection). Whenever you create a site collection from Central Administration, you can specify which quota template to use. Note that sites created by using Self-Service Site Management use the default quota for the web application.
    
- Give enough room for reasonable growth in sites. Depending on what each site is used for, storage space needs can vary dramatically. Sites are designed to grow over time as they are used. A quota limit of 50 MB is unlikely to be enough storage space to start with for most sites, and is unlikely to be anywhere near enough for a site that has a long life.
    
- Allow for reasonable notice between the warning email message and locking the site for exceeding its quota. For example, do not set the warning limit to 80 MB and the site storage limit to 85 MB. If users are in the middle of uploading several large files, they will not be happy if they are blocked from completing that task with very little notice.
    
- Archive obsolete content or sites. However, if you are going to archive or delete obsolete content or sites, be sure that users understand that plan and that you perform these actions only at predictable times. For example, publish a schedule of when you are going to archive content or delete unused sites.
    
- Periodically review site permissions. For example, review the permissions quarterly to remove permissions for any users who have left the group or project.
    
- Create a plan to back up site content often. Determine or discover how often backups will be made, and the process for restoring content when necessary. For more , see [Plan for backup and recovery in SharePoint Server](../administration/backup-and-recovery-planning.md).
    
## Usage reports
<a name="section2"> </a>

Quotas prevent site collections as a whole from exceeding the limits you set, but within a site collection, some sites and pages will be used more than others. In order to balance your system resources you need to be aware of highly used pages and sites and of underused or abandoned sites. The highly used sites may need more resources and underused or abandoned ones should be archived or deleted. One part of your site maintenance plan should be a plan for how to manage the size and number of site collections in your environment. This is most important if you allow Self-Service Site Management. Most organizations want to be able to predict and control how much growth they can expect from sites because of the impact that they can have on database resources. For example, if a content database contains 100 sites, and one of those sites is taking up more than 50 percent of the space, then you might need to move that site collection to a different content database. This will ensure that you preserve some room for additional growth, while maintaining the ability to back up and restore the databases.
  
In SharePoint Server usage reports let you track the number of hits and number of unique users for a site or site collection on a daily and monthly basis. Before you can view the reports, a farm administrator must configure usage and data collection. For more information, see [Configure usage and health data collection in SharePoint Server](../administration/configure-usage-and-health-data-collection.md). For more information on viewing and using usage reports, see [View usage reports in SharePoint Server](../administration/view-usage-reports.md).
  
## Site and site collection deletion
<a name="section3"> </a>

You need to plan how you will handle sites that become inactive after a project has ended, or sites that users created just to test some ideas, but then abandoned. Site use confirmation and deletion can help you keep your environment cleaner, by helping you identify when sites are no longer needed. This feature works by automatically sending an email message to site owners to see if they consider their site active. If the owner does not respond to the email message (after a specified number of messages over a specified length of time), the site can be deleted. For more information on managing unused site collections, see [Manage unused site collections in SharePoint Server](manage-unused-site-collections.md).
  
To plan for site use confirmation and deletion, decide the following:
  
- How long you want to wait before checking to see if a site is inactive. The default length of time for team or project sites is 90 days after site creation. Usually a site that was created, actively used, and is now ready to be deleted or archived, took at least six months and probably a few years to complete that life cycle. Reminders every six months are valuable for those situations.
    
- How often you want to send an email message to site owners to see if their sites are inactive. After the first email message, if the site administrator does not respond, you can continue with additional notices at daily, weekly, or monthly intervals.
    
- If you want to automatically delete unused sites. If the site administrator does not respond to multiple email messages, do you want to go ahead and delete the site automatically? We recommend that you make a backup first. You can do so by making sure that regular backups are performed.
    
- If you are going to automatically delete unused sites, how many email messages will you send to site owners before you do so? By default, four weekly notices are sent before site deletion, but you can increase or decrease this number to suit your needs.
    
## See also
<a name="section3"> </a>

#### Concepts

[Manage unused site collections in SharePoint Server](manage-unused-site-collections.md)
  
[Create, edit, and delete quota templates in SharePoint Server](create-edit-and-delete-quota-templates.md)
  
[Configure usage and health data collection in SharePoint Server](../administration/configure-usage-and-health-data-collection.md)
  
[Delete and restore site collections in SharePoint Server](delete-and-restore-site-collections.md)
  
[Create a site collection in SharePoint Server](create-a-site-collection.md)

