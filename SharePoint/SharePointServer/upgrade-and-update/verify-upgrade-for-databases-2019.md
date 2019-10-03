---
title: "Verify database upgrades in SharePoint Server 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f3819495-4b67-4a71-ba46-23e43b175620
description: "Learn how to verify when a database-attach upgrade to SharePoint Server 2019 has finished, and identify any problems that may have occurred."
---

# Verify database upgrades in SharePoint Server 2019

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)]  
  
After you upgrade databases to SharePoint Server 2019, you must verify that the content was successfully upgraded to the new version. You can verify the status of the database-attach upgrade (is it still in progress, or has it been completed successfully or with errors or failures?) to see whether issues remain for you to address. When you follow these steps as part of a trial upgrade, you can use them to identify customizations that have to be reworked before you attempt to upgrade your production environment. When you upgrade your production environment, it is even more important that you know whether the upgrade has completed and what issues remain to be addressed.
  
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
    
    Review the upgrade log file and the upgrade error log file (generated when you run the upgrade). The upgrade log file and the upgrade error log file are located at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\16\LOGS. The logs are named in the following format: Upgrade- _YYYYMMDD-HHMMSS-SSS-\<GUID\>_.log, where  _YYYYMMDD_ is the date and  _HHMMSS-SSS_ is the time (hours in 24-hour clock format, minutes, seconds, and milliseconds). The upgrade error log file combines all errors and warnings in a shorter file and is named Upgrade-  _YYYYMMDD-HHMMSS-SSS-\<GUID\>_-error.log.
    
    The format of the log files complies with the Unified Logging System (ULS) conventions. To review the log files to find and troubleshoot issues, start at the top of the files. Errors or warnings may be repeated if they occur for several site collections in the environment, or if they block the upgrade process completely. For example, if you cannot connect to the configuration database, the upgrade process will try (and fail) several times and these tries will be listed in the log file.
    
If you find blocking issues in the log file, you can resolve the issues and then restart upgrade to continue with the process.
  
### Check the upgrade status for databases

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
    
  - Are all features associated with the sites working?
    
- Search
    
  - Check that the search configuration settings are alike those in the SharePoint Server 2019 farm.
    
  - Run search queries, and verify that the queries work as expected and provide appropriate results. Twenty-four hours later, view the query reports and look for issues.
    
  - Search for people and profiles.
    
  - Check any Search customizations to make sure that they work as expected.
    

