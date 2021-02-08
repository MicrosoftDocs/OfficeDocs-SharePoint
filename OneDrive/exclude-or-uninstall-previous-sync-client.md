---
title: "Control Groove.exe installation when deploying Office using Click-to-Run"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODB160
- OFF160
- ODB150
- MET150
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 3eff17b9-c709-462f-946c-17719af68aca
description: "Learn how the previous OneDrive for Business sync app (Groove.exe) is excluded or uninstalled with Office Click-to-Run installations."
---

# Control Groove.exe installation when deploying Office using Click-to-Run

> [!IMPORTANT]
> Support for the previous OneDrive for Business sync app (Groove.exe) ended on January 11, 2021. As of February 1, 2021, users can longer sync OneDrive or SharePoint files in Microsoft 365 by using Groove.exe. Groove.exe will continue to work only for files in SharePoint Server.

Starting in October 2017, we changed how the previous OneDrive for Business sync app installs for enterprise customers who deploy Office 2013 or 2016 by using Click-to-Run.
  
- The previous sync app (Groove.exe) is no longer installed by default with Office 2016 Click-to-Run. If your organization provides an Office deployment configuration file to Setup.exe, you need to update your file to exclude Groove.exe from the install.

- When not in use or running, the previous sync app (Groove.exe) is uninstalled, unless: (a) Groove.exe is already configured to sync one or more SharePoint or SharePoint Server libraries or (b) a "PreventUninstall" registry key is present on the computer.

These changes don't affect your organization if you're already using the new OneDrive sync app (OneDrive.exe) to sync OneDrive and SharePoint files. These changes also don't affect your organization if you deploy Office using the traditional Windows Installer-based (MSI) method.
  
> [!NOTE]
> The new OneDrive sync app (OneDrive.exe) is the recommended option for SharePoint Server 2019 customers. However, the previous sync app (Groove.exe) is still used and supported for earlier versions of SharePoint Server. [Which version of OneDrive am I using?](https://support.office.com/article/19246eae-8a51-490a-8d97-a645c151f2ba)
  
## Ensure Groove.exe is no longer installed

If your organization provides an Office deployment configuration file to Setup.exe, add this to your config file to exclude Groove in your deployment:
  
```
<Product ID="O365ProPlusRetail" >
    <Language ID="en-us" />
    <ExcludeApp ID="Groove" />
</Product>
```

For more info about configuration options, see [Configuration options for the Office 2016 Deployment Tool](/DeployOffice/configuration-options-for-the-office-2016-deployment-tool).
  
To override the default behavior and make sure the previous OneDrive for Business sync app installs and stays installed, you must provide a config file that doesn't exclude Groove.exe. Also, you must set the "PreventUninstall" registry key on all computers where you need Groove.exe installed, so that the process doesn't uninstall Groove.exe.
  
## Uninstall Groove.exe when not in use

On Office upgrade, the installer runs on each computer to detect whether Groove.exe is currently in use or the "PreventUninstall" registry key is set. If either Groove.exe is in use or the registry key is set, Groove.exe is left in place. Otherwise, if Groove.exe isn't in use and the registry key isn't set, Groove.exe gets uninstalled automatically on that computer.
  
### Prevent uninstallation (registry key)

[HKLM\SOFTWARE\Microsoft\Office\Groove] "PreventUninstall"=dword:00000001
  
## Timeline

The following table shows more detail about which Office installations were affected by these changes and when. 


|**Office version**|**Groove.exe is no longer installed by default**|**Groove.exe is uninstalled on next update if not in use for 30 days**|
|---------|---------|---------|
|MSI (all versions)  <br/> |Not applicable  <br/> |Not applicable  <br/> |
|Office 2013 Click-to-Run  <br/> |Not applicable  <br/> |Not applicable  <br/> |
|Office 2016 Click-to-Run - Office Insider  <br/> |Sept. 2017 - Version 1710 (Build 8530.1000)  <br/> |Sept. 2017 - Version 1710 (Build 8530.1000)  <br/> |
|Office 2016 Click-to-Run - Monthly Channel  <br/> |Oct. 2017 - Version 1709 (Build 8528.2139)  <br/> |Oct. 2017 - Version 1709 (Build 8528.2139)  <br/> |
|Office 2016 Click-to-Run - Semi-Annual Channel (Targeted)  <br/> |Sept. 2018 - Version 1808 (Build 10730.20102)  <br/> |Sept. 2018 - Version 1808 (Build 10730.20102)  <br/> |
|Office 2016 Click-to-Run - Semi-Annual Channel  <br/> |Jan. 2019 - Version 1808 (Build 10730.20264)  <br/> |Jan. 2019 - Version 1808 (Build 10730.20264)  <br/> |

For more info about Office channels, see [Overview of update channels for Microsoft 365 Apps for enterprise](/DeployOffice/overview-of-update-channels-for-office-365-proplus-for-enterprise).
  
## Related topics

[Learn more about the Sync button update on SharePoint sites](https://support.office.com/article/9762aef3-d17f-4486-aae3-9c20bb979cbf)
