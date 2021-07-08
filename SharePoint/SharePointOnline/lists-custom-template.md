---
title: "Custom list templates"
ms.reviewer: hasaladi
ms.author: kaarins
author: kaarins
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Add and remove custom templates for the Lists app and change who has permission to access them."
---

# Creating custom list templates  

As a global or SharePoint admin in Microsoft 365, you can create and add custom list templates from your organization alongside the ready-made templates Microsoft provides to make it easy for your users to get started on tracking and managing information. This will empower your organization to create repeatable solutions within the same Microsoft Lists infrastructure (including list creation in SharePoint, Teams, and within the Lists app itself). 

You can create custom list templates and manage them using Microsoft PowerShell 

## Adding a custom list template 

The following example takes you through the process of creating a custom list template. 


1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command to extract the site script output from an existing list and write it to a variable:
  
    ```PowerShell
    $extracted = Get-SPOSiteScriptFromList -ListUrl "https://contoso.sharepoint.com/sites/strategy/customer-contacts" 
    ```
4. Reference the variable in the following command to upload a site script that can be used with a list design. 

    ```PowerShell
    Add-SPOSiteScript 
      -Title "Contoso Customer Tracker" 
      -Description "This creates a customer contact list" 
      -Content $extracted 
    ```
5. Create your list design using the site script ID returned from the step above:

    ```PowerShell
    Add-SPOListDesign 
      -Title "Contoso customer tracking" 
      -Description "Tracks key customer data in a list" 
      -SiteScripts "<ID from previous step>" 
      -ListColor Orange 
      -ListIcon BullseyeTarget 
      -Thumbnail "https://contoso.sharepoint.com/SiteAssets/site-thumbnail.png" 
    ```

All users in your organization should now be able to see the custom list template “Contoso customer tracking” wherever they can create lists from (Lists app, SharePoint Sites, Teams) 

Updated list creation dialog
![The list creation dialog with a new tab for custom list templates](media/custom-list-template-tab.png)

## Scoping custom template permissions 

By default, the custom list template will be available to everyone in your organization. Optionally, you can grant view rights to a set of users or a security group effectively scoping the visibility of the custom list template in the UX. This example shows how to grant view rights on the list design from the step above, to Nestor (a user at the fictional Contoso site). 

```PowerShell
Grant-SPOSiteDesignRights 
  -Identity <List design ID to apply rights to> 
  -Principals "nestorw@contoso.onmicrosoft.com" 
  -Rights View 
```
## Removing a custom template 

The following example shows how to remove a custom list template. 

Once the list design is removed, it no longer appears in the UI for creating new lists. 

```PowerShell
Remove-SPOListDesign <List design ID> 
```

You can also remove the associated site scripts that the list design is referencing using:  

```PowerShell
Remove-SPOSiteScript <Site script ID> 
```
List creation dialog without any custom templates
![Empty state for the custom list templates tab](media/empty-state.png)

> [!NOTE]
> Updating a current list template is currently not available, so it is recommended to remove and recreate the list template again using the steps above.
