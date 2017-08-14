---
title: Database has large amounts of unused space (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 18aeede1-07b9-43ee-88ee-602a7a5acfa6
---


# Database has large amounts of unused space (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Database has large amounts of unused space" for SharePoint Server 2016. **Rule Name:** Database has large amounts of unused space. **Summary:**   The database has large amounts of unused space allocated on the disk. This database uses a large amount of space on the file system unless it is shrunk down to a small size. This event occurs if the unused space is more than 20% of the disk space and the unused space is greater than the auto-growth size plus 50 megabytes (MB). **Cause:**   Many activities can create unused space in the database. These activities include running the Windows PowerShell **Move-SPSite** command, and deleting documents, document libraries, lists, list items, and sites. ** Resolution: Ignore this event, or shrink the database if you have to.**
- Normally you can safely ignore this event. You shrink a database only if it proves absolutely necessary — for example, when you have performed an operation that removes a very large quantity of data from a database, and the free space is not expected to be used again. You can shrink the database by using the DBCC ShrinkDatabase command or SQL Server Management Studio. For more information, see  [DBCC SHRINKDATABASE (Transact-SQL)](https://go.microsoft.com/fwlink/p/?LinkID=110852) (https://go.microsoft.com/fwlink/p/?LinkID=110852) and [Shrink a Database](http://go.microsoft.com/fwlink/?LinkID=760771&amp;clcid=0x409) (http://go.microsoft.com/fwlink/p/?LinkID=224904).
    
    The white paper  [Database maintenance for SharePoint](http://go.microsoft.com/fwlink/p/?LinkID=229104) provides very important guidelines for shrinking a database. We strongly recommend that you read this white paper before you shrink a database.
    
  

## 


