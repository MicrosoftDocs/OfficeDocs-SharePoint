---
title: "Manage query client types"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
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
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
      
3. Select **Classic features**.
 
4. Under **Search**, select **Open**.
    
5. On the search administration page, choose **Manage Query Client Types**.
    
6. To add a client type, select **New Client Type**.
    
7. On the Edit a client type page, in the **Query Client Type** field, enter a name for the client type. 
    
8. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
9. Select **OK**.
    
## Prioritize a client query type
<a name="__top"> </a>

You can use throttling tiers to prioritize query processing. When the resource limit is reached, query throttling kicks in, and the search system processes queries, starting from the top tier, right through to the bottom tier.
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
      
3. Select **Classic features**.
 
4. Under **Search**, select **Open**.
    
5. On the search administration page, choose **Manage Query Client Types**.
    
6. Go to the **Client Type** section, and select the **System Type** that you want to change. 
    
7. Choose **Top**, **Middle** or **Bottom** from the **Throttling Tier** list. 
    
    > [!NOTE]
    >  Lower priority queries are throttled first. The search system processes queries from top tier to bottom tier. 
  
8. Select **OK**.
    

