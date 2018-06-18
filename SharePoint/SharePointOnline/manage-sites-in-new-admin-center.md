---
title: "Manage sites in the new SharePoint admin center"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/1/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
ms.assetid: d8c63491-0410-405c-880a-8cef7fa4480a
description: "Learn about tasks you can perform on the Site management page of the new SharePoint admin center."
---

# Manage sites in the new SharePoint admin center

The Site management page of the new SharePoint admin center (preview) lets you view the SharePoint sites in your organization (including the new communication sites and sites that belong to Office 365 groups). It also lets you sort and filter sites, search for a site, and create new sites.
  
![Manage sites in the new SharePoint admin center](media/2a18e27e-47ba-4370-8d91-cb6d75d746b5.png)
  
> [!NOTE]
> The Site management page lists the root website for each site collection. Subsites aren't included in the list. > Some functionality is introduced gradually to organizations that have opted in to the [Set up the Standard or Targeted release options in Office 365](https://support.office.com/article/3b3adfa4-1777-4ff0-b606-fb8732101f47). This means that you may not yet see this feature or it may look different than what is described in this article. 
  
To manage sites in the new SharePoint admin center, go to the current SharePoint admin center, click "Try the preview" in the upper right, and then select **Site management**. For info about the new SharePoint admin center, see [Get started with the new SharePoint admin center](get-started-new-admin-center.md).
  
## Create a site
<a name="createsite"> </a>

You as a SharePoint or global admin in your organization can create new sites from the admin center in the same way that you can allow your users to create sites.
  
1. Click **Create site**.
    
2. Select to create a team site (which will create an Office 365 group), a communication site, or a classic site. For info about the new site templates, see [Create a team site in SharePoint Online](https://support.office.com/article/ef10c1e7-15f3-42a3-98aa-b5972711777d) and [Create a communication site in SharePoint Online](https://support.office.com/article/7fb44b20-a72f-4d2c-9173-fc8f59ba50eb).
    
    ![Create a communication site, team site, or classic site from the admin center](media/c4c5173f-ca83-426f-a940-cb2869a3a64b.png)
  
## Delete a site
<a name="deletesite"> </a>

On the Site management page, you can delete the communication sites you created, as well as all classic sites. (To delete sites that belong to an Office 365 group, you need to delete all the group resources by going to the Office 365 admin center and deleting the group.)
  
1. In the left column, click to select a site.
    
2. Click **Delete**, and then click **Delete** to confirm. 
    
You can recover deleted sites for 93 days. For more info, see [View and restore deleted sites](view-and-restore-deleted-sites-in-new-admin-center.md).
  
## Add or remove admins
<a name="addremoveadmins"> </a>

For all sites except those managed by Office 365 group owners, you can change the primary admin and add or remove additional admins.
  
1. Click the site name to open the details pane.
    
2. Under **Properties**, click **Change primary admin** or **Add or remove admins**.
    
    ![Change the primary admin or add or remove other admins in the details pane](media/690948e4-109e-4398-b9ca-963c92e21450.PNG)
  
## Email admins
<a name="emailadmins"> </a>

On the Site management page, you can email the primary admins of the sites you select.
  
1. In the left column, click to select one or more sites.
    
    > [!NOTE]
    >  You can email the primary admins for all sites except those that belong to an Office 365 group. If you want to email several owners at one time, sort or filter columns to exclude sites that belong to an Office 365 group before you make your selection. >  Users who are the primary admin for more than one site will receive an email for each site. 
  
2. Click **Email admins**.
    
3. Enter a subject and add a message, and then click **Send**.
    
    ![Email admins dialog box](media/28ecaf36-9e47-4757-8c12-8bbbc0c33daf.PNG)
  
## Change the external sharing setting for the site
<a name="changesitesharing"> </a>

On the Site management page, you can change the external sharing setting for any site.
  
1. Click the site name to open the details pane.
    
2. Under **Properties**, next to **Sharing status**, click **Change**.
    
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
    
- The amount of storage used
    
> [!NOTE]
> All these insights are available as columns in the site management list. For info about adding a column that doesn't appear, see [Customize columns](manage-sites-in-new-admin-center.md#customizecolumns). 
  
![Site properties in the details pane](media/addeb5ec-cfc7-4d0c-a789-7eeeabdea67c.PNG)
  
Site properties in the details pane:
  
- The domain
    
- A link to the site
    
- The site template (also available as a column in the site management list)
    
- Whether the site belongs to an Office 365 group (also available as a column in the site management list)
    
- The site description if specified
    
- The primary admin (also available as a column in the site management list) and additional admins, with links to change the admins. If a site belongs to an Office 365 group, you can change the admins by changing the group owners. For info, see [Add or remove members from Office 365 groups using the Office 365 admin center](https://support.office.com/article/e186d224-a324-4afa-8300-0e4fc0c3000a).
    
- The external sharing status (also available as a column in the site management list)
    
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
  
## Export to CSV
<a name="export"> </a>

To export your list of all sites as a .csv file that you can work with in Excel, click **Export to CSV**.
  
> [!NOTE]
> The Export to CSV command exports all sites and includes all columns, even if your current view is filtered. 
  
## Customize columns
<a name="customizecolumns"> </a>

1. Click the arrow next to any column header, and then select **Customize columns**.
    
2. Select and clear check boxes to show and hide columns.
    
3. Rearrange the columns by pointing to a column and clicking the up or down arrow to move the column up or down.
    
    ![Show, hide, and rearrange columns on the Site management page](media/d713dbd8-2ac7-428c-a5b9-b5bd673ce674.PNG)
  
## Switch views and create custom views
<a name="views"> </a>

The new SharePoint admin center (preview) comes with a few built-in views: Largest, Least active, and Most popular shared. You can also create and save custom views.
  
1. Customize columns, sort, and filter your view the way you want. (Views that are filtered through search can't be saved.)
    
2. On the far right of the command bar, next to the Search box, click the View drop-down (the name changes depending on your current view).
    
3. Click **Save view as**.
    
4. In the **Save as** dialog box, enter a name for the view. 
    
    > [!NOTE]
    > To set the view as default, in the View drop-down, click **Set current view as default**. 
  

