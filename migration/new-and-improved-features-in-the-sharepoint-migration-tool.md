---
title: "SharePoint Migration Tool (SPMT) Release notes"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
mscollection: 
- SPMigration
- M365-collaboration
localization_priority: Normal
search.appverid: MET150
description: "Learn about the new features and updates to existing features in SharePoint Migration Tool in these release notes."
---

# Release Notes:  SharePoint Migration Tool (SPMT)

Learn about the new features and updates to existing features in SharePoint Migration Tool.
  

## Current and pre-release versions

Download and install SPMT using one of the links listed below.  

| Release |**Public preview**|**First release**|**Rolling out**|**Full General Availability**|
|:-----|:-----|:-----|:-----|:-----|
|Last released build|[3.4.121.4](https://aka.ms/spmt-beta-page)|[3.4.121.4](https://aka.ms/spmt-ga-page)|[3.4.120.7](https://aka.ms/spmt-ga-page)|[3.4.120.7](https://aka.ms/spmt-ga-page)|


## SPMT 3.4.121.4

**New features and important changes**

|Feature|Description|
|:-----|:-----|
|Support migration of files with size up to 100GB|We now support the migration of individual files up to 100GB, which is file size limit for SharePoint online.|
|Display time elapsed and time remaining for each migration|On the migration progress page, the *time elapsed* and  *time remaining* values are displayed for each migration task. *Time remaining* is estimated based on the migration history and displays when there is enough historical data available to run the estimation. The *time remaining" value adjusts according to the history data. After the migration completes, a performance recommendation based on the analysis of the data displays below the top progress bar. </br>Learn more:  [How to improve migration performance](./spmt-performance-guidance.md) |

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|


## SPMT 3.4.121.2

**New features and important changes**

|Feature|Description|
|:-----|:-----|
|Government Cloud configuration|The configuration value of DoD has been changed from 2 to 3.  DoD customers must change the value of *SPOEnvironmentType* to 3. The value for GCC high is still 2.|
|OneNote setting deprecated|The setting *Migrate OneNote folder as OneNote notebook* has been deprecated. SPMT will now always migrate OneNote folders to the destination as OneNote Notebooks. Discontinue the use of *MigrateOneNoteFolderAsOneNoteNoteBook* in PowerShell.


**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|



## SPMT 3.4.121.1

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|


## SPMT 3.4.121.0

The following improvements were added to this release:

**New Features**

|Feature| Description|
|:-----|:-----|
|New setting|A  new setting for SharePoint migration, **Migrate lists with lookup columns**, will control the behavior of migrating all lists referenced in lookup columns.|
|New PowerShell parameter|A new parameter for SharePoint migration, -LookupReferencePolicy, has been added to the cmdlet Register-SPMTMigration. This parameter will control the behavior of migrating all lists referenced in lookup columns. Setting options include: *FIND_ALL_REFERENCE*, *SKIP_AND_CONTINUE* and *DO_NOT_MIGRATE*. The default setting is *FIND_ALL_REFERENCE*. |

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|
|User interface|Warning messages will display in the tool when migration is throttled by SharePoint.|


## SPMT 3.4.120.7

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|


## SPMT 3.4.120.6

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|


## SPMT 3.4.120.5

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|

## SPMT 3.4.120.4

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|



## SPMT 3.4.120.3

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|



## SPMT 3.4.120.2

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|Performance|New checks have been added when a customer uses the bulk upload feature.|
|User experience|Enhancements have been made to the user interface.|
|General|General improvements have been made to fix bugs in tool.|


## SPMT 3.4.120.1

The following improvements were added to this release:

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|



## SPMT 3.4.120.0

The following features are now available in SPMT:

**New Features**

|Feature| Description|
|:-----|:-----|
|Setting deprecated|The setting, **Migrate files and folders with invalid characters** has been deprecated.|
|New setting|A new setting for file share migration, **Replace invalid filename characters**, will auto-replace invalid characters in a filename with a character chosen by the user.
|New PowerShell parameter|A new parameter for file share migration, **-ReplacementOfInvalidChar**, has been added to the cmdlet **Start-SPMTMigration**. This parameter will auto-replace invalid characters in a filename with a character chosen by the user.|
|UI|Tenant admin users can select the promotional link, "Go to Migration Manager" on the SPMT Welcome page.|

**Improvements**

|Issue|Fix|
|:-----|:-----|
|General|General improvements have been made to fix bugs in tool.|
|Performance|Improvements have been made to optimize migration performance.|
|UI|Warning messages will display in the tool when network issues occur during uploading.|



## SPMT 3.4.119.7

The following features were added in this release:

**New features**

|Feature|Description|
|:----|:-----|
|New/updated setting|The setting, **Migrate site settings**, is now an options setting, giving the user more control over what is migrated.  The user can select one of the following: *Preserve all settings*, *Skip title and logo*, *Only title and logo*, or *Skip all settings*.|
|New parameter|A new parameter, **-MigrateWithoutRootFolder**, has been added to the cmdlet, Register-SPMTMigration. In file share migrations, use this parameter to migrate only the root folder's contents to the target. |

**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|General|General improvements have been made fix bugs in the tool.


## SPMT 3.4.119.6

The following features were added in this release:


**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|General|General improvements have been made in addition to some minor bug fixes in tool.


## SPMT 3.4.119.5

The following features were added in this release:


**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|List URL|The original List URL end part format will now be preserved in the destination. 


## SPMT 3.4.119.4

The following features were added in this release:


**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|General|General improvements have been made to fix bugs in tool.|



## SPMT 3.4.119.3

The following features were added in this release:

**New features**

|**Feature**|**Description**|
|:-----|:-----|
|Added selection feature|When migrating fileshares, users can choose to indicate the root folder as part of their source selection.|

**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|Teams|Improvement in teams pages migration.|


## SPMT 3.4.119.2

The following features were added in this release:

**New features**

|**Feature**|**Description**|
|:-----|:-----|
|SharePoint Server 2016|Ability to migrate SharePoint Server 2016 sites to SharePoint online.|

**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|Group mapping|SPMT now migrates default SharePoint groups. Note: You cannot map to other groups.|



## SPMT 3.2.119.2

The following features were added in this release:

**New features**

|**Feature**|**Description**|
|:-----|:-----|
|Microsoft Teams added as a selection choice|Users can now select Teams and channels directly from the destination selection page.|
|User emails for OneDrive|User email accounts for OneDrive migration are now supported as an input value.|
|Version info |A new file, %\AppData\Local\Apps\SharePointMigrationTool\Logs\SPMT-VersionHistory.log will contain version history.|
|Performance recommendations|The performance report contains direct links to detailed content on  performance recommendations.|
|New setting|A new setting, "Temporarily allow migration of scripts", will automatically allow the migration of scripted web parts without having to go in the tenant admin. | 


**Improvements**

|**Issue**|**Fix**|
|:----|:-----|
|Performance|General improvements have been made to the tool.|


## SPMT 3.2.118.0

**New features**

The following features were added to the SharePoint Migration Tool in this release:

|**Feature**|**Description**|
|:-----|:-----|
|User feedback|Users can now provide feedback directly from the tool.|
|Site creation for file shares|Site structure creation is now supported for file share migration.|
|Records management|Support for SharePoint Server migration of Record libraries with limitations. Library record declaration settings are supported for SharePoint Server 2013 and 2016 only. Files declared as records can be migrated directly. Site collection record declarations settings are not supported for SharePoint Online group sites and communication sites.|
|Enable publishing|Users can now choose to skip enabling publishing feature on SharePoint communication site| 
|Setting|New setting allows you to not migrate the site and list general settings in a single list migration.| 
|Setting|New SharePoint setting, "Migrate site settings". Choose if you want to migrate site logo, title, description and other general settings). Default value is on. If it's turned off, the setting will be skipped when migrating to existing destination site in site migration.| 
|Taxonomy migration|By default, managed metadata migration is turned off, and taxonomy is updated in incremental round.|


**Improvements**

In addition to several minor fixes, the primary improvements made in this release are:

|**Issue**|**Fix**|
|:----|:-----|
|Performance|Improvements have been made to taxonomy migration.|
|User input|Improved handling of full URL for both SharePoint Server and SharePoint.|



## SPMT 3.2.115.3

**New features**

The following features were added to the SharePoint Migration Tool in this release:

|**Feature**|**Description**|
|:-----|:-----|
|Document set support|SPMT will attempt to enable the document set feature on site.  If enabling fails, the items in the document set will be skipped, and all the files under the documents will be skipped.|
|Document Template|You can define a document template and choose to have it applied when adding new files.  SPMT now supports customized document templates.|
|Web part templates|If your web part document template is not available in SPO, SPMT can migrate the template from your source environment.


**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:


|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|
|Progress bar|Enhancements have been made to the migration progress bar to provide greater details of your progress.|
|OneNote migration|Improvements made for importing OneNote notebooks.|




## SPMT 3.2.114.0

**New features**

The following features were added to the SharePoint Migration Tool in this release:

|**Feature**|**Description**|
|:-----|:-----|
|Subfolder section|Support for SharePoint Server subfolder selection|
|SharePoint 2010 sites|Support for SharePoint Server 2010 site migration|
|Government cloud|Support for Government cloud (U.S.)|
|List templates|Support for the following list templates have been added:</br></br>- Promoted Link list (ListTemplateType. Value = 170)</br>- Categories List (ListTemplateType. Value = 500)</br>- Asset Library (ListTemplateType. Value = 851)</br></br>For a complete list of supported list templates see:   [SharePoint list templates supported by SPMT](sharepoint-migration-supported-list-templates.md)|

**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:


|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|



## SPMT V3.1.110.1

**New features**

The following features were added to the SharePoint Migration Tool in this release:

|**Feature**|**Description**|
|:-----|:-----|
|Site migration|SharePoint sites that are "out of the box" - sites that do not use any coding or 3rd party tools - can now be migrated. SPMT now preserves site audits. |
|Navigation|Migration of navigation and icons is now supported.|
|Site descriptions|Site description can now be migrated.|
|SharePoint web parts|SPMT now supports the migration of SharePoint web parts. See the full list of SPMT supported web parts: [SPMT Supported SharePoint Web parts](spmt-supported-webparts.md).|
|Page migration|Pages in the site asset library can now be migrated.|
|Managed metadata|This release supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.|
|JSON improvements|Task level settings are now supported for bulk upload using JSON.|
|Filtering|Added Site and list filtering in settings|


**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:


|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|



## SPMT V2.1.102.0

**New features**

The following features were added to the SharePoint Migration Tool, Version V2.1.102.0

|**Feature**|**Description**|
|:-----|:-----|
|Modern design|The SharePoint Migration tool has a new look and feel that is more closely aligned with the SharePoint design for easier use. |

**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:

|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|


## SPMT V2.1.101.6

**New features**

The following features were added to the SharePoint Migration Tool, Version V2.1.101.6

|**Feature**|**Description**|
|:-----|:-----|
|Support for CustomGrid list template|The **CustomerGrid** list template (template ID:120) is now supported. The user can now migrate lists that contain a set of list items with a grid-editing view.|
|New PowerShell setting|When using the **Register-SPMTMigration** PowerShell cmdlet, users can now set the parameter *MigrateAllFieldsAndContentTypes*.|

**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:

|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|

   
## SPMT V2.1.101.0

**New features**

The following features were added to the SharePoint Migration Tool, Version 2.1.101.0

|**Feature**|**Description**|
|:-----|:-----|
|Save session <br/> |The user now has the ability to save their migration session and resume it at later date.<br>
|Read-only sites supported<br/> |The user can migrate a read-only site configured by site policy or the central admin page. <br/> |

   
**Improvements**

In addition to a number of minor fixes, here are the primary improvements made in this release:
  
|**Issue**|**Fix**|
|:-----|:-----|
|Stability  <br/> |General improvements have been made to remove some errors in tool.  <br/> |
|Reports<br/> |The **packageSummary.csv** and **UserNotMapped.csv** reports are now in the details folder. <br/> |



## SPMT V2.1.100.0

**New features**

The following features were added to the SharePoint Migration Tool, Version 2.1.100.0

|**Feature**|**Description**|
|:-----|:-----|
|Powershell migration solution* <br/> |All features of the SharePoint Migration Tool (SPMT) can now be done by using PowerShell cmdlets.<br>
|Settings<br/> |Improved labels and text descriptions for settings.  <br/> |

**Note:**<br>
To use the SPMT 2.1 PowerShell feature (currently in open beta): <br>  
1. Open SPMT v2.1. The PowerShell .dll's will be copied to      *%userprofile%\Documents\WindowsPowerShell\Modules*<br>
2. Run the following:<br>
    ```powershell
    Import-Module Microsoft.SharePoint.MigrationTool.PowerShell
    ```
    <br>To learn more, see:<br> 
[Migrate to SharePoint using PowerShell](./overview-spmt-ps-cmdlets.md)<br>
[SharePoint Migration Tool PowerShell Reference](/powershell/module/spmt)

   
**Improvements**

In addition to a number of minor fixes, here are the primary improvements made in this release:
  
|**Issue**|**Fix**|
|:-----|:-----|
|Stability  <br/> |General improvements have been made to remove some errors in tool.  <br/> |
|Permissions settings<br/> |Separate settings are now available to set file share permissions and the SharePoint on-premises permissions. <br/> |
|Changes to migrating multiple versions <br/> |Checked-in version(s) of a file will migrate but any the checked-out version will not. <br/> |

## SPMT V1.1.90.1

**New features**

The following features were added to the SharePoint Migration Tool, Version 1.1.901.
  
|**Feature**|**Description**|
|:-----|:-----|
|Allow migration of 0 bytes files  <br/> |Files will be migrated even if they are of zero bytes.  <br/> |
|Computer names column  <br/> |A column containing the name of the computers running the migration job has been added to the report.  <br/> |
|Support of incremental check on target environment  <br/> |In SharePoint, an incremental check of the target environment will be performed. If the modified time of the source file is earlier than the modified time of the target file, the file will not be migrated.  <br/> |
   
**Improvements**

In addition to a number of minor fixes, here are the primary improvements made in this release:
  
|**Issue**|**Fix**|
|:-----|:-----|
|Stability  <br/> |General improvements have been made to remove some errors in tool.  <br/> |
|Permissions fixes  <br/> |We have made several improvements to better preserve the permission when requested and not removing existing permission in the destination.  <br/> |
|Warnings when files are checked out  <br/> |Users will now have warning messages appear in the tool when attempting to migrate a file that was checked out.  <br/> |
|Report when performing only a scan  <br/> |The **FilesReport.csv** file will now show the correct results when only scanning option is turned on.  <br/> |
   


[Download SharePoint Migration Tool](https://spmtreleasescus.blob.core.windows.net/install/default.htm)
  
[How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md)