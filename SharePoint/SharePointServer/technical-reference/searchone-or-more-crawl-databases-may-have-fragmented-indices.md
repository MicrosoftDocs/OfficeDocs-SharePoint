---
title: "Search - One or more crawl databases may have fragmented indices (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0ffd36db-3f34-4f9f-b3fe-c8bea09a9d8f
description: "Learn how to resolve the SharePoint Health Analyzer rule: Search - One or more crawl databases may have fragmented indices, for SharePoint Server."
---

# Search - One or more crawl databases may have fragmented indices (SharePoint Server)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
>[!IMPORTANT]
>This health analyzer rule only applies to SharePoint 2010 as this was removed in [KB4011601](https://support.microsoft.com/help/4011601) for SharePoint Server 2013 and [KB4011576](https://support.microsoft.com/help/4011576) for SharePoint Server 2016.

 **Rule Name:** Search - One or more crawl databases may have fragmented indices. 
  
 **Summary:** This article describes the SharePoint Health Analyzer rule for Search service application crawl database defragmentation. The fragmentation of crawl data indexes occurs on a different level than regular disk fragmentation. It occurs in each crawl database as data is created, updated, or deleted during normal crawl activity. When you run the health rule, the system makes used storage contiguous, eliminates unused storage, and compacts the database. 
  
We recommend that you run the crawl database rule under the following circumstances:
  
- In SQL Server Enterprise, running the crawl database rule automatically enables the Page Compression feature to optimize I/O and disk storage usage.
    
- If significant performance degradation is determined to be caused by crawl database fragmentation. This should be a rare occurrence because crawl databases will usually have some level of fragmentation.
    
**Symptoms:** One or more of the following symptoms might appear: 
  
- Crawl rate may decrease as more time is spent writing crawl history to the crawl database.
    
- The crawl database defragmentation health rule is run and attempts to correct the fragmentation. Note: when this rule is correcting the fragmentation, the crawl rate is affected. Crawl rate may decrease as more time is spent writing metadata to the property database.
    
**Cause:** Fragmentation exists when indexes have pages in which the logical ordering, based on the key value, does not match the physical ordering inside the data file. All leaf pages of an index contain pointers to the next and the previous pages in the index. This forms a doubly linked list of all index/data pages. Ideally, the physical order of the pages in the data file should match the logical ordering. Overall disk throughput is increased when the physical ordering matches the logical ordering of the data. 
  
For more information about database fragmentation, including how to manually detect and repair fragmented indexes, see the SQL Server documentation.
  
 **Resolution: Enable and run the crawl database defragmentation health rule**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration, click **Monitoring**.
    
3. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
4. On the All Rules page, in the **Performance** section, click **Search - One or more crawl databases may have fragmented indices**.
    
5. If the rule is not enabled, in the **Health Analyzer Rule Definitions** dialog, click **Edit Item** on the ribbon. Ensure that the **Enabled** check box is selected, and then click **Save** on the ribbon. 
    
6. On the ribbon, click **Run Now**. 
    
7. Click **Close**.
    
The rule iterates over all crawl databases in all Search service applications. When it runs, it attempts to perform an online defragmentation first, and then it switches to offline defragmentation where required. In online defragmentation, only the SQL Server leaf pages are defragmented, not the SQL Server locked pages. In offline defragmentation, the locked pages and all the leaf pages are defragmented. In SQL Server Enterprise, the health rule automatically enables the Page Compression feature to optimize I/O and disk usage.
  

