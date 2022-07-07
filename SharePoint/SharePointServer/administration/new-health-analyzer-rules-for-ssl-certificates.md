---
title: "New health analyzer rules for SSL certificates"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how SSL certificate implements health analyzer."
---

# New health analyzer rules for SSL certificates

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

SharePoint has implemented the following four new health analyzer rules for SSL certificates:

1. **Certificate notification contacts haven't been configured** health rule that provides notification through Central Administration when certificates are in use and no certificate notification contacts have been configured. This health rule will run weekly. Certificate notification contacts receive emails about SSL certificate expirations and can be configured by customers through the Configure certificate management settings page.
2. **Upcoming SSL certificate expirations** health rule that provides advanced notification through both Central Administration and email of upcoming certificate expirations. This health rule will run weekly to notify certification notification contacts about certificates that are in use and will expire within the next 15 - 60 days. These thresholds are configurable by customers through the Configure certificate management settings page.
3. **SSL certificates are about to expire** health rule that provides advanced notification through both Central Administration and email when certificates are about to expire. This health rule will run daily to notify certificate notification contacts about certificat]es that are in use and will expire within the next 15 days. This threshold is configurable by customers through the Configure certificate management settings page.
4. **SSL certificates have expired** health rule that provides notification through both Central Administration and email when certificates have expired. This health rule will run daily to notify certificate notification contacts about certificates that are in use and have expired within the past 15 days. This threshold is configurable by customers through the Configure certificate management settings page.