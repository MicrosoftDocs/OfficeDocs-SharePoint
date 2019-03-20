---
title: "Performance in the modern SharePoint experience"
ms.author: kvice
author: kelleyvice-msft
manager: laurawi
ms.date: 3/19/2019
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
search.appverid: MET150
description: "Learn about performance improvements in the SharePoint modern experience."
---

# Performance in the modern SharePoint experience

The modern experience in SharePoint is designed to be compelling, flexible and – importantly - more performant. Both SharePoint performance as a whole and the performance of individual SharePoint components such as search, lists and document libraries are affected by many factors, all of which contribute to the decisive performance metric: perceived end user latency, or the speed with which pages are rendered in the client browser. The SharePoint modern experience incorporates key performance improvements that help to minimize latency and improve SharePoint page responsiveness:

+ Client-side processing and data requests
+ Office 365 Content Delivery Network (CDN)

More powerful computers and modern advancements in network architectures and web browsers have made it possible to improve the overall SharePoint user experience by shifting much of the data caching and processing from the server to the client machine. In this article, you will learn about how the SharePoint modern experience leverages client-side processing and the Office 365 CDN to improve performance.

## Client-side processing and data requests

In the classic SharePoint and SharePoint Online architecture, the SharePoint server farm executes data requests and other processing operations, returning results and rendered pages to the client. This model was intended to reduce the load on the the client machine and browser, and also to reduce network traffic between the client and server farm, factors which were critical performance bottlenecks in legacy environments.

The SharePoint modern experience is designed to take advantage of the computing power of user computers and modern web browser capabilities to allow the client computer to directly perform certain data requests and processor-intensive operations such as page rendering.

The SharePoint modern experience client-side processing model can provide dramatic improvement in perceived end user latency over the classic SharePoint architecture. Keep in mind that there may be a greater dependency on the client-side execution environment as compared to the classic SharePoint architecture. As with any change to your network architecture, you should conduct a limited pilot to identify and resolve potential bottlenecks before rolling the SharePoint modern experience into your production environment.

## Office 365 Content Delivery Network (CDN)

SharePoint Online latency is affected in part by the physical distance between your users and the location of the SharePoint Online tenant. This consideration is particularly important for organizations that have a global presence where a site may be hosted on one continent while users on the other side of the world are accessing its content.

You can use the built-in Office 365 Content Delivery Network (CDN) to host static assets to provide better performance for your SharePoint Online pages. The Office 365 CDN improves performance by caching static assets closer to the browsers requesting them, which helps to speed up downloads and reduce latency. Also, the Office 365 CDN uses the [HTTP/2 protocol](https://en.wikipedia.org/wiki/HTTP/2) for improved compression and download speeds.

The Office 365 CDN is composed of multiple CDNs of two distinct classes of CDN: **public** and **private**. Both public and private CDNs allow you to host static assets in multiple locations, or _origins_, and serve them from global high-speed networks. The Office 365 CDN service is included as part of your SharePoint Online subscription.

The **Private CDN** within the Office 365 CDN provides fast, secure access to user content such as SharePoint Online document libraries, sites and media such as videos. Unlike public CDNs, access to content in the Office 365 CDN is secured by default so it can only be accessed by users with permissions to the original document library or storage location.

**Public CDNs** within the Office 365 CDN are hosted by 3rd-party CDN providers like Akamai and Verizon and Microsoft Azure. Content on a public CDN is accessible anonymously, and can be accessed by anyone who has URLs to hosted assets.

For information about how to use the Office 365 CDN, see [Use the Office 365 Content Delivery Network (CDN) with SharePoint Online](https://docs.microsoft.com/en-us/Office365/Enterprise/use-office-365-cdn-with-spo).

For more information about the Office 365 CDN, see [Office 365 CDN](https://docs.microsoft.com/en-us/Office365/Enterprise/content-delivery-networks).

# Related topics

[Performance guidance for SharePoint Online portals](https://docs.microsoft.com/en-us/sharepoint/dev/solution-guidance/portal-performance)

[Tune SharePoint Online performance](https://docs.microsoft.com/en-us/office365/enterprise/tune-sharepoint-online-performance)

[Content Delivery Networks](https://docs.microsoft.com/en-us/Office365/Enterprise/content-delivery-networks)