---
title: "How the SharePoint Migration Tool works"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 1/10/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.custom: Strat_SP_gtc
ms.assetid: 5b22e9e3-9548-442e-bf21-bd753b72bffa
description: "The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO). You do not have to be a global administrator to run the tool, only have write access to the site collection to where you are migrating the data."
---

# How the SharePoint Migration Tool works

The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO). You do not have to be a global administrator to run the tool, only have write access to the site collection to where you are migrating the data.
  
It is available to all Office 365 users.
  
> [!NOTE]
> The SharePoint Migration tool is available to all Office 365 users, with the exception of users of Office 365 operated by 21Vianet in China. 
  
Click here to download: [SharePoint Migration Tool](http://spmtreleasescus.blob.core.windows.net/install/default.md)
  
## How the SharePoint Migration Tool works

The following describes what is happening as you use the SharePoint Migration Tool. Authentication to the destination tenant occurs first, after which you are prompted for your sources and destination SPO site collections where you want the files migrated. After you submit your migration jobs by clicking **Migrate**, the scanning, packaging, uploading and importing steps are performed in parallel across all the files submitted for migration.
  
- **AUTHENTICATION:** After opening the tool, the first thing you must do is authenticate to the destination -- the tenant where you will be migrating your files. Providing your username and password to the tenant associates the migration jobs you submit to this account. This allows your to resume your migration from another computer if needed by logging in with the same credentials. This account should be a site collection administrator of the destination you want to migrate to. 
    
- **SCAN**: After you click **Migrate**, a scan is performed on every file. A scan is always performed, even if you elect to not migrate your files (see Advanced Settings). The scan verifies that there is access to the data source and write access to the SharePoint Online destination. It also scans the file for known potential issues.
    
- **PACKAGING:** In the packaging stage, a content package is created that contains a manifest consisting of 8 XMLs. 
    
- **UPLOAD:** In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from a SPO provided Azure container, the data is encrypted at rest using the AES CBC 256 standard. The files are encrypted along with the manifest files. 
    
- **IMPORT:** During the import phase, the key is provided to SPO SAS. Only Azure and SPO are interacting to fetch and migrate the content into the destination. This process is a timer job based, but does not prevent other jobs from being queued up. During the import, a report is created in the working folder and live updates are made. After the migration job is completed, the log is stored in the Azure container and a final report is created. A log is stored in each Manifest Container. 
    
## Encryption and security

During the upload and import phases, data is encrypted and Azure containers and keys are generated.
  
> [!IMPORTANT]
>  *No one has direct access to the storage accounts or the containers.*  The Sharepoint Online  *service*  has access to the storage accounts and a select number of engineers can run maintenance commands against them, but they do not have direct access to the accounts. Datacenter technicians are not prepped with knowledge of how data is laid out on disk, and do not have ready access to equipment to mount disks. All drives are physically destroyed before leaving the datacenter. Physical security is also in place across all of our datacenters. 
  
Each container is dedicated to the customer who it was provided to and not reused. The data is stored in the Azure blob anywhere from 30 to 90 days after which it is deleted. When the data is deleted, the files are de-linked and later soft deleted from disk. A file in an account and on-disk are may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data if it applies).
  
The default key to the container is generated programmatically, and is only valid for 3 days. This key is the  *only way to gain access to the container*  . It is generated randomly and not reused. 
  
The container itself lives longer than the key. The container is purged anywhere from 30-90 days from its creation date, using SharePoint Online standard methods. SharePoint Online never stores the key, though potentially they could find the container. The container is housed in a shared Microsoft storage, outside the tenant, but within the region, and is protected using the API key.
  
If your key is lost or obtained by someone else, there are two defenses in place that protect you. First, the container has only read/write operations. The container has no list, which means you would need to know the details of the files stored in the container in order to read or write to them. Secondly, the files are encrypted at rest with AES 256 in CBC mode.
  
> [!IMPORTANT]
> Only those who have the key have access. Other users in the subscription or the tenant do not have access. 
  

