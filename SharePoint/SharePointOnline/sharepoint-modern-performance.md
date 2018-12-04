---
title: "SharePoint Modern Performance"
ms.author: kvice
author: kelleyvice-msft
manager: laurawi
ms.date: 12/4/2018
ms.audience: ITPro
ms.topic: conceptual
ms.service: 
localization_priority: Normal
ms.collection:
ms.custom: 
search.appverid:
ms.assetid: 
description: "Summary: Explains how SharePoint Modern performance works."
---

This article applies to single sites that are meant to serve the majority of your portals, etc.
Modern is a client-side rendered technology as opposed to server side rendered. This allows us to use the computing power on the client. This allows us to run the .js on the client and speed up for geopolitical.
We can show updates to the pages you're updating in real time while you edit without having to commit them to the server.

This is ***for mobile***
Page chrome
Header
Nav menu (page to page routing - single page ack)  
We're caching so much data that it improves performance
Web part model
Uses really aggressive caching. Uses LKG. Some experiences then do a full refresh and some do a field by field refresh. Quickly serves up the last known good state of the page.
Suggest that you use a CDN
Minification and bundling still apply as does image optimization
Plug the performance tool – need name.
NAT still applies

Existing articles that no longer apply and need to be marked as not applying in modern:
Object cache -- update because it's not modern
Delay loading images -- old only, not in modern
In modern we load the viewport first and then load the page progressively as you go down and down.
Nav options -- this no longer applies with the changes. Update because it's not modern.
