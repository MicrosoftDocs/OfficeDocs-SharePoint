---
title: "Installing SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/23/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid:
description: "Learn how to install SharePoint Server Subscription edition in various topologies."
---
    
# Installing SharePoint Server Subscription Edition
<a name="section1"> </a>

The procedure to install SharePoint Server Subscription Edition is similar to installing SharePoint Server 2019. The steps are as follows:

1. Install [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019) or Windows Server 2022 on your server.
2. Install [SQL Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-sql-server-2019) on your server or an additional server.
5. The next steps are based on whether you are installing on Windows Server with Desktop Experience or Windows Server Core.

For more information, see [Install SharePoint Server 2019](install-for-sharepoint-server-2019.md).

## Installing SharePoint Server Subscription Edition on Windows Server with Desktop Experience

1. Mount the ISO file to your server by double-clicking on it, or by specifying it as a virtual drive in your virtual machine manager.
2. Run the SharePoint prerequisite installer `prerequisiteinstaller.exe` on your server.
3. Run SharePoint setup `setup.exe` on your server.
4. Run the SharePoint Products Configuration Wizard to create or join a farm `PSConfigUI.exe`
5. Configure the service applications and web applications in your farm, such as through the Farm Configuration Wizard.

## Installing SharePoint Server Subscription Edition on Windows Server Core

1. Mount the ISO file to your server by using the `Mount-DiskImage` cmdlet, or by specifying it as a virtual drive in your virtual machine manager.
    ```
    Mount-DiskImage -ImagePath "C:\SharePoint Files\16.0.14131.10000_OfficeServer_none_ship_x64_en-us.iso"
    ```
2. Run the SharePoint prerequisite installer (`prerequisiteinstaller.exe`) on your server.
3. Copy the **\Files\SetupSilent\config.xml** file from your mounted ISO disk image to a writable location.
    ```
    Copy-Item -Path "D:\Files\SetupSilent\config.xml" -Destination "C:\SharePoint Files"
    ```
4. If the `config.xml` file in your writable location has a read-only file attribute, remove it.
    ```
    Set-ItemProperty -Path "C:\SharePoint Files\config.xml" -Name IsReadOnly -Value $false
    ```
5. Open the `config.xml` file in your writable location for editing.
    ```
    notepad.exe "C:\SharePoint Files\config.xml"
    ```
6. Find and remove the `<!--` and `-->` text strings within the file. Don't remove the text in between these two text strings.
7. Replace the **Enter Product Key Here** text string in the file with your SharePoint Server product key.
8. Save your changes to the `config.xml` file.
9. Run SharePoint setup (`setup.exe`) on your server in command-line mode. Add the following command-line parameters when launching `setup.exe`:
    - `/config <config file>` (Where `<config file>` is the path to your writable `config.xml` file)
    - `/IAcceptTheLicenseTerms` (Specifying this parameter signifies that you have read, understand, and agree to the license terms of SharePoint Server and Project Server.)
    ```
    D:\setup.exe /config "C:\SharePoint Files\config.xml" /IAcceptTheLicenseTerms
    ```
10. Once SharePoint setup has completed, reboot your server.

11. Run the following SharePoint PowerShell cmdlets with their appropriate parameters to create or join a farm.

    1. `New-SPConfigurationDatabase` to create a farm or `Connect-SPConfigurationDatabase` to join a farm
    2. `Install-SPHelpCollection -All`
    3. `Initialize-SPResourceSecurity`
    4. `Install-SPService`
    5. `Install-SPFeature -AllExistingFeatures`
    6. `New-SPCentralAdministration`
    7. `Install-SPApplicationContent`

    > [!Note]
    > You can also use the `PSCONFIG.EXE` command line tool or the `PSConfigUI.exe` GUI tool. However, `PSConfigUI.exe` will crash on Windows Server Core if it needs to display a summary of error messages at the end of the sequence due to a dependency on HTML rendering components.

12. Configure the service applications and web applications in your farm through the **Farm Configuration Wizard**.

    > [!Note]
    > You must use a web browser from another computer to access the Central Administration web site. Windows Server Core does not include a web browser.