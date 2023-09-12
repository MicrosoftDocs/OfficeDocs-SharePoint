---
title: "Installing SharePoint Server Subscription Edition on Windows Server Core"
ms.reviewer: 
ms.author: serdars
author: nimishasatapathy
manager: serdars
ms.date: 04/27/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid:
description: "Learn how to install SharePoint Server Subscription Edition on Windows Server Core."
---
    
# Installing SharePoint Server Subscription Edition on Windows Server Core
<a name="section1"> </a>

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Compared to classic Windows Server with Desktop Experience, Windows Server Core is a leaner deployment mode for SharePoint Server Subscription Edition as server core minimizes the number of OS features and services that are installed and running only those that are truly needed for a server. This deployment option reduces the demand on system resources (CPU, RAM, and disk space) and the potential attack surface for security vulnerabilities. Microsoft encourages Windows Server customers to move to this installation option as and when feasible for better support.

Perform the following steps to install SharePoint Server Subscription Edition on Windows Server Core:

1. Mount the ISO file to your server by using the `Mount-DiskImage` cmdlet, or by specifying it as a virtual drive in your virtual machine manager.
    ```powershell
    Mount-DiskImage -ImagePath "C:\SharePoint Files\OfficeServer.iso"
    ```
2. Run the SharePoint prerequisite installer (`prerequisiteinstaller.exe`) on your server.

3. Copy the **\Files\SetupSilent\config.xml** file from your mounted ISO disk image to a writable location.

    ```powershell
    Copy-Item -Path "D:\Files\SetupSilent\config.xml" -Destination "C:\SharePoint Files"
    ```

4. If the `config.xml` file in your writable location has a read-only file attribute, remove it.

    ```powershell
    Set-ItemProperty -Path "C:\SharePoint Files\config.xml" -Name IsReadOnly -Value $false
    ```

5. Open the `config.xml` file in your writable location for editing.

    ```powershell
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

    1. `New-SPConfigurationDatabase` to create a farm or `Connect-SPConfigurationDatabase` to join a farm.
    2. `Update-SPFlightsConfigFile -FilePath "C:\Program Files\Common Files\microsoft shared\Web Server Extensions\16\CONFIG\SPFlightRawConfig.json"`
    3. `Install-SPHelpCollection -All`
    4. `Initialize-SPResourceSecurity`
    5. `Install-SPService`
    6. `Install-SPFeature -AllExistingFeatures`
    7. `New-SPCentralAdministration`
    8. `Install-SPApplicationContent`

    > [!Note]
    > You can also use the `PSCONFIG.EXE` command line tool or the `PSConfigUI.exe` GUI tool. However, `PSConfigUI.exe` will crash on Windows Server Core if it needs to display a summary of error messages at the end of the sequence due to a dependency on HTML rendering components.

12. Configure the service applications and web applications in your farm through the **Farm Configuration Wizard**.

    > [!Note]
    > You must use a web browser from another computer to access the Central Administration website. Windows Server Core does not include a web browser.
