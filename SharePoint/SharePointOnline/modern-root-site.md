---
title: "Create a modern root site"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160

description: "Learn about modernizing the root site for your organization."
---

# Create a modern root site
  
Previously, when SharePoint was set up for an organization, a classic team site was created as the root (or top-level) SharePoint site. Now, a communication site is set up as the root site for new organizations. If your environment was set up before <date>, you can change your root site to a modern site in one of two ways:

- If you want to keep using the content on the site, you can convert the existing site to a communication site. For info, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). (You can do this only if you never turned on the classic publishing feature for the site.)
- If you have a different site that you want to use as your root site, you can replace the root site with it. For info, see [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap).
  
## Run PowerShell commands to modernize the root site

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run either Enable-SPOCommSite or Invoke-SPOSiteSwap.