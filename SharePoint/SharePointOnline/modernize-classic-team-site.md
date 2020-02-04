---
title: "Modernize classic team sites"
ms.reviewer: dipadur
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

description: "Learn about converting classic team sites to communication sites."
---

# Modernize classic team sites
  
Intro

> [!NOTE]
> "By the way info"


### Limitations

- 



### Run the PowerShell cmdlet

We recommend running this command when site usage is low.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run Enable-SPOCommSite.

```PowerShell
Enable-SPOCommSite -SiteUrl https://contoso.sharepoint.com
```

For more info about this cmdlet, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). 
