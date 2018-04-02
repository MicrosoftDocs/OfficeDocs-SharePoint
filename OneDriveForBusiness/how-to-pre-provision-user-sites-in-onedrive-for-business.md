---
title: "How to pre-provision user sites in OneDrive for Business"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 8/10/2017
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: ceef6623-f54f-404d-8ee3-3ce1e338db07
description: "Learn how to use PowerShell to create OneDrive file storage for your users instead of waiting for the storage space to be automatically provisioned by the service."
---

# How to pre-provision user sites in OneDrive for Business

By default, the first time that a user browses to their newsfeed, site, or a OneDrive link, a OneDrive for Business site is automatically provisioned for them. In some cases, such as the following, you might want OneDrive for Business sites to be ready beforehand, or pre-provisioned:
  
- Your organization has a custom process for adding new employees, and you want to create OneDrive for Business sites when you add new employees.
    
- Your organization plans to migrate from on-premises to Office 365.
    
- Your organization plans to migrate from another online storage service or repository.
    
This article describes how to pre-provision OneDrive for Business sites for your users by using PowerShell. This procedure will walk you through the following :
  
1. Create a PowerShell script to pre-provision OneDrive for Business sites from the provided code.
    
2. Create an input file that includes your users for which you want to pre-provision OneDrive for Business sites.
    
3. Run the PowerShell script to create OneDrive for Business sites for the users that are in the input file.
    
> [!NOTE]
> You can also pre-provision OneDrive for Business sites by using the REST API or CSOM. For more information, see [So you want to programmatically provision Personal Sites (OneDrive for Business) in Office 365](https://go.microsoft.com/fwlink/p/?LinkId=404444) and the section titled "Use the ProfileLoader.CreatePersonalSiteEnqueueBulk method to provision personal sites and OneDrive for Business for multiple users (My Site Host administrators on SharePoint Online only)" in [What's new for developers in social and collaboration features in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=404445). 
  
## Before you begin
<a name="begin"> </a>

Before you begin this task, review the following information about prerequisites:
  
- [Set up the SharePoint Online Management Shell environment](https://support.office.com/article/7b931221-63e2-45cc-9ebc-30e042f17e2c).
    
- Download and install the [SharePoint Online Client Components SDK](https://go.microsoft.com/fwlink/p/?LinkId=506692).
    
- Verify that you're signed in as a global admin in Office 365, and that you have a SharePoint Online license assigned to yourself.
    
- Sign in as a member of the Administrators group on the server on which you are running the PowerShell script.
    
## Pre-provision OneDrive for Business sites for users
<a name="begin"> </a>

1. Copy the following code, paste it into a text editor such as Notepad, save it, and name the file **BulkEnqueueOneDriveSite.ps1** to create the PowerShell script: 
    
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
    
2. In a text editor such as Notepad, create a file that includes the Office 365 user accounts for which you want to provision OneDrive for Business sites. Each user account must be on a separate line.
    
    Save the file with the name **UserInput.txt**.
    
    > [!NOTE]
    > Each Input file is limited to 200 users. If you need to provision OneDrive for Business sites for more than 200 users, create multiple input files (for example, UserInput1.txt, UserInput2.txt, etc.). 
  
3. Open the SharePoint Online Management Shell.
    
4. Change to the directory where you saved the BulkEnqueueOneDriveSite.ps1 PowerShell script.
    
5. At the PowerShell command prompt, use the following command:
    
  ```
  .\BulkEnqueueOneDriveSite.ps1 -SPOAdminUrl <The URL for the SharePoint Admin center> -InputfilePath <location of your UserInput file> 
  ```

    For example:
    
  ```
  .\BulkEnqueueOneDriveSite.ps1 -SPOAdminUrl https://contoso-admin.sharepoint.com -InputfilePath C:\UserInput1.txt 
  ```

    Running the script will prompt you for the Office 365 credentials, which you will need to enter.
    
    When the script has finished, the PowerShell pane shows the status as **Completed**.
    
6. If you have additional User Input files, rerun the script and change the -InputfilePath parameter to the location of the other User Input file.
    
To verify if your users' OneDrive for Business sites have been created, see [How to display a list of OneDrive for Business site collections](https://support.office.com/article/0406c1eb-0ae6-458b-a4a1-c630872db10a).
  
> [!NOTE]
> If you are creating OneDrive for Business sites for a number a users, note that it might take some time for all of your users sites to be created. 
  
## Related Topics
<a name="begin"> </a>

[Plan hybrid OneDrive for Business](https://support.office.com/article/b140bc4c-f54d-4b5a-9409-a3bece4a9cf9)
  

