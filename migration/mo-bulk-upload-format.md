---
title: "How to format your CSV for data content migration using the Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to format your CSV file for bulk upload in Migration Manager"
---

# How to format your CSV for data content migration in Migration Manager

  
## Using a comma separated value (CSV) file for data content migration

Migration Manager lets you use a comma separated (CSV) file to bulk migrate your data. Use any text editor, or an application like Excel, to create the CSV file.
  
 **CSV file format**
  
There are six columns needed in your CSV file -- the first three are your source values, each providing detail about where your data is currently located. The remaining three columns indicate the site, document library and optional subfolder to where you are migrating your data. All six columns must be accounted for in the file, even if you are not needing a value for a given field.
  
Here's an example of the format for the CSV file. The first row show files that are being migrated from a local file share. The second row shows files that are being migrated from an on-premises SharePoint Server site.
  
![Sample format when using a CSV file](media/73fadfad-77ad-4d3a-b738-bc7063bc2659.jpg)
  
This example shows how it would appear in a .txt file.
  
```
Source,SourceDocLib,SourceSubFolder,TargetWeb,TargetDocLib,TargetSubFolder
C:\MigrationTests\testfiles,,,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder
https://sharepoint2013.com/sites/contosoteamsite/,DocumentLibraryName,DocLibrarySubfolder_name,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder

```

> [!IMPORTANT]
>  *Do not*  include a header row in your CSV file. The second example included headers to demonstrate the order of the fields. Remember to account for all six columns in the file, even if you are not needing a value for a given field. 
  
> [!IMPORTANT]
> If you use the standard out-of-the-box Document library ("Shared Documents"), you must use the internal name "Documents" as the placeholder value for the  *Source Document Library*  (Column B) in your CSV file. If you enter "Shared Documents" in that column, you will receive an "invalid document library" error. 
  
> [!IMPORTANT]
> Proxy connections are not supported. Using Proxy connections will yield errors such as "SharePoint login fail" or "cannot load document library". 
  
 **To create a CSV file for data migration**
  
The following example uses Excel to create the CSV file.
  
1. Start Excel.
    
2. Enter the values for your migration jobs. Enter one migration source and destination per row. See the reference table below for further explanation of columns.
    
  - **Column A:** Enter either a file share path or an on-premises SharePoint Server site URL.  *Required.* 
    
  - **Column B:** Enter name of the SharePoint Server document library you are migrating. If you leave this field empty, all document libraries will be migrated. If you are migrating a file share, leave this column empty.  *Optional.* 
    
  - **Column C:** Enter the name of the subfolder in the document library. If this column is left empty, the migration starts from the root. If there is a value in this column, the migrations starts from the subfolder and down.  *Optional.* 
    
  - **Column D:** Enter the SharePoint Online site URL where the files are to be migrated.  *Required.* 
    
  - **Column E:** Enter the name of the document library in the SharePoint Online site where the files are to be migrated.  *Required.* 
    
  - **Column F:** Enter the name of the subfolder in the document library. If this column is left empty then the files will be moved to the root level.  *Optional.* 
    
3. Close and save as a Comma delimited (\*.csv) file.
    
### Column definitions

The following table explain the values needed in each column in your CSV file.
  
|||
|:-----|:-----|
|Source  <br/> | *Required*  . Enter either a file share path or an on-premises SharePoint Server site URL.  <br/> |
|Source DocLib  <br/> | *Optional*  . Enter name of the SharePoint Server document library you are migrating. If you leave this field empty, all document libraries will be migrated. If you are migrating a file share, leave this column empty.  <br/> |
|Source SubFolder  <br/> | *Optional*  . Enter the name of the subfolder in the document library. If this column is left empty, the migration starts from the root. If there is a value in this column, the migrations starts from the subfolder and down.  <br/> This column is used only for SharePoint Server sites. It is ignored for file share migration.  <br/> |
|Target Web  <br/> | *Required*  . Enter the SharePoint Online site URL where the files are to be migrated.  <br/> |
|Target DocLib  <br/> | *Required*  . Enter the name of the document library with the SharePoint Online site where the files are to be migrated.  <br/> |
|Target SubFolder  <br/> | *Optional*  . Enter the name of the subfolder in the document library. If this column is left empty then the files will be moved to the root level.  <br/> |

