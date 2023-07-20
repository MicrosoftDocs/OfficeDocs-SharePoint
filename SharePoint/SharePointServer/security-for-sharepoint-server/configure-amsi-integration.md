---
title: "Configure AMSI integration with SharePoint Server"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 03/14/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 763613ac-83f4-424e-99d0-32efd0667bd9
description: "Learn to secure environments and respond to associated threats from the attacks through AMSI."
---

# Configure AMSI integration with SharePoint Server

[!INCLUDE[appliesto-xxx-2016-2019-SUB-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

## Introduction

The cybersecurity landscape has fundamentally changed, as evidenced by large-scale, complex attacks, and signals that [human-operated ransomware](/security/compass/human-operated-ransomware) are on the rise. More than ever, it's critical to keep your on-premises infrastructure secure and up to date, including SharePoint Servers. 

To help customers secure their environments and respond to associated threats from the attacks, we're introducing integration between SharePoint Server and the Windows
[Antimalware Scan Interface](/windows/win32/amsi/antimalware-scan-interface-portal) (AMSI). AMSI is a versatile standard that allows applications and services to integrate with any AMSI-capable anti-malware product present on a computer. 

The AMSI integration functionality is designed to prevent malicious web requests from reaching SharePoint endpoints. For example, to exploit a security vulnerability in a SharePoint endpoint before the official fix for the security vulnerability has been installed.

## AMSI integration with SharePoint Server

When an AMSI-capable antivirus or anti-malware solution is integrated with SharePoint Server, it can examine `HTTP` and `HTTPS` requests made to the server and prevent dangerous requests from being processed by SharePoint Server. Any AMSI-capable antivirus or anti-malware program that is installed on the server performs the scan as soon as the server starts to process the request.

The purpose of AMSI integration isn't to replace existing antivirus/anti-malware defenses already installed on the server; it's to provide an additional layer of protection from malicious web requests made to SharePoint endpoints. Customers should still deploy SharePoint-compatible antivirus solutions on their servers to prevent their users from uploading or downloading files with viruses.

## Prerequisites

Before enabling AMSI integration, check the following prerequisites on each SharePoint Server:

- Windows Server 2016 or higher
- SharePoint Server Subscription Edition Version 22H2 or higher
- SharePoint Server 2019 build 16.0.10396.20000 or higher (KB 5002358: March 14, 2023 security update for SharePoint Server 2019)
- SharePoint Server 2016 build 16.0.5391.1000 or higher (KB 5002385: April 11, 2023 security update for SharePoint Server 2016)
- Microsoft Defender with AV engine version at 1.1.18300.4 or higher (alternatively, a compatible AMSI-capable third-party antivirus/antimalware provider)

## Activate/Deactivate AMSI for SharePoint Server

The AMSI integration with SharePoint Server is deactivated by default. 

Follow these steps to activate/deactivate the AMSI integration per web application:

1. Open **SharePoint Central Administration**, and select **Application Management**.
2. Under **Web Applications**, select **Manage web applications**.
3. Select the web application for which you want to enable the AMSI integration, and select **Manage Features** in the toolbar.
4. On the **SharePoint Server Antimalware Scanning** screen, select **Activate** to turn on AMSI integration, or select **Deactivate** to turn off AMSI integration.

Alternatively, you can activate AMSI integration for a web application by running the following PowerShell commands:

```powershell
Enable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL> 
```
Or deactivate AMSI integration for a web application via this PowerShell command:

```powershell
Disable-SPFeature -Identity 4cf046f3-38c7-495f-a7da-a1292d32e8e9 -Url <web application URL>  
```

## Test and verify AMSI integration with SharePoint Server

You can test the Antimalware Scan Interface (AMSI) feature to verify that it's working correctly. This involves sending a request to SharePoint Server with a special test string that Microsoft Defender recognizes is for testing purposes. This test string isn't dangerous, but Microsoft Defender will treat it as if it was malicious so you can confirm how it will behave when it encounters malicious requests. 

If AMSI integration is enabled in SharePoint Server and is using Microsoft Defender as its malware detection engine, the presence of this test string will result in the request being blocked by AMSI instead of being processed by SharePoint.

The test string is similar to the [EICAR test file](https://www.eicar.org/download-anti-malware-testfile/) but differs slightly to avoid URL encoding confusion.

You can test AMSI integration by adding the test string as either a query string or an HTTP header in your request to SharePoint Server.

### Use a query string to test AMSI integration

```
amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```
 
**For example**: send a request to https://servername/sites/sitename?amsiscantest:x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*

### Use an HTTP header to test AMSI integration

```
amsiscantest: x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```

**For example**: send a request that looks like the following.

```
GET /sites/sitename HTTP/1.1
Host: servername
amsiscantest: x5opap4pzx54p7cc7$eicar-standard-antivirus-test-fileh+h*
```

Microsoft Defender detects this as the following exploit:
 
```
Exploit:Script/SharePointEicar.A
```

> [!NOTE]
> If you are using a malware detection engine other than Microsoft Defender, then you should check with your malware detection engine vendor to determine the best way to test its integration with the AMSI feature in SharePoint Server.

## Other references

### Performance effects of using Microsoft Defender as the primary AMSI solution

By default, [Microsoft Defender Antivirus](https://support.microsoft.com/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963) (MDAV), an AMSI-capable solution, is automatically enabled and installed on endpoints and devices that are running Windows 10, Windows Server 2016, and later. If you haven't installed an antivirus/anti-malware application, SharePoint Server AMSI integration will work with MDAV. If you install and enable another antivirus/anti-malware application, MDAV will automatically turn off. If you uninstall the other app, MDAV will automatically turn back on, and the SharePoint Server integration will work with MDAV. 

The benefits of using MDAV on SharePoint Server include:

- MDAV fetches signatures that match malicious content. If Microsoft learns about an exploit that can be blocked, a new MDAV signature can be deployed to block the exploit from affecting SharePoint.
- Using existing technology to add signatures for the malicious content.
- Using the expertise of Microsoft's malware research team for adding signatures.
- Using best practices that MDAV already applies for adding other signatures.

There may be a performance impact on the web application because AMSI scanning uses CPU resources. There's no distinct performance impact observed from AMSI scanning when tested with MDAV and no changes to be made to the existing documented SharePoint Server antivirus exclusions. Each antivirus provider develops their own definitions that utilize AMSI technology. Therefore, your level of protection remains dependent on how quickly your specific solution can be updated to detect the latest threats.

### Microsoft Defender version via the command line

> [!NOTE]
> If you are using Microsoft Defender, you can use the command line and ensure to update the signatures with the latest version.

1. Launch `Command Prompt` as an Administrator.
2. Navigate to `%ProgramData%\Microsoft\Windows Defender\Platform\<antimalware platform version>`.
3. Run `mpcmdrun.exe -SignatureUpdate`.

These steps will determine your current engine version, check for updated definitions, and report.  

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

