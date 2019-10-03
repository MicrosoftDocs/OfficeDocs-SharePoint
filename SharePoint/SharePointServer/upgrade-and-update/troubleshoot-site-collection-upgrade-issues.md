---
title: "Troubleshoot site collection upgrade issues in SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/30/2016
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 75113d71-7193-44ab-b79b-34cb9cf9aa94
description: "Learn how to address problems that may occur after you upgrade a site to SharePoint Server 2016."
---

# Troubleshoot site collection upgrade issues in SharePoint Server 2016


  
When you upgrade a site collection to SharePoint Server 2016, errors can occasionally occur. This article helps you understand those errors and address them.
  
## Check upgrade status and log files

Upgrade status indicators and log files should give you an indication of what went wrong during the upgrade process. We recommend that you carefully review all the errors in the upgrade log files. Warnings might not always indicate an issue, but you should review them all to determine whether any of them are likely to cause even more issues.
  
1. Review the upgrade status page for your site collection.
    
    On the **Site Settings** page for the site collection, in the **Site Collection Administration** section, click **Site collection upgrade**. On the **Site Collection Upgrade** page, click **Review Site Collection Upgrade Status**.
    
2. If pages don't render, check the **Site Settings** page. If the **Site Settings** page works and the upgrade has succeeded, there might be issues with the master page or home page. If the **Site Settings** page doesn't work, check the site collection upgrade log file for information about the problem. 
    
3. Review the site collection upgrade log files. You can review the site collection upgrade logs from the following locations:
    
  - **For site collection administrators:** There are also log files for site collection upgrade stored inside the site collection itself, in the Maintenance Logs catalog at (http://<SiteName>/_catalogs/MaintenanceLogs/YYYYMMDD-HHMMSS-SSS.txt , where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). 
    
  - **For farm administrators:** The site collection upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\16\LOGS. The logs are named in the following format: SiteUpgrade-  _YYYYMMDD-HHMMSS-SSS_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). These file system logs have more information if you want details about issues. 
    
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
    
This error indicates that a third-party content type was added to the specified site in SharePoint Server 2013 with Service Pack 1 (SP1). During upgrade to SharePoint Server 2016 its name conflicted with the default content type by the same name. Rename the third-party content type in the specified site to a different name and run upgrade again. For more information, see [Create or customize a site content type](https://support.office.com/article/27eb6551-9867-4201-a819-620c5658a60f). 
  
> [!NOTE]
> Either renaming or removing a content type can cause any customizations dependent on that content type to stop working. 
  
### Q: My site looks ugly, doesn't behave as expected, or I see script errors
<a name="UI"> </a>

- **A:** Either edit the page or reset the page to the default version, or remove or replace the custom files. 
    
    A problem with custom or inline JavaScript or CSS files can cause these issues. 
    
### Q: Custom content in my site disappeared or doesn't work
<a name="UI"> </a>

- **A:** Change the master page, or change the content so that it doesn't require specific zones. 
    
    The master page might have different zone layouts and the content might no longer reference it correctly. As a last resort, you can also reset the page to the default version. However, if you reset the page, you might lose zone specific content. 
    
### Q: I receive an error that says a control or page cannot render
<a name="UI"> </a>

- **A:** Do one of the following: 
    
  - If a Web Part was added that is not installed, contact the farm administrator to have it installed. If is a Web Part that is no longer available or not supported, then use the Web Part maintenance view to remove the Web Part from the page (remove, do not just close the Web Part).
    
  - If a page was directly edited, either edit it again to remove the control or Web Part or reset the page to the default version.
    
    A Web Part or other control might have been added to the page that is not installed or is no longer supported. Either a Web Part was added to a zone or the page was directly edited to add a control or Web Part reference directly inline (possibly on a master page).
    
    A SharePoint feature may need to be activated. For more information, see [Enable or disable site collection features](https://support.office.com/article/a2f2a5c2-093d-4897-8b7f-37f86d83df04) and [Open and use the Web Part Maintenance Page](https://support.office.com/article/eff9ce22-d04a-44dd-ae83-ac29a5e396c2). 
    
### Q: My upgraded site does not render at all; instead, I see an "unexpected error" with a correlation ID
<a name="UI"> </a>

 **A:** Your custom branding may use a custom master page that contains a custom content placeholder. 
  
If your custom master page contains a custom content placeholder, and if custom page layouts also contain this custom content placeholder, then an error may prevent the home page of your site from rendering at all after upgrade. Instead, after upgrade, you may see the error message "An unexpected error has occurred."
  
## See also

#### Concepts

[Upgrade a site collection to SharePoint Server 2016](upgrade-a-site-collection.md)

