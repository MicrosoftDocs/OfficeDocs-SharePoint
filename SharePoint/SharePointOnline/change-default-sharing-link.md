---
title: "Change the default link type when users get links for sharing"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/17/2018
ms.audience: Admin
ms.topic: article
f1_keywords:
- 'WSSCentralAdmin_SharingLinkTypeLearnMore'
- 'SharingLinkTypeLearnMore'
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: 81b763af-f301-4226-8842-8d13bd07face
description: "When a user wants to share a document or folder, they can get a link and send it to others."
---

# Change the default link type when users get links for sharing

When a user wants to share a document or folder, they can get a link to it to send to others.
  
SharePoint Online supports three types of links: Anonymous access links (accessible by anyone), internal links (accessible only by users within your organization) and direct links (accessible only by users who you specify when you create the link). As a SharePoint admin, you may want to enable users to send anonymous access links (as these provide the smoothest experience) but you may not want it to be the default link when the user opens the **Get a link** dialog box. 
  
You can set the default type of link to something more restrictive, while still allowing users to select other types of links as needed. This setting can be configured both globally for SharePoint Online and at the site collection level. The global setting acts as a default for the site collections. As a SharePoint admin, you can change this setting for any site collection.

This setting applies only to modern sites.
  
> [!NOTE]
> This setting does not affect Outlook Web App, Outlook 2016, or Office clients prior to Office 2016. 
  
To change the setting in the classic SharePoint Online admin center:
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
## Change the default link type (SharePoint Online global setting)

1. In the left pane, select **sharing**.
    
2. Under **Default link type** choose the option you want to show by default when a user gets a link. 
    
    ![Default link type dialog box](media/4dc58d77-dccd-474f-b0fb-8ff8b3f1c088.png)
  
3. Under **Default link permission** choose whether you want the default permission to be view or edit. 
    
    ![Screenshot of default link permissions which are view and edit.](media/17172082-7cc4-44e4-9b73-3a0ea9acc577.png)
  
## Change the default link type (site collection setting)

1. In the left pane, select **site collections**.
    
2. Select the site collection that you want to change, and then select **Sharing**.
    
3. Under **Default link type**, clear the **Respect default organization setting** check box, and then choose the option you want to show by default when a user gets a link. 
    
    ![Screenshot of default link type settings for a site collection](media/348a8751-421c-4591-9b6b-6d1d381521cd.png)
  
4. Under **Default link permission**, clear the **Respect default organization setting** check box, and then choose whether you want the default permission to be view or edit. 
    
    ![Screenshot of default link permissions setting for a site collection](media/6e585416-019e-4c14-a057-0fd7e7b3e1f6.png)
  
5. Select **Save**.
    

