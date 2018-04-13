---
title: "How to display a list of OneDrive for Business site collections"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 9/27/2017
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- SPO160
- ODB160
- ODB150
- GOB150
- GOB160
ms.assetid: 8e200cb2-c768-49cb-88ec-53493e8ad80a
description: "Learn how to use PowerShell to display a list of every OneDrive in your organization."
---

# How to display a list of OneDrive for Business site collections

This article provides the administrator a PowerShell script that will display every OneDrive for Business site in your organization. 
  
[Step 1: Connect SharePoint Online Management Shell to your organization](how-to-display-a-list-of-onedrive-for-business-site-collections.md#BKMK_Step1)
  
[Step 2: Collect a list of all OneDrive for Business sites by using Windows PowerShell](how-to-display-a-list-of-onedrive-for-business-site-collections.md#BKMK_Step2)
  
See [More information](how-to-display-a-list-of-onedrive-for-business-site-collections.md#BKMK_MoreInfo) at the end of this topic for tips about using this script. 
  
## Before you begin
<a name="BKMK_Before"> </a>

- Install the SharePoint Online Management Shell. For information, see [Set up the SharePoint Online Management Shell Windows PowerShell environment](https://go.microsoft.com/fwlink/p/?LinkID=286318).
    
    > [!IMPORTANT]
    > An tenant administrator who grants themselves site collection administrator permission for a users' OneDrive for Business site can open a users' OneDrive for Business document libraries and perform the same tasks as the owner. It's important to control and monitor who has been assigned tenant administrator permission in your organization. 
  
- The PowerShell script requires that the SharePoint client object model (CSOM) is installed. This is indicated by the following line:  `[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client")`.
    
- The sample PowerShell scripts provided in this topic aren't supported under any Microsoft standard support program or service. The sample scripts are provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.
    
## Step 1: Connect SharePoint Online Management Shell to your organization
<a name="BKMK_Step1"> </a>

1. On your local computer, open the SharePoint Online Management Shell, and run the following command:
    
  ```
  $credentials = Get-Credential
  ```

    In the **Windows PowerShell Credential Request** dialog box, type the user name and password for your Office 365 global administrator account, and then click **OK**.
    
2. Run the following command to connect the Shell to your SharePoint Online organization:
    
  ```
  Connect-SPOService -Url https://<yourdomain>-admin.sharepoint.com -credential $credentials
  ```

3. To verify that you are connected to your SharePoint Online organization, run the following command to connect to your organization's root site:
    
  ```
  Get-SPOSite https://<yourdomain>.sharepoint.com
  ```

## Step 2: Collect a list of all OneDrive for Business sites by using Windows PowerShell
<a name="BKMK_Step2"> </a>

In this step, you run a PowerShell script to create a list of all OneDrive for Business sites in your organization. This list is saved to a text file.
  
1. Save the following text to a text file. For example, you could save it to a file named **GetOD4BSites.txt**. 
    
  ```
  # Specifies the URL for your organization's SPO admin service
  $AdminURI = "https://your organization name-admin.sharepoint.com"
  # Specifies the User account for an Office 365 global admin in your organization
  $AdminAccount = "global admin account"
  $AdminPass = "password for global admin account"
  # Specifies the location where the list of MySites should be saved
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
  # Sets the first User profile, at index -1
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

2. Edit the following variables in the beginning of the script file, and use the information that's specific to your organization. The following examples assume that the domain name of your organization is contoso.com.
    
  - **$AdminURI** This specifies the URI for your SharePoint Online admin service, for example,  `https://contoso-admin.sharepoint.com`.
    
  - **$AdminAccount** This specifies a global administrator account in your Office 365 organization, for example,  `admin@contoso.onmicrosoft.com`.
    
  - **$AdminPass** This specifies the password for the account that's specified by **$AdminAccount**, for example,  `"J$P1ter1"`.
    
  - **$LogFile** This specifies the full path of the text file that's created and contains a list of all the OneDrive for Business sites in your organization. For example, to save this file to the desktop, use  `'C:\Users\<youralias>\Desktop\ListOfMysites.txt'`. 
    
3. Save the text file as a PowerShell script file by changing the file name suffix to .ps1. For example, save the file GetOD4BSites.txt as GetOD4BSites.ps1.
    
4. In SharePoint Online Management Shell, go to the folder where the script that you created in the previous step is located, and then run the script, for example:
    
  ```
  .\GetOD4BSites.ps1
  ```

After the script successfully completes, a text file is created in the location specified by the **$LogFile** variable in the script. This file contains a list of all OneDrive for Business sites in your SharePoint Online organization. The following text provides an example of how the list of sites in this file should be formatted. You can remove sites from this file if necessary. 
  
```
/personal/annb_contoso_onmicrosoft_com/
/personal/carolt_contoso_onmicrosoft_com/
/personal/esterv_contoso_onmicrosoft_com/
/personal/hollyh_contoso_onmicrosoft_com/
/personal/jeffl_contoso_onmicrosoft_com/
/personal/joeh_contoso_onmicrosoft_com/
/personal/kaia_contoso_onmicrosoft_com/

```

[Return to top](how-to-display-a-list-of-onedrive-for-business-site-collections.md#BKMK_Intro)
  
## More information
<a name="BKMK_MoreInfo"> </a>

You can connect to a OneDrive for Business site by using the [Get-SPOSite](https://technet.microsoft.com/library/fp161380.aspx) cmdlet, and can change ownership by using the [Set-SPOSite](https://technet.microsoft.com/library/fp161394.aspx) cmdlet . Once you are an owner of the site, you can use regular SharePoint Client Side Object Model (CSOM) to take further management operations. 
  

