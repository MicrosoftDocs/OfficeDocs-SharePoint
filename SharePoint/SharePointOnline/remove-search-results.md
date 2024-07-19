---
ms.date: 07/11/2018
title: "Remove search results"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: End User
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: b8177720-ff41-478e-bbe7-72183b97824f
description: "As a search administrator, you can temporarily remove items from the search results with immediate effect. These items can be documents, pages, or sites that you don't want users to see when they search."
---

# Remove search results

As a user who has [SharePoint administrator](/sharepoint/site-permissions#site-admins) or [above](/sharepoint/site-permissions) permissions in Microsoft 365, you can temporarily remove items from search results with immediate effect. The items that you can remove can be documents or pages that you don't want users to see. An example of this could be a Word document containing an invitation to an event that has been canceled, but the organizer has not removed the document from the site yet. Removing a result removes it from both classic and modern search results. 
  
> [!IMPORTANT]
>  This is only a quick fix! Unless you delete the items or change the permissions of items manually, they will show up again in your search results after the next crawl. 
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
   
3. On the **search administration** page, select **Remove Search Results**.
    
4. On the **Remove Search Results** page, in the **URLs to remove** box, enter the URLs that you want to remove from the search results, for example, https://contoso.sharepoint.com/sites/site1. URLs cannot contain a wildcard (\*) character. Enter one URL on each line. 
    
5. Select **Remove Now**. The URLs are immediately removed from your search results.

