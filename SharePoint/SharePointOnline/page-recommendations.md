title: How SharePoint page recommendations are genreated
ms.reviewer: patkel
ms.author: loreenl
author: spowriter
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how recommendations on modern pages are generated."

SharePoint recommendations on modern pages help you and your users discover pages and news in your organization. At the bottom of news posts and pages, you'll see recommendations especially for you or your users. Recommendations show below the heading **You may also be interested in**.

SharePoint recommendations are powered by a machine learning model that determines what other viewers have viewed the page, and ranks these viewers as they relate to the user. In general, the recommendations shown are based on what other people have read next; what is popular with your colleagues; and what is popular on your site. Only pages and posts that users have access to are shown.

FAQ​

Are Recommendations cached?​

No – SharePoint Recommendations are generated in real time. When you load a SharePoint page, the latest recommendations personalized for you are generated. This way you will always receive the latest recommendations.​


How does SharePoint Recommendations work?​

A ML model takes numerous factors into account: Recent viewers to the page, page view history of recent viewers, the relationship between recent viewers to a page and the current user, the recent view count of content. Over time, additional signals will be incorporated including likes and comments.​

What type of content is returned on SharePoint Recommendations?​

SharePoint News Posts, SharePoint Pages. Classic Pages will also show up in Recommendations.​

Can SharePoint Recommendations be enabled on Classic Pages?​

No. SharePoint Recommendations is only available on Modern Pages.​

What kind of Page View lift should I expect to see for SharePoint Recommendations?​

In Microsoft, the click through rate for SharePoint Recommendations varies between 3%-6%.​

How can I disable SharePoint Recommendations?​

Any News Post or Page editor can disable recommendations on their page. This is done through the same mechanism as comments. Click on Edit on a News Post or SharePoint Page, at the bottom of the page change the SharePoint Recommendation toggle to off.​

If you want to broadly disable SharePoint Recommendations across a site, in the Site Features section of Site Settings, there’s a toggle to turn SharePoint Recommendations on or off. PowerShell can also be used to disable recommendations across a SharePoint site.​