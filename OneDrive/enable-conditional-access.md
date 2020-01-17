---
title: "Pre-provision OneDrive for users in your organization"
ms.reviewer: waynewin
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
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
description: "Learn how to use PowerShell to create OneDrive file storage for your users instead of waiting for the storage space to be automatically provisioned by the service."
---

# Pre-provision OneDrive for users in your organization

By default, the first time that a user browses to their OneDrive it's automatically provisioned for them. In some cases, such as the following, you might want your users' OneDrive locations to be ready beforehand, or pre-provisioned:
  
- Your organization has a custom process for adding new employees, and you want to create a OneDrive when you add a new employee.

- Your organization plans to migrate from SharePoint Server on-premises to Office 365.

- Your organization plans to migrate from another online storage service.

This article describes how to pre-provision OneDrive for your users by using PowerShell.

- For info about setting the default storage size, see [Set the default storage space for OneDrive users](set-default-storage-space.md).

- For info about the storage you get with each plan, see [OneDrive for Business Service Description](/office365/servicedescriptions/onedrive-for-business-service-description.md).
  
> [!IMPORTANT]
> The user accounts that you are pre-provisioning must be allowed to sign in.

## Pre-provision OneDrive for users

1. If you're pre-provisioning OneDrive for many users, create a list of these users and save it as a file. For example, create a text file named Users.txt that contains:

```
    user1@contoso.com
    user2@contoso.com
    user3@contoso.com
```

2. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall �SharePoint Online Management Shell.� <br>On the Download Center page, select your language and then click the Download button. You�ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you�re running the 64-bit version of Windows or the x86 file if you�re running the 32-bit version. If you don�t know, see [Which version of Windows am I running?](https://support.microsoft.com/help/13443/windows-which-operating-system). After the file downloads, run it and follow the steps in the Setup Wizard.

3. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

    > [!NOTE]
    > The PowerShell command Request-SPOPersonalSite works only for users who are allowed to sign in. If you've blocked users from signing in, you can allow them to sign in by running the PowerShell command **Set-MsolUser** using the text file you created in Step 1.

    >```PowerShell
    >Get-Content -path "C:\Users.txt" | foreach{Set-MsolUser -UserPrincipalName $_ -BlockCredential $False}
    >```

4. Run the PowerShell command [Request-SPOPersonalSite](/powershell/module/sharepoint-online/request-spopersonalsite?view=sharepoint-ps), consuming the text file you previously created in Step 1.

    >```PowerShell
    >$users = Get-Content -path "C:\Users.txt"
    >Request-SPOPersonalSite -UserEmails $users
    >```

To verify that OneDrive has been created for your users, see [Get a list of all user OneDrive URLs in your organization](list-onedrive-urls.md).
  
   >[!NOTE]
   >If you are pre-provisioning OneDrive for many users, it might take up to 24 hours for the OneDrive locations to be created. If a    user's OneDrive isn't ready after 24 hours, please contact Support.
  
# Pre-provisioning many users at the same time.

The following snipped of code will pre-provision Onedrive for a large number of users in bigger companies.

```Powershell
    $list = @()
    #Counters
    $i = 0; $j = 0

    #Get licensed Users
    $users=get-msoluser -All | ? {$_.islicensed -eq $true}
    #total Licensed users
    $count = $users.count

    foreach ($u in $users){
        $i++; $j++; 
        Write-Host "$i/$count"

        if ($j -lt 199){
            $upn = $u.userprincipalname
            $list += $upn
        }
        if ($j -gt 199){
            Request-SPOPersonalSite -UserEmails $list
            Start-Sleep -Milliseconds 655
            $list = @()
            $j = 0
        }
    }
```
## See also

[Plan hybrid OneDrive for Business](/SharePoint/hybrid/plan-hybrid-onedrive-for-business)
