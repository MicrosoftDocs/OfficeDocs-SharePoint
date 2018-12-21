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

As a global or SharePoint admin in Office 365, you can decide whether to use the new or classic list and library experience by default in your organization. This article describes how to change this setting at the organization level. You can also change it for a specific site collection, web, or list by using PowerShell. (For info, see [Opting out of the modern list and library experience](/sharepoint/dev/transform/modernize-userinterface-lists-and-libraries-optout).)

In addition, users can select the default experience for an individual list or library, overriding what you set. For info, see [Switch the default experience for lists or document libraries from new or classic](https://support.office.com/article/66dac24b-4177-4775-bf50-3d267318caa9). 

In general, we recommend using the new experience by default because it's faster, simpler, and responsive on mobile devices. If sites have features or customizations that don't work in the new experience, they will switch back to the classic experience automatically. If you have lots of sites that still require the classic experience, you might want to keep the classic experience as the default for a while. To detect lists that won't work well with the new experience, run the [SharePoint Modernization scanner](https://aka.ms/sppnp-modernizationscanner). 
  
## Change the default experience for all lists and document libraries

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Choose **settings**.
    
5. Next to **SharePoint Lists and Libraries experience**, select either **Classic experience** or **New experience (auto-detect)**.
    
    ![Setting for default List and Library experience](media/e153485c-9351-4b09-8989-c00395246b66.png)
  



