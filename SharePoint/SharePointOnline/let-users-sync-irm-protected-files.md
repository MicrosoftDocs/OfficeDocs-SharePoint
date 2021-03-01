---
title: "Let users sync IRM-protected files with the OneDrive sync app"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_OD_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- ODB160
- ODB150
ms.assetid: 6778d4de-b5f8-423c-af43-a1b2449e9b99
description: "Enable users in your organization to sync IRM-protected locations using the new OneDrive sync app (OneDrive.exe)."
---

# Let users sync IRM-protected files with the OneDrive sync app

This article is for Microsoft 365 global or SharePoint admins who want their users to be able to sync IRM-protected SharePoint document libraries and OneDrive locations using the new OneDrive sync app (OneDrive.exe).

> [!NOTE]
> Any IRM-protected files will maintain their IRM protection during the sync process, both during upload and download. The OneDrive sync app doesn't support the IRM setting that expires document access rights.
  
## Prerequisites

- You've applied [Information Rights Management (IRM) to a library](https://support.office.com/article/3bdb5c4e-94fc-4741-b02f-4e7cc3c54aa1) in Microsoft 365.

- You've installed the RMS client on your users' computers. [Download the Rights Management Service client](https://aka.ms/odirm).

    To silently install the client on computers, use the /qn switch as part of the command-line options of the Microsoft Windows Installer Tool (Msiexec.exe). For example, the following command shows the silent mode installation (assuming the RMS Client installer package is already downloaded to C:\Downloads).
  
    msiexec /qn c:\downloads\setup.msi
  
    You can have the setup file on a network share and use managed software deployment to run the msiexec command.
  
## To sync an IRM-protected library

Users sync IRM-protected libraries in the same way they sync other libraries. For info, see [Sync SharePoint files with the new OneDrive sync app](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88).
