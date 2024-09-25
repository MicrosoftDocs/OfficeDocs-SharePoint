---
ms.date: 07/06/2021
title: "Custom list templates"
ms.reviewer: hasaladi
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Add and remove custom templates and change who has permission to access them."
---

# Creating custom list templates  

As a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) and [above](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365, you can provide custom list templates for users in your organization. When users create new lists, they can select from these templates alongside the built-in templates from Microsoft. This feature enables your organization to create repeatable list solutions (in SharePoint, Teams, and within the Lists app itself). 

You can create and manage custom list templates using Microsoft PowerShell:

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

## Add a custom template 

Follow these steps to create a custom list template.

1. Run the following command to extract the site script output from an existing list and write it to a variable:
  
    ```PowerShell
    $extracted = Get-SPOSiteScriptFromList -ListUrl "https://contoso.sharepoint.com/sites/strategy/customer-contacts" 
    ```

2. Reference the variable in the following command to upload a site script that can be used with a list design. 

    ```PowerShell
    Add-SPOSiteScript 
      -Title "Contoso Customer Tracker" 
      -Description "This creates a customer contact list" 
      -Content $extracted 
    ```

3. Create your list design using the site script ID returned from the step above:

    ```PowerShell
    Add-SPOListDesign 
      -Title "Contoso customer tracking" 
      -Description "Tracks key customer data in a list" 
      -SiteScripts "<ID from previous step>" 
      -ListColor Orange 
      -ListIcon BullseyeTarget 
      -Thumbnail "https://contoso.sharepoint.com/SiteAssets/site-thumbnail.png" 
    ```

When users in your organization create a list (in SharePoint, Teams, or the Lists app), they see the template on the "From your organization" tab. 

![The "Contoso customer tracking" template on the "From your organization" tab of the Create a list dialog box.](media/contoso-customer-tracking.png)

> [!NOTE]
> List templates can't be updated after you add them. Instead, remove the existing template and add the updated version.

## Scope the permissions to a custom template 


By default, the custom list template is available to everyone in your organization. If you want, you can limit access to specific users or a security group. The following example shows how to grant an individual user view rights to a template. 


```PowerShell
Grant-SPOSiteDesignRights 
  -Identity <List design ID to apply rights to> 
  -Principals "nestorw@contoso.onmicrosoft.com" 
  -Rights View 
```

## Get templates 

The following example retrieves all custom list templates. 

```PowerShell
Get-SPOListDesign <List design ID> 
```

## Remove a custom template 

The following example shows how to remove a custom list template so that it's no longer available to users when they create lists. 

```PowerShell
Remove-SPOListDesign <List design ID> 
```

You can also remove the associated site scripts that the list design is referencing using:  

```PowerShell
Remove-SPOSiteScript <Site script ID> 
```


