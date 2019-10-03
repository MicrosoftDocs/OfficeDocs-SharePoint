---
title: "Upgrade a site collection to SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 78e2f208-e4b9-49cd-a036-89809fa24baf
description: "Learn how site collection administrators can upgrade their sites to SharePoint Server 2016 and then review site collections for issues."
---

# Upgrade a site collection to SharePoint Server 2016


  
In SharePoint Server 2016 the way site collection upgrades are performed has changed. After a server farm administrator has upgraded the databases, site collections are automatically upgraded.
  
> [!NOTE]
> There is no concept of "site collection compatibility modes" in SharePoint Server 2016. You must be running the latest version at all times. 
  
## Upgrade a site collection

SharePoint Server 2016 introduces a new site collection upgrade experience. There are three ways to upgrade a site collection: 
  
- In conjunction with content databases upgrade
    
- On-browse upgrade
    
- Manually triggered by using PowerShell.
    
 **Content databases upgrade**-  To upgrade the databases run the [Mount-SPContentDatabase](/powershell/module/sharepoint-server/Mount-SPContentDatabase?view=sharepoint-ps) cmdlet. After the databases have been upgraded the site collections are automatically upgraded during database upgrade process by default. 
  
> [!NOTE]
> This is the default behavior and recommended method to upgrade databases. 
  
> [!IMPORTANT]
> If you want to delay the sites upgrade, use the **SkipSiteUpgrade** parameter of the [Mount-SPContentDatabase](/powershell/module/sharepoint-server/Mount-SPContentDatabase?view=sharepoint-ps) cmdlet. > When the parameter is provided, the site collection is upgraded when first browsed. 
  
 **On-browse upgrade** - You do not need to know whether the site collection has pending upgrade, SharePoint decides it for you during the upgrade process. Once the site is browsed, SharePoint checks if the site needs to be upgraded, if so, the site will be put in a queue and a timer job will pick it up for upgrade. 
  
Farm administrators can use PowerShell to upgrade a site collection.
  
 **Manually trigger site upgrade** - You can use the [Upgrade-SPSite](/powershell/module/sharepoint-server/Upgrade-SPSite?view=sharepoint-ps) cmdlet to manually upgrade the site collections. 
  
> [!NOTE]
> This is a legacy option to upgrade a site collection. 
  
This option is ideal for databases with large number of sites and for customers who use only a subset of all their sites.
  
## Verify that site collection upgrade has succeeded
<a name="ver"> </a>

Site collection administrators can view the **Upgrade Status** page in Site Settings to verify that upgrade has succeeded for a site collection. 
  
 **To view upgrade status in Site Settings**
  
1. Verify that the user account that performs this procedure is a site collection administrator.
    
2. On the **Site Settings** page for the site collection, in the **Site Collection Administration** section, click **Site collection upgrade**.
    
3. On the **Site Collection Upgrade** page, click **Review Site Collection Upgrade Status**.
    
    The **Upgrade Status** page for the site collection is displayed. 
    
Farm administrators can use PowerShell to view site collection upgrade status.
  
## Review site collections upgraded to SharePoint Server 2016
<a name="ver"> </a>

After the site collections have been upgraded to SharePoint Server 2016, review your upgraded sites to fix any issues after you have upgraded a site collection. Use the steps in this section to identify any issues before you upgrade your production environment. 
  
When you perform tests before upgrading your environment:
  
- Begin by validating high-impact or high-profile sites, and then move on to lower-priority sites. As part of the planning process, you should have identified which sites are high-impact and high-profile and require immediate attention, and which can wait a bit longer.
    
- To verify basic functionality, create a new site collection by using a representative set of lists, libraries, Web Parts, and so on. Review the new site to make sure that the common, basic elements of your sites are working.
    
- If pages do not render, you can check the **Site Settings** page by going directly to the URL (http://  _siteurl_/_layouts/settings.aspx). If the **Site Settings** page works and the upgrade has succeeded, there might be issues with the master page or home page. If the **Site Settings** page does not work, go to the site collection upgrade log file to see whether you can get more information about the problem. 
    
You can review the site collection upgrade logs from the following locations:
  
- **For site collection administrators:** If site collections are upgraded by using the [Mount-SPContentDatabase](/powershell/module/sharepoint-server/Mount-SPContentDatabase?view=sharepoint-ps) cmdlet, there are no separate SiteUpgrade*.log files. The SiteUpgrade logs are inside Upgrade*.log files. 
    
    > [!NOTE]
    > You can retrieve the log files by using PowerShell . > From a PowerShell command prompt type the following syntax:  `Get-SPSiteUpgradeSessionInfo -Site <siteUrl> OR $site.UpgradeInfo`
  
- **For farm administrators:** The site collection upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\16\LOGS. The logs are named in the following format: SiteUpgrade-  _YYYYMMDD-HHMMSS-SSS_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). These file system logs have more information if you want details about issues. 
    
    For additional information on how to troubleshoot error messages, see [Troubleshoot site collection upgrade issues in SharePoint Server 2016](troubleshoot-site-collection-upgrade-issues.md).
    
Use the following checklists to review your upgraded sites and look for issues for either trial upgrades or upgrades in a production environment.
  
## Checklists for reviewing upgraded sites
<a name="Review"> </a>

### Large lists

By default, large list query throttling is turned on in SharePoint Server 2016. If a list is very large, and users use a view or perform a query that exceeds the limit or throttling threshold, the view or query will not be permitted. Check any large lists in your environment and have the site administrator or list owner address the issue. For example, they can create indexed columns with filtered views, organize items into folders, set an item limit on the page for a large view, or use an external list. For more information about large list throttling and how to address issues with large lists, see [Manage lists and libraries with many items](https://go.microsoft.com/fwlink/p/?LinkId=251456). 
  
### Styles and appearance

The following table lists common issues with the style and appearance of your web site after upgrade and how to address them.
  
> [!TIP]
> Most of the issues in this section can be resolved by correcting the links to an item. 
  
|**What to check**|**What to do if there is a problem**|
|:-----|:-----|
|Are all the images on your pages displayed correctly?  <br/> |Verify or fix the links to the images.  <br/> |
|Are the appropriate cascading style sheet colors and styles used in the appropriate locations?  <br/> |Verify or fix the links to the cascading style sheet file. Verify the link on the master page.  <br/> |
|Theme choices are different in SharePoint 2016 - which theme do you want to use?  <br/> |Your site's home page, or other pages on your site, may look different after the site is upgraded. You may have to re-create or revise a theme and reapply it.  <br/> |
|Do you have any JavaScript controls that are not working?  <br/> |Verify or fix the links to the controls.  <br/> |
|Are your pages displayed correctly in the browser?  <br/> |Verify that any HTML on the page is in strict XHTML mode.  <br/> |
|Are any script errors displayed on any pages?  <br/> |Verify the scripts and links, and verify that any HTML is in strict XHTML mode.  <br/> |
   
## See also
<a name="Review"> </a>

#### Concepts

[Overview of the upgrade process to SharePoint Server 2016](overview-of-the-upgrade-process.md)

