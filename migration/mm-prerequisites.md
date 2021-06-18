---
title: "Migration Manager Prerequisites and Endpoints"
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
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: "Learn about the prerequisites and endpoints required when using Migration Manager in the modern SharePoint Admin Center."
---
# Prerequisites & Endpoints for Migration Manager

This article is a resource where you can find prerequisites and endpoint information when using Migration Manager in the modern SharePoint Admin Center.


## Prerequisites

|**Component**|**Recommendation for best performance**|**Minimum - expect slow performance**|
|:-----|:------|:-----|
|CPU|64-bit quad core processor or better|64-bit 1.4 GHz 2-core processor or better|
|.NET version|V4.6.2 or higher. Learn more: [How to determine which versions are installed](https://docs.microsoft.com/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|V4.6.2 or higher|
|RAM|16 GB|8 GB|
|Local Storage|Solid-state disk: 150-GB free space|Solid-state disk: 150-GB free space|
|Network card|1 Gbps|High-speed internet connection|
|Operating system|Windows Server 2012 R2 or higher </br>Windows 10 agent|Windows Server 2012 R2 or higher </br>Windows 10 agent|
|Anti-virus|Anti-virus software on your computer can slow down the migration speed. Evaluate and consider the risk of turning off your organization's antivirus software. |


</br></br>

## Required endpoints

|**Required endpoints**|**For**|
|:-----|:-----|
|https://<spam><spam>secure.<spam><spam>aadcdn.microsoftonline-p<spam><spam>.com|Authentication|
|https://<spam><spam>api.office<spam><spam>.com|Microsoft 365 APIs for content move and validation|
|https://<spam><spam>graph.windows<spam><spam>.net|Microsoft 365 APIs for content move and validation|
|https://<spam><spam>spmtreleasescus.blob.core.windows<spam><spam>.net|Installation|
|https://*<spam><spam>.queue.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>blob.core.windows<spam><spam>.net|Migration API Azure requirement|
|https://*.<spam><spam>pipe.aria.microsoft<spam><spam>.com|Telemetry/update|
|https://*.<spam><spam>sharepoint<spam><spam>.com|Destination for migration|
|https://<spam><spam>*.blob.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|
|https://<spam><spam>*.queue.core.usgovcloudapi.<spam><spam>net|Migration API Azure Government requirement|
|https://<spam><spam>*.login.microsoftonline.<spam><spam>com|Sign into the MMA agent for SPO access|
|https://<spam><spam>*.msauth.<spam><spam>net|Sign into the MMA agent for SPO access|
|https://<spam><spam>spmt.<spam><spam>sharepointonline.<spam><spam>com|SPMT Installation link.
|https://<spam><spam>api.mover.<spam><spam>io|Mover 

