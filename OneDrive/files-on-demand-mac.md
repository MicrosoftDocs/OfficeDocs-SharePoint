---
title: "Set Files On-Demand states"
ms.reviewer: joleung
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- OFF160
- ODB150
- MET150
ms.assetid: 3eff17b9-c709-462f-946c-17719af68aca
description: "Learn how to query and set file and folder states when you use OneDrive Files On-Demand."
---

# Query and set Files On-Demand states

With OneDrive Files On-Demand, files can be in one of three states. Each of these states corresponds to a file attribute state.
To query the current state of a file or folder, use the following commands:

- Windows: attrib <Path to file or folder>
- Mac: /Applications/OneDrive.App/Contents/MacOS/OneDrive /getpin <Path to file or folder>

## Scriptable commands

Use the following commands to set file and folder states.

|**Files On-Demand state**|**File attribute state**|**Windows command**|**Mac command**|
|:-----|:-----|:-----|:-----|
|Always available	<br/> |Pinned	<br/> |attrib +p <path\><br/> |	/Applications/OneDrive.App/Contents/MacOS/OneDrive /setpin <path\><br/> |
|Locally available 	<br/> |Clearpin	<br/> |attrib -p <path\>	<br/> |/Applications/OneDrive.App/Contents/MacOS/OneDrive /clearpin <path\>|
|Online-only	<br/> |Unpinned	<br/> |attrib +u <path\><br/> |	/Applications/OneDrive.App/Contents/MacOS/OneDrive /unpin <path\>|

 > [!NOTE]
> To set the file attribute state for all items within a folder on Mac, add the /r parameter.<br>Pinning an online-only file makes the sync app download the file contents, and unpinning a downloaded file frees up space on the device by not storing the file contents locally.<br>
To set an online-only file or folder to "locally available," you must first set it to "always available."

<br>If you meet the [Windows and OneDrive sync app requirements](https://support.office.com/en-us/article/onedrive-system-requirements-cc0cb2b8-f446-445c-9b52-d3c2627d681e) and still can't see the Files On-Demand option under "Settings", make sure the service "Windows Cloud Files Filter Driver" start type is set to 2 (AUTO_START). Enabling this feature sets the following registry key value to 2.
[HKLM\SYSTEM\CurrentControlSet\Services\CldFlt]"Start"="dword:00000002"
