---
title: "Uninstall SharePoint Server Subscription edition"
ms.reviewer: 
ms.author: nimishasatapathy
author: nimisha
manager: serdars
ms.date: 7/24/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: hub-page
ms.prod: sharepoint-server-itpro
localization_priority: Critical
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 47db8aed-7e2b-4ccb-b248-d71df3bffa99

description: "Learn how to install SharePoint Server in various topologies."
---

# Uninstall on Windows Server with Desktop Experience

1. Click **Start**.
2. Click **Settings**.
3. Click **Apps**.
4. Click **Microsoft SharePoint Subscription Edition Preview**.
5. Click **Uninstall**.
6. When prompted that this app and its related info will be uninstalled, click **Uninstall**.
7. If prompted by the User Account Control (UAC) consent dialog, click **Yes** to allow the Microsoft Setup Bootstrapper app to make changes to your device.
8. When prompted if you’re sure you want to remove Microsoft SharePoint Server Subscription Edition Preview from your computer, click **Yes**.
9. When prompted with a warning asking if you want to uninstall now, click **OK**.
10. After setup finishes uninstalling SharePoint, click **Close** to exit.

# Uninstall on Windows Server Core

1. Run SharePoint setup (setup.exe) from your "\Program Files\Common Files\Microsoft Shared\SERVER16\Server Setup Controller" directory with the following parameters:
- */config <config file> (Where <config file> is the path to your writable config.xml file)
- /uninstall OSERVER
- For example: "$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "C:\SharePoint Files\config.xml" /uninstall OSERVER*