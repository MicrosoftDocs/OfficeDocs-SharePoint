---
title: "Let users sync SharePoint files with the new OneDrive sync app"
ms.reviewer: gacarini
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
- ODB160
- SPB160
- ODB150
- BSA160
- MET150
ms.assetid: 22e1f635-fb89-49e0-a176-edab26f69614
description: "Learn how to enable users in your organization to sync SharePoint Online files with the new OneDrive sync app."
---

# Let users sync SharePoint files with the new OneDrive sync app

This article is for IT administrators in large organizations who want to enable users in their organizations to sync SharePoint Online team sites with the new OneDrive sync app. Smaller organizations and organizations that are new to Office 365 are already set up to sync OneDrive and SharePoint files with the new OneDrive sync app.
  
When you enable this feature, users will be able to sync the files in a SharePoint Online team site to their PCs and Macs using the OneDrive sync app (OneDrive.exe). As part of this, they will be able to:
  
- Browse to a SharePoint Online site or shared folder and click **Sync** to sync all contents in the document library or only selected folders that are important to them. 
    
- Change the folders they sync directly from their PC or Mac.
    
- Sync shared folders.
    
- Sync read-only files and folders.
    
- Coauthor files in real time with Office 2016 (C2R build 16.0.7167.2xxx or MSI build 16.0.4432.100x)
    
- Automatically transition from the existing OneDrive for Business sync app (Groove.exe)
    
   
## Deploy and configure the OneDrive sync app
<a name="TestFeature"> </a>

To enable users in your organization to sync SharePoint Online team sites with the OneDrive sync app, you first need to deploy the OneDrive sync app to your organization.
  
See [Deploy the new OneDrive sync app using SCCM](/onedrive/deploy-on-windows)
  
See [Deploy and configure the new OneDrive sync app for Mac](/onedrive/deploy-and-configure-on-macos)

For info about the latest sync app releases, see [New OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).
  
## Set SharePoint to sync with the OneDrive sync app
<a name="admincenter"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  
    
2. In the left pane of the admin center, under **Admin centers**, select **SharePoint** to open the SharePoint admin center. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 
    
3. In the left pane, select **Settings**, and then select **classic settings page**.
    
4. Make sure "OneDrive Sync Button" is set to "Show the Sync button."
    
    ![Admin settings for OneDrive sync button](media/66be619a-fec1-4719-a819-7e3fa6e222f1.PNG)
  
    To sync SharePoint files with the new client, you must also sync OneDrive files with the new client.
    
5. For "Sync Client for SharePoint," select **Start the new client**.
    
    ![Admin setting for OneDrive sync client](media/894772b5-3e43-4a60-9887-99aca47a261c.PNG)
  
    > [!NOTE]
    > If you don't see the "Sync Client for SharePoint" setting on the Settings page, your organization is already set up to use the new OneDrive sync app. When users sign in to the OneDrive sync app (OneDrive.exe), it will automatically take over syncing the site libraries that the previous new OneDrive sync app (Groove.exe) was syncing. For information about how this works, and about the types of libraries that will continue syncing with the previous sync app, see [Transition from the previous OneDrive for Business sync app](/onedrive/transition-from-previous-sync-client). 
  
6. Select **OK**.
    
    These changes take several hours to propagate. To check that they've propagated, go to a SharePoint Online site and select **Sync**. In the browser dialog box that confirms the request to open a program, the "Program" should appear as "Microsoft OneDrive" and the "Address" should start with "odopen://"
    
## See also
<a name="admincenter"> </a>

[Sync SharePoint files with the new OneDrive sync app](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88)
