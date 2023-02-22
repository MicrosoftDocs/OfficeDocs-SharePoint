---
ms.date: 07/11/2018
title: "Change the default list and library experience"
ms.reviewer: jdemaris
manager: serdars
recommendations: true
ms.author: mikeplum
author: MikePlumleyMSFT
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: a0d90eaf-5755-4b8d-96ee-9e25bdf9114e
description: "How to select the new or classic list and library experience for a site. "
---

# Change the default list and library experience

The new SharePoint list and library experience is faster, simpler, and responsive on mobile devices. It also supports many new capabilities that are not available in the classic experience, including Power Apps and Power Automate integration, the Filters pane, and column formatting. Many sites that have features or customizations that don't work in the new experience will automatically switch back to the classic experience. For more information about this behavior, see [Differences between the new and classic experiences for lists and libraries](https://support.office.com/article/30e1aab0-a5cc-4363-b7f2-09e2ae07d4dc). To detect lists that won't work well with the new experience, run the [SharePoint Modernization scanner](/sharepoint/dev/transform/modernize-scanner).

It's no longer possible to select the classic experience as the default for all sites in your organization. Instead, we recommend setting it for only the specific sites that need it. You can activate the site collection feature _SharePoint Lists and Libraries experience_ to turn off the new list and library experience for a site collection. To learn how, see [Enable or disable site collection features](https://support.office.com/article/a2f2a5c2-093d-4897-8b7f-37f86d83df04). For info about changing this setting using PowerShell, see [Opting out of the modern list and library experience](/sharepoint/dev/transform/modernize-userinterface-lists-and-libraries-optout).

> [!NOTE]
> Users can select the default experience for an individual list or library, overriding what you set. For info, see [Switch the default experience for lists or document libraries from new or classic](https://support.office.com/article/66dac24b-4177-4775-bf50-3d267318caa9).

