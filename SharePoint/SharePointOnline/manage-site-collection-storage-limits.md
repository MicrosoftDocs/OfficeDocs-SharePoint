---
title: "Manage site collection storage limits"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection: Strat_SP_admin
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: 77389c2c-8e7e-4b16-ab97-1c7103784b08
description: "Learn how to use the SharePoint admin center to manage storage and resource usage quotas for your site collections."
---

# Manage site collection storage limits

The amount of SharePoint Online space your organization has is based on your number of users (see [SharePoint Online Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)). If you're a global admin in Office 365, you can [Change storage space for your subscription](/office365/admin/subscriptions-and-billing/add-storage-space) if you run out. 
  
## Set automatic or manual site storage limits
<a name="__toc365547981"> </a>

By default, your SharePoint storage is available in a central pool from which all sites can draw. You, as a global or SharePoint admin, don't need to divvy up storage space or reallocate space based on usage. That's all handled automatically: sites use what they need when they need it, up to a maximum of 25 terabyte (TB) per site collection. If you previously set storage limits manually and switch to using pooled storage, SharePoint resets all the limits to 1 TB. 

If you prefer to fine tune the storage space allocated to each site collection, you can set your storage management option to "manual" and specify individual site collection storage limits. 
  
> [!IMPORTANT]
> SharePoint Online storage is now calculated in gigabytes (GB). [More info](manage-site-collection-storage-limits.md#storagecalculation). 
    
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Admin centers** \> **SharePoint**. If this opens the classic SharePoint admin center, select **Try it now** to open the new SharePoint admin center.
    
3. Select **Settings** in the left pane.
    
4. Select **Site storage limits**.
     
5. Select **Automatic** or **Manual**, and then select **Save**.
    
## Manage individual site collection storage limits
<a name="__toc365547981"> </a>

Follow these steps to specify individual site collection storage limits when your storage management option is set to "manual." We recommend that you also set an email alert so that you and other site collection admins can be notified when site collections are nearing the storage limit.  
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Admin centers** \> **SharePoint**. If this opens the classic SharePoint admin center, select **Try it now** to open the new SharePoint admin center.
    
3. On the **Active sites** page, select a site and then select **Storage**. 
    
5. Enter the maximum storage in GB for the site.
    
6. Make sure **Notifications** is turned on to send an email to site collection administrators when the site  approaches the storage limit. Then enter a value as a percent for how full you want the storage to be when the email is sent. 
 
  
7. Select **Save**.
    
### Monitor site collection storage limits by using PowerShell

If you manage storage limits manually, you need to regularly monitor them to make sure they aren't affecting site performance. We recommend that you also set up your own alert emails to notify site collection admins before a site collection reaches the limit. The built-in storage quota warning emails are typically sent weekly to site collections that have reached the specified warning level. So site collection admins often receive the storage quota warning email too late. For example, if the Disk Quota Warning timer job (which triggers the warning email) is scheduled weekly and sends the email warning every Sunday, but a site collection reaches the quota warning limit on Monday, the site collection admin doesn't receive the alert email for 6 days. There is a chance that this site collection can reach the maximum storage limit before the site collection admin receives the alert email. This could cause the site collection to be set to read-only and stop production.
  
You can use the following Microsoft PowerShell script to monitor your site collections. This script pulls the data, composes, and then sends a storage warning alerts to the site collection administrator.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Copy the following text with the variable declarations, and paste it into a text editor, such as Notepad. You must set all of the input values to be specific to your organization. Save the file, and then rename it "GetEmailWarning.ps1". 
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file with the extension .ps1. 
  
  ```
  #Connect to SharePoint admin center using admin account  $username = "<global or SharePoint admin account>"  $password = ConvertTo-SecureString "<Password>" -AsPlainText -Force  $cred = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, $password)  Connect-SPOService -Url <SharePoint admin center URL> -Credential $cred  #Local variable to create and store output file  $filename = Get-Date -Format o | foreach {$_ -replace ":", ""}  $result = "<Local folder path>"+$filename+".txt"  #SMTP and Inbox details  $smtp = "<smtpserver>"  $from = "<sender email>"  $to = "<recipient email>"  $subject = "Alert : PFA Site Collection Quota Usage details"  $body = "PFA quota usage details"  #Enumerating all site collections and calculating storage usage  $sites = Get-SPOSite -detailed  foreach ($site in $sites)  {  $percent = $site.StorageUsageCurrent / $site.StorageQuota * 100  $percentage = [math]::Round($percent,2)  Write-Output "$percentage %         $($site.StorageUsageCurrent)kb of $($site.StorageQuota)kb        $($site.url)" | Out-File $result -Append  }  #Sending email with output file as attachment  sleep 5  Send-MailMessage -SmtpServer $smtp -to $to -from $from -subject $subject -Attachments $result -body $body -Priority high
  ```

4. Where:
    
  - **\<global or SharePoint admin account\>** is the username for the account that has the global admin or SharePoint admin role in Office 365. 
    
  - **\<password\>** is the password for the global or SharePoint admin account. 
    
  - **\<SharePoint admin center URL\>** is the URL for your SharePoint admin center. 
    
  - **\<local folder path\>** is the local path for the folder where you want the data saved. 
    
  - **\<smtpserver\>** is the name of your SMTP mail server. 
    
  - **\<sender email\>** is the global admin or SharePoint admin account that appears in the From line in the warning email. 
    
  - **\<recipient email\>** is the admin account that will receive the email warning. 
    
5. In SharePoint Online Management Shell, change to the local directory where you saved the script file.
    
  ```
  ./GetEmailWarning.ps1
  ```

   After the script successfully completes, a text file is created in the location that you specified in the **\<Local folder path\>** variable in the script. 
    
   > [!NOTE]
   > If you get an error message about being unable to run scripts, you might need to change your execution policies. For info, see [About Execution Policies](https://go.microsoft.com/fwlink/?linkid=869255). 
  
## How SharePoint storage is calculated
<a name="storagecalculation"> </a>

Previously, SharePoint storage was calculated in megabytes (MB). Now it's calculated in gigabytes (GB) using only full integers. If you previously set your storage quota in MB, it will be converted to GB (1024 MB=1 GB) and rounded down to the nearest integer. So a value of 5000 MB becomes 4 GB. A minimum of 1 GB can be set per site collection. If you set your SharePoint storage quota by using PowerShell, that value will be rounded up to the nearest integer GB to prevent a value of less than one GB turning into 0 GB.
  
## See also
<a name="storagecalculation"> </a>

[SharePoint Online limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)

