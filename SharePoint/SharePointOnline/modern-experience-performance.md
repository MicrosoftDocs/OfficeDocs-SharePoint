---
title: "Performance in the modern SharePoint experience"
ms.reviewer: 
ms.author: kvice
author: kelleyvice-msft
manager: laurawi
ms.date: 3/19/2019
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
search.appverid: MET150
description: "Learn about performance improvements in the SharePoint modern experience."
---

# Performance in the modern SharePoint experience

The modern experience in SharePoint is designed to be compelling, flexible and – importantly - more performant. Both SharePoint performance as a whole and the performance of individual SharePoint components such as search, lists and document libraries are affected by many factors, all of which contribute to the decisive performance metric: perceived end user latency, or the speed with which pages are rendered in the client browser. The SharePoint modern experience incorporates key performance improvements that help to minimize latency and improve SharePoint page responsiveness:

+ Client-side processing and data requests
+ Microsoft 365 Content Delivery Network (CDN)

More powerful computers and modern advancements in network architectures and web browsers have made it possible to improve the overall SharePoint user experience by shifting much of the data caching and processing from the server to the client machine. In this article, you will learn about how the SharePoint modern experience leverages client-side processing and the Microsoft 365 CDN to improve performance.

## Client-side processing and data requests

In the classic SharePoint and SharePoint Online architecture, the SharePoint server farm executes data requests and other processing operations, returning results and rendered pages to the client. This model was intended to reduce the load on the client machine and browser, and also to reduce network traffic between the client and server farm, factors which were critical performance bottlenecks in legacy environments.

The SharePoint modern experience is designed to take advantage of the computing power of user computers and modern web browser capabilities to allow the client computer to directly perform certain data requests and processor-intensive operations such as page rendering.

The SharePoint modern experience client-side processing model can provide dramatic improvement in perceived end user latency over the classic SharePoint architecture. Keep in mind that there may be a greater dependency on the client-side execution environment as compared to the classic SharePoint architecture. As with any change to your network architecture, you should conduct a limited pilot to identify and resolve potential bottlenecks before rolling the SharePoint modern experience into your production environment.

## Microsoft 365 Content Delivery Network (CDN)

SharePoint Online latency is affected in part by the physical distance between your users and the location of your SharePoint Online environment (tenant). This consideration is particularly important for organizations that have a global presence where a site may be hosted on one continent while users on the other side of the world are accessing its content.

You can use the built-in Microsoft 365 Content Delivery Network (CDN) to host static assets to provide better performance for your SharePoint sites. The Microsoft 365 CDN improves performance by caching static assets closer to the browsers requesting them, which helps to speed up downloads and reduce latency. Also, the Microsoft 365 CDN uses the [HTTP/2 protocol](https://en.wikipedia.org/wiki/HTTP/2) for improved compression and download speeds.

The Microsoft 365 CDN is composed of multiple CDNs that allow you to host static assets in multiple locations, or _origins_, and serve them from global high-speed networks. Depending on the kind of content you want to host in the Microsoft 365 CDN, you can add **public** origins, **private** origins or both.

Content in **public** origins within the Microsoft 365 CDN is accessible anonymously, and can be accessed by anyone who has URLs to hosted assets. Because access to content in public origins is anonymous, you should only use them to cache non-sensitive generic content such as JavaScript files, scripts, icons and images. The Microsoft 365 CDN is used by default for downloading generic resource assets like the Microsoft 365 client applications from a public origin.

**Private** origins within the Microsoft 365 CDN provide private access to user content such as SharePoint Online document libraries, sites and media such as videos. Access to content in private origins is secured with dynamically generated tokens so it can only be accessed by users with permissions to the original document library or storage location. Private origins in the Microsoft 365 CDN can only be used for SharePoint Online content, and you can only access assets through redirection from your SharePoint Online environment.

The Microsoft 365 CDN service is included as part of your SharePoint Online subscription.

For info about how to use the Microsoft 365 CDN, see [Use the Microsoft 365 Content Delivery Network (CDN) with SharePoint Online](/Office365/Enterprise/use-office-365-cdn-with-spo).

For more info about the Microsoft 365 CDN, see [Microsoft 365 CDN](/Office365/Enterprise/content-delivery-networks).

## Related topics

[Performance guidance for SharePoint Online portals](/sharepoint/dev/solution-guidance/portal-performance)

[Tune SharePoint Online performance](/office365/enterprise/tune-sharepoint-online-performance)

[Content Delivery Networks](/Office365/Enterprise/content-delivery-networks)

[Use the Microsoft 365 Content Delivery Network (CDN) with SharePoint Online](/Office365/Enterprise/use-office-365-cdn-with-spo)
