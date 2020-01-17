---
title: "Upload on-premises content to SharePoint Online using PowerShell cmdlets"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.custom: 
ms.assetid: 555049c6-15ef-45a6-9a1f-a1ef673b867c
description: ""
---

# Upload on-premises content to SharePoint Online using PowerShell cmdlets

> [!NOTE]
>  *January 10, 2018* > The **SharePoint Migration Tool** is now available to help simplify your migration process. This new tool provides a wizard-like experience to guide you through the process of migrating either your SharePoint on-premises document libraries or your on-premises file shares and move them to either SharePoint or OneDrive in Office 365. It is available to all Office 365 users. > To download the tool, go here: [SharePoint Migration Tool](https://spmtreleasescus.blob.core.windows.net/install/default.htm)
  
> [!IMPORTANT]
> Currently the SharePoint Migration Tool is not available for users of Office 365 operated by 21Vianet in China. 
  
This is a step by step guide on how to use the SharePoint Online Migration PowerShell cmdlets to migrate content from an on-premises file share to Office 365.
  
SharePoint Online Migration PowerShell cmdlets are designed to move on-premises content from file shares. Requiring minimal CSOM calls, it leverages Azure temporary BLOB storage to scale to the demand of large migration of data content.
  
Here are the steps for using SPO Migration powershell to upload your on-premises data into SharePoint Online:
  
[Step 1: Install the SharePoint Online Management Shell](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#Step1InstallShell)
  
[Step 2: Setup your working directory](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#Step2Setupworkingdir)
  
[Step 3: Determine your locations and credentials](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#Step3loccredentials)
  
[Step 4: Create a new content package from an on-premises file share](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#step4createpackage)
  
[Step 5: Convert the content package for your target site](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#step5convertpackage)
  
[Step 6: Submit content to import](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#step6submitimport)
  
[(Optional) Step 7: Processing and Monitoring your SPO Migration](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md#step7monitoring)
  
## Prerequisites

- Supported Operating Systems: Windows 7 Service Pack 1, Windows 8, Windows Server 2008 R2 SP1, Windows Server 2008 Service Pack 2, Windows Server 2012, Windows Server 2012 R2
    
- Windows PowerShell 4.0
    
> [!NOTE]
> Permissions: You must be a site collection administrator on the site you are targeting. 
  
## Before you begin

- Provision your Office 365 with either your existing active directory or one of the other options for adding accounts to Office 365. See See [Office 365 integration with on-premises environments](https://go.microsoft.com/fwlink/?LinkID=616610&amp;clcid=0x409) and [Add users to Office 365 for business](https://go.microsoft.com/fwlink/?LinkID=616611&amp;clcid=0x409) for more information. 
    
- Install the SharePoint Online Management Shell and set up your working directory.
    
## Step 1: Install the SharePoint Online Management Shell
<a name="Step1InstallShell"> </a>

The first step is install the SharePoint Online Management shell.
  
1. Uninstall all previous versions of the SharePoint Online Management Shell.
    
2. Install from here: [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?LinkID=617148&amp;clcid=0x409).
    
3. Open **SharePoint Online Management Shell** and select **Run as Administrator**.
    
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Step 2: Setup your working directory
<a name="Step2Setupworkingdir"> </a>

Before you start the migration process, you need to setup your working directory by creating two empty folders. These folders to not require a lot of disk space as they will only contain XML.
  
1. Create a Temporary package folder.
    
2. Create a Final package folder.
    
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Step 3: Determine your locations and credentials
<a name="Step3loccredentials"> </a>

In this step you need to identify your locations and credentials, including the location of your source files, target files and web location.
  
On your local computer, open the SharePoint Online Management Shell. Run the following commands substituting your values.

```Powershell
$cred = (Get-Credential admin@contoso.com)
$sourceFiles = '\\fileshare\users\charles'
$sourcePackage = 'C:\migration\CharlesDocumentsPackage_source'
$targetPackage = 'C:\migration\CharlesDocumentsPackage_target'
$targetWeb = 'https://contoso-my.sharepoint.com/personal/charles_contoso_com'
$targetDocLib = 'Documents'

New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $sourcePackage -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib -IgnoreHidden -ReplaceInvalidCharacters
```
  
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Step 4: Create a new content package from an on-premises file share
<a name="step4createpackage"> </a>

In this step, you will create a new migration package from a file share. To create a content package from a file share, the  *New-SPOMigrationPackage*  command reads the list of content targeted by the source path and will generate XML to perform migration. 
  
The following parameters are required unless marked optional:
  
- SourcefilesPath: points to the content you want to migrate
    
- OutputPackagePath: points to your Temporary folder
    
- TargetWebUrl: point to your destination web
    
- TargetDocumentLibraryPath: point to the document library inside the web.
    
- IgnoreHidden: option to skip hidden files (optional)
    
- ReplaceInvalidCharacters: will fix invalids characters when possible (optional)
    
 **Example:**
  
This example shows how to create a new package from a file share, ignoring hidden files and replacing unsupported characters in a file/folder name.
  
```Powershell
    New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $sourcePackage -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib -IgnoreHidden -ReplaceInvalidCharacters`
```
  
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Step 5: Convert the content package for your target site
<a name="step5convertpackage"> </a>

After you have created the content package, use the  *ConvertTo-SPOMigrationTargetedPackage*  command to convert the xml generated in your temporary folder. It saves a new set of targeted migration package metadata files to the target directory. This is the final package. 
  
> [!NOTE]
> Your target site collection administrator credentials are used to gather data to connect to the data site collection. 
  
There are six required parameters to enter (others are optional
  
- ParallelImport : Tell the tool to optimise performance by using parallel threads.
    
- SourceFiles: points to the directory location where the package's source content files exist
    
- SourcePackagePath: points to your Temporary package folder
    
- OutputPackagePath: points to your final package folder
    
- Credentials: SPO credential that has admin rights to the destination site
    
- TargetWebU﻿rl: point to your destination web
    
- TargetDocumentLibraryPath: the path to your destination library
    
 **Example:**
  
This example shows how to convert a package to a targeted one by looking up data in the target site collection. It uses the -ParallelImport parameter to boost file share migration performance.
  
```Powershell
$finalPackages = ConvertTo-SPOMigrationTargetedPackage -ParallelImport -SourceFilesPath $sourceFiles -SourcePackagePath $sourcePackage -OutputPackagePath $targetPackage -Credentials $cred -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib`
```
  
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Step 6: Submit content to import
<a name="step6submitimport"> </a>

In this step, the  `Invoke-SPOMigrationEncryptUploadSubmit` command creates a new migration job in the target site collection, and then returns a GUID representing the JobID. This command will upload encrypted source files and manifests into temporary Azure blob storage per job. 
  
There are four required parameters to enter (others are optional):
  
- TargetwebURL: Points to the web of the destination
    
- SourceFilesPath : Points to the files to import
    
- SourcePackagePath : Points to the final manifest of the files to import
    
- Credentials: The SharePoint Online credentials that have Site Collection Administrator rights to the destination site
    
 **Example 1:**
  
This example shows how to submit package data to create a new migration job.
  
```Powershell
 $job = Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $sourceFiles -SourcePackagePath $targetPackage -Credentials $cred -TargetWebUrl $targetWeb
```
  
 **Example 2:**
  
This example shows how to submit package data to create new migration jobs for parallel import.
```Powershell  
$jobs = $finalPackages | % {Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $_.FilesDirectory.FullName -SourcePackagePath $_.PackageDirectory.FullName -Credentials $cred -TargetWebUrl $targetWeb}
```

  
For each submitted job, the Invoke cmdlet returns these properties as part of a job:
  
- JobId: the ID of the job in SPO
    
- ReportingQueueUri: the SPO Azure queue that stores the real-time progress messages of the migration.
    
- Encryption: The encryption key and method used during uploading the content to Azure. This is required when you decrypt the queue messages and import logs.
    
If you're using your own Azure storage account, then use  *Set-SPOMigrationPackageAzureSource*  and  *Submit-SPOMigrationJob*  to upload content into your storage. 
  
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## (Optional) Step 7: Processing and Monitoring your SPO Migration
<a name="step7monitoring"> </a>

After the job is submitted, only Azure and SPO are interacting to fetch and migrate the content into the destination. This process is timer-job based, which means it's in a queue on a first come first served basis. This does not prevent other jobs from being queued up by the same person.
  
There is a potential of a 1 minute delay if there are no other jobs running.
  
### Checking job status

You can check the status of your job by viewing the real time updates posted in the Azure storage account queue by using the Encryption.EncryptionKey returned in step 6.
  
### Viewing logs

If you're using your own Azure storage account, you can look into the manifest container in the Azure Storage for logs of everything that happened. At this stage, it is now safe to delete those containers if you don't want to keep them as backup in Azure.
  
If there were errors or warnings, **.err** and **.wrn** files will be created in the manifest container. 
  
If you're using the temporary Azure storage created by  *Invoke-SPOMigrationEncryptUploadSubmit*  in step 6, the import log SAS URL can be obtained by decrypting the Azure queue message with the "Event" value "JobLogFileCreate". With the import log SAS URL, you can download the log file and decrypt it with the same encryption key as returned in Step 6. 
  
[Upload on-premises content to SharePoint Online using PowerShell cmdlets](upload-on-premises-content-to-sharepoint-online-using-powershell-cmdlets.md)
  
## Scripting Scenarios for Reuse
<a name="step7monitoring"> </a>

The following is a sample script you can use that includes the complete steps from determining your locations and credentials to submitting your package data to create a new migration job.
  
```Powershell
$userName = "admin@contoso.onmicrosoft.com"
$sourceFiles = "d:\data\documents"
$packagePath = "d:\data\documentPackage"
$spoPackagePath = "d:\data\documentPackageForSPO"
$targetWebUrl = "https://contoso.sharepoint.com/sites/finance"
$targetLibrary = "Documents"
$cred = Get-Credential $userName
  
New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $packagePath -TargetWebUrl $targetWebUrl -TargetDocumentLibraryPath $targetLibrary -IgnoreHidden -ReplaceInvalidCharacters
```

## Convert package to a targeted one by looking up data in target site collection

```Powershell  
$finalPackages = ConvertTo-SPOMigrationTargetedPackage -SourceFilesPath $sourceFiles -SourcePackagePath $packagePath -OutputPackagePath $spoPackagePath -TargetWebUrl $targetWebUrl -TargetDocumentLibraryPath $targetLibrary -Credentials $cred
```
  
## Submit package data to create new migration job
  
$job = Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $sourceFiles -SourcePackagePath $spoPackagePath -Credentials $cred -TargetWebUrl $targetWebUrl
  
This sample shows how to get the returned information of a job, which comes in the form of a GUID.
  
```Powershell
$job = $jobs[0]
$job.JobId
Guid
----
779c4b3b-ec24-4705-bb58-c38f4329418c
```

This sample shows how to get the $job.ReportingQueueURi.AbosoluteUri.
  
```Powershell
# To obtain the $job.ReportingQueueUri.AbsoluteUri
https://spodm1bn1m013pr.queue.core.windows.net/953pq20161005-f84b9e51038b4139a179f973e95a6d6f?sv=2014-02-14&amp;sig=TgoUcrMk1Pz8VzkswQa7owD1n8TvLmCQFZGzyV7WV8M%3D&amp;st=2016-10-04T07%3A00%3A00Z&amp;se=2016-10-26T07%3A00%3A00Z&amp;sp=rap
```

This sample demonstrates how to obtain the encryption key and the sample return.
  
```Powershell
$job.Encryption
EncryptionKey                                       EncryptionMethod
-----------------------                            ------------------
{34, 228, 244, 194...}                              AES256CBC

```

> [!IMPORTANT]
> All messages are encrypted in the queue. If you want to read from the ReportingQueue, you must have the EncryptionKey. 
  
## Best Practices and Limitations
<a name="step7monitoring"> </a>

|||
|:-----|:-----|
|**Description** <br/> |**Recommendation** <br/> |
|Package size  <br/> |10-20 GB  <br/> Use -ParallelImport switch for File Share migration which will automatically split the big package into smaller ones.  <br/> |
|File size  <br/> |2 GB  <br/> |
|Target size  <br/> |Target site should remain non-accessible to users until migration is complete  <br/> |
|SharePoint Online limits  <br/> |[SharePoint Online and OneDrive for Business: software boundaries and limits](https://go.microsoft.com/fwlink/?LinkID=616612&amp;clcid=0x409)SharePoint Online: software boundaries and limits  <br/> |
   
## Azure Limits
<a name="step7monitoring"> </a>

|||
|:-----|:-----|
|**Resource** <br/> |**Default/Limit** <br/> |
|TB per storage account  <br/> |500 TB  <br/> |
|Max size of single blob container, table, or queue  <br/> |500 TB  <br/> |
|Max number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account  <br/> |Only limit is the 500 TB storage account capacity  <br/> |
|Target throughput for single blob  <br/> |Up to 60 MB per second, or up to 500 requests per second  <br/> |
   
## Related Topics
<a name="step7monitoring"> </a>

[Use Windows PowerShell cmdlets for SharePoint Online and OneDrive Migration](https://go.microsoft.com/fwlink/p/?LinkID=717917)
  

