---
title: "Change a site address (preview)"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
f1_keywords:
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- FRP150
- MET150
ms.assetid: aa93f89b-ffce-4edb-aa89-22b16d6915a7
description: "Learn how to change the URL of a SharePoint site."
---

# Change a site address

As a global or SharePoint admin in your organization, you can change the URL for the following types of sites:

- Office 365 group-connected team sites
- Modern team sites that don't belong to an Office 365 group
- Communication sites
- Classic team sites

You can't change the URL of sites that are locked or on hold. 

You can change only the address of the site within the URL, for example:

https://contoso.sharepoint.com/sites/*projectx*  
to
https://contoso.sharepoint.com/sites/*projecty* 

You can't change the domain ("contoso" in the previous example) or any other part of the path. For example, you can't move the site from "/sites" to "/teams."

It can take about 10 minutes to change the site address (depending on the size of the site), and the site will be read-only during this time. We recommend changing addresses during times when the site is not heavily used. 

For this preview, you can change the address of up to 10 sites at a time. To change an additional site address, wait for another change to finish. 

## Change a site address in the new SharePoint admin center

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  
    
2. In the left pane of the admin center, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.).
 
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, select **Active sites**.

5. Click the site name to open the details pane.

6. In the Properties list, next to URL, select **Edit**.

    ![Changing the address of a site from /teams](media/change-site-address.png)

7. Enter the new site address, and then select **Save**.

## Rename site addresses by using Microsoft PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command to verify that the site can be renamed:

    ```PowerShell
    Start-SPOSiteContentRename -Identity <SiteUrL> -NewSiteUrl <NewSiteUrl> -ValidationOnly
    ```

4. Run the following command to rename the site:

    ```PowerShell
    Start-SPOSiteContentRename -Identity <SiteUrL> -NewSiteUrl <NewSiteUrl> -ValidationOnly
    ```

For more info about this cmdlet, see <link to PowerShell reference article>


