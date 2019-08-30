---
title: "Verify database upgrades in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 56c70ee5-4ed2-4560-b2ba-53ae87774c2f
description: "Learn how to verify when a database-attach upgrade to SharePoint 2013 has finished, and identify any problems that may have occurred."
---

# Verify database upgrades in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
After you upgrade databases to SharePoint 2013, you must verify that the content was successfully upgraded to the new version. You can verify the status of the database-attach upgrade (is it still in progress, or has it been completed successfully or with errors or failures?) to see whether issues remain for you to address. When you follow these steps as part of a trial upgrade, you can use them to identify customizations that have to be reworked before you attempt to upgrade your production environment. When you upgrade your production environment, it is even more important that you know whether the upgrade has completed and what issues remain to be addressed.
  
In some cases, you might have to restart upgrade to finish upgrading your databases. For more information about how to restart upgrade, see [Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013](restart-a-database-attach-upgrade-or-a-site-collection-upgrade-to-sharepoint-201.md). For information about how to restart a site collection upgrade, see [Manage site collection upgrades to SharePoint 2013](manage-site-collection-upgrades-to-sharepoint-2013.md).
  
## Verify upgrade status for databases
<a name="Verify"> </a>

You can use the following methods to verify upgrade: 
  
- Use the Upgrade Status page in Central Administration
    
    This page lists all farm, service, or content database upgrades and their statuses. This includes a count of errors or warnings.
    
- Review the log files to look for errors or warnings
    
    If upgrade was not successfully completed, you can view the log files to find the issues, address them, and then restart the upgrade process.
    
### Review the log files for database attach upgrade

To verify that upgrade has succeeded, you can review the following log and error files: 
  
- The upgrade log file and the upgrade error log file.
    
    Review the upgrade log file and the upgrade error log file (generated when you run the upgrade). The upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\15\LOGS. The logs are named in the following format: Upgrade- _YYYYMMDD-HHMMSS-SSS_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). The upgrade error log file combines all errors and warnings in a shorter file and is named Upgrade-  _YYYYMMDD-HHMMSS-SSS_-error.log.
    
    The format of the log files complies with the Unified Logging System (ULS) conventions. To review the log files to find and troubleshoot issues, start at the top of the files. Errors or warnings may be repeated if they occur for several site collections in the environment, or if they block the upgrade process completely. For example, if you cannot connect to the configuration database, the upgrade process will try (and fail) several times and these tries will be listed in the log file.
    
If you find blocking issues in the log file, you can resolve the issues and then restart upgrade to continue with the process.
  
### Check upgrade status for databases

The Upgrade Status page lists the upgrade sessions and gives details about the status of each session — whether it succeeded or failed, and how many errors or warnings occurred for each server. The Upgrade Status page also includes information about the log and error files for the upgrade process and suggests remedies for issues that might have occurred.
  
 **To view upgrade status in SharePoint Central Administration**
  
1. Verify that you have the following administrative credentials:
    
  - To use SharePoint Central Administration, you must be a member of the Farm Administrators group.
    
2. On the Central Administration home page, in the **Upgrade and Migration** section, click **Check upgrade status**.
    
## Validate the upgraded environment
<a name="ValidateEnv"> </a>

After you determine whether upgrade was completed successfully, validate your environment. Review the following items:
  
- Service applications
    
  - Are they configured correctly?
    
  - Are the service application proxies configured the way that you want?
    
  - Do you have to create new connections between farms?
    
- Site collections
    
  - Are sites that were not upgraded working as expected in 2010 mode?
    
  - Are all features associated with the sites working?
    
- Search
    
  - Run a crawl, and review the log files.
    
  - Run search queries, and verify that the queries work as expected and provide appropriate results. Twenty-four hours later, view the query reports and look for issues.
    
  - Search for people and profiles.
    
  - Check any Search customizations to make sure that they work as expected.
    
## See also
<a name="ValidateEnv"> </a>

#### Other Resources

[Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013](restart-a-database-attach-upgrade-or-a-site-collection-upgrade-to-sharepoint-201.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)
  
[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md)

