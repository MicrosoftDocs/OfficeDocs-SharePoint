---
title: "Changes to OneDrive sync client deployment in Office Click-to-Run"
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
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
description: "Learn about the changes to how the previous OneDrive for Business sync client is included in Office 2016 Click-to-Run installations."
---

# Changes to OneDrive sync client deployment in Office Click-to-Run

Starting in October 2017, we're changing how the previous OneDrive for Business sync client installs for enterprise customers using Office 365 ProPlus or Office 2016 with [Click-to-Run](https://go.microsoft.com/fwlink/p/?LinkId=526674).
  
- The previous OneDrive for Business sync client (Groove.exe) will no longer be installed by default with Office 2016 Click-to-Run. If your organization provides an Office deployment configuration file to Setup.exe, you'll need to update your file to exclude Groove from the install.
    
- When not in use or running, the previous OneDrive for Business sync client (Groove.exe) will be uninstalled, unless: (a) Groove is already configured to sync one or more SharePoint Online or SharePoint Server libraries or (b) a "PreventUninstall" registry key is present on the computer.
    
These changes won't affect Office 365 customers who are already using the new OneDrive sync client (OneDrive.exe) to sync OneDrive and SharePoint Online files. Neither will these changes affect enterprises who have deployed Office with the traditional Windows Installer-based (MSI) method.
  
> [!NOTE]
> The new OneDrive sync client (OneDrive.exe) is the recommended option for Office 365 customers. However, the previous OneDrive for Business sync client (Groove.exe) is still fully supported and is used for on-premises instances of OneDrive for Business or SharePoint Server (when your organization doesn't subscribe to an Office 365 Business plan). [Which version of OneDrive am I using?](https://support.office.com/article/19246eae-8a51-490a-8d97-a645c151f2ba)
  
## Ensuring Groove.exe is no longer installed

When these changes roll out, the previous OneDrive for Business sync client (Groove.exe) will no longer be installed by default when a user installs Office 2016 via Click-to-Run. If your organization provides an Office deployment configuration file to Setup.exe, you'll need to update your file to exclude Groove from the install.
  
To exclude Groove in your deployment, add this to your config file:
  
```
<Product ID="O365ProPlusRetail" >
    <Language ID="en-us" />
    <ExcludeApp ID="Groove" />
</Product>
```

For more information about configuration options, see [Configuration options for the Office 2016 Deployment Tool](/DeployOffice/configuration-options-for-the-office-2016-deployment-tool).
  
To override the default behavior and make sure the previous OneDrive for Business sync client installs and stays installed, you'll need to provide a config file that doesn't exclude Groove.exe. Also, you'll need to set the "PreventUninstall" registry key on all computers where you need Groove.exe installed, so that the process doesn't uninstall Groove.exe.
  
## Uninstalling Groove when not in use

On Office upgrade, the installer runs on each computer to detect whether Groove.exe is currently in use or the "PreventUninstall" registry key is set. If either Groove.exe is in use or the registry key is set, Groove.exe is left in place. Otherwise, if Groove.exe isn't in use and the registry key isn't set, Groove.exe gets uninstalled automatically on that computer.
  
### Registry key to prevent uninstallation

[HKLM\SOFTWARE\Microsoft\Office\Groove] "PreventUninstall"=dword:00000001
  
## Who these changes affect and when

These changes will affect organizations who have deployed the previous OneDrive for Business sync client to sync on-premises SharePoint libraries, or libraries that have Information Rights Management enabled on them.
  
The following table shows more detail about which Office installations are affected by these changes and when. All these changes are Office client-level changes rolled out across clients, and are not turned on organization by organization.
  
|**Office version**|**Groove.exe is no longer installed by default**|**Groove.exe is uninstalled on next update if not in use for 30 days**|
|:-----|:-----|:-----|
|MSI (all versions)  <br/> |Not applicable  <br/> |Not applicable  <br/> |
|Office 2013 Click-to-Run  <br/> |Not applicable  <br/> |Not applicable  <br/> |
|Office 2016 Click-to-Run - Office Insider channel  <br/> |Sept. 2017 - Version 1710 (Build 8530.1000)  <br/> |Sept. 2017 - Version 1710 (Build 8530.1000)  <br/> |
|Office 2016 Click-to-Run - Monthly channel  <br/> |Oct. 2017 - Version 1709 (Build 8528.2139)  <br/> |Oct. 2017 - Version 1709 (Build 8528.2139)  <br/> |
|Office 2016 Click-to-Run - Semi-annual channel (Targeted)  <br/> |Sept. 2018 - Version 1808 (Build 10730.20102)  <br/> |Sept. 2018 - Version 1808 (Build 10730.20102)  <br/> |
|Office 2016 Click-to-Run - Semi-annual channel  <br/> |Jan. 2019 - Version 1808 (Build 10730.20264)  <br/> |Jan. 2019 - Version 1808 (Build 10730.20264)  <br/> |
   
For more information about Office channels, see [Overview of update channels for Office 365 ProPlus](/DeployOffice/overview-of-update-channels-for-office-365-proplus).
  
Unless you need Groove.exe for some of your scenarios (for example, syncing on-premises SharePoint files), we strongly recommend leaving the new defaults in place and excluding Groove.exe from Office 2016 installations.
  
## Related Topics

[Learn more about the Sync button update on SharePoint sites](https://support.office.com/article/9762aef3-d17f-4486-aae3-9c20bb979cbf)
  

