---
title: "Pre-provision OneDrive for users in your organization"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/21/2018
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
ms.assetid: ceef6623-f54f-404d-8ee3-3ce1e338db07
description: "Learn how to use PowerShell to create OneDrive file storage for your users instead of waiting for the storage space to be automatically provisioned by the service."
---

# Pre-provision OneDrive for users in your organization

By default, the first time that a user browses to their OneDrive it's automatically provisioned for them. In some cases, such as the following, you might want your users' OneDrive locations to be ready beforehand, or pre-provisioned:
  
- Your organization has a custom process for adding new employees, and you want to create a OneDrive when you add a new employee.
    
- Your organization plans to migrate from SharePoint Server on-premises to Office 365.
    
- Your organization plans to migrate from another online storage service.
    
This article describes how to pre-provision OneDrive for your users by using PowerShell. 
  
> [!NOTE]
> You can also pre-provision OneDrive for your users by using the REST API or CSOM. For more information, see [So you want to programmatically provision Personal Sites (OneDrive for Business) in Office 365](https://go.microsoft.com/fwlink/p/?LinkId=404444) and the section titled "Use the ProfileLoader.CreatePersonalSiteEnqueueBulk method to provision personal sites and OneDrive for Business for multiple users" in [What's new for developers in social and collaboration features in SharePoint](https://go.microsoft.com/fwlink/p/?LinkId=404445). 
  
## Pre-provision OneDrive for users

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Download and install the [SharePoint Online Client Components SDK](https://go.microsoft.com/fwlink/p/?LinkId=506692).
    
3. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
    > [!NOTE]
    > If you get an error message about being unable to run scripts, you might need to change your execution policies. For info, see [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255). 
  
4. Copy the following code and paste it into a text editor such as Notepad:
    
  ```
  <#
  .SYNOPSIS
   This script adds an entry for each user specified in the input file 
   into the OneDrive provisioning queue
   
  .DESCRIPTION
   This script reads a text file with a line for each user. 
   Provide the User Principal Name of each user on a new line.
   An entry will be made in the OneDrive provisioning queue for each
   user up to 200 users.
  .EXAMPLE
   .\BulkEnqueueOneDriveSite.ps1 -SPOAdminUrl https://contoso-admin.sharepoint.com -InputfilePath C:\users.txt 
  .PARAMETER SPOAdminUrl
   The URL for the SharePoint Admin center
   https://contoso-admin.sharepoint.com
  .PARAMETER InputFilePath
   The path to the input file.
   The file must contain 1 to 200 users
   C:\users.txt
  .NOTES
   This script needs to be run by a SharePoint Online Tenant Administrator
   This script will prompt for the username and password of the Tenant Administrator
  #>
  param
  (
      #Must be SharePoint Administrator URL
      [Parameter(Mandatory = $true)]
      [ValidateNotNullOrEmpty()]
      [string] $SPOAdminUrl,
      
      [Parameter(Mandatory = $true)]
      [ValidateNotNullOrEmpty()]
      [string] $InputFilePath
  )
  [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client") | Out-Null
  [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.Runtime") | Out-Null
  [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.UserProfiles") | Out-Null
  $ctx = New-Object Microsoft.SharePoint.Client.ClientContext($SPOAdminUrl)
  $Users = Get-Content -Path $InputFilePath
  if ($Users.Count -eq 0 -or $Users.Count -gt 200)
  {
      Write-Host $("Unexpected user count: [{0}]" -f $Users.Count) -ForegroundColor Red
      return 
  }
  $web = $ctx.Web
  Write-Host "Please enter a Tenant Admin username" -ForegroundColor Green
  $username = Read-Host
  Write-Host "Please enter your password" -ForegroundColor Green
  $password = Read-Host -AsSecureString
  $ctx.Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username,$password )
  $ctx.Load($web)
  $ctx.ExecuteQuery()
  $loader = [Microsoft.SharePoint.Client.UserProfiles.ProfileLoader]::GetProfileLoader($ctx)
  $ctx.ExecuteQuery()
  $loader.CreatePersonalSiteEnqueueBulk($Users)
  $loader.Context.ExecuteQuery()
  Write-Host "Script Completed" 
  
  ```

    Notice that comments are included in the code to describe the script and the parameters that are used in it. They will not affect the running of the PowerShell script.
    
5. Save the text file and then change the file name extension to .ps1. In this example, we use the name **BulkEnqueueOneDriveSite.ps1**. 
    
6. In a text editor such as Notepad, create a file that includes the Office 365 user accounts for which you want to provision OneDrive. Each user account must be on a separate line.
    
    Save the file with the name **UserInput.txt**.
    
    > [!NOTE]
    > Each Input file is limited to 200 users. If you need to provision OneDrive for more than 200 users, create multiple input files (for example, UserInput1.txt, UserInput2.txt, etc.). 
  
7. In the SharePoint Online Management Shell, change to the directory where you saved the BulkEnqueueOneDriveSite.ps1 PowerShell script.
    
8. Run the following command:
    
  ```
  .\BulkEnqueueOneDriveSite.ps1 -SPOAdminUrl <The URL for the SharePoint Admin center> -InputfilePath <location of your UserInput file> 
  ```

    For example:
    
  ```
  .\BulkEnqueueOneDriveSite.ps1 -SPOAdminUrl https://contoso-admin.sharepoint.com -InputfilePath C:\UserInput1.txt 
  ```

    Running the script will prompt you for the Office 365 credentials, which you will need to enter.
    
    When the script has finished, the PowerShell pane shows the status as **Completed**.
    
9. If you have additional User Input files, rerun the script and change the -InputfilePath parameter to the location of the other User Input file.
    
To verify that OneDrive has been created for your users, see [How to display a list of OneDrive for Business site collections](list-onedrive-urls.md).
  
> [!NOTE]
> If you are pre-provisioning OneDrive for many users, it might take some time for the OneDrive locations to be created. 
  
## See also

[Plan hybrid OneDrive for Business](https://support.office.com/article/b140bc4c-f54d-4b5a-9409-a3bece4a9cf9)

