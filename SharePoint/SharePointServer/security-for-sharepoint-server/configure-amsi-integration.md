---
title: "Configure AMSI integration with SharePoint Server"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 09/05/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 763613ac-83f4-424e-99d0-32efd0667bd9
description: "Learn about security hardening for SharePoint Server and database server roles, including specific hardening requirements for ports, protocols, and services."
---

# Configure AMSI integration with SharePoint Server

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]
  
   
## Introduction

The cybersecurity landscape has fundamentally changed, as evidenced by large-scale, complex attacks, and signals that [human-operated ransomware](https://docs.microsoft.com/security/compass/human-operated-ransomware) are on the rise. More than ever, it is critical to keep your on-premises infrastructure secure and up to date, including SharePoint Servers. 

To help customers secure their environments and respond to associated threats from the attacks, we are introducing integration between SharePoint Server and the Windows [Antimalware Scan Interface](https://docs.microsoft.com/windows/win32/amsi/antimalware-scan-interface-portal) (AMSI). AMSI is a versatile standard that allows applications and services to integrate with any antimalware product present on a machine. 

## SharePoint Server AMSI integration

When an AMSI-capable antivirus or antimalware solution is integrated with SharePoint Server, it can check the content of `HTTP` and `HTTPS` requests made to the server and prevent dangerous requests from being processed by the SharePoint Server. Any AMSI-capable antivirus or antimalware programme that is installed on the SharePoint Server scans the system as soon as the server starts to process the request. The purpose of AMSI is not to replace current server-level antivirus/antimalware defences; it solely scans the `HTTP` and `HTTPS` protocols.

## Prerequisites

Before turning on/off AMSI check the following prerequisites on each SharePoint Server:

- Windows Server 2016, or higher
- SharePoint Server Subscription Edition
- Microsoft Defender with AV engine version

## Turn on/off AMSI for SharePoint Server

The AMSI integration with SharePoint Server is turned off by default. 

Following are the steps to turn on/off the AMSI integration per web application:

1. Open **SharePoint Central Administration**.
2. Under **Web Applications**, click **Manage web applications**.
3. The **Manage Features** toolbar will open after you click to select the web application for which you want to enable the AMSI integration.
4. On the **SharePoint Server Antimalware Scanning** screen, click **Activate** to turn on AMSI intergration, or click **Deactivate** to turn off AMSI integration.

Alternatively, you can turn on AMSI integration for a web application by running this `PowerShell` command:

```powershell
Enable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL> 
```

Or turn off AMSI integration for a web application via this `PowerShell` command:

```powershell
Disable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL>  
```

