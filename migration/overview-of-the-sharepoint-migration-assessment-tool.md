---
title: "Overview of the SharePoint Migration Assessment Tool"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 01/11/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: a6dca2a3-72d6-4717-abe9-a58f025ea26e
description: "Overview of the SharePoint Migration Assessment Tool"
---

# Overview of the SharePoint Migration Assessment Tool

The SharePoint Migration assessment tool (SMAT) is a simple command line executable that scans the contents of your SharePoint farm to help identify the impact of migrating your server to SharePoint Online with Office 365.
  
As the tool is designed to run without impacting your environment, you may observe the tool requires one to two days to complete a scan of your environment. During this time, the tool will report progress in the console window. After the scan is complete, you can find output files in the Logs directory. This is where you will find the summary and more detailed insights into the scenarios that could be impacted by migration.
  
> [!NOTE]
> To download the SharePoint Migration Tool, click here: [Download the SharePoint Migration Assessment Tool ](https://www.microsoft.com/en-us/download/details.aspx?id=53598)
  
> [!NOTE]
> To improve the quality of Microsoft products and services, the tool will report anonymous statistical information back to Microsoft. Optionally, you can identify your organization when prompted at the end of the scan. If the tool is not able to connect to the internet to report this information, the tool will still function as otherwise expected. 
  
## Overview

The tool offers two modes: Assessment and Identity Mapping.
  
### Assessment

This is the default mode. If you run SMAT.exe, assessment will run. The assessment process runs scans against the SharePoint farm and associated content looking for issues that have been known to cause issues for customers migrating into SharePoint Online. For more information on the scans that are available, see [SharePoint Migration Assessment Tool: Scan Reports Roadmap](sharepoint-migration-assessment-toolscan-reports-roadmap.md)
  
### Identity Mapping

Identity Mapping allows you to generate a report of all the user and group identities that have access to your SharePoint environment and attempts to map those identities to Azure AD user and group identities.
  
This process is very important to migration. If identities are not properly set up prior to migration, it can result in users losing access to content as well as information being incorrect in the site. For example, the Created By and Modified fields will not show the correct identity post migration.
  
For more information on Identity Mapping, see [SharePoint Migration Identity Mapping Tool](sharepoint-migration-identity-mapping-tool.md).
  
## Prerequisites

The tool is built to be run from within a SharePoint 2010 or 2013 farm.
  
- To run the tool, all files must be extracted from any compressed package before execution.
    
- The tool must run as the Farm service account. A farm administrator account is acceptable as long as the account has been given read access to all web applications. The account also needs explicit Full Control permissions on both Operations | Administrators and Sharing | Permissions on the User Profile Service Application. There are a series of checks to ensure the account has enough permissions prior to scanning the environment.
    
## Config files

You can modify two config files for SMAT.
  
 **SiteSkipList.csv** is installed in same directory as SMAT.exe. Adding sites to this CSV will tell SMAT not to include these sites in the report output. See SiteSkipList.csv for examples of how to add sites to the skip list. 
  
 **ScanDef.json** is installed in the same directory as the SMAT tool. You can use ScanDef.json to enable or disable individual scans for the assessment tool. This file contains configurations for assessment on both SharePoint 2010 and 2013 as well as Identity Mapping. 
  
To disable a scan, locate the entry in the ScanDef.json file and set  *Enabled*  to **false**. This is useful if there is a scan that your business doesn't care about and disabling the scan will reduce the overall execution time of the assessment tool.
  
The following disables the Alerts scan.
  
{ "Name": "Alerts", "Type": "AlertsScanner", "SupportedVersions": [ "2010", "2013", "2016" ], "ReportCategoryType": "SPSite", "Enabled": false }
  
The SupportedVersion will tell the assessment tool which versions of SharePoint a given scan applies to. For example, SharePoint 2010 did not have SharePoint Add-ins, so the Apps scanner does not list 2010 as a supported version.
  
{ "Name": "Apps", "Type": "AppsScanner", "SupportedVersions": [ "2013", "2016" ], "ReportCategoryType": "SPSite", "Enabled": true }
  
Some scans have additional configuration options. These are configurable in the ScanDef.json file. Not all scans have configurable properties. However, if a scan does have a property, there is a default configured in the ScanDef.json file that can be modified. For example, the SiteTemplateLanguage scan has a filter to exclude English sites [locale 1033]. If your team has concerns about migrating English sites, you could modify the filter to include those sites:
  
{ "Name": "SiteTemplateLanguage", "Type": "SiteTemplateLanguageScanner", "SupportedVersions": [ "2010", "2013", "2016" ], "Property": { "ExcludedLanguages": "" }, "ReportCategoryType": "SPSite", "Enabled": true }
  
If you remove or corrupt the ScanDef.json file, a default configuration that is embedded in the SMAT.exe executable will be used instead. This will be noted in the SMAT.log file. If you make a change to disable a scan or a property and notice the change is not picked up when you run SMAT.exe, look in the SMAT.log file for details.
  
## Execution

Run smat.exe from the extracted files location. To see all the available parameters, run: smat.exe /help.
  
SMAT.exe is a launcher program that determines your intentions based on the parameters passed in and then loading the appropriate application to do the work requested. Under the covers, there are 3 executables that are responsible for doing the work:
  
- SMAT2010.exe - Performs assessment on SharePoint 2010 environments.
    
- SMAT2013.exe - Performs assessment on SharePoint 2013 environments.
    
- SMIT.exe - Performs identity mapping work for both SharePoint 2010 and 2013 environments.
    
Here is what you will see when running SMAT.exe to perform assessment from PowerShell.exe. Note the PowerShell window ran SMAT.exe which launched the application to perform the work. Once the working application is loaded, the SMAT.exe loader program terminates and returns control to the operator. The tool performing the work will run in its own window until it completes.
  
## Log files

You may see up to 3 log files in the output directory.
  
- **SMAT.log** - This file contains all the logging from the tool execution. This will contain 3 levels of logging. Information, Warning, and Errors. Information help track down progress and troubleshooting issues. Warnings are typically expected error conditions. Errors are unexpected conditions that our tooling was unable to determine if they will be a blocker to moving forward. These need to be looked at. 
    
- **SMAT_Errors.log** - This contains only the Error events. If this file is missing after the tooling completes, it indicates there were no errors found. 
    
- **SMATTelemetry.log** - This contains logging for the telemetry upload tooling. Any issues in here will not impact generating your reports. 
    
## Automating assessment

If you have the need to schedule the assessment process, you can do so by running the specific EXE. For example, if you want to setup a scheduled task on a SharePoint 2010 farm for assessment, you would point the scheduled task to SMAT2010.exe. If you wanted to write a PowerShell script that ran assessment on SharePoint 2013, you would point the script to SMAT2013.exe.
  
Any scripting scenario will need to use the -q switch to run the EXE in quiet mode. This mode does not output anything to the console and avoids anything that would prompt the operator for input.
  
At this time the executable for Identity Mapping [SMIT.exe] does not support scripting. This process will prompt for credentials to Azure at a minimum and may prompt for credentials to connect to Active Directory. If you attempt to script against this executable, you will find that it hangs and never completes when the program prompts for credentials.
  
## More info

To download the SharePoint Migration Tool and for more information about how to address issues identified in the assessment reports see.
  
- [Download the SharePoint Migration Assessment Tool ](https://www.microsoft.com/en-us/download/details.aspx?id=53598)
    
- [SharePoint Migration Assessment Tool: Scan Reports Roadmap](sharepoint-migration-assessment-toolscan-reports-roadmap.md)
    

