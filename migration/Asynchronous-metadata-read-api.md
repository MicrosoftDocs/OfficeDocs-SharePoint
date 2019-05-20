---
title: "Migration Asynchronous Metadata Read API"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ROBOTS: NOINDEX, NOFOLLOW
ms.collection: 
- Strat_SP_gtc
- SPMigration
description: "Migration Asynchronous Metadata Read API"
---

# Migration Asynchronous Metadata Read API

> [!Important]
>This is a preliminary beta trial and not a full production release, hence not all features are tested and verified. Features are subject to change without notice.

 

## Overview
The goal of the new Migration Asynchronous Metadata Read API is to reduce the number of CSOM calls by 50% or more, reduce throttling, reduce the cost to the database, and improve overall migration performance. 
The new Migration Asynchronous Read API lets your tools perform a read operation of a provided URL. The Microsoft backend software then queries the database with the specified URL and its subdirectories aggregates all the information into a designated manifest. The ISV can read back from the manifest and parse the metadata without sending thousands of CSOM calls individually.


This document targets ISVs and any third party vendors/developers who is developing and maintaining migration tool.

### Background:
Currently, the SharePoint Online Migration API, CreateMigrationJob, lets your migration tool efficiently migrate large amounts data to SharePoint Online. However, the lack of an official API to read content from SharePoint Online means that these tools must rely on CSOM function calls to perform individual metadata read operations. 
</br>
Large numbers of CSOM calls increase the likelihood of throttling which impacts migration performance and customer experience. Ineffective CSOM usage results in large SQL round trip per function calls that can potentially bring down the database and impact its reliability.

A migration performance study identified four areas where CSOM calls are heavily used: 
- **Incremental migration** relies on CSOM calls to retrieve the SharePoint online (SPO) content. It compares it with source location to determine if there have been any changes to the content and whether to proceed with migration.  
- **Structure creation** leverages CSOM calls for site ,webpart and navigation creation.
- **After migration verification** is done when migration is completed and is used to ensure the source and destination file metadata matches.
- **Permission settings** are CSOM function calls made getting user permission information.

## Migration Asynchronous Metadata Read API

The migration asynchronous metadata read API aims to reduce the CSOM calls in areas: incremental migration, after migration verification and permission settings and potentially other use cases. 


The new Migration Asynchronous Read API is:</br>

   **public SPAsyncReadJobInfo CreateSPAsyncReadJob(Uri url, SPAsyncReadOptions options)**

The API is made up of two input parameters, a URL, an Optional Flag, and one output structure field. 
Currently, all items specified in the URL are queried. This often results in unnecessary reads and creates an extra load to the database especially if your migration tool only wants to know the delta (e.g. incremental migration).
To eliminate unnecessary reads, changeToken is being introduced.  It will read the metadata of specified duration. Only the objects specified in the changeToken range is read. ChangeToken will not be supported in the beta test release, but will be included in the first official release.

> [!Note]
>The Asynchronous Metadata Read API returns only metadata; no file or object transfer takes place.

## Input Parameters

### URL 
The URL lets your migration tool to specify the root URL path of the SharePoint objects to be read.  The server-side code will read and return all the metadata of subfolders, files, and lists of that root URL.

*Example:*</br></br> 
This document library URL: **<span><span>https://www.contoso.com/my-resource-document<span><span>**
will be read back for any files or folder that shares the same root URL, or supporting content.</br></br>
For **<span><span>https://www.contoso.com/my-resource-document/file1.doc<span><span>** or 
**<span><span>https://www.contoso.com/my-resource-document/folderA/file2.doc<span><span>**, only the root URL needs to be specified.  It is sent as a single read request.

> [!Note]
>The first version of the AsyncMigrationRead supports files, folders, lists, list items, and the document library. Permission are expected to be covered in second version. The third version will extend to cover webpart and potentially taxonomy. 

#### Corner Cases for URL

##### Unsupported Type
If an unsupported type is detected, the read operation for that URL will not be executed and an error information will be logged, but the rest of the supported URL will still be executed.

*Example:* 
In this example, URL A is the taxonomy and URL B is a file. 
URL A will fail with an error until we support taxonomy. The error will be logged, but URL B will be executed.

##### Duplication
If your migration tool passes duplicate URLs. 
Example:
In this example, URL A is link A and URL B is also link A. 
Given URL A and URL B are sent in two different packets, the server code will execute both despite the fact they both pointed to the same root URL. The user has the option to cancel the second job. 

##### Unidentified URL
If your migration tool passes an incorrect, NULL, or unidentified URL, an error will be generated for that URL.

##### No Content to Read back 
If the root site is empty and there is nothing to read back, the Asynchronous Read function will not return an error but no content will be recorded in the manifest.

##### Special Character 
If there are special characters in the URL, please use the escape character to circumvent the problem.

### Optional Flag 
The read asynchronous function will include the SPAsyncReadOptions structure which covers the optional flags to allow the user to specify version and security setting on the site level more is described below.

##### IncludeVersions 
{ get; set; }</br>
If set, this indicates all the files and list item version history is to be included in the export operation. If absent, only the default version is provided

##### IncludeSecurity
 { get; set; }</br>
This flag indicates whether to include all user or group information from a site. By default, it assumes the security is not set, hence no user or group information is provided.

### ChangeToken (TBD, not supported in first release)

The changeToken uses the same SharePoint changeToken.  In the official release, a range will be specified;  startChangeToken and endChangeToken. If Null, everything will be exported. ChangeToken can also be specified in past time ranges. This means both the start time and the end time needs to be less than the present time. If use in this format, the read asynchronous API will only read back the items that are specified within the time range.
More documentation will be provided one the feature is completed.


#### Corner Cases for ChangeToken
##### Invalid Time Format 
If an invalid time format is detected, other than NULL, an error will be generated, and the operation will be terminated. 

##### Invalid Time Range 
If Invalid time range is detected. For example, the user specified start time in past but end time in future, an error will be thrown and not read will take place.

#### Time Provided Larger than Present
If end time provided is larger than present time, an error is also expected to be generated and no content migration will take place.

## Output Parameters

AsyncMigrationRead is expected to return a list of fields including JobID of the unique URL, encryptionKey, azureContainerManifestUrl, and jobQueueUri in the SPAsyncReadJobInfo structure.

#### UniqueJobID
*public Guid JobId { get; set; }*</br>
The unique job associates with this asynchronous read request.  You migration tool will leverage this unique ID per URL for status check and to query the read process.

#### AzureContainerManifestUri
*public Uri ManifestContainerUri { get; set; }*</br>

The server code creates an azureContainer for the manifest . The manifest container Uri is included as a part of the return code. After the asyncMigrationRead function finishes execution, the final manifest will be placed in the container specified. 
Manifest export package structure will be like the createMigration Import Package structure. The general output structure is summarized in table below.

|**XML file**|**Schema File**|**Description**|
|:-----|:-----|:-----|
|ExportSettings.XML|DeploymentExportSettings Schema|ExportSettings.XML does the following:</br></br>- Contains the export settings specified by using the SPExportSettings class and other classes that are part of the content migration object model. </br></br>- Ensures that the subsequent export process (at the migration target site) enforces the directives specified in the export settings.</br></br>- Maintains a catalog of all objects exported to the migration package.|
|LookupListMap.XML|DeploymentLookupListMap Schema|Provides validation for the LookupListMap.XML file exported into the content migration package. LookupListMap.XML maintains a simple lookup list that records SharePoint list item (list item to list item) references.|
|Manifest.XML|DeploymentManifest Schema|Provides validation for the Manifest.xml file that is exported into the content migration package.Provides a comprehensive manifest containing listings of both the contents and the structure of the destination site (E.g. SPO) . |
|Requirements.XML|DeploymentRequirements Schema|"Provides validation for the Requirements.xml file exported into the content migration package. Requirements.xml maintains list of deployment requirements in the form of installation requirements on the migration target, such as feature definitions,  template versions, Web Part assemblies, and language packs."|
|RootObjectMap.XML|DeploymentRootObjectMap Schema|"Provides validation for the RootObjectMap.xml file exported into the content migration package.RootObjectMap.xml maintains a list of mappings of secondary (dependent) objects, which allows the import phase of the migration operation to correctly place the dependent objects relative to the locations of the root object mappings."|
|SystemData.XML|DeploymentSystemData Schema|Provides validation for the SystemData.xml file exported into the content migration package.SystemData.xml does the following: Collects a variety of low-level system data. Records the number and names of Manifest.xml files (in cases where the migration uses multiple manifests).|
|UserGroupMap.XML|DeploymentUserGroupMap Schema|Provides validation for the UserGroup.xml file exported into the content migration package. UserGroup.xml maintains a list of users and user security groups with respect to access security and permissions.|
|ViewFormsList.XML|DeploymentViewFormsList Schema|Provides validation for the ViewFormsList.xml file exported into the content migration package.ViewFormsList.xml maintains a list of Web Parts and tracks whether each is a view or form.|

#### JobQueueUri:
public Uri JobQueueUri { get; set; }
The reporting features is the same as createMigrationJob. Logging will be provided to track the status of the asynchronous read.  In additional, the log will provide an estimate number of items to be read per url after scan through the database and a rough estimate for your tools.
In terms of blob queue permission and settings, all access will be by default and the same as when the ISV called ProvisionMigrationContainer during the createMigrationJob.

#### EncryptionKey:
public byte[] EncryptionKey { get; set; }</br></br>
It returns the AES256CBC encryption key used to decrypt the message in azureManifest container and azureReport Queue.

|**Output parameter**|**Description**|
|:-----|:-----|
|JobID/GUID|Return a unique Job ID associated with this asynchronous read|
|AzureContainerManifest|Return the URL for accessing the async read manifest|
|JobQueueUri|URL for accessing Azure queue used for returning notification of migration job process|
|EncryptionKey|AES256CBC encryption key used to decrypt messages from job/manifest queue|

## Set up Guidelines
The following provides high level guidelines for implementing the asynchronous metadata migration function. This documentation does not go into details on how to interact with SharePoint RESTful service. It is assumed that the ISV has prior knowledge and will be able to access the target website with proper permission. </br>,</br>For more information on how to access the Sharepoint website, refer to [Get to Know the SharePoint Rest Service](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service).

1. Install and update the latest Microsoft.SharePointOnline.CSOM version. The minimum version requirement is V16.1.8600 or later.
2. ISVs figure out the folder, document library or files of interested to be query and issued with CreateSPAsyncReadJob function. 
3. Once successfully created, query the job status using the *jobQueueUri*. It provides the job process status and any error logging. After job completion, parse the Manifest to retrieve the metadata.


## Metadata Support

For the first release, a selected set of metadata will be provided for test purposes. We will be continually adding to the metadata fields that are available in the asynchronous read upon ISV feedback.

## Limitations
For the first release, the limits for all supported migration will cap at 1 million. The 1 million count includes items such as role assignment and alerts. The only exception is for multiple versions of a single file, which will count as one. More information will be provided in future update.</br>

By default, each URL supports up to 1 million limits. At the start of the migration, the asynchronous read migration function will check. If more than 1 million is detected an error will be thrown. Multiple versions of a single file will count as one. (More information will be provided in future update). 

**Asynchronous Read API Limitations**</br>


|**Type**|**SharePoint Online Limit**|**Recommended limit</br>for async read**|**Description**|
|:-----|:-----|:-----|:-----|
|Lists|30 million items|1 million|Per list URL, the migration read will process up to 1 million rea|
|Document Library|30 million files/folders|1 million|Per list URL, the migration job will process up to 1 million reads|
|Users|2 million per site collection|1 million|Per site collection. This is only supported in a future permission setting.|


## Performance Expectation
The preliminary performance test provides a rough estimate of 300-400 items per second throughput. This does not account for any potential throttle over the network. If the read asynchronous function fails to reach the server due to throttling, then performance will be impacted. 
At the start of read asynchronous migration, the server calculates the number of objects to confirm that it is within the 1 million object limit and can impact performance depending on the size of your migration. Hence the throughput for a small number of objects (e.g. 100 objects) is less than if 100,000 objects are migrated.


