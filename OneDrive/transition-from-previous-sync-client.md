---
title: "Transition from the previous OneDrive for Business sync app"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: 4100df3a-0c96-464f-b0a8-c20de34da6fa
description: "Learn how to upgrade users from the previous OneDrive for Business sync app to the new OneDrive sync app (OneDrive.exe)."
---

# Transition from the previous OneDrive for Business sync app

> [!IMPORTANT]
> Support for the previous OneDrive for Business sync app (Groove.exe) will end on January 11, 2021. On February 1, 2021, users will no longer be able to sync OneDrive or SharePoint files in Microsoft 365 by using Groove.exe. Groove.exe will continue to work only for files in SharePoint Server.

This article is for global and SharePoint admins who want to transition their users off of the previous OneDrive for Business sync app (Groove.exe) so that they sync with only the new OneDrive sync app (OneDrive.exe).
  
If you're not an IT admin, to learn how to begin syncing files using the new OneDrive sync app, see [Sync files with the new OneDrive sync app in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49).
  
> [!NOTE]
> If your organization never used the previous OneDrive for Business sync app, or had fewer than 250 licensed Office 365 users in June 2016, your users are already using the new OneDrive sync app to sync files in OneDrive and SharePoint.
  
  
## Syncing files with OneDrive sync app to OneDrive sync app 

When users who are syncing files with the previous OneDrive for Business sync app (Groove.exe) sign in to the new OneDrive sync app (OneDrive.exe), the following things happen:
  
- If the new OneDrive sync app can take over syncing a library, the previous sync app stops syncing it and the new OneDrive sync app takes over syncing it without re-downloading the content. If the new OneDrive sync app can't sync the library, the previous sync app continues to sync it. If a library requires checkout or has required columns or metadata, it will be synced read-only.
    
- The previous sync app stops running and removes itself from automatic startup, unless it's still syncing libraries that the new OneDrive sync app can't sync.
    
When SharePoint libraries begin syncing with the new OneDrive sync app, the folder hierarchy that appears in File Explorer may be simplified.

  
## Limits

The following library types are not yet supported by the new OneDrive sync app, and will not transition from the previous sync app:
  
- On-premises locations in SharePoint Server 2016 or earlier. [Learn about using the OneDrive sync app with SharePoint Server 2019](/SharePoint/install/new-onedrive-sync-client)
    
- SharePoint libraries that people from other organizations shared that your users are syncing with the previous sync app.

For more info about sync restrictions and limitations, see [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)

## Requirements

To transition users off of the previous sync app, first make sure users have:

- Windows 10, Windows 8.1, Windows 8, or Windows 7.

- A current version of the new OneDrive sync app installed. For info about deploying the new OneDrive sync app, see [Deploy OneDrive apps using Microsoft Endpoint Configuration Manager](deploy-on-windows.md). OneDrive.exe must be deployed and configured before you try the takeover command. [Download the latest version of the new OneDrive sync app that's fully released to production](https://go.microsoft.com/fwlink/p/?linkid=844652). To learn about the versions that are rolling out to different rings, see [New OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).

- The following versions of Office or higher installed. For info about deploying Office, see [Choose how to deploy Microsoft 365 Apps for enterprise](/DeployOffice/plan-office-365-Apps-for-enterprise). Make sure you don't install the previous OneDrive for Business sync app. For info, see [Changes to OneDrive sync app deployment in Office Click-to-Run](exclude-or-uninstall-previous-sync-client.md).
    
    |||
    |:-----|:-----|
    |Office version  <br/> |Minimum version  <br/> |
    |Microsoft 365 Apps for enterprise  <br/> |16.0.7167.2\*  <br/> |
    |Office 2016 MSI  <br/> |16.0.4432.1\*  <br/> |
    |Office 2013 MSI/C2R  <br/> |15.0.4859.1\*  <br/> |


   > [!NOTE]
   > If any users have Office 2010 installed, we strongly recommend removing the SharePoint Workspace component. If users previously set up SharePoint Workspace (even if they're no longer using it), it will cause problems syncing team sites. Before starting OneDrive Setup, either [Uninstall Office from a PC](https://support.office.com/article/9dd49b83-264a-477a-8fcc-2fdf5dbf61d8#OfficeVersion=2010) or modify the installation. To do this by running Setup, first create the following XML file:
   >
   > ```xml
   > <?xml version="1.0" encoding="UTF-8"?>
   > <Configuration Product="ProPlus">
   >    <Display Level="none" CompletionNotice="no" SuppressModal="yes" NoCancel="yes" AcceptEula="yes" />
   >    <Logging Type="standard" Path="C:\Windows\temp\" Template="MicrosoftSharePointWorkspaceSetup(*).txt" />
   >    <Setting Id="SETUP_REBOOT" Value="Never" />
   >    <OptionState Id="GrooveFiles" State="absent" Children="force" />
   > </Configuration>
   > ```
   >
   > Then run Setup:
   >
   > ```console
   > Setup.exe /modify ProPlus /config RemoveSharepointDesigner.xml
   > ```
   > For more info, see [Setup command-line options for Office 2010](/previous-versions/office/office-2010/cc178956(v=office.14)) and [Config.xml file in Office 2010](/previous-versions/office/office-2010/cc179195(v=office.14)). 
 
- The latest [Rights Management Service (RMS) client](https://aka.ms/odirm) if you want users to be able to sync IRM-protected SharePoint document libraries and OneDrive locations.
  
## Configure takeover

When the required software is installed on your users' computers, you can configure automatic takeover of syncing in two ways:
  
- Silently - [Review the prerequisites and steps](use-silent-account-configuration.md), and then [use this policy](use-group-policy.md#silently-sign-in-users-to-the-onedrive-sync-app-with-their-windows-credentials).  
  
- Manually - In the SharePoint admin center, [set OneDrive and SharePoint to sync with the new OneDrive sync app](/sharepoint/let-users-use-new-onedrive-sync-client#set-sharepoint-to-sync-with-the-onedrive-sync-client). This will run the new sync app the next time users click the Sync button in a SharePoint document library. If the options aren't available in the SharePoint admin center, the new OneDrive sync app is already set up to sync files in OneDrive and SharePoint.  
  
After you install and configure OneDrive.exe, Groove.exe should no longer be able to sync. If the takeover did not succeed, or your users are stuck in a hybrid state (some content syncing with OneDrive.exe and some with Groove.exe), try running: `%localappdata%\Microsoft\OneDrive\OneDrive.exe /takeover`.  
  
> [!TIP] 
> Make sure to run the command in a user context, rather than as admin, or the error "OneDrive.exe cannot be run with Admin privileges" appears. <br>To affect all users on the computer, configure the command to run on every user account so it will run for any user who signs in.

If the takeover did not succeed, the previous OneDrive for Business sync app (Groove.exe) may be an older version that can't successfully transition to the new client. To patch the previous sync app, update groove-x in [Office 2016](/officeupdates/msp-files-office-2016) or [Office 2013](/officeupdates/msp-files-office-2013), and then try again.


## See also  

To help your users get started with the OneDrive sync app, you can refer them to the following articles:

- [Sync files with the new OneDrive sync app in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49)

- [Get started with the new OneDrive sync app for Mac](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f)

- [Sync SharePoint files with the new OneDrive sync app](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88)
