---
title: "Performance testing for SharePoint Server 2013"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 8/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: fe3d1a2a-6147-4d10-8d88-cba86ee2f436
description: "Learn about how to plan and execute performance testing of a SharePoint Server 2013 environment."
---

# Performance testing for SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
This article describes how to test the performance of SharePoint Server 2013. The testing and optimization stage is a critical component of effective capacity management. You should test new architectures before you deploy them to production and you should conduct acceptance testing in conjunction with following monitoring best practices in order to ensure the architectures you design achieve the performance and capacity targets. This allows you to identify and optimize potential bottlenecks before they impact users in a live deployment. If you are upgrading from an Office SharePoint Server 2007 environment and plan to make architectural changes, or are estimating user load of the new SharePoint Server 2013 features, then testing particularly important to make sure your new SharePoint Server 2013-based environment will meet performance and capacity targets. 
  
Once you have tested your environment, you can analyze the test results to determine what changes need to be made in order to achieve the performance and capacity targets you established in [Step 1: Model](capacity-planning.md#step1) of [Capacity planning for SharePoint Server 2013](capacity-planning.md).
  
These are the recommended sub steps you should follow for pre-production:
  
- Create the test environment that mimics the initial architecture you designed in [Step 2: Design](capacity-planning.md#step2).
    
- Populate the storage with the dataset or part of the dataset that you've identified in [Step 1: Model](capacity-planning.md#step1).
    
- Stress the system with synthetic load that represents the workload you've identified in [Step 1: Model](capacity-planning.md#step1).
    
- Run tests, analyze results, and optimize your architecture.
    
- Deploy your optimized architecture in your data center, and roll out a pilot with a smaller set of users.
    
- Analyze the pilot results, identify potential bottlenecks, and optimize the architecture. Retest if needed. 
    
- Deploy to the production environment.
    
Before you read this article, you should read [Capacity management and sizing overview for SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ff758647(v=office.14)).
  
    
## Create a Test Plan
<a name="createplan"> </a>

Verify that your plan includes:
  
- Hardware that is designed to operate at expected production performance targets. Always measure the performance of test systems conservatively.
    
- If you have custom code or custom component, it is important that you test the performance of those components in isolation first to validate their performance and stability. After they are stable, you should test the system with those components installed and compare performance to the farm without them installed. Custom components are often a major culprit of performance and reliability problems in production systems.
    
- Know the goal of your testing. Understand ahead of time what your testing objectives are. Is it to validate the performance of some new custom components that were developed for the farm? Is it to see how long it will take to crawl and index a set of content? Is it to determine how many requests per second your farm can support? There can be many different objectives during a test, and the first step in developing a good test plan is deciding what your objectives are.
    
- Understand how to measure for your testing goal. If you are interested in measuring the throughput capacity of your farm for example, you will want to measure the RPS and page latency. If you are measuring for search performance then you will want to measure crawl time and document indexing rates. If your testing objective is well understood, that will help you clearly define what key performance indicators you need to validate in order to complete your tests.
    
## Create the Test Environment
<a name="createenvironment"> </a>

Once your test objectives have been decided, your measurements have been defined, and you have determined what the capacity requirements are for your farm (from steps 1 and 2 of this process), the next objective will be to design and create the test environment. The effort to create a test environment is often underestimated. It should duplicate the production environment as closely as possible. Some of the features and functionality you should consider when designing your test environment include:
  
- **Authentication**: Decide whether the farm will use Active Directory Domain Services (AD DS), forms-based authentication (and if so with what directory), claims-based authentication, etc. Regardless of which directory you are using, how many users do you need in your test environment and how are you going to create them? How many groups or roles are you going to need and how will you create and populate them? You also need to ensure that you have enough resources allocated to your authentication services that they don't become a bottleneck during testing.
    
- **DNS**: Know what the namespaces are that you will need during your testing. Identify which servers will be responding to those requests and make sure you've included a plan that has what IP addresses will be used by which servers, and what DNS entries you will need to create.
    
- **Load balancing**: Assuming you are using more than one server (which you normally would or you likely wouldn't have enough load to warrant load testing), you will need some kind of load balancer solution. That could be a hardware load balancing device, or you could use software load balancing like Windows NLB. Figure out what you will use and write down all of the configuration information you will need to get it set up quickly and efficiently. Another thing to remember is that load test agents typically try and resolve the address to a URL only once every 30 minutes. That means that you should not use a local hosts file or round robin DNS for load balancing because the test agents will likely end up going to the same server for every single request, instead of balancing around all available servers.
    
- **Test servers**: When you plan your test environment, you not only need to plan for the servers for the SharePoint Server 2013 farm, you also need to plan for the machines needed to execute the tests. Typically that will include 3 servers at a minimum; more may be necessary. If you are using Visual Studio Team System (Team Test Load Agent) to do the testing, one machine will be used as the load test controller. There are generally 2 or more machines that are used as load test agents. The agents are the machines that take the instructions from the test controller about what to test and issue the requests to the SharePoint Server 2013 farm. The test results themselves are stored on a SQL Server-based computer. You should not use the same SQL Server-based computer that is used for the SharePoint Server 2016 farm, because writing the test data will skew the available SQL Server resources for the SharePoint Server 2013 farm. You also need to monitor your test servers when running your tests, the same way as you would monitor the servers in the SharePoint Server 2013 farm, or domain controllers, etc. to make sure that the test results are representative of the farm you're setting up. Sometimes the load agents or controller can become the bottleneck themselves. If that happens then the throughput you see in your test is typically not the maximum the farm can support.
    
- **SQL Server**: In your test environment, follow the guidance in the sections "Configure SQL Server" and "Validate and monitor storage and SQL Server performance" in the article [Storage and SQL Server capacity planning and configuration (SharePoint Server)](storage-and-sql-server-capacity-planning-and-configuration.md).
    
- **Dataset validation**: As you decide what content you are going to run tests against, remember that in the best case scenario you will use data from an existing production system. For example, you can back up your content databases from a production farm and restore them into your test environment, then attach the databases to bring the content into the farm. Anytime you run tests against made up or sample data, you run the risk of having your results skewed because of differences in your content corpus.
    
If you do have to create sample data, there are a few considerations to keep in mind as you build out that content:
  
- All pages should be published; nothing should be checked out
    
- Navigation should be realistic; don't build beyond what you would reasonably expect to use in production.
    
- You should have an idea of the customizations the production site will be using. For example, master pages, style sheets, JavaScript, etc. should all be implemented in the test environment as closely as possible to the production environment. 
    
- Determine how many SharePoint groups and/or permission levels you are going to need, and how you are going to associate users with them.
    
- Figure out whether you'll need to do profile imports, and how long that will take.
    
- Determine whether you'll need Audiences, and how you'll create and populate them. 
    
- Determine whether you need additional search content sources, and what you will need to create them. If you won't need to create them, determine whether you'll have network access to be able to crawl them. 
    
- Determine whether you have enough sample data - documents, lists, list items, etc. If not, create a plan for how you will create this content.
    
- Have a plan for enough unique content to adequately test search. A common mistake is to upload the same document - maybe hundreds or even thousands of times - to different document libraries with different names. That can impact search performance because the query processor will spend an ordinate amount of time doing duplicate detection that it wouldn't otherwise have to in a production environment with real content.
    
## Create Tests and Tools
<a name="createtests"> </a>

After the test environment is functional, it is time to create and fine-tune the tests that will be used to measure the performance capacity of the farm. This section will at times make references specifically to Visual Studio Team System (Team Test Load Agent), but many of the concepts are applicable irrespective of which load test tool you use. For more information about testing tools available for Azure DevOps (formerly VSTS), see [DevOps tools overview for Azure DevOps](/azure/devops/user-guide/devops-alm-overview). 
  
You can also use the SharePoint Load Test Kit (LTK) in conjunction with VSTS for load testing of SharePoint 2010 farms. The Load Test Kit generates a Visual Studio Team System 2008 load test based on Windows SharePoint Services 3.0 and Microsoft Office SharePoint Server 2007 IIS logs. The VSTS load test can be used to generate synthetic load against SharePoint Foundation 2010 or SharePoint Server 2010 as part of a capacity planning exercise or a pre-upgrade stress test.
  
The Load Test Kit is included in the Microsoft SharePoint 2010 Administration Toolkit v2.0, available from the [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=20022). 
  
A key criterion to the success of the tests is to be able to effectively simulate a realistic workload by generating requests across a wide range of the test site data, just as users would access a wide range of content in a production SharePoint Server 2013 farm. In order to do that, you will typically need to construct your tests such that they are data driven. Rather than creating hundreds of individual tests that are hard-coded to access a specific page, you should use just a few tests that use data sources containing the URLs for those items to dynamically access that set of pages.
  
 In Visual Studio Team System (Team Test Load Agent), a data source can come in a variety of formats, but a CSV file format is often easiest to manage and transport between development and test environments. Keep in mind that creating CSV files with that content might require the creation of custom tools to enumerate the SharePoint Server 2013-based environment and record the various URLs being used. 
  
You may need to use tools for tasks like:
  
- Creating users and groups in Active Directory or other authentication store if you're using forms based authentication
    
- Enumerating URLs for sites, lists and libraries, list items, documents, etc. and putting them into CSV files for load tests
    
- Uploading sample documents across a range of document libraries and sites
    
- Creating site collections, webs, lists, libraries, folders and list items
    
- Creating My Sites
    
- Creating CSV files with usernames and passwords for test users; these are the user accounts that the load tests will execute as. There should be multiple files so that, for example, some contain only administrator users, some contain other users with elevated privileges (like author / contributor, hierarchy manager, etc.), and others are only readers, etc.
    
- Creating a list of sample search keywords and phrases
    
- Populating SharePoint groups and permission levels with users and Active Directory groups (or roles if you are using forms based authentication)
    
When creating the web tests, there are other best practices that you should observe and implement. They include:
  
- Record simple web tests as a starting point. Those tests will have hard-coded values in them for parameters like URL, ID's, etc. Replace those hard-coded values with links from your CSV files. Data binding those values in Visual Studio Team System (Team Test Load Agent) is extremely easy.
    
- Always have validation rules for your test. For example, when requesting a page, if an error occurs you will often get the error.aspx page in response. From a web test perspective it appears as just another positive response, because you get an HTTP status code of 200 (successful) in the load test results. Obviously an error has occurred though so that should be tracked differently. Creating one or more validation rules allows you to trap when certain text is sent as a response so that the validation fails and the request is marked as a failure. For example, in Visual Studio Team System (Team Test Load Agent) a simple validation rule might be a ResponseUrl validation - it records a failure if the page that is rendered after redirects is not the same response page that was recorded in the test. You could also add a FindText rule that will record a failure if it finds the word "access denied", for example, in the response.
    
- Use multiple users in different roles for tests. Certain behaviors such as output caching work differently depending on the rights of the current user. For example, a site collection administrator or an authenticated user with approval or authoring rights will not get cached results because we always want them to see the most current version of content. Anonymous users, however, will get the cached content. You need to make sure that your test users are in a mix of these roles that approximately matches the mix of users in the production environment. For example, in production there are probably only two or three site collection administrators, so you should not create tests where 10% of the page requests are made by user accounts that are site collection administrators over the test content.
    
- Parsing dependent requests is an attribute of a Visual Studio Team System (Team Test Load Agent) that determines whether the test agent should attempt to retrieve just the page, or the page and all associated requests that are part of the page, such as images, style sheets, scripts, etc. When load testing, we usually ignore these items for a few reasons:
    
  - After a user hits a site the first time these items are often cached by the local browser
    
  - These items don't typically come from SQL Server in a SharePoint Server 2013-based environment. With BLOB caching turned on, they are instead served by the Web servers so they don't generate SQL Server load.
    
If you regularly have a high percentage of first time users to your site, or you have disabled browser caching, or for some reason you don't intend to use the blob cache, then it may make sense to enable parsing dependent requests in your tests. However this is really the exception and not the rule of thumb for most implementations. Be aware that if you do turn this on it can significantly inflate the RPS numbers reported by the test controller. These requests are served so quickly it may mislead you into thinking that there is more capacity available in the farm than there actually is.
  
- Remember to model client application activity as well. Client applications, such as Microsoft Word, PowerPoint, Excel and Outlook generate requests to SharePoint Server 2013 farms as well. They add load to the environment by sending the server requests such as retrieving RSS feeds, acquiring social information, requesting details on site and list structure, synchronizing data, etc. These types of requests should be included and modeled if you have those clients in your implementation.
    
- In most cases a web test should only contain a single request. It's easier to fine-tune and troubleshoot your testing harness and individual requests if the test only contains a single request. Web tests will typically need to contain multiple requests if the operation it is simulating is composed of multiple requests. For example, to test this set of actions you will need a test with multiple step: checking out a document, editing it, checking it in and publishing it. It also requires reserving state between the steps - for example, the same user account should be used to check it out, make the edits, and check it back in. Those multi-step operations that require state to be carried forward between each step are best served by multiple requests in a single web test.
    
- Test each web test individually. Make sure that each test is able to complete successfully before running it in a larger load test. Confirm that all of the names for web applications resolve, and that the user accounts used in the test have sufficient rights to execute the test.
    
Web tests comprise the requests for individual pages, uploading documents, view list items, etc. All of these are pulled together in load tests. A load test is where you plug in all of the different web tests that are going to be executed. Each web test can be given a percentage of time that it will execute - for example, if you find that 10% of requests in a production farm are search queries, then in the load test you would configure a query web test to run 10% of the time. In Visual Studio Team System (Team Test Load Agent), load tests are also how you configure things like the browser mix, network mix, load patterns, and run settings. 
  
There are some additional best practices that should be observed and implemented for load tests:
  
- Use a reasonable read/write ratio in your tests. Overloading the number of writes in a test can significantly impact the overall throughput of a test. Even on collaboration farms, the read/write ratios tend to have many more reads than writes. 
    
- Consider the impact of other resource intensive operations and decide whether they should be occurring during the load test. For example, operations like backup and restore are not generally done during a load test. A full search crawl may not be usually run during a load test, whereas an incremental crawl may be normal. You need to consider how those tasks will be scheduled in production - will they be running at peak load times? If not, then they should probably be excluded during load testing, when you are trying to determine the maximum steady state load you can support for peak traffic.
    
- Don't use think times. Think times are a feature of Visual Studio Team System (Team Test Load Agent) that allow you to simulate the time that users pause between clicks on a page. For example a typical user might load a page, spend three minutes reading it, then click a link on the page to visit another site. Trying to model this in a test environment is nearly impossible to do correctly, and effectively doesn't add value to the test results. It's difficult to model because most organizations don't have a way to monitor different users and the time they spend between clicks on different types of SharePoint sites (like publishing versus search versus collaboration, etc.). It also doesn't really add value because even though a user may pause between page requests, the SharePoint Server 2013-based servers do not. They just get a steady stream of requests that may have peaks and valleys over time, but they are not waiting idly as each user pauses between clicking links on a page.
    
- Understand the difference between users and requests. Visual Studio Team System (Team Test Load Agent) has load pattern where it asks you to enter the number of users to simulate. This doesn't have anything to do with application users, it's really just how many threads are going to be used on the load test agents to generate requests. A common mistake is thinking that if the deployment will have 5,000 users for example, then 5,000 is the number that should be used in Visual Studio Team System (Team Test Load Agent) - it is not! That's one of the many reasons why when estimating capacity planning requirements, the usage requirements should be based on number of requests per second and not number of users. In a Visual Studio Team System (Team Test Load Agent) load test, you will find that you can often generate hundreds of requests per second using only 50 to 75 load test "users".
    
- Use a constant load pattern for the most reliable and reproducible test results. In Visual Studio Team System (Team Test Load Agent) you have the option of basing load on a constant number of users (threads, as explained in the previous point), a stepped up load pattern of users, or a goal based usage test. A stepped load pattern is when you start with a lower number of users and then "step up" adding additional users every few minutes. A goal based usage test is when you establish a threshold for a certain diagnostic counter, like CPU utilization, and test attempts to drive the load to keep that counter between a minimum and maximum threshold that you define for it. However, if you are just trying to determine the maximum throughput your SharePoint Server 2013 farm can sustain during peak load, it is more effective and accurate to just pick a constant load pattern. That allows you to more easily identify how much load the system can take before starting to regularly exceed the thresholds that should be maintained in a healthy farm.
    
Each time you run a load test remember that it is changing data in the database. Whether that's uploading documents, editing list items, or just recording activity in the usage database, there will be data that is written to SQL Server. To ensure a consistent and legitimate set of test results from each load test, you should have a backup available before you run the first load test. After each load test is complete the backup should be used to restore the content back to the way it was before the test was started. 
  
## See also
<a name="createtests"> </a>

#### Concepts

[Capacity planning for SharePoint Server 2013](capacity-planning.md)
  
[Monitoring and maintaining SharePoint Server 2013](monitoring-and-maintaining.md)
  
[Software boundaries and limits for SharePoint Server 2016](../install/software-boundaries-and-limits-0.md)
#### Other Resources

[Capacity management and sizing overview for SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ff758647(v=office.14))

