---
title: Improving your SPMT performance
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to improved performance when using the SharePoint Migration Tool."
---
# Improving your migration performance when using SPMT

When using the SharePoint Migration Tool (SPMT), follow these guidelines to help improve your migration performance.

## Recommendations 

-	[Improving the speed at which the source can be read](#improving-the-speed-at-which-the-source-can-be-read)
-	[Improving the migration computer speed](#improving-the-migration-computer-speed)
-	[Improving your connectivity to 0ffice 365 and Azure](#improving-your-connectivity-to-0ffice-365-and-azure)
-	[Performing migration following our published guidance](https://docs.microsoft.com/sharepointmigration/sharepoint-online-and-onedrive-migration-speed)


## Improving the speed at which the source can be read 
During migration, information needs to be read from the source location. The speed at which that information can be read can impact your migration.  We recommend doing further testing to understand the actual bottleneck. 

The speed is usually impacted by either 
- The local network speed (between the computer or VM running SPMT and the file server, or 
- The performance of the file server itself.

Suggestions:

- Often local network speed is the problem. When the source content is located on the same computer or VM on which SPMT is running, stop other applications which may compete the disk load for reading the data. 
-  Change the SPMT working folder setting to point to a different physical disk (if there is one) on your computer or VM running SPMT.



## Improving the migration computer speed
SPMT executes a heavy load of data exchanging during the migration. Therefore the performance of the local disk of the computer or VM running SPMT is important.

Suggestions:
 
- Install and run SPMT on a computer with better disk performance, such as a fast SSD.   
- The disk which hosts the SPMT working folder impacts the SPMT performance. If there are multiple disks on the computer, configure SPMT working folder setting to point to the disk with the best performance. 
- Stop other applications which  creates a heavy load of disk operations when doing the migration.

## Improving your connectivity to 0ffice 365 and Azure 

The speed of the network connection between the computer running SPMT and the Azure blob storage service can impact your migration performance.  

Suggestions: 

- Improve the bandwidth of the network access of the computer running SPMT.
- Run SPMT on a computer with fast network access
- Stop other applications that may compete for network access with SPMT


## Performing migration following our best practice 

Migration performance can be impacted by network infrastructure, file size, migration time, and throttling. Understanding these will help you plan and maximize the efficiency of your migration. These are detailed here:

- [General guidelines for migration performance](https://docs.microsoft.com/sharepointmigration/sharepoint-online-and-onedrive-migration-speed)


