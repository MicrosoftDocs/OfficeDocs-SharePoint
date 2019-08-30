---
title: "Plan self-service site creation in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f7b617fc-cc45-41bf-bb71-f3d49ed4a59c
description: "Learn the critical decisions that you need to make when preparing for Self Service Site creation and management in SharePoint Server."
---

# Plan self-service site creation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Organizations have two ways to create site collections in their web applications. One way is to restrict site collection creation to Farm Administrators. The Farm Administrators create site collections either through the SharePoint Central Administration website or through the SharePoint Management Shell. This provides tight control. Another way is to enable Self Service Site Creation, to let users with the necessary rights create site collections under predefined paths. For information about using Microsoft PowerShell to create self-service sites with the SPSiteMaster cmdlets, see [SharePointServer](/powershell/module/sharepoint-server/?view=sharepoint-ps).
  
> [!NOTE]
> My Sites and the policies feature are not available in SharePoint Foundation 2013 and Self-Service Site Creation is disabled by default. 
  
    
## Determine who can create sites and a method for site creation
<a name="section1"> </a>

By default, new site collections can only be created by using Central Administration or the SharePoint Management Shell, by members of the Farm Administrators group. If your organization wants to tightly control and manage the environment so only a few people are allowed to add top-level sites, this is the method to use. However, if you have any of the following requirements, then self-service site creation might be the better choice for your organization:
  
- You want users to be able to easily create informal, perhaps even disposable, top-level sites, such as for short-term projects.
    
- You want to create an informal space for team, group, or community interaction.
    
- You are hosting top-level sites (either internally or externally) and want the process for requesting and receiving a top-level site to be as quick and low cost as possible.
    
There are several ways to allow users to create their own sites, while still maintaining some control over your environment. Consider which of the following methods will work best for your organization.
  
- **Self-Service Site Creation** Self-Service Site Creation enables users to create site collections under the /sites path (or other path you specify) within a particular web application. This method is best used when you want to allow groups or communities to create sites. This method also works well if you are hosting sites and want to allow users to create sites without waiting for a complicated process. The create a site user interface can be customized or replaced with a custom form that includes all of the information you might need to integrate with a billing system or to track custom metadata about the site at creation time. This method does not work well when large numbers of users need access to multiple sites. Because Self-Service Site Creation creates site collections, which have separate permissions, users need to be added uniquely to different site collections. If you use subsites instead, the users can be inherited from the parent site in the site collection. For more information, see [Configure self-service site creation in SharePoint Server 2019](/SharePoint/sites/configure-self-service-site-creation-in-sharepoint-server-2019). 
    
    Self-Service Site Creation can also be configured to create sites instead of site collections. When enabled, users can create a new site quickly and easily from their personal site. Clicking the **new site** link from the Sites page creates a new site. The site is created by using the Team Site template and will have separate permissions. The site creator can add additional users to the new site. 
    
- **Subsites of existing sites** Limit users to creating subsites of existing sites, instead of new site collections and top-level sites. Any user who has the Full Control or Manage Hierarchy permission level on an existing site can create a subsite. This method is the most limited, because you still control how many site collections there are. Because the sites are always subsites of other sites, they can be either easy to organize (if there are just a few) or very difficult to organize and browse. For example, if everyone in your organization wants a subsite and they create them at different levels in the site collection's hierarchy, the site collection can soon become very difficult to navigate. 
    
    > [!NOTE]
    > If you do not want users to have this capability, you can remove the Create Subsites right from the Full Control and Manage Hierarchy permission levels, either at the site collection or web application level. 
  
- **My Sites** Allow users to create personal sites (also known as My Sites). Personal sites are site collections stored under the /personal path of the web application. Personal sites are created for individual users, so they are not the appropriate method to use if you are trying to create sites for groups or communities. Self-Service Site Creation is used to create My sites For more information on My Sites, see [Configure My Sites in SharePoint Server](../install/configure-my-sites.md). 
    
> [!NOTE]
> Keep in mind that none of these methods can control how much space each site takes up in your content databases. To control site sizes, you should use quotas and set a size limit for site collections. You cannot set individual size limits for subsites. For more information, see [Quotas](plan-site-maintenance-and-management.md#section1). 
  
## Plan for Self-Service Site Creation
<a name="section2"> </a>

When you enable users to create site collections, they must have Use Self-Service Site Creation permission on the host site collection. When you enable users to create sites, they must have Create Subsites permission on the parent site. This capability can affect the security for your web server. You enable Self-Service Site Creation for a single web application at a time. If you want to use it on all web applications in your server farm, you must enable it for every web application individually.
  
> [!NOTE]
> Self-service site creation only creates path based site collections. You cannot create host-named site collections with self-service site collections. 
  
> [!NOTE]
> In SharePoint Foundation 2013, Self-Service Site Creation is disabled by default. When you enable Self-Service Site Creation, users can use the site creation page (http://\<server\>/_layouts/15/scsignup.aspx) to create a new site or site collection. 
  
> [!NOTE]
> If you want to use a path other than /sites for Self-Service Site Creation, you must add the path as a wildcard inclusion. 
  
If you enable Self-Service Site Creation, you should consider the following:
  
- We recommend that you should require a secondary site contact. Administrative alerts, such as those for when quotas are exceeded, or checking for unused websites, go to the primary and secondary administrators. Having more than one contact reduces administrator involvement with these sites because the secondary contact can perform required tasks even if the primary contact is not available.
    
- Define a storage quota and set it as the default quota for the web application.
    
    > [!NOTE]
    > You can also configure Self-Service Site Creation to apply a quota template to any site collections that are created. 
  
- Consider requiring a retention policy. When users create a site or site collection, they must select a policy to apply. For more information on site policies see, [Overview of site policies in SharePoint Server](site-policy-overview.md).
    
- Review the number of sites allowed per content database. Combined with quotas, this will help you limit the size of the databases in your system.
    
- Enable unused website notifications, so that sites that are forgotten or no longer of value can be identified.
    
Because Self-Service Site Creation creates new top-level websites on an existing web application, any new sites automatically conform to the web application's default quota settings, unused website notification settings, and other administrative policies.
  
You can configure Self-Service Site Creation in a variety of ways to meet your needs. For example, if you have a web application dedicated to My Sites, you can enable Self-Service Site Creation but select to hide the **new site** link so that no one can use it to create new sites or site collections. You can also create a custom form that users utilize to create a site or site collection.
  
## Plan for custom site creation processes
<a name="section3"> </a>

You can also create your own process for site creation by using a custom form to request a site that integrates with a back-end billing system to charge a customer's credit card or a corporate cost center. If you have a complicated system or process that you want to include as part of site creation, you should create a custom application to call the site creation interface and perform any other tasks that you require. However, if you simply want to add a few custom fields to the site creation page (for example, to track which department in your company is requesting a particular site), you should consider using Self-Service Site Creation and customize the sign-up page to include the information that you need. You can customize the scsignup.aspx page in the site definition to include the metadata that you need without having to develop an entire application.
  
## See also

[Configure self-service site creation in SharePoint Server 2019](/SharePoint/sites/configure-self-service-site-creation-in-sharepoint-server-2019)
  
