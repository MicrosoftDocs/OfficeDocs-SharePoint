---
title: "Repair SharePoint Server Subscription edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
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

## Repair on Windows Server with Desktop Experience

1. Click **Start**.
2. Click **Settings**.
3. Click **Apps**.
4. Click **Microsoft SharePoint Subscription Edition Preview**.
5. Click **Modify**.
6. If prompted by the User Account Control (UAC) consent dialog, click **Yes** to allow the Microsoft Setup Bootstrapper app to make changes to your device.
7. In the Microsoft SharePoint Server Subscription Edition Preview setup application, select **Repair** and then click **Continue**.
8. After setup finishes repairing SharePoint, click **Close** to exit.
9. If prompted to reboot your computer, click **Yes** to reboot.
10. After the computer reboots, launch the SharePoint Products Configuration Wizard.
11. Click **Next**.
12. If prompted to automatically start or reset services, click **Yes**.
13. In the Modify server farm Settings page, select **Do not disconnect from this server farm** and then click Next.
14. If prompted whether to modify the SharePoint Central Administration web application settings, select **No, this machine will continue to host the web site** and then click **Next**.
15. In the Completing the SharePoint Products Configuration Wizard page, click **Next** to begin the repair operation.
16. After the repair operation has finished, click **Finish**.

## Repair on Windows Server Core

1. Run SharePoint setup (setup.exe) from your "\Program Files\Common Files\Microsoft Shared\SERVER16\Server Setup Controller" directory with the following parameters:
- /config <config file> (Where <config file> is the path to your writable config.xml file)
- /repair OSERVER
- For example: "$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "C:\SharePoint Files\config.xml" /repair OSERVER
2. Once SharePoint setup has completed, reboot your test server.
3. Run the following SharePoint PowerShell cmdlets with their appropriate parameters to repair the server in the farm.
- Install-SPHelpCollection -All
- Initialize-SPResourceSecurity
- Install-SPService
- Install-SPFeature -AllExistingFeatures
- New-SPCentralAdministration (If hosting the Central Administration site on this server.)
- Install-SPApplicationContent
> [!NOTE]
> You can also use the "PSCONFIG.exe" command line tool or the PSConfigUI.exe GUI tool. However, PSConfigUI.exe will crash on Windows Server.
Core if it needs to display a summary of error messages at the end of the sequence due to a dependency on HTML rendering components.