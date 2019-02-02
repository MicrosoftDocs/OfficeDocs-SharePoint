---
title: "How the SharePoint Migration Tool works"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
search.appverid:
- MET150
ms.custom: 
ms.assetid: 5b22e9e3-9548-442e-bf21-bd753b72bffa
description: "The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO). 
---

# How the SharePoint Migration Tool works

The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO).

> [!NOTE]
> The SharePoint Migration tool is available to all Office 365 users, with the exception of users of Office 365 operated by 21Vianet in China.

>[!NOTE]
>To install the current release download here: [SharePoint Migration Tool](http://spmtreleasescus.blob.core.windows.net/install/default.htm)
  
## How the SharePoint Migration Tool works

The SharePoint Migration Tool authenticates to the destination tenant after which you are prompted for the source file location and destination SPO site collection where you want the files to be migrated. After you submit the migration jobs by clicking **Migrate**, the scanning, packaging, uploading, and importing steps are performed in parallel across all the files submitted for migration.
  
> [!NOTE]
> Use a Site Collection administrator account on the target SharePoint Online site when prompted for credentials.

**AUTHENTICATION:** After opening the tool, the first thing you must do is authenticate to the destination -- the tenant where you will be migrating your files. Providing your username and password to the tenant associates the migration jobs you submit to this account. This allows your to resume your migration from another computer if needed by logging in with the same credentials. This account should be a site collection administrator of the destination you want to migrate to.


> [!NOTE]
> SharePoint Migration Tool supports the following authentication methods:
> - NTLM
> - Kerberos
> - Forms
> - Active Directory Federation Services (SAML)
> - Multi-factor authentication (MFA or 2FA)
> - Client-certificate authentication

>[!IMPORANT]
> If multiple authentication methods including NTLM or Kerberos, are enabled in the on-premises SharePoint Web Application, NTLM and Kerberos authentication are not supported by the SharePoint Migration Tool. Please use a secondary form of authentication or convert the Web Application to use NTLM and/or Kerberos authentication only.
    
**SCAN**: After you click **Migrate**, a scan is performed on every file. A scan is always performed, even if you elect to not migrate your files (see Advanced Settings). The scan verifies that there is access to the data source and write access to the SharePoint Online destination. It also scans the files for known issues.

**PACKAGING:** In the packaging stage, a content package is created that contains a manifest. 
 
**UPLOAD:** In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from an SPO provided Azure container, the files and manifest are encrypted at rest using the AES-256-CBC standard.
  
**IMPORT:** During the import phase, the key is provided to SPO. Only Azure and SPO are interacting to fetch and migrate the data to the destination. This process is a timer job based but does not prevent other jobs from being queued. During the import, a report is created in the working folder. After the migration job is completed the log is stored in the Azure container and a final report is created.

**SESSION AND RESUME:** While the migration is being performed, the tool saves information of the session in a hidden list on the users OneDrive for Business site. This allows the migration tool to resume any previous migration sessions.
    
## Encryption and security

During the upload and import phases, data is encrypted and Azure containers and keys are generated.
  
> [!IMPORTANT]
> The SharePoint Online service and a select number of engineers can run maintenance commands against the storage accounts, but they do not have direct access. Datacenter technicians do not have ready access to equipment to mount disks nor have the knowledge of how the data is laid out on the disk. All drives are physically destroyed before leaving the datacenter. Physical security is also in place across all of our datacenters. 
  
Each container is dedicated to the customer and not reused. The data is stored in the Azure blob anywhere from 30 to 90 days after which it is deleted. When the data is deleted, the files are de-linked and later soft deleted from disk. A file in an account and on-disk are may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data, if applicable).
  
The random, single-use default container key is generated programmatically and is only valid for 3 days. This key is the only way to gain access to the container. SharePoint Online never stores the key.
  
The container itself lives longer than the key. The container is purged anywhere from 30 to 90 days from its creation date.  The container is housed in a shared Microsoft storage outside the tenant but within the region and is protected using the container key.
  
If your key is lost or obtained by someone else, there are two defenses in place that protect you. First, the container only enables read/write operations. The container has no list which means you would need to know the details of the files stored in the container in order to read or write to them. Secondly, the files are encrypted at rest with AES-256-CBC.
  
> [!IMPORTANT]
> Only those who have the key have access to the container. Other users in the subscription or the tenant do not have access. 
