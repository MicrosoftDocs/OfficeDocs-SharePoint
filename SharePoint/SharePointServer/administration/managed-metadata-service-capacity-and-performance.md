---
title: "Estimate capacity and performance for Managed Metadata Service (SharePoint Server 2013)"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 8/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: fe802699-9c9e-4389-a674-720769b72aaa
description: "Learn how to plan to deploy a Managed Metadata Service application for SharePoint Server 2013 by using tested capacity and performance data."
---

# Estimate capacity and performance for Managed Metadata Service (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
This article contains information and recommendations that are related to sizing and performance optimization of the Managed Metadata Service in SharePoint Server 2013. We also provide some best practices about how to configure the service and structure the service application databases for maximum performance. Use this information to determine whether your planned deployment fits in the capacity and performance limits that our tests provide.
  
The following new features in SharePoint Server 2013 directly affect the Managed Metadata Service and are important for capacity planning. The load from these features is included in our test dataset and test scenarios.
  
- Hashtags in feeds (in My Sites or Team Sites)
    
- Sites using managed navigation
    
- New CSOM endpoints that clients can call
    
For a typical SharePoint Server 2013 deployment with similar characteristics as our test dataset, we recommend that the Managed Metadata Service application run on the computers that assume the front-end web server role. The database for the Managed Metadata Service application can be placed on a SQL Server instance that hosts other SharePoint service application databases.
  
For deployments that contain significantly more items than compared to the dataset we provide in our tests, we'll attempt to provide guidance through the results of tests where we change one of the variables and keep the other components of our test dataset constant. Users with larger deployments should consider these results and size their SharePoint Server 2013 farms accordingly.
  
    
For general information about capacity management and how to plan for SharePoint Server 2013, see [Capacity management and sizing for SharePoint Server 2013](capacity-management-and-sizing-for-sharepoint-server-2013.md).
  
## Introduction
<a name="intro"> </a>

We recommend that in a typical SharePoint Server 2013 deployment with similar characteristics as our test dataset, that the Managed Metadata Service application be enabled only on computers that run as a front-end web server. The database for the Managed Metadata Service application can be put on a SQL Server instance that hosts other SharePoint service application databases.
  
Note that for deployments that contain significantly more items than are in the dataset that we provide in our tests, we provide separate recommendations. In our tests we attempt to provide guidance using the test results where we change one of the variables and keep the other components constant. Users with larger deployments should consider these results and size their SharePoint farms accordingly.
  
## Test dataset
<a name="Tdata"> </a>

To provide capacity planning guidance, we created a test dataset that includes the features in SharePoint Server 2010 and new features in SharePoint Server 2013 and ran tests on a SharePoint deployment. The following table shows the test dataset that we used:
  
|**Variable**|**Number of items**|
|:-----|:-----|
|**Term set groups** <br/> |500  <br/> |
|**Term sets** <br/> |1,000 (2 per group)  <br/> |
|**Managed terms (does not include enterprise keywords)** <br/> |20,000 (20 per term set)  <br/> |
|**Enterprise keywords** <br/> |80,000  <br/> |
|**Hashtags** <br/> |200,000  <br/> |
|**Total terms (includes managed terms, enterprise keywords, and hashtags)** <br/> |300,000  <br/> |
|**Labels** <br/> |300,000 (1 per item)  <br/> |
|**Term label length** <br/> |30 characters per label  <br/> |
   
## Test scenarios
<a name="TS"> </a>

We used the tests in the following table for this dataset:
  
|**Test**|**Description**|**Percentage in test**|
|:-----|:-----|:-----|
|**GetSuggestions** <br/> |A single call to the web service and a single character prefix string. The string will be chosen to match 20% of the terms in the term store, similar to how metadata column suggestions work in the SharePoint user interface.  <br/> |10%  <br/> |
|**GetMatches** <br/> |Web service for a string that matches 1% of the terms in the term store.  <br/> |5%  <br/> |
|**ValidateTerms** <br/> |Web service call to validate a single term.  <br/> |5%  <br/> |
|**CreateTaxonomyItem** <br/> |Web service call to a call to create a keyword with a random name.  <br/> |5%  <br/> |
|**GetChildTermsInTermSetWithPaging** <br/> |Web service call to multiple term sets. Similar to the call made by SharePoint Server 2013 to retrieve terms sets used by the managed navigation feature, the results of which are then cached in the front-end web server.  <br/> |5%  <br/> |
|**GetTermSets** <br/> |Web service call to get term sets.  <br/> |5%  <br/> |
|**GetTermsByLabel** <br/> |Web service call with a list of term GUIDs. Similar to the call made by SharePoint Server 2013 when a My Site home page is loaded.  <br/> |10%  <br/> |
|**HT GetSuggestions** <br/> |Web service call to get suggestions for hashtags with a single character. Similar to the call made by SharePoint UI when you work with hashtags in the feeds.  <br/> |10%  <br/> |
|**HT NewHashTag** <br/> |2 web service calls. One to get terms, then another to create the term.  <br/> |5%  <br/> |
|**HT GetTermsByLabel** <br/> |Web service call to get existing terms. Used when a hashtag is used in a feed post.  <br/> |15%  <br/> |
|**HT AddAssociation** <br/> |Web service call to add an association to an existing hashtag term.  <br/> |5%  <br/> |
|**CSOM GetTerms** <br/> |Test to GetTerms a list of terms GUIDs. Has 2 individual CSOM calls.  <br/> |10%  <br/> |
|**CSOM SetProperty** <br/> |Test to SetProperty for a single term. Has 4 individual CSOM calls.  <br/> |5%  <br/> |
|**CSOM CreateTerm** <br/> |Test to add a term to the term store. Has 4 individual CSOM calls.  <br/> |5%  <br/> |
   
In our tests we put more weight on operations that are expected to be used more frequently.
  
## Test topology
<a name="TTop"> </a>

We ran the tests in our lab environment that has the topology shown in the following diagram:
  
**Figure 1: Test lab server topology**

![Visio diagram showing the test server topology that included a single computer hosting SQL Server and a single computer hosting SharePoint server running as either an application server or front-end web server.](../media/ECMCapacityEMMTopol.gif)
  
We started our tests with one computer that is running the Managed Metadata Service application and serving as the front-end web server. Later, we added another computer that has the same configuration.
  
## Test results
<a name="TR"> </a>

We used the dataset and the scenarios that were described in earlier sections to test the total number of Managed Metadata Service application operations that executed for a given configuration.
  
We ran our tests with the different load profiles in the following list:
  
- **Green Zone**
    
    Servers are under 60% utilization. This should be the target for most of the time when the servers are running.
    
- **Red Zone**
    
    Servers are close to full utilization. This can be considered a state where the SharePoint site is under more load than usual. In the Red Zone, server response time values start increasing as the server tries to meet the demand of incoming requests.
    
The following table shows the results of our measurements with a single computer:
  
||**Green Zone**|**Red Zone**|
|:-----|:-----|:-----|
|**Server Response Time 50th percentile for read operations:** <br/> |32 ms.  <br/> |44 ms.  <br/> |
|**Server Response Time 95th percentile for read operations:** <br/> |1090 ms.  <br/> |1335 ms.  <br/> |
|**Server Response Time 50th percentile for write operations:** <br/> |1837 ms.  <br/> |2038 ms.  <br/> |
|**Server Response Time 95th percentile for write operations:** <br/> |2283 ms.  <br/> |3515 ms.  <br/> |
|**Tests completed per second:** <br/> |9  <br/> |15  <br/> |
|**Average CPU (application server or front-end web server)** <br/> |56%  <br/> |92%  <br/> |
|**Average CPU (SQL Server)** <br/> |7%  <br/> |12%  <br/> |
|**Peak memory usage (application Server or front-end web server)** <br/> |6 GB  <br/> |6.2 GB  <br/> |
   
We then added a second application server or front-end web server virtual machines (VMs) to the deployment with the same configuration. The following table shows the results for a two VM farm with approximately two times (2x) the load as our earlier tests:
  
||**Green Zone**|**Red Zone**|
|:-----|:-----|:-----|
|**Server Response Time 50th percentile for read operations:** <br/> |44 ms.  <br/> |110 ms.  <br/> |
|**Server Response Time 95th percentile for read operations:** <br/> |1161 ms.  <br/> |1679 ms.  <br/> |
|**Server Response Time 50th percentile for write operations:** <br/> |1828 ms.  <br/> |2253 ms.  <br/> |
|**Server Response Time 95th percentile for write operations:** <br/> |3321 ms.  <br/> |4648 ms.  <br/> |
|**Tests completed per second:** <br/> |15  <br/> |28  <br/> |
|**Average CPU (application server or front-end web server)** <br/> |49%  <br/> |88%  <br/> |
|**Average CPU (SQL Server)** <br/> |14%  <br/> |28%  <br/> |
|**Peak memory usage (application server or front-end web server)** <br/> |6.1 GB  <br/> |6.3 GB  <br/> |
   
The following graph shows the data in the previous two tables:
  
**Figure 2: Managed Metadata Service application performance**

![Excel bar chart shows Managed Metadata Service application performance data from the previous tables. First performance data shows a single application server or front-end web server and then shows two with twice the load, for both green and red zones.](../media/ECMCapacityMetadataSrvPerf.gif)
  
### Effect of friendly URLs on Search crawls for friendly URLs

SharePoint Server 2013 includes the Managed Navigation feature and two timer jobs that are triggered to make sure that the search crawl receives the latest versions of pages that use friendly URLs. Our tests found that running these timer jobs that communicated with the Managed Metadata Service application did not have a significant effect on read and write operations that target the same application.
  
### Effect of CSOM calls

Some tests increased the CSOM calls made in our test procedure compared to the baseline case. We increased these from 20 percent of tests to 66 percent. The test results show that the number of executed tests declined from 28 to 22 per second. The server response times are comparable to the baseline. The reduction in the number of executed tests is because of the increased overhead of multiple calls to the front-end web server for each action for the CSOM calls compared to fewer calls involved in the web service calls.
  
### Effect of having more hashtag operations

In another test case, we increased the percentage of the hashtag operations from 35 percent in our baseline to 71 percent in our tests. The results show that the number of executed tests declined from 28 to 19. The server response times are also about 30 percent greater than the baseline. The reduction in the number of executed tests is attributed to the fairly high number of terms in the hashtags term set and the much increased percentage of write operations in the changed procedure.
  
## See also
<a name="TR"> </a>

#### Concepts

[Plan for managed metadata in SharePoint Server](../governance/managed-metadata-planning.md)
#### Other Resources

[Overview of managed metadata service applications in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ee424403(v=office.14))
  
[Plan terms and term sets in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ee519604(v=office.14))

