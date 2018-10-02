---
title: "Let users sync SharePoint files with the new OneDrive sync client"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/20/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- SPO160
- ODB160
- SPB160
- ODB150
- BSA160
- MET150
ms.assetid: 22e1f635-fb89-49e0-a176-edab26f69614
description: "Learn how to enable users in your organization to sync SharePoint Online files with the new OneDrive sync client."
---

# Let users sync SharePoint files with the new OneDrive sync client

This article is for IT administrators in large organizations who want to enable users in their organizations to sync SharePoint Online team sites with the new OneDrive sync client. Smaller organizations and organizations that are new to Office 365 are already set up to sync OneDrive and SharePoint files with the new OneDrive sync client.
  
When you enable this feature, users will be able to sync the files in a SharePoint Online team site to their PCs and Macs using the OneDrive sync client (OneDrive.exe). As part of this, they will be able to:
  
- Browse to a SharePoint Online site or shared folder and click **Sync** to sync all contents in the document library or only selected folders that are important to them. 
    
- Change the folders they sync directly from their PC or Mac.
    
- Sync shared folders.
    
- Sync read-only files and folders.
    
- Coauthor files in real time with Office 2016 (C2R build 16.0.7167.2xxx or MSI build 16.0.4432.100x)
    
- Automatically transition from the existing OneDrive for Business sync client (Groove.exe)
    
## Test the feature before you enable it for your organization
<a name="TestFeature"> </a>

Follow these steps if you want to preview the syncing of SharePoint Online files before enabling the feature for your entire organization.
  
> [!IMPORTANT]
> You only need to follow these steps to set registry keys on computers you want to use to preview the functionality. When you're ready to enable SharePoint sync for your organization, you can remove these registry keys and follow the steps under [Set SharePoint to sync with the OneDrive sync client](let-users-use-new-onedrive-sync-client.md#admincenter). 
  
 **Test SharePoint Online sync for Windows**
  
1. [Download and install the latest OneDrive sync client for Windows](https://go.microsoft.com/fwlink/?LinkId=844652).
    
2. Download and open [TeamSiteSyncPreview.reg](https://go.microsoft.com/fwlink/?LinkId=827743) to enable SharePoint document library sync. 
    
    > [!NOTE]
    >  There are known issues when you use the registry keys to preview the feature using Internet Explorer on Windows 7, or on SharePoint sites that use the classic experience. These issues don't affect the feature when you enable it in the SharePoint admin center. Enabling TeamSiteSyncPreview.reg makes the OneDrive sync client update on the Insiders Ring. For info about the build currently released to this ring, see [New OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0). 
  
3. Restart the sync client:
    
  - Right-click the blue cloud icon in your system tray and click **Exit**.
    
  - Search for "OneDrive" in the Start menu and choose **OneDrive Desktop app**.
    
This preview automatically takes over syncing the libraries that are synced using the previous OneDrive for Business sync client (Groove.exe). For more information about how this works, see [Transition from the previous OneDrive for Business sync client](https://support.office.com/article/4100df3a-0c96-464f-b0a8-c20de34da6fa).
  
 **Test SharePoint Online sync for Mac**
  
1. If you're using the OneDrive Mac Store app, uninstall it. To do this, open Finder and search for "OneDrive.app" or "OneDriveDF.app" from "This Mac." Move all returned items to the trash.
    
2. [Install the latest build of OneDrive for Mac](https://go.microsoft.com/fwlink/?linkid=823060).
    
3. Exit the OneDrive sync client by clicking on the OneDrive cloud icon in the Menu bar and selecting **Quit OneDrive**.
    
4. Open a terminal window by using cmd+space and searching for "Terminal."
    
5. Run the following commands:
    
     `Defaults write com.microsoft.OneDrive TeamSiteSyncPreview -bool True`
    
     `Defaults write com.microsoft.OneDriveUpdate Tier Team`
    
     `Killall cfprefsd`
    
    > [!NOTE]
    > You must be an Administrator on your Mac to preview this feature. 
  
6. Restart the sync client and log in again if prompted.
    
## Deploy and configure the OneDrive sync client
<a name="TestFeature"> </a>

To enable users in your organization to sync SharePoint Online team sites with the OneDrive sync client, you first need to deploy the OneDrive sync client to your organization.
  
See [Deploy the new OneDrive sync client for Windows](https://support.office.com/article/3f3a511c-30c6-404a-98bf-76f95c519668)
  
See [Deploy and configure the new OneDrive sync client for Mac](https://support.office.com/article/eadddc4e-edc0-4982-9f50-2aef5038c307)
  
## Set SharePoint to sync with the OneDrive sync client
<a name="admincenter"> </a>

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. In the left pane, click **settings**.
    
5. Make sure "OneDrive Sync Button" is set to "Show the Sync button."
    
    ![Admin settings for OneDrive sync button](media/66be619a-fec1-4719-a819-7e3fa6e222f1.PNG)
  
    To sync SharePoint files with the new client, you must also sync OneDrive files with the new client.
    
6. For "Sync Client for SharePoint," select **Start the new client**.
    
    ![Admin setting for OneDrive sync client](media/894772b5-3e43-4a60-9887-99aca47a261c.PNG)
  
    > [!NOTE]
    > If you don't see the "Sync Client for SharePoint" setting on the Settings page, your organization is already set up to use the new OneDrive sync client. When users sign in to the OneDrive sync client (OneDrive.exe), it will automatically take over syncing the site libraries that the previous new OneDrive sync client sync client (Groove.exe) was syncing. For information about how this works, and about the types of libraries that will continue syncing with the previous sync client, see [Transition from the previous OneDrive for Business sync client](https://support.office.com/article/4100df3a-0c96-464f-b0a8-c20de34da6fa). 
  
7. Click **OK**.
    
    These changes take several hours to propagate. To check that they've propagated, go to a SharePoint Online site and click **Sync**. In the browser dialog box that confirms the request to open a program, the "Program" should appear as "Microsoft OneDrive" and the "Address" should start with "odopen://"
    
## See also
<a name="admincenter"> </a>

[Sync SharePoint files with the new OneDrive sync client](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88)

