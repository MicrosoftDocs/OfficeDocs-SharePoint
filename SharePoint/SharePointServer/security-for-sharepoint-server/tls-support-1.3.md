---
title: "TLS Support 1.3"
ms.reviewer: 
ms.author: v-satapathy
author: nimishasatapathy
manager: serdars
ms.date: 6/28/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- IT_Sharepoint16
ms.assetid: 559dddb1-95c9-4242-99ca-cf9cf1cbd0c3
description: "This article describes the supported and unsupported components on Transport Layer Security (TLS) protocol version 1.3."
---

## Supported components on TLS 1.3

[!INCLUDE [appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
By default, many networking and security components in Windows Server vNext support TLS 1.3,

- Schannel (core Windows library for SSL/TLS)
- HTTP.SYS (core HTTP/HTTPS server component of IIS)
  
## Unsupported components on TLS 1.3

By default, many networking and security components in Windows Server vNext do not support TLS 1.3,
- WinHTTP (HTTP client library)
- WinInet (HTTP client library for legacy applications like Internet Explorer)
- .NET Framework 4.8
- SQL Server 2019
