---
title: "Optimize performance for SharePoint Server 2013"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 8/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 4e01d36b-34a2-4e34-a785-9c2366de2a5b
description: "Learn about the techniques and tools available for optimizing SharePoint Server 2013 performance."
---

# Optimize performance for SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]

Learn about the techniques and tools available for optimizing SharePoint Server 2013 performance.
  
This article provides information about techniques and tools for optimizing SharePoint Server 2013 performance.
  
## Optimizing performance

There are many technologies and techniques available to optimize SharePoint Server 2013 performance. In a given environment, some or all of these techniques may apply. 
  
### Using BranchCache to optimize WAN performance

BranchCache is a feature of the Windows 7, Windows 8, Windows Server 2008 R2 and Windows Server 2012 operating systems that caches content from file and web servers on a wide area network (WAN) on computers at a local branch office. In a geographically distributed SharePoint Server 2013 environment, BranchCache can optimize WAN performance by caching large files that users download from SharePoint Server 2013. 
  
After you install and configure BranchCache, a computer on the branch office network caches files that branch office users download from SharePoint Server 2013. BranchCache also stores file version metadata when the following Office applications access files:
  
- OneNote
    
- Word 
    
- Excel 
    
- Visio 
    
- PowerPoint 
    
Every time a branch office user requests a cached file from SharePoint Server 2013, BranchCache checks to see if a more recent file exists on the server. If not, BranchCache will serve the cached version of the file.
  
For more information about BranchCache, see the following resources: 
  
    
- [BranchCache Overview](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831696(v=ws.11)) for Windows 8 and Windows Server 2012 
    
- [BranchCache Overview](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd996634(v=ws.10)) for Windows 7 and Windows Server 2008 R2 
    
- [BranchCache Deployment Guide](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj572990(v=ws.11)) for Windows 8 and Windows Server 2012 
    
- [BranchCache Deployment Guide](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee649232(v=ws.10)) for Windows 7 and Windows Server 2008 R2 
    
#### Configuring BranchCache for use with SharePoint Server 2013

This section describes how to install and configure BranchCache for use with SharePoint Server 2013. 
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - You must be logged in as a farm administrator to enable BranchCache for SharePoint Server 2013.
    
  - You must be logged in as a domain administrator or local computer administrator to install and enable BranchCache on a Windows 7 or Windows Server computer.
    
2. Deploy BranchCache on each web server in your SharePoint Server 2013 farm by following the instructions in the following topics:
    
  - For Windows Server 2012, see [Install Content Servers that Use the BranchCache Feature](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj572976(v=ws.11)).
    
  - For Windows Server 2008 R2, see [Install content servers that use the BranchCache feature](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee649269(v=ws.10)).
    
3. Deploy BranchCache in your branch office network environment by following the instructions in the following topics:
    
  - For Windows 8 and Windows Server 2012, see the [BranchCache Deployment Guide](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj572990(v=ws.11)).
    
  - For Windows 7 and Windows Server 2008 R2, see the [BranchCache Deployment Guide](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee649232(v=ws.10))
    
4. If you have deployed BranchCache in Distributed mode, and the AuthNoEncap policy is enabled in your environment, you must install the update described in [Performance issue when you enable the AuthNoEncap policy to handle large payloads in a network environment in Windows 7 or in Windows Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkId=263618) on all Windows 7 client computers. 
    
After you have installed and configured BranchCache in the operating system of each web server in your SharePoint Server 2016 farm and each computer in your branch office, content in SharePoint Server 2013 will be cached automatically, and no further configuration is required.
  
## See also

#### Concepts

[Performance planning in SharePoint Server 2013](performance-planning-in-sharepoint-server-2013.md)
#### Other Resources

[Plan for SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261834(v=office.14))

