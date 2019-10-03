---
title: "Database has large amounts of unused space (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/28/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 18aeede1-07b9-43ee-88ee-602a7a5acfa6
description: "Learn how to resolve the SharePoint Health Analyzer rule: Database has large amounts of unused space, for SharePoint Server."
---

# Database has large amounts of unused space (SharePoint Server)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
>[!IMPORTANT]
>This health analyzer rule only applies to SharePoint 2010 as this was removed in [KB4011601](https://support.microsoft.com/help/4011601) for SharePoint Server 2013 and [KB4011576](https://support.microsoft.com/help/4011576) for SharePoint Server 2016.

 **Rule Name:** Database has large amounts of unused space. 
  
 **Summary:** The database has large amounts of unused space allocated on the disk. This database uses a large amount of space on the file system unless it is shrunk down to a small size. This event occurs if the unused space is more than 20% of the disk space and the unused space is greater than the auto-growth size plus 50 megabytes (MB). 
  
 **Cause:** Many activities can create unused space in the database. These activities include running the Windows PowerShell [Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps) command, and deleting documents, document libraries, lists, list items, and sites. 
  
 **Resolution: Ignore this event, or shrink the database if you have to.**
  
- Normally you can safely ignore this event. You shrink a database only if it proves absolutely necessary — for example, when you have performed an operation that removes a very large quantity of data from a database, and the free space is not expected to be used again. You can shrink the database by using the DBCC ShrinkDatabase command or SQL Server Management Studio. For more information, see [DBCC SHRINKDATABASE (Transact-SQL)](https://go.microsoft.com/fwlink/p/?LinkID=110852) (https://go.microsoft.com/fwlink/p/?LinkID=110852) and [Shrink a Database](http://go.microsoft.com/fwlink/?LinkID=760771&amp;clcid=0x409) (http://go.microsoft.com/fwlink/p/?LinkID=224904). 
    
    The white paper [Database maintenance for SharePoint](http://go.microsoft.com/fwlink/p/?LinkID=229104) provides very important guidelines for shrinking a database. We strongly recommend that you read this white paper before you shrink a database. 
    
## See also

#### Other Resources

[Shrinking a Database](http://go.microsoft.com/fwlink/p/?LinkID=127459)

