---
title: "Transition from the previous OneDrive for Business sync client"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/3/2018
ms.audience: Admin
ms.topic: get-started-article
ms.prod: office-online-server
localization_priority: Priority
ms.collection: Strat_OD_sync
ms.assetid: 4100df3a-0c96-464f-b0a8-c20de34da6fa
description: "Learn how to upgrade your users to the new OneDrive sync client (OneDrive.exe)."
---

# Transition from the previous OneDrive for Business sync client

 *Last updated*  : January 2018 
  
This article is for Office 365 admins whose users are running the previous OneDrive for Business sync client (Groove.exe) on Windows computers and who want to upgrade to the new OneDrive sync client (OneDrive.exe) to sync files in OneDrive for Business and SharePoint Online.
  
If you're not an IT admin, see [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49) to learn how to begin syncing files using the new OneDrive sync client. 
  
> [!IMPORTANT]
>  The new OneDrive sync client for Windows now supports syncing IRM-protected SharePoint document libraries and OneDrive locations. To create a seamless IRM sync experience for your end users, deploy the latest [Rights Management Service (RMS) client](https://aka.ms/odirm) to your users' computers. >  If your organization never used the previous OneDrive for Business sync client, or had fewer than 250 licensed Office 365 users in June 2016, your users must use the new OneDrive sync client to sync OneDrive for Business and SharePoint Online files. >  The new OneDrive sync client supports Windows 10, Windows 8.1, Windows 8, and Windows 7. It doesn't yet support syncing on-premises instances of OneDrive for Business or SharePoint Server (when your organization doesn't subscribe to an Office 365 business plan). 
  
 **If you're ready now, [download the latest version of the new OneDrive sync client that's fully released to production](https://go.microsoft.com/fwlink/p/?linkid=844652).** To learn about other versions that are rolling out to different rings, see [New OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).
  
Installation and setup guides for users are available for syncing [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49), [Get started with the new OneDrive sync client on Mac OS X](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f), and [Sync SharePoint files with the new OneDrive sync client](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88).
  
## Overview

When users who are syncing files with the previous OneDrive for Business sync client (Groove.exe) sign in to the new OneDrive sync client (OneDrive.exe), the following things happen:
  
- If the new OneDrive sync client can take over syncing a library, the previous sync client stops syncing it and the new OneDrive sync client takes over syncing it without re-downloading the content. If the new OneDrive sync client can't sync the library, the previous sync client continues to sync it. If a library requires checkout or has required columns or metadata, it will be synced read-only.
    
- The previous sync client stops running and removes itself from automatic startup, unless it's still syncing libraries that the new OneDrive sync client can't sync.
    
When SharePoint Online libraries begin syncing with the new OneDrive sync client, the folder hierarchy that appears in File Explorer may be simplified.
  
The following library types are not yet supported by the new OneDrive sync client, and will not transition from the previous sync client:
  
- On-premises instances of OneDrive for Business and SharePoint Server (when your organization doesn't subscribe to an Office 365 business plan).
    
- SharePoint Online libraries that people from other organizations shared that your users are syncing with the previous sync client.
    
## Prerequisites

1. Make sure users have the following versions of Office or higher installed. For info about deploying Office, see [Choose how to deploy Office 365 ProPlus](https://support.office.com/article/e471ef30-2a09-4767-a172-aa74e1dc4686). Make sure you don't install the previous OneDrive for Business sync client. For info, see [Changes to the previous OneDrive sync client (Groove.exe) in Office 2016 Click-to-Run](changes-to-the-previous-onedrive-sync-client-groove-exe-in-office-2016-click-to).
    
|||
|:-----|:-----|
|Office version  <br/> |Minimum version  <br/> |
|Office 365 ProPlus  <br/> |16.0.7167.2\*  <br/> |
|Office 2016 MSI  <br/> |16.0.4432.1\*  <br/> |
|Office 2013 MSI/C2R  <br/> |15.0.4859.1\*  <br/> |
   
2. Make sure users have version 17.3.6743.1212 or higher of the new OneDrive sync client installed. For info about deploying the OneDrive sync client, see [Deploy the new OneDrive sync client in an enterprise environment](deploy-the-new-onedrive-sync-client).
    
> [!NOTE]
> If Office 2010 is installed on a computer, the SharePoint Workspace component must be removed. Before starting OneDrive Setup, either [Uninstall Office 2016, Office 2013, or Office 365 from a PC](https://support.office.com/article/9dd49b83-264a-477a-8fcc-2fdf5dbf61d8#OfficeVersion=2010) or [Install or remove individual Office 2010 programs and components](https://support.office.com/article/aeb80df5-326c-4afc-8064-bd195f560753). 
  
## Configure takeover

1. In the SharePoint admin center, [Enable users to sync SharePoint files with the new OneDrive sync client](https://support.office.com/article/22e1f635-fb89-49e0-a176-edab26f69614). If the options aren't available, the new OneDrive sync client is already set up to sync OneDrive for Business and SharePoint Online files.
    
2. If you're running Windows 10, you can use silent account configuration to sign in users. For info, see [(Preview) Silently configure OneDrive using Windows 10 or domain credentials](use-group-policy-to-control-onedrive-sync-client-settings.md#SilentConfig).
    
## Run the takeover command

If you don't run the takeover command, users transition to the new sync client by:
  
- Launching OneDrive Setup (first-time users of the new OneDrive sync client).
    
- Setting up additional libraries (existing users of the new OneDrive sync client).
    
To automatically transition file syncing without the need for user interaction, you can run the takeover command. Use a tool such as System Center Configuration Manager (SCCM) and run the following command for each user on a PC:
  
```
%localappdata%\Microsoft\OneDrive\OneDrive.exe /takeover
```

> [!TIP]
>  Make sure to run the command in a user context, rather than as admin, or the user will see a "OneDrive.exe cannot be run with Admin privileges" error. >  To affect all users on computer, configure the command to run on every user account. This will ensure that it's executed for any user who signs in. For an example of how to deploy an .exe on every user account, see [How to deploy the OneDrive sync client with SCCM](https://go.microsoft.com/fwlink/?linkid=839723). 
  
## Block the previous sync client from syncing

To prevent users from using the previous OneDrive for Business sync client to sync their OneDrive for Business and SharePoint Online files, run the following command in Microsoft PowerShell:
  
```
Set-SPOTenantSyncClientRestriction [-GrooveBlockOption <String> "OptOut"|"HardOptIn"|"SoftOptIn"] 
```

For more information, see [Get-SPOTenantSyncClientRestriction](https://go.microsoft.com/fwlink/p/?linkid=855909). For information about using PowerShell, see [Introduction to the SharePoint Online Management Shell](https://support.office.com/article/c16941c3-19b4-4710-8056-34c034493429).
  
## Additional resources
<a name="step6"> </a>

See the following article for more info about the new OneDrive sync client.
  
|**Title**|**Description**|
|:-----|:-----|
|[Deploy the new OneDrive sync client in an enterprise environment](deploy-the-new-onedrive-sync-client) <br/> |Deploy the OneDrive sync client to Windows users in your organization.  <br/> |
|[Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49) <br/> |How Windows users can set up the OneDrive sync client.  <br/> |
|[Sync SharePoint files with the new OneDrive sync client](https://support.office.com/article/6de9ede8-5b6e-4503-80b2-6190f3354a88) <br/> |Use the OneDrive sync client to sync SharePoint Online files.  <br/> |
|[Use Group Policy to control OneDrive sync client settings](use-group-policy-to-control-onedrive-sync-client-settings) <br/> |Configure the OneDrive sync client using Group Policy.  <br/> |
|[Restrictions and limitations when you use the new OneDrive sync client to sync OneDrive for Business libraries](https://go.microsoft.com/fwlink/?LinkId=717734) <br/> |Knowledge base article with info about file size limits and file name restrictions.  <br/> |
   

