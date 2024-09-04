---
ms.date: 07/25/2024
title: Set up OneDrive in Omnissa Horizon Virtual Apps
ms.reviewer: 
ms.author: haroldw
author: haroldwongms
manager: tgrandison
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom:
- Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection:
- Strat_OD_admin
- M365-collaboration
description: In this article, you'll learn how to enable OneDrive in Omnissa Horizon Virtual Apps.
---

# Prerequisites

•	Omnissa Horizon\
•	Microsoft Windows OS

All the Omnissa Horizon and Windows OS requirements are detailed in the below articles which can be referred prior to the Horizon Virtual App environment configurations.

Supported Windows 10 and Windows 11 Guest Operating Systems for Horizon Agent and Remote Experience, for Omnissa Horizon 8.x (2006 and later) (78714)
Supported Non-Windows 10 and 11 Guest Operating Systems for Horizon 8 Agent (78715)
•	Omnissa Dynamic Environment Manager (DEM) or a product which enables the user environment personalization. 

The system on which you plan to install DEM must meet certain software requirements.
Please refer to the article for more information.

https://docs.omnissa.com/bundle/DEMInstallConfigGuideV2406/page/SoftwareRequirements.html

## Required registry keys

Following registries help to roam the user environment on multiple nodes in the virtual application farm. We can use Omnissa Dynamic Environment Manager or a similar user environment management tool to deploy the registry to all farm servers.

[IncludeRegistryTrees]
HKCU\Software\Microsoft\Office
HKCU\Software\Microsoft\Internet Explorer
HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings
HKCU\Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Cached
HKCU\Software\Microsoft\OneDrive

[IncludeFolderTrees]
\<Appdata>\Microsoft\Windows\Recent
\<Appdata>\Microsoft\crypto
\<Appdata>\SystemCertificates
\<LocalAppdata>\Microsoft\IdentityCache
\<LocalAppdata>\Microsoft\Internet Explorer
\<LocalAppdata>\Microsoft\Windows\INetCache

### Configure Omnissa Dynamic Environment Manager with Horizon Apps 

1.	Launch the Omnissa Dynamic Environment Manager management console, select **Create Config File** and select **Use an Application Template**.

2.	Select the application template (Microsoft Office 2016 and 2019, or Microsoft 365), Select **OneDrive for Business** and click **Next**.

3.	Provide the file name and description and select **Finish**.

4.	Add the previously listed **required registry keys** to **Import / Export** settings.


#### Configure FSLogix with Omnissa Dynamic Environment Manager

Configuring FSLogix in combination with Dynamic Environment Manager will help with store OneDrive cache and the save location for Microsoft and non-Microsoft applications.

Please refer to the following article to configure FSLogix Office Container (ODFC) on all Horizon Virtual App farm servers.

[FSLogix](/fslogix/tutorial-configure-odfc-containers)

Please install the OneDrive sync client with /allusers switch on all the Horizon Virtual App farm hosts as machine installer. 

Also, please create the following entries in each Horizon farm servers. We can use DEM or similar user environment management tool to deploy the registry to all virtual app farm servers. 

Key: HKLM\Software\Microsoft\Windows\CurrentVersion\Run
Type: REG_SZ
Name: OneDrive
Data: "C:\Program Files\Microsoft OneDrive\OneDrive.exe"/background

Key: HKLM\Software\Policies\Microsoft\Onedrive
Type: REG_DWORD
Name: SilentAccountconfig
Data: 1

Note: Sometimes the silent login may take a few seconds; if the first attempt fails, a second attempt might be required. 

By following the above-mentioned steps, you can set up the OneDrive web client or Sync client as the save option in Horizon Virtual Apps. 
