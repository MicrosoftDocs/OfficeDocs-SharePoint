---
title: "Manage query client types"
ms.author: tlarsen
author: tlarsen
manager: arnek
ms.date: 5/16/2014
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
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

Note: You can change the name of a client type that has been created for your tenant only.
  
1. Sign in to the Office 365 Admin Center as a search administrator.
    
2. Choose **Admin** > **SharePoint**. You're now in the SharePoint admin center.
    
3. Choose **search**.
    
4. On the search administration page, choose **Manage Query Client Types**.
    
5. To add a client type, click **New Client Type**.
    
6. On the Edit a client type page, in the **Query Client Type** field, enter a name for the client type. 
    
7. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
> [!NOTE]
>  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
1. Click **OK**.
    
[Learn how query client types decide in which order queries are performed. A query client type is how a client performing a query tells the system what type of client it is. For example, a client might tell us it is UI, or an automated query. Query throttling monitors the use of resources and protects the search system. Administrators can use client-type information for throttling, to make sure lower-priority clients like automated queries don't squeeze out higher-priority clients like UI. Query client types are also used for things like logging, reports, and determining relevance.The client sets the client type as a label in the query. The administrator configures the valid client types (though some are default and mandatory), and the client chooses one for each query. You can't turn query throttling on or off.](query-throttling.md#__top)
  
## Prioritize a client query type
<a name="__top"> </a>

You can use throttling tiers to prioritize query processing. When the resource limit is reached, query throttling kicks in, and the search system processes queries, starting from the top tier, right through to the bottom tier.
  
1. Sign in to the Office 365 Admin Center as a search administrator.
    
2. Choose **Admin** > **SharePoint**. You're now in the SharePoint admin center.
    
3. Choose **search**.
    
4. On the search administration page, choose **Manage Query Client Types**.
    
5. Go to the **Client Type** section, and click the **System Type** that you want to change. 
    
6. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
> [!NOTE]
>  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
1. Click **OK**.
    
[Learn how query client types decide in which order queries are performed. A query client type is how a client performing a query tells the system what type of client it is. For example, a client might tell us it is UI, or an automated query. Query throttling monitors the use of resources and protects the search system. Administrators can use client-type information for throttling, to make sure lower-priority clients like automated queries don't squeeze out higher-priority clients like UI. Query client types are also used for things like logging, reports, and determining relevance.The client sets the client type as a label in the query. The administrator configures the valid client types (though some are default and mandatory), and the client chooses one for each query. You can't turn query throttling on or off.](query-throttling.md#__top)
  

