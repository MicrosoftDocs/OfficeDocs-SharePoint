---
title: "Create a hub site in SharePoint Online"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/20/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid: SPO160
ms.assetid: 92bea781-15d8-4bda-805c-e441e2191ff3
description: "Learn how to use PowerShell to create a hub site in SharePoint Online"
---

# Create a hub site in SharePoint Online

If you're a global or SharePoint admin in Office 365, you can convert any existing site to a hub site using Microsoft PowerShell.
  
> [!NOTE]
>  We recommend selecting a communication site, or a team site that uses the new template. If you use a classic team site, the hub navigation will appear only on modern pages, and hub site settings will only appear on modern pages. Sites that are already associated to another hub can't be converted to a hub site. >  You can create up to 50 hub sites for an organization. There is no limit on the number of sites that can be associated with a hub site. >  Hub sites aren't available if you set up SharePoint Multi-Geo for your organization. >  When users associate their sites with a hub, it doesn't impact the permissions of either the hub site or the associated sites. It's important to make sure all users you allow to associate sites to the hub have permission to the hub. 
  
## Create a hub site using PowerShell

1. Download and install the latest [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you already have a previous version installed, uninstall it first and then install the latest version.
    
2. Connect the SharePoint Online Management Shell to SharePoint Online for your organization. For info, see [Connect the SharePoint Online PowerShell](https://go.microsoft.com/fwlink/?linkid=869066). 
    
3. (Optional) If you want a group of people to be able to associate their sites to the hub, create a mail-enabled security group and add the users.
    
4. Run the following command to convert the site to a hub site and enable the hub site features:
    
  ```
  Register-SPOHubSite URL
  ```

    (Where  *URL*  is the URL of the site.) 
    
5. When prompted with **Principals[0]**, provide the group created in step 3, or the UPN of an individual user. You can enter additional principals, one per line. Once you are finished assigning permissions, press Enter. If you want all site owners in the organization to be able to associate their sites with the hub, press Enter at the first prompt.﻿ 
    
    Note: To restrict permission to associate sites to the hub after creation, run the following command:
    
    Grant-SPOHubSiteRights -Identity -Principals GroupEmail -Rights Join
    
    (Where Identity is the URL of the site and GroupEmail is the email address of the mail-enabled security group.) 
    
6. Notify the hub site owners that their site has been converted to a hub site.
    
## More info

- For info about the above PowerShell commands, as well as the other commands for managing hub sites, see [Manage SharePoint hub sites](https://go.microsoft.com/fwlink/?linkid=869058).
    
- You can also use a site design to automate the joining of a newly created site to an existing hub site by using the joinHub site script action. For info about how to create the site script and site design, see [SharePoint site design and site script overview](https://go.microsoft.com/fwlink/?linkid=870437).
    
- For info about how site owners can customize hub sites, see [Set up your SharePoint hub site](https://support.office.com/article/e2daed64-658c-4462-aeaf-7d1a92eba098).
    
## See Also

[Remove a hub site](remove-a-hub-site)
  

