---
title: "SharePoint Modern Experience Performance Improvements"
ms.author: kvice
author: kelleyvice-msft
manager: laurawi
ms.date: 1/9/2019
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
search.appverid: MET150
description: "Learn about performance improvements in the SharePoint modern experience."
---

# SharePoint performance

The performance of individual SharePoint components such as search, lists and document libraries are affected by many factors, and all of these may contribute to the ultimate performance metric: the responsiveness of the user interface. The SharePoint modern experience incorporates several features that help to minimize latency and speed up the response of the user interface.

Modern network architectures and browsers have made it possible for data caching and processing to take place on the client rather than the server, which has the following net benefits:

+ Minimize latency in data requests
+ Reduce server load

## Client-side caching

The traditional SharePoint architecture provides server-side disk-based caches that help improve the speed at which web pages load in the browser: the BLOB cache, the page output cache, the object cache, and the anonymous search results cache. Caching helps to reduce the amount of time it takes for requests to render in the user interface.

The SharePoint modern experience is designed to minimize the time required to render cached content by allowing blobs and other objects to be cached locally on the user machine, minimizing latency and reducing network traffic between the client and the SharePoint front-end servers.

## Client-side processing and data requests

The traditional SharePoint architecture is based on the server-side processing model, in which the SharePoint server farm executes data requests, calculations and lookups and returns results and rendered pages to the client. In this model, the client machine 

# Related topics

[Performance guidance for SharePoint Online portals](https://docs.microsoft.com/en-us/sharepoint/dev/solution-guidance/portal-performance)
[Tune SharePoint Online performance](https://docs.microsoft.com/en-us/office365/enterprise/tune-sharepoint-online-performance)