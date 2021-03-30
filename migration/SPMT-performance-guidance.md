---
title: Improve SPMT or Migration Manager agent performance
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to improve performance when using the SharePoint Migration Tool or the Migration Manager agent."
---
# Improve migration performance when using SPMT or Migration Manager

When using either the SharePoint Migration Tool (SPMT) or running a Migration Manager agent, follow these guidelines to help improve your migration performance.

>[!Note]
>For simplicity,for the remainder of this article, SPMT and the Migration Manager agent will be referred to as the "*migration computer*".

## Recommendations 

-	[Improving the speed at which the source can be read](#improving-the-speed-at-which-the-source-can-be-read)
-	[Improving the migration computer speed](#improving-the-migration-computer-speed)
-	[Improving your connectivity to Microsoft 365 and Azure](#improving-your-connectivity-to-microsoft-365-and-azure)
-	[Performing migration following our published guidance](sharepoint-online-and-onedrive-migration-speed.md)


## Improving the speed at which the source can be read 
During migration, information needs to be read from the source location. The speed at which that information can be read can impact your migration.  We recommend doing further testing to understand the actual bottleneck. 

The speed is usually impacted by either 
- The local network speed between the migration computer and the file server, or 
- The performance of the file server itself.

Suggestions:

- Often local network speed is the problem. When the source content is located on the same computer or VM as the migration computer, stop other applications that may compete with the disk load for reading the data. 
-  Change the working folder setting to point to a different physical disk (if there is one) on your migration computer.



## Improving the migration computer speed
A heavy load of data is exchanged during migration, so the performance of the local disk of the migration computer is important.

Suggestions:
 
- Install and run the migration tool on a computer with better disk performance, such as a fast SSD.   
- The disk that hosts the migration working folder impacts migration performance. If there are multiple disks on the computer, configure the working folder setting to point to the disk with the best performance. 
- Stop other applications that create a heavy load of disk operations when doing the migration.

## Improving your connectivity to Microsoft 365 and Azure 

The speed of the network connection between the migration computer and the Azure blob storage service can impact your migration performance.  

Suggestions: 

- Improve the bandwidth of the network access of the migration computer.
- Use a computer with fast network access as your migration computer
- Stop other applications that may compete for network access with the migration computer.


## Performing migration following our best practice 

Migration performance can be impacted by network infrastructure, file size, migration time, and throttling. Understanding these will help you plan and maximize the efficiency of your migration. These are detailed here:

- [General guidelines for migration performance](sharepoint-online-and-onedrive-migration-speed.md)