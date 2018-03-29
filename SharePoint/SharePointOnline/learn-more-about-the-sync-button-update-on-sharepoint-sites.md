---
title: "Learn more about the Sync button update on SharePoint sites"
ms.author: matteva
author: matteva
manager: pamgreen
ms.date: 8/14/2017
ms.audience: Admin
ms.topic: get-started-article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_OD_sync
ms.assetid: 9762aef3-d17f-4486-aae3-9c20bb979cbf
description: "We're updating the Sync button in SharePoint Online sites libraries and Office 365 Groups to point to the new OneDrive sync client (onedrive.exe), instead of the old OneDrive for Business sync client (groove.exe) that it points to today. We're also simplifying the sync settings in the OneDrive admin center."
---

# Learn more about the Sync button update on SharePoint sites

We're updating the Sync button in SharePoint Online sites libraries and Office 365 Groups to point to the new OneDrive sync client (onedrive.exe), instead of the old OneDrive for Business sync client (groove.exe) that it points to today. We're also simplifying the sync settings in the OneDrive admin center.
  
## 

This update will result in the following changes:
  
- The Sync button in SharePoint Online site libraries, Office 365 Groups, and shared OneDrive for Business site libraries will open the OneDrive sync client instead of the old OneDrive for Business sync client. 
    
- Two blue cloud icons in the Windows notification area will converge to one (unless you're syncing SharePoint site libraries that still require the old sync client). This happens because when your organization is transitioned, the OneDrive sync client (onedrive.exe) automatically takes over syncing SharePoint libraries that the OneDrive for Business sync client was syncing. No action is required by either you or your users.
    
- The SharePoint admin center will no longer have the option to sync SharePoint Online sites with the old OneDrive for Business sync client (groove.exe).
    
## Libraries that won't transition

The following types of libraries won't transition from the old sync client:
  
- On-premises instances of OneDrive for Business (libraries that aren't part of an Office 365 business plan).
    
- SharePoint Online site libraries with Information Rights Management enabled on them.
    
- SharePoint Online site libraries that people from other organizations shared with you and that you're syncing with the old sync client.
    
## Libraries that transition as read-only

The following types of libraries will transition from the old sync client as read-only:
  
- Libraries that contain multiple required columns, extra metadata, or custom columns. See [Create a column in a SharePoint list or library](https://support.office.com/article/2b0361ae-1bd3-41a3-8329-269e5f81cfa2).
    
- Libraries that [Set up a library to require check-out of files](https://support.office.com/article/0c73792b-f727-4e19-a1f9-3173899e695b).
    
> [!NOTE]
> If you want to sync a read-only library so that you can edit the contents, you'll need to change the library settings to no longer [Set up a library to require check-out of files](https://support.office.com/article/0c73792b-f727-4e19-a1f9-3173899e695b), and remove extra metadata and custom columns. If your organization uses the syncing of these libraries as a part of your essential workflow, you can [Opt out of the sync update](learn-more-about-the-sync-button-update-on-sharepoint-sites.md#BKMK_OptOut) and continue syncing with the old OneDrive for Business sync client. 
  
## Which organizations are affected by this change

This change affects small and medium sized organizations which had fewer than 250 paid Office 365 seats as of June 2016.
  
## PowerShell commands (for advanced admins)

### Check your sync client configuration status

You can check for sure whether you'll receive this change by running the following PowerShell command:
  
Get-SPOTenantSyncClientRestriction
  
If the result doesn't come back as "OptOut", you will receive this change. For more information, see [Get-SPOTenantSyncClientRestriction](https://go.microsoft.com/fwlink/p/?linkid=855909).
  
### Opt out of the sync update
<a name="BKMK_OptOut"> </a>

We've created a tenant admin PowerShell control that you can use to opt out or opt in to this sync update. 
  
Set-SPOTenantSyncClientRestriction [-GrooveBlockOption \<String\> "OptOut"|"HardOptIn"|"SoftOptIn"] 
  
In particular, to opt out, a tenant would run the command: 
  
Set-SPOTenantSyncClientRestriction -GrooveBlockOption "OptOut" 
  
For information about using PowerShell, see [Introduction to the SharePoint Online Management Shell](introduction-to-the-sharepoint-online-management-shell).
  

