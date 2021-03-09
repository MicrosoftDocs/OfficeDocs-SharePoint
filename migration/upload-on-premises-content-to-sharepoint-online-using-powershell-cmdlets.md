---
title: "Use PowerShell cmdlets to migrate on-premises content - SharePoint"
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
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
ms.assetid: 555049c6-15ef-45a6-9a1f-a1ef673b867c
description: "Learn how to use PowerShell cmdlets to migrate content from an on-premises file share to SharePoint in Microsoft 365."
---

# Upload on-premises content to SharePoint using PowerShell cmdlets

> [!NOTE]
>  The SharePoint Migration Tool (SPMT) helps simplify your migration process. SPMT provides a wizard-like experience to guide you through migrating SharePoint Server team sites or network file shares to Microsoft 365. It is available to all Microsoft 365 users:  [Download SPMT](https://spmtreleasescus.blob.core.windows.net/install/default.htm).
  
> [!IMPORTANT]
> The SharePoint Migration Tool isn't currently available for users of Office 365 operated by 21Vianet in China.
  
This article shows how to use SharePoint Migration PowerShell cmdlets to migrate content from an on-premises file share to Microsoft 365.
  
SharePoint Migration PowerShell cmdlets are designed to move on-premises content from file shares. They require minimal CSOM calls and use Azure temporary Blob Storage to handle large migrations of data.
  
  
## Prerequisites

- Supported operating systems:
    - Windows 7 Service Pack 1
    - Windows 8
    - Windows Server 2008 R2 SP1
    - Windows Server 2008 Service Pack 2
    - Windows Server 2012, Windows Server 2012 R2
    
- Windows PowerShell 4.0
    
> [!NOTE]
> Permissions: You must be a site collection administrator on the sit that you're targeting.
  
## Before you begin

- Provision your Microsoft 365 setup with your existing active directory or one of the other options for adding accounts to Microsoft 365. For more information, see [Microsoft 365 integration with on-premises environments](https://go.microsoft.com/fwlink/?LinkID=616610&amp;clcid=0x409) and [Add users and assign licenses at the same time](https://go.microsoft.com/fwlink/?LinkID=616611&amp;clcid=0x409). 
    
- Install the SharePoint Online Management Shell and set up your working directory.
    
## Step 1: Install the SharePoint Online Management Shell
<a name="Step1InstallShell"> </a>

1. Uninstall all previous versions of the SharePoint Online Management Shell.
    
2. [Download](https://go.microsoft.com/fwlink/?LinkID=617148&amp;clcid=0x409) and install SharePoint Online Management Shell.
    
3. Open **SharePoint Online Management Shell**, and select **Run as Administrator**.
  
## Step 2: Set up your working directory
<a name="Step2Setupworkingdir"> </a>

Before you start the migration, you need to set up your working directory with two empty folders. These folders don't need much disk space, as they'll only contain XML.
  
1. Create a temporary package folder.
    
2. Create a final package folder.
  
## Step 3: Determine locations and credentials
<a name="Step3loccredentials"> </a>

Identify your credentials and the locations of your source files, target files, and web.
  
On your local computer, open SharePoint Online Management Shell. Run the following commands, but insert your values:

```powershell
$cred = (Get-Credential admin@contoso.com)
$sourceFiles = '\\fileshare\users\charles'
$sourcePackage = 'C:\migration\CharlesDocumentsPackage_source'
$targetPackage = 'C:\migration\CharlesDocumentsPackage_target'
$targetWeb = 'https://contoso-my.sharepoint.com/personal/charles_contoso_com'
$targetDocLib = 'Documents'

New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $sourcePackage -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib -IgnoreHidden -ReplaceInvalidCharacters
```
  
## Step 4: Create a new content package from an on-premises file share
<a name="step4createpackage"> </a>

In this step, you create a new migration package from a file share. To create a content package from a file share, the  `New-SPOMigrationPackage` command reads the list of content targeted by the source path and generates XML to do the migration.
  
The following parameters are required unless marked optional:
  
- *SourcefilesPath*: Points to the content you plan to migrate.
    
- *OutputPackagePath*: Points to your Temporary folder.
    
- *TargetWebUrl*: Points to your destination web.
    
- *TargetDocumentLibraryPath*: Points to the document library inside the web.
    
- *IgnoreHidden*: Skip hidden files *(optional)*.
    
- *ReplaceInvalidCharacters*: Fix invalid characters when possible *(optional)*.
    
 **Example:**
  
The following example shows how to create a new package from a file share. It ignores hidden files and replaces unsupported characters in file/folder names.
  
```powershell
    New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $sourcePackage -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib -IgnoreHidden -ReplaceInvalidCharacters`
```
  
## Step 5: Convert the content package for your target site
<a name="step5convertpackage"> </a>

Use the `ConvertTo-SPOMigrationTargetedPackage`  command to convert the SML generated in your temporary folder. It saves a new set of targeted migration package metadata files to the target directory. This is the final package.
  
> [!NOTE]
> Your target site collection administrator credentials are used to gather data to connect to the data site collection.
  
There are six required parameters to enter (others are optional):
  
- *ParallelImport*: Instructs the tool to use parallel thread optimize performance.
    
- *SourceFiles*: Points to the directory location of the package's source content files.
    
- *SourcePackagePath*: Points to your temporary package folder.
    
- *OutputPackagePath*: Points to your final package folder.
    
- *Credentials*: SharePoint credential that has admin rights to the destination site.
    
- *TargetWebUrl*: URL of your destination web.
    
- *TargetDocumentLibraryPath*: Path to your destination library.
    
 **Example:**
  
This example shows how to convert a package to a targeted one by looking up data in the target site collection. To boost file share migration performance, it uses the *-ParallelImport* parameter.
  
```powershell
$finalPackages = ConvertTo-SPOMigrationTargetedPackage -ParallelImport -SourceFilesPath $sourceFiles -SourcePackagePath $sourcePackage -OutputPackagePath $targetPackage -Credentials $cred -TargetWebUrl $targetWeb -TargetDocumentLibraryPath $targetDocLib`
```
  
## Step 6: Submit content to import
<a name="step6submitimport"> </a>

In this step, the `Invoke-SPOMigrationEncryptUploadSubmit` command creates a new migration job in the target site collection and then returns a GUID that represents the JobID. This command uploads encrypted source files and manifests into temporary Azure Blob Storage per job.
  
There are four required parameters to enter. Others are optional.
  
- *TargetwebURL*: Points to the web of the destination.
    
- *SourceFilesPath*: Points to the files to import.
    
- *SourcePackagePath*: Points to the final manifest of the files to import.
    
- *Credentials*: The SharePoint credentials that have Site Collection Administrator rights to the destination site.
    
 **Example 1:**
  
This example shows how to submit package data to create a new migration job.
  
```powershell
 $job = Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $sourceFiles -SourcePackagePath $targetPackage -Credentials $cred -TargetWebUrl $targetWeb
```
  
 **Example 2:**
  
This example shows how to submit package data to create new migration jobs for parallel import.

```powershell  
$jobs = $finalPackages | % {Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $_.FilesDirectory.FullName -SourcePackagePath $_.PackageDirectory.FullName -Credentials $cred -TargetWebUrl $targetWeb}
```
  
For each submitted job, the `Invoke` cmdlet returns these properties as part of a job:
  
- *JobId*: ID of the job in SPO.
    
- *ReportingQueueUri*: SharePoint Azure queue that stores the real-time progress messages of the migration.
    
- *Encryption*: Encryption key and method used for uploading the content to Azure. This key is required when you decrypt the queue messages and import logs.
    
If you're using your own Azure Storage account to upload content into your storage, use *Set-SPOMigrationPackageAzureSource*  and  *Submit-SPOMigrationJob*.

>[!Important]
>If you choose to use your Azure Storage, you could incur Bandwidth charges. Charged would depend on your Azure offer type and migration size. For general prices, refer to [bandwidth pricing](https://azure.microsoft.com/pricing/details/bandwidth/).
 
## *(Optional)* Step 7: Process and monitor your SharePoint migration
<a name="step7monitoring"> </a>

After the job is submitted, only Azure and SharePoint interact to fetch and migrate the content to the destination. This process is timer-job based, which means it's in a queue on a first-come, first-served basis. This process doesn't prevent the same person from queuing other jobs.
  
If no other jobs running are running, there may be a 1-minute delay.
  
### Check job status

To check the status of your job, use the *EncryptionKey* returned in step 6 to view the real-time updates posted in the Azure Storage account.
  
### View logs

If you're using your own Azure Storage account, you can view logs of everything that happened in the manifest container in the Azure Storage. At this stage, it's safe to delete those containers, if you don't want to keep them as backup in Azure.
  
If there were errors or warnings, *.err* or *.won* files are created in the manifest container. 
  
If you're using the temporary Azure Storage created by  *Invoke-SPOMigrationEncryptUploadSubmit* in step 6, you can get the import log SAS URL by decrypting the Azure queue message with the "Event" value *JobLogFileCreate*. You can use the import log SAS URL to download the log file and decrypt it with the encryption key returned in step 6.
  
## Scripting scenarios for reuse
<a name="step7monitoring"> </a>

Use the following sample script. It includes the steps from determining your locations and credentials, to submitting your package data, to creating a new migration job.
  
```powershell
$userName = "admin@contoso.onmicrosoft.com"
$sourceFiles = "d:\data\documents"
$packagePath = "d:\data\documentPackage"
$spoPackagePath = "d:\data\documentPackageForSPO"
$targetWebUrl = "https://contoso.sharepoint.com/sites/finance"
$targetLibrary = "Documents"
$cred = Get-Credential $userName
  
New-SPOMigrationPackage -SourceFilesPath $sourceFiles -OutputPackagePath $packagePath -TargetWebUrl $targetWebUrl -TargetDocumentLibraryPath $targetLibrary -IgnoreHidden -ReplaceInvalidCharacters
```

## Convert the package to a targeted one by looking up data in target site collection

```powershell  
$finalPackages = ConvertTo-SPOMigrationTargetedPackage -SourceFilesPath $sourceFiles -SourcePackagePath $packagePath -OutputPackagePath $spoPackagePath -TargetWebUrl $targetWebUrl -TargetDocumentLibraryPath $targetLibrary -Credentials $cred
```
  
## Submit the package data to create the migration job

```Powershell   
$job = Invoke-SPOMigrationEncryptUploadSubmit -SourceFilesPath $sourceFiles -SourcePackagePath $spoPackagePath -Credentials $cred -TargetWebUrl $targetWebUrl
  
This sample shows how to get the returned information of a job, which comes in the form of a GUID.
  
```powershell
$job = $jobs[0]
$job.JobId
Guid
----
779c4b3b-ec24-4705-bb58-c38f4329418c
```

This sample shows how to get the *$job.ReportingQueueURi.AbosoluteUri*.
  
```powershell
# To obtain the $job.ReportingQueueUri.AbsoluteUri
https://spodm1bn1m013pr.queue.core.windows.net/953pq20161005-f84b9e51038b4139a179f973e95a6d6f?sv=2014-02-14&amp;sig=TgoUcrMk1Pz8VzkswQa7owD1n8TvLmCQFZGzyV7WV8M%3D&amp;st=2016-10-04T07%3A00%3A00Z&amp;se=2016-10-26T07%3A00%3A00Z&amp;sp=rap
```

This sample shows how to obtain the encryption key and the sample return.
  
```powershell
$job.Encryption
EncryptionKey                                       EncryptionMethod
-----------------------                            ------------------
{34, 228, 244, 194...}                              AES256CBC

```

> [!IMPORTANT]
> All messages are encrypted in the queue. To read from the *ReportingQueue*, you must have the *EncryptionKey*. 
  
## Best practices and limitations
<a name="step7monitoring"> </a>

|**Description** |**Recommendation**|
|:-----|:-----|
|Package size  |10-20 GB  <br/> Use the *-ParallelImport* switch for file share migration, which automatically splits the large package into smaller ones. |
|File size  <br/> |2 GB  <br/> |
|Target size  <br/> |The target site should remain non-accessible to users until migration is complete |
|SharePoint limits  <br/> |[Service limits in SharePoint for Microsoft 365](https://go.microsoft.com/fwlink/?LinkID=616612&amp;clcid=0x409)|
   
## Azure limits
<a name="step7monitoring"> </a>

| Resource | Default/Limit |
|:-----|:-----|
|TB per storage account  <br/> |500<br/> |
|Max size of single blob container, table, or queue.  <br/> |500  |
|Max number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account.  <br/> |The only limit is the 500-TB storage account capacity.  <br/> |
|Target throughput for single blob  <br/> |Up to 60 MB or 500 requests per second.  <br/> |
   
## Related articles
<a name="step7monitoring"> </a>

[Cmdlet references are for SharePoint Online](https://go.microsoft.com/fwlink/p/?LinkID=717917)
  