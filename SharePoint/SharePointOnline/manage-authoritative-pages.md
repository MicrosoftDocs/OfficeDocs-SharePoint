---
ms.date: 07/11/2018
title: "Manage authoritative pages"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
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
ms.assetid: 68429de6-7c7b-455c-a90a-2afaa3444647
description: "You can influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages."
---

# Manage authoritative pages

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../SharePointServer/includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

As a Global Administrator or SharePoint Administrator in Microsoft 365, you can influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages. Authoritative pages link to the most relevant information. A typical example of an authoritative page could be the home page of your company portal.

Authoritative pages only work for **classic** search and only for web parts that use the **default** ranking model.
  
If you have specific knowledge of an area, you can influence the relative importance of pages by adding more levels of authoritative pages (second-level and third-level). 
  
In the same way, you can also add non-authoritative pages. A typical example of a non-authoritative page could be the URL of a site that contains outdated information.

## Specify authoritative or non-authoritative pages
<a name="__top"> </a>

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

> [!NOTE]
> If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

2. Under **Search**, select **Open**.

3. On the search administration page, select **Manage Authoritative Pages**.
    
4. In the **Authoritative Web Pages** section, in the **Most authoritative pages** box, enter the URLs of pages that are the most important. Separate the URLs with returns so that there is one URL per line. 
    
5. In the **Second-level authoritative pages** box, enter the URLs of any pages that should be seen as second-level. 
    
6. In the **Third-level authoritative pages** box, enter the URLs of any pages that should be seen as third-level. 
    
7. In the **Non-authoritative Sites** section, in the **Sites to demote** box, enter the URLs of any sites that you want to be ranked lower than all of the other sites. Type one URL per line. 
  
    > [!TIP]
    >  All URLs whose prefix matches the prefix of a URL in the **Sites to demote** box are demoted. Example: Entering http://archive/ demotes the rank of all URLs that begin with http://archive/. 
  
8. Select **OK**.
    
## How results are ranked
<a name="__top"> </a>

Classic search uses the list of authoritative pages to calculate the ranking of results. Static rank determines the relative importance of a page. Static rank is calculated as the smallest number of clicks that it would take a user to navigate from an authoritative page to a document. The closer a document is to the most authoritative page, the higher the static rank of the page is.

