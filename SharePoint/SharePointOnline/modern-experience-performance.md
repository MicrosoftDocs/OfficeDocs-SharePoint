---
title: "Performance in the modern SharePoint experience"
ms.author: kvice
author: kelleyvice-msft
manager: laurawi
ms.date: 3/13/2019
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
+ Use of content delivery networks (CDNs)

More powerful computers and modern advancements in network architectures and web browsers have made it possible to improve the overall SharePoint user experience by shifting much of the data caching and processing from the server to the client machine. In this article, you will learn about how the SharePoint modern experience leverages client-side processing and CDNs to improve performance.

## Client-side processing and data requests

In the classic SharePoint and SharePoint Online architecture, the SharePoint server farm executes data requests and other processing operations, returning results and rendered pages to the client. This model was intended to reduce the load on the the client machine and browser, and also to reduce network traffic between the client and server farm, factors which were critical performance bottlenecks in legacy environments.

The SharePoint modern experience is designed to take advantage of high-bandwidth low-latency networks, the computing power of user computers, and modern web browser capabilities to allow the client computer to directly perform certain data requests and processor-intensive operations such as page rendering.

The SharePoint modern experience client-side processing model can provide dramatic improvement in perceived end user latency over the classic SharePoint architecture. Keep in mind that there may be a significant increase in client-to-server network traffic and a greater dependency on the client-side execution environment as compared to the classic SharePoint architecture. As with any change to your network architecture, you should conduct a limited pilot to identify and resolve potential bottlenecks before rolling the SharePoint modern experience into your production environment.

## Content Delivery Networks (CDNs)

A Content Delivery Network, or CDN, is a worldwide network of servers that host certain files on servers that are physically closer to client computers, which can make downloads of these files faster. Office 365 tenants are configured out-of-the-box to use [public CDNs](https://docs.microsoft.com/en-us/Office365/Enterprise/content-delivery-networks) to access icons, scripts, and other generic content.

You can also choose to opt in to the Microsoft-hosted [Office 365 CDN](https://docs.microsoft.com/en-us/Office365/Enterprise/use-office-365-cdn-with-spo) to access common SharePoint libraries (such as JavaScript and CSS files) and SharePoint content (such as video files for Office 365 Video) from the fastest possible location relative to the client machine.

SharePoint Online latency is affected in part by the physical distance between your users and the location of the SharePoint Online tenant. This consideration is particularly important for organizations that have a global presence where a site may be hosted on one continent while users on the other side of the world are accessing its content. CDNs help mitigate this situation by automatically identifying frequently requested web assets and hosting copies in locations closer to the end users.

# Related topics

[Performance guidance for SharePoint Online portals](https://docs.microsoft.com/en-us/sharepoint/dev/solution-guidance/portal-performance)

[Tune SharePoint Online performance](https://docs.microsoft.com/en-us/office365/enterprise/tune-sharepoint-online-performance)

[Content Delivery Networks](https://docs.microsoft.com/en-us/Office365/Enterprise/content-delivery-networks)

[Use the Office 365 content delivery network with SharePoint Online](https://docs.microsoft.com/en-us/Office365/Enterprise/use-office-365-cdn-with-spo)

[Using content delivery networks with SharePoint Online](https://docs.microsoft.com/en-us/office365/enterprise/using-content-delivery-networks-with-sharepoint-online)

[General availability of Office 365 CDN](https://developer.microsoft.com/en-us/office/blogs/general-availability-of-office-365-cdn/)