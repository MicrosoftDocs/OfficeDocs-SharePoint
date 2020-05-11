---
title: "How to format a CSV or JSON file for bulk upload in Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to format a CSV or JSON file for bulk upload in Migration Manager"
---

# How to format a CSV or JSON file for bulk upload in Migration Manager

>[!Note]
>Features noted in this topic are part of a preview release. The content and the functionality are subject to change and are not subject to the standard SLAs for support.



  
## Using a comma separated value (CSV) file for data content migration

Migration Manager lets you use a comma separated (CSV) file to bulk migrate your data. Use any text editor, or an application like Excel, to create the CSV file.
  
 **CSV file format**
  
There are six columns needed in your CSV file -- the first three are your source values, each providing detail about where your data is currently located. The remaining three columns indicate the site, document library and optional subfolder to where you are migrating your data. All six columns must be accounted for in the file, even if you are not needing a value for a given field.
  
Here's an example of the format for the CSV file. The first row show files that are being migrated from a local file share. The second row shows files that are being migrated from an on-premises SharePoint Server site.
  
![Sample format when using a CSV file](media/73fadfad-77ad-4d3a-b738-bc7063bc2659.jpg)
  
This example shows how it would appear in a .txt file.
  
```
Source,SourceDocLib,SourceSubFolder,TargetWeb,TargetDocLib,TargetSubFolder
\\contoso\MigrationTests\testfiles,,,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder
https://sharepoint2013.com/sites/contosoteamsite/,DocumentLibraryName,DocLibrarySubfolder_name,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder

```

> [!IMPORTANT]
>  *Do not*  include a header row in your CSV file. The second example included headers to demonstrate the order of the fields. Remember to account for all six columns in the file, even if you are not needing a value for a given field. 

  
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

## Using a JSON file for data content migration



The following example shows the JSON format used in migrating your data.

As with the CSV files, the minimum required values are Source, Source DocLib, Target Web and Target DocLib.  

```json
{
  "Tasks": [
    {
      "SourcePath": \\contoso\fileshare\MigTest",
      "TargetPath": "https://a830edad9050849387E18042320.sharepoint.com",
      "TargetList": "Documents",
      "TargetListRelativePath": "subfolder"
    },
    {
      "SourcePath": "http://EXHB-1873",
      "TargetPath": "https://a830edad9050849387E18042320.sharepoint.com",
      "Items": {
        "Lists": [
          {
            "SourceList": "versionList",
            "TargetList": "NewVersionList"
          }
        ],
        "SubSites": []
      }
    },
    {
      "SourcePath": "http://EXHB-1873",
      "TargetPath": "https://a830edad9050849387E18042320.sharepoint.com",
      "Items": {
        "Lists": [
          {
            "SourceList": "listVersion2",
            "TargetList": "ListVersion2"
          },
          {
            "SourceList": "listVersion3",
            "TargetList": "ListVersion3"
          }
        ],
        "SubSites": [
          {
            "SourceSubSitePath": "subSite",
            "TargetSubSitePath": "targetSubSite",
            "Lists": [
              {
                "SourceList": "testSubListB",
                "TargetList": "TargetSubList"
              }
            ]
          }
        ]
      }
    },
    {
      "SourcePath": "http://EXHB-1873/subsite2",
      "TargetPath": "https://a830edad9050849387E18042320.sharepoint.com/targetSubSite2"
    }
  ]
}
```
   

