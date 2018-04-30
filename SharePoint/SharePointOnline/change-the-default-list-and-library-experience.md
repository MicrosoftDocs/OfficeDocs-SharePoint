---
title: "Change the default list and library experience"
ms.author: kaarins
author: kaarins
ms.date: 4/26/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- SPO160
- GSA150
- BSA160
- GSP150
ms.assetid: a0d90eaf-5755-4b8d-96ee-9e25bdf9114e
description: "Admin instructions for how to switch SharePoint Online libraries from new to classic experience and back, using the Admin center or Windows PowerShell. "
---

# Change the default list and library experience

You may notice a change in the look and navigation of your document libraries and lists. This new experience is faster, has additional phone and tablet features, and simpler navigation. As an administrator, you may want to switch the default experience back to the previous (classic experience) for a time. Keep in mind that users can change the experience in specific libraries or sites back to new if they choose. A change to settings at the library and list level overrides changes at the site, site collection, and tenant level.
  
> [!NOTE]
> This article is for admins who want to change the default experience for users. If you are an individual user and you want to return to classic experience, click **Return to classic SharePoint** in the bottom, left corner of the page. To exit the classic experience, click **Exit classic experience** in the bottom, left corner of the page. 
  
For information about how library and list owners can switch the list and library experience, see [Switch the default experience for lists or document libraries from new or classic](https://support.office.com/article/66dac24b-4177-4775-bf50-3d267318caa9).
  
## Change the default experience for all lists and document libraries

1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4.md) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. Choose **settings**.
    
5. Next to **SharePoint Lists and Libraries experience**, select either **Classic experience** or **New experience (auto-detect)**.
    
    ![Setting for default List and Library experience](media/e153485c-9351-4b09-8989-c00395246b66.png)
  
## Change the default experience at the site and site collection level by using Windows PowerShell

 **Check for customizations that affect lists or library pages**
  
One reason you may want to change the default experience at the site and site collection level is because you have customizations that affect list or library pages and represent business-critical functionality. If you want to check for these kinds of customizations to help you determine which sites and site collections you want to change the default for, you must use a Windows PowerShell script with a CSOM (Client-side object model) wrapper. The following script detects customactions that deploy custom scripts.
  
1. Verify that you meet the following minimum requirements:
    
  - You are a global administrator
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
2. Copy the following code and paste it into a text editor, such as Notepad. For this article, we will name the script file, CustomActions.ps1.
    
    > [!NOTE]
    > This script needs to be run separately for each website you want to check CustomActions for. The placeholder names indicated in \< \> need to be change to meet your organizational requirements. > There are commented lines, denoted by the pound sign (#), in the sections of script for site collection level and site levels. To run the appropriate script, remove the pound sign (#) in front of the lines in the section that you want to change the experience for. 
  
  ```
  # This file uses CSOM. Replace the paths below with the path to CSOM on this computer.
  # If CSOM is in the user's downloads folder, you only have to replace the <username> placeholder.
  Add-Type -Path "C:\Users\<username>\downloads\Microsoft.SharePointOnline.CSOM.16.1.5026.1200\lib\net45\Microsoft.SharePoint.Client.dll"
  Add-Type -Path "C:\Users\<username>\downloads\Microsoft.SharePointOnline.CSOM.16.1.5026.1200\lib\net45\Microsoft.SharePoint.Client.Runtime.dll"
  # All strings in braces < >are placeholders that you must replace with the appropriate strings.
  $webUrl = 'https://<domain>.sharepoint.com/<relative-path-to-website>'
  $username = '<username>@<domain>.onmicrosoft.com'
  $password = Read-Host -Prompt "Password for $username" -AsSecureString
  [Microsoft.SharePoint.Client.ClientContext]$clientContext = New-Object Microsoft.SharePoint.Client.ClientContext($webUrl)    
  $clientContext.Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, $password)
  $site = $clientContext.Site;
  $customActions = $site.UserCustomActions
  $clientContext.Load($customActions)
  $clientContext.ExecuteQuery()
  $first = $true
  foreach($customAction in $customActions)
  {
      if($customAction.Location -eq "scriptlink" -and -Not ([string]::IsNullOrEmpty($customAction.ScriptBlock)))
      {
          if ($first)
          {
              Echo " "
                  Echo ($webUrl + " has the following inline JavaScript custom actions")
          $first = $false
          }
          Echo $customAction.Title
      }
  }
  
  ```

3. Save the file, naming it  `CustomActions.ps1`.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is  `.ps1`
  
4. Change to the directory where you saved the file.
    
5. At the Windows PowerShell command prompt, type the following command:
    
     `./CustomActions.ps1`
    
 **Change the default experience for sites and site collections**
  
To change the default experience for document libraries on a site collection or site level, you must use a Windows PowerShell script with a CSOM (Client-side object model) wrapper, as follows.
  
1. Verify that you meet the following minimum requirements:
    
  - You are a global administrator
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
2. Copy the following code and paste it into a text editor, such as Notepad. For this article, we will name the script file, DocLib.ps1.
    
    > [!NOTE]
    > There are commented lines, denoted by the pound sign (#), in the sections of script for site collection level and site levels. To run the appropriate script, remove the pound sign (#) in front of the lines in the section that you want to change the experience for. 
  
  ```
  ##The first two lines of the script load the CSOM model:
  Add-Type -Path "C:\Users\{username}\downloads\Microsoft.SharePointOnline.CSOM.16.1.5026.1200\lib\net45\Microsoft.SharePoint.Client.dll"
  Add-Type -Path "C:\Users\{username}\downloads\Microsoft.SharePointOnline.CSOM.16.1.5026.1200\lib\net45\Microsoft.SharePoint.Client.Runtime.dll"
  $webUrl = 'https://{domain}.sharepoint.com/[optional path to subweb]'
  $username = Read-Host -Prompt "Enter or paste the site collection administrator's full O365 email, for example, name@domain.onmicrosoft.com" 
  $password = Read-Host -Prompt "Password for $username" -AsSecureString
  [Microsoft.SharePoint.Client.ClientContext]$clientContext = New-Object Microsoft.SharePoint.Client.ClientContext($webUrl)
  $clientContext.Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, $password)
  # To apply the script to the site collection level, uncomment the next two lines.
  #$site = $clientContext.Site; 
  #$featureguid = new-object System.Guid "E3540C7D-6BEA-403C-A224-1A12EAFEE4C4"
  # To apply the script to the website level, uncomment the next two lines, and comment the preceding two lines.
  #$site = $clientContext.Web;
  #$featureguid = new-object System.Guid "52E14B6F-B1BB-4969-B89B-C4FAA56745EF" 
  # To turn off the new UI by default in the new site, uncomment the next line.
  #$site.Features.Add($featureguid, $true, [Microsoft.SharePoint.Client.FeatureDefinitionScope]::None);
  # To re-enable the option to use the new UI after having first disabled it, uncomment the next line.
  # and comment the preceding line.
  #$site.Features.Remove($featureguid, $true);
  $clientContext.ExecuteQuery();
  
  ```

3. Save the file, naming it  `DocLib.ps1`.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is  `.ps1`
  
4. Change to the directory where you saved the file.
    
5. At the Windows PowerShell command prompt, type the following command:
    
     `./DocLib.ps1`
    
For additional information about Windows PowerShell, see [Using Windows PowerShell](https://msdn.microsoft.com/powershell/scripting/getting-started/fundamental/using-windows-powershell).
  

