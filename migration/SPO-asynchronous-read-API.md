---
title: "Migration Asynchronous Read API"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: Overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Strat_SP_gtc
- SPMigration
search.appverid: MET150
ms.custom: 
description: "This article explains the SharePoint Migration asynchonrous read API that allows the SPMT/third party tools to perform a read operation of a provided URL. "
---
## Overview
Sharepoint Online Migration API CreateMigrationJob has allowed the SPMT/ third party tools to move large migration data to Sharepoint Online at an efficient pace. However, lack of official API to read content from Sharepoint Online means the SPMT/third party tools rely on CSOM function calls to perform individual read operations. Large number of CSOM calls increase the likelihood of throttling which impacts migration performance and customer experience. Furthermore, ineffective CSOM usage results in large SQL round trip per function call and can potentially bring down the database impacting the database reliability.
A migration performance study was done and identified three areas where CSOM calls are heavily used: incremental migration, after migration verification and permission setting.
 
1.	Incremental migration relies on CSOM calls to retrieve the Sharepoint online (SPO) content and compare with source location to determine whether there had been any changes to the content and whether to proceed with migration.  
2.	After migration verification is done when migration is completed and is used to ensure the source and destination file metadata matches.
3.	Permission setting are CSOM function calls made either getting user permission information.

The goal of the new migration asynchronous read API is to reduce the number of CSOM calls by 50% , reduce throttling and to improve overall migration performance.

Please note, this is a preliminary beta trial and not a full production release, hence not all features are tested and verified.
 
## Migration Asynchronous Read API
The asynchonrous read API allows the SPMT/third party tools to perform a read operation of a provided URL. The Microsoft server then queries Sharepoint Online with the specified URL and its subdirectories aggregates all the information into designated manifest container specified by the SPMT/third-party tools. This eliminates thousands of CSOM calls sent individually to retrieve a root folder metadata information.

By default, all the item specified in the URL will be queried. This may incur unnecessary read and create extra load to the database especially if SPMT/third-party tool are performing incremental migration.  To eliminate unnecessary read, changeToken is introduced to read metadata of Sharepoint objects if the modified date is larger than the one provided by the changeToken. (Please note for first release, change Token is not supported)

The new migration asynchronous read API is shown below: 

```xml
public SPAsyncReadJobInfo CreateSPAsyncReadJob(Uri url, SPAsyncReadOptions options)
```

The API is made up of two input parameters url,  and an Optional Flag  and one output structure field.  Details breakdown arecovered below.

### Input Parameters

#### URL 
The URL allows SPMT or third party tools to specify the root URL path of the Sharepoint objects to be read.  The server side code will read and return all the subfolder/files/list of that root URL.

For example, if a document library URL is https://www.contoso.com/my-resource-document/, any files or folders share the same root URL, their individual URLs will look like https://www.contoso.com/my-resource-document/file1.doc or https://www.contoso.com/my-resource-document/folderA/file2.doc. Only the root url needs to be specified and it should be sent as a single request.

In terms of coverage, for the first version of the asyncMigrationRead covers the File/folder, list/list item and document library. Permission are expected to be covered in second version. The third version will extend to cover webpart and potentially taxonomy.
 
#### Corner Cases for URL
 
##### Unsupported Type
If unsupported type is detected, the read operation for that URL will not be executed and an error information will be logged, but the rest of the supported URL will still be executed.
For example, url_a= taxonomy and url_b = file. url_a will fail with an error until we start support taxonomy and the error will be logged to the log, but url_b , it will be executed.

##### Duplication
If SPMT/third-party tools pass duplicated URLs. For example url_a = link_a and url_b= link_a . Given url_a and url_b are sent in two different packet, the server code will execute both despite the fact they both pointed to the same root url. User has the option to cancel the second job if desired. 

##### Unidentified URL
If the SPMT or third-party tools pass incorrect, NULL or unidentified URL, then an error will be thrown for that URL.

##### No Content to Read back 
If the root site is empty and there is nothing to read back. The asyn read function will still return with good status but no content will be recorded in the manifest 

#### Optional Flag 

The read async function will include the SPAsyncReadOptions structure which covers the optional flags to allow the user to specify version and security setting on the site level more is described below.

##### IncludeVersions { get; set; }

If set, this indicates all the files/list item version history to be included in the export operation. If absent then only the default version is provided

##### IncludeSecurity { get; set; }

This flag indicates whether to include all user/group information from a site. By default, it assumes the security is not set, hence no user/group information is provided.

#### ChangeToken(TBD, do not support in the first release)
The changeToken takes in a DateTime parameter. If specified, only the modified date larger than the ChangeToken will be exported. If Null, everything will be exported. To keep consistency, dateTime will be based on UTC time. The change token will be compared based off the last modified time of an object type (e.g. file/folder or list item). If last modified time attribute is not supported, the object will be read by default.

### Corner Cases for ChangeToken

#### Invalid Time Format 
If Invalid time format is detected, other than NULL, an error will be thrown and then operation will be terminated. 
Time Provided Larger than Present
If current time provided is larger than present time, an error is also expected to be thrown and no content migration will take place.

## Output Parameters

*asyncMigrationRead* is expected to return a list of fields including job ID of the unique URL, encryptionKey, azureContainerManifstUrl, and azureReportUri including in the SPAsyncReadJobInfo structure.

#### UniqueJobID

public Guid JobId { get; set; }

The unique job associates with this asynchronous read request. SPMT/third party tools leverage this unique ID per URL for status check and to query the read process. 

#### AzureContainerManifestUri

public Uri ManifestContainerUri { get; set; }
The server code creates an azureContainer for the manifest . The manifest container Uri is included as a part of the return code. After the asyncMigrationRead function finishes execution, the final manifest will be placed in the container specified. 
Manifest export package structure will be similar to createMigration Import Package structure. 

The general output structure is summarized in table below.

|**XML file**|**Schema File**|**Description**|
|:-----|:-----|:-----|
|ExportSettings.XML|DeploymentExportSettings Schema|ExportSettings.XML does the following: </br>Contains the export settings specified by using the SPExportSettings class and other classes that are part of the content migration object model. </br>Ensures that the subsequent export process (at the migration target site) enforces the directives specified in the export settings.</br>Maintains a catalog of all objects exported to the migration package.|
|LookupListMap.XML|DeploymentLookupListMap Schema|Provides validation for the LookupListMap.XML file exported into the content migration package. LookupListMap.XML maintains a simple lookup list that records SharePoint list item (list item to list item) references.|
|Manifest.XML|DeploymentManifest Schema|Provides validation for the Manifest.xml file that is exported into the content migration package.Provides a comprehensive manifest containing listings of both the contents and the structure of the destination site (E.g. SPO) . |
|Requirements.XML|DeploymentRequirements Schema|Provides validation for the Requirements.xml file exported into the content migration package. Requirements.xml maintains list of deployment requirements in the form of installation requirements on the migration target, such as feature definitions, template versions, Web Part assemblies, and language packs.|
|RootObjectMap.XML|DeploymentRootObjectMap Schema|Provides validation for the RootObjectMap.xml file exported into the content migration package.RootObjectMap.xml maintains a list of mappings of secondary (dependent) objects, which allows the import phase of the migration operation to correctly place the dependent objects relative to the locations of the root object mappings.|
|SystemData.XML|DeploymentSystemData Schema|Provides validation for the SystemData.xml file exported into the content migration package.SystemData.xml does the following: Collects a variety of low-level system data. Records the number and names of Manifest.xml files (in cases where the migration uses multiple manifests).|
|UserGroupMap.XML|DeploymentUserGroupMap Schema|Provides validation for the UserGroup.xml file exported into the content migration package. UserGroup.xml maintains a list of users and user security groups with respect to access security and permissions.|
|ViewFormsList.XML|DeploymentViewFormsList Schema|Provides validation for the ViewFormsList.xml file exported into the content migration package.ViewFormsList.xml maintains a list of Web Parts and tracks whether each is a view or form.|

### AzureQueueReportUri

```xml
public Uri JobQueueUri { get; set; }

```

The reporting features is the same as createMigrationJob. Logging will be provided to track the status of the asynchronous read.  In additional, the log will provide an estimate number of items to be read per url after scan through the database and a rough estimate for SPMT/third party tools.

### EncryptionKey
```xml
public byte[] EncryptionKey { get; set; }

```
It returns the AES256CBC encryption key used to decrypt the message in azureManifest container and azureReport Queue.

#### Other functions
Aside from asyncMigrationRead, two additional functions are provided to support the new features: deleteMigrationJob and getReadAsyncStatus.

*deleteMigrationJob(GUID readID)*

The existing deleteMigrationJob will also be used to delete any pending read request.  SPMT/third party tools pass the unique GUID per asyncMigrationRead. The same implementation details as published.

*getReadAsyncStatus(GUID readID)*

getReadAsyncStatus allows the SPMT/third party tools to query the asyncReadstatus for the specified read GUID. SPMT/third party tools should only query getReadAsyncStatus if no progress is received through the azureQueueReportUri or no azureQueueReportUri is defined. This function serves as a backup and provided minimal job status (e.g. job started, job in progress and job completed).

## Metadata Support
In the first release, the asynchronous read manifest would support similar metadata output as export-spweb. As previously mentioned, the first migration coverages include file, folder, list/document library and list items. 
 

## Limitation

For the first release, the limits for all supported migration will cap at 1 million.  For performance reasons, do not migrate more than 1 million of the table. 

|**Type**|**SharePoint Online Limit**|**Recommended async read limit**|**Description**|
|:-----|:-----|:-----|:-----|
|Lists|30 million items|1 million|Per list URL, the migration read will process up to 1 million read|
|Document library|30 million files/folders|1 million|
|Users|2 million per site collection|1 million|Per site collections.  This only applies/spports fo future permission setting|
