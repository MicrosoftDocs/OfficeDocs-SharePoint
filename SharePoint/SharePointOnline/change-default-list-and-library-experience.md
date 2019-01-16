---
title: "Change the default list and library experience"
ms.author: kaarins
author: kaarins
ms.audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: a0d90eaf-5755-4b8d-96ee-9e25bdf9114e
description: "How admins can choose the modern or classic list and library experience as the default in their organization. "
---

# Change the default list and library experience

As a global or SharePoint admin in Office 365, you can decide whether to use the new or classic list and library experience by default in your organization. This article describes how to change this setting at the organization level. You can also change it for a specific site collection or web by using PowerShell. (For info, see [Opting out of the modern list and library experience](/sharepoint/dev/transform/modernize-userinterface-lists-and-libraries-optout).)

In addition, users can select the default experience for an individual list or library, overriding what you set. For info, see [Switch the default experience for lists or document libraries from new or classic](https://support.office.com/article/66dac24b-4177-4775-bf50-3d267318caa9). 

In general, we recommend using the new experience by default because it's faster, simpler, and responsive on mobile devices. It also supports many new capabilities that are not available in classic, including Flow and PowerApps integration, the Filters pane, and column formatting. Many sites that have features or customizations that don’t work in the new experience will automatically switch back to the classic experience.  For more information on this behavior, see [Differences between the new and classic experiences for lists and libraries](https://support.office.com/article/30e1aab0-a5cc-4363-b7f2-09e2ae07d4dc). If you have lots of sites that still require the classic experience, you might want to keep the classic experience as the default for a while. To detect lists that won't work well with the new experience, run the [SharePoint Modernization scanner](https://aka.ms/sppnp-modernizationscanner). 
  
## Change the default experience for all lists and document libraries

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Admin centers** \> **SharePoint**. If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
3. Choose **settings**.
    
4. Next to **SharePoint Lists and Libraries experience**, select either **Classic experience** or **New experience (auto-detect)**.
    
    ![Setting for default List and Library experience](media/e153485c-9351-4b09-8989-c00395246b66.png)
  



