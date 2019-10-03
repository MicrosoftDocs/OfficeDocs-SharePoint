---
title: "Best practices for upgrading to SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/17/2016
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 1c3b661f-7d88-4b2c-bc3a-3337253f3f30
description: "Understand how to get the most out of testing upgrade and how to guarantee a successful upgrade to SharePoint Server 2016."
---

# Best practices for upgrading to SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]
  
To increase your chances of a successful and faster upgrade to SharePoint Server 2016, follow these best practices to test and complete an upgrade.
  
## Best practices for testing upgrade

To understand your environment before you upgrade it, and to plan for the time that an upgrade will require, you should try one or more trial upgrades. The goal of testing upgrade is to find and fix issues and develop confidence in the outcome before the real upgrade. To develop an accurate trial of the upgrade process from SharePoint Server 2013 with Service Pack 1 (SP1) to SharePoint Server 2016, follow these best practices:
  
1. Know what is in your environment. Do a full survey first.
    
    Document the hardware and software in your environment, where server-side customizations are installed and used, and the settings that you need. This helps you plan the trial environment and also helps you recover if upgrade fails. 
    
2. Make your test environment as similar as possible to your real environment.
    
    If possible, use the same kind of hardware and use the same settings, the same URLs, and so on to configure it. Minimize the differences between your test environment and your real environment. As you introduce more differences, you are likely to spend time resolving unrelated issues to make sure that they will not occur during the actual upgrade.
    
3. Use real data.
    
    Use copies of your actual databases to run the tests. When you use real data, you can identify trouble areas and also determine upgrade performance. You can also measure how long different upgrade sequences and actions take on different kinds of data. If you cannot test all the data, test a representative subset of the data. Make sure that you find issues with the different kinds and sizes of sites, lists, libraries, and customizations that are present in your environment. If you cannot test all data because of storage concerns, try going over the data in several passes, removing the old trial copies before going on to the next batch.
    
4. Run multiple tests.
    
    A single test can tell you whether you will encounter big problems. Multiple tests will help you find all the issues that you might face and help you estimate a more accurate timeline for the process. By running multiple tests, you can determine the following:
    
  - The upgrade approaches that will work best for your environment
    
  - The downtime mitigation techniques that you should plan to use
    
  - How the process or performance may change after you address the issues that you uncovered in your first tests
    
    Your final test pass can help you validate whether you have addressed the errors and are ready to upgrade your production environment.
    
5. Do not ignore errors or warnings.
    
    Even though a warning is not an error, a warning could lead to problems in the upgrade process. Resolve errors, but also investigate warnings to make sure that you know the results that a warning might produce.
    
6. Test the upgraded environment, not just the upgrade process.
    
    Check your service applications and run a search crawl and review the log files. 
    
## Best practices for upgrading to SharePoint Server 2016

To guarantee a smooth upgrade from SharePoint Server 2013 to SharePoint Server 2016, follow these best practices:
  
1. Install the latest [Cumulative Update for SharePoint Server 2013](https://docs.microsoft.com/en-us/officeupdates/sharepoint-updates#sharepoint-2013-update-history) and latest [Public Update for SharePoint Server 2016](https://docs.microsoft.com/en-us/officeupdates/sharepoint-updates#sharepoint-2016-update-history) (but at a minimum, SharePoint Server 2013 must be running the March 2013 PU (15.0.4481.1005)).

2. Ensure that the environment is fully functioning before you begin to upgrade.
    
    An upgrade does not solve problems that already exist in your environment. Therefore, make sure that the environment is fully functioning before you start to upgrade. For example, if you are not using web applications, unextend them before you upgrade. If you want to delete a web application in Internet Information Services (IIS), unextend the web application before you delete it. Otherwise, SharePoint Server 2016 will try to upgrade the web application even though it does not exist, and the upgrade will fail. If you find and solve problems beforehand, you are more likely to meet the estimated upgrade schedule.
    
3. Perform a trial upgrade on a test farm first.
    
    Copy your databases to a test environment and perform a trial upgrade. Examine the results to determine the following: 
    
  - Whether the service application data was upgraded as expected
    
  - The appearance of upgraded sites
    
  - The time to allow for post-upgrade troubleshooting
    
  - The time to allow for the upgrade process
    
    Try a full search indexing crawl.
    
4. Plan for capacity.
    
    Ensure that you have enough disk, processor, and memory capacity to handle upgrade requirements. For more information about system requirements, see [System requirements for SharePoint Server 2016](../install/system-requirements-for-sharepoint-server-2016.md). 
    
5. Clean up before you upgrade
    
    Issues in your environment can affect the success of upgrade, and unnecessary or very large amounts of data can affect upgrade performance for both databases and site collections. If you don't need something in your environment, consider removing it before upgrade. If there are issues detected, try to resolve them before you start to upgrade. .
    
6. Back up your databases.
    
    Perform a full backup of your databases before you upgrade. That way, you can try upgrade again if it fails. 
    
7. Optimize your environment before upgrade.
    
    Be sure to optimize your SharePoint Server 2013 with Service Pack 1 (SP1) environment to meet any limits or restrictions, either from your business or governance needs or from the SharePoint Server 2016 boundaries and limits before upgrade. This will help reduce errors during the upgrade process and prevent broken lists or sites after upgrade. 
    
8. (Optional) Set the original databases to read-only if you want to keep your original environment available while you upgrade.
    
    If you expect a long outage period while you upgrade, you can set the databases in the original environment to read-only. Users can continue to access the data but cannot change it. For more information, see [Upgrade content databases to SharePoint Server 2016](upgrade-content-databases.md).
    
9. After upgrade, review the Upgrade Status page and upgrade logs to determine whether you must address issues. Then review the upgraded sites.
    
    The Upgrade Status page reports on the upgrade progress, and the upgrade logs list any errors or warnings that occurred during the upgrade process. Verify all the sites and test them before you consider the upgrade finished. For more information, see [Verify database upgrades in SharePoint Server 2016](verify-upgrade-for-databases.md) and the **Review site collections upgraded** section in [Upgrade site collections to SharePoint Server 2016](upgrade-site-collections.md).
    
10. Make sure that the appropriate service pack or update is applied to your 2013 environment. If you are using remote blob storage (RBS) in your environment, you must be running SharePoint Server 2013 with Service Pack 1 (SP1) in your environment before you start the upgrade process.
    

