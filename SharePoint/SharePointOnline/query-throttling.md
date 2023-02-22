---
ms.date: 07/11/2018
title: "Manage query client types"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.custom: admindeeplinkSPO
ms.localizationpriority: medium
search.appverid:
- SPS150
- SPO160
- MET150
ms.assetid: 0d335bc4-e7a0-46bc-ba40-da34e414174f
description: "Learn how query client types decide in which order queries are performed."
---

# Manage query client types

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../SharePointServer/includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

Learn how query client types decide in which order queries are performed. 
  
A query client type is how a client performing a query tells the system what type of client it is. For example, a client might tell us it is UI, or an automated query. Query throttling monitors the use of resources and protects the search system. Administrators can use client-type information for throttling, to make sure lower-priority clients like automated queries don't squeeze out higher-priority clients like UI. Query client types are also used for things like logging, reports, and determining relevance.
  
The client sets the client type as a label in the query. The administrator configures the valid client types (though some are default and mandatory), and the client chooses one for each query. 
  
> [!NOTE]
>  You can't turn query throttling on or off. 
  
## Add a query client type
<a name="__top"> </a>

> [!NOTE]
> You can change the name of a client type that has been created for your tenant only. 
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
    
3. On the search administration page, select **Manage Query Client Types**.
    
4. To add a client type, select **New Client Type**.
    
5. On the **Edit a client type** page, in the **Query Client Type** field, for the client type, enter a name. 
    
6. From the **Throttling Tier** list, select either **Top**, **Middle**, or **Bottom**. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
7. Select **OK**.
    
## Prioritize a client query type
<a name="__top"> </a>

You can use throttling tiers to prioritize query processing. When the resource limit is reached, query throttling kicks in, and the search system processes queries, starting from the top tier, right through to the bottom tier.
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
    
3. On the search administration page, select **Manage Query Client Types**.
    
4. Go to the **Client Type** section, and select the **System Type** that you want to change. 
    
5. From the **Throttling Tier** list, select either **Top**, **Middle**, or **Bottom**. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
6. Select **OK**.

