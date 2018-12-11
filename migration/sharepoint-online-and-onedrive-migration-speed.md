---
title: "SharePoint Online and OneDrive Migration Speed"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom: 
description: "This article explains the factors that influence migration speed at each phase while using the SharePoint Online Migration API ."
---

# SharePoint Online and OneDrive migration performance and best practices 

TThis article explains the factors that influence performance when migrating content to SharePoint Online and OneDrive.

Currently, Microsoft’s SharePoint Migration Tool (SPMT) as well as several third party vendor tools utilize the SharePoint API for migration. It leverages Azure and uses channel for large content transfer. We do not recommend migrating by copying and pasting large amounts of content.  Regardless of which migration tool you use, these factors will apply.

Migration performance can be impacted by network infrastructure, file size, migration time, and throttle. Understanding these will help you plan and maximize the efficiency of your migration.


  
## Before migration

Planning is the key to optimizing your migration.  Determine what content you need to migrate,  prioritize when the content needs to be migrated, and decide on the optimal migration infrastructure should be. 

### I. Plan your Network Infrastructure
A basic migration infrastructure includes a source computer, migration computer, the network, Azure Storage and SharePoint Online (SPO).

- Source computer (where the content resides): 	Increase the speed of moving content out of the source location by spreading your source data across several computers or client VMs.
- Migration computer (running SPMT or 3rd party migration tool): Launch migration jobs from more than one computer to maximize speed.
- Network:	Spread your migration jobs over different networks or set the timing of your jobs to maximize low network usage to improve performance of your migration job.

### II. Scan the source

The first rule of a good migration is to know your source. Evaluate your data and triage what your needs are. What content really needs to move? What can be left behind? How many file versions should be included?
Take the time before starting your migration to clean up archives since the amount of content you are moving will determine to overall size of your project.

### III. Package the content
This step is where  the tool creates a proper package for the content to be imported into the cloud. This step is automated in SPMT and in most third-party tools. 
Package size: At a minimum, we advise that to package at least 250 files per transfer or at least 100MB size per transfer to improve the migration throughput Scale your packages by limiting your package to have less than 1000 objects and less than 250MB per package. This will result in a faster upload speed to Azure and as well as leverages the scale capabilities of the migration API. 

Below is a table shows estimates of the type of speed you may achieve based on the types of content you are migrating.  

The type of metadata directly impacts the speed of migration:
  
|**Type of metadata**|**Examples**|**Maximum**|
|:-----|:-----|:-----|
|Light  <br/> |ISO files, video files  <br/> |2 TB/day  <br/> |
|Medium  <br/> |List items, Office files (~1.5MB)  <br/> |1 TB/day  <br/> |
|Heavy  <br/> |List items with custom columns, small files (~50kb)  <br/> |250 GB /day  <br/> |

Large file size migrates faster than smaller ones and files migrate faster than object and list items.
 
Small file size or file content can result in larger overhead and processing time which directly impact the performance. 

The speed of this step depends on the efficiency of the tool and the type of content that you package. Splitting your packages in a smart way is something that will also greatly improve the last step. Also, please check to ensure the permission, sharing, or other limits are set up properly for migration.  

## During migration


### I. Upload to Azure
As you move content into SharePoint Online using the new Migration API, Azure is leveraged as a temporary holding place. The network speed to upload to Azure is much faster and lets you choose your datacenter. If you have a good connection, you might want to choose the same datacenter location for your Azure and your O365 account. If your network is slow, consider using the Azure Datacenter the closest geographically to you. The last option is to ship physical hard drives to Azure. The speed of this step depends on your internet connection or the time it takes to ship the drives to Microsoft. Sites such as Microsoft Azure Storage Performance and Scalability Checklist can provide a good idea of what to expect.  In addition, migration data throughput is highest during off-peak hours, which are typically nights and weekends in your region’s time zone.  Note:  Your region's time zone is determined by where your SPO (Sharepoint Online) tenant is set up.

SPO Import: The speed of ingesting data into SharePoint. The import speed largely impacted by the complexity of the metadata in the migrated content.

### II. The Migration API

The final step is the migration of data from Azure to SharePoint Online. This action is transparent when using SPMT or 3rd party tool.
Your goal when using the API is to try to have as many migration jobs running in parallel all the time to maximize your throughput. Some tools already do the splitting of the packages in a smart way and others leave it up to you to do the smart splitting of the jobs.
 
There is a limit to how many jobs can be run against the same site collection. This is why it is very important to run parallel jobs against different site collections as much as possible. Pre-partition your site collections so that your content is evenly spread out.

We do not encourage user to submit more than 5000 migration jobs at one time. Over queuing the network will create an extra load on the database and slow migration down. Make sure your job is processed as you upload new migration request.

During migration, it is not uncommon that your migration job will be throttled. Throttling is implemented to ensure the best user experience and reliability of Sharepoint Online. It is primarily used to load balance the database and can occur if user misconfigures the settings, using a single thread or attempts to migrate during peak hours competing resource with end user who is actively using the SPO at the same time.  

For more technical background and information, please see (link TBD).
## After migration
After the migration is completed, check your SPO to ensure completed and the data transfer is transferred successfully.

## FAQ & Troubleshooting


*Question:* My migration is going so slow or I am being throttled.  What can I do?</br></br>
*Answer:* Check the throttled session to make sure you have configured your migration settings properly. Turn off any software that you do not use during migration, such as the Sync program. This will limit the database resource contention.</br>


Question: How much can I migrate per day?</br>
Answer:   Plan to migrate a maximum of 2TB/day.


Question:  I have a very big migration (> 100 TB) and I would like some help, who should I contact?</br>
Answer:   For larger than 100TB migration, please contact Microsoft

Question: I have tried everything, but nothing works. Now what do I do?</br>
Answer:   Open a support ticket with [http://support.microsoft.com](http://support.microsoft.com). 



## Related Topics

[Avoid getting throttled or blocked in SharePoint Online](http://go.microsoft.com/fwlink/?LinkID=619858&amp;clcid=0x409)
  

