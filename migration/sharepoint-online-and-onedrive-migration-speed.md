---
title: "SharePoint Online and OneDrive Migration Speed"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.custom: 
description: "This article explains the factors that influence migration speed at each phase while using the SharePoint Online Migration API."
---

# General guidance for improving SharePoint and OneDrive migration performance

This article explains the factors that influence performance when migrating content to SharePoint Online and OneDrive.

Migration performance can be impacted by network infrastructure, file size, migration time, and throttling. Understanding these will help you plan and maximize the efficiency of your migration.

Currently, Microsoft's [SharePoint Migration Tool (SPMT)](https://docs.microsoft.com/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool) as well as several third party vendor tools utilize the SharePoint API for migration. It leverages Azure and uses channels for large content transfer.  Regardless of which migration tool you use, these factors will apply. Follow the recommendations listed below for each phase of your migration process.

## Before migration

Planning is the key to optimizing your migration.  Determine what content you need to migrate,  prioritize when the content needs to be migrated, and decide on what the optimal migration infrastructure should be.

### I. Scan the source

The first rule of a good migration is to know your source; evaluate and triage your content before you migrate. What content really needs be migrated? What can be left behind? How many file versions should be included? The amount of content you migrate will determine the overall size of your project. 

### II. Package the content
This step is where the tool creates a proper package for the content to be imported into the cloud. This step is automated in SPMT and in most third-party tools. 

**Package size.** To improve migration throughput, we recommend that you package at least 250 files per transfer. For the transfer size we recommend a minimum of 100MB and less than 250MB per package. This will result in a faster upload speed to Azure and leverages the scale capabilities of the migration API.

The following table provides estimates of the type of speed you may achieve based on the types of content you are migrating.  


|**Type of metadata**|**Examples**|**Maximum**|
|:-----|:-----|:-----|
|Light|ISO files, video files |2 TB/day|
|Medium |List items, Office files (~1.5MB)|1 TB/day|
|Heavy|List items with custom columns, small files (~50kb)|250 GB /day|


- Large file size migrates faster than smaller ones. Small file size can result in larger overhead and processing time which directly impacts the performance.

- Files migrate faster than objects and list items.

The speed of this step depends on the efficiency of the tool you are using and the type of content that you package. Splitting your packages in a smart way is something that will greatly improve this step. In addition, ensure that your permissions, sharing, or other limits are set up properly for migration and are within [SharePoint Online limits and boundaries](https://docs.microsoft.com/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).


## During migration


### I. Upload to Azure
SPMT or your third-party tool will migrate your content into SharePoint Online using the Migration API, leveraging Azure as a temporary holding place.

If you have a good connection and can configure your datacenter, choose the same datacenter location closest geographically to you for your Azure and your Office 365 account. 
Migration data throughput is highest during off-peak hours, which are typically nights and weekends in your region's time zone. Your region's time zone is determined by where your SharePoint Online tenant is set up.



### II. The Migration API

The final step of the migration process is when the data is moved from Azure to SharePoint Online. This action is transparent to the user when using SPMT or a third- party tool.

To improve throughput, users are encouraged to run parallel tasks against different site collections if possible. We recommend that you do not submit more than 5,000 migration jobs/requests at one time. Over-queuing the network will create an extra load on the database and slow migration down. Make sure your task has completed before you upload a new migration request. Some tools may already be doing this for you.

During migration, it is not uncommon for your migration task to be throttled. Throttling is implemented to ensure the best user experience and reliability of SharePoint Online. It is primarily used to load balance the database and can occur if you misconfigure migration settings, such as migrating all your content in a single task or attempting to migrate during peak hours. 


For more technical background and information, please see 
- [Migration API Overview](https://docs.microsoft.com/en-us/sharepoint/dev/apis/migration-api-overview) 
- [Avoid getting throttled or blocked in SharePoint Online](http://go.microsoft.com/fwlink/?LinkID=619858&amp;clcid=0x409)

## After migration
After the migration is completed, verify that your content has been successfully moved to SharePoint Online or OneDrive.

## FAQ and Troubleshooting


*Question:* My migration is going so slow or I am being throttled. What can I do?</br>
*Answer:*  Check that you have configured your migration settings properly. Turn off any software that you do not need to use during migration. For example, disable any file synchronization program or antivirus program on the migrated content. This will help reduce throttle and improve performance.

*Question:* I continually getting throttled while I am attempting to migrate. Can Microsoft turn off the throttle to help me with migration?</br>
*Answer:* Unfortunately, we are not able to disable throttle. Throttle is built into our server to protect the database from going down. If you are being throttled with a 429 error, it's an indication that your migration tool is overly aggressive and is over its allocated quota.  Please try to migrate during off-peak hours or reduce the number of VMs you are using.

If after several days you are still experiencing excessive throttling, please open a Microsoft support ticket.
Include the following in your support ticket:

- How often are you seeing the throttle (e.g. throttle count/hour)
- How much data were you being able to migrate (e.g., 2MB per hour or per day)
- The name of the third party app are you running
- The total size of the content you wish to migrate
- Your migration schedule
- Your Company name and Tenant URL



*Question:* How much can I migrate per day?</br>
*Answer:* Plan to migrate at a maximum of 2TB/day.

*Question:* I have a very big migration (> 100 TB) and I would like some help, who should I contact?</br>
*Answer:* For larger than a 100TB migration, please submit a support request with Microsoft indicating that you are doing a large migration (>100TB).
Follow these steps:
1. Click on **Need help?**
2. For the title, enter **"SharePoint Migration over 100TB"**.
3. Include all of the following on the support ticket:
    - Your company name and Tenant URL
    - Estimated size of your migration
    - An estimate of when you would like to start and complete your migration
    - Describe where you are migrating your content from, such as SharePoint Server, Box, GDrive, File shares, etc.

*Question:* I have tried everything, but nothing works. Now what do I do?</br>
*Answer:* Open a support ticket with [http://support.microsoft.com](http://support.microsoft.com).





## Related Topics

[Avoid getting throttled or blocked in SharePoint Online](http://go.microsoft.com/fwlink/?LinkID=619858&amp;clcid=0x409)

