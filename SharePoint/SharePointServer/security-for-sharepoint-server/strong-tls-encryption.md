---
title: "Strong TLS Encryption"
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
description: "This article describes the strong encryption of Transport Layer Security (TLS)."
---



[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
​SSL/TLS encrypts data between a client and a server, but some types of encryption are stronger than others. SharePoint Server v.Next will utilize the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to the server only use the strongest encryption.

SharePoint Server will configure itself to enforce the minimum TLS version and cipher suite requirements specified by section 9.2 of RFC 7540 on its SSL bindings regardless of whether the connection ends up using HTTP/2. Specifically:

-The SSL/TLS protocol version negotiated must be TLS 1.2 or higher. TLS protocol versions lower than TLS 1.2, and all SSL protocol versions, will be blocked for connections made to its SSL bindings.
- The TLS cipher suite negotiated must support forward secrecy and AEAD encryption modes such as GCM. Cipher suites that do not offer forward secrecy, or cipher suites that are based on null, weak stream ciphers (such as RC4), or block cipher modes (such as CBC), will be blocked for connections made to its SSL bindings.


