---
title: "Portal launch landing page"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 09/30/2019
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: M365-collaboration
description: "Portal launch landing page"
---

# Creating a healthy SharePoint portal 

A portal is a SharePoint site where your default landing page(s) for your company is created. In large organizations there could be several of these. If you expect more than 20% of your users to access the page, you should consider that a portal page.
 
## Guidance 
This set of guidance will walk you through best practices and recommendations before you launch your portal and how to keep your portal healthy.
  
||**What to do**|**Follow this**|
|:-----|:-----|:-----|
|![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/deploy-blue-32.png "Staged rollout")|Plan the rollout of your portal|Launch in waves|
|![Alt image text](https://docs.microsoft.com/en-us/office/media/icons/PNGs/document-3-blue-32.png "Look and feel")|Portal design guidance|Review the guidance while designing your sites|</br>
|![Alt image text](https://docs.microsoft.com/en-us/office/media/icons/PNGs/task-checklist-planning-blue-32.png "Optimize your Performance")|Optimize your Performance|Follow the guidance below and run the Page Diagnostics for SharePoint tool|</br>
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/globe-hyperlink-blue-32.png "CDN") Use Content Delivery Networks (CDN) for better performance|Implement Public and Private CDN|
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/graph-4-blue-32.png "Batch REST calls") Batch calls to SharePoint when using the REST API|Combine operations into fewer requests|
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/graph-4-blue-32.png "Cache 3rd party web parts") Cache 3rd party web parts|Cache repetitive calls for 15 mins|
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/analytics-usage-report-blue-32.png "Slow web parts") Improve performance for slow web parts||
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/bandwidth-blue-32.png "Page weight") Review page weight||
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/task-list-planning-blue-32.png "Calls on a page") Limit the number of requests to a page|Limit the number of web parts and calls into SharePoint|
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/picture-photo-blue-32.png "Optimize images") Optimize your images|Follow basic image optimization for the web|
||![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/files-blue-32.png "iFrames") Limit and use Iframes carefully|Don't use more than 2 Iframes on a page|
|![Alt image text](https://docs.microsoft.com/en-us/Office/media/icons/PNGs/toolbox-32.png "Modern diagnostics tool")| Run the Page Diagnostics for SharePoint tool|Validate your pages and follow the guidance|
|![Alt image text](https://docs.microsoft.com/en-us/office/media/icons/PNGs/task-checklist-planning-blue-32.png "Limitations")|Limitations||</br>
