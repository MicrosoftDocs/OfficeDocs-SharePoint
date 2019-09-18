---
title: "Manage sites in the new SharePoint admin center"
ms.reviewer: 
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
  
To manage sites in the new SharePoint admin center, go to the current SharePoint admin center, click "Try it now" in the upper right, and then select **Active sites**. For info about the new SharePoint admin center, see [Get started with the new SharePoint admin center](get-started-new-admin-center.md).
  
## Create a site
<a name="createsite"> </a>
  
1. Click **Create**.
    
2. Select to create a team site (which will create an Office 365 group) or a communication site. To create a classic site, or a new team site that doesn't include an Office 365 group, click **Other options**. For info about the new site templates, see [Create a team site in SharePoint Online](https://support.office.com/article/ef10c1e7-15f3-42a3-98aa-b5972711777d) and [Create a communication site in SharePoint Online](https://support.office.com/article/7fb44b20-a72f-4d2c-9173-fc8f59ba50eb).
    
    ![Create a group-connected team site, communication site, or other site from the admin center](media/c4c5173f-ca83-426f-a940-cb2869a3a64b.png)
  
## Delete a site
<a name="deletesite"> </a>

Global admins and SharePoint admins can now delete sites that belong to an Office 365 group. Deleting these sites will delete the group and all its resources, including the Outlook mailbox and calendar, and any Teams channels. 
  
1. In the left column, click to select a site.
    
2. Click **Delete**, and then click **Delete** to confirm. 
    
You can recover deleted sites for 93 days. For more info, see [Restore deleted sites](/restore-deleted-site-collection.md). Note that deleted groups must be restored within 30 days.
  
## Add or remove owners
<a name="addremoveadmins"> </a>
  
1. In the left column, click to select a site. 
    
2. Click **Owners**. For a group-connected team site, you can add and remove group owners. For other sites, you can change the primary admin and add and remove other admins. Note that if you remove a person as a primary admin, they will still be listed as an additional admin. 
    
## Change a site's hub site association
<a name="hubsite"> </a>
  
1. In the left column, click to select a site. 
    
2. Click **Hub site**. The options that appear depend on whether the site you selected is registered as a hub site, or associated with a hub site. The hub site menu lets you register a site as a hub site, associate it with a hub site, change its hub site association, and unregister it as a hub site. [More info about hub sites](planning-hub-sites.md) 

## Change the external sharing setting for a site
<a name="changesitesharing"> </a>
  
1. In the left column, click to select a site.
    
2. Click **Sharing**.
    
3. Select an option, and then click **Save**.
    
    > [!NOTE]
    > The options that are available depend on the organization-wide setting you've selected. The setting for a site can be more restrictive, but not more permissive. 

  

  
## View site details
<a name="viewsitedetails"> </a>

To see more info about a site, click the site name to open the details pane.
  
![Site insights in the details pane](media/d0ddbc56-328e-42fb-b143-3faa14799fac.PNG)
  
Site insights in the details pane:
  
- The number of page views in the last 30 days
    
- The number of files viewed or edited in the last 30 days
    
- The date of the last activity on the site
    
- The number of files
    
- The amount of storage used (this value doesn't include changes made within the last 24-48 hours)
    
> [!NOTE]
> All these insights are available as columns in the site list. For info about adding a column that doesn't appear, see [Customize columns](manage-sites-in-new-admin-center.md#customizecolumns). 
  
![Site properties in the details pane](media/addeb5ec-cfc7-4d0c-a789-7eeeabdea67c.PNG)
  
Site properties in the details pane:
  
- The domain
    
- A link to the site
    
- The site template (also available as a column in the site list)

- Hub site association
    
- Whether the site belongs to an Office 365 group (also available as a column in the site list)
    
- The site description if specified
    
- The primary admin (also available as a column in the site list) and additional admins, with links to change the admins. If a site belongs to an Office 365 group, you can change the admins by changing the group owners. 
    
- The external sharing status (also available as a column in the site list)
    
## Sort and filter the site list
<a name="sortfilter"> </a>

Sorting and filtering the site list is just like sorting and filtering other lists in SharePoint.
  
1. Click the arrow next to the column header.
    
2. Select how you want to arrange the items. The options vary depending on the column. For example, you might have options to sort alphabetically, in numeric order, or chronologically.
    
    If the column allows filtering, you'll see a "Filter by" option. Select the value or values that you want to show. Your selections will appear with a check mark beside them. To remove a selection, click that value again. To clear all filters on the column, select **Clear filters**.
    
    ![Filter options for the Template column](media/0d188752-2bce-4d69-9cf4-a16ab87a2892.PNG)
  
## Search for a site
<a name="search"> </a>

You can search for a site by name, URL, primary admin, or template. To do this, enter keywords in the Search box and press Enter.

> [!NOTE] 
> Search doesn't look in hub site display names for the keywords you enter. <br>All characters you enter are treated as part of the query. Search doesn't recognize operators or wildcards (*). 
  
## Export to CSV
<a name="export"> </a>

To export your list of all sites as a .csv file that you can work with in Excel, click **Export**.
  
> [!NOTE]
> The Export command exports all sites and includes all columns, even if your current view is filtered. 
  
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
    
2. On the far right of the command bar, next to the Search box, click the View drop-down (the name changes depending on your current view).
    
3. Click **Save view as**.
    
4. In the **Save as** dialog box, enter a name for the view. 
    
    > [!NOTE]
    > To set the view as default, in the View drop-down, click **Set current view as default**. 
  

