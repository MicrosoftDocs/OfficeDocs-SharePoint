---
title: "Manage authoritative pages"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: End User
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 68429de6-7c7b-455c-a90a-2afaa3444647
description: "You can influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages."
---

# Manage authoritative pages

As a global or SharePoint admin in Office 365, you can influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages. Authoritative pages link to the most relevant information. A typical example of an authoritative page could be the home page of your company portal.
  
If you have specific knowledge of an area, you can influence the relative importance of pages by adding more levels of authoritative pages (second-level and third-level). 
  
In the same way, you can also add non-authoritative pages. A typical example of a non-authoritative page could be the URL of a site that contains outdated information.

    > [!NOTE]
    > Authorative pages and sites does not impact ranking in Microsoft Search and will only work in classic search and web parts using the default ranking model.
  
## Specify authoritative or non-authoritative pages
<a name="__top"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  

2. In the left pane of the admin center, under **Admin centers**, select **SharePoint** to open the SharePoint admin center. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

3. Under **Search**, select **Open**.

4. On the search administration page, choose **Manage Authoritative Pages**.
    
5. In the **Authoritative Web Pages** section, in the **Most authoritative pages** box, type the URLs of pages that are the most important. Separate the URLs with returns so that there is one URL per line. 
    
6. In the **Second-level authoritative pages** box, type the URLs of any pages that should be seen as second-level. 
    
7. In the **Third-level authoritative pages** box, type the URLs of any pages that should be seen as third-level. 
    
8. In the **Non-authoritative Sites** section, in the **Sites to demote** box, type the URLs of any sites that you want to be ranked lower than all of the other sites. Type one URL per line. 
  
    > [!TIP]
    >  All URLs whose prefix matches the prefix of a URL in the **Sites to demote** box are demoted. Example: Entering http://archive/ demotes the rank of all URLs that begin with http://archive/. 
  
9. Select **OK**.
    
## How results are ranked
<a name="__top"> </a>

Search uses the list of authoritative pages to calculate the ranking of results. Static rank determines the relative importance of a page. Static rank is calculated as the smallest number of clicks that it would take a user to navigate from an authoritative page to a document. The closer a document is to the most authoritative page, the higher the static rank of the page is.
  

