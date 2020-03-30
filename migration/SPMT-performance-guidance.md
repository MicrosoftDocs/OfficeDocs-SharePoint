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


## Recommendations possibility 

-	Improving the speed at which the source can be read will be most beneficial
-	Improving the migration machine speed will be most beneficial
-	Improving your connectivity to Azure/0365 will be most beneficial
-	[Performing migration following our published guidance will be most beneficial](https://docs.microsoft.com/sharepointmigration/sharepoint-online-and-onedrive-migration-speed)


Article for each recommendation

Improving the speed at which the source can be read 
When it comes to migration, the information needs to be read from a source and the speed at which that information can be one of bottleneck for your migration.
We recommend doing further test to understand which of the two is the actual bottleneck.
the local network speed (between the SPMT machine and the file server)
or
the performance of the file server itself.
Often, local network speed is the problem.
When the source is the migrating machine, it is suggested to stop other application which may compete the disk load for reading the data. In the same time, configuring the SPMT setting to change the working folder to a different physical disk (if there is) is also something worth trying.



Improving the migration machine speed
SPMT need a heavy load for data exchanging during the migration. So, the performance of the local disk of machine running the migration is important.
Suggestion: 
1.	Running the migration in a machine with better disk performance. It’s better to use a fast SSD. 
2.	The disk which hosts the SPMT working folder impacts the SPMT performance. If there are multi disks in the machine, make sure the working folder is setting to the disk with better performance. There is a setting item in SPMT to configure the working folder.
3.	Stop other applications which may put heave load of disk operations when doing the migration.

Improving your connectivity to 0365/Azure 
This is the speed of the network connection between the migration machine and Azure blob storage service. 
Suggestion: 
1.	Improve the bandwidth of the network access of the migration machine.
2.	Running the SPMT in a machine with fast network access
3.	Stop other application which may compete the network access with SPMT

Performing migration following our best practice 
Article that Annie created


