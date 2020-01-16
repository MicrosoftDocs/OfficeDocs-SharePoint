---
title: "Change the default sharing link for a site"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
f1_keywords:
- 'WSSCentralAdmin_SharingLinkTypeLearnMore'
- 'SharingLinkTypeLearnMore'
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: 81b763af-f301-4226-8842-8d13bd07face
description: "Learn how to change the default sharing link for a specific site."
---

# Change the default link type for a site

Users can share files and folders in SharePoint and OneDrive by sending a link. They should select a link type based on the people to whom they want to give permission. The following link types are available: 

- Anyone with the link (previously called "anonymous access" or "shareable")
- People in your organization with the link 
- People with existing access
- Specific people 

![Screenshot of Link settings.](media/link-settings.png)

As a global or SharePoint admin, you may want to enable users to send "Anyone" links, but you may not want this to the be the default type of link when users select to share files and folders. You can set the default type of link to something more restrictive, while still allowing users to select other types of links as needed. You can change this setting at the organization level and at the site (previously called "site collection") level. 
  
> [!NOTE]
> The default sharing link setting applies only to libraries that use the new experience.<br>This setting does not affect Outlook Web App, Outlook 2016, or Office clients prior to Office 2016. 


For info about the changing this setting at the organization level, see [File and folder links](turn-external-sharing-on-or-off.md#file-and-folder-links).

  
## Change the default link type for a site

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. In the left pane of the new SharePoint admin center, under **Sites** select **Active sites**.
    
4. Click the site name, and then select the **Policies** tab.

5. Under **External sharing**, select **Edit**.
     
6. Under **Default sharing link type**, clear the **Same as organization-level setting** check box.

    ![Screenshot of site-level default sharing link settings](media/default-sharing-link-type-site.png)

7. Choose the default sharing link setting that you want to use for this site, and then click **Save**.

> [!NOTE]
> You can set the default link type to *People with existing access* by running [Set-SPOSite](https://docs.microsoft.com/powershell/module/sharepoint-online/set-sposite) with the `-DefaultLinkToExistingAccess` parameter.

## See also

[Turn external sharing on or off for a site](change-external-sharing-site.md)
