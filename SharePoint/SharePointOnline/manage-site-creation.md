---
title: "Manage site creation in SharePoint"
ms.reviewer: metorres
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- m365initiative-spsitemanagement
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: e72844a3-0171-47c9-befb-e98b23e2dcf9
description: "In this article, you'll learn how to allow or prevent users from creating their own sites in SharePoint."
---

# Manage site creation in SharePoint

As a global or SharePoint admin in Microsoft 365, you can let your users create and administer their own SharePoint sites, determine what kind of sites they can create, and specify the location of the sites. By default, users can create communication sites and [Microsoft 365 group-connected team sites](https://support.office.com/article/b565caa1-5c40-40ef-9915-60fdb2d97fa2).
  
>[!NOTE]
>Disabling site creation for users does not remove their ability to create Microsoft 365 groups or resources, such as Microsoft Teams, which rely on a group. When a Microsoft 365 group is created, a SharePoint site is also created. To restrict creation of Microsoft 365 groups and the resources that rely on groups see [Manage who can create Microsoft 365 Groups](/office365/admin/create-groups/manage-creation-of-groups). 
  
## Manage site creation in the new SharePoint admin center

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   >[!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Settings page.
    
2. Select **Site creation**.

    ![Site creation settings in the new SharePoint admin center](media/site-creation.png)

3. If you want users to be able to create sites from these services, select **Let users create sites from the SharePoint start page and OneDrive**.

    > [!NOTE]
    > Even if you clear this check box, users may be able to create Microsoft 365 groups from other places in Microsoft 365. Each group always comes with a team site. [Learn how to manage who can create Microsoft 365 groups](/office365/admin/create-groups/manage-creation-of-groups)

4. Under /sites or /teams, select to create Microsoft 365 group-connected team sites, and then select the default time zone and storage limit for new sites.

5. Select **Save**.
 


## Manage detailed site and subsite creation settings in the classic SharePoint admin center

Admins in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> can choose to either enable or disable subsite creation across sites or enable for classic sites only. When disabling subsite creation, not only will the subsite option be hidden from the command bar including classic but also users will not be able to create new subsites directly through a URL or API.  

> [!NOTE]
> For info about classifying Microsoft 365 groups, see [Manage Microsoft 365 Groups with PowerShell](/office365/enterprise/manage-office-365-groups-with-powershell).


1.  In the left pane of the new SharePoint admin center, select <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings**</a>. At the bottom of the page, select **classic settings page**. 
    
2. Under **Site Creation**, select to show or hide the **Create site** command.

    ![Site creation settings in the classic SharePoint admin center](media/admin-site-creation.png)

   - If you choose **Disable subsite creation for all sites** it will also hide the subsite creation command (including classic) and disable users from being able to create new subsites through a URL or API. 
   - If you choose **Enable subsite creation for classic sites only** users will be able to create new subsites for classic sites. 
   - If you choose **Enable subsite creation for all sites** users will be able to create new subsites from any SharePoint site. 
 

3. Select **OK** when you are done.

> [!NOTE]
>  Creation of subsite on OneDrive is not supported, you will see an error “New subsites are not available in this site. Create a new site instead”.

> [!NOTE]
> Currently, the following site templates are considered "modern".
> 
> - GROUP#0
> - STS#3
> - SITEPAGEPUBLISHING#0
> - TEAMCHANNEL#0
> - TEAMCHANNEL#1


> [!TIP]
> Instead of using subsites, we recommend that you use hub sites. [SharePoint hub sites](https://support.microsoft.com/office/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f) allow you to group similar topics and content together using modern architecture design. Plan to [create hub sites.](create-hub-site.md) 
