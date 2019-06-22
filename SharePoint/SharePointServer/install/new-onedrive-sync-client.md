---
title: "Configure syncing with the new OneDrive sync client for SharePoint 2019"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: ITPro
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

1. Install SharePoint Server 2019
2. Install the OneDrive sync client version 18.131.0701.0004 or higher ([download](https://go.microsoft.com/fwlink/p/?LinkId=248256))
  
## Configure OneDrive for SharePoint Server 2019

To set up OneDrive with SharePoint Server 2019, you can either use Group Policy or set the registry keys directly. 

For settings that require a tenant ID, you can use **OP1** if you sync a single domain. Do not use this if you sync multiple domains. 

The Known Folder Move settings don't work for SharePoint Server.

### Using Group Policy

Configure the following two Group Policy objects to configure OneDrive to be used with SharePoint 2019:
  
**Specify SharePoint Server URL and organization name**

The URL will help the sync client locate the SharePoint Server and allows the sync client to authenticate and set up sync.
The organization name lets you specify the name of the root folder that will be created in File Explorer. If you don’t supply an organization name, the sync client will use the first segment of the URL as the name. For example, office.sharepoint.com would become “office”.

**Specify the OneDrive location in a hybrid environment**

This setting lets you specify if the sync client should authenticate against SharePoint Online or the SharePoint on-premises server if the identity exists in both identity providers.

You should be able to find these Group Policy objects using the Group Policy Editor (gpedit.msc) when navigating to Computer Configuration\Administrative Templates\OneDrive. If the OneDrive folder is not present, you can add the OneDrive Group Policy template by coping the following two files from the OneDrive installation folder after you have installed the latest OneDrive sync client on that computer:

- C:\Users\\*username*\AppData\Local\Microsoft\OneDrive\\*onedrivesyncclientversion*\adm\OneDrive.admx
to
C:\Windows\PolicyDefinitions\OneDrive.admx
- C:\Users\\*username*\AppData\Local\Microsoft\OneDrive\\*onedrivesyncclientversion*\adm\OneDrive.adml
to
C:\Windows\PolicyDefinitions\en-US\OneDrive.adml

To automate this copying using PowerShell, you could use:

```powershell
Get-ChildItem -Recurse -Path "$env:LOCALAPPDATA\Microsoft\OneDrive" -Filter "OneDrive.admx" | ? FullName -like "*\adm\OneDrive.admx" | Copy-Item -Destination "$env:WINDIR\PolicyDefinitions" -Force
Get-ChildItem -Recurse -Path "$env:LOCALAPPDATA\Microsoft\OneDrive" -Filter "OneDrive.adml" | ? FullName -like "*\adm\OneDrive.adml" | Copy-Item -Destination "$env:WINDIR\PolicyDefinitions\en-US" -Force
```

More information:
[Learn how to manage OneDrive using Group Policy](/onedrive/use-group-policy)

### By setting the registry keys

Alternatively, you can also directly configure the following underlying registry keys:

|**Key**|**Type**|**Value**|
|:-----|:-----|:-----|
|HKLM:\\Software\Policies\Microsoft\OneDrive\SharePointOnPremPrioritization|DWORD (32-bit)|1|
|HKLM:\\Software\Policies\Microsoft\OneDrive\SharePointOnPremFrontDoorUrl|String|https://sharepoint.contoso.local|
|HKLM:\\Software\Policies\Microsoft\OneDrive\SharePointOnPremTenantName|String|Contoso|
 
## Differences between syncing files in SharePoint Server and SharePoint Online

If your organization also uses the OneDrive sync client to sync files in Office 365, here’s what will be different for users who sync on-premises files.
  
### Folder names
The OneDrive sync client creates the following folders on users’ computers:
OneDrive – Contoso (for syncing personal My Site files)
Contoso (for syncing SharePoint team site files)

In SharePoint Online, “Contoso” is the tenant name that has been set for the SharePoint Online instance. In SharePoint on-premises, there is no tenant name associated to the instance of SharePoint. You can set the this with the “Specify SharePoint Server URL and organization name” group policy, or the sync client will use the first segment of your SharePoint URL. 
   
### File thumbnails and previews
Thumbnails don’t appear in File Explorer for files synced from SharePoint on-premises. If you enable Files On-Demand, and a file is online-only, a file preview won’t be available. Image files and Office files will not have a thumbnail in File Explorer until the file is downloaded.
  
### Sharing from File Explorer

When users share files and folders from File Explorer, the sharing option will open the browser instead of the Share dialog box. 
  
### Privacy settings

When setting up SharePoint Server, you’ll be prompted to select if clients should send error reports and usage statistics back to Microsoft. If you enable the setting, individual users can opt out by following these steps:
1.	Right-click the OneDrive cloud icon in the notification area, at the far right of the taskbar.
2.	Click **Settings**. 
3.	Click the **Settings** tab, and then clear the option under **Privacy**. 

  


