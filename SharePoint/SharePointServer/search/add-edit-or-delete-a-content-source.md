---
title: "Add, edit, or delete a content source in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f687788b-f9b6-4a63-94d2-008939108c65
description: "Learn how to create a content source to specify what type of content to crawl, schedules for crawling, start addresses, and crawl priority."
---

# Add, edit, or delete a content source in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A content source is a set of options that you use to specify what, when, and how to crawl. 
  
When a Search service application is created, a content source named "Local SharePoint sites" is automatically created and configured for crawling all SharePoint Server sites in the local server farm. You can create additional content sources to specify other content to crawl and how the system should crawl that content. After you create a content source, you can edit or delete it at any time. 
  
> [!CAUTION]
> Changing a content source requires a full crawl for that content source. 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites: 
  
- Create a Search service application
    
## Create, edit, or delete a content source
<a name="proc1"> </a>

 **To get to the Manage Content Sources page**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application. 
    
2. On the home page of the SharePoint Server Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application.
    
4. On the Search Administration Page, in the **Crawling** section, click **Content Sources**.
    
## 
<a name="proc2"> </a>

 **To create a content source**
  
1. On the Manage Content Sources page, click **New Content Source**.
    
2. On the Add Content Source page, in the **Name** section, in the **Name** box, type a name for the new content source. 
    
3. In the **Content Source Type** section, select the type of content that you want to crawl. 
    
4. In the **Start Addresses** section, in the **Type start addresses below (one per line)** box, type the URLs from which the crawler should begin crawling. 
    
5. In the **Crawl Settings** section, select the crawling behavior that you want. 
    
6. In the **Crawl Schedules** section, to specify a schedule for full crawls, select a defined schedule from the **Full Crawl** list. A full crawl crawls all content that is specified by the content source, regardless of whether the content has changed. To define a full crawl schedule, click **Create schedule**.
    
7. To specify a schedule for incremental crawls, select a defined schedule from the **Incremental Crawl** list. An incremental crawl crawls content that is specified by the content source that has changed since the last crawl. To define a schedule, click **Create schedule**. You can change a defined schedule by clicking **Edit schedule**.
    
    > [!NOTE]
    > For a content source that is of type SharePoint Server sites, you can enable continuous crawls. For more information, see [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md). 
  
8. To set the priority of this content source, in the **Content Source Priority** section, on the **Priority** list, select **Normal** or **High**. 
    
9. Click **OK**. 
    
## 
<a name="proc3"> </a>

 **To edit a content source**
  
1. You can edit a content source to change the schedule on which the content is crawled, the crawl start addresses, the content source priority, or the name of the crawl. Crawl settings and content source type cannot be changed when you edit a content source.
    
2. On the Manage Content Sources page, in the list of content sources, point to the name of the content source that you want to edit, click the arrow that appears, and then click **Edit**. 
    
3. After you make the changes that you want, click **OK**.
    
## 
<a name="proc4"> </a>

 **To delete a content source**
  
1. On the Manage Content Sources page, in the list of content sources, point to the name of the content source that you want to delete, click the arrow that appears, and then click **Delete**.
    
2. Click **OK** to confirm that you want to delete this content source. 
    

