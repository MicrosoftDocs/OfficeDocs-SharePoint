---
ms.date: 04/23/2024
title: Manage site storage limits in SharePoint in Microsoft 365
ms.reviewer: trgreen
ms.author: ruihu
author: maggierui
manager: jtremper
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
ms.assetid: 77389c2c-8e7e-4b16-ab97-1c7103784b08
description: "In this article, you'll learn how to use the SharePoint admin center to manage the storage limits for sites in your organization."
---

# Manage site storage limits in SharePoint in Microsoft 365

The amount of SharePoint space your organization has is based on your number of licenses (see [SharePoint Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)). If you're a Global Administrator in Microsoft 365, you can [Add storage space for your subscription](/office365/admin/subscriptions-and-billing/add-storage-space) if you run out.

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
  
## View the total and available storage space for your organization

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

2. In the upper right of the page, see the amount of storage available and the total storage for your subscription. (If your organization has configured Multi-Geo in Microsoft 365, you can point to the bar to see the amount of storage used in the current geo location and all other geo locations.) 

    ![Storage bar on the Active sites page](media/active-sites-storage-bar.png)

    > [!NOTE]
    > Storage usage doesn't include changes made within the last 24-48 hours.

## Set automatic or manual site storage limits
<a name="__toc365547981"> </a>

By default, your SharePoint storage is available in a central pool from which all sites can draw. You, as a Global Administrator or SharePoint Administrator, don't need to divvy up storage space or reallocate space based on usage. That's all handled automatically: sites use what they need when they need it. If you previously set storage limits manually and switch to using pooled storage, SharePoint resets all the limits to 25 TB (25600 GB). (Note that the total storage for your organization might be less than 25 TB.)  

If you prefer to fine-tune the storage space allocated to each site, you can set your storage management option to "manual" and specify individual site storage limits. 

> [!NOTE]
> Some functionality is introduced gradually to organizations that have opted in to the [Targeted release option in Microsoft 365](/office365/admin/manage/release-options-in-office-365). This means that you might not yet see some features described in this article, or they might look different.

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

2. Select **Site storage limits**.

    ![Managing site storage limits](media/site-storage-limits.png)
     
3. Select **Automatic** or **Manual**, and then select **Save**.
    
## Manage individual site storage limits
<a name="__toc365547981"> </a>

Follow these steps to specify individual site storage limits *when your storage management option is set to "manual."* We recommend that you also set an email alert so that you and other site admins can be notified when sites are nearing the storage limit. To learn how to set the default storage limit for new sites, see [Manage site creation](manage-site-creation.md). 
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

2. In the left column, select the site, or for a channel site, select the link in the **Channel sites** column.

3. On the **General** tab, under **Storage limit**, select **Edit** to open the edit storage limit panel.

    ![Changing the storage limit for a site](media/site-storage-limit.png)
    
4. Enter the maximum storage in GB for the site. 

    > [!NOTE]
    > The max value you can enter is 25600 GB, although this may be more space than your organization has. To learn how your total storage is calculated, see [SharePoint Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).
    
5. Make sure **Notifications** is turned on to send an email to site admins when the site approaches the storage limit. Then, enter a value as a percent for how full you want the storage to be when the email is sent. 
 
6. Select **Save**.

If a site runs out of storage, site admins can request more by following these steps:

1. Go to the Site Settings page.

1. Under **Site Collection Administration**, select **Storage Metrics**.

> [!NOTE]
> Depending on your site, you may need to do the following to see the **Site Collection Administration** section:
> On the upper right corner of your site, select **Settings** and then select **Site Settings**. If you don't see **Site settings**, select **Site information** and then select **View all site settings**.

3. Select **Request more quota** in the upper right.

This sends a storage request email to the Global Administrators in the organization.
