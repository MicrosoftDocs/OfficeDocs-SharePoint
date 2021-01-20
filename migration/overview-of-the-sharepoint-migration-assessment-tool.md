---
title: "SharePoint Migration Assessment Tool"
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
ms.date: 01/11/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
ms.assetid: a6dca2a3-72d6-4717-abe9-a58f025ea26e
description: "Overview of the SharePoint Migration Assessment Tool (SMAT). A tool that helps identify the impact of migrating your server to SharePoint in Microsoft 365."
---

# Overview of the SharePoint Migration Assessment Tool

The SharePoint Migration Assessment Tool is a simple command line executable tool. It scans the contents of your SharePoint farm to help identify the impact of migrating your server to SharePoint with Microsoft 365.
  
The tool is designed to run without impacting your environment, so you might observe that the tool requires one to two days to complete a scan of your environment. During this time, the tool reports progress in the console window. After the scan finishes, the output files are in the Logs directory. This is where you can find the summary and more detailed insights into the scenarios that could be impacted by migration.
  
> [!NOTE]
> To download the SharePoint Migration Tool, see [Download the SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598).
  
> [!NOTE]
> To improve the quality of Microsoft products and services, the tool reports anonymous statistical information back to Microsoft. Optionally, you can identify your organization when prompted at the end of the scan. If the tool can't connect to the internet to report this information, the tool still functions as otherwise expected.

## Modes in SharePoint Migration Assessment Tool

The tool offers two modes: Assessment and Identity Mapping.
  
### Assessment

This is the default mode. If you run SMAT.exe, the assessment runs. The assessment process runs scans against the SharePoint farm and associated content. It looks for issues that have been known to cause issues for customers who are migrating into SharePoint. For more info about the scans that are available, see [SharePoint Migration Assessment Tool: Scan Reports Roadmap](sharepoint-migration-assessment-toolscan-reports-roadmap.md).
  
### Identity Mapping

You can use Identity Mapping to generate a report of all the user and group identities that have access to your SharePoint environment and attempts to map those identities to Azure AD user and group identities.
  
This process is very important to migration. If identities aren't correctly set up before migration, users could possibly lose access to content, as well as incorrect information on the site. For example, the **Created By** and **Modified** fields might not show the correct identity post migration.
  
For more info about Identity Mapping, see [SharePoint Migration Identity Mapping Tool](sharepoint-migration-identity-mapping-tool.md).
  
## Prerequisites

The tool is built to be run from within a SharePoint 2010 or 2013 farm and has these prerequisites:
  
- To run the tool, all files must be extracted from any compressed package before execution.
    
- The tool must run as the Farm service account. A farm administrator account is acceptable as long as the account has been given read access to all web applications. The account also needs explicit Full Control permissions on both **Operations** > **Administrators** and **Sharing** > **Permissions** on the User Profile service application. There are a series of checks to ensure that the account has enough permissions before it scans the environment.

- The tool supports only English versions of SharePoint.
    
## Config files

You can modify two config files for SMAT:

-  **SiteSkipList.csv** is installed in the same directory as SMAT.exe. Adding sites to this CSV tells SMAT not to include these sites in the report output. For examples about how to add sites to the skip list, see SiteSkipList.csv. 
  
 - **ScanDef.json** is installed in the same directory as the SMAT. You can use ScanDef.json to enable or disable individual scans for SMAT. This file contains configurations for assessment on both SharePoint 2010 and 2013, as well as Identity Mapping. 
  
To disable a scan, locate the entry in the ScanDef.json file, and set  *Enabled*  to **false**. This is useful if there is a scan that your business doesn't care about. Disabling the scan reduces the overall execution time of SMAT.
  
The following disables the Alerts scan.
 
`{ "Name": "Alerts", "Type": "AlertsScanner", "SupportedVersions": [ "2010", "2013", "2016" ], "ReportCategoryType": "SPSite", "Enabled": false }`
  
The **SupportedVersion** informs SMAT which versions of SharePoint a specific scan applies to. For example, SharePoint 2010 didn't have SharePoint add-ins, so the Apps scanner doesn't list 2010 as a supported version.
  
`{ "Name": "Apps", "Type": "AppsScanner", "SupportedVersions": [ "2013", "2016" ], "ReportCategoryType": "SPSite", "Enabled": true }`
  
Some scans have additional configuration options. These are configurable in the ScanDef.json file. Not all scans have configurable properties. However, if a scan does have a property, there's a default property configured in the ScanDef.json file that can be modified. For example, the **SiteTemplateLanguage** scan has a filter to exclude English sites [locale 1033]. If your team has concerns about migrating English sites, you could modify the filter to include those sites:
  
`{ "Name": "SiteTemplateLanguage", "Type": "SiteTemplateLanguageScanner", "SupportedVersions": [ "2010", "2013", "2016" ], "Property": { "ExcludedLanguages": "" }, "ReportCategoryType": "SPSite", "Enabled": true }`
  
If you remove or corrupt the ScanDef.json file, a default configuration that is embedded in the SMAT.exe executable file will be used instead. This is noted in the SMAT.log file. If you disable a scan or change a property and notice that the change isn't picked up when you run SMAT.exe, look in the SMAT.log file for details.
  
## Execution

Run smat.exe from the extracted files location. To see all the available parameters, run: `smat.exe /help`.
  
SMAT.exe is a launcher program that determines your intentions based on the parameters passed in, and then loads the appropriate application to do the requested work. Under the covers, there are three executable files that are responsible for doing the work:
  
- **SMAT2010.exe** - Performs assessment on SharePoint 2010 environments.
    
- **SMAT2013.exe** - Performs assessment on SharePoint 2013 environments.
    
- **SMIT.exe** - Performs identity mapping work for both SharePoint 2010 and 2013 environments.
    
When running SMAT.exe to perform an assessment from PowerShell.exe, the following actions occur. The PowerShell window running SMAT.exe launches the app to perform the work. After the working app is loaded, the SMAT.exe loader program terminates, and returns control to the operator. The tool performing the work runs in its own window until it completes.
  
## Log files

You might see up to three log files in the output directory:
  
- **SMAT.log** - This file contains all the logging from the tool execution. This contains three levels of logging: *Information*, *Warning*, and *Errors*. Information helps track down progress and troubleshooting issues. Typically, Warnings are expected error conditions. Errors are unexpected conditions that our tooling was unable to determine whether they will be a blocker to moving forward. These need to be reviewed. 
    
- **SMAT_Errors.log** - This contains only the Error events. If this file is missing after the tooling completes, it indicates that no errors were found. 
    
- **SMATTelemetry.log** - This contains logging for the telemetry upload tooling. Any issues in here don't impact generating your reports. 
    
## Automating assessment

If you need to schedule the assessment process, you can do so by running the specific .exe file. For example, if you want to set up a scheduled task on a SharePoint 2010 farm for assessment, you would point the scheduled task to SMAT2010.exe. If you want to write a PowerShell script that ran assessment on SharePoint 2013, you would point the script to SMAT2013.exe.
  
Any scripting scenario must use the `-q` switch to run the .exe file in quiet mode. This mode doesn't provide any output to the console and avoids anything that would prompt the operator for input.
  
At this time, the executable file for Identity Mapping (SMIT.exe) doesn't support scripting. This process prompts for credentials to Azure at a minimum and might prompt for credentials to connect to Active Directory. If you attempt to script against this executable file, it hangs and doesn't complete when the program prompts for credentials.
  
## More info

To download the SharePoint Migration Tool, and for more info about how to address issues identified in the assessment reports, see
  
- [Download the SharePoint Migration Assessment Tool ](https://www.microsoft.com/download/details.aspx?id=53598)
    
- [SharePoint Migration Assessment Tool: Scan Reports Roadmap](sharepoint-migration-assessment-toolscan-reports-roadmap.md)
