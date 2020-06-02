---
title: "Cloud hybrid search service (Cloud SSA) FAQ"
ms.reviewer: mbiswas
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.collection: SPO_Content
localization_priority: Priority
ms.custom: 
description: "Cloud hybrid search service (Cloud SSA) FAQ"
---

# Cloud hybrid search service (Cloud SSA) FAQ

Quite frequently, we receive questions regarding Cloud hybrid search service application, hybrid, and its supportability around various use cases. The goal of this article is to collate and have a home for these questions for ease of reference.

***Is there an automated wizard that can help configure hybrid in my environment?***

Yes, you can leverage the Hybrid picker in SharePoint admin center for hybrid configurations. This wizard automates certain configuration steps required to connect on-premises SharePoint Server environment with SharePoint in Microsoft 365. You can read more about the Hybrid picker [here](https://docs.microsoft.com/SharePoint/hybrid/hybrid-picker-in-the-sharepoint-online-admin-center).

***Can I leverage SharePoint Hybrid picker to perform a clean-up of hybrid environment or deactivate the hybrid features that was activated by picker?***

The Hybrid picker automates certain configuration steps to configure hybrid between on-premises SharePoint Server with SharePoint in Microsoft 365. This is not designed to undo the changes once the wizard completes. The Hybrid picker creates a Server-to-Server (S2S)/OAuth trust between the SharePoint in Microsoft 365 and SharePoint on-premises farm. After this is configured, re-running the wizard does not clean up the trust. You can refer to the documentation at [Hybrid picker in the SharePoint admin center](https://docs.microsoft.com/SharePoint/hybrid/hybrid-picker-in-the-sharepoint-online-admin-center#sharepoint-hybrid-features-offered-in-the-hybrid-picker).

> [!IMPORTANT]
> If the Hybrid picker is run a second time with an enabled feature unchecked, this will not cause the feature to be uninstalled. Any additional selections will be installed and previously installed features will remain.

***I plan to configure Cloud hybrid search with high availability (HA) topologies. Is there a script available to configure the same?***

If you plan to configure Cloud hybrid search with HA topologies in SharePoint Server, you can configure it with Hybrid picker. Hybrid picker has automated certain configuration steps needed to connect your on-premises SharePoint Server environment with SharePoint in Microsoft 365 for Cloud hybrid search. [Learn more](https://docs.microsoft.com/SharePoint/hybrid/configure-cloud-hybrid-searchroadmap).

***What is hybrid federated search and how is it different from Cloud hybrid search?***

Hybrid federated search and Cloud hybrid search are the two hybrid experiences that a search administrator can choose while configuring hybrid search with Microsoft 365.

With hybrid federated search solution for SharePoint, the results are federated from your search index in SharePoint Server as well as index in Microsoft 365. SharePoint on-premises crawls on-premises content and SharePoint in Microsoft 365 crawls SharePoint corpus. Post hybrid configurations, when authenticated users submit a query in a search center, a real time query would be fired against both indexes and authorized users will get search results from the Microsoft 365 search index as well as from the SharePoint Server search index. However, the results are separate and distinct from one another often displayed in separate search verticals or result blocks.

Cloud hybrid search service application for SharePoint Server is a crawl-based solution. All crawled content, including on-premises content, is processed by Microsoft 365 search engine and resides in search index in Office 365. When authenticated users submits a query in SharePoint in Microsoft 365 search center, they get search results from Microsoft 365 search index, thus see items both from on-premises and Microsoft 365 content. If you want to get the same experience in on-premises SharePoint Server search center, you need to configure a remote result source in the on-premises farm to fetch results from Microsoft 365 index.

***What are the supported topologies in hybrid federated search?***

There are three topology types for hybrid federated search.

Hybrid infrastructure setup (server to server (S2S) authentication) is a must for any of the below scenarios to work.

**Outbound**: In an outbound scenario, a remote result source will only be configured in the on-premises SharePoint Server farm. Outbound can be defined as the ability to only query from the on-premises farm to SharePoint in Microsoft 365 search farm. Results appear in the on-premises search center in separate search verticals (one for SharePoint in Microsoft 365 results, another for SharePoint on-premises). If outbound is configured, then querying from SharePoint in Microsoft 365 search center will not return any search results from the on-premises SharePoint Server farm.

**Inbound**: In an inbound scenario, a remote result source will only be configured in the SharePoint in Microsoft 365 search center. Inbound can be defined as the ability to query only from SharePoint in Microsoft 365 farm to on-premises farm. Results will be displayed in the SharePoint in Microsoft 365 search center in separate search verticals (one for SharePoint in Microsoft 365 results, another for SharePoint on-premises). There are additional certificate and reverse proxy requirements in addition to the outbound configurations mentioned above. This is outlined in steps 3 and 5 of the [Configure hybrid federated search from SharePoint in Microsoft 365 to SharePoint Server - roadmap](https://docs.microsoft.com/SharePoint/hybrid/configure-hybrid-federated-search-sharepoint-onlineroadmap) article.

**Two way**: A combination of the above two (outbound and inbound) is a two way hybrid federated search. Two way is typically the desired state of hybrid federated search deployment in an organization, where result sources are created in both SharePoint in Microsoft 365 as well as SharePoint Server farm. When queried from either of the search centers, users see a set of search verticals with results from SharePoint in Microsoft 365 and another from on-premises SharePoint Server farm.

***What are the some of the tested and documented reverse proxies for hybrid?***

In hybrid federated search, the reverse proxy must be able to:

- Support client certificate authentication with a wildcard or SAN certificate.

- Support pass-through authentication for OAuth 2.0.

- Accept unsolicited inbound traffic on TCP port 443 (HTTPS).

- Bind a wildcard or SAN SSL certificate to a published endpoint.

- Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.

[Configure a reverse proxy device for SharePoint Server hybrid](https://docs.microsoft.com/SharePoint/hybrid/configure-a-reverse-proxy-device-for-sharepoint-server-hybrid) article outlines the tested reverse proxy solutions.

***When should I deploy Cloud hybrid search or hybrid federated search?  Are there any recommendations ?***

The recommendation is to choose Cloud hybrid search for the following benefits.

- Your users get unified search results, search relevance ranking, and refiners even if your organization has a hybrid deployment with content both on-premises and in Microsoft 365.

- Your users automatically get the newest SharePoint in Microsoft 365 search experience without your organization having to update your existing SharePoint servers.

- Your users can use cloud capabilities such as Office Delve also for your on-premises content.

- You no longer have to worry about the size of your search index, because your search index is in Office 365. This means that the footprint of your SharePoint Server search farm is smaller, and your total cost of ownership for search is lower.

- You don't need to upgrade any of your existing installations of SharePoint to have enterprise search in the cloud because SharePoint Server supports crawling of existing SharePoint Server 2007 through SharePoint Server 2019 content farms.

- You no longer have to migrate your search farm to a newer version of SharePoint because this happens automatically in Microsoft 365.

If you have some on-premises content that's highly sensitive and shouldn't be indexed outside your on-premises network, then hybrid federated search may be the way to go.

> [!NOTE]
> Authenticated user queries will be routed in real time to two separate indices (SharePoint in Microsoft 365 index and SharePoint on-premises) and results appear in separate search verticals.

***Can hybrid Search results be displayed in a SharePoint 2010 search center?***

Out of box, there is no way to configure Server to Server authentication in a SharePoint 2010 environment. Cloud hybrid search service application can only be installed in SharePoint Server 2013 through SharePoint Server 2019 environment. The recommendation is ideally to upgrade the SharePoint 2010 farm to SharePoint Server 2013 or higher the upgrade guidelines. However, if there is a business requirement to remain on SharePoint 2010, then there is a workaround through which you will be able to display results. You need to publish search service application from SharePoint Server 2013 and consume from SharePoint 2010 farm. Whichever hybrid search model you deploy (Cloud hybrid search service application or federated hybrid search), consuming the same from SharePoint 2010 farm will show authenticated users search results from Microsoft 365.

> [!NOTE]
> The search center site in SharePoint 2010 must be Enterprise search center.

***What are supported topologies while publishing/consuming Cloud hybrid search service application?***

Publishing/consuming of Cloud search service application follows the exact same support matrix as any other service application within SharePoint. The following table lists the supported options:

| **Published CloudSSA version** | **Can be consumed by** |
| ------------------------------ | ---------------------- |
| SharePoint Server 2019         | SharePoint Server 2019 |
| SharePoint Server 2019         | SharePoint Server 2016 |
| SharePoint Server 2016         | SharePoint Server 2016 |
| SharePoint Server 2016         | SharePoint Server 2013 |
| SharePoint Server 2013         | SharePoint Server 2013 |
| SharePoint Server 2013         | SharePoint Server 2010 |

***What is user rehydration and why does it play a key role in hybrid setup with Microsoft 365?***

Server-to-server authentication (S2S) allows servers (for example, SharePoint Server) to access and request resources from one another on behalf of users. This is a key requirement for hybrid search to work. For example, in a Cloud hybrid search service farm when a user queries for an item in a SharePoint Server search center, the query needs to be routed to SharePoint in Microsoft 365 farm (as the index is in SharePoint in Microsoft 365 farm). The user identity needs to be re-hydrated and then an ACL match has to happen, and only after that a set of results that the user has permission to would be returned in search results. To do so, it's a must that the following tasks can be accomplished:

- Resolve the request to a specific SharePoint user.

- Determine the set of role claims that are associated with the user, a process known as rehydrating the user's identity.

When a request is made to obtain a resource from another server (ex. SharePoint Server), the claims from the incoming security token is leveraged to resolve it to a specific SharePoint user. By default, SharePoint Server uses the built-in User Profile service application to resolve the identity. A match of the set of claims is done against some user attributes for locating the corresponding user profile. The match is performed against one of the following attributes:

- Windows Security Identifier (SID)

- Simple Mail Transfer Protocol (SMTP) address

- User principal name (UPN)

- Session Initiation Protocol (SIP) address

Therefore, it's recommended that at least one of these user attributes must be current in user profiles both in SharePoint on-premises as well as in SharePoint in Microsoft 365.

***What is the List of attributes that are synced by the Azure Active Directory Sync tool***

The article [here](https://docs.microsoft.com/azure/active-directory/hybrid/reference-connect-sync-attributes-synchronized) has the list of attributes that are synchronized out of the box by the Azure Active Directory Sync tool.

***Search service application in my on-premises SharePoint Server 2013/2016 farm is partitioned. Can I configure hybrid query federation?***

Microsoft 365 doesn't support incoming hybrid search queries when the on-premises Search Service Application Proxy is deployed in partitioned mode. Outbound search fails when the Search Service Application or the proxy is partitioned. This is because the search query passes a partitionID (tenantID) to the search query processor, which fails because this is a GUID and therefore unique. The unique partitionID will not be found in the Microsoft 365 search index and so no search query can be scoped to that ID. Security trimming will not allow results from one ID to be passed to another ID. Search admins need to fix/rebuild their Service Application to be fully supported. This [hybrid deployment troubleshooting article](https://docs.microsoft.com/sharepoint/support/search/online-content-not-displayed-in-on-premises-search) describes the errors and some workarounds.

***What content sources can you crawl using Cloud hybrid search service application?***

All SharePoint Server content sources are supported.

***My SharePoint topology consists of multiple SharePoint farms (i.e., Content farm, Service Farm). What is the preferred farm to configure Cloud hybrid search service application?***

In a content/service SharePoint scenario, assuming Search is in the service farm, Cloud SSA should ideally be configured in the service farm. For implementation details, refer to the [Share service applications across farms in SharePoint Server](https://docs.microsoft.com/sharepoint/administration/share-service-applications-across-farms) article.

***Is single sign-on mandatory to configure server-to-server authentication or Cloud hybrid search service application?***

Single sign-on is not a mandatory pre-requisite to configure server-to-server authentication or Cloud hybrid search service application. Below is an overview of features that need to be configured between Microsoft 365 and SharePoint Server to configure a hybrid environment.

1. Sign up for Microsoft 365.

2. Register your domain with Microsoft 365.

3. Synchronize accounts with Microsoft 365.

4. Assign licenses to your users.

5. Create Cloud hybrid search service application.

6. Onboard cloud hybrid search service application.

***Can I connect multiple Cloud hybrid search service applications to the same Microsoft 365 organization?***

Companies have SharePoint Farms across different geographical locations. Having Cloud SSA across geographical locations and connecting them to the same Microsoft 365 organization is supported. Cloud SSA provides the ability to crawl and parse on-premises content, and process and index it in single Microsoft 365 organization that these Cloud SSA farms are connected to.

It is important to note that each Cloud SSA farm must only crawl unique content (for example, crawling the same source content from multiple Cloud SSA farms connected to the same Microsoft 365 organization **is not supported**).

> [!TIP]
> The name of the content source in SharePoint on-premises is included in the managed property "ContentSource". If you name the content sources in your different farms uniquely, you can identify the content source by name in queries. If you use the default "Local SharePoint Sites" you will have to find another way to segregate your content.

***Is it supported to run multiple Cloud hybrid search service applications on the same farm? Or is it supported to host a farm that has both regular search service application as well as Cloud hybrid search service application sharing farm hardware?***

Separate farms should be used to host individual Cloud search service applications to avoid resource consumption and possible unexpected behaviors. However, it is a supported configuration to operate two search service applications (SSA) on the same farm if only one of the SSAs is a Cloud hybrid search service application. You also need to ensure that the servers in the farm only host components from one SSA. If the Cloud hybrid search service application and the regular search service application components do not share hardware between any components, only then it's supported that machines in the farm can be used to host both SSAs.

***What are the supported topologies for document collaboration using Exchange Server 2016, Office Online Server (OOS), and SharePoint Server?***

The following are documented and supported topologies:

- [Configure rich document collaboration using Exchange Server 2016, Office Online Server (OOS) and SharePoint Server](https://techcommunity.microsoft.com/t5/Exchange-Team-Blog/Configure-rich-document-collaboration-using-Exchange-Server-2016/ba-p/606021)

- [Configure document collaboration with OneDrive and Exchange 2016 on-premises](https://docs.microsoft.com/exchange/hybrid-deployment/set-up-document-collaboration)

- Exchange Online + SharePoint in Microsoft 365.

***Can we deploy Cloud hybrid search service application in an environment that has multiple forests?***

Cloud hybrid search service application works in an environment that has multiple forests. You need to ensure that the accounts across these forests are synched to Microsoft 365. Azure AD Connect sync should take care of this situation. When you have multiple forests, all forests must be reachable by a single Azure AD Connect sync server. You don't have to join the server to a domain. If necessary, to reach all forests, you can place the server in a perimeter network. The articles below discuss this configuration.

- [Topologies for Azure AD Connect](https://docs.microsoft.com/azure/active-directory/hybrid/plan-connect-topologies)

- [Implement-support-for-multiple-forests](https://support.office.com/article/73c4a525-f6c4-434c-8409-0121a83ab26b)

***When Cloud hybrid search service application crawls on-premises content, do crawled properties from SharePoint on-premises propagate to SharePoint in Microsoft 365?***

Following the crawl of content via Cloud hybrid search service application, crawled properties from SharePoint Server on-premises propagate to SharePoint in Microsoft 365 search schema. The crawled properties in on-premises should be a part of default property set. You also need to ensure that you are looking up the crawl properties in SharePoint in Microsoft 365 search schema using an account synchronized to from Active Directory to Azure AD and one which has rights to the crawled content. For example, if you can look up using the content access account of your on-premises Cloud hybrid search service application farm, you should see the Crawl Properties in SharePoint in Microsoft 365 search schema.

***Can Cloud hybrid search service application be onboarded in a farm that has already been configured for provider hosted apps?***

This question primarily revolves around the following use cases:

- You have a SharePoint Server farm where you plan to implement provider-hosted add-ins and/or associate with workflow manager.

- You have a SharePoint Server farm that already has provider-hosted add-ins and/or leverages workflow manager.

Hybrid features/Cloud search service application can be implemented on same SharePoint farm as mentioned above. When you try to establish a S2S trust via the Cloud SSA onboarding script or Hybrid picker, the authentication realm of the on-premises Farm is updated to match the Microsoft 365 organization context id. Within the script, we set it using [Set-SPAuthenticationRealm](https://docs.microsoft.com/powershell/module/sharepoint-server/set-spauthenticationrealm). Once the authentication realm is changed, existing SharePoint Add-ins fail to authenticate; users will get a HTTP 401 when they are redirected to the add-ins. You can read more about the problem as well and fix in the article [Provider-hosted add-ins stop working and HTTP 401 error after you configure SharePoint farm hybrid features](https://docs.microsoft.com/sharepoint/support/administration/provider-hosted-add-ins-stop-working-and-http-401-error-after-configure-farm-hybrid-features).

> [!NOTE]
> If you configure hybrid using Hybrid picker from the classic SharePoint admin center, then the wizard takes care of the fix.

***What are the out-of-box Cloud hybrid search service application crawl limits? Also, can I request additional index quota for my tenant?***

The maximum number of on-premises items crawled by Cloud hybrid search service that can be indexed in Microsoft 365 is 20 million. For each 1 TB of storage space an organization has in Microsoft 365, one can index 1 million items of on-premises content in tenant's search index. Once the limit on how many items can indexed is reached, the on-premises farm hosting Cloud search service application will start seeing errors while crawling new items. Below is a snippet of the error from ULS logs from a SharePoint 2016 farm:

```
mssearch.exe (0x5304) 0x97D0 SharePoint Server Search Crawler:Azure Plugin a9sz7 Verbose AzureServiceProxy::SubmitDocuments: submit returned : Forbidden, docid : 4653596 DocIDString : sts4s://
SharePoint Server Search Crawler:Azure Plugin ayg2m High AzureServiceProxy::SubmitDocuments: submit failed for the document: HTTP status: Forbidden
```

If Cloud search service application is hosted in a SharePoint Server 2013 environment, the uls tag tracking the error would be `amnz2` and `amoeu`.

You need to request an increase in the available quota to fix the issue. To increase the maximum items that can be indexed beyond 20 million, you need to contact Microsoft Support via the [Microsoft 365 Admin center](https://docs.microsoft.com/office365/admin/contact-support-for-business-products?view=o365-worldwide&tabs=online).

***My Microsoft 365 organization is configured for hybrid. Can I query for only on-premises items that have been crawled using Cloud hybrid search service application?***

The hybrid Cloud SSA exposes a new managed property **IsExternalContent**. When crawling on-premises content, this property is automatically populated with the value 1. You can leverage the managed property `IsExternalContent` and search for the value 1 for content that is crawled on-premises. The querystring for this example is constructed as follows

`http://<searchcenter url>/Pages/results.aspx?k=IsExternalContent:1`

You can test for the online content only by stipulating NOT IsExternalContent:1 as follows:

`http://<searchcenter url>/Pages/results.aspx?k=(NOT IsExternalContent:1)`

***What would be the People crawl experience if you are crawling on-premises profile store using Cloud hybrid search service application?***

By default, all people in the SharePoint in Microsoft 365 User Profile application will be indexed by the SharePoint in Microsoft 365 search service. If you additionally crawl people using the on-premises cloud search service application, you will generate an additional set of people content items in the Microsoft 365 Search index. Since these would have two different DocID's, both will be returned in search results when queried for a person - one will have url pointing to users OneDrive site in SharePoint in Microsoft 365 and another pointing to SharePoint on-premises. This will be confusing to end users as searching for a person will return multiple results per person.

There are two ways to approach this problem today:

- Make the Microsoft 365 User Profile service the primary source of user info, and let Microsoft 365 Search take care of the indexing and presentation. With this approach, you do not need to crawl people on-premises.

- Crawl the on-premises people profile store in addition to Microsoft 365 crawling the tenant profile store. This will result in the described scenario of duplicate search results for each person; however, you can use query transformation to decide which results you want to display, even providing the ability for end users to choose between the different result sources at query time.

To utilize the on-premises profile store as the primary people search source, follow these steps:

1. Create a new result source or copy the existing people results source.

2. Edit the new result source, and modify the Query Transformation box to include the Managed Property IsExternalContent, as follows: `{?{searchTerms} ContentClass=urn:content-class:SPSPeople IsExternalcontent:1}`

3. Create a new search results page and configure the Core Search Results web part to consume this new search result source.

4. Complete the implementation by adding the new page to the search navigation settings. This adds the new page as a search vertical within the search center.

To utilize the Microsoft 365 profile store as the primary people search source, follow the same steps but using a slightly different query transformation at step two, as follows:

`{?{searchTerms} ContentClass=urn:content-class:SPSPeople NOT IsExternalcontent:1}`

> [!NOTE]
> The difference in the two transform is the insertion of NOT before the managed property to force the exclusion of External content, (for example, non-Microsoft 365 People Results).

***I only see preview of Office documents in search results if the content resides in SharePoint in Microsoft 365. Office documents that reside in SharePoint on-premises do not show previews. Is this expected?***

To enable previews for on-premises content, you need to set up an on-premises Office Web Apps Server (SharePoint Server 2013 only) or Office Online Server (SharePoint Server 2013 and higher) and configure SharePoint Server to use it. The guidelines are documented [here](https://docs.microsoft.com/SharePoint/hybrid/enable-previews-of-on-premises-search-results-in-cloud-hybrid-search). The behavior is a little different with site/webpage previews (aspx). When searching from SharePoint in Microsoft 365, previews appear of aspx pages for the pages in SharePoint in Microsoft 365 farm and not for the aspx pages from SharePoint Server. Currently, the site and web page hover templates check that the result item has the same host name as the current host. This is by design.

***Can Perfmon be leveraged to look at crawl statistics for Cloud hybrid search service application? If yes, what are the Perfmon counters?***

There are perfmon counters that have been introduced for Cloud hybrid search service application. To get a list of all counters, in PowerShell, run the following command:

`((Get-Counter -ListSet "Search Gatherer Azure Plugin - SharePointServerSearch").counter`

***What is the recommended number of crawl databases for Cloud hybrid search service application?***

Use one crawl database for each 20 million items in the content corpus. For more info, see this [article](https://docs.microsoft.com/SharePoint/search/redesign-for-specific-performance-requirements?redirectedfrom=MSDN#how-to-handle-more-items-in-the-index).

***I am using Cloud hybrid search service application to crawl content. In my Cloud SSA, I see all 6 components of the search topology. Which ones are hosted locally? For example, is there a local index?***

No. The Cloud hybrid search service application is a crawler. The crawl component gets content from your on-premises farm and sends this content to the search index in Office 365. It uses connectors to interact with the content sources and uses the crawl database to store both temporary and historical information about the items it crawls, just like a regular crawl component.

***What is pushed by Cloud hybrid search service application to SharePoint in Microsoft 365 endpoint during a crawl?***

Cloud hybrid search service application identifies the document that has changed in SharePoint. Crawler picks up the document and parses it, extracting a structured view of the content and removing unnecessary markup. Crawler sends the encrypted content to the Indexing API associated with the SharePoint in Microsoft 365 content farm. Encrypted batch submission happens, which consists of ACLs, keywords, metadata, destination tenant info, etc. The following types of operations can be submitted from the crawler:

1. **Insert**: Creates or overwrites a document's content and access control list.

2. **Security update**: Overwrites an existing document's access control list.

3. **Delete**: Deletes all content for a document.

From Cloud hybrid search service application farm's ULS logs, you can track the submission of items including the crawled properties. To do so, you need to enable VerboseEx for \[SharePoint Server Search\] "Crawler:Azure Plugin" categories.

***What size Cloud hybrid search service architecture do I need?***

Search architecture for Cloud hybrid search service application consists of search components and databases. Ideally, you need to plan the number of crawl components for your topology, which servers to host the components and databases on, and the hardware required for each server. When you set up a Cloud hybrid search service application, all components of the search service application are set up and need to be online.

The grey components as shown in this [TechNet](https://docs.microsoft.com/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint?redirectedfrom=MSDN#step-2-what-size-cloud-search-architecture-do-i-need) article are inactive in Cloud hybrid search, but they still need to be placed on servers as recommended in the article.

| Application Server            | Database Server    |
| ----------------------------- | ------------------ |
| Admin                         | Admin database     |
| Crawl.                        | Crawl database     |
| Content processing component. | Link database      |
| Analytics                     | Analytics database |
| Index                         |                    |
| Query Processing component    |                    |

Deploying additional crawlers will provide high availability for the crawler function. Adding query processors will also provide high availability when the on-premises farm is configured to send search queries to Microsoft 365. Content processing is performed in the Microsoft 365 service, so there is no requirement for additional content processors on-premises. Regardless of the number of items crawled by the Cloud Search Service Application, there is no requirement for additional index components. The index is stored in the Microsoft 365 search farms, which saves a significant amount of on-premises capacity and capital outlay for large corpora. You must scale the on-premises crawl databases to match the number of items crawled because the Cloud Search Service Application must maintain an up-to-date crawl log of the items crawled. Scaling-out employs the same processes as a regular Search Service Application; follow the steps at [Change the default search topology in SharePoint Server](https://docs.microsoft.com/SharePoint/search/change-the-default-search-topology#Topology_ExampleDefaultSmall). If you need to tune crawling, follow the recommendation in [Redesign enterprise search topology for specific performance requirements in SharePoint 2016](https://docs.microsoft.com/SharePoint/search/redesign-for-specific-performance-requirements). The same guidelines apply for Cloud hybrid search service application.

***What are the Highly Available (HA) and Disaster Recovery (DR) recommendations for Cloud hybrid search service application?***

We recommend that for HA, at least two servers are configured in the same SharePoint on-premises farm and each machine hosts all the search roles. Additional servers can be used, but if at least two of each component are present, the Cloud SSA can be considered Highly Available.

For disaster recovery, a second Cloud hybrid search service application can be built in the Disaster Recovery farm. Ensure that Cloud hybrid search service application must not crawl the same content as the primary farm unless a failover is initiated. In the event of failover, the Disaster Recovery farm can immediately serve search results from the same Microsoft 365 search index.

***Can users query for items secured with SAML claims if crawled by a Cloud search service application?***

Items secured with SAML claims when crawled using Cloud Search Service application will not show up in search results. This does not work as those identities cannot be interpreted during the ACL mapping process in the Cloud search service application. As of today, we do not have a way to map an on-premises SAML identity to a Microsoft 365 user, which is a core requirement for ACL mapping to work. This is by design. For such supportability questions, a request can be submitted at [SharePoint UserVoice](https://sharepoint.uservoice.com/) for evaluation.

***On-premises environment Cloud search service application crawls site collection secured with NT Authority\\Authenticated users. How does this translate to ACL mapping in SharePoint in Microsoft 365?***

The SIDs/SID claims in incoming ACLs are translated in SharePoint when a Cloud hybrid search service application is used to crawl on-premises content. User security identifiers (SID) are mapped to passport unique ID (PUID). Similarly, group SIDs are mapped to Object IDs. NT AUTHORITY\\Authenticated Users and Everyone ([the built-in SIDSs](https://support.microsoft.com/help/243330/) S-1-5-11 and S-1-1-0) are translated to "Everyone except external users" in SharePoint in Microsoft 365 (for example, all users in tenant except the external ones that have been invited to share by email). Cloud search service application only support Windows identity that has been synced to Azure AD. If customer is not using Windows identity and wants to Crawl using Cloud SSA, a workaround can be to add Everyone claim to the source content to ensure that users are able to search for that Content.

***Result Type Rules are configured at the site collection. Where do I configure Result Type Rules and Display Templates when using Cloud hybrid search?***

The awesome [blog post](http://bit.ly/abHybridResultTypes) from our friend MVP Matthew McDermott highlights what to configure & where. Also, thank you Matt for providing some of your valuable comments for this article.

***Can I view Popularity trend reports in SharePoint in Microsoft 365 for content crawled with Cloud search service application?***

Popularity trends works based out of analytics. Usage Analytics reporting isn't operational under a Cloud search service application as of today. Usage analysis uses view events created on the farm where the actual content resides. When you configure Cloud SSA to crawl content from an on-premises SharePoint farm, the view events are not passed on to the SharePoint in Microsoft 365 search farm. The analysis processing happens on SharePoint in Microsoft 365 search farm so it will not see the view events and thus will not have the possibility to update the usage reports. This also means that the number of views shown on a document hover panel will no longer appear.

***Cloud hybrid search service application is crawling a SharePoint farm that has http:// prefix in the default zone, extranet zone is https://. Query from SharePoint in Microsoft 365 ends up showing http in the search result is this expected behavior?***

Yes, this is expected. Users will see http:// prefix in the search results. As my friend Brian explains it very nicely [here](https://blogs.msdn.microsoft.com/sharepoint_strategery/2013/02/20/beware-crawling-the-non-default-zone-for-a-sharepoint-2013-web-application/), SharePoint Server URL-related managed properties including Path, ParentURL and SPSiteUrl all store values relative to the URL that was crawled. The crawler simply passes what it can gather to the Search Content Services in the cloud. SharePoint in Microsoft 365 search has no knowledge of the Alternate Access Mappings on your on-premises farm and so is unable to correctly set the mappings you would expect to see. Thus, it's recommended to crawl the Default zone for a SharePoint Server Web Application.

***Cloud search service application is crawling my on-premises content. Can I remove on-premises items from SharePoint in Microsoft 365?***

The "URLs to remove" option within SharePoint admin center (https://\<tenantname\>-admin.sharepoint.com/\_layouts/15/searchadmin/searchresultremoval.aspx) cannot be leveraged to remove items from SharePoint in Microsoft 365 index. If you want to remove specific URLs, your option is to use the crawl log in the on-premises Cloud search service application server to remove the same.

***Can I run Cloud hybrid search Onboarding script when multifactor authentication (MFA)is enabled in my tenant?***

Yes, you need to ensure you have the latest version of Azure AD PowerShell. You can download it from [here](https://docs.microsoft.com/powershell/azure/active-directory/install-adv2).

***What are the firewall ports and protocols requirement to configure Cloud hybrid search service application?***

The following articles outline the complete infrastructure firewall requirement for end-to-end connectivity with Microsoft 365. The first blog below talks about Cloud search service application specific ports and protocols.

[Ports and Protocols requirement for the Hybrid Cloud Search Service Application](https://blogs.technet.microsoft.com/beyondsharepoint/2016/08/15/ports-and-protocols-requirement-for-the-hybrid-cloud-search-service-application/)

[Microsoft 365 URLs and IP address ranges](https://docs.microsoft.com/office365/enterprise/urls-and-ip-address-ranges)

[Hybrid Identity Required Ports and Protocols](https://docs.microsoft.com/azure/active-directory/hybrid/reference-connect-ports)

***All Outbound requests in my network are filtered or get routed via proxy server. Is there any specific requirement Cloud hybrid search service application to work?***

You need to ensure that account running the search service (msssearch, noderunner accounts) (for crawl and Query federation scenarios to work) in the Cloud Search Service Application farm have unrestricted outbound internet access. If not, set system level proxy settings for these search service accounts. You can follow the steps documented in our post [here](https://blogs.technet.microsoft.com/beyondsharepoint/2017/10/17/cloud-search-service-applications-fails-to-crawl-and-throws-403-forbidden-error/).

Cloud search service application always communicates with endpoints using port 443. Assuming there are multiple SharePoint servers in a farm that hosts Cloud search service application components, all SharePoint servers need to communicate to the following sites.

1. \*.sharepoint.com

2. [https://accounts.accesscontrol.windows.net](https://accounts.accesscontrol.windows.net/)

3. <https://login.windows.net/common/oauth2/authorize>

4. <https://sts.windows.net/*>

5. [https://login.microsoftonline.com](https://login.microsoftonline.com/)

If there are dedicated Search servers in the farm topology they should be able to communicate to the following sites as well.

1. https://provisioningapi.microsoftonline.com

2. \*.search.production.us.trafficmanager.net

3. \*.search.production.emea.trafficmanager.net

4. \*.search.production.apac.trafficmanager.net

***Where can I download Cloud hybrid search service application onboarding script?***

The latest version of Windows PowerShell scripts to configure Cloud hybrid search for SharePoint can be downloaded [here](https://www.microsoft.com/download/details.aspx?id=51490&e6b34bbe-475b-1abd-2c51-b5034bcdd6d2=True).

***Is Cloud hybrid search service application onboarding supported for Government community cloud (GCC) & Office 365 operated by 21Vianet.***

Yes, you can refer to our [post](https://blogs.technet.microsoft.com/beyondsharepoint/2017/06/30/announcing-hybrid-search-availability-for-office-365-us-government-communication-and-office-365-operated-by-21vianet/) for details.

***Is it possible to perform an index reset and cleanup just the content that has been crawled via Cloud hybrid search service application?***

Yes, you can follow the steps outlined in this [blog](https://blogs.msdn.microsoft.com/spses/2016/05/18/cloud-search-service-application-removing-items-from-the-office-365-search-index/) article.

***Is there a forum where I can discuss and ask questions regarding issues with Cloud hybrid search?***

Yes, you can submit your questions regarding Cloud search service application at the [TechNet](https://social.technet.microsoft.com/Forums/en-US/home?forum=CloudSSA) forum.

***Are there any eBook available to configure SharePoint hybrid capabilities?***

Yes, you can download the eBook [Configuring Microsoft SharePoint hybrid Capabilities (ISBN 9781509302437)](https://blogs.msdn.microsoft.com/microsoft_press/2016/07/06/free-ebook-configuring-microsoft-sharepoint-hybrid-capabilities/).
