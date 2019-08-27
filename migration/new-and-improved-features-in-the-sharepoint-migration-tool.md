---
title: "New and improved features in the SharePoint Migration Tool"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
mscollection: 
- SPMigration
- M365-collaboration
localization_priority: Normal
search.appverid: MET150
description: "Learn about the new features and updates to existing features in SharePoint Migration Tool."
---

# Release Notes:  SharePoint Migration Tool (SPMT)

Learn about the new features and updates to existing features in SharePoint Migration Tool.
  
>[!NOTE]
>To install the current release download here: [SharePoint Migration Tool ](http://spmtreleasescus.blob.core.windows.net/install/default.htm)

>[!NOTE]
>**NEW**: To download the new public preview release: [SharePoint Migration Tool Public Preview](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)

### SPMT Public Preview 3.2.113.6

- Support for SharePoint Server subfolder selection
- Support for SharePoint Server 2010 site migration
- Support for Government cloud (U.S.)
- Support for the following list templates:
    - Promoted Link list (ListTemplateType. Value = 170)
    - Categories List (ListTemplateType. Value = 500)
    - Asset Library (ListTemplateType. Value = 851) 

### SPMT V3.1.110.1 (Current release)

**New features**

The following features were added to the SharePoint Migration Tool V3.0.

|**Feature**|**Description**|
|:-----|:-----|
|Site migration|SharePoint sites that are "out of the box" - sites that do not use any coding or 3rd party tools - can now be migrated. SPMT now preserves site audits. |
|Navigation|Migration of navigation and icons is now supported.|
|Site descriptions|Site description can now be migrated.|
|SharePoint webparts|SPMT now supports the migration of SharePoint webparts. See the full list of SPMT supported web parts: [SPMT Supported SharePoint Webparts](spmt-supported-webparts.md).|
|Page migration|Pages in the site asset library can now be migrated.|
|Managed metadata|This release supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.|
|JSON improvements|Task level settings are now supported for bulk upload using JSON.|
|Filtering|Added Site and list filtering in settings|


**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:


|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|



### SPMT V2.1.102.0

**New features**

The following features were added to the SharePoint Migration Tool, Version V2.1.102.0

|**Feature**|**Description**|
|:-----|:-----|
|Modern design|The SharePoint Migration tool has a new look and feel that is more closely aligned with the Sharepoint Online design for easier use. |

**Improvements**

In addition to several minor fixes, here are the primary improvements made in this release:

|**Issue**|**Fix**|
|:----|:-----|
|Stability|General improvements have been made to remove some errors in tool.|


### SPMT V2.1.101.6

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

   
### SPMT V2.1.101.0

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



### SPMT V2.1.100.0

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
[Migrate to SharePoint Online using PowerShell](/sharepointmigration/overview-spmt-ps-cmdlets)<br>
[SharePoint Migration Tool PowerShell Reference](/powershell/module/spmt)

   
**Improvements**

In addition to a number of minor fixes, here are the primary improvements made in this release:
  
|**Issue**|**Fix**|
|:-----|:-----|
|Stability  <br/> |General improvements have been made to remove some errors in tool.  <br/> |
|Permissions settings<br/> |Separate settings are now available to set file share permissions and the SharePoint on-premises permissions. <br/> |
|Changes to migrating multiple versions <br/> |Checked-in version(s) of a file will migrate but any the checked-out version will not. <br/> |

### SPMT V1.1.90.1

**New features**

The following features were added to the SharePoint Migration Tool, Version 1.1.901.
  
|**Feature**|**Description**|
|:-----|:-----|
|Allow migration of 0 bytes files  <br/> |Files will be migrated even if they are of zero bytes.  <br/> |
|Computer names column  <br/> |A column containing the name of the computers running the migration job has been added to the report.  <br/> |
|Support of incremental check on target environment  <br/> |In SharePoint Online, an incremental check of the target environment will be performed. If the modified time of the source file is earlier than the modified time of the target file, the file will not be migrated.  <br/> |
   
**Improvements**

In addition to a number of minor fixes, here are the primary improvements made in this release:
  
|**Issue**|**Fix**|
|:-----|:-----|
|Stability  <br/> |General improvements have been made to remove some errors in tool.  <br/> |
|Permissions fixes  <br/> |We have made several improvements to better preserve the permission when requested and not removing existing permission in the destination.  <br/> |
|Warnings when files are checked out  <br/> |Users will now have warning messages appear in the tool when attempting to migrate a file that was checked out.  <br/> |
|Report when performing only a scan  <br/> |The **FilesReport.csv** file will now show the correct results when only scanning option is turned on.  <br/> |
   


[Download SharePoint Migration Tool](http://spmtreleasescus.blob.core.windows.net/install/default.htm)
  
[How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md)

