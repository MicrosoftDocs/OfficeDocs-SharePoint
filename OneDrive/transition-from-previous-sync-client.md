---
title: "Transition from the previous OneDrive for Business sync client"
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: 4100df3a-0c96-464f-b0a8-c20de34da6fa
description: "Learn how to upgrade your users to the new OneDrive sync client (OneDrive.exe)."
---

# Transition from the previous OneDrive for Business sync client

This article is for Office 365 admins who would like to transition their users off of the previous OneDrive for Business sync client (Groove.exe) so that they sync only with the new OneDrive sync client (OneDrive.exe).
  
If you're not an IT admin, see [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49) to learn how to begin syncing files using the new OneDrive sync client. 
  
> [!IMPORTANT]
> If your organization never used the previous OneDrive for Business sync client, or had fewer than 250 licensed Office 365 users in June 2016, your users are already using the new OneDrive sync client to sync files in OneDrive and SharePoint Online.<br>The new OneDrive sync client supports Windows 10, Windows 8.1, Windows 8, and Windows 7. It can also be used with SharePoint Server 2019.<br>The OneDrive sync client for Windows now supports syncing IRM-protected SharePoint document libraries and OneDrive locations. To create a seamless IRM sync experience for your end users, deploy the latest [Rights Management Service (RMS) client](https://aka.ms/odirm) to your users' computers.  
  
 **If you're ready now, [download the latest version of the new OneDrive sync client that's fully released to production](https://go.microsoft.com/fwlink/p/?linkid=844652).** To learn about other versions that are rolling out to different rings, see [New OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).
  
> [!IMPORTANT]
> OneDrive.exe must be deployed and configured before you try the takeover command.


  
## Overview

When users who are syncing files with the previous OneDrive for Business sync client (Groove.exe) sign in to the new OneDrive sync client (OneDrive.exe), the following things happen:
  
- If the new OneDrive sync client can take over syncing a library, the previous sync client stops syncing it and the new OneDrive sync client takes over syncing it without re-downloading the content. If the new OneDrive sync client can't sync the library, the previous sync client continues to sync it. If a library requires checkout or has required columns or metadata, it will be synced read-only.
    
- The previous sync client stops running and removes itself from automatic startup, unless it's still syncing libraries that the new OneDrive sync client can't sync.
    
When SharePoint Online libraries begin syncing with the new OneDrive sync client, the folder hierarchy that appears in File Explorer may be simplified.

To help your users get started with the OneDrive sync client, you can refer them to the following articles: 

- [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49)

- [Get started with the new OneDrive sync client on Mac OS X](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f)

- [Sync SharePoint files with the new OneDrive sync client](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88)
  
The following library types are not yet supported by the new OneDrive sync client, and will not transition from the previous sync client:
  
- On-premises locations in SharePoint Server 2016 or earlier.
    
- SharePoint Online libraries that people from other organizations shared that your users are syncing with the previous sync client.

For more info about sync restrictions and limitations, see [Invalid file names and file types in OneDrive, OneDrive for Business, and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)
    
## Prerequisites

1. Make sure users have the following versions of Office or higher installed. For info about deploying Office, see [Choose how to deploy Office 365 ProPlus](/DeployOffice/plan-office-365-proplus). Make sure you don't install the previous OneDrive for Business sync client. For info, see [Changes to the previous OneDrive sync client (Groove.exe) in Office 2016 Click-to-Run](exclude-or-uninstall-previous-sync-client.md).
    
|||
|:-----|:-----|
|Office version  <br/> |Minimum version  <br/> |
|Office 365 ProPlus  <br/> |16.0.7167.2\*  <br/> |
|Office 2016 MSI  <br/> |16.0.4432.1\*  <br/> |
|Office 2013 MSI/C2R  <br/> |15.0.4859.1\*  <br/> |
   
2. Make sure users have version 17.3.6743.1212 or higher of the new OneDrive sync client installed. For info about deploying the new OneDrive sync client, see [Deploy OneDrive apps by using System Center Configuration Manager](deploy-on-windows.md).
    
> [!NOTE]
> If any users have Office 2010 installed, we strongly recommend removing the SharePoint Workspace component. If users previously set up SharePoint Workspace (even if they're no longer using it), it will cause problems syncing team sites. Before starting OneDrive Setup, either [Uninstall Office from a PC](https://support.office.com/article/9dd49b83-264a-477a-8fcc-2fdf5dbf61d8#OfficeVersion=2010) or modify the installation. To do this by running Setup, first create the following XML file:<br>   `<Configuration Product="ProPlus"> <Display Level="none" CompletionNotice="no" SuppressModal="yes" NoCancel="yes" AcceptEula="yes" /> <Logging Type="standard" Path="C:\Windows\temp\" Template="MicrosoftSharePointWorkspaceSetup(*).txt" /> <Setting Id="SETUP_REBOOT" Value="Never" /> <OptionState Id="GrooveFiles" State="absent" Children="force" /> </Configuration>`<br> Then run Setup: `Setup.exe /modify ProPlus /config RemoveSharepointDesigner.xml` For more info, see [Setup command-line options for Office 2010](/previous-versions/office/office-2010/cc178956(v=office.14)
) and [Config.xml file in Office 2010](/previous-versions/office/office-2010/cc179195(v=office.14)
). 
  
## Configure takeover

When the new OneDrive sync client (OneDrive.exe) is deployed and configured on a computer, it will automatically transition off of the previous OneDrive for Business sync client (Groove.exe).

You can configure the sync client in two ways: 
  
- Silently - [Review the prerequisites and steps](use-silent-account-configuration.md), and then [use this policy](use-group-policy.md#SilentAccountConfig).  
  
- Manually - In the SharePoint admin center, [set OneDrive and SharePoint to sync with the new OneDrive sync client](/sharepoint/let-users-use-new-onedrive-sync-client#set-sharepoint-to-sync-with-the-onedrive-sync-client). This will run the new sync client the next time users click the Sync button in a SharePoint document library. If the options aren't available in the SharePoint admin center, the new OneDrive sync client is already set up to sync files in OneDrive and SharePoint Online.  
  
Once OneDrive.exe is installed and configured, Groove.exe should no longer be able to sync. If the takeover did not succeed or your users are stuck in a hybrid state (some content syncing with OneDrive.exe and some with Groove.exe), try running %localappdata%\Microsoft\OneDrive\OneDrive.exe /takeover. You must set up OneDrive.exe on the computer before you run this command. 
  
> [!TIP] 
> Make sure to run the command in a user context, rather than as admin, or the user will see the error "OneDrive.exe cannot be run with Admin privileges."<br>To affect all users on the computer, configure the command to run on every user account so it will run for any user who signs in. 

If the takeover did not succeed, the previous OneDrive for Business sync client (Groove.exe) may be an older version that can't successfully transition to the new client. To patch the previous sync client, update groove-x in [Office 2016](/officeupdates/msp-files-office-2016) or [Office 2013](/officeupdates/msp-files-office-2013), and then try again. 


  
## Block the previous sync client from syncing

To prevent users from using the previous OneDrive for Business sync client, follow these steps.

> [!WARNING]
> Running this command will disconnect Groove.exe even if the user is still syncing content.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online). 

3. Run the following command:
  
```PowerShell
Set-SPOTenantSyncClientRestriction [-GrooveBlockOption <String> "OptOut"|"HardOptIn"|"SoftOptIn"] 
```

For more information, see [Get-SPOTenantSyncClientRestriction](/powershell/module/sharepoint-online/Get-SPOTenantSyncClientRestriction). 
  

  


