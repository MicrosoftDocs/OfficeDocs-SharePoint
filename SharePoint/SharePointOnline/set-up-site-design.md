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
description: "Learn how to create and add a site script, create a site design and scope access to it, and set the design as the hub site design."
---

# Set up a site design for your hub site  

A site design is one or more site scripts that SharePoint runs when a site is associated with a hub site. Actions describe changes to apply to the new site, such as creating a new list or adding nodes to the site navigation. Site designs provide reusable lists, or custom actions so your users can quickly get started with the features they need. To get started, follow these steps.  

## 1. Create a site script 

Create a JSON script such as the following, detailing the actions you want to perform. For the full list of supported actions, see [Site design JSON schema](/sharepoint/dev/declarative-customization/site-design-json-schema/). 

```JSON
{ 
  "$schema": "schema.json", 
  "actions": [ 
        { 
      "verb": "createSPList", 
      "listName": "Issues List", 
      "templateType": 100, 
      "subactions": [ 
        { 
          "verb": "SetDescription", 
          "description": "Describe the issue in detail" 
        }, 
        { 
          "verb": "addSPField", 
          "fieldType": "Number", 
          "displayName": "Priority", 
          "addToDefaultView": true, 
          "isRequired": true 
        }, 
        { 
          "verb": "addSPField", 
           "fieldType": "User", 
          "displayName": "Contact", 
          "addToDefaultView": true, 
          "isRequired": true 
        }, 
      ] 
    } 
{ 
    "verb": "addPrincipalToSPGroup", 
    "principal": "HRFTE", /* mail-enabled sg */ 
    "group": "Visitors" 
}, 
  ], 
  "version": 1 
} 
```
## 2. Add the site script 

Each site script must be registered in SharePoint so that it is available to use. Add the site script by using the Add-SPOSiteScript cmdlet. The following example shows how to add the JSON script described previously. 

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066)

3. Run the following command.
 
```PowerShell
Add-SPOSiteScript  
 -Title "Human Resources hub join"  
 -Content $site_script  
 -Description "Creates issues list, adds administrators’ group and adds link to policies to site nav” 
```
After running the cmdlet, you get a result that lists the site script ID of the added script. Keep track of this ID somewhere because you will need it later when you create the site design.

## 3. Create the site design 

Run the following cmdlet to create the site design and associate it with one or more site scripts. Replace <ID> with the site script ID from when you added the site script. 

```PowerShell
Add-SPOSiteDesign  
 -Title "Human Resources hub"  
 -SiteScripts "<ID>"  
 -Description "Creates issues list, adds administrators’ group and adds link to policies to site nav " 
```

## 4. Scope access to the hub site design 
 
When a site design is first created, it is available to everyone. You can grant View rights to the site design. After rights are granted, only the users or groups (principals) specified have access. We recommend granting access to the same principal used to scope the hub site.

```PowerShell  
Grant-SPOSiteDesignRights  
  -Identity db752673-18fd-44db-865a-aa3e0b28698e` 
  -Principals ("HR@contoso.sharepoint.com") ` 
  -Rights View 
```

## 5. Set your site design for the hub site 
You can set the hub site design in two ways. You can do it using the following PowerShell command: 

```PowerShell   
Set-SPOHubSite https://contoso.sharepoint.com/sites/Marketing ` 
-Title "Marketing Hub" ` 
-LogoUrl https://contoso.sharepoint.com/sites/Marketing/SiteAssets/hublogo.png ` 
-Description "Hub for the Marketing division” 
-SiteDesignId "db752673-18fd-44db-865a-aa3e0b28698e” 
```
 
You can also let hub site owners set the hub site design by using a new option available in the UI.  

