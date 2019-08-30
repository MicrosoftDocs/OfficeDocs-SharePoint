---
title: "Custom Tiles in SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 8e7535ee-8a38-4878-aaf3-78b669f4aca8
description: "This article describes Custom Tiles which is one of the new features in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1)."
---

# Custom Tiles in SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
In SharePoint Server, users can quickly and easily get to all of their SharePoint and Office 365 workloads directly from the app launcher. Now in addition to those, you can also add your own custom tiles that point to other SharePoint sites, external sites, legacy apps, and more. This makes it easy to find the relevant sites, apps, and resources to do your job
  
This feature is configured on the web app level by an ITPro administrator by using PowerShell cmdlets.
  
> [!NOTE]
> The list for the custom tiles is provisioned at the root level of the web application so anyone will be able to see or remove the list. 
  
## Enable Custom Tiles

The custom tile feature is not enabled by default. To enable the feature, do these steps.
  
1. Verify that you have the following memberships:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance 
    
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated. 
    
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
    If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions.
    
    For additional information about PowerShell permissions, see [Permissions](/powershell/sharepoint/sharepoint-server/sharepoint-server-cmdlets?view=sharepoint-ps) and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. On the **Start** menu, click **All Programs**
    
3. Click **Microsoft SharePoint Products**.
    
4. Click **SharePoint Management Shell**.
    
5. To ensure the feature is available, at the PowerShell command prompt, type the following command:
    
  ```
  Get-SPFeature -Identity CustomTiles
  ```

  > [!NOTE]
  > If the feature is not available, then ensure your SharePoint farm is patched with at least Feature Pack 1 contained in all cumulative updates of SharePoint 2016 of November 2016 and later. To validate this, you can run the following PowerShell command. Your SharePoint build version should be at 16.0.4456.1004 or later.
  
  ```
(Get-SPFarm).BuildVersion
  ```

6. To enable the feature, at the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPFeature -Identity CustomTiles -Url http://web_app -Force
  ```

  > [!NOTE]
  > The URL you provide will be the location of where the Custom Tile list is provisioned, so you may need to provide permission access to the list accordingly. Custom Tiles List will be Created on specified URL on feature enable command as hidden list. 
  
7. Since this list is Created as a Hidden List, browse to https://web_app/Lists/Custom%20Tiles/AllItems.aspx to access Custom tiles list.
    
8. Click **new item** to add a new item to the list. 
    
     ![Displays dialog box to create a new entry for a CustomTile in the November 2016 PU for SharePoint Server 2016](../media/6597a87e-cd66-463e-b405-8897926f9c55.jpg)
  
9. Enter a **Title** for the new tile. The name will appear in the tile. 
    
10. Enter a number for **Tile Order**. This is the order you want the tile to appear after the default three tiles (that is, Newsfeeds, OneDrive, Sites).
    
11. Enter a **Url** for the tile. This is the location where you want your users to go when they select the tile. 
    
12. Enter an **IconURL** for the tile. The recommended size for an icon is 50x50 pixels, however the thumbnail will automatically scale. The image appears on the app launcher.
    
13. Type the name of an **Audience** you want to use this tile. For example, Marketing. 
    
    > [!NOTE]
    > List or library items in SharePoint Server can be targeted to appear only to people who are members of a particular group or audience. An audience can be identified by using SharePoint groups, distribution lists, or security groups or by using a rules-based system to create a global audience. 
  
After you add a new item in the custom tiles list due to caching, it may take up to 24 hours before you can see it appear in the app launcher. If you want to see it immediately, you can run **ClearSuiteLinksCache()** function in the developer browser's console which is displayed by pressing **F12** while in a browser session as displayed in the following diagram. 

  > [!NOTE]
  > The **ClearSuiteLinksCache()** function is not available in SharePoint Server 2019 and will generate an error if used.
  
![Displays the developer browser's console in a browser session](../media/313b5ce5-07df-4fd3-8861-59d3c7635970.jpg)
  
After the **ClearSuiteLinksCache()** function is run, it returns "undefined". 
  
![Displays results in the developer browser's console](../media/12b97d35-e877-40f7-ae0a-73003c0cff47.jpg)
  
You must refresh the page by pressing **F5** or the refresh button ![Displays the Refresh key on the Address toolbar of your browser](../media/8b874097-7bdd-4571-96e8-a3f3ee6af8d4.jpg) on the Address bar of your browser for the tile to now appear in the app launcher. 
  
## Enable Custom Tiles across multiple web applications

If you want to use the same list of custom tiles across multiple web applications, enable the feature on each web application, and then update the web application property **CustomTilesListHostUrl** to the web application that contains the desired custom tiles list. To do this, follow these steps: 
  
1. Verify that you have the following memberships:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance 
    
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated. 
    
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
    If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions.
    
    For additional information about PowerShell permissions, see [Permissions](/powershell/sharepoint/sharepoint-server/sharepoint-server-cmdlets?view=sharepoint-ps) and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. On the **Start** menu, click **All Programs**
    
3. Click **Microsoft SharePoint Products**.
    
4. Click **SharePoint Management Shell**.
    
5. To ensure the feature is available, at the PowerShell command prompt, type the following commands:
    
  ```
  $w = Get-SPWebApplication http://web_app
  $w.Properties.CustomTilesListHostUrl = "http://web_app url"
  $w.Update()
  ```

If you want to unhide list of custom tiles you can do this by using PowerShell.
  
From a PowerShell command prompt, type the follow commands:
  
```
$web = get-spweb "http://web_app"
$list = $web.Lists["Custom Tiles"]
$list.hidden = $false
$list.update()
```

> [!NOTE]
> The List will be visible when site Contents is viewed. 
  
To add this list to Left Navigation pane, do the follow steps:
  
1. Browse to List settings.
    
2. Click on **List** name, description and navigation. 
    
3. Select **Yes** for Navigation setting to display list on **Quick Launch** as displayed with this image. 
    
![Displays Quick Launch settings](../media/22b5e6e8-37c1-4120-9c89-456d06867a6e.jpg)
  

