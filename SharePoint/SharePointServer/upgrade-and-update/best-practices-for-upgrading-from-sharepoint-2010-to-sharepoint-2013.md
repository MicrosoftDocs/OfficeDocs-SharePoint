---
title: "Best practices for upgrading from SharePoint 2010 to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5844f7f1-56ac-4742-bc76-2466e02cb7fb
description: "Understand how to get the most out of testing upgrade and how to guarantee a smooth upgrade to SharePoint 2013."
---

# Best practices for upgrading from SharePoint 2010 to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]

To increase your chances of a successful and faster upgrade to SharePoint 2013, follow these best practices to test and complete an upgrade.
  
## Best practices for testing upgrade

To understand your environment before you upgrade it, and to plan for the time that an upgrade will require, you should try one or more trial upgrades. The goal of testing upgrade is to find and fix issues and develop confidence in the outcome before the real upgrade. To develop an accurate trial of the upgrade process from SharePoint 2010 Products to SharePoint 2013, follow these best practices:
  
1. Know what is in your environment. Do a full survey first.
    
    Document the hardware and software in your environment, where server-side customizations are installed and used, and the settings that you need. This helps you plan the trial environment and also helps you recover if upgrade fails. A worksheet is available to record information about your environment. 
    
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
    
For more information about how to test upgrade, see [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)) and the [SharePoint 2013 Products Preview - Test Your Upgrade Process model](https://go.microsoft.com/fwlink/?LinkId=252098).
  
## Best practices for upgrading to SharePoint 2013

To guarantee a smooth upgrade from SharePoint 2010 Products to SharePoint 2013, follow these best practices:
  
1. Ensure that the environment is fully functioning before you begin to upgrade.
    
    An upgrade does not solve problems that already exist in your environment. Therefore, make sure that the environment is fully functioning before you start to upgrade. For example, if you are not using web applications, unextend them before you upgrade. If you want to delete a web application in Internet Information Services (IIS), unextend the web application before you delete it. Otherwise, SharePoint 2013 will try to upgrade the web application even though it does not exist, and the upgrade will fail. If you find and solve problems beforehand, you are more likely to meet the estimated upgrade schedule.
    
2. Perform a trial upgrade on a test farm first.
    
    Copy your databases to a test environment and perform a trial upgrade. Examine the results to determine the following: 
    
  - Whether the service application data was upgraded as expected
    
  - The appearance of upgraded sites
    
  - The time to allow for post-upgrade troubleshooting
    
  - The time to allow for the upgrade process
    
    Try a full search indexing crawl. For more information, see [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)).
    
3. Plan for capacity.
    
    Ensure that you have enough disk, processor, and memory capacity to handle upgrade requirements. For more information about system requirements, see [Hardware and software requirements for SharePoint 2013](../install/hardware-and-software-requirements-0.md). For more information about how to plan the disk space that is required for upgrade, see [Plan for performance during upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262891(v=office.14)) and [Performance planning in SharePoint Server 2013](../administration/performance-planning-in-sharepoint-server-2013.md)
    
4. Clean up before you upgrade
    
    Issues in your environment can affect the success of upgrade, and unnecessary or very large amounts of data can affect upgrade performance for both databases and site collections. If you don't need something in your environment, consider removing it before upgrade. If there are issues detected, try to resolve them before you start to upgrade. For more information, see [Clean up an environment before an upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff382641(v=office.14)).
    
5. Back up your databases.
    
    Perform a full backup of your databases before you upgrade. That way, you can try upgrade again if it fails. 
    
6. Optimize your environment before upgrade.
    
    Be sure to optimize your SharePoint 2010 Products environment to meet any limits or restrictions, either from your business or governance needs or from the SharePoint 2013 boundaries and limits before upgrade. This will help reduce errors during the upgrade process and prevent broken lists or sites after upgrade. For more information about limits in the product, see [Software boundaries and limits for SharePoint 2013](../install/software-boundaries-and-limits.md). For more information about large lists and how to address the lower limit on site collections, see [Clean up an environment before an upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff382641(v=office.14)).
    
7. (Optional) Set the original databases to read-only if you want to keep your original environment available while you upgrade.
    
    If you expect a long outage period while you upgrade, you can set the databases in the original environment to read-only. Users can continue to access the data but cannot change it. For more information, see [Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md).
    
8. After upgrade, review the Upgrade Status page and upgrade logs to determine whether you must address issues. Then review the upgraded sites.
    
    The Upgrade Status page reports on the upgrade progress, and the upgrade logs list any errors or warnings that occurred during the upgrade process. Verify all the sites and test them before you consider the upgrade finished. For more information, see [Verify database upgrades in SharePoint 2013](verify-upgrade.md) and [Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md).
    
9. Defer upgrade for site collections until you can get updated customizations to support 2013 mode.
    
    If you wait until the customizations are available, you can complete the initial upgrade of database and services without significantly affecting use of the existing sites in 2010 mode.
    
10. Make sure that the appropriate service pack or update is applied to your 2010 environment. If you are using remote blob storage (RBS) in your environment, you must be running Service Pack 1 for SharePoint 2010 Products in your environment before you start the upgrade process.
    
## See also

#### Other Resources

[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Get started with upgrades to SharePoint 2013](get-started-with-upgrade-0.md)
  
[Plan for upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc303429(v=office.14))

