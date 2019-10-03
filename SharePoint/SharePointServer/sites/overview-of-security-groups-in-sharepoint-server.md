---
title: "Overview of security groups in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4cc0d9fc-943d-4c71-ab14-bda709f50f1a
description: "Overview of SharePoint Server groups."
---

# Overview of security groups in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can manage users of SharePoint sites more efficiently if you assign permission levels to groups instead of to individual users. A SharePoint group is a set of individual users and can also include Active Directory Domain Services (AD DS) groups.
    
## Introduction

In AD DS, the following groups are commonly used to organize users: 
  
- **Distribution group** A group that is used only for e-mail distribution and that is not security-enabled. Distribution groups cannot be listed in discretionary access control lists (DACLs), which are used to define permissions on resources and objects. 
    
- **Security group** A group that can be listed in DACLs. A security group can also be used as an e-mail entity. 
    
You can use security groups to control permissions for your site by adding security groups to SharePoint groups and granting permissions to the SharePoint groups. You cannot add distribution groups to SharePoint groups, but you can expand a distribution group and add the individual members to a SharePoint group. If you use this method, you must manually keep the SharePoint group synchronized with the distribution group. If you use security groups, you do not need to manage the individual users in the SharePoint application. Because you included the security group instead of the individual members of the group, AD DS manages the users for you. 
  
> [!NOTE]
>  For ease of security management, we do not recommend the following items when you manage AD DS groups. >  Assign permission levels directly to AD DS groups. >  Adding security groups that contain nested security groups, contacts, or distribution lists. 
  
## Decide whether to add security groups
<a name="section1"> </a>

Adding security groups to SharePoint groups provides centralized management of groups and security. The security group is the only place where you manage individual users. Once you add the security group to a SharePoint group, you do not have to manage security group members in that SharePoint group. If a user is removed from the security group, the user will be automatically removed from the SharePoint group.
  
However, security groups in SharePoint sites do not provide full visibility of what is occurring. For example, when a security group is added to a SharePoint group for a specific site, the site will not appear in the users' My Sites. The User Information List will not show individual users until they have contributed to the site. In addition, security groups that have deep nested structure might break SharePoint sites.
  
Considering the previous advantages and disadvantages, here are the recommendations:
  
- For intranet sites that are broadly accessed by your users, use security groups because you do not care about the individual users who accessed the intranet site home page.
    
- For collaboration sites that are accessed by a small group of users, add users directly to SharePoint groups. In this case, there is more of a need to know who is a member so the group members know each other's e-mail addresses and how to contact one another.
    
## Determine which security groups to use for granting access to sites
<a name="section1.1"> </a>

Each organization sets up its security groups differently. For easier permission management, security groups should be: 
  
- Large and stable enough that you are not continually adding additional security groups to your SharePoint sites. 
    
- Small enough that you can assign appropriate permissions. 
    
For example, a security group that is named "all users in building 2" is probably not small enough to assign permissions, unless all users in building 2 have the same job function, such as accounts receivable clerks. This is rarely the case. Therefore, you should look for a smaller, more specific set of users, such as "Accounts Receivable".
  
## Decide whether to allow access for all authenticated users
<a name="section2"> </a>

If you want all users within your domain to be able to view content on your site, consider granting access to all authenticated users (the Domain Users Windows security group). This special group allows all members of your domain to access a website (at the permission level that you choose), without your having to enable anonymous access. 
  
## Decide whether to allow access for anonymous users
<a name="section3"> </a>

You can enable anonymous access to allow users to view pages anonymously. Most Internet web sites allow anonymous viewing of a site, but might ask for authentication when someone wants to edit the site or buy an item on a shopping site. Anonymous access is disabled by default and must be granted at the web application level at the time that the web application is created.
  
If anonymous access is allowed for the web application, site administrators can decide whether to grant anonymous access to a site or any of the content on that site. 
  
Anonymous access relies on the anonymous user account on the web server. This account is created and maintained by Internet Information Services (IIS), not by your SharePoint site. By default in IIS, the anonymous user account is IUSR. When you enable anonymous access, you are in effect granting that account access to the SharePoint site. Allowing access to a site, or to lists and libraries, grants the View Items permission to the anonymous user account. Even with the View Items permission, however, there are restrictions to what anonymous users can do. Anonymous users cannot: 
  
- Open sites for editing in Office SharePoint Designer.
    
- View sites in My Network Places.
    
- Upload or edit documents in document libraries, such as wiki libraries. 
    
    > [!IMPORTANT]
    > To improve security for sites, lists, or libraries, do not enable anonymous access. Anonymous access allows users to contribute to lists, discussions, and surveys, which will possibly use up server disk space and other resources. Anonymous access also allows anonymous users to discover site information, including user e-mail addresses and any content posted to lists, and libraries, and discussions. 
  
Permission policies provide a centralized way to configure and manage a set of permissions that applies to only a subset of users or groups in a web application. You can manage permission policy for anonymous users by enabling or disabling anonymous access for a web application. If you enable anonymous access for a web application, site administrators can then grant or deny anonymous access at the site collection, site, or item level. If anonymous access is disabled for a web application, no sites within that web application can be accessed by anonymous users. 
  
- **None** No policy. This is the default option. No additional permission restrictions or additions are applied to site anonymous users. 
    
- **Deny Write** Anonymous users cannot write content, even if the site administrator specifically attempts to grant the anonymous user account that permission. 
    
- **Deny All** Anonymous users cannot have any access, even if site administrators specifically attempt to grant the anonymous user account access to their sites. For more information about permission policies, see [Manage permission policies for a web application in SharePoint Server](/SharePoint/administration/manage-permission-policies-for-a-web-application).
    
## See also
<a name="section3"> </a>

#### Other Resources

[Permissions planning for sites and content in SharePoint Server](/SharePoint/sites/permissions-planning-for-sites-and-content)
  
[Manage permission policies for a web application in SharePoint Server](/SharePoint/administration/manage-permission-policies-for-a-web-application)

