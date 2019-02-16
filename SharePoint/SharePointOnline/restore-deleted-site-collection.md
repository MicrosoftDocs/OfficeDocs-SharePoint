---
title: "Restore deleted sites"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 91c18651-c017-47d1-9c27-3a22f325d6f1
description: "Learn how to restore deleted sites"
---

# Restore deleted sites

Deleted sites are retained for 93 days. After 93 days, sites and all their content and settings are permanently deleted, including lists, libraries, pages, and any subsites.
  
> [!NOTE]
> If you need to retain content for a minimum period of time to comply with industry regulations or internal policies, you can create a retention policy to keep a copy of it in the Preservation Hold library. For info, see [Overview of retention policies](/office365/securitycompliance/retention-policies).<br> For info about restoring items within a site, see [Restore items in the Recycle Bin of a SharePoint site](https://support.office.com/article/6df466b6-55f2-4898-8d6e-c0dff851a0be). <br> To create a new site that uses the same URL as a deleted site, you must first permanently delete the deleted site. For info, see [Permanently delete a deleted site](restore-deleted-site-collection.md#permanently-delete-a-site-by-using-powershell).<br>For info about restoring deleted sites in SharePoint Server, see [Restore deleted site collections using Microsoft Powershell](/powershell/module/sharepoint-server/restore-spdeletedsite). 
  
 
## Restore a deleted site in the new SharePoint admin center

In the new SharePoint admin center, you can delete and restore all the new types of sites. You can do this even as a SharePoint admin - you don't need to be a global admin.

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Try it now** to open the new SharePoint admin center. 

4. In the left pane, under **Sites**, select **Deleted sites**.
 
    ![Deleted sites in the new SharePoint admin center](media/b195b8c7-ee2b-4a02-92cb-ed61899edd24.png)

    > [!NOTE]
    > You can sort and filter deleted sites the same way you sort and filter sites on the Active sites page. You can also sort and filter deleted sites by Time deleted.
    
5. Select the site you want to restore.

6. Select **Restore**. (If you don't see the Restore button, make sure only one site is selected. The button won't appear if multiple sites are selected.)
 
> [!NOTE]
> Restoring a site that belongs to an Office 365 group restores the Office 365 group and all its resources. Note that the other group resources are retained for only 30 days, whereas the site is retained for 93. If the other group resources have been deleted, you can use the PowerShell command [Remove-SPODeletedSite](/powershell/module/sharepoint-online/remove-spodeletedsite) to permanently delete the site.   
    
For more info about the new SharePoint admin center, see [Get started with the new SharePoint admin center](get-started-new-admin-center.md).
  
 
## Restore a deleted site in the classic SharePoint admin center
<a name="__toc315681383"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
3. On the site collection page of the classic SharePoint admin center, select **Recycle Bin**.
    
4. Select the check box next to the site collection that you want to restore.
    
5. On the ribbon, click **Restore Deleted Items**.
    
## Permanently delete a site by using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 

2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
      ```PowerShell
      Remove-SPODeletedSite -Identity https://contoso.sharepoint.com/sites/sitetoremove
      ```
 (Where https://contoso.sharepoint.com/sites/sitetoremove is the URL of the site you want to permanently delete). For more info about using this command, see [Remove-SPODeletedSite](/powershell/module/sharepoint-online/remove-spodeletedsite).