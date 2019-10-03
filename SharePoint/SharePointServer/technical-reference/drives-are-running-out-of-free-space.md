---
title: "Drives are running out of free space (SharePoint Server)"
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
ms.assetid: 6ed5b73c-6403-46ea-9d56-f42d972e7748
description: "Learn how to resolve the SharePoint Health Analyzer rule: Drives are running out of free space, for SharePoint Server."
---

# Drives are running out of free space (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Drives are running out of free space. 
  
 **Summary:** Disk drives on one or more of the servers in the SharePoint Server farm are running out of disk space. 
  
> [!NOTE]
> This rule checks disk space as a proportion of the RAM that is installed on the computer. When disk space is less than twice the RAM on the computer, the health rule triggers an error. When disk space is less than five times the RAM on the server, the health rule triggers a warning. Servers with large amounts of RAM are more likely to experience a failure of this rule. 
  
 **Resolution: Free disk space on the server**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Server Manager, click **Tools**, and then click **Disk Cleanup**.
    
**Resolution: Decrease the number of days to store log files**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.
    
3. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number. 
    
4. Click **OK**.
    

