---
title: "Pre-provision OneDrive for users in your organization"
ms.reviewer: waynewin
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
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
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: ceef6623-f54f-404d-8ee3-3ce1e338db07
ms.custom: seo-marvel-apr2020
description: "Learn how to use PowerShell to create OneDrive file storage for your users instead of waiting for the storage space to be automatically provisioned by the service."
---

# Pre-provision OneDrive for users in your organization

By default, the first time that a user browses to their OneDrive it's automatically created (provisioned) for them. In some cases, such as the following, you might want your users' OneDrive locations to be ready beforehand, or pre-provisioned:

- Your organization has a custom process for adding new employees, and you want to create a OneDrive when you add a new employee.

- Your organization plans to migrate from SharePoint Server on-premises to Microsoft 365.

- Your organization plans to migrate from another online storage service.

This article describes how to pre-provision OneDrive for your users by using PowerShell.

- For info about setting the default storage size, see [Set the default storage space for OneDrive users](set-default-storage-space.md).

- For info about the storage you get with each plan, see [OneDrive Service Description](/office365/servicedescriptions/onedrive-for-business-service-description).

> [!IMPORTANT]
> The user accounts that you're pre-provisioning must be allowed to sign in and must also have a SharePoint license assigned.
> To provision OneDrive by using this cmdlet, you must be a global or SharePoint administrator and must be assigned a SharePoint license.


> [!NOTE]
> If you're pre-provisioning OneDrive for a large number of users, it might take multiple days for the OneDrive locations to be created. 

## Pre-provision OneDrive for users

1. If you're pre-provisioning OneDrive for many users, create a list of these users and save it as a file. For example, create a text file named Users.txt that contains:

    ```
    user1@contoso.com
    user2@contoso.com
    user3@contoso.com
    ```

2. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

3. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

    > [!NOTE]
    > The PowerShell command Request-SPOPersonalSite works only for users who are allowed to sign in. If you've blocked users from signing in, you can allow them to sign in by running the PowerShell command **Set-MsolUser** using the text file you created in Step 1.
    >
    >```PowerShell
    >Get-Content -path "C:\Users.txt" | ForEach-Object { Set-MsolUser -UserPrincipalName $_ -BlockCredential $False }
    >```

4. Run the PowerShell command [Request-SPOPersonalSite](/powershell/module/sharepoint-online/request-spopersonalsite?view=sharepoint-ps&preserve-view=true), consuming the text file you previously created in Step 1.

    ```PowerShell
    $users = Get-Content -path "C:\Users.txt"
    Request-SPOPersonalSite -UserEmails $users
    ```

To verify that OneDrive has been created for your users, see [Get a list of all user OneDrive URLs in your organization](list-onedrive-urls.md).


## Pre-provision OneDrive for all licensed users in your organization

The following code snippet will pre-provision OneDrive in batches of 199.

```PowerShell
$Credential = Get-Credential
Connect-MsolService -Credential $Credential
Connect-SPOService -Credential $Credential -Url https://contoso-admin.sharepoint.com

$list = @()
#Counters
$i = 0


#Get licensed users
$users = Get-MsolUser -All | Where-Object { $_.islicensed -eq $true }
#total licensed users
$count = $users.count

foreach ($u in $users) {
    $i++
    Write-Host "$i/$count"

    $upn = $u.userprincipalname
    $list += $upn

    if ($i -eq 199) {
        #We reached the limit
        Request-SPOPersonalSite -UserEmails $list -NoWait
        Start-Sleep -Milliseconds 655
        $list = @()
        $i = 0
    }
}

if ($i -gt 0) {
    Request-SPOPersonalSite -UserEmails $list -NoWait
}
```

## Related topics

[Plan hybrid OneDrive](/SharePoint/hybrid/plan-hybrid-onedrive-for-business)
