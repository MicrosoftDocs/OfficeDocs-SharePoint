---
ms.date: 03/13/2018
title: "Format your JSON or CSV file for data content migration - SharePoint"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150 
ms.assetid: 
description: "How to format a JSON or CSV file for data content migration by using the SharePoint Migration tool (SPMT)."
---

# Bulk upload SPMT migration tasks using JSON or CSV files

The SharePoint Migration tool (SPMT) lets you bulk upload your migration task information by using either a JSON or CSV file. This method helps if you're creating a large number of tasks.

Learn how to:

- [Bulk upload using a CSV file](#use-a-csv-file-for-bulk-upload)
- [Bulk upload using a JSON file](#use-a-json-file-for-bulk-upload)
- [Troubleshooting](#troubleshooting)
  
## Use a CSV file for bulk upload

Use any text editor, or an application like Microsoft Excel, to create the CSV file. The first three columns are source values that detail where your data is currently located. The remaining three columns indicate the site, document library, and optional subfolder where you're migrating your data.

### Column definitions  
  
|Column content|Description|
|:-----|:-----|
|Column 1 "Source" | *Required*. Enter an on-premises SharePoint Server site URL or the path to a local file share. For SharePoint Server 2013 and 2016, you can also use the log-in name or the SID in this column. |
|Column 2 "Source DocLib" | *Optional*. Enter the name of the SharePoint Server document library that you're migrating. If you leave this field empty, all document libraries are migrated. This column needs to be empty when migrating from a local file share.|
|Column 3 "Source SubFolder" | *Optional*. Enter the name of the subfolder in the document library. If this column is left empty, the migration starts from the root. If there's a value in this column, the migration starts from the subfolder. This column needs to be empty when migrating from a local file share.|
|Column 4 "Target Web" | *Required*. Enter the destination SharePoint site URL where the files are to be migrated.|
|Column 5 "Target DocLib" | *Required*. Enter the name of the document library with the SharePoint site where the files are to be migrated.|
|Column 6 "Target SubFolder "| *Optional*. Enter the name of the subfolder in the document library. If this column is left empty, the files are moved to the root level. |
|Column  7 "RegisterAsHubSite"|*Optional.*  To register a site as a hub site after migration, enter the name of hub site and leave the next column, AssociateWithHubURL, blank. For SharePoint site migration only. |
|Column 8 "AssociateWithHubURL"|*Optional.* To associate the site to another hub site, enter the URL of an existing hub site. In this case, column 7 "RegisterAsHubSite" is left blank. For SharePoint site migration only.|

>[!Important]
>**Hub site association:** Registering and associating hubsites occurs at the final stage of the migration. If you terminate a task before it completes, the hub site work may not be performed.  SPMT will not change the hub association if it finds the site is already associated to a hub site.  A site will not be -"un-registered" if it already registered as a hub site.

## Example CSV  

Here's an example of the CSV file format. The first row shows files that are being migrated from a local file share to SharePoint. The second row shows files that are being migrated from an on-premises SharePoint Server site to SharePoint in Microsoft 365. The third row show files that are being migrated from a local file share to OneDrive. 

**Before you begin**

- Enter one migration source and destination per row.
- If you use the standard out-of-the-box document library ("Shared Documents"), you must use the internal name "Documents" as the placeholder value for the *Source Document Library* (column B) in your CSV file. If you enter "Shared Documents" in that column, you get an "invalid document library" error.
- If the language of the destination SharePoint site isn't English, check the internal name of the "Shared Documents" Document library at https://contoso.sharepoint.com/sites/SampleSite/_layouts/15/viewlsts.aspx?view=14.

> [!IMPORTANT]
> All columns detailed above must be present and can be blank if not needed.
  
![Spreadsheet view of SharePoint Migration Tool sample format when using a CSV file.](media/73fadfad-77ad-4d3a-b738-bc7063bc2659.jpg)
  
The following example shows how it would look if opened in a text editor.
  
```
C:\MigrationTests\testfiles,,,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder
https://sharepoint2013.com/sites/contosoteamsite/,DocumentLibraryName,DocLibrarySubfolder_name,https://contoso.sharepoint.com/sites/Sample/,DocLibraryName,DocLibraryName_subfolder
\\sharedfolder\homedrives\meganb,,,https://contoso-my.sharepoint.com/personal/meganb_contoso_com/,DocLibraryName,DocLibraryName_subfolder
```

## Use a JSON file for bulk upload

The following example shows the JSON file format that you can use to migrate your data.

The minimum required values are *SourcePath* and *TargetPath*.  

```json
{
  "Tasks": [
    {
      "SourcePath": "D:\\MigTest",
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

## Troubleshooting

### Proxy connections

Proxy connections aren't supported for either SharePoint or file share migrations. By default, SPMT doesn't use system proxy credentials and web requests fail if Internet Explorer proxy is configured. Examples of errors you may see include "SharePoint login fail" or "can't load document library". However, you can modify the SPMT app config file to follow your system proxy settings. 

If you wish to use your system proxy settings, use one of these methods:

**Update proxy** 

1. Download the latest version of SPMT. Start SPMT.
2. If SPMT doesn't connect to Microsoft 365, go to  **%localappdata%\Apps\SharePointMigrationTool\SPMT**.
3. Open the **microsoft.sharepoint.migrationtool.advancedapp.exe.config** file.
4. Uncomment the default proxy setting shown here:  
![Edit the config file to comment out the proxy setting](media/spmt-proxy-edits.png)  
5. Restart SPMT.

</br>

**If SPMT doesn't upgrade**

1. If SPMT can't upgrade itself, go to **%localappdata%\Apps\SharePointMigrationTool\InstallerClient.**
2. Open the **installclient.exe.config** file. 
3. Add the following configuration at line 31, just after the ```<appSettings></appSettings``` tag:  
![Edit the config file](media/spmt-proxy-edits.png)  
4. Launch installclient.exe and SPMT should auto-upgrade to latest SPMT release.
5. Open the **microsoft.sharepoint.migrationtool.advancedapp.exe.config** file.
6. Uncomment the default proxy setting:  
![Edit the config file to comment out the proxy setting](media/spmt-proxy-edits.png)  
5. Restart SPMT.

### Additional Errors

|Error|Description|
|:-----|:-----|
|**Destination site cannot associate to an invalid hub site**|This error occurs if the destination site is already registered as a hub site.  SPMT won't change the hub registration of a destination site.|
|**Destination site cannot associate to an invalid hub site**|This happens if you're attempting to associate with an invalid hub site. Check the URL and try again.|
|**Destination site associates with an existing hub, it cannot be changed during migration**| This error occurs if the destination site is already associated with a different hub.  SPMT won't change the association a destination site.|


