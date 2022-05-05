---
title: "Hybrid site following"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 9b8d7f82-45d5-45e5-91c9-d728535a6567
description: "When a user follows a site, a link to that site is added to the user's Followed Sites list. If you're using both SharePoint Server and SharePoint in Microsoft 365, your users will have different followed lists for sites in each location. With SharePoint hybrid, you can consolidate the info from both locations into the SharePoint in Microsoft 365 list in Microsoft 365."
---

# Hybrid site following

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)]

When a user follows a site, a link to that site is added to the user's Followed Sites list. If you're using both SharePoint Server and SharePoint in Microsoft 365, your users will have different followed lists for sites in each location. With SharePoint hybrid, you can consolidate the info from both locations into the SharePoint in Microsoft 365 list in Microsoft 365.
  
## How hybrid site following works

When you enable hybrid site following:
  
- The **Sites** link in a SharePoint Server site is redirected to Office 365 (SharePoint Server 2013). 
    
- The **Sites** tile in the app launcher ![Microsoft 365 app launcher icon](../media/0aaa6945-f9a4-4b13-bf5f-d5c5dbe978fb.png) is redirected to Microsoft 365 (SharePoint Server 2016 and SharePoint Server 2019). 
    
- When a user follows a site in SharePoint Server, it is added to the followed list in both SharePoint Server and Microsoft 365.
    
While the SharePoint Server followed list continues to be updated, users are directed to the followed list in Microsoft 365, which contains followed sites from both locations.
  
The SharePoint in Microsoft 365 newsfeed functionality is unaffected. Users will continue to have separate newsfeeds in SharePoint Server and Microsoft 365, and each will show activities for sites and documents for SharePoint Server and Microsoft 365, respectively. Also, follow documents functionality remains unaffected, and follow people functionality remains in SharePoint Server only.
  
Note that existing followed sites lists in SharePoint Server are not migrated to Microsoft 365 when you turn this feature on (though any sites in the Microsoft 365 list will remain there). Users will have to follow their SharePoint Server sites again once the feature is turned on.
  
## Setting up hybrid site following

Hybrid site following is part of Hybrid Sites Features, and is available on both SharePoint Server 2013 and SharePoint Server 2016. For info about the other features included with Hybrid Sites Features, see [Hybrid sites features and OneDrive](sharepoint-hybrid-sites-and-search.md#SitesFeatures). 
  

