---
title: "Get a list of all user OneDrive URLs in your organization"
ms.reviewer: 
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
ms.collection: M365-collaboration
ms.assetid: 8e200cb2-c768-49cb-88ec-53493e8ad80a
description: "Learn how to display a list of every OneDrive in your organization."
---

# Get a list of all user OneDrive URLs in your organization

This article is for global and SharePoint admins in Office 365.
  
## View the list of OneDrive users and URLs in your organization

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Reports** \> **Usage**. (You might need to select **Show all** to see the Reports option.) 
    
3. Select the **OneDrive files** tile, or select **Select a report** \> **OneDrive usage**.

    > [!NOTE]
    > If you see GUIDs in the report instead of URLs and names, in the left pane, select **Settings** > **Services & add-ins**, and then select **Reports**. Clear the box **Display anonymous identifiers instead of names in all reports**.
    
4. In the upper right of the table at the bottom, select **Export**.
    
## Create a list of all the OneDrive URLs in your organization using Microsoft PowerShell
<a name="BKMK_Step2"> </a>

The list you create in these steps will be saved to a text file.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br> On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard.
      
2. Save the following text to a PowerShell file. For example, you could save it to a file named OneDriveSites.ps1.
    
     ```PowerShell
    $TenantUrl = Read-Host "Enter the SharePoint Online Tenant Admin Url"
	$LogFile = [Environment]::GetFolderPath("Desktop") + "\OneDriveSites.log"
	Connect-SPOService -Url $TenantUrl
	Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like '-my.sharepoint.com/personal/'" | select Url | Out-File $LogFile -Force
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

Once you have the URL for a user's OneDrive, you can get more info about it by using the [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326) cmdlet, and change settings by using the [Set-SPOSite](https://go.microsoft.com/fwlink/?linkid=872325) cmdlet.
