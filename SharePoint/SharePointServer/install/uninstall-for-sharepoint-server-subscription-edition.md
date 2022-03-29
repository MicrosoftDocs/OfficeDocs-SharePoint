---
title: "Uninstall SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 7/24/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: landing-page
ms.prod: sharepoint-server-itpro
localization_priority: Critical
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 

description: "Learn how to uninstall SharePoint Server Subscription Edition in various topologies."
---

# Uninstall SharePoint Server Subscription Edition
<a name="section1"> </a>

SharePoint Server uninstallation steps are as follows:

## Uninstall on Windows Server with Desktop Experience

1. Click **Start**.

2. Click **Settings**.

3. Click **Apps**.

4. Click **Microsoft SharePoint Subscription Edition Preview**.

5. Click **Uninstall**.

6. When prompted that this app and its related information will be uninstalled, click **Uninstall**.

7. If prompted by the User Account Control (UAC) consent dialog, click **Yes** to allow the Microsoft Setup Bootstrapper app to make changes to your device.

8. When prompted if you are sure you want to remove Microsoft SharePoint Server Subscription Edition Preview from your computer, click **Yes**.

9. When prompted with a warning asking if you want to uninstall now, click **OK**.

10. After setup finishes uninstalling SharePoint, click **Close** to exit.

## Uninstall on Windows Server Core

1. Run SharePoint setup (`setup.exe`) from your **C:\Program Files\Common Files\Microsoft Shared\SERVER16\Server Setup Controller** directory with the following parameters:
    - `/config <config file>` (Where `<config file>` is the path to your writable `config.xml` file)
    - `/uninstall OSERVER`

    ```powershell
    "$env:CommonProgramFiles\Microsoft Shared\SERVER16\Server Setup Controller\setup.exe" /config "C:\SharePoint Files\config.xml" /uninstall OSERVER   
    ```

