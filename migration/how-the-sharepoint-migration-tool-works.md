---
title: "How does the SharePoint Migration Tool work?"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: The SharePoint Migration Tool simplifies migrating your data from on-premises SharePoint Server document libraries and local file shares to SharePoint in Microsoft 365.
---

# How the SharePoint Migration Tool works

 The SharePoint Migration Tool authenticates to the destination tenant. Then you're prompted for the source file location and the destination SharePoint site collection. After you select **Migrate** to submit the migration jobs, the scanning, packaging, uploading, and importing steps run in parallel across all the files targeted for migration.
 
>[!Note]
> Use a Site Collection administrator account on the target SharePoint site when you're prompted for credentials.
  
**AUTHENTICATION:** After you open the tool, you must first authenticate to the destination, which is the tenant where you'll migrate your files. Providing your username and password to the tenant associates the migration jobs you submit to this account. This functionality allows you to resume your migration from another computer if needed by logging in with the same credentials. This account should be a site collection administrator of the destination you're migrating to. The following authentication methods are supported:

- NTLM
- Kerberos
- Forms
- ADFS
- Multi-factor authentication
- SAML-based claims
- Client certificate authentication

> [!IMPORTANT] 
> If multiple authentication methods, including NTLM or Kerberos, are enabled in the on-premises SharePoint Web Application, NTLM and Kerberos authentication are not supported by the SharePoint Migration Tool. Use a secondary form of authentication, or convert the Web Application to use NTLM and/or Kerberos authentication only.
    
**SCAN**: After you select **Migrate**, a scan is done on every file, even if you decide not to migrate your files (see Advanced Settings). The scan verifies that there's access to the data source and write access to the SharePoint destination. It also scans the files for known potential issues.

**PACKAGING:** In the packaging stage, a content package is created that contains a manifest.
 
**UPLOAD:** In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from a SharePoint-provided Azure container, the files and manifest are encrypted at rest using the AES-256-CBC standard.
  
**IMPORT:** During the import phase, the key is provided to SharePoint SAS. Only Azure and SharePoint interact to fetch and migrate the data to the destination. This process is timer job-based but doesn't prevent other jobs from being queued up. During the import, a report is created in the working folder, and live updates are made. After the migration job is completed, the log is stored in the Azure container, and a final report is created.

**SESSION AND RESUME:** While the migration run, the tool saves information about the session in a hidden list on the user's OneDrive. This information allows the migration tool to resume any previous migration sessions.
    
## Encryption and security

During the upload and import phases, data is encrypted, and Azure containers and keys are generated.
  
> [!IMPORTANT]
> The SharePoint service and a select number of engineers can run maintenance commands, but they don't have direct access to the accounts. Datacenter technicians don't know how the data is laid out on disk and don't have ready access to equipment to mount disks. All drives are physically destroyed before leaving our datacenters. Physical security is also in place across all our datacenters.
  
Each container is dedicated to the customer and not reused. The data is stored in the Azure blob for 4 to 30 days. Then it's deleted. When the data is deleted, the files are delinked and later soft-deleted from disk. A file in an account and on disk may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data if applicable).
  
The random, single-use default container key is generated programmatically and is only valid for three days. This key is the only way to gain access to the container. SharePoint never stores the key.
  
The container itself lives longer than the key. The container is purged 30 to 90 days after its creation date. The container is housed in a shared Microsoft storage outside the tenant but within the region. It's protected by the container key. For "multi-Geo" customers, The containers are generated based on the destination URL to dictate in what Geo it will be stored.
  
There are two defenses in place that protect you if your key is lost or someone else obtains it. First, the container only enables read/write operations. The container has no list. You would need to know the details of the files in the container to read or write to them. Secondly, the files are encrypted at rest with AES-256-CBC.

> [!IMPORTANT]
> Only those who have the key have access to the container. Other users in the subscription or the tenant don't have access.
  
>[!NOTE]
>The **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud using the data trustee, *German Telekom*. However, it is supported for users in Germany whose data location is not in the German data center.
