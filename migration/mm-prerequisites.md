---
ms.date: 03/22/2021
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
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: "Learn about the prerequisites and endpoints required when using Migration Manager in the modern SharePoint Admin Center."
---
# Prerequisites & Endpoints for Migration Manager

This article is a resource where you can find prerequisites and endpoint information when using the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center</a> in the modern SharePoint admin center.


## Prerequisites

| Component | Recommendation for best performance | Minimum - expect slow performance |
|:-----|:------|:-----|
|CPU|64-bit quad core processor or better|64-bit 1.4 GHz 2-core processor or better|
|.NET version|V4.6.2 or higher. Learn more: [How to determine which versions are installed](/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed)|V4.6.2 or higher|
|RAM|16 GB|8 GB|
|Local Storage|Solid-state disk: 150-GB free space|Solid-state disk: 150-GB free space|
|Network card|1 Gbps|High-speed internet connection|
|Operating system|Windows Server 2012 R2 or higher <br/>Windows 10 agent|Windows Server 2012 R2 or higher <br/>Windows 10 agent|
|Anti-virus|Anti-virus software on your computer can slow down the migration speed. Evaluate and consider the risk of turning off your organization's antivirus software. |
|SMB 2.0|For file share migration, the server hosting the source data must support SMB 2.0 or higher


<br/><br/>

## Required endpoints

Migration Manager agent sends requests to and receives responses from these endpoints.  They can never call Migration Manager.

Two endpoints, https://production.odyssey.ops.mover.io and https://production-wus2-signalr.service.signalr.net, are used for SignalR connections. Migration Manager agent won’t open a port to accept remote connections.


| Required endpoints | For |
|:-----|:-----|
|`https://secure.aadcdn.microsoftonline-p.com`|Authentication|
|`https://graph.windows.net`|Microsoft 365 APIs for content move and validation.|
|`https://spmtreleasescus.blob.core.windows.net`|Installation|
|`https://*.queue.core.windows.net`|Migration API Azure requirement|
|`https://*.blob.core.windows.net`|Migration API Azure requirement|
|`https://*.pipe.aria.microsoft.com`|Telemetry/update|
|`https://*.sharepoint.com`|Destination for migration|
|`https://*.blob.core.usgovcloudapi.net`|Migration API Azure Government requirement|
|`https://*.queue.core.usgovcloudapi.net`|Migration API Azure Government requirement|
|`https://*.login.microsoftonline.com`|Sign into the MMA agent for SPO access|
|`https://*.login.windows.net`|Sign into the MMA agent for SPO access|
|`https://*.msauth.net`|Sign into the MMA agent for SPO access|
|`https://spmt.sharepointonline.com`|SPMT Installation link.
|`https://api.mover.io`|Scan feature for Migration Manager requirement.|
|`https://production.odyssey.ops.mover.io`|Scan feature for Migration Manager requirement.|
|`https://production-wus2-signalr.service.signalr.net`|Scan feature for Migration Manager requirement. Used to communicate with the server.|
|`https://api.prod.migrations.microsoft.com`|Migration Manager Web UI requirement|
|`https://odyssey.prod.migrations.microsoft.com`|Scan feature for Migration Manager requirement.|
|`https://odyssey-production-weu-1.service.signalr.net`|Scan feature for Migration Manager requirement.|
|`https://odyssey-production-weu-2.service.signalr.net`|Scan feature for Migration Manager requirement.|
|`https://odyssey-production-neu-1.service.signalr.net`|Scan feature for Migration Manager requirement.|
|`https://odyssey-production-eus2-1.service.signalr.net`|Scan feature for Migration Manager requirement.|
|`https://odyssey-production-wus2-2.service.signalr.net`|Scan feature for Migration Manager requirement.|
