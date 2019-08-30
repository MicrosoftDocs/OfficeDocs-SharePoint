---
title: "Best practices for crawling in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 73f19541-9321-4abd-b014-98df79f84d2a
description: "Learn about best practices for crawling in SharePoint Server."
---

# Best practices for crawling in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Learn about best practices for crawling in SharePoint Server.
  
The Search system crawls content to build a search index that users can run search queries against. This article contains suggestions as to how to manage crawls most effectively.
  
    
## Use the default content access account to crawl most content
<a name="BKMK_UseDefault"> </a>

The default content access account is a domain account that you specify for the SharePoint Server Search service to use by default for crawling. For simplicity, it is best to use this account to crawl as much as possible of the content that is specified by your content sources. To change the default content access account, see [Change the default account for crawling in SharePoint Server](change-the-default-account-for-crawling.md).
  
When you cannot use the default content access account for crawling a particular URL (for example, for security reasons), you can create a crawl rule to specify one of the following alternatives for authenticating the crawler:
  
- A different content access account
    
- A client certificate
    
- Form credentials
    
- A cookie for crawling
    
- Anonymous access
    
For more information, see [Manage crawl rules in SharePoint Server](manage-crawl-rules.md).
  
## Use content sources effectively
<a name="BKMK_UseContentSources"> </a>

A content source is a set of options in a Search service application that you use to specify each of the following:
  
- One or more start addresses to crawl.
    
- The type of content in the start addresses (such as SharePoint Server sites, file shares, or line-of-business data). You can specify only one type of content to crawl in a content source. For example, you would use one content source to crawl SharePoint Server sites, and a different content source to crawl file shares.
    
- A crawl schedule and a crawl priority for full or incremental crawls that will apply to all of the content repositories that the content source specifies.
    
When you create a Search service application, the search system automatically creates and configures one content source, which is named **Local SharePoint sites**. This preconfigured content source is for crawling user profiles, and for crawling all SharePoint Server sites in the web applications with which the Search service application is associated. You can also use this content source for crawling content in other SharePoint Server farms, including SharePoint Server 2007 farms, SharePoint Server 2010 farms, SharePoint Server 2013 farms, or other SharePoint Server farms.
  
Create additional content sources when you want to do any of the following:
  
- Crawl other types of content
    
- Limit or increase how much content to crawl
    
- Crawl certain content more or less frequently
    
- Set different priorities for crawling certain content (this applies to full and incremental crawls, but not to continuous crawls)
    
- Crawl certain content on different schedules (this applies to full and incremental crawls, but not to continuous crawls)
    
However, to keep administration as easy as possible, we recommend that you limit the number of content sources that you create and use.
  
### Using content sources to schedule crawls

You can edit the preconfigured content source **Local SharePoint sites** to specify a crawl schedule; it does not specify a crawl schedule by default. For any content source, you can start crawls manually, but we recommend that you schedule incremental crawls or enable continuous crawls to make sure that content is crawled regularly. 
  
Consider using different content sources to crawl content on different schedules for the following reasons.
  
- To accommodate server down times and periods of peak server usage.
    
- To crawl content that is hosted on slower servers separately from content that is hosted on faster servers.
    
- To frequently crawl content that is updated more often.
    
Crawling content can significantly decrease the performance of the servers that host the content. The effect depends on whether the host servers have sufficient resources (especially CPU and RAM) to handle the load. Therefore, when you plan crawl schedules, consider the following best practices:
  
- Schedule crawls for each content source during times when the servers that host the content are available and when there is low demand on the server resources.
    
- Stagger crawl schedules so that the load on crawl servers and host servers is distributed over time. You can optimize crawl schedules in this manner as you become familiar with the typical crawl durations for each content source by checking the crawl log. For more information, see [Crawl log](view-search-diagnostics.md#proc3) in [View search diagnostics in SharePoint Server](view-search-diagnostics.md).
    
- Run full crawls only when it is necessary. For more information, see [Reasons to do a full crawl](plan-crawling-and-federation.md#Plan_full_crawl) in [Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md). For any administrative change that requires a full crawl to take effect, such as creation of a crawl rule, perform the change shortly before the next full crawl so that an additional full crawl is not necessary. For more information, see [Manage crawl rules in SharePoint Server](manage-crawl-rules.md).
    
## Crawl user profiles before you crawl SharePoint Server sites
<a name="BKMK_CrawlUserProfiles"> </a>

By default, in the first Search service application in a farm, the preconfigured content source **Local SharePoint sites** contains at least the following two start addresses: 
  
- https://webAppUrl, which is for crawling the Default Zone URL specified for the existing Web Application(s)
    
- sps3s://myWebAppUrl, which is for crawling user profiles
    
However, if you are deploying "People Search", we recommend that you create a separate content source for the start address sps3s://myWebAppUrl and run a crawl for that content source first. The reason for doing this is that after the crawl finishes, the search system generates a list to standardize people's names. This is so that when a person's name has different forms in one set of search results, all results for that person are displayed in a single group (known as a **result block**). For example, for the search query "Anne Weiler", all documents authored by Anne Weiler or A. Weiler or alias AnneW can be displayed in a result block that is labeled "Documents by Anne Weiler". Similarly, all documents authored by any of those identities can be displayed under the heading "Anne Weiler" in the refinement panel if "Author" is one of the categories there.
  
 **To crawl user profiles and then crawl SharePoint Server sites**
  
1. Verify that the user account that performs this procedure is an administrator for the Search service application that you want to configure.
    
2. Follow the instructions in [Deploy people search in SharePoint Server](deploy-people-search.md). As part of those instructions, you do the following:
    
  - Create a content source that is only for crawling user profiles (the profile store). You might give that content source a name such as People. In the new content source, in the **Start Addresses** section, type sps3s:// myWebAppUrl, where myWebAppUrl is the URL of the My Site host. 
    
  - Start a crawl for the People content source that you just created. 
    
  - Delete the start address sps3s://myWebAppUrl from the preconfigured content source **Local SharePoint sites**.
    
3. Wait about two hours after the crawl for the People content source finishes. 
    
4. Start the first full crawl for the content source **Local SharePoint sites**.
    
## Use continuous crawls to help ensure that search results are fresh
<a name="BKMK_UseContinuousCrawls"> </a>

 **Enable continuous crawls** is a crawl schedule option that you can select when you add or edit a content source of type **SharePoint Sites**. A continuous crawl crawls content that was added, changed, or deleted since the last crawl. A continuous crawl starts at predefined time intervals. The default interval is every 15 minutes, but you can set continuous crawls to occur at shorter intervals by using Microsoft PowerShell. Because continuous crawls occur so often, they help ensure search-index freshness, even for SharePoint Server content that is frequently updated. Also, while an incremental or full crawl is delayed by multiple crawl attempts that are returning an error for a particular item, a continuous crawl can be crawling other content and contributing to index freshness, because a continuous crawl doesn't process or retry items that repeatedly return errors. Such errors are retried during a "clean-up" incremental crawl, which automatically runs every four hours for content sources that have continuous crawl enabled. Items that continue to return errors during the incremental crawl will be retried during future incremental crawls, but will not be picked up by the continuous crawls until the errors are resolved.

A single continuous crawl includes all content sources in a Search service application for which continuous crawls are enabled. Similarly, the continuous crawl interval applies to all content sources in the Search service application for which continuous crawls are enabled. For more information, see [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md).
  
Continuous crawls increase the load on the crawler and on crawl targets. Make sure that you plan and scale out accordingly for this increased consumption of resources. For each large content source for which you enable continuous crawls, we recommend that you configure one or more front-end web servers as dedicated targets for crawling. For more information, see [Manage crawl load (SharePoint Server 2010)](/previous-versions/office/sharepoint-server-2010/dd335962(v=office.14)).
  
## Use crawl rules to exclude irrelevant content from being crawled
<a name="BKMK_UseCrawlRules"> </a>

Because crawling consumes resources and bandwidth, during initial deployment it might be better to crawl a small amount of content that you know is relevant, instead of crawling a larger amount of content, some of which might not be relevant. To limit how much content that you crawl, you can create crawl rules for the following reasons:
  
- To avoid crawling irrelevant content by excluding one or more URLs.
    
- To crawl links on a URL without crawling the URL itself. This is useful for sites that do not contain relevant content but have links to relevant content.
    
By default, the crawler will not follow complex URLs, which are URLs that contain a question mark followed by additional parameters — for example, http://contoso/page.aspx?x=y. If you enable the crawler to follow complex URLs, this can cause the crawler to gather many more URLs than is expected or appropriate. This can cause the crawler to gather unnecessary links, fill the crawl database with redundant links, and result in an index that is unnecessarily large.
  
These measures can help reduce the use of server resources and network traffic, and can increase the relevance of search results. After the initial deployment, you can review the query and crawl logs and adjust content sources and crawl rules to include more content if it is necessary. For more information, see [Manage crawl rules in SharePoint Server](manage-crawl-rules.md).
  
## Crawl the default zone of SharePoint Server web applications
<a name="BKMK_CrawlDefaultZone"> </a>

When you crawl the default zone of a SharePoint Server web application, the query processor automatically maps and returns search-result URLs so that they are relative to the alternate access mapping (AAM) zone from which queries are performed. This makes it possible for users to readily view and open search results.
  
However, if you crawl a zone of a web application other than the default zone, the query processor does not map search-result URLs so that they are relative to the AAM zone from which queries are performed. Instead, search-result URLS will be relative to the non-default zone that was crawled. Because of this, users might not readily be able to view or open search results.
  
For example, assume that you have the following AAMs for a web application named WebApp1:
  
| **Default** |  **Public URL**  | **Authentication provider**  |
| :---------- | :--------------- | :--------------------------- |
| Default     | https://contoso  | Windows authentication: NTLM |
| Extranet    | https://fabrikam | Forms-based authentication   |
| Intranet    | http://fabrikam  | Windows authentication: NTLM |
   
Now, say that you crawl the default zone, https://contoso. When users perform queries from https://contoso/searchresults.aspx, URLs of results from WebApp1 will all be relative to https://contoso, and therefore will be of the form https://contoso/ _path_/ _result_.aspx.
  
Similarly, when queries originate from the Extranet zone—in this case, https://fabrikam/searchresults.aspx—results from WebApp1 will all be relative to https://fabrikam, and therefore will be of the form https://fabrikam/ _path_/ _result_.aspx.
  
In both of the previous cases, because of the zone consistency between the query location and the search-result URLs, users will readily be able to view and open search results, without having to change to the different security context of a different zone.
  
However, now instead say that you crawl a non-default zone such as the Intranet zone, http://fabrikam. In this case, for queries from any zone, URLs of results from WebApp1 will always be relative to the non-default zone that was crawled. That is, a query from https://contoso/searchresults.aspx, https://fabrikam/searchresults.aspx, or http://fabrikam/searchresults.aspx will yield search-result URLs that begin with the non-default zone that was crawled, and therefore will be of the form http://fabrikam/ _path_/ _result_.aspx. This can cause unexpected or problematic behavior such as the following:
  
- When users try to open search results, they might be prompted for credentials that they don't have. For example, forms-based authenticated users in the Extranet zone might not have Windows authentication credentials.
    
- The results from WebApp1 will use HTTP, but users might be searching from the Extranet zone at https://fabrikam/searchresults.aspx. This might have security implications because the results will not use secure sockets layer (SSL) encryption.
    
- Refinements might not filter correctly, because they filter on the public URL for the default zone instead of the URL that was crawled. This is because URL-based properties in the index will be relative to the non-default URL that was crawled.
    
## Reduce the effect of crawling on SharePoint Server crawl targets
<a name="BKMK_ReduceEffect"> </a>

You can reduce the effect of crawling on SharePoint Server crawl targets (that is, SharePoint Server front-end web servers) by doing the following:
  
- For a small SharePoint Server environment, redirect all crawl traffic to a single SharePoint Server front-end web server. For a large environment, redirect all crawl traffic to a specific group of front-end web servers. This prevents the crawler from using the same resources that are being used to render and serve web pages and content to active users.
    
- Limit search database usage in Microsoft SQL Server to prevent the crawler from using shared SQL Server disk and processor resources during a crawl.
    
For more information, see [Manage crawl load (SharePoint Server 2010)](/previous-versions/office/sharepoint-server-2010/dd335962(v=office.14)).
  
### Using crawler impact rules to limit the effect of crawling

To limit crawler impact, you can also create crawler impact rules, which are available from the Search_service_application_name: Search Administration page. A crawler impact rule specifies the rate at which the crawler requests content from a start address or range of start addresses. Specifically, a crawler impact rule either requests a specified number of documents at a time from a URL without waiting between requests, or it requests one document at a time from the URL and waits a specified time between requests. Each crawler impact rule applies to all crawl components.
  
For servers in your organization, you can set crawler impact rules based on known server performance and capacity. However, this might not be possible for external sites. Therefore, you might unintentionally use too many resources on external servers by requesting too much content or requesting content too frequently. This could cause administrators of those external servers to limit server access so that it becomes difficult or impossible for you to crawl those repositories. Therefore, set crawler impact rules to have as little effect on external servers as possible while you still crawl enough content frequently enough to make sure that that the freshness of the index meets your requirements. 
  
## Use Active Directory groups instead of individual users for permissions
<a name="BKMK_UseADGroups"> </a>

The ability of a user or group to perform various activities on a site is determined by the permission level that you assign. If you add or remove users individually for site permissions, or if you use a SharePoint Server group to specify site permissions and you change the membership of the group, the crawler must perform a "security-only crawl", which updates all affected items in the search index to reflect the change. Similarly, adding or updating web application policy with different users or SharePoint Server groups will trigger a crawl of all content covered by that policy. This increases crawl load and can reduce search-results freshness. Therefore, to specify site permissions, it is best to use Active Directory Domain Services (AD DS) groups, because this does not require the crawler to update the affected items in the search index.
  
## Add a second crawl component to provide fault tolerance
<a name="BKMK_AddSecond"> </a>

When you create a Search service application, the default search topology includes one crawl component. A crawl component retrieves items from content repositories, downloads the items to the server that hosts the crawl component, passes the items and associated metadata to a content processing component, and adds crawl-related information to associated crawl databases. You can add a second crawl component to provide fault tolerance. If one crawl component becomes unavailable, the remaining crawl component will take over all of the crawling. For most SharePoint Server farms, a total of two crawl components is sufficient.
  
For more information, see the following articles:
  
- [Overview of search architecture in SharePoint Server](search-architecture-overview.md)
    
- [Change the default search topology in SharePoint Server](change-the-default-search-topology.md)
    
- [Manage search components in SharePoint Server](manage-search-components.md)
    
- [New-SPEnterpriseSearchCrawlComponent](/powershell/module/sharepoint-server/New-SPEnterpriseSearchCrawlComponent?view=sharepoint-ps)
    
## Manage environment resources to improve crawl performance
<a name="BKMK_ManageEnvironment"> </a>

As the crawler crawls content, downloads the content to the crawl server (the server that hosts the crawl component), and feeds the content to content processing components, several factors can adversely affect performance. To improve crawl performance, you can do the following:
  
| **To address this potential performance bottleneck** |                                       **Implement this solution**                                        |
| :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| Slow response time from crawled servers              | Provide more CPU and RAM and faster disk I/O                                                             |
| Low network bandwidth                                | Install one or two one-gigabit-per-second network adapters on each crawl server                          |
| Content processing                                   | Provide more content processing components, and more CPU resources for each content processing component |
| Slow processing by the index components              | Add I/O resources for servers that host index components                                                 |
   
For more information, see the following resources:
  
- [Scale search for Internet sites in SharePoint Server](scale-search-for-internet-sites.md)
    
- [SharePoint 2013: Crawl scaling recommendations](https://social.technet.microsoft.com/wiki/contents/articles/16490.sharepoint-2013-crawl-scaling-recommendations.aspx)
    
## Make sure no crawls are active before you change the search topology
<a name="BKMK_MakeSureNoCrawls"> </a>

We recommend that you confirm that no crawls are in progress before you initiate a change to the search topology. Otherwise, it is possible that the topology change will not occur smoothly.
  
If necessary, you can manually pause or stop full or incremental crawls, and you can disable continuous crawls. For more information, see the following articles:
  
- [Start, pause, resume, or stop a crawl in SharePoint Server](start-pause-resume-or-stop-a-crawl.md)
    
- [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md)
    
> [!NOTE]
> Pausing a crawl has the disadvantage that references to crawl components can remain in the MSSCrawlComponentsState table in the search administration database. This can cause a problem if you want to remove any crawl components (say, because you want to remove a server that hosts those components from the farm). However, when you stop a crawl, references to crawl components in the MSSCrawlComponentsState table are deleted. Therefore, if you want to remove crawl components, it is better to stop crawls than to pause crawls. 
  
To confirm that no crawls are in progress, on the  _Search_service_application_name_: Manage Content Sources page, make sure that the value in the **Status** field for each content source is either **Idle** or **Paused**. (When a crawl is completed, or when you stop a crawl, the value in the **Status** field for the content source will change to **Idle**.)
  
## Remove crawl components from a crawl host before you remove the host from a farm
<a name="BKMK_RemoveCrawlComponents"> </a>

When a server hosts a crawl component, removing the server from the farm can make it impossible for the Search system to crawl content. Therefore, before you remove a crawl host from a farm, we strongly recommend that you do the following:
  
1. Make sure that no crawls are active.
    
    For more information, see the previous section, [Make sure no crawls are active before you change the search topology](#BKMK_MakeSureNoCrawls).
    
2. Remove or relocate crawl components that are on that host.
    
For more information, see the following resources:
  
- [Manage the search topology in SharePoint Server](manage-the-search-topology.md)
    
- [Change the default search topology in SharePoint Server](change-the-default-search-topology.md)
    
- [Remove a search component](manage-search-components.md#Search_Comp_Remove) or [Move a search component](manage-search-components.md#Search_Comp_Move) in [Manage search components in SharePoint Server](manage-search-components.md)
    
- [Remove a server from a farm in SharePoint Server 2016](../administration/remove-a-server-from-a-farm-in-sharepoint-server-2016.md)
    
- [SP2010: Removing/Re-joining Server to a Farm Can Break Search](https://blogs.msdn.com/b/sharepoint_strategery/archive/2013/07/08/sp2010-broken-topology-and-hung-crawls-can-be-caused-by-serverid-mismatch.aspx)
    
## Test crawl and query functionality after you change the crawl configuration or apply updates
<a name="BKMK_TestCrawl"> </a>

We recommend that you test the crawl and query functionality in the server farm after you make configuration changes or apply updates. The following procedure is an example of an easy way to perform such a test.
  
 **To test the crawl and query functionality**
  
1. Verify that the user account that performs this procedure is an administrator for the Search service application that you want to configure.
    
2. Create a content source that you will use temporarily just for this test.
    
    In the new content source, in the **Start Addresses** section, in the **Type start addresses below (one per line)** box, specify a start address that contains several items that are not already in the index — for example, several TXT files that are on a file share. For more information, see [Add, edit, or delete a content source in SharePoint Server](add-edit-or-delete-a-content-source.md).
    
3. Start a full crawl for that content source.
    
    For more information, see [Start, pause, resume, or stop a crawl in SharePoint Server](start-pause-resume-or-stop-a-crawl.md). When the crawl is complete, on the  _Search_service_application_name_: Manage Content Sources page, the value in the **Status** column for the content source will be **Idle**. (To update the **Status** column, refresh the Manage Content Sources page by clicking **Refresh**.)
    
4. When the crawl is complete, go to the Search Center and perform search queries to find those files.
    
    If your deployment does not already have a Search Center, see [Create a Search Center site in SharePoint Server](create-a-search-center-site.md).
    
5. After you finish testing, delete the temporary content source.
    
    This removes the items specified by that content source from the search index so that they do not appear in search results after you finish testing.
    
## Use the crawl log and crawl-health reports to diagnose problems
<a name="BKMK_UseCrawlLog"> </a>

The crawl log tracks information about the status of crawled content. The log includes views for content sources, hosts, errors, databases, URLs, and history. For example, you can use this log to determine the time of the last successful crawl for a content source, whether crawled content was successfully added to the index, whether it was excluded because of a crawl rule, or whether crawling failed because of an error. 
  
Crawl-health reports provide detailed information about crawl rate, crawl latency, crawl freshness, content processing, CPU and memory load, continuous crawls, and the crawl queue.
  
You can use the crawl log and crawl-health reports to diagnose problems with the search experience. The diagnostic information can help you determine whether it would be helpful to adjust elements such as content sources, crawl rules, crawler impact rules, crawl components, and crawl databases.
  
For more information, see [View search diagnostics in SharePoint Server](view-search-diagnostics.md).
  

