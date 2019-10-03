---
title: "Drives are at risk of running out of free space (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ac16bc32-f623-4658-8bc5-6e6b958629a4
description: "Learn how to resolve the SharePoint Health Analyzer rule: Drives are at risk of running out of free space, for SharePoint Server."
---

# Drives are at risk of running out of free space (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Drives are at risk of running out of free space. 
  
 **Summary:** This rule checks disk space as a proportion of the RAM that is installed on the SharePoint Server. Servers with large amounts of RAM are more likely to experience a failure of this rule. 
  
 **Cause:** When disk space is less than five times the RAM on the server, this health rule triggers a warning. For example, if your SharePoint Server has 16GB of RAM installed, the rule checks for 80GB of free space on the disk. 
  
 **Resolution: Free disk space on the server**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On Server Manager, click **Tools**, and then click **Disk Cleanup**.
    
**Resolution: Decrease the number of days to store log files**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.
    
3. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number. 
    
4. Click **OK**.
    

