---
title: "Restore a deleted OneDrive"
ms.author: v-thehay
author: SteyerTHaynie
manager: scotv
ms.date: 4/24/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: e487f40d-5321-46a8-9504-92b600b65cb9
description: "If a work or school account is deleted from the Office 365 admin center, or is removed through Active Directory synchronization, their OneDrive site is marked for deletion. After a 93 day retention period, their site is moved to their recycle bin."
---

# Restore a deleted OneDrive

If a work or school account is deleted from the Office 365 admin center, or is removed through Active Directory synchronization, their OneDrive site is marked for deletion. After a 93 day retention period, their site is moved to their recycle bin.
  
## Why can't I restore a OneDrive for Business site through Admin UI?

The user's recycle bin is not visible to Administrators, and it is not possible to restore or recover deleted OneDrive sites through the Admin UI.
  
> [!NOTE]
> OneDrive sites remain in the recycle bin for 93 days before being permanently deleted. 
  
### Recovery process

Admins should use PowerShell to confirm that the OneDrive site is in the recycle bin and is available to be restored.
  
> [!NOTE]
> To perform the steps that follow, you will need to have the SharePoint Management Shell installed. 
  
1. Open PowerShell
    
2. Connect to the service:
    
  - **Connect-SPOService -Url** \<https://yourdomain-admin.sharepoint.com\> 
    
  - Sign in with administrator credentials
    
3. Determine if the site is available for restore
    
  - If you know the URL of the deletedsite, use the following command:
    
    **Get-SPODeletedSite -Identity \<ODBSiteUrl\>**
    
  - If you do not know the URL of the deleted site, use the following command:
    
    **Get-SPODeletedSite -IncludeOnlyPersonalSite | FT url**
    
  - If the site appears in the results, it is in the recycle bin and available to be restored.
    
4. Once the site is located, restore the site to an active state:
    
    **Restore-SPODeletedSite -Identity \<ODBSiteURL\>**
    
5. Assign an owner to the site to access the needed data:
    
    **Set-SPOUser -Site** \<ODBSiteURL\> -LoginName \<UPNofDesiredAdmin\> -IsSiteCollectionAdmin $True 
    
### Action after data recovery

Once you have obtained the data from the restored site, we recommend that you delete the site to prevent an orphaned site from remaining in your tenant.
  
> [!NOTE]
> This deletion is permanent, and the site will not be available to be restored again. 
  
Delete the site using this cmdlet:
  
 **Remove-SPOSite -Identity \<ODBSiteURL\>**
  
### More information

Read more about [OneDrive retention and deletion](onedrive-retention-and-deletion.md)
  
See also [Restore a deleted site collection](https://support.office.com/article/91c18651-c017-47d1-9c27-3a22f325d6f1).
  

