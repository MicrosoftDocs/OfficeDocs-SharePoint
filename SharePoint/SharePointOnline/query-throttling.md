---
title: "Manage query client types"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 6/29/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPS150
- SPO160
- MET150
ms.assetid: 0d335bc4-e7a0-46bc-ba40-da34e414174f
description: "Learn how query client types decide in which order queries are performed."
---

# Manage query client types

Learn how query client types decide in which order queries are performed. 
  
A query client type is how a client performing a query tells the system what type of client it is. For example, a client might tell us it is UI, or an automated query. Query throttling monitors the use of resources and protects the search system. Administrators can use client-type information for throttling, to make sure lower-priority clients like automated queries don't squeeze out higher-priority clients like UI. Query client types are also used for things like logging, reports, and determining relevance.
  
The client sets the client type as a label in the query. The administrator configures the valid client types (though some are default and mandatory), and the client chooses one for each query. 
  
> [!NOTE]
>  You can't turn query throttling on or off. 
  
## Add a query client type
<a name="__top"> </a>

> [!NOTE]
> You can change the name of a client type that has been created for your tenant only. 
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Choose **search**.
    
5. On the search administration page, choose **Manage Query Client Types**.
    
6. To add a client type, click **New Client Type**.
    
7. On the Edit a client type page, in the **Query Client Type** field, enter a name for the client type. 
    
8. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
9. Click **OK**.
    
## Prioritize a client query type
<a name="__top"> </a>

You can use throttling tiers to prioritize query processing. When the resource limit is reached, query throttling kicks in, and the search system processes queries, starting from the top tier, right through to the bottom tier.
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Microsoft 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Choose **search**.
    
5. On the search administration page, choose **Manage Query Client Types**.
    
6. Go to the **Client Type** section, and click the **System Type** that you want to change. 
    
7. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
8. Click **OK**.
    

