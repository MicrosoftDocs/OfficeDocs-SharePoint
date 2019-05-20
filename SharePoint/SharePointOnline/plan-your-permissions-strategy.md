---
title: "Plan your permissions strategy"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/2/2016
audience: Admin
ms.topic: conceptual
ms.prod: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_OD_share
- M365-collaboration
- Adm_SPO
- SharePoint_Online
ms.custom:
- Adm_O365_FullSet
search.appverid:
- WSU140
- WSU150
- SPO160
- BSA160
- OSU140
- OSU150
- OSU160
ms.assetid: c6183e49-9287-4689-999e-0d3f817a41a3
description: "Recommendations when you plan permissions in SharePoint Online, includes information on SharePoint Groups, site collection administrators, and securing data."
---

# Plan your permissions strategy

An effective permissions strategy will enhance the manageability and performance of your site, ensure compliance with your organization's data governance policies, and minimize the cost of maintenance for you and your organization.
    
## Why strategize?
<a name="__toc268492727"> </a>

Most websites are created speedily, with the aim of solving a particular problem or getting a specific set of information to people who need it quickly. 
  
That's good, but the structure of the site that you start with often becomes the default structure as your site collection grows and is required to meet other kinds of needs. This growth can result in permissions-settings chaos, where everyone in the organization has full control over subsites or every individual requires new permissions for every new site they need to use. 
  
A good permissions strategy can catch these problems before they get started. 
  
An effective permissions strategy gains you control in three main areas:
  
- **Manageability and performance.** The permissions settings you choose have long-term consequences for how much work it takes to manage your sites, and how speedily your sites respond to user commands. 
    
- **Data governance.** A planned permissions strategy can help you ensure compliance with your organization's data governance policies, which may be unique to your company or an essential part of complying with financial and accounting disclosure and retention legislation, such as Sarbanes-Oxley. 
    
- **Cost of maintenance.** A strategy that takes advantage of built-in efficiency tools, such as security groups, permission levels, and permissions inheritance will enhance ease of use for your site users, and minimize the requests for individual access that permissions managers have to respond to during the life of the site. 
    
## Tips for an effective permissions strategy
<a name="__toc252213638"> </a>

Keep these tips in mind to help create a simple, easy-to-maintain permissions strategy. 
  
### The principle of least privilege
<a name="__toc268492729"> </a>

Give people the lowest permission levels they need to perform their assigned tasks. 
  
### Work with security groups
<a name="__toc268492730"> </a>

- When you give people access, add them to standard, default security groups (such as Members, Visitors, and Owners). 
    
- Make most people members of the Members or Visitors groups. 
    
- People in the Members group can add or remove items or documents, but they cannot change the site structure, site settings, or site appearance. 
    
- People in the Visitors group have read-only access to the site, which means that they can see pages and items, and open items and documents, but cannot add, edit, or remove pages, items, or documents.
    
- Limit the number of people in the Owners group. 
    
- Only people you trust to change the structure, settings, or appearance of the site should be in the Owners group.
    
### Work with permissions inheritance
<a name="__toc268492731"> </a>

- Use permissions inheritance to create a clean, easy-to-visualize hierarchy.
    
- Managing permissions becomes more difficult and time-consuming when some lists within a site have fine-grained permissions, and when some sites have subsites with unique permissions and others with inherited permissions. 
    
- If you break permissions inheritance to use fine-grained permissions extensively, users may experience slower performance when they try to access site content. 
    
- It is much easier to manage and explain permissions when there is a clear hierarchy of permissions and inherited permissions. 
    
- Organize your content to take advantage of permissions inheritance.
    
- Consider segmenting your content by security level. Create a site or a library specifically for sensitive documents, rather than having them scattered in a larger library and protected by unique permissions.