---
ms.date: 04/24/2024
title: "Create a site"
ms.reviewer: metorres
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'TellMe_Admin'
- 'O365P_SitesMgmtModern'
- 'O365M_SitesMgmtModern'
- 'O365E_SitesMgmtModern'
- 'How To'
- 'seo-marvel-apr2020'
- admindeeplinkSPO
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- m365initiative-spsitemanagement
search.appverid:
- SPO160
- MOE150
- MED150
- MBS150
- MET150
ms.assetid: 3a3d7ab9-5d21-41f1-b4bd-5200071dd539
description: "This article describes how global and SharePoint admins can create sites."
---

# Create a site

This article describes how being at least a [SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365 can create sites (previously called "site collections") in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>. For info about creating sites and adding users and groups to them by using Microsoft PowerShell, see [Create SharePoint sites and add users with PowerShell](/microsoft-365/enterprise/create-sharepoint-sites-and-add-users-with-powershell).
  
For info about creating site collections in SharePoint Server, see [Create a site collection in SharePoint Server](../SharePointServer/sites/create-a-site-collection.md).

## Create a team site or communication site
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

> [!NOTE]
> If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.

2. Select **Create**.

    ![The Create button on the Active sites page.](media/create-site-button.png)

    > [!TIP]
    > If you go to **Resources** > **Sites** in the Microsoft 365 admin center and select **Add a site**, it opens <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a> in a new tab, and opens the Create a site panel.  

3. Select **Team site** (to create a Microsoft 365 group-connected team site), **Communication site**, or **Browse more sites**.

    ![The Create a site panel.](media/new-site-creation-admin.png)

4. Browse and select a template. Select **Use template**. 

1. Follow the steps to specify a site name, owner, language, and other settings. When you're done, select **Create site**.
 
    > [!NOTE]
    > If you enter a site name and another site already exists at the default address for that name, the site address will automatically be changed to an available address. For example, if you enter "Marketing" as the site name, and you already have a site at /sites/marketing, you will receive a warning ***This site address is available with modification*** and will be offered a new URL automatically at /sites/marketing2. If you want to re-use the URL "marketing" for the new site, you need to [permanently delete the existing site](delete-site-collection.md#permanently-delete-a-site) or [delete the redirect at that address](manage-site-redirects.md).   
 
## Create a classic site
<a name="__toc323551189_1"> </a>

We recommend using the new site templates for all your new sites. However, if you need to create a site that uses a classic template, you can do so using the following steps:  
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and select **Create**.
    
    ![The Create button on the Active sites page.](media/create-site-button.png)
  
2. At the bottom of the panel, select **Brose more sites**.

    ![Image of the site creation panel with admin controls highlighted.](media/new-site-admin-bottom.png)

3. Under **Choose a template**, select **More templates**. 

    
    ![More templates in the Choose a template list.](media/create-site-classic-template.png)

    - In the **Title** box, enter a name for the site. 
    
    - In the **Web Site Address** drop-down lists, select a domain name and a URL path—either **/sites/** or **/teams/—and then type a URL name for the site. 
    
    - In the **Template Selection** section, in the **Select a language** drop-down list, select a language for the site. You can enable the SharePoint multiple language interface on your sites, but the primary language for the site will remain the one you select here. 
    
      > [!NOTE]
      > It's important to select the appropriate language for the site, because once it's set, it cannot be changed. After creating a site, verify the locale and regional settings are accurate. (For example, a site created for Chinese will have its locale set to China.) 
  
    - In the **Template Selection** section, under **Select a template**, select the template that most closely describes the purpose of your site. 
    
      > [!TIP]
      > For more information about the classic templates, see [Using templates to create different kinds of SharePoint sites](https://support.office.com/article/449eccec-ff99-4cf3-b62e-dcfee37e8da4). 
  
    - In the **Time Zone** box, select the time zone that's appropriate for the location of the site. 
      
    - In the **Administrator** box, enter the user name of the person you want to be the site administrator. You can also use the **Check Names** or **Browse** button to find a user to make site administrator. 
      
    - In the **Storage Quota** box, enter the number of megabytes (MB) you want to allocate to this site. Do not exceed the available amount that is displayed next to the box. 
      
    - In the **Server Resource Quota** box, accept the resource quota default. This setting no longer affects the resource amounts available for the site. 
    
4. Select **OK**.
   

