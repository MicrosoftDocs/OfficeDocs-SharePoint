---
title: Feature comparison:  SPO Migration Manager vs. Mover
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: Feature comparison:  SPO Migration Manager vs. Mover
---

|**Feature**|**Description**|**SPO Migration Manager**|**Mover**|
|:-----|:-----|:-----|:-----|
|Entry point to the product|How users enter the product|From SPO tenant admin experience|From mover.io and from SPO tenant admin experience|
|Product experience modality|Browser vs standalone|Primarily browser/cloud based experience. Agent installation in Windows|Primarily browser/cloud based experience. 
Agent installation in Windows app for file based migrations|
|Migration sources|What sources are supported|File shares on Windows SharePoint on-prem in CY20|Cloud compete include Amazon, S3,  Amazon WorkDocs  Azure Blob Storage  Box  Dropbox consumer and Business  Egnyte  FTP  Google Drive consumer and business  Google Cloud Storage  SFTP  WebDAV File shares on Windows  Linux  Mac Document libraries from SPO SharePoint on-prem document libraries (deprecated)|
|Migration destinations|what destinations are supported|ODB  SharePoint sites|ODB SharePoint Online (including Teams  same thing) Azure blob ODC|
|Credentials required to access the product|how users login to the product|SPO admin/Global M365 admin|Mover credentials (deprecated) Microsoft account (CY20 Q1)|
|Migration workflow|Highlevel steps required to finish a migration|Deploy at least one local agent.Create a task with source  destination URLs and configure settings. Run Task. Manage and monitor tasks from the task lists|Deploy at least one local agent (only for file share scenarios) Create a connector each for the source (another cloud storage provider) and destination (SPO admin) Map users Map permissions Run.|
|Ability to schedule tasks|not supported|Ability to create an hourly  daily  weekly and monthly schedule to a transfer. |
|Agent targeting|Ability to route certain migration tasks to specific agents|not supported|Yes|
|Task notifications|Can users get notified when a task completes or fails|not supported|User can choose to receive email notifications either on completion or on error or never.|
|File  folder  list items|Supports migration of files  folders and lists.|Yes (confirm)|Files only|
|Permissions|Separate settings are available to set file share permissions and the SharePoint on-premises permissions.|Yes (confirm)|Yes|
|Versions|We will preserve your file history  as determined by you.|Yes (confirm)|Not supported (we could never justify this need)|
|Managed Metadata & Taxonomy|SPMT supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.|No|N/A|
|Navigation & icons|Site navigation for out of box sites is preserved and migrated|No|N/A|
|Site features|We support an extensive number of site features|No|N/A|
|SharePoint web parts|SPMT supports the migration of SharePoint webparts|No|N/A|
|Site migration|SharePoint sites that are out of the box; sites that do not use any coding or 3rd party tools can be migrated|No|N/A|
|Site description|Site descriptions can be migrated|No|N/A|
|Incremental|Tasks can also be saved to be rerun at a later date  allowing you to move only those new or updated files in the source location.|Yes|Yes|
|Save tasks for later|Ability to save tasks for a later execution|Not supported. Once a task is added  it starts migrating immediately. User can pause a task and then re-run when needed.|Yes|
|Pages|Pages in the site asset library|No|N/A|
|Allow custom storage|Ability to specify a blob storage used to store temporary transiting data|No|No|
|Allow source and folder selection||Yes|
|Allow destination and folder selection|No|Yes|
|Max number of tasks in bulk file|1000|10 million (Theoretical. We had to scale to 3 million for the Walmart migration)|
|Auto-provision destination sites – File shares|Provision OneDrives or teams sites|No|No|
|Enable OneNote migration|?|Yes  with some caveats|
|Scan Only feature|Yes|Yes|
|Teams migration|Selection of channels and migrating to Teams|No|No|
|Group connected sites support|No|No|
|Bulk task upload via CSV and JSON|Yes|Yes|
|PowerShell support|<include what features are supported via PowerShell>|No|No|
|Local client/agent type|Service|User or Service|
|Gov cloud support|?|Sure  if someone wanted to test it :P|
|2010 2013 2016 2019 support as source|No|Yes  technically but we've deprecated it.|
|Reporting support|Yes|Yes|
|Settings | https://docs.microsoft.com/en-ca/sharepointmigration/spmt-settings|?|
|Task-level settings|Ability to set task-level settings|Yes|Yes|
|Filtering|Including list and library filtering|Yes  whitelist and blacklist|
|Leverages Asynchronous Meta Read (AMR)|No|No|
|Leverages App ID|No|Yes|
|Site settings migration||No|
|List settings migration||No|
|Authentications type|Supported
*     NTLM
*    Kerberos
*    Forms
*    ADFS
*    Multi-factor authentication
*    SAML based claims
*    Client certificate authentication|?|
|SPMT error code and FAQ||NA|
| missing SharePoint versions supported as source ||NA|
