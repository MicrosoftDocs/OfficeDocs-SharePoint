---
title: "Custom list templates"
ms.reviewer: hasaladi
ms.author: kaarins
author: kaarins
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Add and remove custom templates for the Lists app and change who has permission to access them."
---

# Custom list templates

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -DisablePersonalListCreation $true
    ```

