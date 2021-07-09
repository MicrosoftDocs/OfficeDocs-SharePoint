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

# Strong TLS Encrpytion by default for SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

​SSL/TLS encrypts data between a client and a server, but some types of encryption are stronger than others. SharePoint Server will utilize the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to the server only use the strongest encryption.

SharePoint Server will configure itself to enforce the minimum TLS version and cipher suite requirements specified by section 9.2 of RFC 7540 on its SSL bindings regardless of whether the connection ends up using HTTP/2. Specifically:

-The SSL/TLS protocol version negotiated must be TLS 1.2 or higher. TLS protocol versions lower than TLS 1.2, and all SSL protocol versions, will be blocked for connections made to its SSL bindings.
- The TLS cipher suite negotiated must support forward secrecy and AEAD encryption modes such as GCM. Cipher suites that do not offer forward secrecy, or cipher suites that are based on null, weak stream ciphers (such as RC4), or block cipher modes (such as CBC), will be blocked for connections made to its SSL bindings.

These requirements will apply by default to all SharePoint web applications that use an SSL binding, as well as the SSL binding of the "SharePoint Web Services" IIS web site, which hosts SharePoint service application endpoints. If the customers need to continue supporting legacy encryption for backward compatibility (such as older TLS protocol versions and cipher suites), they can configure this through the "Allow Legacy Encryption" setting in Central Administration. It can also be configured through the -AllowLegacyEncryption parameter in the following `PowerShell cmdlets` and command line tools:
- `New-SPWebApplication`
- `New-SPWebApplicationExtension`
- `Set-SPWebApplication ("Zone" parameter set)`
- `New-SPCentralAdministration`
- `Set-SPCentralAdministration`
- `Set-SPServiceHostConfig`
- `PSConfig.exe -cmd adminvs`

This security feature requires SharePoint Server or higher. SharePoint Server will not use this security feature on earlier versions of Windows Server such as Windows Server 2019, regardless of the state of the "Allow Legacy Encryption" setting.