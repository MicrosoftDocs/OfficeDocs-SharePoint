---
title: "Plan crawling and federation in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/6/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 4356bad9-de1d-4e81-b049-17248b4a86c1
description: "Plan to crawl or federate for search in SharePoint Server."
---

# Plan crawling and federation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Before users can perform searches in SharePoint Server, you must crawl or federate the content that you want them to be able to search. When you crawl content, the Search service builds a search index that users can run queries (search requests) against. You can also configure the Search system to display search results from an external provider (such as Bing) alongside the results from the local search index. The process of getting search results from an external provider and displaying the results locally is called federation.
  
    
## Plan content sources
<a name="Section2"> </a>

A  *content source*  is a definition of a group of crawl settings such as which hosts to crawl, the type of content that will be crawled (such as SharePoint content or file shares), a crawl schedule, and how deep to crawl. 
  
When you create a Search service application, the service application automatically provides the pre-configured content source **Local SharePoint sites**. You can use this content source to specify how to crawl all SharePoint content in web applications that are associated with the Search service application. 
  
If you have only one type of content (for example, all content is of type SharePoint sites or type file shares), you might need only one content source. However, if you have different types of content or unique requirements per host, you might want to define multiple content sources. Plan to create additional content sources when you have to do the following:
  
- Crawl different types of content — for example, file shares and data in a line-of-business application
    
- Crawl some content on different schedules than other content
    
- Limit or increase the quantity of content that is crawled
    
- Set different priorities for crawling different sites
    
- Keep some types of content fresher than others
    
You can create a large number of content sources in each Search service application, but there is overhead associated with each content source. Therefore, we recommend that you create the smallest number of content sources that satisfy your other operational requirements, such as differences in crawl priority and crawl scheduling. Each content source can contain up to 100 start addresses.
  
### Plan to crawl different kinds of content
<a name="Section3"> </a>

You can crawl only one kind of content per content source. For example, you can create a content source that contains start addresses for SharePoint sites and another content source that contains start addresses for file shares, but you cannot create a single content source that contains start addresses to both SharePoint sites and file shares. The following table lists the kinds of content sources that you can configure.
  
| **Use this kind of content source** |                                                                                                                                                                                                                                                                                                                                                                                                **For this content**                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SharePoint sites                    | SharePoint sites from the same farm or different SharePoint Server farms.  <br/><br/> SharePoint sites from the same farm or different SharePoint Server 2019, SharePoint Server 2016, SharePoint Server 2013, SharePoint Server 2010, SharePoint Foundation 2010, or Microsoft Search Server 2010 farms.  <br/> <br/>SharePoint sites from the same farm or different Office SharePoint Server 2007, Windows SharePoint Services 3.0, or Search Server 2008 farms.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Web sites                           | Other web content in your organization that is not located in SharePoint sites.  <br/><br/> Content on web sites on the Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| File shares                         | Content on file shares in your organization.  <br/> <br/>**Security note:** When the Search service crawls a file share, if the permissions on a file on the share are different from the permissions on folders that contain the file, then the permissions on the file take precedence and are used for security trimming of search results. Therefore, to ensure that only appropriate items appear in search results, make sure that the permissions for files on file shares are appropriate. For cases in which file permissions are not appropriate, you can delete particular items from the search index or from search results. For more information, see [Delete items from the search index or from search results in SharePoint Server](delete-items-from-the-search-index-or-from-search-results.md). |
| Exchange public folders             | Exchange 2007 and Exchange Server 2010 public folders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Lotus Notes                         | E-mail messages stored in Lotus Notes databases.  <br/> <br/>**Note:** Unlike all other kinds of content sources, the Lotus Notes content source option does not appear in the user interface until you have installed and configured the appropriate prerequisite software. For more information, see [Configure and use the Lotus Notes connector for SharePoint Server](configure-and-use-the-lotus-notes-connector.md) (also applies to SharePoint Server).                                                                                                                                                                                                                                                                                                                                                     |
| Documentum                          | Content from the EMC Documentum system.  <br/> <br/>**Note:** You can't crawl EMC Documentum content before you have installed and configured the appropriate prerequisite software and the Microsoft SharePoint Indexing Connector for Documentum. For more information, see [Configure and use the Documentum connector in SharePoint Server](configure-and-use-the-documentum-connector.md) (also applies to SharePoint Server).                                                                                                                                                                                                                                                                                                                                                                            |
| Line-of-business data               | Business data that is stored in line-of-business applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Custom repository                   | Content sources that can only be crawled after a custom connector is installed and registered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   
#### Content sources for line-of-business data

Business data content sources require that the applications hosting the data are specified in an Application Model in a Business Data Connectivity service application. You can create one content source to crawl all applications that are registered in the Business Data Connectivity service, or you can create separate content sources to crawl individual applications. For more information, see [Search connector framework in SharePoint 2013](https://msdn.microsoft.com/library/office/ee556429%28v=office.15%29) (This MSDN article also applies to SharePoint Server). 
  
Often, the people who plan for integration of business data into site collections are not the same people involved in the overall content planning process. Therefore, include business application administrators in content planning teams so that they can advise you how to integrate the business application data into content and effectively present it in the site collections. 
  
### Crawl content on different schedules
<a name="Section5"> </a>

Consider defining content sources with different schedules for the following reasons:
  
- To accommodate down times and periods of peak usage.
    
- To more frequently crawl content that is more frequently updated.
    
- To crawl content that is located on slower servers separately from content that is located on faster servers.
    
- To continuously crawl a SharePoint content source because of high freshness demands. For more information, see [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md).
    
### Reasons to do a full crawl
<a name="Plan_full_crawl"> </a>

Reasons for a Search service application administrator to do a full crawl for one or more content sources include the following:
  
- A Search service application has just been created and the preconfigured content source **Local SharePoint sites** has not been crawled yet. 
    
- Some other content source is new and has not been crawled yet.
    
- The Search service application administrator has changed a content source.
    
- A software update or service pack was installed on servers in the farm. See the instructions for the software update or service pack for more information.
    
- A Search service application administrator or site collection administrator added or changed a managed property. A full crawl of all affected content sources is required for the new or changed managed property to take effect. 
    
- You want to detect security changes that were made to local groups on a file share after the last full crawl of the file share.
    
- You want to resolve consecutive incremental crawl failures. If an incremental crawl fails a large number of consecutive times for any particular content, the system removes the affected content from the search index.
    
- Crawl rules have been added, deleted, or modified.
    
- You want to replace a corrupted search index.
    
- The permissions for the user account that is assigned to the default content access account have changed.
    
The system does a full crawl even when an incremental crawl or continuous crawl is scheduled under the following circumstances:
  
- A search administrator stopped the previous crawl.
    
- A content database was restored, or a farm administrator has detached and reattached a content database.
    
- A full crawl of the content source has never been done from this Search service application.
    
- The crawl database does not contain entries for the addresses that are being crawled. Without entries in the crawl database for the items being crawled, incremental crawls cannot occur.
    
### Limit or increase the quantity of content that is crawled
<a name="Section6"> </a>

The options available in the properties for each content source vary depending on the content source type that you select. You can use crawl setting options to limit or increase the quantity of content that is crawled. For each content source, you can specify how extensively to crawl the start addresses. Most content source types allow you to specify how many levels deep in the hierarchy from each start address to crawl. This behavior is applied to all start addresses in a particular content source. If you have to crawl some sites at deeper levels, you can create additional content sources that include those sites. The following table describes best practices when you configure crawl setting options.
  
|    **For this kind of content source**    |                                                                                           **If this pertains**                                                                                           |                                                                                                                               **Use this crawl setting option**                                                                                                                                |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SharePoint sites                          | You want to include the content that is on the site itself and you do not want to include the content that is on subsites, or you want to crawl the content that is on subsites on a different schedule. | Crawl only the SharePoint site of each start address.                                                                                                                                                                                                                                          |
| SharePoint sites                          | You want to include the content on the site itself.  <br/> <br/> -or-  <br/> <br/> You want to crawl all content under the start address on the same schedule.                                           | Crawl everything under the host name of each start address.                                                                                                                                                                                                                                    |
| Web sites                                 | Content available on linked sites is unlikely to be relevant.                                                                                                                                            | Crawl only within the server of each start address.                                                                                                                                                                                                                                            |
| Web sites                                 | Relevant content is located on only the first page.                                                                                                                                                      | Crawl only the first page of each start address.                                                                                                                                                                                                                                               |
| Web sites                                 | You want to limit how deep to crawl the links on the start addresses.                                                                                                                                    | Custom — Specify the number of pages deep and number of server hops to crawl.  <br/> <br/> **Note:** For a highly connected site, we recommend that you start with a small number, because specifying more than three pages deep or more than three server hops can crawl the entire Internet. |
| File shares <br/> Exchange public folders | Content available in the subfolders is unlikely to be relevant.                                                                                                                                          | Crawl only the folder of each start address.                                                                                                                                                                                                                                                   |
| File shares<br/> Exchange public folders  | Content in the subfolders is likely to be relevant.                                                                                                                                                      | Crawl the folder and subfolders of each start address.                                                                                                                                                                                                                                         |
| Business data                             | All applications that are registered in the Business Data Catalog metadata store contain relevant content.                                                                                               | Crawl the whole Business Data Catalog metadata store.                                                                                                                                                                                                                                          |
| Business data                             | Not all applications that are registered in the BDC metadata store contain relevant content.  <br/> <br/> -or- <br/> <br/> You want to crawl some applications on a different schedule.                  | Crawl selected applications.                                                                                                                                                                                                                                                                   |
   
### Plan connectors
<a name="Section4"> </a>

The crawler uses connectors (known as "protocol handlers" in earlier versions of SharePoint Server) to acquire and index content. For the most commonly-used protocols, SharePoint Server provides and automatically uses the appropriate connectors. To crawl content that requires a connector that is not provided by default, you must first install a third-party connector or build a custom connector. For a list of connectors that are installed by default, see [Default connectors in SharePoint Server](../technical-reference/default-connectors.md) (also applies to SharePoint Server). 
  
### Other considerations when planning content sources
<a name="Section4"> </a>

For content repositories that are of the same type, such as SharePoint sites, your decision about whether to use one or more content sources depends largely upon administrative considerations. To make administration easier, organize content sources in such a way that updating content sources, crawl rules, and crawl schedules is convenient for administrators.
  
- You can't crawl the same start addresses by using multiple content sources in the same Search service application. For example, if you use a particular content source to crawl a site collection and all its subsites, you cannot use a different content source to crawl one of those subsites separately on a different schedule.
    
- Administrators often update content sources. Changing a content source requires a full crawl for that content source. Therefore, consider creating separate content sources so that you can run multiple full crawls at the same time if necessary, and so that a full crawl for any particular content source is less time-consuming.
    
### Plan crawl rules to optimize crawls
<a name="Section7"> </a>

Crawl rules apply to all content sources in the Search service application. You can apply crawl rules to a particular URL or set of URLs to do the following things:
  
- Avoid crawling irrelevant content by excluding one or more URLs. This also helps reduce the use of server resources and network traffic.
    
- Crawl links on the URL without crawling the URL itself. This option is useful for sites that have links of relevant content when the page that contains the links does not contain relevant information.
    
- Enable complex URLs to be crawled. This option directs the system to crawl URLs that contain a query parameter specified with a question mark. Depending upon the site, these URLs might not include relevant content. Because complex URLs can often redirect to irrelevant sites, it is a good idea to enable this option only on sites where you know that the content available from complex URLs is relevant.
    
- Enable content on SharePoint sites to be crawled as HTTP pages. This option enables the Search system to crawl SharePoint sites that are behind a firewall or in scenarios in which the site being crawled restricts access to the Web service that is used by the crawler (a crawl component in the search topology).
    
- Specify whether to use the default content access account, a different content access account, or a client certificate for crawling the specified URL.
    
Because crawling content consumes resources and bandwidth, it is better to include a smaller amount of content that you know is relevant than a larger amount of content that might be irrelevant. After the initial deployment, you can review the query and crawl logs and adjust content sources and crawl rules to be more relevant and include more content. 
  
### Plan crawler authentication
<a name="PlanCrawlerAuth"> </a>

When the crawler accesses the start addresses that are listed in content sources, the crawler must be authenticated by, and granted access to, the servers that host that content. By default, the system uses the default content access account. Or, you can use crawl rules to specify a different content access account to use when crawling particular content. Whether you use the default content access account or a different content access account specified by a crawl rule, the content access account that you use must have at least read permissions on all content that is crawled. If the content access account does not have read permissions, the content is not crawled, is not indexed, and therefore is not available to queries.
  
We recommend that the account that you specify as the default content access account has access to most of your crawled content. Only use other content access accounts when security considerations require separate content access accounts. 
  
For each content source that you plan, determine the start addresses that cannot be accessed by the default content access account, and then plan to add crawl rules for those start addresses.
  
> [!IMPORTANT]
> Ensure that the domain account that is used for the default content access account or any other content access account is not the same domain account that is used by an application pool associated with any Web application that you crawl. Doing so can cause unpublished content in SharePoint sites and minor versions of files (that is, history) in SharePoint sites to be crawled and indexed. 
  
Another important consideration is that the crawler must use the same authentication protocol as the host server. By default, the crawler authenticates by using NTLM. You can configure the crawler to use a different authentication protocol, if it is necessary.
  
If you are using claims-based authentication, make sure that Windows authentication is enabled on any Web applications to be crawled. 
  
## Plan content processing
<a name="Section8"> </a>

The crawler crawls content repositories specified by content sources and then feeds the contents and metadata of crawled items to the content processing component. The content processing component reads and parses the crawled properties and then reports the properties to the Search Administration database.
  
You can map crawled properties to managed properties and configure property settings by editing the search schema. The content processing component reads the search schema and uses it to carry out the mapping. Only managed properties are included in the search index. Managed properties can be used to create refiners, for example. For more information, see [Overview of the search schema in SharePoint Server](search-schema-overview.md). 
  
### Include or exclude file types
<a name="Section9"> </a>

Content from any file type can be included in the search index. In order for content to be indexed, it must first be crawled by a crawl component and then parsed by a content processing component. A crawl component can crawl a file only if the file extension is included in the list of file name extensions on the Manage File Types page. A content processing component can parse the contents of a crawled file only under the following conditions:
  
- The content processing component has a format handler that can parse the file format.
    
- The content processing component is enabled to parse files that have the file format and file name extension.
    
If the content processing component is unable to parse a file, the search index will only include file properties, such as the file name.
  
By default, SharePoint Server satisfies these requirements for many types of files and it can crawl and parse these file types without your having to install additional format handlers. For an overview of the file types, see [Default crawled file name extensions and parsed file types in SharePoint Server](../technical-reference/default-crawled-file-name-extensions-and-parsed-file-types.md).
  
> [!NOTE]
> You can extend the initial collection of file formats that SharePoint Server can parse by adding third-party filter-based format handlers, known as iFilters. A third party iFilter can override a built-in format handler. 
  
When you plan to include content in the search index from content repositories that have file types that are **not** on the Manage File Types page, review the following: 
  
- To crawl the file type, add the file type to the Manage File Types page.
    
- To parse the file type: 
    
  - If SharePoint Server does not have a format handler for the format, install a third-party filter-based format handler for the file format on each server that hosts a content processing component in the Search service application.
    
  - Enable parsing of the file format and file name extension on each server that hosts a content processing component in the Search service application
    
For more information, see [Add or remove a file type from the search index in SharePoint Server](add-or-remove-a-file-type-from-the-search-index.md).
  
### Plan to use (custom) entity extractors
<a name="Section11"> </a>

You can configure the search system to look for "entities" in unstructured content, such as in the body text or the title of a document. These entities can be words or phrases, such as product names. To specify which entities to look for, you can create and deploy your own dictionaries. 
  
The extracted entities are stored in the search index as separate managed properties, which are automatically configured to be searchable, queryable, retrievable, sortable and refinable. You can use those properties in search refiners, for example, to help users filter their search results. 
  
For companies, you can use the pre-populated company extraction dictionary that SharePoint Server provides.
  
In addition, you can deploy several types of custom entity extractors in the form of custom entity extraction dictionaries. You deploy these dictionaries using Microsoft PowerShell. The entries in these dictionaries (single or multiple words) will be matched on words or parts of words in the content in a case-sensitive or case-insensitive way. For more information, see [Create and deploy custom entity extractors in SharePoint Server](create-and-deploy-custom-entity-extractors.md).
  
****

| **Custom entity extractor / dictionary** |                                                           **Description**                                                            |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| Word Extraction                          | Case-insensitive, maximum 5 dictionaries. For example, the entry "anchor" would match "anchor" and "Anchor", but not "anchorage".    |
| Word Part Extraction                     | Case-insensitive, maximum 5 dictionaries. For example, the entry "anchor" would match "anchor", "Anchor" and within "anchorage".     |
| Word Exact Extraction                    | Case-sensitive, maximum 1 dictionary. For example, the entry "anchor" would match "anchor", but not "Anchor" or "Anchorage".         |
| Word Part Exact Extraction               | Case-sensitive, maximum 1 dictionary. For example, the entry "anchor" would match "anchor" and within "anchorage", but not "Anchor". |
   
## About result sources and federation
<a name="Section12"> </a>

In SharePoint Server, you use a result source to specify the URL of a provider to get search results from, a protocol to use to get those results, and other related settings. For example, the preconfigured default result source is **Local SharePoint Results**.
  
You can add result sources that specify external search providers (such as remote search engines or feeds) from which to get search results. This is called federation.
  
### About federation

When you use federation, users can search for and retrieve content that has not been crawled by servers in the local farm. For example, federation can provide search results from a web-search provider such as Bing, or perhaps from a private data set that you do not have access to crawl.
  
Federation can also be a good solution for a geographically distributed organization that wants to provide search access to content at its various locations when each location has its own search index. Because each location provides search results from its own index, it is not necessary to deploy a centralized search service that builds and accesses a single, unified index. In this context, federation can provide advantages such as the following:
  
- **Low bandwidth requirements** ─ An organization that is geographically dispersed might not have the high network bandwidth that is required to crawl and index large amounts of remote content. When an organization uses federation, the main data that is transmitted for search across the wide-area network is only a set of search results from each federated content repository. 
    
- **Freshness of search results** ─ Each division within an organization can crawl the local content more quickly than a centralized search deployment would be able to crawl all of the content in the entire organization. 
    
- **Divisional search variability** ─ When an organization uses federation, each division within the organization can provide and control its own search environment. Each division can tailor search to its own requirements and preferences, with its own user experience and its own search connectors, for example. A centralized search portal would not allow for such differences. 
    
- **Limited size of search indexes** ─ A large, geographically distributed organization might have millions of documents. It might not be practical for the organization to have a single, unified search index because of the infrastructure that would be required to support such a large index. Federation enables users in each division to perform a single search to find relevant content that is distributed across multiple smaller search indexes in the organization. 
    
### Using result sources for federation

To use federation in SharePoint Server, you select one of the following protocols in the **Protocol** section on the Add/Edit Result Source page: 
  
| **You select this protocol** |          **To get federated search results from this kind of provider**           |
| :--------------------------- | :-------------------------------------------------------------------------------- |
| **Remote SharePoint**        | The index of a search service in another SharePoint Server farm                   |
| **OpenSearch 1.0/1.1**       | An external search engine or feed that uses the OpenSearch protocol, such as Bing |
| **Exchange**                 | Exchange Server 2013                                                              |
   
> [!NOTE]
> On the Add/Edit Result Source page, when you select one of the protocols shown in the preceding table, you must also fill in other related fields on the page to fully specify the result source. 
  
## See also
<a name="Section12"> </a>


[Understanding result sources for search in SharePoint Server](understanding-result-sources-for-search.md)
  
[Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md)
  
[Manage crawling in SharePoint Server](manage-crawling.md)
  
[Default connectors in SharePoint Server](../technical-reference/default-connectors.md)
  
[Default crawled file name extensions and parsed file types in SharePoint Server](../technical-reference/default-crawled-file-name-extensions-and-parsed-file-types.md)
  
[Search connector framework in SharePoint 2013](https://msdn.microsoft.com/library/office/ee556429%28v=office.15%29)

