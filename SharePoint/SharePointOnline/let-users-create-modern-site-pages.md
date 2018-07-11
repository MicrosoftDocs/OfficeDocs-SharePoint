---
title: "Let users create modern site pages"
ms.author: loreenl
author: LoreenLa
manager: pamgreen
ms.date: 4/19/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_SP_modern
search.appverid:
- SPO160
- BSA160
ms.assetid: c41d9cc8-c5c0-46b4-8b87-ea66abc6e63b
description: "Learn how to allow or prevent users from adding pages on SharePoint sites."
---

# Let users create modern site pages

Using SharePoint Online pages is a great way to share ideas using images, Excel, Word and PowerPoint documents, video, and more. Users can [Add a page to a site](https://support.office.com/article/b3d46deb-27a6-4b1e-87b8-df851e503dec) quickly and easily, and they look great on any device. 
  
If you're a global or SharePoint admin in Office 365, you can allow or prevent the creation of SharePoint Online site pages by users. You can do this organization-wide by changing settings in the SharePoint admin center, or at the site level by using a Microsoft PowerShell script.
  
> [!NOTE]
> The following procedures are for SharePoint pages only. When you allow creation of site pages, the **Add a page** command in the **Settings** menu creates new site pages. If you turn off the ability to create site pages, users can still add a SharePoint page from the **New** menu on the Home page and add from the classic page to a Wiki library using the same command. 
  
## Allow or prevent creation of site pages at the organization level in the SharePoint admin center

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. In the left pane, choose **settings**.
    
5. Next to **Site pages**, select either **Allow users to create site pages** or **Prevent users from creating site pages**.
    
## Prevent users from creating modern pages on a specific site by using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Install the [SharePoint Online Client Components SDK](https://www.microsoft.com/en-us/download/details.aspx?id=42038).
    
3. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
    > [!NOTE]
    > Read [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255) and make sure you run the SharePoint Online Management Shell as an administrator and the correct execution policy to run unsigned scripts. 
  
4. Copy the following code and paste it into a text editor, such as Notepad. 
    
  ```
  # Load SharePoint Online Client Components SDK Module
  Import-Module 'C:\Program Files\Common Files\microsoft shared\Web Server Extensions\16\ISAPI\Microsoft.SharePoint.Client.dll'
  # Set script constants
  $sitePagesFeatureIdString = 'B6917CB1-93A0-4B97-A84D-7CF49975D4EC'
  # Set up client context
  $userName = Read-Host "Username"
  $password = Read-Host "Password" -AsSecureString
  $siteUrl = Read-Host "Site Url"
  $webUrl = Read-Host "Server-Relative Web Url"
  $context = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)
  $credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($userName, $password)
  $context.Credentials = $credentials
  # Get the list of existing features
  $web = $context.Site.OpenWeb($webUrl)
  $features = $web.Features
  $context.Load($features)
  $context.ExecuteQuery()
  # Verify that the Site Pages feature is present in the web
  if(($features | ? { $_.DefinitionId -eq $sitePagesFeatureIdString }).Count -eq 0)
  {
  	Write-Host "The Site Pages feature is already disabled in this web"
  	return
  }
  # Remove the Site Pages feature from the web
  $features.Remove((new-object 'System.Guid' $sitePagesFeatureIdString), $false)
  $context.ExecuteQuery()
  # Verify that the Site Pages feature is no longer present in the Web
  $web = $context.Site.OpenWeb($webUrl)
  $features = $web.Features
  $context.Load($features)
  $context.ExecuteQuery()
  if(($features | ? { $_.DefinitionId -eq $sitePagesFeatureIdString }).Count -eq 0)
  {
  	Write-Host "The Site Pages feature has been successfully disabled"
  }
  else
  {	
  	throw "The Site Pages feature failed to be disabled"
  }
  
  ```

5. Save the text file, and then change its extension. In this example, we name it SitePagesOut.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
6. Change to the directory where you saved the file.
    
7. Run the following command:
    
  ```
  ./SitePagesOut.ps1
  ```

8. The script will prompt you for a **SiteUrl** and **WebUrl**. 
    
    If you have a site such as "https://contoso.sharepoint.com/sites/marketing/northwindcompete"
    
    For the **SiteUrl** you would enter:  `https://contoso.sharepoint.com/sites/marketing`
    
    And for the **WebUrl** you would enter  `sites/marketing/northwindcompete`
    
## Allow users to create modern pages on a specific site by using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Install the [SharePoint Online Client Components SDK](https://www.microsoft.com/en-us/download/details.aspx?id=42038).
    
3. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
    > [!NOTE]
    > Read [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255) and make sure you run the SharePoint Online Management Shell as an administrator and the correct execution policy to run unsigned scripts. 
  
4. Copy the following code and paste it into a text editor, such as Notepad. 
    
  ```
  # Load SharePoint Online Client Components SDK Module
  Import-Module 'C:\Program Files\Common Files\microsoft shared\Web Server Extensions\16\ISAPI\Microsoft.SharePoint.Client.dll'
  # Set script constants
  $sitePagesFeatureIdString = 'B6917CB1-93A0-4B97-A84D-7CF49975D4EC'
  # Set up client context
  $userName = Read-Host "Username"
  $password = Read-Host "Password" -AsSecureString
  $siteUrl = Read-Host "Site Url"
  $webUrl = Read-Host "Server-Relative Web Url"
  $context = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)
  $credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($userName, $password)
  $context.Credentials = $credentials
  # Get the list of existing features
  $web = $context.Site.OpenWeb($webUrl)
  $features = $web.Features
  $context.Load($features)
  $context.ExecuteQuery()
  # Verify that the Site Pages feature is not present in the web
  if(($features | ? { $_.DefinitionId -eq $sitePagesFeatureIdString }).Count -gt 0)
  {
  	Write-Host "The Site Pages feature is already enabled in this web"
  	return
  }
  # Add the Site Pages feature back to the web
  $features.Add((new-object 'System.Guid' $sitePagesFeatureIdString), $false, [Microsoft.SharePoint.Client.FeatureDefinitionScope]::None)
  $context.ExecuteQuery()
  # Verify that the Site Pages feature is now present in the web
  $web = $context.Site.OpenWeb($webUrl)
  $features = $web.Features
  $context.Load($features)
  $context.ExecuteQuery()
  if(($features | ? { $_.DefinitionId -eq $sitePagesFeatureIdString }).Count -gt 0)
  {
  	Write-Host "The Site Pages feature has been successfully enabled"
  }
  else
  {
  	throw "The Site Pages feature failed to be enabled"
  }
  
  ```

5. Save the text file, and then change its extension. In this example, we name it SitePagesIn.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
6. Change to the directory where you saved the file.
    
7. Run the following command:
    
  ```
  ./SitePagesIn.ps1
  ```

8. The script will prompt you for a **SiteUrl** and **WebUrl**. 
    
    If you have a site such as "https://contoso.sharepoint.com/sites/marketing/northwindcompete"
    
    For the **SiteUrl** you would enter:  `https://contoso.sharepoint.com/sites/marketing`
    
    And for the **WebUrl** you would enter  `sites/marketing/northwindcompete`
    

