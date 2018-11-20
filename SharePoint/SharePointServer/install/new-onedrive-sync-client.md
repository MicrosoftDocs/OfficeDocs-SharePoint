---
title: "Configure syncing with the new OneDrive sync client for Sharepoint 2019"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn how to configure the new OneDrive sync client (OneDrive.exe) for SharePoint Server 2019."
---

# Configure syncing with the new OneDrive sync client

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)]
   
When you deploy SharePoint Server 2019 in your organization, your users can sync their OneDrive for Business files as well as SharePoint team site files by using the new OneDrive sync client (OneDrive.exe) for Windows. Compared with the previous OneDrive for Business sync client (Groove.exe), the new sync client provides:
- Improved performance and reliability
- Files On-Demand
- Support for larger files
- Higher sync limits
- The ability to silently deploy
If your users are already syncing document libraries with the previous OneDrive for Business sync client, they will transition to the new OneDrive sync client automatically.
    
## Requirements

Install SharePoint Server 2019.

Configure OneDrive to update from the Insiders ring to version 18.131.0701.0004 or higher. To do this, do one of the following:
- Join the [Windows Insider program](https://insider.windows.com/) or the [Office Insider](https://products.office.com/office-insider) program.
- Use this [registry key](https://oneclient.sfx.ms/Win/Preview/EnableInsiderUpdates.zip).
  
  
## Configure OneDrive for SharePoint Server 2019

To set up OneDrive with SharePoint Server 2019, configure the following Group Policy objects: 
  
1.	SharePoint on-premises server URL and tenant folder name
The URL will help the sync client locate the SharePoint Server and allows the sync client to authenticate and set up sync. The tenant folder name lets you specify the name of the root folder that will be created in File Explorer. If you don’t supply a tenant name, the sync client will use the first segment of the URL as the name. For example, office.sharepoint.com would become “Office.”
2.	SharePoint prioritization setting for hybrid customers that use SharePoint Online (SPO) and SharePoint on-premises server
This setting lets you specify if the sync client should authenticate against SharePoint Online or the SharePoint on-premises server if the identity exists in both identity providers.
 [Learn how to manage OneDrive using Group Policy](https://docs.microsoft.com/onedrive/use-group-policy)
  
## Differences between syncing files in SharePoint Server and SharePoint Online

If your organization also uses the OneDrive sync client to sync files in Office 365, here’s what will be different for users who sync on-premises files.
  
### Folder names
The OneDrive sync client creates the following folders on users’ computers:
OneDrive – Contoso (for syncing personal My Site files)
Contoso (for syncing SharePoint team site files)

In SharePoint Online, “Contoso” is the tenant name that has been set for the SharePoint Online instance. In SharePoint on-premises, there is no tenant name associated to the instance of SharePoint. You can set the this with the “SharePoint on-premises server URL and tenant folder name” group policy, or the sync client will use the first segment of your SharePoint URL. 
   
### File thumbnails and previews
Thumbnails don’t appear in File Explorer for files synced from SharePoint on-premises. If you enable Files On-Demand, and a file is online-only, a file preview won’t be available. Image files and Office files will not have a thumbnail in File Explorer until the file is downloaded.
  
### Sharing from File Explorer

When users share files and folders from File Explorer, the sharing option will open the browser instead of the Share dialog box. 
  
### Privacy settings

When setting up SharePoint Server, you’ll be prompted to select if clients should send error reports and usage statistics back to Microsoft. If you enable the setting, individual users can opt out by following these steps:
1.	Right-click the OneDrive cloud icon in the notification area, at the far right of the taskbar.
2.	Click **Settings**. 
3.	Click the **Settings** tab, and then clear the option under **Privacy**. 

  


