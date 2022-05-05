---
title: "Prerequisites and Endpoints for SharePoint Migration Tool"
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
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
description: "This article is a resource where you can find prerequisites and endpoint information for the SharePoint Migration Tool."
---
# Prerequisites & Endpoints for the SharePoint Migration Tool</br>

This article is a resource where you can find prerequisites and endpoint information for the SharePoint Migration Tool.

## Recommended requirements for best performance


| Component | Recommendation |
|:-----|:-----|
|CPU |64-bit quad core processor or better|
|RAM |16 GB |
|Local Storage|Solid-state disk: 150 GB free space|
|Network card|1 Gbps|
|Operating system |Windows Server 2012 R2 or Windows 10 client or later  <br/> .NET Framework 4.6.2 or later |

</br>


### Minimum requirements (expect slow performance)

| Component | Requirement |
|:-----|:-----|
|CPU  |64-bit 1.4-GHz 2-core processor or better |
|RAM|8 GB|
|Local Storage|Hard disk: 150 GB free space|
|Network card|High-speed Internet connection|
|Operating system|Windows Server 2012 R2 or Windows 10 client or later  <br/> .NET Framework 4.6.2 or later|



## Required endpoints

The following table lists the required endpoints for using the SharePoint Migration Tool.</br>


| Required Endpoint | Why |
|:-----|:-----|
|https://<span><span>secure.aadcdn.microsoftonline-p.<span><span>com|Authentication|
|https://<span><span>login.microsoftonline.<span><span>com|Authentication|
|https://<span><span>login.windows.<span><span>net|Authentication|
|https://<span><span>aadcdn.msftauth.<span><span>net|Authentication|
|https://<span><span>api.office.<span><span>com|Microsoft 365 APIs for content move and validation|
|https://<span><span>graph.windows.<span><span>net|Microsoft 365 APIs for content move and validation|
|https://<span><span>spmtreleasescus.blob.core.windows.<span><span>net|Installation|
|https://<span><span>*.queue.core.windows.<span><span>net|Migration API Azure requirement|
|https://<span><span>*.blob.core.windows.<span><span>net|Migration API Azure requirement|
|https://<span><span>*.pipe.aria.microsoft.<span><span>com|Telemetry/update|
|https://<span><span>*.sharepoint.<span><span>com|Destination for migration|
|https://<span><span>*.blob.core.usgovcloudapi.<span><span>net|Migration API Azure Government requirement|
|https://<span><span>*.queue.core.usgovcloudapi.<span><span>net|Migration API Azure Government requirement|
|https:<span><span>//<span><span>spoprod-a.akamaihd.<span><span>net|UI icons|
|https://<span><span>static2.sharepointonline.<span><span>com|UI icons|
|https:<span><span>//graph.<span><span>microsoft.<span><span>com| Access Microsoft Graph API to get tenant information and site information for public cloud and GCC|
|https:<span><span>//graph.<span><span>microsoft.<span><span>us |Access Microsoft Graph API to get tenant information and site information for GCC high|
|https:<span><span>//dod-graph.<span><span>microsoft.<span><span>us |Access Microsoft Graph API to get tenant information and site information for DoD|
|https:<span><span>//spmt.sharepointonline.<span><span>com|SPMT Installation link.




## Optional endpoints

| Optional Endpoint | Why |
|:-----|:-----|
|https:<span><span>//*.table.core.windows.net|Required only if you choose to use your Azure Storage account.  See **Use custom Azure storage** in Settings.|


