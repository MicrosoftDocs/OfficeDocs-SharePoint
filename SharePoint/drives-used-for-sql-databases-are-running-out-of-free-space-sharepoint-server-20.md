---
title: Drives used for SQL databases are running out of free space (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 24292545-0844-4eb0-9e80-7d4c9985755d
---


# Drives used for SQL databases are running out of free space (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Drives used for SQL databases are running out of free space" in SharePoint Server 2016. **Rule Name:** Drives used for SQL databases are running out of free space. **Summary:**  The databases have one or more files that exceed the available free disk drive space. If this happens, operations will fail. A disk drive should have enough free space to allow the largest database file to automatically grow to twice its size. **Cause:**   The databases have large files that may exceed the available free space. ** Resolution: Free disk space on the database server computer.**
1. Verify that the user account that is performing the following step is a member of the Administrators group on the local database server computer.
    
  
2. In **Server Manager**, click **Tools**, and then click **Defragment and Optimize Drives**.
    
  
3. Run the Optimize Drives tool to free disk space on the server computer.
    
  
4. If the event persists, move some large files to another disk drive to free up space.
    
  
 **Resolution:   Decrease the number of days to store log files.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group. 
    
  
2. On the Central Administration Home page, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.
    
  
4. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.
    
  
5. Click **OK**.
    
  

## 


