---
title: "Set up a site design for your hub site"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- SPO160
- MOE150
- GEA150
- BSA160
- BCS160
- GSP150
- MET150
description: "Learn how to run scripts on sites when they're associated with a hub site."
---

# Set up a site design for your hub site  

A site design is one or more site scripts that SharePoint runs when a site is associated with a hub site. Actions describe changes to apply to the new site, such as creating a new list or adding nodes to the site navigation. Site designs provide reusable lists and custom actions so your users can quickly get started with the features they need. 

> [!NOTE]
> Some functionality is introduced gradually to organizations that have opted in to the [Targeted release option in Office 365](https://support.office.com/article/3b3adfa4-1777-4ff0-b606-fb8732101f47). This means that you may not yet see this feature or it may look different than what is described in this article. 

## 1. Create a JSON script, add it, and create the site design 

Follow the steps in [Get started creating site designs and site scripts](/sharepoint/dev/declarative-customization/get-started-create-site-design/). For the full list of supported actions, see [Site design JSON schema](/sharepoint/dev/declarative-customization/site-design-json-schema/). Note that when you create the site design, the site template you provide ("64" for team site or "68" for communication site) doesn't matter. 

## 2. Scope access to the hub site design 
 
When a site design is first created, it is available to everyone. You can grant View rights to the site design. After rights are granted, only the users or groups (principals) specified have access. We recommend granting access to the same principal used to scope the hub site.

```PowerShell  
Grant-SPOSiteDesignRights  
  -Identity <ID>` 
  -Principals ("HR@contoso.sharepoint.com") ` 
  -Rights View 
```

Replace <ID> with the site script ID from when you added the site script.

## 3. Set your site design for the hub site 
You can set the hub site design in two ways. You can do it using the following PowerShell command: 

```PowerShell   
Set-SPOHubSite https://contoso.sharepoint.com/sites/Marketing ` 
-Title "Marketing Hub" ` 
-LogoUrl https://contoso.sharepoint.com/sites/Marketing/SiteAssets/hublogo.png ` 
-Description "Hub for the Marketing division” 
-SiteDesignId "<ID>” 
```

Replace <ID> with the site script ID from when you added the site script.  

You can also let hub site owners set the hub site design by using a new option available in the UI. For info about the hub site settings available to site owners, see [Set up your SharePoint hub site](https://support.office.com/article/e2daed64-658c-4462-aeaf-7d1a92eba098). 

