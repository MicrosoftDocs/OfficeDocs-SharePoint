---
title: "The paging file size should exceed the amount of physical RAM in the system (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: fb651b8b-5657-4686-b084-443016aba76c
description: "Learn how to resolve the SharePoint Health Analyzer rule: The paging file size should exceed the amount of physical RAM in the system, for SharePoint Server."
---

# The paging file size should exceed the amount of physical RAM in the system (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The paging file size should exceed the amount of physical RAM in the system. 
  
 **Summary:** The paging file size on some servers in the SharePoint farm is smaller than the total physical memory that is available on the servers. 
  
 **Cause:** A Windows best practice is to set the paging file size to equal to or greater than the total amount of available physical memory. Garbage collection is typically more effective at automatic recovery of heap memory when managed heap size approximates paging size. When paging file size is smaller than RAM size, new allocations of managed memory are granted, which leads to more garbage collection and higher CPU usage. 
  
 **Resolution: Increase the minimum size of the paging file**
  
1. Verify that you are a member of the Administrators group on the local computer.
    
2. In the **System Properties** dialog box, on the **Advanced** tab, in the **Performance** section, click **Settings**.
    
3. In the **Performance Options** dialog box, on the **Advanced** tab, in the **Virtual memory** section, click **Change**.
    
4. In the **Virtual Memory** dialog box, select the **Automatically manage paging file size for all drives** check box, or clear the check box and specify a paging file size that is equal to or greater than the physical memory that is available on the computer. We recommend that you either allow the system to manage the page file size or to set it at 150% of the size of the physical RAM. 
    
5. Click **OK**, and then restart the computer to apply the changes.
    

