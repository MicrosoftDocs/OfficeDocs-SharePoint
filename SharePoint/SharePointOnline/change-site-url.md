---
title: "Change a site address (preview)"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
f1_keywords:
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- FRP150
- MET150
ms.assetid: aa93f89b-ffce-4edb-aa89-22b16d6915a7
description: "Learn how to change the URL of a SharePoint site."
---

# Change a site address

As a global or SharePoint admin in your organization, you can change the URL for the following types of sites:

- Office 365 group-connected team sites
- Modern team sites that don't belong to an Office 365 group
- Communication sites
- Classic team sites

You can't change the URL of sites that are locked or on hold. 

You can change only the address of the site within the URL, for example:

https://contoso.sharepoint.com/sites/*projectx*  
to
https://contoso.sharepoint.com/sites/*projecty* 

You can't change the domain ("contoso" in the previous example) or any other part of the path. For example, you can't move the site from "/sites" to "/teams."

It can take about 10 minutes to change the site address (depending on the size of the site), and the site will be read-only during this time. We recommend changing addresses during times when the site is not heavily used. 

For this preview, you can change the address of up to 10 sites at a time. To change an additional site address, wait for another change to finish. 

## Effects of changing a site address

Make sure to communicate to users when the address will change, what the new address will be, and what to expect during and after the change. A redirect will be put in place for the previous URL. File permissions will not change. Any sharing links will be automatically redirected. The OneDrive sync client (Version 17.3.6943.0625 or later) will automatically switch to syncing folders at the new URL. During the URL change, users may see that uploads are pending. The Recent lists in the Office Desktop apps and in Office Online will be updated with the new URL. The OneNote Windows Store app (version 16.0.8431.1006 and later), desktop app (version 16.0.8326.2096 and later), and mobile app (version 16.0.8431.1011 and later) will automatically detect the address change and sync notebooks at the new URL. The latest mobile apps for Android and iOS will detect the new site address

## Known issues

Users will be able to open team files through the Teams app, but only by selecting to open the library in SharePoint. 

### SharePoint mobile apps



### Apps

If an app refers to   

