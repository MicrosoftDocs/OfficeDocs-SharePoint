---
title: "Manage authoritative pages"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 6/29/2018
ms.audience: End User
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

As a SharePoint Online administrator, you can influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages. Authoritative pages link to the most relevant information. A typical example of an authoritative page could be the home page of your company portal.
  
If you have specific knowledge of an area, you can influence the relative importance of pages by adding more levels of authoritative pages (second-level and third-level). 
  
In the same way, you can also add non-authoritative pages. A typical example of a non-authoritative page could be the URL of a site that contains outdated information.
  
## Specify authoritative or non-authoritative pages
<a name="__top"> </a>

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Choose **search**. 
    
5. On the search administration page, choose **Manage Authoritative Pages**.
    
6. In the **Authoritative Web Pages** section, in the **Most authoritative pages** box, type the URLs of pages that are the most important. Separate the URLs with returns so that there is one URL per line. 
    
7. In the **Second-level authoritative pages** box, type the URLs of any pages that should be seen as second-level. 
    
8. In the **Third-level authoritative pages** box, type the URLs of any pages that should be seen as third-level. 
    
9. In the **Non-authoritative Sites** section, in the **Sites to demote** box, type the URLs of any sites that you want to be ranked lower than all of the other sites. Type one URL per line. 
  
    > [!TIP]
    >  All URLs whose prefix matches the prefix of a URL in the **Sites to demote** box are demoted. Example: Entering http://archive/ demotes the rank of all URLs that begin with http://archive/. 
  
10. Click **OK**.
    
## How results are ranked
<a name="__top"> </a>

Search uses the list of authoritative pages to calculate the ranking of results. Static rank determines the relative importance of a page. Static rank is calculated as the smallest number of clicks that it would take a user to navigate from an authoritative page to a document. The closer a document is to the most authoritative page, the higher the static rank of the page is.
  

