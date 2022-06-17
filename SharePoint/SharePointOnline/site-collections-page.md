---
title: "Find site collection features in the new SharePoint admin center"
ms.reviewer: kaarins
manager: serdars
recommendations: true
ms.author: mikeplum
author: MikePlumleyMSFT
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ROBOTS: NOINDEX
description: "In this article, you'll learn about finding site collection features in the new SharePoint admin center."
---

# Find site collection features in the new SharePoint admin center

This article covers all the features on the classic site collections page and where you can find them in the new <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>.

![Ribbon on site collections page](media/site-collections-menu.png)

> [!IMPORTANT]
> The classic site collections page has been removed. This article shows the features that were present on the classic site collections page and where to find them in the new SharePoint admin center.

## New (create a new private site collection)

To create a site collection in the new SharePoint admin center, go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites**</a>, and then select **Create**. To create a classic site, select **Other options**.

<br/>

|Classic|New|
|:-----|:-----|
|![New private site collection](media/new-private-site-collection.png)|![Classic other options](media/classic-other-options.png)|

<br/>

|Classic|New|
|:-----|:-----|
|Title|Site name|
|Change the URL path to /sites/ or /teams/|Site address boxes appear after you begin entering a site name.|
|Web Site Address|Site address boxes appear after you begin entering a site name. The name is entered by default as the address. To change it, select the Edit icon.|
|Select a language|Select a language|
|Select a template: </br>**Community**: Team site (classic experience), Blog, Developer site, Project Site, Community Site</br>**Enterprise**: Document Center, eDiscovery Center, Records Center, Team Site – SharePoint Online configuration, Business Intelligence Center, Compliance Policy Center, My Site Host, Community Portal, Basic Search Center, Visio Process Repository</br>**Publishing**: Publishing Portal, Enterprise Wiki, Product Catalog </br>**Custom**: \<Select template later...>|In the **Choose a template** box, you can select **Document Center**, **Enterprise Wiki**, or **Publishing Portal**. To select the others, select **More templates**. This opens the classic Create Site Collection window.|
|Time Zone|Expand **Advanced settings** and select **Time zone**.|
|Administrator|Primary Administrator|
|Server Resource Quota|This setting has had no effect for more than a year.|
|Private Site Collection with Project Web App|Create a site and then use the [PowerShell cmdlet Set-SPOSite -EnablePWA](/powershell/module/sharepoint-online/set-sposite) to add or remove Project Web App.|

## Delete

On the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>, select the site, and on the command bar, select **Delete**. As with the classic SharePoint admin center, you can't delete the root (top-level) site. To swap this site with a different site, see [Replace your root site](./modern-root-site.md).

## Properties

The columns on the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a> show most of this information, so you don't even need to select a site to see details. To see the properties for an individual site, select anywhere in the site row, except in the URL column.

<br/>

|Classic|New|
|:-----|:-----|
|![Site collections properties](media/site-collection-properties.png)|![Communication site](media/communication-site.png)|

<br/>

|Classic|New|
|:-----|:-----|
|Title|Site name column|
|Complete Web Site Address link|URL column shows the path after the domain. You can copy the link to save the full URL to the Clipboard.|
|Primary Administrator|Primary admin column.|
|Other Administrators|For any sites that aren't connected to a Microsoft 365 group, select the site, and on the command bar, select **Permissions**, and then select **Manage admins**. (For group-connected sites, you have options for managing group owners and additional admins.)|
|Number of subsites|Not available|
|Storage Usage|Storage used (GB) column.|
|Resource Usage, Server Resource Quota, Resource Usage Warning Level|These settings have had no effect for more than a year.|

## Owners

To change the owners for any site that isn't connected to a Microsoft 365 group, go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>, select the site, select **Permissions** on the command bar, and then select **Manage admins**.

<br/>

|Classic|New|
|:-----|:-----|
|![Manage administrators](media/manage-administrators.png)|![Manage admins](media/manage-admins.png)|

<br/><br/>

|Classic|New|
|:-----|:-----|
|Primary Site Collection Administrator|Switch the role of an existing admin to Primary Admin, or add an admin and then switch them to Primary admin.|
|Site Collection Administrators|Use the Add an admin box to add an admin and the Remove button to remove an admin.|
|Add Support Partner|This option is available in PowerShell only. Go to the Site Permissions page for a site where you've added the support partner. Copy the encoded string for the partner, and to add it to other sites, use the [PowerShell cmdlet Set-SPOUser](/powershell/module/sharepoint-online/set-spouser?view=sharepoint-ps&preserve-view=true).|

## Sharing

To change sharing settings for a site, go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>, select the site, and select **Sharing** on the command bar.

<br/>

|Classic|New|
|:-----|:-----|
|![Sharing classic](media/sharing-classic.png)|![Sharing modern](media/sharing-modern.png)|

<br/>

|Classic|New|
|:-----|:-----|
|Sharing outside your company|External sharing <br/> - "Don't allow sharing outside your organization" is the same as "Only people in your organization." <br/> - "Allow sharing only with the external users that already exist in your organization's directory" is the same as "Existing guests only." <br/> - "Allow external users who accept sharing invitations and sign in as authenticated users" is the same as "New and existing guests." <br/> - "Allow sharing with all external users, and by using anonymous access links" is the same as "Anyone." <br/>|
|Default link type|Default sharing link type <br/> - "Respect default organization setting" is the same as "Same as organization-level setting."  <br/> - "Direct" is the same as "Specific people." <br/> - "Internal" is the same as "Only people in your organization." <br/> - "Anonymous Access" is the same as "Anyone with the link." <br/>|
|Default link permission|"Respect default organization setting" is the same as "Same as organization-level setting." Both the classic and new admin centers have View and Edit options.  <br/>|
|Limit external sharing by domain <br/>|Under **Advanced settings for external sharing**, select **Limit sharing by domain**. <br/>|
|Turn off sharing for all non-owners on all sites in the site collection <br/>|This option is available in PowerShell only. Use the cmdlet [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) -DisableSharingForNonOwners <br/>|

## Storage quota

These options appear if you use manual site storage limits in your organization. To change the storage limit for a site, go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>, select the site, and select **Storage** on the command bar.

<br/>

|Classic|New|
|:-----|:-----|
|![Set storage quota](media/set-storage-quota.png)|![Edit storage limit](media/edit-storage-limit.png)|

<br/>

|Classic|New|
|:-----|:-----|
|Limit storage quota for each selected site collection to a maximum of|Maximum storage for this site <br/>|
|Send e-mail to site collection administrators when a site collection's storage reaches|Allow notifications|

## Buy storage

In the Microsoft 365 admin center, go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=868433" target="_blank">**Purchase services** page</a>. For more information, see [Add storage space for your subscription](/microsoft-365/commerce/add-storage-space).

## Server resource quota

These settings have had no effect for more than a year. 

## Upgrade settings and notifications

These features haven't been in use for more than a year.

## Project Web App

![Project Web App](media/project-web-app.png)

<br/>

|Classic|New|
|:-----|:-----|
|Add or remove<br/>|These commands are available in PowerShell only. Use the cmdlet [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) -EnablePWA<br/>|
|Settings (SharePoint Permission Mode or Project Permission Mode) and Project Web App Size <br/>|To change the permission mode, go to the site as the Project Web App Administrator and follow the steps in [Change permission management in Project Online](/projectonline/change-permission-management-in-project-online). You can review the size of the Project Web App site using the above instructions where it is located on the same page under the section "Project Web App Usage". <br/>|

## Recycle bin

To view your deleted sites, go to the new SharePoint admin center, go to <a href="https://go.microsoft.com/fwlink/?linkid=2185070" target="_blank">**Deleted sites**</a>.

<br/>

|Classic|New|
|:-----|:-----|
|![Recycle bin](media/recycle-bin.png)|![Deleted sites](media/deleted-sites.png)|

<br/>

|Classic|New|
|:-----|:-----|
|Restore Deleted Items|Select the site, and on the command bar, select **Restore**.  <br/>|
|Deleted (date)|Time deleted column.|
|Days remaining  <br/>|This info is incorrect in the classic admin center. To calculate this value in the new SharePoint admin center, use the Time deleted column. <br/>|

## Search by URL

On the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>, use the Search box. As with the classic SharePoint admin center, you can also sort by URL.

## Available storage and storage limit bar

The upper-right corner of the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a> shows the storage used (in GB) and storage limit for your organization.

## Available resources bar

Server resource quota and availability have had no effect for more than a year. 

## Project Web App instances available

This information is no longer displayed because you shouldn't need to worry about running out of Project Web App instances.

## Site list

![Storage columns](media/storage-columns.png)

Most of the sites that were listed in the classic SharePoint admin center are included on the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>. A few are hidden because they're system sites that you shouldn't need to change. The Active sites page contains all the new team sites and communication sites that didn't appear in the classic SharePoint admin center. To see the site list as it appeared in the classic SharePoint admin center, from the **Built-in views** menu, select **Classic sites**.  

In both the classic and new admin centers, you can select multiple sites and bulk edit the sharing or storage settings, or delete the sites.  

In the classic site list, locked sites appeared with an icon. In the new SharePoint admin center, to see if a site is locked, select the site to open the details panel. **This site is locked** appears at the top of the panel. 

If you use manual storage limits, the Storage limit and Percent used columns appear. In the new SharePoint admin center, the Storage limit and Storage used columns appear. The Storage used column isn't color coded. The Storage limit column can be sorted by size.
