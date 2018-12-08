---
title: "Get a list of all user OneDrive Urls in your organization"
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

# Get a list of all user OneDrive Urls in your organization

This article is for Global Admins and SharePoint Admins in Office 365.
  
## View the list of OneDrive users and Urls in your organization

1. Sign in to Office 365 as a Global Admin or SharePoint Admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, select **Reports**, and then select **Usage**.
    
4. Click the **OneDrive files** tile, or click **Select a report**, and then click **OneDrive usage**.
    
5. In the upper right of the table at the bottom, click **Export**.
    
## Create a list of all the OneDrive Urls in your organization using Microsoft PowerShell
<a name="BKMK_Step2"> </a>

The list you create in these steps will be saved to a text file.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
      
2. Save the following text to a PowerShell file. For example, you could save it to a file named OneDriveSites.ps1.
    
  ```PowerShell
	$TenantUrl = Read-Host "Enter the SharePoint Online Tenant Admin Url"
	$LogFile = [Environment]::GetFolderPath("Desktop") + "\OneDriveSites.log"
	Connect-SPOService -Url $TenantUrl
	Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like '-my.sharepoint.com/personal/" |select Url | Out-File $LogFile -Force
	Write-Host "Done! File saved as $($LogFile)."
  ```

3. Open the SharePoint Online Management Shell. Navigate to the directory where the script has been saved and run:

```PowerShell
PS C:\>.\OneDriveSites.ps1
```

    > [!NOTE]
    > If you get an error message about being unable to run scripts, you might need to change your execution policies. For info, see [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255). 
	
4. The script will prompt you for the SharePoint Online tenant admin Url. For example, "https://contoso-admin.sharepoint.com" is the Contoso SharePoint Online tenant admin Url.

5. You will then be prompted to log into the tenant. Use a SharePoint Online Administrator or Global Administrator account.

After the script successfully completes, a text file is created in the location specified by the **$LogFile** variable in the script. This file contains a list of all OneDrive Urls in your organization. The following text provides an example of how the list of Urls in this file should be formatted. 
  
```
Url                                                                
---                                                                
https://contoso-my.sharepoint.com/personal/annb_contoso_onmicrosoft_com/
https://contoso-my.sharepoint.com/personal/carolt_contoso_onmicrosoft_com/
https://contoso-my.sharepoint.com/personal/esterv_contoso_onmicrosoft_com/  
https://contoso-my.sharepoint.com/personal/hollyh_contoso_onmicrosoft_com/
```

## More information
<a name="BKMK_MoreInfo"> </a>

Once you have the Url for a user's OneDrive, you can get more info about it by using the [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326) cmdlet, and change settings by using the [Set-SPOSite](https://go.microsoft.com/fwlink/?linkid=872325) cmdlet.
