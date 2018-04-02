---
title: "Restore a deleted site collection"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 1/31/2018
ms.audience: Admin
ms.topic: article
ms.service: o365-administration
localization_priority: Normal
ms.assetid: 91c18651-c017-47d1-9c27-3a22f325d6f1
description: "Learn how to get back a deleted site collection in SharePoint Online for Enterprises."
---

# Restore a deleted site collection

 *Last updated: January 2018* 
  
When a global or SharePoint admin in Office 365 deletes a site collection, it's placed in the site collection Recycle Bin, where it's kept for 93 days before it's permanently deleted. This article describes how global admins and SharePoint admins can restore deleted site collections. For info about restoring other items from the site collection Recycle Bin, see [Restore deleted items from the site collection recycle bin ](https://support.office.com/article/5fa924ee-16d7-487b-9a0a-021b9062d14b).
  
If you're an admin for SharePoint Server, learn how to [Restore deleted site collections using Microsoft Powershell](https://go.microsoft.com/fwlink/?linkid=866959).
  
## Overview
<a name="__toc315681381"> </a>

In the site collection Recycle Bin, you can view deleted site collections and see how many days are left before each site collection is permanently deleted.
  
> [!NOTE]
> When sites and items within them are deleted, they're sent to the site Recycle Bin (sometimes called the "first-stage recycle bin") and are only moved to the site collection Recycle Bin (or "second-stage recycle bin") if they're deleted from site recycle bin. When you delete a site collection, it's sent directly to the site collection Recycle Bin. For info about restoring items from the site Recycle Bin, see [Restore items in the Recycle Bin of a SharePoint site](https://support.office.com/article/6df466b6-55f2-4898-8d6e-c0dff851a0be). 
  
Deleted site collections are automatically emptied from the site collection Recycle Bin after 93 days. You can restore a deleted site collection before this time if you haven't exceeded your SharePoint Online storage or usage quota.
  
To create a new site collection that uses the same URL as a site collection that's in the site collection Recycle Bin, you must permanently delete the site collection in the site collection Recycle Bin first.
  
## Restore a deleted site collection
<a name="__toc315681383"> </a>

1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. On the ribbon, click **Recycle Bin**.
    
5. In the Recycle Bin, select the check box next to the site collection that you want to restore.
    
6. On the ribbon, click **Restore Deleted Items**.
    

