---
title: "Overview of analytics processing in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 31b74292-9333-455d-8c52-aba97bbfc0e6
description: "Learn how the Analytics Processing Component analyzes content and user actions to improve search relevance."
---

# Overview of analytics processing in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
To help identify and surface the content that users consider to be the most useful and relevant, the **Analytics Processing Component** in SharePoint Server analyzes both the content itself, and also the way that users interact with it. The results from the analysis are added to the items in the search index so that search relevance improves automatically over time. Also, the results are used in reports that help search administrators see which manual steps they can take to improve the search system. 
  
    
## The analytics architecture
<a name="BKMK_TheAnalyticsArchitechture"> </a>

The analytics architecture consists of these main parts:
  
- The **Analytics Processing Component** runs the analytics jobs. For more information, see [The different types of analyses](overview-of-analytics-processing.md#BKMK_TheDifferentType).
    
- The **Analytics reporting database** stores statistical information, such as usage event counts, from the different analyses. SharePoint Server uses the information in this database to create Excel reports for the search administrators. For more information, see [Usage analytics](overview-of-analytics-processing.md#BKMK_UsageAnalytics) and [Reports based on analytics processing](overview-of-analytics-processing.md#BKMK_Reporting).
    
- The **Link database** stores information about searches and crawled documents. The data in this database is processed in different sub-analyses. For more information, see [Search analytics](overview-of-analytics-processing.md#BKMK_SearchAnalytics).
    
## The different types of analyses
<a name="BKMK_TheDifferentType"> </a>

The Analytics Processing Component runs two main types of analyses: **Search analytics** and **Usage analytics**. Search analytics analyzes content in the search index, and usage analytics analyzes the user actions.
  
- **Search analytics** analyzes content that is being crawled and added to the search index. 
    
- **Usage analytics** analyzes user actions, or usage events, such as clicks or viewed items, on the SharePoint Server site.
    
### Search analytics
<a name="BKMK_SearchAnalytics"> </a>

Search analytics is a set of analyses that extracts information such as links and anchor text from content as it is being crawled and processed and stored in the search index. The extracted information is stored in the Link database together with information about clicks on search results. The information in the Link database is further processed in several sub-analyses.
  
Information that results from the search analyses is used to enrich items in the search index with information to help improve relevance and recall, and is stored in the Reporting database and included in reports.
  
**Analyses in search analytics**

|      **Analysis**      |                                                                                                                                                                                                                                                          **Description**                                                                                                                                                                                                                                                          |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anchor text processing | Anchor text processing analyzes how items in the content corpus are interlinked. It also includes the anchor texts associated with the links in the analysis. The Analytics Processing Component uses the results of the analysis to add rank points to the items in the search index.                                                                                                                                                                                                                                            |
| Click Distance         | The Click Distance analysis calculates the number of clicks between an authoritative page and the items in the search index. An authoritative page can be a top level site, for example http://www.contoso.com, or other pages that are viewed as important. You can define Authorative pages in Central Administration. <br/> <br/>  The Analytics Processing Component uses the results of the analysis to add rank points to the items in the search index.                                                                    |
| Search Clicks          | The Search Clicks analysis uses information about which items users click in search results to boost or demote items in the search index. The analysis calculates a new ranking of items compared to the base relevance.   <br/> <br/>The clicks data is stored in the Link database.                                                                                                                                                                                                                                             |
| Social Tags            | The Social Tags analysis analyses social tags, which are words or phrases that users can apply to content to categorize information in ways that are meaningful to them.   <br/> <br/>In SharePoint Server, social tags are not used for refinement, ranking, or recall by default. However, you can create custom search experiences that use social tags and the information from this analysis.                                                                                                                                |
| Social Distance        | The Social Distance analysis calculates the relationship between users who use the Follow person feature. The analysis calculates first and second level Followings: first level Followings first, and then Followings of Following.   <br/> <br/>The information is used to sort People Search results by social distance.                                                                                                                                                                                                       |
| Search Reports         | The Search Reports analysis aggregates data and stores the data in the Analytics reporting database where it's used to generate these search reports:      <br/> <br/>Number of queries    <br/> <br/>Top queries    <br/> <br/>Abandoned queries    <br/> <br/>No result queries    <br/> <br/>Query rule usage    <br/> <br/>The report information is saved in the Search service application, and not with the items in the search index. If you delete the Search service application, the report information is also deleted. |
| Deep Links             | The Deep Links analysis uses information about what people actually click in the search results to calculate what the most important sub-pages on a site are. These pages are displayed in the search results as important shortcuts for the site, and users can access the relevant sub-pages directly from the search results.                                                                                                                                                                                                  |
   
### Usage analytics
<a name="BKMK_UsageAnalytics"> </a>

Usage analytics is a set of analyses that receive information about user actions, or usage events, such as clicks or viewed items, on the SharePoint Server site. Usage analytics combines this information with information about crawled content from the Search analyses, and processes the information. Information about recommendations and usage events is added to the search index. Statistics on the different usage events is added to the search index and sent to the Analytics reporting database.
  
A default set of usage events is defined out of the box. The default events are always registered and analyzed by SharePoint Server. You can also configure custom event types. For more information about the default usage events, see [The usage events used by Usage analytics](overview-of-analytics-processing.md#BKMK_TheDefaultUsageEvents).
  
**Analyses in usage analytics**

|   **Analysis**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Usage counts     | The Usage counts analysis analyzes events, such as viewed or clicked items. The analysis calculates how many times an item is opened  *overall*  , not just from the search result page, but also, for example, when a document is opened from Word or clicked in a SharePoint Server library.   <br/> <br/>The analysis calculates both recent events and all time events, for all defined event types. By default, recent events is set to the last 14 days, but you can set it between 1 and 14 days (on-premises). The statistics data is aggregated on site level, on site collection level, and on tenant level (SPO).   <br/> <br/>The usage events are stored temporarily on the web front end and are pushed to the Search Service Application every 15 minutes. Usage events are kept on disk for up to 14 days before they are deleted. Every day, the previous full day of Usage counts data is analyzed.   <br/> <br/>Usage counts are added to the items in the search index to improve search relevancy. The information is also stored in the Analytics reporting database, and can be used to display popular items on a site. |
| Recommendations  | The Recommendations analysis creates recommendations between items based on how users have interacted with the items on a site. The analysis uses the same event file as Usage counts, but looks for patterns in the usage. The analysis calculates an item-to-item relationship graph and adds the information to the items in the search index.   <br/> <br/>The information can be used to display recommendations on a site, for example "People who viewed this also viewed".   <br/> <br/>The data is stored in the Analytics reporting database for recovery purposes. Reports related to recommendations are based on the Usage counts analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Activity ranking | The Activity ranking analysis uses the activity tracking of usage events (the event rate) to influence search relevancy. Items that have high usage activity (clicks or views) typically get a higher activity rank score than less popular items.   <br/> <br/>The analysis looks for  *trends*  in item activity. If you only count the number of events, older items will typically "win" in relevancy, because the older documents have had more time to collect activity. The activity tracking helps newer documents that have high usage activity get a higher rank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   
## The usage events used by Usage analytics
<a name="BKMK_TheDefaultUsageEvents"> </a>

SharePoint Server includes the following default usage events:
  
- Views
    
- Recommendations displayed
    
- Recommendations clicked
    
In addition to the default events, you can add up to twelve custom events. For example, you can add a custom event that tracks how often an item is accessed from a mobile platform. 
  
All usage events are counted per item, site collection, and tenant (SPO).
  
## Reports based on analytics processing
<a name="BKMK_Reporting"> </a>

The Analytics Processing Component generates data that is used to create the following usage reports:
  
- **Popularity Trends** An Excel report that shows the daily and monthly count per usage event for a site collection, site, or specific item in a SharePoint library or list. 
    
    > [!NOTE]
    > **Unique Users** shows the number of unique users per day, while **Unique Users** *per month*  shows SUM(UU/Day) for the month. 
  
- **Most Popular Items** Shows ranking per usage event for  *all items*  in a library or list, for example the most viewed items in the library or list. The ranking can be sorted by **Recent** or **Ever**. 
    
## Privacy protection of the data collected by the Analytics Processing Component
<a name="BKMK_Reporting"> </a>

Parts of the data that the Analytics Processing Component collects are related to personally identifiable information. SharePoint Server has different features to protect the privacy of this information.
  
For each usage event, the Analytics Processing Component logs the following information:
  
- The URL of the item where the usage event occurred.
    
- The SiteID, the WebID, and the TenantID where the usage event occurred.
    
- The time and the date when the usage event occurred.
    
- The obfuscated user ID of the person who caused the usage event to occur.
    
This data is stored in the Search service application before it is processed by the Analytics Processing Component. The data is automatically removed after 30 days. The following list shows the results of the data processing:
  
- The total number of usage events.
    
- The total number of unique usage events.
    
- Item-to-item recommendations.
    
- Relevance features.
    
These results are stored in the analytics reporting database, and in the search index. No user information is stored as a result of the data processing. The obfuscated user ID is only used when calculating the unique usage event counts, and calculating item-to-item recommendations.
  
You can view the results in two usage reports. For more information, see [View usage reports in SharePoint Server](../administration/view-usage-reports.md).
  
### Usage cookies for sites that have anonymous users

By default, usage cookies are not enabled for a SharePoint Server web application. To generate unique user counts and item-to-item recommendations for sites that have anonymous users, SharePoint Server enables you to use usage cookies for a SharePoint web application. When you enable usage cookies, this generates a unique GUID that is used as a user ID when data is being processed. The GUID is available for the lifetime of the cookie, and it is used as a user ID when data is being processed. The lifetime of the cookie is 14 days.
  
> [!IMPORTANT]
> Local legal restrictions might apply when you enable cookies on sites that have anonymous users. 
  
To enable usage cookies for a SharePoint web application, see [Edit general settings on a web application in SharePoint Server](/SharePoint/administration/edit-general-settings-on-a-web-application). This article also applies to SharePoint Server 2016.
  

