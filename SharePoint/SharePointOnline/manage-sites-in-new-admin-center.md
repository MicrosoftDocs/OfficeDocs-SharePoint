---
title: "Manage sites in the new SharePoint admin center"
ms.reviewer: trgreen
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160
ms.assetid: d8c63491-0410-405c-880a-8cef7fa4480a
description: "Learn about tasks you can perform on the Active sites page of the new SharePoint admin center."
---

# Manage sites in the new SharePoint admin center

The Active sites page of the new SharePoint admin center lets you view the SharePoint sites in your organization (including the new communication sites and sites that belong to Office 365 groups). It also lets you sort and filter sites, search for a site, and create new sites.
  
![Manage sites in the new SharePoint admin center](media/2a18e27e-47ba-4370-8d91-cb6d75d746b5.png)
  
> [!NOTE]
> The Active sites page lists the root website for each site collection. Subsites aren't included in the list. <br>Some functionality is introduced gradually to organizations that have opted in to the [Targeted release option in Office 365](/office365/admin/manage/release-options-in-office-365). This means that you may not yet see this feature or it may look different than what is described in this article. 
  
To manage sites in the new SharePoint admin center, go to the current SharePoint admin center, select "Open it now" in the upper right, and then select **Active sites**. For info about the new SharePoint admin center, see [Get started with the new SharePoint admin center](get-started-new-admin-center.md).
  
For info about creating sites, see [Create a site](create-site-collection.md). For info about deleting sites, see [Delete a site](delete-site-collection.md)
  
## Add or remove site admins and group owners
<a name="addremoveadmins"> </a>
  
1. In the left column, click to select a site. 
    
2. Select **Permissions**. For a group-connected team site, you can add and remove group owners and additional site admins. For other sites, you can add and remove site admins and change the primary admin. Note that if you remove a person as a primary admin, they will still be listed as an additional admin. For info about each role, see [About site permissions](site-permissions.md). 
    
## Change a site's hub association
<a name="hubsite"> </a>
  
1. In the left column, click to select a site. 
    
2. Select **Hub**. The options that appear depend on whether the site you selected is registered as a hub site, or associated with a hub. The Hub menu lets you register a site as a hub site, associate it with a hub, change its hub association, and unregister it as a hub site. [More info about hub sites](planning-hub-sites.md) 

## Change the external sharing setting for a site
<a name="changesitesharing"> </a>
  
1. In the left column, click to select a site.
    
2. Select **Sharing**.
    
3. Select an option, and then click **Save**. For info about the options, see [Turn external sharing on or off for for a site](change-external-sharing-site.md).
    
    > [!NOTE]
    > The options that are available depend on the organization-wide setting you've selected. The setting for a site can be more restrictive, but not more permissive. 

  
## View site details
<a name="viewsitedetails"> </a>

To see more info about a site, click the site name to open the details panel.
  
![The General tab of the details panel](media/d0ddbc56-328e-42fb-b143-3faa14799fac.PNG)
  
To view site activity including the number of files stored and storage usage, select the **Activity** tab.
  
To view site admins, owners, members, and visitors, select the **Permissions** tab.

![The Permissions tab of the details panel](media/addeb5ec-cfc7-4d0c-a789-7eeeabdea67c.PNG)
  
For info about the roles in this panel, see [About site permissions](site-permissions.md).
    
## Sort and filter the site list
<a name="sortfilter"> </a>

Sorting and filtering the site list is just like sorting and filtering other lists in SharePoint.
  
1. Click the arrow next to the column header.
    
2. Select how you want to arrange the items. The options vary depending on the column. For example, you might have options to sort alphabetically, in numeric order, or chronologically.
    
    If the column allows filtering, you'll see a "Filter by" option. Select the value or values that you want to show. Your selections will appear with a check mark beside them. To remove a selection, click that value again. To clear all filters on the column, select **Clear filters**.
    
    ![Filter options for the Template column](media/0d188752-2bce-4d69-9cf4-a16ab87a2892.PNG)

## Customize columns
<a name="customizecolumns"> </a>

1. Click the arrow next to any column header, and then select **Customize columns**.
    
2. Select and clear check boxes to show and hide columns.
    
3. Rearrange the columns by pointing to a column and clicking the up or down arrow to move the column up or down.
    
    ![Show, hide, and rearrange columns on the Active sites page](media/d713dbd8-2ac7-428c-a5b9-b5bd673ce674.PNG)
  
## Switch views and create custom views
<a name="views"> </a>

The new SharePoint admin center comes with a few built-in views: Office 365 group sites, Sites without a group, Largest sites, Least active sites, and Most popular shared sites. You can also create and save custom views.
  
1. Customize columns, sort, and filter your view the way you want. (Views that are filtered through search can't be saved.)
    
2. On the far right of the command bar, next to the Search box, click the View menu (the name changes depending on your current view).

    ![The View menu](media/view-menu.PNG)
    
3. Click **Save view as**.
    
4. In the **Save as** dialog box, enter a name for the view. 
    
    > [!NOTE]
    > To set the view as default, in the View drop-down, click **Set current view as default**. 
  
  
## Search for a site
<a name="search"> </a>

You can search for a site by name, URL, primary admin, or template. To do this, enter keywords in the Search box and press Enter.

> [!NOTE] 
> Search doesn't look in hub site display names for the keywords you enter. <br>All characters you enter are treated as part of the query. Search doesn't recognize operators or wildcards (*). 
  
## Export to CSV
<a name="export"> </a>

To export your list of all sites as a .csv file that you can work with in Excel, click **Export**.
  
> [!NOTE]
> The Export command exports all sites, even if your current view is filtered. 
  


