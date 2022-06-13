---
title: "Set Files On-Demand states in Windows"
ms.reviewer: 
ms.author: adjoseph
author: adeejoseph
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
search.appverid:
- ODB160
- OFF160
- ODB150
- MET150
ms.assetid: 3eff17b9-c709-462f-946c-17719af68aca
description: "Learn how to query and set file and folder states when you use OneDrive Files On-Demand on Windows."
---

# Query and set Files On-Demand states in Windows

With OneDrive Files On-Demand, files can be in one of three states. Each of these states corresponds to a file attribute state. To query the current state of a file or folder, use the following command:

- attrib \<Path to file or folder>

## Scriptable commands

Use the following commands to set file and folder states.

|**Files On-Demand state**|**File attribute state**|**Command**|
|:-----|:-----|:-----|
|Always available    <br/> |Pinned    <br/> |attrib +p \<path\><br/> |
|Locally available     <br/> |Clearpin    <br/> |attrib -p \<path\>    <br/> |
|Online-only    <br/> |Unpinned    <br/> |attrib +u \<path\><br/> |

 > [!NOTE]
> Pinning an online-only file makes the sync app download the file contents, and unpinning a downloaded file frees up space on the device by not storing the file contents locally.<br>
To set an online-only file or folder to "locally available," you must first set it to "always available."<br>If you meet the [Sync app requirements](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e) and still can't see the Files On-Demand option under "Settings", make sure the service "Windows Cloud Files Filter Driver" start type is set to 2 (AUTO_START). Enabling this feature sets the following registry key value to 2.`[HKLM\SYSTEM\CurrentControlSet\Services\CldFlt]"Start"="dword:00000002"`

