---
title: "TLS 1.3 Support"
ms.reviewer: 
ms.author: v-nsatapathy
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
ms.assetid: 
description: "This article describes the supported and unsupported components on Transport Layer Security (TLS) protocol version 1.3."
---

# TLS 1.3 Support

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

TLS 1.3 is the latest and strongest version of the TLS encryption protocol. SharePoint Server Subscription Edition supports TLS 1.3 by default when deployed with Windows Server 2022 and the 2021-06 Cumulative Update for .NET Framework 3.5 and 4.8 for Microsoft server operating system for x64 (KB5003529)” is installed. There is no additional configuration necessary for it and not all software and systems may support TLS 1.3 and should contact their software and hardware vendors to find out whether their products support TLS 1.3.

> [!NOTE]
> This security feature requires SharePoint Server or higher. SharePoint Server will not use this security feature on earlier versions of Windows Server such as Windows Server 2019, regardless of the state of the "Allow Legacy Encryption" setting.


