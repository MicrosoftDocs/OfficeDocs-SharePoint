---
title: "Add, edit, or delete a content source in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 7/14/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f687788b-f9b6-4a63-94d2-008939108c65
description: "Learn how to create a content source to specify what type of content to crawl, schedules for crawling, start addresses, and crawl priority."
---

# Add, edit, or delete a content source in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
A content source is a set of options that you use to specify what, when, and how to crawl. 
  
When a Search service application is created, a content source named "Local SharePoint sites" is automatically created and configured for crawling all SharePoint Server sites in the local server farm. You can create additional content sources to specify other content to crawl and how the system should crawl that content. After you create a content source, you can edit or delete it at any time. 
  
> [!CAUTION]
> Changing a content source requires a full crawl for that content source. 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, see the following article for information about prerequisites regarding the creation of content sources: 
  
- [Create a Search service application](create-and-configure-a-search-service-application.md)

    
## Create, edit, or delete a content source

<a name="proc1"> </a>

 **To get to the Manage Content Sources page**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application. 
    
2. On SharePoint Server Central Administration home page, navigate to **Application Management > Manage service applications > Search service application**.
      
3. On the **Search Administration** page, under **Crawling**, select **Content Sources**.
    

<a name="proc2"> </a>

 **To create a content source**
  
1. On the **Manage Content Sources** page, select **New Content Source**.
    
2. On the **Add Content Source** page, under **Name**, type a name for the new content source in the **Name** box.. 
    
3. Under **Content Source Type**, select the type of content that you want to crawl. 
    
4. Under **Start Addresses**, type the URLs from which the crawler should begin crawling in the **Type start addresses below (one per line)** box.
    
5. Under **Crawl Settings**, select the crawling behavior that you want.
    
6. Under **Crawl Schedules**, to specify a schedule for full crawls, select a defined schedule from the **Full Crawl** list. A full crawl involves crawling all content that is specified by the content source, regardless of whether the content has changed. To define a full crawl schedule, select **Create schedule**.
    
7. To specify a schedule for incremental crawls, select a defined schedule from the **Incremental Crawl** list. An incremental crawl involves crawling content that is specified by the content source that has changed since the last crawl. To define a schedule, select **Create schedule**. You can change a defined schedule by selecting **Edit schedule**.
    
   > [!NOTE]
   > For a content source that is of type SharePoint Server sites, you can enable continuous crawls. For more information, see [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md). 
  
8. To set the priority of this content source, under **Content Source Priority**, select **Normal** or **High** from the **Priority** list. 
    
9. Select **OK**. 
    

<a name="proc3"> </a>

 **To edit a content source**
  
1. You can edit a content source to change the schedule on which the content is crawled, the crawl start addresses, the content source priority, or the name of the crawl. Crawl settings and content source type cannot be changed when you edit a content source.
    
2. On the **Manage Content Sources** page, in the list of content sources, point to the name of the content source that you want to edit, click the arrow that appears, and then select **Edit**. 
    
3. After you make the changes that you want, select **OK**.

<a name="proc4"> </a>

 **To delete a content source**
  
1. On the **Manage Content Sources** page, in the list of content sources, point to the name of the content source that you want to delete, click the arrow that appears, and then select **Delete**.
    
2. Select **OK** to confirm that you want to delete this content source. 
    
Starting with the SharePoint Server Subscription Edition Version 23H2 feature update, you have the ability to configure the HTTP protocol version that applications would use to search your content sources.

> [!NOTE]
> By default, the search service application search crawler uses the HTTP 1.1 protocol version. The search crawler will use the HTTP 1.0 protocol version when configured so.

You can configure an HTTP protocol version to be applicable to specific content sources. These HTTP protocol versions can be configured only by using the following cmdlets:

- New-SPEnterpriseSearchCrawlContentSource
- Set-SPEnterpriseSearchCrawlContentSource

When you use these PowerSell cmdlets, you must also specify the `HttpProtocol` parameter which has the following options that a user can leverage:

- **Default**: This option refers to the system default one, currently HTTP 1.1.
- **Http_1_0**: This option refers to the HTTP 1.0 protocol.
- **Http_1_1**: This option refers to the HTTP 1.1 protocol.
