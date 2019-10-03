---
title: "Crawl log permissions"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
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

As a global or SharePoint admin in Office 365, you can grant users read access to crawl log information for the tenant. The crawl log tracks information about the status of crawled content. 
  
A typical use case is in eDiscovery, where you can grant a security group permission to view the crawl log information for the tenant. The users in the security group can view the crawl log data via the eDiscovery portal to check whether crawled content was successfully added to the search index, or whether indexing failed because of an error.
  
## Grant users permission to view the crawl log information
<a name="__top"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
    
3. Choose **Classic features**. 
 
4. Under **Search**, select **Open**.
    
5. On the search administration page, choose **Crawl Log Permissions**.
    
6. In the **Crawl Log Permissions** box, enter names or email addresses. The names of valid users or user groups are shown in the list as you type letters in the box. 
    
7. Select **OK**.
    

