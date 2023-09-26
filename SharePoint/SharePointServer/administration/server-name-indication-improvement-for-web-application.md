---
title: "Server Name Indication improvement for web application"
ms.reviewer: 
ms.author: serdars
author: nimishasatapathy
manager: serdars
ms.date: 4/25/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 41ec2552-43cd-471a-ba22-1962297758c0
description: "Learn how to configure Server Name Indication (SNI) in SharePoint Central Administration."
---

# Server Name Indication improvement for web application

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]
  
You can configure Server Name Indication (SNI) by the "Use Server Name Indication" setting on the **Create New Web Application** and **Extend Web Application** pages in SharePoint Central Administration.

Server Name Indication allows multiple Internet Information Server (IIS) websites with unique host headers and unique server certificates to share the same SSL port. The server examines the server name specified by the client during the SSL handshake to determine, which server certificate should be used to complete the connection. Your IIS web site must have a host header and must use SSL to use Server Name Indication. If Server Name Indication isn't used, all IIS websites sharing the same SSL port must share the same server certificate.
  
Following are the list of commands that are also used to configure Server Name Indication:
- `psconfig.exe -adminvs -port <port number> -hostheader <host header> -ssl -usesni`
- `New-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
- `Set-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
- `New-SPWebApplication -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
- `Set-SPWebApplication -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
- `New-SPWebApplicationExtension -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`