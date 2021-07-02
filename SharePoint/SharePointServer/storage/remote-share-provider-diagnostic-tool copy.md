---
title: "Remote Share Provider"
ms.reviewer: 
ms.author: v-satapathy
manager: nimishasatapathy
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how the new PowerShell cmdlet helps admin to validate the data consistency of content database that is remote share provider enabled. This makes it easier for admin to figure out what are the problems in the remote storage."
---

# Remote Share Provider Overview

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

While there are more and more contents accumulating inside SharePoint, the storage requirement is also increasing. And, this increases when organization is using SharePoint for sharing rich contents rather than normal documents. Administrators need to either regularly review and clean up contents inside SharePoint.
By default, all the contents in SharePoint Server are stored in content databases in attached SQL server. Inside content databases, there are either structured data, such as meta data or unstructured data, such as files. Unstructured data in SharePoint are stored in content database as Binary Large Object (BLOB) and they are immutable.

From SharePoint 2013, Remote BLOB Storage (RBS) was created in SQL server to offload BLOBs from content database. SharePoint server supports both FILESTREAM provider.
SharePoint v.Next provides a reasonable and easy to use storage solution to the IT administrators to lower down the overall cost of SharePoint deployment in on-premise environment.

In this new generation of SharePoint server, we provide a new RBS provider -"Remote Share Provider".
  
You must perform the following tasks to configure remote share provider:
- This provider is built in SharePoint, hence no additional installation process is needed as compared to FILESTREAM provider.
- This provider supports offload Binary Large Object (BLOB) storage to remote SMB system and totally enables content database storage in SQL server side. Therefore, with the same amount of limitation of content database, as in 200GB size, more file volumes can be stored in one content database. Hence, it helps not only to reduce the cost for storage but also for the maintenance.
- There is no diagnostic PS cmdlet to check the data completeness to figure out storage problem.'
- By leveraging the existing backup and restore methodology of SMB system, it provides relatively reasonable disaster recover.

To know how to use remote share provider, see "Remote Share Provider User Guide.docx"

  
