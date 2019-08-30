---
title: "Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state (SharePoint Server)"
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
ms.assetid: 85aa1c35-1322-42ad-a625-1496aee67858
description: "Learn how to resolve the SharePoint Health Analyzer rule: Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state, for SharePoint Server."
---

# Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state. 
  
 **Summary:** The databases are set to read-only and cannot be upgraded. 
  
 **Cause:** The databases are set to read-only. 
  
 **Resolution: Set the databases to read-write using SQL Server.**
  
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database. 
    
2. Start SQL Server Management Studio.
    
3. Right-click the content database that you want to make read-only, and then click **Properties**.
    
4. Select the **Options** page, and, in the **Other options** list, scroll to the **State** section. 
    
5. In the **Database Read-Only** row, click the arrow next to **True**, select **False**, and then click **OK**.
    
6. Repeat for all other content databases.
    
    > [!NOTE]
    > When a database is set to read-only, all connections except the one that is setting the read-only flag are stopped. After the read-only flag is set, other connections are enabled. 
  

