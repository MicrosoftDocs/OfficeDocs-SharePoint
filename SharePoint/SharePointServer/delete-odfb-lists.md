---
title: "Deleting OneDrive for Business experience settings"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: o365-solutions
ms.custom: 
localization_priority: Priority
description: "Learn about deleting OneDrive for Business experience settings."
---

# Deleting OneDrive for Business experience settings

The recommended way to delete all OneDrive for Business experience settings and information is to remove the user's OneDrive for Business site, after reassigning any retained files to other users.

An admin can delete these lists by using [PowerShell Script](/powershell/scripting/powershell-scripting?view=powershell-6) and [SharePoint Client-Side Object Model (CSOM)](/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-client-library-code) commands. All of the needed CSOM assemblies are included in the SharePointPnPPowerShellOnline Microsoft PowerShell module.

You can adapt the script included in this article to meet the your needs. For example, you can extract the information for user1@contoso.com as follows:

1.	Assign yourself permissions to the user's OneDrive for Business account. This can be done in the Microsoft 365 admin center as described here.

2.  Install the required Microsoft PowerShell modules:

    `Install-Module SharePointPnPPowerShellOnline`

    `Install-Module CredentialManager`

3.	Run the DeleteODBLists PowerShell script below (or a customized version of the script); for example:

    `$ODBSite = "https://contoso-my.sharepoint.com/personal/user1_contoso_com"`

    `DeleteODBLists -siteUrl $ODBSite`

The script will permanently delete the hidden lists containing these settings. 
  
> [!IMPORTANT]
> Do not run this script on OneDrive for Business accounts for active users that are still in the organization. 

## DeleteODBLists script
Copy the contents below and paste them into a text file. Save the file as DeleteODBLists.ps1.

> [!NOTE]
> If you see an error about an assembly not being loaded, double-check the path to the latest version of the SharePointPnPPowerShellOnline PowerShell Module as defined in the Add-Type Path parameters. The path may be different on your computer or you may be using a different version of the module (the module version is part of the path).

```powershell
#DeleteODBLists
#Deletes ODB experience settings, stored in several SharePoint Lists
param([string]$siteUrl, [bool]$useStoredCreds=$true)
Add-Type -Path "C:\Program Files\WindowsPowerShell\Modules\SharePointPnPPowerShellOnline\2.26.1805.0\Microsoft.SharePoint.Client.dll"
Add-Type -Path "C:\Program Files\WindowsPowerShell\Modules\SharePointPnPPowerShellOnline\2.26.1805.0\Microsoft.SharePoint.Client.Runtime.dll"

if (!$siteUrl)
{
    Write-Host "Please specify a OneDrive site using -siteUrl."
    return
}

if ($useStoredCreds)
{
    Write-Host "Retrieving stored Windows credentials for $siteUrl."
    $cred = Get-StoredCredential -Target $siteUrl
    if (!$cred)
    {
        Write-Host "Didn't find stored credential for $siteUrl. Please provide credentials to connect."
        $cred = Get-Credential
    }
}
else
{
   $cred = Get-Credential
}

$credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($cred.UserName,$cred.Password)
$webURL = $siteUrl
$ctx = New-Object Microsoft.SharePoint.Client.ClientContext($webURL)
$ctx.Credentials = $credentials

#Root folders of lists to export
$SWMRoot = "Reference " #starts with this string
$notificationsRoot = "notificationSubscriptionHiddenList6D1E55DA25644A22"
$activityFeedRoot = "userActivityFeedHiddenListF4387007BE61432F8BDB85E6"
$accessRequestsRoot = "Access Requests"
$microfeedRoot = "PublishedFeed"
$SPHomeCacheRoot = "SharePointHomeCacheList"
$sharingLinksRoot = "Sharing Links"
$socialRoot = "Social"


#Get all lists in the web
try{
    $lists = $ctx.web.Lists
    $ctx.load($lists)
    $ctx.executeQuery()
}
catch{
	write-host "$($_.Exception.Message)" -foregroundcolor red
}


#Process all lists and identify the settings lists to be deleted
$listsToDelete = @()
foreach($list in $lists)
{
    $ctx.load($list)
    $ctx.load($list.RootFolder)
    $ctx.executeQuery()
    $listTitle = [string]$list.Title
    $listRoot = $list.RootFolder.Name
    $listTemplateId = $list.TemplateFeatureId
    
    Write-host ("Processing List: " + $list.Title + " with " + $list.ItemCount + " items").ToUpper() -ForegroundColor Yellow
    Write-host (">> List Root Folder: " + $listRoot) -ForegroundColor Yellow

    if ($listRoot.StartsWith($SWMRoot,"CurrentCultureIgnoreCase") -and $list.ItemCount -ge 1)
    {
        Write-Host ">> Found: Shared With Me List" -ForegroundColor Green
        $listDetails = @{listType = "Shared With Me List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $notificationsRoot)
    {
        Write-Host ">> Found: Notifications List" -ForegroundColor Green
        $listDetails = @{listType = "Notifications List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $activityFeedRoot)
    {
        Write-Host ">> Found: User Activity Feed List" -ForegroundColor Green
        $listDetails = @{listType = "User Activity Feed List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $accessRequestsRoot)
    {
        Write-Host ">> Found: Access Requests List" -ForegroundColor Green
        $listDetails = @{listType = "Access Requests List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $microfeedRoot)
    {
        Write-Host ">> Found: MicroFeed List" -ForegroundColor Green
        $listDetails = @{listType = "Microfeed List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $SPHomeCacheRoot)
    {
        Write-Host ">> Found: SharePoint Home Cache List" -ForegroundColor Green
        $listDetails = @{listType = "SharePoint Home Cache List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $sharingLinksRoot)
    {
        Write-Host ">> Found: Sharing Links List" -ForegroundColor Green
        $listDetails = @{listType = "Sharing Links List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
    elseif ($listRoot -eq $socialRoot)
    {
        Write-Host ">> Found: Social List" -ForegroundColor Green
        $listDetails = @{listType = "Social List"; listTitle = $listTitle; listRoot = $listRoot; listTemplateId = $listTemplateId}
        $listsToDelete += $listDetails
    }
}

#Retrieve web features
$webFeatures = $ctx.Web.Features 
$ctx.Load($webFeatures)
$ctx.ExecuteQuery()

#Export list function
function deleteList
{
    Param ([string] $listTitle, [string] $listTemplateId)

    Write-Host ("Deleting List: " + $listTitle).ToUpper() -ForegroundColor Red

    #Remove features the list may depend on
    $webfeatures.Remove($listTemplateId, $true)
    $ctx.executeQuery()

    #Set the list to allow deletion
	$list = $lists.GetByTitle($listTitle)
    $list.AllowDeletion = $true
    $list.Update()
    $ctx.executeQuery()
    
    #Delete the list    
    $list.DeleteObject()
    $ctx.executeQuery()
}

#Delete all target lists
foreach ($list in $listsToDelete)
{
    deleteList -listTitle $list["listTitle"] -listTemplateId $list["listTemplateId"]
}
```
