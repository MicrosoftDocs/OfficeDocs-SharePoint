---
title: "Crawl log permissions"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: b3a165dc-d2ad-42d3-8a41-d3fb64d0ad86
description: "You can grant users or groups read access to crawl log information for the tenant. A typical use case is in eDiscovery, where users may need to check whether crawled content was in fact added to the search index."
---

# Crawl log permissions

As a global or SharePoint admin in Microsoft 365, you can grant users read access to crawl log information for the tenant. The crawl log tracks information about the status of crawled content. 
  
A typical use case is in eDiscovery, where you can grant a security group permission to view the crawl log information for the tenant. The users in the security group can view the crawl log data via the eDiscovery portal to check whether crawled content was successfully added to the search index, or whether indexing failed because of an error.
  
## Grant users permission to view the crawl log information
<a name="__top"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Microsoft 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Microsoft 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.
    
3. On the search administration page, select **Crawl Log Permissions**.
    
4. In the **Crawl Log Permissions** box, enter names or email addresses. The names of valid users or user groups appear in the list as you enter letters in the box. 
    
5. Select **OK**.
