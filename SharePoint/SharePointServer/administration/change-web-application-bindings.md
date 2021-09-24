---
title: "Change web application bindings for SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Learn how to change a web application bindings for SharePoint Server."
---

# Change web application bindings for SharePoint Server Subscription Edition

This article provides detailed guidance for changing the IIS bindings of a web application.

## Editing a web appliction bindings for SharePoint Server Subscription Edition

To configure the existing zone attached with the web application and set the port, URL, SSL certificate host header, do the following:

![Select-edit](../SharePointServer/media/extend-exit.PNG)

![edit-web-application-part1](../SharePointServer/media/edit2.PNG)

![edit-web-application-part2](../SharePointServer/media/edit3.PNG)

## Extending a web appliction bindings for SharePoint Server Subscription Edition

You can extend a web application into a zone with a set of Internet Information Services (IIS) bindings and alternate access mapping URLs, or you might decide that you want to use a different URL to reach the web application.

> [!NOTE]
> If you want to add additional URLs and IIS bindings to a web application, you can do so by extending the web application into an unused zone. 

To extend a web application to existing or new zone with port, URL, SSL certificate and host header specified, do the following:

![Select-extend](../SharePointServer/media/extend-exit.PNG)

![extend-web-application-part1](../SharePointServer/media/extend2.PNG)

![extend-web-application-part2](../SharePointServer/media/extend3.PNG)

![extend-web-application-part3](../SharePointServer/media/extend4.PNG)
