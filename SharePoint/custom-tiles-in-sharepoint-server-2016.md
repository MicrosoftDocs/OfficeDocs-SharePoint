---
title: Custom Tiles in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 8e7535ee-8a38-4878-aaf3-78b669f4aca8
---


# Custom Tiles in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** This article describes Custom Tiles which is one of the new features in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1).In SharePoint Server 2016, users can quickly and easily get to all of their SharePoint and Office 365 workloads directly from the app launcher. Now in addition to those, you can also add your own custom tiles that point to other SharePoint sites, external sites, legacy apps, and more. This makes it easy to find the relevant sites, apps, and resources to do your jobThis feature is configured on the web app level by an ITPro administrator by using PowerShell cmdlets.
> [!NOTE:]

  
    
    


## Enable Custom Tiles

The custom tile feature is not enabled by default. To enable the feature, do these steps.
1. Verify that you have the following memberships:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance
    
  
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated.
    
  
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
  

    If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions.
    
    For additional information about PowerShell permissions, see  [Permissions](ae4901b4-505a-42a9-b8d4-fca778abc12e.md#section3) and **Add-SPShellAdmin**.
    
  
2. On the **Start** menu, click **All Programs**
    
  
3. Click **Microsoft SharePoint 2016 Products**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. To ensure the feature is available, at the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPFeature -Identity CustomTiles
  ```


    > [!NOTE:]
      

  ```
  
Install-SPFeature -Path <path to CustomTiles>
  ```

6. To enable the feature, at the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPFeature -Identity CustomTiles -Url http://web_app -Force
  ```


    > [!NOTE:]
      
7. Since this list is Created as a Hidden List, browse to http://web_app/lists/custom tiles to access Custom tiles list.
    
  
8. Click **new item** to add a new item to the list.
    
     ![Displays dialog box to create a new entry for a CustomTile in the November 2016 PU for SharePoint Server 2016](images/)
  

  
9. Enter a **Title** for the new tile. The name will appear in the tile.
    
  
10. Enter a number for **Tile Order**. This is the order you want the tile to appear after the default three tiles (that is, Newsfeeds, OneDrive, Sites).
    
  
11. Enter a **Url** for the tile. This is the location where you want your users to go when they select the tile.
    
  
12. Enter an **IconURL** for the tile. The recommended size for an icon is 50 x50 pixels, however the thumbnail will automatically scale. The image appears on the app launcher
    
  
13. Type the name of an **Audience** you want to use this tile. For example, Marketing.
    
    > [!NOTE:]
      
After you add a new item in the custom tiles list due to caching, it may take up to 24 hours before you can see it appear in the app launcher. If you want to see it immediately, you can run **ClearSuiteLinksCache()** function in the developer browser's console which is displayed by pressing **F12** while in a browser session as displayed in the following diagram.
  
    
    
![Displays the developer browser's console in a browser session](images/)
  
    
    
After the **ClearSuiteLinksCache()** function is run, it returns "undefined".
  
    
    
![Displays results in the developer browser's console](images/)
  
    
    
You must refresh the page by pressing **F5** or the refresh button
  
    
    
![Displays the Refresh key on the Address toolbar of your browser](images/)
  
    
    
 on the Address bar of your browser for the tile to now appear in the app launcher.
## Enable Custom Tiles across multiple web applications

If you want to use the same list of custom tiles across multiple web applications, enable the feature on each web application, and then update the web application property **CustomTilesListHostUrl** to the web application that contains the desired custom tiles list. To do this, follow these steps:
1. Verify that you have the following memberships:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance
    
  
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated.
    
  
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
  

    If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions.
    
    For additional information about PowerShell permissions, see  [Permissions](ae4901b4-505a-42a9-b8d4-fca778abc12e.md#section3) and **Add-SPShellAdmin**.
    
  
2. On the **Start** menu, click **All Programs**
    
  
3. Click **Microsoft SharePoint 2016 Products**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. To ensure the feature is available, at the PowerShell command prompt, type the following commands:
    
  ```
  
$w = Get-SPWebApplication http://web_app
$w.Properties.CustomTilesListHostUrl = "http://web_app url"
$w.Update()
  ```

If you want to unhide list of custom tiles you can do this by using PowerShell.From a PowerShell command prompt, type the follow commands:


```

$web = get-spweb "http://web_app"
$list = $web.Lists["Custom Tiles"]
$list .hidden = $false
$list.update()
```


> [!NOTE:]

  
    
    

To add this list to Left Navigation pane, do the follow steps:
1. Browse to List settings.
    
  
2. Click on **List** name, description and navigation.
    
  
3. Select **Yes** for Navigation setting to display list on **Quick Launch** as displayed with this image.
    
  

  
    
    
![Displays Quick Launch settings](images/)
  
    
    

  
    
    

  
    
    

