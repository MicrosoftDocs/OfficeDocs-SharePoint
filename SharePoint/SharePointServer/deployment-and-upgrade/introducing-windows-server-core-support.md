---
title: "Introducing Windows Server Core support"
ms.reviewer: 
ms.author: v-benzyd
author: benzicald
manager: serdars
ms.date: 7/2/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 

description: "Windows Server Core is a leaner Windows Server deployment type compared to the classic Windows Server with Desktop Experience."
---

# Introducing Windows Server Core support

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Compared to classic Windows Server with Desktop Experience, Windows Server Core is a leaner deployment mode for SharePoint Server Subscription Edition as Server Core minimizes the number of OS features and services that are installed and running only those that are truly needed for a server. This deployment option reduces the demand on system resources (CPU, RAM, and disk space) and the potential attack surface for security vulnerabilities. Microsoft encourages Windows Server customers to move to this installation option as and when feasible for better support.

Windows Server Core support has been introduced with the SharePoint Server release. This support makes SharePoint Server Subscription Edition an even better citizen in the Windows Server ecosystem and makes easier to host SharePoint Server in datacenters that have standardized on Server Core. We encourage customers to start testing this installation option in addition to the classic Windows Server with Desktop Experience.

## What’s new in Windows Server Core

The following improvements to the SharePoint Server deployment experience on Windows Server Core:

- Shows a report about what operation is being performed (install, uninstall, or repair)
- Displays a message during setup reminding users that setup may take a while to complete
- Percentage indicator to indicate the progress of the operation
- Notifies the user when a reboot is required

## Install on Windows Server Core

To install SharePoint Server Subscription Edition on Windows Server Core, see [Installing SharePoint Server Subscription Edition on Windows Server Core](../install/install-sharepoint-subscription-edition.md#installing-sharepoint-server-subscription-edition-on-windows-server-core)

## Repair on Windows Server Core

To repair SharePoint Server Subscription Edition on Windows Server Core, see [Repair on Windows Server Core](../install/repair-sharepoint-server-subscription-edition.md#repair-on-windows-server-core)

## Uninstall on Windows Server Core

To uninstall SharePoint Server Subscription Edition on Windows Server Core, see [Uninstall on Windows Server Core](../install/uninstall-for-sharepoint-server-subscription-edition.md#uninstall-on-windows-server-core)

> [!Note]
> The SharePoint Hybrid Configuration Wizard can't authenticate Microsoft 365 global administrator accounts on Windows Server Core. Customer can use PowerShell scripts to configure SharePoint hybrid features on Windows Server Core.
