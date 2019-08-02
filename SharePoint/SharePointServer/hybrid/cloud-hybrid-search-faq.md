---
title: "Cloud hybrid search service (CSSA)-FAQ"
ms.reviewer: mbiswas
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.collection:
localization_priority: Priority
ms.custom: 
description: "Cloud hybrid search service (CSSA)-FAQ"
---

# Cloud hybrid search service (CSSA)-FAQ

Quite frequently, we receive questions regarding Cloud hybrid search service application, Hybrid and its supportability around various use cases. The goal of this post is to collate and have a home for these questions for ease of reference.

***What are the current supported Hybrid features in SharePoint?***

Hybrid is not limited to search/Cloud hybrid search service application (CloudSSA) anymore. Below is a consolidated list of Hybrid features along with Microsoft Official reference to configure the same.

1. [Hybrid OneDrive for Business](https://support.office.com/en-us/article/Plan-hybrid-OneDrive-for-Business-b140bc4c-f54d-4b5a-9409-a3bece4a9cf9?ui=en-US&rs=en-US&ad=US)

2. [Hybrid Sites Features](https://support.office.com/en-us/article/SharePoint-hybrid-sites-and-search-5ff7e56a-7af2-4511-adec-1e043afe244e?ui=en-US&rs=en-US&ad=US)

3. [Hybrid App Launcher](https://support.office.com/en-us/article/The-extensible-hybrid-app-launcher-617a7cb5-53da-4128-961a-64a840c0ab91?ui=en-US&rs=en-US&ad=US)

4. [Hybrid Extranet Business-to-Business sites](https://support.office.com/en-us/article/Use-Office-365-SharePoint-Online-as-a-business-to-business-B2B-extranet-solution-7b087413-165a-4e94-8871-4393e0b9c037?ui=en-US&rs=en-US&ad=US)

5. [Hybrid Auditing](https://support.office.com/en-us/article/SharePoint-Hybrid-Auditing-in-Preview-3a379540-f72b-406f-866a-d6121715ec8c?ui=en-US&rs=en-US&ad=US) (Works only in SharePoint 2016)

6. [Hybrid Taxonomy and Content Types](https://support.office.com/en-us/article/Plan-hybrid-SharePoint-taxonomy-and-hybrid-content-types-71ae4d00-da98-407b-bee2-8d9972e1875c?ui=en-US&rs=en-US&ad=US)

7. [Hybrid self-service site creation](https://support.office.com/en-us/article/Hybrid-self-service-site-creation-f8849a20-7cb7-44e6-bfd6-4c6415ae7785?ui=en-US&rs=en-US&ad=US) (Hybrid self-service site creation is available in SharePoint Server 2013 with the March 2017 PU. November 2017 CU adds this to 2016)

8. [Hybrid Search \[Query federation\]](https://support.office.com/en-us/article/Plan-cloud-hybrid-search-for-SharePoint-33926857-302c-424f-ba78-03286cf5ac30)

9. [Cloud Hybrid search(CloudSSA)](https://support.office.com/en-us/article/Plan-cloud-hybrid-search-for-SharePoint-33926857-302c-424f-ba78-03286cf5ac30)

10. [Business connectivity services](https://technet.microsoft.com/en-us/library/dn197239.aspx)

***Is there an automated wizard that can help configure Hybrid in my environment?***

Yes, you can leverage the Hybrid picker in SharePoint Online admin center for hybrid configurations. This wizard automates certain configuration steps required to connect on-premises SharePoint Server environment with SharePoint Online in Office 365. You can read more about the Hybrid picker [here](https://technet.microsoft.com/en-us/library/mt844711\(v=office.16\).aspx).

***Can I leverage SharePoint Hybrid picker to perform a clean-up of Hybrid environment or deactivate the Hybrid features that was activated by picker?***

The picker automates certain configuration steps to configure Hybrid between On-premises SharePoint Server with SharePoint Online. This is not designed to undo the changes once the wizard completes. Example, Hybrid Picker creates a Server-to-Server (S2S)/OAuth trust between the SharePoint Online and SharePoint On-premises farm. Once this is configured, re-running the wizard does not clean up the trust. You can refer to the official guidance [here](https://technet.microsoft.com/library/mt844711\(v=office.16\).aspx?ui=en-US&rs=en-US&ad=US) that mentions the Server-to-Server trust: "*Note that the hybrid picker does not uninstall features. If you run the hybrid picker and deselect a feature that you previously installed, it will remain installed.*"

***I plan to configure cloud hybrid search with high availability (HA) topologies. Is there a script available to configure the same?***

If you plan to configure cloud hybrid search with HA topologies in either SharePoint 2013/2016, you can configure it with hybrid picker. Hybrid picker has automated certain configuration steps needed to connect your on-premises SharePoint Server environment with SharePoint Online in Office 365 for cloud hybrid search. ([Learn more](https://technet.microsoft.com/en-us/library/dn720906\(v=office.16\).aspx))

***What is hybrid federated search and how is it different from cloud hybrid search?***

Hybrid federated search and Cloud hybrid search are the two Hybrid experiences that a search administrator can choose while configuring hybrid search with Office365.

With hybrid federated search solution for SharePoint, the results are federated from your search index in SharePoint Server 2013/2016 as well as index in Office 365. SharePoint on-premise crawls on-premises content and SharePoint Online crawls SharePoint Online corpus. Post hybrid configurations, when authenticated users submit a query in a search center, a real time query would be fired against both indexes and authorized users will get search results from the Office 365 search index as well as from the SharePoint On-premises 2013/2016 search index. However, the results are separate and distinct from one another often displayed in separate search verticals or result blocks.

Cloud hybrid search service application for SharePoint 2013/2016 is a crawl-based solution. All crawled content, including on-premises content, is processed by Office365 search engine and resides in search index in Office 365. When authenticated users submits a query in SharePoint Online search center, they get search results from Office 365 search index, thus see items both from on-premises and Office 365 content. If you want to get the same experience in on-premises SharePoint 2013/2016 search center, you need to configure a remote result source in the on-premises farm to fetch results from Office365 index.

***What are the supported topologies in Hybrid federated search?***

There are three topology types for Hybrid federated search.

Hybrid infrastructure setup (server to server (S2S) authentication) is a must for any of the below scenarios to work.

**Outbound**: In an outbound scenario, a remote result source will only be configured in the on-premise SharePoint 2013/2016 farm. Outbound can be defined as the ability to only query from the on-premise farm to SharePoint Online search(SPO) farm. Results will be displayed in the on-premise search center in separate search verticals (one for SPO results, another for SharePoint on premise). If outbound is configured, then querying from SharePoint Online (SPO) search center will not return any search results from the on-premises SharePoint 2013/2016 farm.

**Inbound**: In an inbound scenario, a remote result source will only be configured in the SharePoint Online (SPO) search center. Inbound can be defined as the ability to query only from SPO farm to on-premise farm. Results will be displayed in the SPO search center in separate search verticals (one for SPO results, another for SharePoint on premise). There are additional certificate and reverse proxy requirements in addition to the outbound configurations mentioned above. The blog here [outlines](https://blogs.msdn.microsoft.com/spses/2014/01/05/office-365-configure-inbound-hybrid-search-with-directory-synchronization-password-sync-part2/) the requirement.

**Two way**: A combination of the above two (outbound and inbound) is a two way hybrid federated search. Two way is typically the desired state of hybrid federated search deployment in an organization, where result sources are created in both SharePoint Online as well as SharePoint 2013/2016 farm. When queried from either of the search centers, users see a set of search verticals with results from SharePoint Online and another from on-premise SharePoint 2013/2016 farm.

***What are the some of the tested and documented reverse proxies for Hybrid?***

In Hybrid federated search, the reverse proxy must be able to:

- Support client certificate authentication with a wildcard or SAN certificate.

- Support pass-through authentication for OAuth 2.0.

- Accept unsolicited inbound traffic on TCP port 443 (HTTPS).

- Bind a wildcard or SAN SSL certificate to a published endpoint.

- Relay traffic to an on-premises SharePoint Server 2013 or 2016 farm or load balancer without rewriting any packet headers.

As described in [this](https://technet.microsoft.com/en-us/library/dn607304.aspx) article, below is a list of tested reverse proxy solution.

| <span class="underline">Supported reverse proxy devices</span> | <span class="underline">Configuration article</span>                                                                                                                                                |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows Server 2012 R2 with Web Application Proxy (WA-P)       | [Configure Web Application Proxy for a hybrid environment](https://technet.microsoft.com/en-us/library/dn551377.aspx)                                                                               |
| Forefront Threat Management Gateway (TMG) 2010                 | [Configure Forefront TMG for a hybrid environment](https://technet.microsoft.com/en-us/library/dn197170.aspx)                                                                                       |
| F5 BIG-IP                                                      | [Enabling SharePoint 2013 Hybrid Search with the BIG-IP](https://devcentral.f5.com/articles/enabling-sharepoint-2013-hybrid-search-with-the-big-ip)                                                 |
| Citrix NetScaler                                               | [Citrix NetScaler and Microsoft SharePoint 2013 Hybrid Deployment Guide](https://www.citrix.com/content/dam/citrix/en_us/documents/products-solutions/deployment-guide-netscaler-office-365-en.pdf) |

***When should I deploy cloud hybrid search or hybrid federated search?  Are there any recommendations ?***

The recommendation is to choose Cloud hybrid search for these benefits as per [TechNet](https://technet.microsoft.com/library/mt844713\(v=office.16\).aspx?ui=en-US&rs=en-US&ad=US) guidelines.

- Your users get unified search results, search relevance ranking, and refiners even if your organization has a hybrid deployment with content both on-premises and in Office 365.

- Your users automatically get the newest SharePoint Online search experience without your organization having to update your existing SharePoint servers.

- Your users can use cloud capabilities such as Office Delve also for your on-premises content.

- You no longer have to worry about the size of your search index, because your search index is in Office 365. This means that the footprint of your SharePoint Server 2013/2016 search farm is smaller, and your total cost of ownership for search is lower.

- You don't need to upgrade any of your existing installations of SharePoint to have enterprise search in the cloud because SharePoint Server 2013/2016 supports crawling of existing SharePoint Server 2007, SharePoint Server 2010, and SharePoint Server 2013 content farms.

- You no longer have to migrate your search farm to a newer version of SharePoint because this happens automatically in Office 365.

If you have some on-premises content that's highly sensitive and shouldn't be indexed outside your on-premises network, then hybrid federated search may be the way to go. **Note**: Authenticated user queries will be routed in real time to two separate indices (SharePoint Online index and SharePoint on-premise) and results will be displayed in separate search verticals.

***Can Hybrid Search results be displayed in a SharePoint 2010 search center?***

Out of box, there is no way to configure Server to Server authentication in a SharePoint 2010 environment. Cloud hybrid search service application can only be installed in SharePoint 2013/2016 environment. The recommendation is ideally to upgrade the SharePoint 2010 farm to SharePoint 2013 and or SharePoint 2016 following the upgrade guidelines. However, if there is a business requirement to remain on SharePoint 2010, then there is a workaround through which you will be able to display results. You need to publish search service application from SharePoint 2013 and consume from SharePoint 2010 farm. Whichever hybrid search model you deploy (cloud hybrid search service application or federated hybrid search), consuming the same from SharePoint 2010 farm will show authenticated users search results from Office365. **Note**: The search center site in SharePoint 2010 must be Enterprise search center.

***What are supported topologies while publishing/consuming Cloud hybrid search service application?***

Publishing/consuming of Cloud search service application follows the exact same support matrix as any other service application within SharePoint. The following table lists the supported options:

| **Published CloudSSA version** | **Can be consumed by** |
| ------------------------------ | ---------------------- |
| SharePoint Server 2016         | SharePoint Server 2016 |
| SharePoint Server 2016         | SharePoint Server 2013 |
| SharePoint Server 2013         | SharePoint Server 2013 |
| SharePoint Server 2013         | SharePoint Server 2010 |

***What is user rehydration and why does it play a key role in hybrid setup with Office365?***

Server-to-server authentication (S2S) allows servers (ex. SharePoint 2013/2016) to access and request resources from one another on behalf of users. This is a key requirement for Hybrid search to work. For example, in a Cloud hybrid search service farm when a user queries for an item in a SharePoint 2013 search center, the query needs to be routed to SharePoint Online farm (as the index is in SPO farm). The user identity needs to be re-hydrated and then an ACL match has to happen, and only after that a set of results that the user has permission to would be returned in search results. To do so, it's a must that the following tasks can be accomplished:

- Resolve the request to a specific SharePoint user.

- Determine the set of role claims that are associated with the user, a process known as rehydrating the user's identity.

When a request is made to obtain a resource from another server (ex. SharePoint 2013/2016), the claims from the incoming security token is leveraged to resolve it to a specific SharePoint user. By default, SharePoint Server 2013 uses the built-in User Profile service application to resolve the identity. A match of the set of claims is done against some user attributes for locating the corresponding user profile. The match is performed against one of the following attributes:

- Windows Security Identifier (SID)

- Simple Mail Transfer Protocol (SMTP) address

- User principal name (UPN)

- Session Initiation Protocol (SIP) address

Therefore, it's recommended that at least one of these user attributes must be current in user profiles both in SharePoint On-premises as well as in SharePoint Online.

***What is the List of attributes that are synced by the Azure Active Directory Sync tool***

The article [here](https://social.technet.microsoft.com/wiki/contents/articles/19901.dirsync-list-of-attributes-that-are-synced-by-the-azure-active-directory-sync-tool.aspx) has the list of attributes that are synchronized out of the box by the Azure Active Directory Sync tool.

***Search service application in my On premises SharePoint 2013/2016 farm is partitioned. Can I configure hybrid query federation?***

Office 365 doesn't support incoming Hybrid Search queries when the on-premises Search Service Application Proxy is deployed in partitioned mode. Outbound search fails when the Search Service Application or the proxy is partitioned. This is because the search query passes a partitionID (tenantID) to the search query processor, which fails because this is a GUID and therefore unique. The unique partitionID will not be found in the O365 search index and so no search query can be scoped to that ID. Security trimming will not allow results from one ID to be passed to another ID. Search admins need to fix/rebuild their Service Application to be fully supported. This [KB article describes](https://support.microsoft.com/en-in/help/2989740/sharepoint-online-content-isn-t-displayed-in-a-sharepoint-on-premises) the errors and some workarounds.

***What content sources can you crawl using Cloud hybrid search service application?***

All SharePoint 2013/SharePoint 2016 content sources are supported.

***My SharePoint topology consists of multiple SharePoint farms (i.e., Content farm, Service Farm). What is the preferred farm to configure Cloud hybrid search service application?***

In a content/service SharePoint scenario, assuming Search is in the service farm, CloudSSA should ideally be configured in the service farm. For implementation details, refer to this link. <https://technet.microsoft.com/en-us/library/ff621100(v=office.16).aspx>

***Is ADFS/Single-sign-on mandatory to configure server-to-server authentication or Cloud hybrid search service application?***

ADFS/Single-sign is not a mandatory pre-requisite to configure server-to-server authentication or Cloud hybrid search service application. Below is an overview of features that need to be configured between Office 365 and SharePoint Server 2016 /2013 to configure a hybrid environment.

1. Sign up for Office 365.

2. Register your domain with Office 365.

3. Synchronize accounts with Office 365.

4. Assign licenses to your users.

5. Create cloud hybrid search service application.

6. Onboard cloud hybrid search service application.

***Can I connect multiple Cloud hybrid search service applications (CloudSSA) to the same Office365 tenant?***

Companies have SharePoint Farms across different geographical locations. Having CloudSSA across geographical locations and connecting them to the same Office365 tenant is supported. CloudSSA provides the ability to crawl and parse on-premises content, and process and index it in single Office 365 tenant that these CloudSSA farms are connected to.

However, it is important to note that each CloudSSA farm must only crawl unique content (i.e., crawling the same source content from multiple CloudSSA farms connected to the same Office365 tenant **is not supported**).

- **Pro Tip:** The name of the content source in SharePoint on-premises is included in the managed property "ContentSource". If you name the content sources in your different farms uniquely, you can identify the content source by name in queries. If you use the default "Local SharePoint Sites," you will have to find another way to segregate your content.

***Is it supported to run multiple Cloud hybrid search service applications on the same farm? Or is it supported to host a farm that has both regular search service application as well as Cloud hybrid search service application sharing farm hardware?***

Separate farms should be used to host individual Cloud search service applications (CSSA) to avoid resource consumption and possible unexpected behaviors. However, it is a supported configuration to operate two search service applications (SSA) on the same farm if only one of the SSAs is a Cloud hybrid search service application. You also need to ensure that the servers in the farm only host components from one SSA. If the Cloud hybrid search service application and the regular search service application components do not share hardware between any components, only then it's supported that machines in the farm can be used to host both SSAs.

***What are the supported topologies for document collaboration using Exchange Server 2016, Office Online Server (OOS), and SharePoint Server?***

The following are documented and supported topologies:

- [Exchange On-Premises + SharePoint On-Premises](https://blogs.technet.microsoft.com/exchange/2016/11/03/configure-rich-document-collaboration-using-exchange-server-2016-office-online-server-oos-and-sharepoint-server-2016/)

- [Exchange On-Premises + SharePoint Online](https://docs.microsoft.com/en-us/exchange/hybrid-deployment/set-up-document-collaboration)

- Exchange Online + SharePoint Online.

***Can we deploy Cloud hybrid search service application in an environment that has multiple forests?***

Cloud hybrid search service application works in an environment that has multiple forests. You need to ensure that the accounts across these forests are synched to Office365. Azure AD Connect sync should take care of this situation. When you have multiple forests, all forests must be reachable by a single Azure AD Connect sync server. You don't have to join the server to a domain. If necessary, to reach all forests, you can place the server in a perimeter network. The articles below discuss this configuration.

- [Topologies for Azure AD Connect](https://docs.microsoft.com/en-us/azure/active-directory/connect/active-directory-aadconnect-topologies.)

- [Implement-support-for-multiple-forests](https://support.office.com/en-us/article/Implement-support-for-multiple-forests-73c4a525-f6c4-434c-8409-0121a83ab26b)

***When Cloud hybrid search service application crawls On Premises content, do crawled properties from SharePoint on-premises propagate to SharePoint Online?***

Following the crawl of content via Cloud hybrid search service application, crawled properties from SharePoint 2013/2016 on-premises propagate to SharePoint online search schema. The crawled properties in on-premises should be a part of default propset. You also need to ensure that you are looking up the crawl properties in SharePoint Online search schema using the correct account. (By 'correct account', I mean an account in on-premises Active directory having rights in SharePoint On Premises as well synched to Office365 Azure AD in your tenant.) For example, if you can look up using the content access account of your On premises Cloud hybrid search service application farm, you should definitely see the Crawl Properties in SharePoint Online search schema.

***Can Cloud hybrid search service application be onboarded in a farm that has already been configured for provider hosted apps?***

This question primarily revolves around the following use cases:

- You have a SharePoint 2013 or SharePoint 2016 farm where you plan to implement provider-hosted add-ins and/or associate with workflow manager.

- You have a SharePoint 2013 or SharePoint 2016 farm that already has provider-hosted add-ins and/or leverages workflow manager.

Hybrid features/Cloud search service application (CSSA) can be implemented on same SharePoint farm as mentioned above. When you try to establish a S2S trust via the CSSA onboarding script or Hybrid picker, the authentication realm of the on premises Farm is updated to match the Office 365 tenant context id. Within the script, we set it using Set-SPAuthenticationRealm. Once the authentication realm is changed, existing SharePoint Add-ins fail to authenticate; users will get a HTTP 401 when they are redirected to the add-ins. You can read more about the problem as well and fix in our post [here](https://blogs.technet.microsoft.com/beyondsharepoint/2016/09/15/considerations-when-deploying-sharepoint-office365-hybrid-workloads-in-a-farm-utilizing-provider-hosted-add-ins-or-workflow-manager/). **Note**: If you configure Hybrid using Hybrid picker from SharePoint tenant admin, then the wizard takes care of the fix.

***What are the out-of-box Cloud hybrid search service application crawl limits? Also, can I request additional index quota for my tenant?***

The maximum number of on-premises items crawled by Cloud hybrid search service that can be indexed in Office 365 is 20 million. For each 1 TB of storage space a tenant has in Office 365, one can index 1 million items of on-premises content in tenant's search index. Once the limit on how many items can indexed is reached, the on-premises farm hosting Cloud search service application will start seeing errors while crawling new items. Below is a snippet of the error from ULS logs from a SharePoint 2016 farm:

*mssearch.exe (0x5304) 0x97D0 SharePoint Server Search Crawler:Azure Plugin a9sz7 Verbose AzureServiceProxy::SubmitDocuments: submit returned : Forbidden, docid : 4653596 DocIDString : sts4s://*

*SharePoint Server Search Crawler:Azure Plugin ayg2m High AzureServiceProxy::SubmitDocuments: submit failed for the document: HTTP status: Forbidden*

If Cloud search service application is hosted in a SharePoint 2013 environment, the uls tag tracking the error would be *amnz2* and *amoeu*.

You need to request an increase in the available quota to fix the issue. To increase the maximum items that can be indexed beyond 20 million, you need to contact Microsoft Support (see [here](https://support.office.com/en-us/article/Search-limits-for-SharePoint-Online-7C06E9ED-98B6-4304-A900-14773A8FA32F)).

***My Office365 tenant is configured for Hybrid. Can I query for only on-premises items that have been crawled using Cloud hybrid search service application?***

The Hybrid Cloud SSA exposes a new managed property **IsExternalContent**. When crawling on premises content, this property is automatically populated with the value 1. You can leverage the managed property "IsExternalContent" and search for the value 1 for content that is crawled on-premises. The querystring for this example is constructed as follows

http://\<searchcenter url\>/Pages/results.aspx?k=IsExternalContent:1

You can test for the online content only by stipulating NOT IsExternalContent:1 as follows:

http://\<searchcentre url\>/Pages/results.aspx?k=(NOT IsExternalContent:1)

***What would be the People crawl experience if you are crawling On-premise profile store using Cloud hybrid search service application?***

By default, all people in the SharePoint Online SPO User Profile application will be indexed by the SharePoint online search service. If you additionally crawl people using the on-premises cloud search service application, you will generate an additional set of people content items in the Office 365 Search index. Since these would have two different DocID's, both will be returned in search results when queried for a person - one will have url pointing to users mysite in SPO and another pointing to SharePoint On-premises. This will be confusing to end users as searching for a person will return multiple results per person.

There are two ways to approach this problem today:

- Make O365 User Profile service the primary source of user information and let Office 365 Search take care of the indexing and presentation. With this approach, you do not need to crawl people on-premises.

- Crawl the on-premises people profile store in addition to O365 crawling the tenant profile store. This will result in the described scenario of duplicate search results for each person; however, you can use query transformation to decide which results you want to display, even providing the ability for end users to choose between the different result sources at query time.

To utilise the on-premises profile store as the primary people search source, you should follow these steps:

1. Create a new result source or copy the existing people results source.

2. Edit the new result source and modify the Query Transformation box to include the Managed Property IsExternalContent as follows: `{?{searchTerms} ContentClass=urn:content-class:SPSPeople IsExternalcontent:1}`

3. Create a new search results page and configure the Core Search Results web part to consume this new search result source.

4. Complete the implementation by adding the new page to the search navigation settings. This will add the new page as a search vertical within the search center.

To utilise the Office 365 profile store as the primary people search source, you should follow the same steps but using a slightly different query transformation at step two, as follows:

`{?{searchTerms} ContentClass=urn:content-class:SPSPeople NOT IsExternalcontent:1}`

**Note**: The difference in the two transform is the insertion of NOT before the managed property to force the exclusion of External content i.e Non O365 People Results.

***I only see preview of Office documents in search results if the content resides in SharePoint Online. Office documents that reside in SharePoint On-premises do not show previews. Is this expected?***

To enable previews for on-premises content, you need to set up an on-premises Office Web Apps Server and configure SharePoint Server 2013 to use it (or Office Online Server for SharePoint 2016). The guidelines are documented [here](https://technet.microsoft.com/en-us/library/mt668456.aspx). The behavior is a little different with site/webpage previews (aspx). When searching from SharePoint Online, you will see previews of aspx pages for the pages in SharePoint Online farm and not for the aspx pages from SharePoint On-Premises. Currently, the site and web page hover templates check that the result item has the same host name as the current host. This is by design.

***Can Perfmon be leveraged to look at crawl statistics for Cloud hybrid search service application? If yes, what are the Perfmon counters?***

There are Preform counters that have been introduced for Cloud hybrid search service application. To get a list of all counters, you can run the following command in powershell:

`((Get-Counter -ListSet "Search Gatherer Azure Plugin - SharePointServerSearch").counter`

***What is the recommended number of crawl databases for Cloud hybrid search service application?***

Use one crawl database for each 20 million items in the content corpus. You can refer to this [article](https://technet.microsoft.com/en-in/library/dn727118.aspx) for further details.

***I am using Cloud hybrid search service application(CSSA) to crawl content. In my CSSA, I see all 6 components of the search topology. Which ones are hosted locally? For example, is there a local index?***

No\!\! Cloud hybrid search service application is a crawler. The crawl component gets content from your on-premises farm and sends this content to the search index in Office 365. It uses connectors to interact with the content sources and uses the crawl database to store both temporary and historical information about the items it crawls, just like a regular crawl component.

***What is pushed by* *Cloud hybrid search service application to Office365 SPO endpoint during a crawl?***

Cloud hybrid search service application identifies the document that has changed in SharePoint. Crawler picks up the document and parses it, extracting a structured view of the content and removing unnecessary markup. Crawler sends the encrypted content to the Indexing API associated with the SharePoint Online content farm. Encrypted batch submission happens, which consists of ACLs, keywords, metadata, destination tenant info, etc. The following types of operations can be submitted from the crawler:

1. **Insert**: Creates or overwrites a document's content and access control list.

2. **Security update**: Overwrites an existing document's access control list.

3. **Delete**: Deletes all content for a document.

From cloud hybrid search service application farm's ULS logs, you can track the submission of items including the crawled properties. To do so, you need to enable VerboseEx for \[SharePoint Server Search\] "Crawler:Azure Plugin" categories.

***What size Cloud hybrid search service architecture do I need?***

Search architecture for Cloud hybrid search service application consists of search components and databases. Ideally, you need to plan the number of crawl components for your topology, which servers to host the components and databases on, and the hardware required for each server. When you set up a Cloud hybrid search service application, all components of the search service application are set up and need to be online.

The grey components as shown in this [TechNet](https://technet.microsoft.com/library/mt844716\(v=office.16\).aspx?ui=en-US&rs=en-US&ad=US#bkmk_plan_search_architecture) article are inactive in cloud hybrid search, but they still need to be placed on servers as recommended in the article.

| Application Server            | Database Server    |
| ----------------------------- | ------------------ |
| Admin                         | Admin database     |
| Crawl.                        | Crawl database     |
| Content processing component. | Link database      |
| Analytics                     | Analytics database |
| Index                         |                    |
| Query Processing component    |                    |

Deploying additional crawlers will provide high availability for the crawler function. Adding query processors will also provide high availability when the on-premises farm is configured to send search queries to Office 365. Content processing is performed in the Office 365 service, so there is no requirement for additional content processors on-premises. Regardless of the number of items crawled by the Cloud Search Service Application, there is no requirement for additional index components. The index is stored in the Office 365 search farms, which saves a significant amount of on-premises capacity and capital outlay for large corpora. You must scale the on-premises crawl databases to match the number of items crawled because the Cloud Search Service Application must maintain an up-to-date crawl log of the items crawled. Scaling-out employs the same processes as a regular Search Service Application; follow the steps at <https://technet.microsoft.com/library/jj862356(v=office.15).aspx#Topology_ExampleDefaultSmall>. If you need to tune crawling, follow the recommendation in [Redesign enterprise search topology for specific performance requirements in SharePoint 2016](https://technet.microsoft.com/en-us/library/dn727118\(v=office.16\).aspx). The same guidelines apply for Cloud hybrid search service application.

***What are the Highly Available (HA) and Disaster Recovery (DR) recommendations for Cloud hybrid search service application?***

It is recommended that for HA, at least two servers are configured in the same SharePoint on-premises farm and each machine hosts all the search roles. Additional servers can be used, but if at least two of each component are present, the CloudSSA can be considered Highly Available.

For disaster recovery, a second Cloud hybrid search service application can be built in the Disaster Recovery farm. You need to ensure that Cloud hybrid search service application must not crawl the same content as the primary farm unless a failover is initiated. In the event of failover, the Disaster Recovery farm can immediately serve search results from the same Office 365 search index.

***Can users query for items secured with SAML claims if crawled by a Cloud search service application?***

Items secured with SAML claims when crawled using Cloud Search Service application will not show up in search results. This does not work as those identities cannot be interpreted during the ACL mapping process in the Cloud search service application. As of today, we do not have a way to map an on premises SAML identity to an Office 365 user, which is a core requirement for ACL mapping to work. This is by design. For such supportability questions, a request can be submitted at [https://sharepoint.uservoice.com](https://sharepoint.uservoice.com/) for evaluation.

***On premises environment Cloud search service application crawls site collection secured with NT Authority\\Authenticated users. How does this translate to ACL mapping in SharePoint Online?***

The SIDs/SID claims in incoming ACLs are translated in SPO when a cloud hybrid search service application is used to crawl on-premises content. User security identifiers (SID) are mapped to passport unique ID (PUID). Similarly, group SIDs are mapped to Object IDs. NT AUTHORITY\\Authenticated Users and Everyone ([the built-in SIDSs](https://support.microsoft.com/en-in/help/243330/well-known-security-identifiers-in-windows-operating-systems) S-1-5-11 and S-1-1-0) are translated to "Everyone except external users" in SPO (i.e., all users in tenant except the external ones that have been invited to share by email). Cloud search service application only support Windows identity that has been synced to AAD. If customer is not using Windows identity and wants to Crawl using Cloud SSA, a workaround can be to add Everyone claim to the source content to ensure that users are able to search for that Content.

***Result Type Rules are configured at the site collection. Where do I configure Result Type Rules and Display Templates when using Cloud hybrid search?***

The awesome [blog post](http://bit.ly/abHybridResultTypes) from our friend MVP Matthew McDermott highlights what to configure & where. Also, thank you Matt for providing some of your valuable comments for this post.

***Can I view Popularity trend reports in SPO for content crawled with Cloud search service application?***

Popularity trends works based out of analytics. Usage Analytics reporting isn't operational under a Cloud search service application as of today. Usage analysis uses view events created on the farm where the actual content resides. When you configure CloudSSA to crawl content from an on-premises SharePoint farm, the view events are not passed on to the SharePoint Online search farm. The analysis processing happens on SharePoint Online search farm so it will not see the view events and thus will not have the possibility to update the usage reports.

***Cloud hybrid search service application is crawling a SharePoint farm that has http:// prefix in the default zone, extranet zone is https://. Query from SharePoint Online ends up showing http in the search result is this expected behavior?***

Yes, this is expected. Users will see http:// prefix in the search results. As my friend Brian explains it very nicely [here](https://blogs.msdn.microsoft.com/sharepoint_strategery/2013/02/20/beware-crawling-the-non-default-zone-for-a-sharepoint-2013-web-application/) , SharePoint 2013, URL-related managed properties including Path, ParentURL and SPSiteUrl all store values relative to the URL that was crawled. The crawler simply passes what it can gather to the Search Content Services in the cloud. SPO search has no knowledge of the AAMs on your on-prem farm and so is unable to correctly set the mappings you would expect to see. Thus, it's recommended to crawl the Default zone for a SharePoint 2013 Web Application.

***Cloud search service application is crawling my On-Premises content. Can I remove on-premises items from SPO?***

The "urls to remove" option within SharePoint admin center (https://\<tenantname\>-admin.sharepoint.com/\_layouts/15/searchadmin/searchresultremoval.aspx) cannot be leveraged to remove items from SharePoint Online index. If you want to remove specific urls, your option is to use the crawl log in the on-premises Cloud search service application server to remove the same.

***Can I run Cloud hybrid search Onboarding script when multifactor authentication (MFA)is enabled in my tenant?***

Yes, you need to ensure you have the latest version of Azure AD PowerShell. You can download it from [here](http://connect.microsoft.com/site1164/Downloads/DownloadDetails.aspx?DownloadID=59185).

***What are the firewall ports and protocols requirement to configure Cloud hybrid search service application?***

The articles below outline the complete infrastructure firewall requirement for end to end connectivity with Office365. The first blog below talks about Cloud search service application specific ports and protocols.

[Ports and Protocols requirement for the Hybrid Cloud Search Service Application](https://blogs.technet.microsoft.com/beyondsharepoint/2016/08/15/ports-and-protocols-requirement-for-the-hybrid-cloud-search-service-application/)

[Office 365 URLs and IP address ranges](https://support.office.com/en-us/article/Office-365-URLs-and-IP-address-ranges-8548a211-3fe7-47cb-abb1-355ea5aa88a2)

[Hybrid Identity Required Ports and Protocols](https://docs.microsoft.com/en-us/azure/active-directory/connect/active-directory-aadconnect-ports)

***All Outbound requests in my network are filtered or get routed via proxy server. Is there any specific requirement Cloud hybrid search service application to work?***

You need to ensure that account running the search service (msssearch, noderunner accounts) (for crawl and Query federation scenarios to work) in the Cloud Search Service Application farm have unrestricted outbound internet access. If not, set system level proxy settings for these search service accounts. You can follow the steps documented in our post [here](https://blogs.technet.microsoft.com/beyondsharepoint/2017/10/17/cloud-search-service-applications-fails-to-crawl-and-throws-403-forbidden-error/).

Cloud search service application always communicates with endpoints using port 443. Assuming there are multiple SharePoint servers in a farm that hosts Cloud search service application components, all SharePoint servers need to communicate to the following sites

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

The latest version of Windows PowerShell scripts to configure cloud hybrid search for SharePoint can be downloaded [here](https://www.microsoft.com/en-us/download/details.aspx?id=51490&e6b34bbe-475b-1abd-2c51-b5034bcdd6d2=True).

***Is Cloud hybrid search service application onboarding supported for Government community cloud (GCC) & Office 365 operated by 21Vianet.***

Yes, you can refer to our [post](https://blogs.technet.microsoft.com/beyondsharepoint/2017/06/30/announcing-hybrid-search-availability-for-office-365-us-government-communication-and-office-365-operated-by-21vianet/) for details.

***Is it possible to perform an index reset and cleanup just the content that has been crawled via Cloud hybrid search service application?***

Yes, you can follow the steps outlined in this [blog](https://blogs.msdn.microsoft.com/spses/2016/05/18/cloud-search-service-application-removing-items-from-the-office-365-search-index/) article.

***Is there a forum where I can discuss and ask questions regarding issues with Cloud hybrid search?***

Yes, you can submit your questions regarding Cloud search service application at the [TechNet](https://social.technet.microsoft.com/Forums/en-US/home?forum=CloudSSA) forum.

***Hybrid references on TechNet***

Below are some links to Hybrid articles at TechNet

- [Minimum public update levels for SharePoint hybrid features](https://technet.microsoft.com/library/mt844712\(v=office.16\).aspx)

- [SharePoint hybrid sites and search](https://technet.microsoft.com/library/mt844709\(v=office.16\).aspx)

- [Hybrid search in SharePoint](https://technet.microsoft.com/library/mt844713\(v=office.16\).aspx)

- [Learn about cloud hybrid search for SharePoint](https://technet.microsoft.com/library/mt844708\(v=office.16\).aspx)

- [Learn about hybrid federated search for SharePoint](https://technet.microsoft.com/library/mt844710\(v=office.16\).aspx)

- [Hybrid picker in the SharePoint Online admin center](https://technet.microsoft.com/library/mt844711\(v=office.16\).aspx)

- [Plan hybrid SharePoint taxonomy and hybrid content types](https://technet.microsoft.com/library/mt844714\(v=office.16\).aspx)

- [Plan hybrid OneDrive for Business](https://technet.microsoft.com/library/mt844715\(v=office.16\).aspx)

- [Plan cloud hybrid search for SharePoint](https://technet.microsoft.com/library/mt844716\(v=office.16\).aspx)

- [Plan hybrid profiles](https://technet.microsoft.com/library/mt844717\(v=office.16\).aspx)

- [The extensible hybrid app launcher](https://technet.microsoft.com/library/mt844718\(v=office.16\).aspx)

- [Hybrid site following](https://technet.microsoft.com/library/mt844719\(v=office.16\).aspx)

- [Hybrid self-service site creation](https://technet.microsoft.com/library/mt844720\(v=office.16\).aspx)

- [Configure hybrid SharePoint taxonomy and hybrid content types](https://technet.microsoft.com/library/mt844721\(v=office.16\).aspx)

***Are there any eBook available to configure SharePoint Hybrid capabilities?***

Yes , you can download the eBook on Configuring Microsoft SharePoint Hybrid Capabilities (ISBN 9781509302437) from this *[link](https://blogs.msdn.microsoft.com/microsoft_press/2016/07/06/free-ebook-configuring-microsoft-sharepoint-hybrid-capabilities/).*

