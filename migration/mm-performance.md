---
title: Improving your Migration Manager performance
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "How to improve performance when using Migration Manager."
---

# Improving your migration performance when using Migration Manager

There are four general areas to examine when trying to improve performance when using Migration Manager.  Migration Manager will detect an area that needs improvement and direct you to guidance to make adjustments.

The concept of "score" as it relates to performance is only available in the SharePoint Migration Tool (SPMT), and is not part of Migration Manager.  Instead, Migration Manager identifies one or more specific areas for improvement so you can more effectively refine your efforts to improve performance.

## Recommendations

- [Improving the speed at which the source can be read](#improving-the-speed-at-which-the-source-can-be-read)
- [Improving the migration computer speed](#improving-the-migration-computer-speed)
- [Improving your connectivity to Office 365 and Azure](#improving-your-connectivity-to-office-365-and-azure)
- [Performing migration following our published guidance](./sharepoint-online-and-onedrive-migration-speed.md)

## Improving the speed at which the source can be read

During migration, information needs to be read from the source location. The speed at which that information can be read can impact your migration.  We recommend doing further testing to understand the actual bottleneck.

The speed is usually impacted by either

- The local network speed (between the computer or VM running the Migration Manager agent and the file server, or
- The performance of the file server itself.

Suggestions:

- Often local network speed is the problem. When the source content is located on the same computer or VM on which Migration Manager agent is running, stop other applications which may compete the disk load for reading the data.

## Improving the migration computer speed

Migration Manager executes a heavy load of data exchanging during the migration. Therefore the performance of the local disk of the computer or VM running the Migration Manager agent is important.

Suggestions:

- Install and run the migration agent on a computer with better disk performance, such as a fast SSD.
- Stop other applications which  creates a heavy load of disk operations when doing the migration.

## Improving your connectivity to Office 365 and Azure

The speed of the network connection between the computer running Migration Manager and the Azure blob storage service can impact your migration performance.

Suggestions:

- Improve the bandwidth of the network access of the computer running the Migration Manager agent.
- Run the Migration Manager agent on a computer with fast network access
- Stop other applications that may compete for network access with Migration Manager

## Performing migration following our best practice

Migration performance can be impacted by network infrastructure, file size, migration time, and throttling. Understanding these will help you plan and maximize the efficiency of your migration. These are detailed here:

- [General guidelines for migration performance](./sharepoint-online-and-onedrive-migration-speed.md)
