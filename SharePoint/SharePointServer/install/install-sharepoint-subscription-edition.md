---
title: "Install SharePoint Subscription edition"
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
ms.assetid: 356d3a0b-fc26-455c-9afb-6d2ffdceef84
description: "Learn how to install SharePoint Subscription edition in various topologies."
---
    
# Overview
<a name="section1"> </a>

SharePoint Server v.Next installation is similar to SharePoint Server 2019. The steps are:

1. Install [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019) on your test server.
2. Install [SQL Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-sql-server-2019) on your test server or an additional test server.
3. Download the installation package from the [SharePoint v.Next TAP Engagement Portal](https://partner.microsoft.com/dashboard/directory). There will be two packages – one package for the server install, and one package that will have documentation and other small supporting files that may be needed as described below.
4. Choose the next steps based on whether you’re installing on Windows Server with Desktop Experience or Windows Server Core.

For more information, see [Install SharePoint Server 2019](install-for-sharepoint-server-2019.md)

## Installation on Windows Server with Desktop Experience

1. Mount the ISO file to your test server by double clicking on it, or by specifying it as a virtual drive in your virtual machine manager.
2. Run the SharePoint prerequisite installer "prerequisiteinstaller.exe" on your test server.
3. Run SharePoint setup (setup.exe) on your test server.
4. Run the SharePoint Products Configuration Wizard to create or join a farm "PSConfigUI.exe"
5. Configure the service applications and web applications in your farm, such as through the Farm Configuration Wizard.

## Installation on Windows Server Core

1. Mount the ISO file to your test server by using the Mount-DiskImage cmdlet, or by specifying it as a virtual drive in your virtual machine manager.

For example: Mount-DiskImage -ImagePath "C:\SharePoint Files\16.0.14131.10000_OfficeServer_none_ship_x64_.iso"

2. Run the SharePoint prerequisite installer "prerequisiteinstaller.exe" on your test server.
3. Copy the "\Files\SetupSilent\config.xml" file from your mounted ISO disk image to a writable location.

For example: Copy-Item -Path "D:\Files\SetupSilent\config.xml" -Destination "C:\SharePoint Files

4. If the config.xml file in your writable location has a read-only file attribute, remove it.
For example: Set-ItemProperty -Path "C:\SharePoint Files\config.xml" -Name IsReadOnly -Value $fals

5. Open the config.xml file in your writable location for editing.

For example: notepad.exe "C:\SharePoint Files\config.xml

6. Find and remove the "<!--" and "-->" text strings within the file. Do not remove the text in between those two text strings.
7. Replace the "Enter Product Key Here" text string in the file with your SharePoint Server product key.
8. Save your changes to the config.xml file.
9. Run SharePoint setup (setup.exe) on your test server in command line mode. This is done by adding the following command line parameters when launching setup.exe:
- */config <config file> (Where <config file> is the path to your writable config.xml file)*
- */IAcceptTheLicenseTerms (Specifying this parameter signifies that you have read, understand, and agree to the license terms of SharePoint Server and Project Server.)
- For example: D:\setup.exe /config "C:\SharePoint Files\config.xml" /IAcceptTheLicenseTerms*
10. Once SharePoint setup has completed, reboot your test server.
11. Run the following SharePoint PowerShell cmdlets with their appropriate parameters to create or join a farm.
- New-SPConfigurationDatabase to create a farm or Connect-SPConfigurationDatabase to join a farm
- Install-SPHelpCollection -Al
- Initialize-SPResourceSecurity
- Install-SPService
- Install-SPFeature -AllExistingFeatures
- New-SPCentralAdministration
- Install-SPApplicationContent

> [!NOTE]
> You can also use the "PSCONFIG.exe" command line tool or the PSConfigUI.exe GUI tool. However, PSConfigUI.exe will crash on Windows Server Core if it needs to display a summary of error messages at the end of the sequence due to a dependency on HTML rendering components.

12. Configure the service applications and web applications in your farm, such as through the Farm Configuration Wizard.

> [!NOTE]
> You must use a web browser from another computer to access the Central Administration web site. Windows Server Core does not include a web browser.
  

