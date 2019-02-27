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
- M365-collaboration
search.appverid:
- MET150
description: "The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO).
---

# How the SharePoint Migration Tool works

The SharePoint Migration Tool provides a wizard-like experience, prompting you for information to simplify migrating your data from your on-premises SharePoint Server document libraries and local file shares to SharePoint Online (SPO). You do not have to be a global administrator to run the tool, only have write access to the site collection to where you are migrating the data.
 
 As you use the SharePoint Migration Tool, authentication to the destination tenant occurs first, after which you are prompted for your sources and destination SPO site collections where you want the files migrated. After you submit your migration jobs by clicking **Migrate**, the scanning, packaging, uploading and importing steps are performed in parallel across all the files submitted for migration.
  
**AUTHENTICATION:** After opening the tool, the first thing you must do is authenticate to the destination -- the tenant where you will be migrating your files. Providing your username and password to the tenant associates the migration jobs you submit to this account. This allows your to resume your migration from another computer if needed by logging in with the same credentials. This account should be a site collection administrator of the destination you want to migrate to.The following authentication methods are supported:

 - NTLM
- Kerberos
- Forms
- ADFS
- Multi-factor authentication
- SAML based claims
- Client certificate authentication

    **Important Note:**  If the on-perm server is configured to support multiple authentication methods including the Windows authentication, then Windows authentication will not be supported. 
    If this describes your environment, use other authentication methods instead of Windows authentication. <br>
<br>
    
**SCAN**: After you click **Migrate**, a scan is performed on every file. A scan is always performed, even if you elect to not migrate your files (see Advanced Settings). The scan verifies that there is access to the data source and write access to the SharePoint Online destination. It also scans the file for known potential issues.<br>

**PACKAGING:** In the packaging stage, a content package is created that contains a manifest consisting of 8 XMLs.<br>
 
**UPLOAD:** In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from a SPO provided Azure container, the data is encrypted at rest using the AES CBC 256 standard. The files are encrypted along with the manifest files.<br>
  
**IMPORT:** During the import phase, the key is provided to SPO SAS. Only Azure and SPO are interacting to fetch and migrate the content into the destination. This process is a timer job based, but does not prevent other jobs from being queued up. During the import, a report is created in the working folder and live updates are made. After the migration job is completed, the log is stored in the Azure container and a final report is created. A log is stored in each Manifest Container.<br>

**SESSION AND RESUME:** While the migration is being performed the tool save some information of its session in the users hidden list on their mysite. That information will be used later when the tool is reopened to allow to resume any previous migration session. It is possible to remove that information if the user requires more space in their mysite. this will only remove the session from the resume option in the tool and wont affect previous imports. 
    
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
  
>[!NOTE]
>The **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. It is also not available for users of Office 365 with the German cloud using the data trustee, *German Telekom*. However, it is supported for users in Germany whose data location is not in the German datacenter. 

