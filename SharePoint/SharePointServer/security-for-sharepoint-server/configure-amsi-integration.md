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
description: "Learn to secure environments and respond to associated threats from the attacks through AMSI."
---

# Configure AMSI integration with SharePoint Server

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]
  
   
## Overview

The cybersecurity landscape has fundamentally changed, as evidenced by large-scale, complex attacks, and signals that  [human-operated ransomware](https://docs.microsoft.com/security/compass/human-operated-ransomware) are on the rise. More than ever, it's critical to keep your on-premises infrastructure secure and up to date, including SharePoint Servers. 

To help customers secure their environments and respond to associated threats from the attacks, we're introducing integration between SharePoint Server and the Windows [Antimalware Scan Interface](https://docs.microsoft.com/windows/win32/amsi/antimalware-scan-interface-portal) (AMSI). AMSI is a versatile standard that allows applications and services to integrate with any anti-malware product present on a machine. 

## AMSI integration with SharePoint Server

When an AMSI-capable antivirus or anti-malware solution is integrated with SharePoint Server, it can check the content of, `HTTP` and `HTTPS` requests made to the server and prevent dangerous requests from being processed by the SharePoint Server. Any AMSI-capable antivirus or anti-malware program that is installed on the SharePoint Server scans the system as soon as the server starts to process the request. The purpose of AMSI isn't to replace current server-level antivirus/anti-malware defenses; it solely scans the `HTTP` and `HTTPS` protocols.

## Prerequisites

Check the following prerequisites on each SharePoint Server, before turning on/off AMSI:

- Windows Server 2016, or higher
- SharePoint Server Subscription Edition
- Microsoft Defender with AV engine version at 1.1.18300.4 or higher (alternatively, a compatible AMSI capable third-party AV provider)

## Turn on/off AMSI for SharePoint Server

The AMSI integration with SharePoint Server is turned off by default. 

Following are the steps to turn on/off the AMSI integration per web application:

1. Open **SharePoint Central Administration**.
2. Under **Web Applications**, select **Manage web applications**.
3. The **Manage Features** toolbar will open after you click to select the web application for which you want to enable the AMSI integration.
4. On the **SharePoint Server Antimalware Scanning** screen, click **Activate** to turn on AMSI intergration, or click **Deactivate** to turn off AMSI integration.

Alternatively, you can turn on AMSI integration for a web application by running the following `PowerShell` commands:

```powershell
Enable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL> 
```

Or turn off AMSI integration for a web application via this `PowerShell` command:

```powershell
Disable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL>  
```

## Other references

### Performance effects of using Microsoft Windows Defender as the primary AMSI solution

By default, [Microsoft Defender Antivirus](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963) (MDAV), an AMSI-capable solution, is automatically enabled and installed on endpoints and devices that are running Windows 10, Windows Server 2016, and later. If you haven’t installed an antivirus/anti-malware application, SharePoint Server AMSI integration will work with MDAV. If you install and enable another antivirus/anti-malware application, MDAV will automatically turn off. If you uninstall the other app, MDAV will automatically turn back on, and the SharePoint Server integration will work with MDAV. 

Following are the specific benefits when using MDAV on SharePoint Server:
- MDAV fetches signatures that match malicious content. If Microsoft learns about an exploit that can be blocked, a new MDAV signature can be deployed to block the exploit from affecting SharePoint.
- Using existing technology to add signatures for the malicious content
- Using the expertise of Microsoft's malware research team for adding signatures
- Using best practices that MDAV already applies for adding other signatures


There may be a performance impact on the web application because AMSI scanning uses CPU resources. There's no distinct performance impact observed from AMSI scanning when tested with MDAV and no changes to be made to the existing documented SharePoint Server antivirus exclusions. Each antivirus provider develops their own definitions that utilize AMSI technology. Therefore, your level of protection remains dependent on how quickly your specific solution can be updated to detect the latest threats.

### Microsoft Windows Defender version via the command line

> [!NOTE]
> If you are using Microsoft Windows Defender, you can use the command line and ensure to update the signatures with the latest version.

1. Launch `Command Prompt` as an Administration.
2. Navigate to `C:\ProgramData\Microsoft\Windows Defender\Platform\<antimalware platform version>`.
3. Run `mpcmdrun.exe -SignatureUpdate`.

This will determine your current engine version, check for updated definitions, and report.  

Microsoft Windows command prompt is as follows:

```powershell

Copyright (C) Microsoft Corporation. All rights reserved.
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2105.5-0>MpCmdRun.exe -SignatureUpdate
Signature update started . . .
Service Version: 4.18.2106.6
Engine Version: 1.1.18300.4 
AntiSpyware Signature Version: 1.343.1364.0
AntiVirus Signature Version: 1.343.1364.0
Signature update finished. No updates needed
C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2105.5-0>

```

