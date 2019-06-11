---
title: "Manage site storage limits"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: 77389c2c-8e7e-4b16-ab97-1c7103784b08
description: "Learn how to use the SharePoint admin center to manage site collection storage quotas."
---

# Manage site storage limits

The amount of SharePoint Online space your organization has is based on your number of users (see [SharePoint Online Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)). If you're a global admin in Office 365, you can [Change storage space for your subscription](/office365/admin/subscriptions-and-billing/add-storage-space) if you run out. 
  
## Set automatic or manual site storage limits
<a name="__toc365547981"> </a>

By default, your SharePoint storage is available in a central pool from which all sites can draw. You, as a global or SharePoint admin, don't need to divvy up storage space or reallocate space based on usage. That's all handled automatically: sites use what they need when they need it, up to a maximum of 25 terabytes (TB) per site (previously called "site collection"). If you previously set storage limits manually and switch to using pooled storage, SharePoint resets all the limits to 25 TB. 

If you prefer to fine tune the storage space allocated to each site, you can set your storage management option to "manual" and specify individual site storage limits. 
  
   
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 
    
3. In the left pane of the new SharePoint admin center, select **Settings**.
    
4. Select **Site storage limits**.

![Managing site storage limits](media/site-storage-limits.png)
     
5. Select **Automatic** or **Manual**, and then select **Save**.
    
## Manage individual site storage limits
<a name="__toc365547981"> </a>

Follow these steps to specify individual site storage limits when your storage management option is set to "manual." We recommend that you also set an email alert so that you and other site admins can be notified when sites are nearing the storage limit.  
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. On the **Active sites** page of the new SharePoint admin center, select a site, select the ellipsis (...), and then select **Storage**. 

![Changing the storage limit for a site](media/site-storage-limit.png)
    
4. Enter the maximum storage in GB for the site. 

  > [!NOTE]
  > The max value you can enter is 25600 GB, although this may be more space than your organization has. To see how much space comes with your subscription, see [SharePoint Online Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).<br> If you set site storage limits in PowerShell, you enter them in MB. The values are converted and rounded down to the nearest integer to appear in GB in both the new and classic SharePoint admin centers. So a value of 5000 MB becomes 4 GB. The minimum storage limit is 1 GB, so if you set a value of less than 1024 MB by using PowerShell, it will be rounded up to 1 GB.
    
5. Make sure **Notifications** is turned on to send an email to site admins when the site approaches the storage limit. Then enter a value as a percent for how full you want the storage to be when the email is sent. 
 
  
6. Select **Save**.
    
### Monitor site storage limits by using PowerShell

If you manage storage limits manually, you need to regularly monitor them to make sure they aren't affecting site performance. We recommend that you also set up your own alert emails to notify site admins before a site reaches the limit. The built-in storage quota warning emails are typically sent weekly for sites that have reached the specified warning level. So site admins often receive the storage quota warning email too late. For example, if the Disk Quota Warning timer job (which triggers the warning email) is scheduled weekly and sends the email warning every Sunday, but a site reaches the quota warning limit on Monday, the site admin doesn't receive the alert email for 6 days. This site could reach the maximum storage limit and be set to read-only before the site admin receives the alert email. 
  
You can use the following Microsoft PowerShell script to monitor your sites. This script pulls the data, composes, and then sends a storage warning alerts to the site admin.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Copy the following text with the variable declarations, and paste it into a text editor, such as Notepad. You must set all of the input values to be specific to your organization. Save the file, and then rename it "GetEmailWarning.ps1". 
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1. 
  
  ```PowerShell
#Connect to SharePoint admin center using an admin account
#Specify the URL to your SharePoint admin center site, e.g. https://contoso-admin.sharepoint.com

$url = 'https://contoso-admin.sharepoint.com'

#Specify a folder path to output the results into
$path = '.\'

#SMTP details
$Smtp = '<SmtpServer>'
$From = '<SenderEmailAddress>'  
$To = '<RecipientEmailAddress>'
$Subject = 'Site Storage Warning'  
$Body = 'Storage Usage Details'

if($url -eq '') {
    $url = Read-Host -Prompt 'Enter the SharePoint admin center URL'
}

Connect-SPOService -Url $url

#Local variable to create and store output file  
$filename = (Get-Date -Format o | foreach {$_ -Replace ":", ""})+'.csv'  
$fullpath = $path+$filename

#Enumerating all sites and calculating storage usage  
$sites = Get-SPOSite
$results = @()

foreach ($site in $sites) {
    $siteStorage = New-Object PSObject
    
    $percent = $site.StorageUsageCurrent / $site.StorageQuota * 100  
    $percentage = [math]::Round($percent,2)

    $siteStorage | Add-Member -MemberType NoteProperty -Name "Site Title" -Value $site.Title
    $siteStorage | Add-Member -MemberType NoteProperty -Name "Site Url" -Value $site.Url
    $siteStorage | Add-Member -MemberType NoteProperty -Name "Percentage Used" -Value $percentage
    $siteStorage | Add-Member -MemberType NoteProperty -Name "Storage Used (MB)" -Value $site.StorageUsageCurrent
    $siteStorage | Add-Member -MemberType NoteProperty -Name "Storage Quota (MB)" -Value $site.StorageQuota

    $results += $siteStorage
    $siteStorage = $null
}

$results | Export-Csv -Path $fullpath -NoTypeInformation

#Sending email with output file as attachment  
Send-MailMessage -SmtpServer $Smtp -To $To -From $From -Subject $Subject -Attachments $fullpath -Body $Body -Priority high
```

4. Where:

  - **$url** is the URL of your SharePoint admin center. If the `$url` variable is left empty, you will be prompted to enter the URL of your admin center site.
  
  - **$path** is the file system path you want the CSV file to output to.
   
  - **\<SmtpServer\>** is the name of your SMTP mail server. 
    
  - **\<SenderEmailAddress\>** is the global admin or SharePoint admin account that appears in the From line in the warning email. 
    
  - **\<RecipientEmailAddress\>** is the admin account that will receive the email warning. 
    
5. In SharePoint Online Management Shell, change to the local directory where you saved the script file.
    
  ```
  ./GetEmailWarning.ps1
  ```

   After the script successfully completes, a text file is created in the location that you specified in the **$path** variable in the script. 
    
   > [!NOTE]
   > If you get an error message about being unable to run scripts, you might need to change your execution policies. For info, see [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255). 
  
  
## See also

[SharePoint Online limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)

