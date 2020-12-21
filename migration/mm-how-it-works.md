---
title: How does Migration Manager work
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
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "How does Migration Manager in the Microsoft 365 SharePoint admin center work."
---
# How does Migration Manager work?

The Migration Manager centralizes the management of large file share migrations by configuring one or more computers or virtual machines (VMs) as migration "agents".  Each computer or VM can be running migration tasks simultaneously. 

## User process

**Agent setup**

From Migration Manager in the SharePoint admin center, the user downloads the agent setup file to a local computer or VM. The agent setup file prompts for two sets of credentials; the SharePoint Admin credentials to access your destination, and the Windows credentials that have read access to any of the network file shares you plan to migrate. 

This pair of credentials creates a trust with Migration Manager. Migration Manager now sees it as an available agent to which it can automatically distribute migrations tasks. 

**Task creation**

After the user configures the agent, anyone with the permission to go into the SharePoint Admin center can create tasks. 

Migration Manager authenticates to the destination tenant and then prompts for the source file location and destination location where the files are to be migrated. After you submit the migration task by selecting Migrate, the scanning, packaging, uploading, and importing steps are performed in parallel across all the files provided for migration.

## Migration Process 

**Authentication**

Sign in to your tenant admin center as a either a tenant administrator or SharePoint admin user in the destination where you want to migrate content. The tenant associates the migration jobs you submit to this account.

**Scan**

After selecting Migrate, a scan is always performed on every file, even if you decide not to migrate your files (see Settings). The scan verifies that there is access to the data source and write access to the SharePoint destination. It also scans the files for known potential issues.

**Packaging**

In the packaging stage, a content package is created that contains a manifest.

**Upload**

In the upload stage, the content package is uploaded to Azure with the manifest. Before a migration job can be accepted from a SharePoint-provided Azure container, the files and manifest are encrypted at rest using the AES-256-CBC standard.

**Import**

During the import phase, the key is provided to SharePoint SAS. Only Azure and SharePoint are interacting to fetch and migrate the data to the destination. This process is a timer job-based but does not prevent other jobs from being queued up. A report is created in the working folder, and live updates are made during the import.

After the migration job completes, reports are generated for the user and can be downloaded. Report files are cleared when the user deletes the tasks.

**Sessions**

The session's information, including the tasks and settings, is saved in the Tenant Admin site hidden list. When you click **Run** to resume a paused task, Migration Manager issues a command to the agent. If the migration task has already completed, clicking **Run** restarts the task with the same source, destination, and settings. 


## Encryption and security
During the upload and import phases, data is encrypted and Azure containers and keys are generated.

>[!Important]
>The SharePoint service and a select number of engineers can run maintenance commands against them, but they do not have direct access to the accounts. Datacenter technicians are not prepped with how data is laid out on disk and do not have ready access to equipment to mount disks. All drives are physically destroyed before leaving the datacenter. Physical security is also in place across all of our datacenters.

Each container is dedicated to the customer and not reused. The data is stored in the Azure blob from 4 to 30 days after which it is deleted. When the data is deleted, the files are de-linked and later soft-deleted from disk. A file in an account and on-disk may be shared across many servers. The same process is used for replicas, including backup copies (geo-replicated data if applicable).

The random, single-use default container key is generated programmatically and is only valid for three days. This key is the only way to gain access to the container. SharePoint never stores the key.

The container itself lives longer than the key. The container is purged anywhere from 30 to 90 days from its creation date. The container is housed in a shared Microsoft storage outside the tenant but within the region. It is protected using the container key. For multi-Geo customers, The containers are generated based on the destination URL to dictate in what Geo it will be stored. 

If your key is lost or obtained by someone else, there are two defenses in place that protect you. First, the container only enables read/write operations. The container has no list, which means you need to know the details of the files stored in the container to read or write to them. Secondly, the files are encrypted at rest with AES-256-CBC.

>[!Important]
>Only those who have the key have access to the container. Other users in the subscription or the tenant do not have access.

