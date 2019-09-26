---
title: "Troubleshoot site collection upgrade issues in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: eb76be2d-d053-4b3d-b2fc-fa97ed048a21
description: "Learn how to address problems that may occur after you upgrade a site to SharePoint 2013."
---

# Troubleshoot site collection upgrade issues in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
When you upgrade a site collection to SharePoint 2013, errors can occasionally occur. This article helps you understand those errors and address them.
  
For more information about how to review UI issues in sites, see [Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md).
  
## Check upgrade status and log files

Upgrade status indicators and log files should give you an indication of what went wrong during the upgrade process. We recommend that you carefully review all the errors in the upgrade log files. Warnings might not always indicate an issue, but you should review them all to determine whether any of them are likely to cause even more issues.
  
1. Review the upgrade status page for your site collection.
    
    On the **Site Settings** page for the site collection, in the **Site Collection Administration** section, click **Site collection upgrade**. On the **Site Collection Upgrade** page, click **Review Site Collection Upgrade Status**.
    
2. If pages don't render, check the **Site Settings** page. If the **Site Settings** page works and the upgrade has succeeded, there might be issues with the master page or home page. If the **Site Settings** page doesn't work, check the site collection upgrade log file for information about the problem. 
    
3. Review the site collection upgrade log files. You can review the site collection upgrade logs from the following locations:
    
  - **For site collection administrators:** There are also log files for site collection upgrade stored inside the site collection itself, in the Maintenance Logs catalog at (http://<SiteName>/_catalogs/MaintenanceLogs/YYYYMMDD-HHMMSS-SSS.txt , where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). 
    
  - **For farm administrators:** The site collection upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\15\LOGS. The logs are named in the following format: SiteUpgrade-  _YYYYMMDD-HHMMSS-SSS_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). These file system logs have more information if you want details about issues. 
    
## Common issues

Check to see whether any of the following issues are causing an upgrade error, a warning, or a problem in your site.
  
### Q: I don't see a UI control on the page that used to be there
<a name="UI"> </a>

- **A:** Reset the page to the default version (that is, reghost it). 
    
Making changes to the site UI can cause problems in site upgrades. If a page was customized to place a UI control in a non-standard location, you can reset the page to the default version to recover the control.
  
To reset the page, you can use the **Reset to site definition** link under **Site Actions** on the Site Settings page or use the **Reset to Template** command in SharePoint Designer. 
  
### Q: The view on a large list is not working any longer
<a name="UI"> </a>

- **A:** Create indexed columns, folders, or new views for large lists. You might have to add the indexed column to your existing views. 
    
If a list is very large, and users use a view or perform a query that exceeds the limit or throttling threshold, the view or query will not be permitted. You can create indexed columns with filtered views, organize items into folders, set an item limit on the page for a large view, or use an external list. For more information about large list throttling and how to address issues with large lists, see [Manage lists and libraries with many items](https://go.microsoft.com/fwlink/p/?LinkId=251456). 
  
### Q: I see an error about a duplicate content type name
<a name="UI"> </a>

- **A:** Rename content types or fields that conflict with default names. 
    
Occasionally, custom elements (such as a content type) may have a name that conflicts with a name in the new version. 
  
In the upgrade log files, you may see an error such as the following:
  
- Failed to activate site collection features on site Site Url. Exception: A duplicate content type name  _"name"_ was found. 
    
This error indicates that a third-party content type was added to the specified site in SharePoint Server 2010. During upgrade to SharePoint 2013 its name conflicted with the default content type by the same name. Rename the third-party content type in the specified site to a different name and run upgrade again. For more information, see [Create or customize a content type](http://office.microsoft.com/en-us/office365-sharepoint-online-enterprise-help/create-or-customize-a-content-type-HA102773269.aspx?CTT=5&amp;origin=HA103591373). 
  
> [!NOTE]
> Either renaming or removing a content type can cause any customizations dependent on that content type to stop working. 
  
### Q: My site looks ugly, doesn't behave as expected, or I see script errors
<a name="UI"> </a>

- **A:** Either edit the page or reset the page to the default version, or remove or replace the custom files. 
    
    A problem with custom or inline JavaScript or CSS files can cause these issues. For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).
    
### Q: Custom content in my site disappeared or doesn't work
<a name="UI"> </a>

- **A:** Change the master page, or change the content so that it doesn't require specific zones. 
    
    The master page might have different zone layouts and the content might no longer reference it correctly. As a last resort, you can also reset the page to the default version. However, if you reset the page, you might lose zone specific content. For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).
    
### Q: I receive an error that says a control or page cannot render
<a name="UI"> </a>

- **A:** Do one of the following: 
    
  - If a Web Part was added that is not installed, contact the farm administrator to have it installed. If is a Web Part that is no longer available or not supported, then use the Web Part maintenance view to remove the Web Part from the page (remove, do not just close the Web Part).
    
  - If a page was directly edited, either edit it again to remove the control or Web Part or reset the page to the default version.
    
    A Web Part or other control might have been added to the page that is not installed or is no longer supported. Either a Web Part was added to a zone or the page was directly edited to add a control or Web Part reference directly inline (possibly on a master page).
    
    A SharePoint feature may need to be activated. For more information, see [Enable or disable site collection features](https://office.microsoft.com/en-us/office365-sharepoint-online-enterprise-help/enable-or-disable-site-collection-features-HA102772720.aspx?CTT=1) and [Open and use the Web Part Maintenance Page](https://office.microsoft.com/en-us/sharepoint-help/open-and-use-the-web-part-maintenance-page-HA104046809.aspx?CTT=1). 
    
### Q: I receive an error that I cannot create a subsite based on a site template because the site template uses the 2010 experience version and my site collection is in the 2013 experience version
<a name="UI"> </a>

- **A:** Recreate the site template in the 2013 experience. 
    
    To recreate the site template, create a new subsite based on the 2013 experience, customize it again to match the template that you had, and then save the customized subsite as a template (on the **Site Settings** page, click **Save site as template**).
    
### Q: I receive an error when I try to upgrade a FAST Search Center site to the 2013 experience
<a name="UI"> </a>

- **A:** Recreate the site by using the Enterprise Search Center template. 
    
    FAST Search Center sites cannot be upgraded to the 2013 experience. Existing FAST Search Center sites can continue to work in 2010 mode after upgrade. If you want the new functionality, you must create new Enterprise Search Center sites in 2013 mode.
    
### Q: My custom branding doesn't look right or there are issues in my upgraded site
<a name="UI"> </a>

 **A:** Create an evaluation site collection, and then re-create the master page in the SharePoint 2013 site. 
  
To support the new faster, more fluid UI in SharePoint 2013, changes have been made to the default master pages and CSS files. For this reason, you cannot apply a master page created in SharePoint 2010 to a site in SharePoint 2013. However, when you upgrade your SharePoint 2010 site to SharePoint 2013, the master page is reset to use the default master page in SharePoint 2013. Therefore, after upgrade, your site will not appear with its custom branding. 
  
To resolve this, you should first create an evaluation site collection, and then re-create the master page in the SharePoint 2013 site. For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).
  
### Q: My upgraded site does not render at all; instead, I see an "unexpected error" with a correlation ID
<a name="UI"> </a>

 **A:** Your custom branding may use a custom master page that contains a custom content placeholder. 
  
If your custom master page contains a custom content placeholder, and if custom page layouts also contain this custom content placeholder, then an error may prevent the home page of your site from rendering at all after upgrade. Instead, after upgrade, you may see the error message "An unexpected error has occurred." For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).
  
## See also

#### Other Resources

[Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md)
  
[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)
  
[Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14))

