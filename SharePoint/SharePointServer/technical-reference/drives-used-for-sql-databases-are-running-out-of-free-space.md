---
title: "Drives used for SQL databases are running out of free space (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/29/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 24292545-0844-4eb0-9e80-7d4c9985755d
description: "Learn how to resolve the SharePoint Health Analyzer rule: Drives used for SQL databases are running out of free space, for SharePoint Server."
---

# Drives used for SQL databases are running out of free space (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Drives used for SQL databases are running out of free space. 
  
 **Summary:** The databases have one or more files that exceed the available free disk drive space. If this happens, operations will fail. A disk drive should have enough free space to allow the largest database file to automatically grow to twice its size. 
  
 **Cause:** The databases have large files that may exceed the available free space. 
  
 **Resolution: Free disk space on the database server computer.**
  
1. Verify that the user account that is performing the following step is a member of the Administrators group on the local database server computer.
    
2. In **Server Manager**, click **Tools**, and then click **Defragment and Optimize Drives**.
    
3. Run the Optimize Drives tool to free disk space on the server computer.
    
4. If the event persists, move some large files to another disk drive to free up space.
    
**Resolution: Decrease the number of days to store log files.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group. 
    
2. On the Central Administration Home page, click **Monitoring**.
    
3. On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.
    
4. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number. 
    
5. Click **OK**.
    

