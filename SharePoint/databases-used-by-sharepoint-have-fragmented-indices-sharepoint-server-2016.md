---
title: Databases used by SharePoint have fragmented indices (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 043481c0-f467-44ed-9772-d822eb314a81
---


# Databases used by SharePoint have fragmented indices (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Databases used by SharePoint have fragmented indices" for SharePoint Server 2016. **Rule Name:**   Databases used by SharePoint have fragmented indices. **Summary:**   SharePoint Server 2016 uses SQL Server to store most of the content for the Web site and configuration settings. One or more of the databases used by SharePoint Server have fragmented indexes. A fragmented index can cause a degrade in performance. **Cause:**   Database indexes can fragment over time as a result of insert and update operations performed by SharePoint Server 2016. We recommend that you periodically delete and rebuild these indexes to improve system performance. **Resolution: Reorganize and rebuild indexes**
1. To correct index fragmentation, you can reorganize an index or rebuild an index. For more information, see  [Reorganize and Rebuild Indexes](http://go.microsoft.com/fwlink/?LinkID=780583&amp;clcid=0x409).
    
  

