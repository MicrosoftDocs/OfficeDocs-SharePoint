---
title: "Get a list of all user OneDrive URLs in your organization"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 04/30/2018
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
search.appverid:
- SPO160
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: 8e200cb2-c768-49cb-88ec-53493e8ad80a
description: "Learn how to use PowerShell to display a list of every OneDrive in your organization."
---

# Get a list of all user OneDrive URLs in your organization

This article is for global admins and SharePoint admins in Office 365.
  
## View the list of OneDrive users and URLs in your organization

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, select **Reports**, and then select **Usage**.
    
4. Click the **OneDrive files** tile, or click **Select a report**, and then click **OneDrive usage**.
    
5. In the upper right of the table at the bottom, click **Export**.
    
## Create a list of all the OneDrive URLs in your organization using Microsoft PowerShell
<a name="BKMK_Step2"> </a>

The list you create in these steps will be saved to a text file.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. [Download the SharePoint and Project Client Object Model libraries](https://go.microsoft.com/fwlink/?linkid=872342).
    
4. Save the following text to a text file. For example, you could save it to a file named **GetODSites.txt**. 
    
  ```PowerShell
  # Specifies the URL for your organization's SPO admin service
  $AdminURI = "https://your organization name-admin.sharepoint.com"

  # Specifies the User account for an Office 365 global admin in your organization
  $AdminAccount = "global admin account"
  $AdminPass = "password for global admin account"

  # Specifies the location where the list of URLs should be saved
  $LogFile = 'C:\Users\youralias\Desktop\ListOfMysites.txt'

  # Begin the process
  $loadInfo1 = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client")
  $loadInfo2 = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.Runtime")
  $loadInfo3 = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.UserProfiles")

  # Convert the Password to a secure string, then zero out the cleartext version ;)
  $sstr = ConvertTo-SecureString -string $AdminPass -AsPlainText -Force
  $AdminPass = ""

  # Take the AdminAccount and the AdminAccount password, and create a credential
  $creds = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($AdminAccount, $sstr)

  # Add the path of the User Profile Service to the SPO admin URL, then create a new webservice proxy to access it
  $proxyaddr = "$AdminURI/_vti_bin/UserProfileService.asmx?wsdl"
  $UserProfileService= New-WebServiceProxy -Uri $proxyaddr -UseDefaultCredential False
  $UserProfileService.Credentials = $creds

  # Set variables for authentication cookies
  $strAuthCookie = $creds.GetAuthenticationCookie($AdminURI)
  $uri = New-Object System.Uri($AdminURI)
  $container = New-Object System.Net.CookieContainer
  $container.SetCookies($uri, $strAuthCookie)
  $UserProfileService.CookieContainer = $container
  
# Set the first User profile, at index -1
  $UserProfileResult = $UserProfileService.GetUserProfileByIndex(-1)
  Write-Host "Starting- This could take a while."
  $NumProfiles = $UserProfileService.GetUserProfileCount()
  $i = 1

  # As long as the next User profile is NOT the one we started with (at -1)...
  While ($UserProfileResult.NextValue -ne -1) 
  {
      Write-Host "Examining profile $i of $NumProfiles"
      # Look for the Personal Space object in the User Profile and retrieve it
      # (PersonalSpace is the name of the path to a user's OneDrive for Business site. Users who have not yet created a 
      # OneDrive for Business site might not have this property set.)
      $Prop = $UserProfileResult.UserProfile | Where-Object { $_.Name -eq "PersonalSpace" } 
      $Url= $Prop.Values[0].Value
      # If "PersonalSpace" (which we've copied to $Url) exists, log it to our file...
      if ($Url) {
          $Url | Out-File $LogFile -Append -Force
      }
      # And now we check the next profile the same way...
      $UserProfileResult = $UserProfileService.GetUserProfileByIndex($UserProfileResult.NextValue)
      $i++
  }
  Write-Host "Done!"
  ```

5. Edit the following variables in the beginning of the script file, and use the information that's specific to your organization. The following examples assume that the domain name of your organization is contoso.com.
    
  - **$AdminURI** This specifies the URI for your SharePoint Online admin service, for example,  `https://contoso-admin.sharepoint.com`.
    
  - **$AdminAccount** This specifies a global administrator account in your Office 365 organization, for example,  `admin@contoso.onmicrosoft.com`.
    
  - **$AdminPass** This specifies the password for the account that's specified by **$AdminAccount**, for example,  `"J$P1ter1"`.
    
  - **$LogFile** This specifies the full path of the text file that's created and contains a list of all the OneDrive URLs in your organization. For example, to save this file to the desktop, use  `'C:\Users\<youralias>\Desktop\ListOfMysites.txt'`. 
    
    > [!NOTE]
    > The sample PowerShell scripts provided in this topic aren't supported under any Microsoft standard support program or service. The sample scripts are provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages. 
  
6. Save the text file as a PowerShell script file by changing the file name suffix to .ps1. For example, save the file GetODSites.txt as GetODSites.ps1.
    
7. In the SharePoint Online Management Shell, go to the folder where the script that you created in the previous step is located, and then run the script, for example:
    
      ```
      .\GetODSites.ps1
      ```

    > [!NOTE]
    > If you get an error message about being unable to run scripts, you might need to change your execution policies. For info, see [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255). 
  
After the script successfully completes, a text file is created in the location specified by the **$LogFile** variable in the script. This file contains a list of all OneDrive URLs in your organization. The following text provides an example of how the list of URLs in this file should be formatted. 
  
```
/personal/annb_contoso_onmicrosoft_com/
/personal/carolt_contoso_onmicrosoft_com/
/personal/esterv_contoso_onmicrosoft_com/
/personal/hollyh_contoso_onmicrosoft_com/
/personal/jeffl_contoso_onmicrosoft_com/
/personal/joeh_contoso_onmicrosoft_com/
/personal/kaia_contoso_onmicrosoft_com/

```

## More information
<a name="BKMK_MoreInfo"> </a>

Once you have the URL for a user's OneDrive, you can get more info about it by using the [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326) cmdlet, and change settings by using the [Set-SPOSite](https://go.microsoft.com/fwlink/?linkid=872325) cmdlet . 
  

