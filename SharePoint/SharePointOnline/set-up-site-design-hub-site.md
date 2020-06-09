---
title: "Set up a site design for your hub site"
ms.reviewer: metorres
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
ms.custom: 
- Adm_O365
- seo-marvel-apr2020
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- GEA150
- BSA160
- BCS160
- GSP150
- MET150
description: In this article, you will learn how to run scripts on sites when they're associated with a hub site.
---

# Set up a site design for your hub site  

A site design is one or more site scripts that Microsoft SharePoint runs when a site is associated with a hub site. Actions describe changes to apply to the new site, such as creating a new list or adding nodes to the site navigation. Site designs provide reusable lists and custom actions so your users can quickly get started with the features they need. 

> [!NOTE]
> For organizations using Multi-Geo Capabilities in Microsoft 365, hub site designs work only when sites are in the same geo location as the hub site.

> [!NOTE]
> These instructions require the SharePoint admin or Global Admin role in Microsoft 365.

## 1. Create a JSON script, add it, and create the site design 

Follow the steps in [Get started creating site designs and site scripts](/sharepoint/dev/declarative-customization/get-started-create-site-design/). For the full list of supported actions, see [Site design JSON schema](/sharepoint/dev/declarative-customization/site-design-json-schema/). Note that when you create the site design, the site template you provide ("64" for team site or "68" for communication site) doesn't matter. 

## 2. Scope access to the hub site design 
 
When a site design is first created, it is available to everyone. You can grant View rights to the site design. After rights are granted, only the users or groups (principals) specified have access. We recommend granting access to the same principal used to scope the hub site.

```PowerShell  
Grant-SPOSiteDesignRights  
  -Identity <ID> 
  -Principals ("HR@contoso.sharepoint.com")  
  -Rights View 
```

Replace <ID> with the site design ID from when you added the site script.

## 3. Set your site design for the hub site 
You can set the hub site design in two ways. You can do it using the following PowerShell command: 

```PowerShell   
Set-SPOHubSite https://contoso.sharepoint.com/sites/Marketing  
-Title "Marketing Hub"  
-LogoUrl https://contoso.sharepoint.com/sites/Marketing/SiteAssets/hublogo.png  
-Description "Hub for the Marketing division" 
-SiteDesignId "<ID>" 
```

Replace <ID> with the site script ID from when you added the site script.  

You can also let hub site owners set the hub site design by using a new option available in the UI. For info about the hub site settings available to site owners, see [Set up your SharePoint hub site](https://support.office.com/article/e2daed64-658c-4462-aeaf-7d1a92eba098). 

