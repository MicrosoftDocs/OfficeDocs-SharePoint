---
title: "Strong Transport Layer Security (TLS) Encryption"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 6/28/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- IT_Sharepoint16
ms.assetid: 
description: "This article describes the strong encryption of Transport Layer Security (TLS)."
---

# Strong Transport Layer Security (TLS) Encryption

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Secure Socket Layer (SSL) / Transport Layer Security (TLS) encrypts data between a client and a server, but some types of encryption are stronger than others. SharePoint Server utilizes the advanced security capabilities of Windows Server 2022 to ensure that [TLS connections made to the server use only the strongest encryption](/security/engineering/disable-legacy-tls).

SharePoint Server configures itself to enforce the minimum TLS version and cipher suite requirements specified by section 9.2 of [RFC 7540](https://datatracker.ietf.org/doc/html/rfc7540) on its SSL bindings regardless of the HTTP version the connection uses. 

Specifically:

- The SSL/TLS protocol version negotiated must be TLS 1.2 or higher. TLS protocol versions lower than TLS 1.2, and all SSL protocol versions, will be blocked for connections made to its SSL bindings.

- The TLS cipher suite negotiated must support forward secrecy and Authenticated encryption with associated data (AEAD) encryption modes such as GCM. Cipher suites that do not offer forward secrecy, or cipher suites that are based on null, weak stream ciphers (such as RC4), or block cipher modes (such as CBC), will be blocked for connections made to its SSL bindings.

These requirements will apply by default to all SharePoint web applications that use an SSL binding and the SSL binding of the "SharePoint Web Services" IIS website, which hosts SharePoint service application endpoints. If customers need to continue supporting legacy encryption for backward compatibility (such as older TLS protocol versions and cipher suites), they can configure this through the "Allow Legacy Encryption" setting in Central Administration. It can also be configured through the -AllowLegacyEncryption parameter in the following `PowerShell cmdlets` and command-line tools:

- `New-SPWebApplication`

- `New-SPWebApplicationExtension`

- `Set-SPWebApplication` ("Zone" parameter set)

- `New-SPCentralAdministration`

- `Set-SPCentralAdministration`

- `Set-SPServiceHostConfig`

- `PSConfig.exe -cmd adminvs`

> [!NOTE]
> Strong TLS encryption by default is not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.
