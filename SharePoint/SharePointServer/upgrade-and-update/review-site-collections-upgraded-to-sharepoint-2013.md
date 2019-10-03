---
title: "Review site collections upgraded to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e23aa6ff-e48d-44f0-a6ab-ca47da171dc0
description: "Learn what to look for when you review site collections after you upgrade to SharePoint 2013 and find tips to address issues."
---

# Review site collections upgraded to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Use these steps in your test environment to identify any issues before you upgrade your production environment. And review your upgraded sites to fix any issues after you have upgraded a site collection. 
  
When you perform tests before upgrading your environment:
  
- Begin by validating high-impact or high-profile sites, and then move on to lower-priority sites. As part of the planning process, you should have identified which sites are high-impact and high-profile and require immediate attention, and which can wait a bit longer.
    
- To verify basic functionality, create a new site collection by using a representative set of lists, libraries, Web Parts, and so on. Review the new site to make sure that the common, basic elements of your sites are working.
    
- If pages do not render, you can check the **Site Settings** page by going directly to the URL (http://  _siteurl_/_layouts/settings.aspx). If the **Site Settings** page works and the upgrade has succeeded, there might be issues with the master page or home page. If the **Site Settings** page does not work, go to the site collection upgrade log file to see whether you can get more information about the problem. 
    
You can review the site collection upgrade logs from the following locations:
  
- **For site collection administrators:** There are also log files for site collection upgrade stored inside the site collection itself, in the Maintenance Logs catalog at (http://<SiteName>/_catalogs/MaintenanceLogs/YYYYMMDD-HHMMSS-SSS.txt , where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). 
    
- **For farm administrators:** The site collection upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\15\LOGS. The logs are named in the following format: SiteUpgrade-  _YYYYMMDD-HHMMSS-SSS_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). These file system logs have more information if you want details about issues. 
    
Use the following checklists to review your upgraded sites and look for issues for either trial upgrades or upgrades in a production environment.
  
## Checklists for reviewing upgraded sites
<a name="Review"> </a>

### Web Parts

The following table lists issues with Web Parts that can occur after upgrade and how to address them.
  
> [!TIP]
> To test your Web Parts quickly, you can build a new Web Part page that contains all the custom Web Parts before you test an upgrade, and then review the page for any missing or broken Web Parts after the trial upgrade. 
  
|**What to check**|**What to do if there is a problem**|
|:-----|:-----|
|Do all the Web Parts from your original site appear in your upgraded site?  <br/> |If a Web Part zone exists in a customized (unghosted) page, but not in the site definition, the Web Parts from that Web Part zone may have been moved into the bottom zone on the page during the upgrade.  <br/> Either in Edit Mode for the page in the browser or in SharePoint Designer 2013, look for missing Web Parts in the bottom zone or other zones, or check whether the Web Parts were closed. For more information about how to work with Web Parts and Web Part zones in SharePoint Designer 2013, see the SharePoint Designer Help system.  <br/> |
|Are there any broken Web Parts pages and are the Web Parts displayed correctly (in the correct zone, location, and size)?  <br/> |Either in Edit Mode for the page in the browser or in SharePoint Designer 2013, drag the Web Part into the correct zone or modify the Web Part properties to correct any sizing or positioning problems.  <br/> |
|Are there any extra or missing Web Parts?  <br/> |Open the page either in Edit Mode for the page in the browser or in SharePoint Designer 2013. If you see additional Web Parts on your page, look for closed or inactive Web Parts on the original version of the page. Were the closed or inactive Web Parts opened by the upgrade process? If so, you can modify the Web Part properties to close these Web Parts.  <br/> If Web Parts are missing, look for errors in SharePoint Designer 2013 such as "Error Rendering Control" or "Missing Assembly." These errors indicate that the Web Part was not installed or was configured incorrectly for the new environment and must be reinstalled or reconfigured.  <br/> |
|Do the Web Parts work correctly?  <br/> |Open the page either in Edit Mode for the page in the browser or in SharePoint Designer 2013, and look for errors that indicate that a component or service is missing. Make sure that any components or services that the Web Parts rely on exist in the upgraded site. Particularly for the database attach upgrade approach, you must make sure that you have installed all the components or services that you must have for your Web Parts, and that you have configured them correctly (for example, you have configured the Web.config Safe Controls list).  <br/> Update and redeploy any Web Parts that exist but no longer function correctly.  <br/> |
|Are any Web Parts pages still checked out?  <br/> |If you check out a page to make changes, make sure that you check in the page again.  <br/> |
|Are your Excel Web Access Web Parts working correctly? Did you create your connections again correctly? Are external data sources still working?  <br/> |Verify all connections and external data sources.  <br/> |
   
> [!TIP]
> If you have problems with a Web Part, append **?contents=1** to the end of the URL syntax (http://  _siteurl_/default.aspx? **contents=1** ), and then press ENTER. This opens the Web Part Maintenance page where you can remove and repair the broken Web Part. 
  
### Large lists

By default, large list query throttling is turned on in SharePoint 2013. If a list is very large, and users use a view or perform a query that exceeds the limit or throttling threshold, the view or query will not be permitted. Check any large lists in your environment and have the site administrator or list owner address the issue. For example, they can create indexed columns with filtered views, organize items into folders, set an item limit on the page for a large view, or use an external list. For more information about large list throttling and how to address issues with large lists, see [Manage lists and libraries with many items](https://go.microsoft.com/fwlink/p/?LinkId=251456). 
  
### Styles and appearance

The following table lists common issues with the style and appearance of your web site after upgrade and how to address them.
  
> [!TIP]
> Most of the issues in this section can be resolved by correcting the links to an item. 
  
|**What to check**|**What to do if there is a problem**|
|:-----|:-----|
|Are all the images on your pages displayed correctly?  <br/> |Verify or fix the links to the images.  <br/> |
|Are the appropriate cascading style sheet colors and styles used in the appropriate locations?  <br/> |Verify or fix the links to the cascading style sheet file. Verify the link on the master page.  <br/> |
|Theme choices are different in SharePoint 2013 - which theme do you want to use?  <br/> |Your site's home page, or other pages on your site, may look different after the site is upgraded. You may have to re-create or revise a theme and reapply it.  <br/> |
|Do you have any JavaScript controls that are not working?  <br/> |Verify or fix the links to the controls.  <br/> |
|Are your pages displayed correctly in the browser?  <br/> |Verify that any HTML on the page is in strict XHTML mode.  <br/> |
|Are any script errors displayed on any pages?  <br/> |Verify the scripts and links, and verify that any HTML is in strict XHTML mode.  <br/> |
   
### Customized (unghosted) pages

Customized (also known as unghosted) pages are pages that were edited and are now unique versions of the pages for the site, instead of the default template pages. The following table lists issues with customized pages that can occur after upgrade and how to address them.
  
|**What to check**|**What to do if there is a problem**|
|:-----|:-----|
|Are your customizations still in place?  <br/> |Determine whether you have only one issue or a larger problem with the whole page.  <br/> If you added a brand-new page to your original site (for example, if you replaced Default.aspx with a different file instead of changing the existing Default.aspx file), the new page has no association with the site definition. Therefore, it might not resemble the other pages on the upgraded site — nor can it be reset to resemble them. If you want your customized page to have the same appearance and behavior as the other pages on your site, consider creating a brand-new page that is based on the site definition and then transferring your customizations to that new page.  <br/> |
|Can you still access the editing controls on the pages?  <br/> |If you customized the editing controls (for example, the Site Actions link or the Edit Page link in SharePoint 2010 Products), check whether they still appear. If they don't appear, you can replace them with the editing controls of the new version by resetting the page to the default version.  <br/> Use the **Reset to Template** command in SharePoint Designer to reset the page to the default version (also known as reghosting). After you have restored the default page, you can then reapply your customizations in the browser by applying a different master page, or by reapplying the customizations in SharePoint Designer.  <br/> |
|Are your customizations still appropriate in the new environment, or do you want to update to the new functionality and look?  <br/> |If you want the new functionality and features, you must reset any customized pages to use the template. Resetting the page basically discards the customizations and attaches your page to the appropriate master page. Any customizations that you want can then be transferred to the master page instead of being stored in individual pages.  <br/> Use the **Reset to Template** command in SharePoint Designer to reset the page to the default version (that is, reghost it). After you have restored the default page, you can then reapply your customizations in the browser by applying a different master page, or by reapplying the customizations in SharePoint Designer.  <br/> |
|Are any pages still checked out?  <br/> |If you check out a page to make changes, make sure that you check in the page again.  <br/> |
   
## See also
<a name="Review"> </a>

#### Other Resources

[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)
  
[Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013](restart-a-database-attach-upgrade-or-a-site-collection-upgrade-to-sharepoint-201.md)

