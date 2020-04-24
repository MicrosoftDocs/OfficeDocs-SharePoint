---
title: Migration Manager - Troubleshooting installation issues
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Troubleshoot common installation issues in Migration Manager."
---
# Troubleshooting agent installation issues in Migration Manager

If you are having trouble installing the agent file on your computers, this article provides information on the possible causes and steps to correct the problem.


## Agent installation prerequisites

Make sure you have met the installation requirements for installing an agent on your computer or virtual machine.


|**Component**|**Recommendation for best performance**|**Minimum - expect slow performance**|
|:-----|:------|:-----|
|CPU|64-bit quad core processor or better|64-bit 1.4 GHz 2-core processor or better|
|.Net version|V4.6.2 or higher. Learn more: [How to determine which versions are installed](https://docs.microsoft.com/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|V4.6.2 or higher|
|RAM|16 GB|8GB|
|Local Storage|Solid state disk: 150 GB free space|Solid state disk: 150 GB free space|
|Network card|1 Gbps|High speed internet connection|
|Operating system|Windows Server 2012 R2 or Windows 10 client|Windows Server 2012 R2 or Windows 10 client|
|Microsoft Visual C++ 2015 Redistributable|Required for OneNote migration|Required for OneNote migration|
|Anti-virus|Anti-virus software on your computer can slow down the migration speed. Be aware of this, but consider the risk of turning off your organization's antivirus software. |</br>


## Government cloud support

If you are on a **worldwide consumer cloud** or **GCC** government cloud, you must first take these steps:

1. Open microsoft.sharepoint.migration.common.dll.config.
2. Change the value of **SPOEnvironmentType** to **0** if you use the Worldwide consumer cloud or GCC.
3. Double-click "microsoft.sharepoint.migrationtool.advancedapp.exe" to start SPMT.


## Install errors

|**Error**|**Suggested action**|
|:-----|:-----|
|"Application SharePoint Migration Tool is already installed from another location".|An unfinished installation may be the cause of this error. Uninstall the tool and then reinstall.|

</br></br>

## Required Endpoints


|**Required Endpoint**|**Why**|
|:-----|:-----|
|https://<spam><spam>secure.aadcdn.microsoftonline-p.<spam><spam>com|Authentication|
|https://<spam><spam>login.microsoftonline.<spam><spam>com|Authentication|
|https://<spam><spam>api.office.<spam><spam>com|Office 365 APIs for content move and validation|
|https://<spam><spam>graph.windows.<spam><spam>net|Office 365 APIs for content move and validation|
|https://<spam><spam>spmtreleasescus.blob.core.windows.<spam><spam>net|Installation|
|https://<spam><spam>*.queue.core.windows.<spam><spam>net|Migration API Azure requirement|
|https://<spam><spam>*.blob.core.windows.<spam><spam>net|Migration API Azure requirement|
|https://<spam><spam>*.pipe.aria.microsoft.<spam><spam>com|Telemetry/update|
|https://<spam><spam>*.sharepoint.<spam><spam>com|Destination for migration|
|https://<spam><spam>*.blob.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|
|https://<spam><spam>*.queue.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|   




