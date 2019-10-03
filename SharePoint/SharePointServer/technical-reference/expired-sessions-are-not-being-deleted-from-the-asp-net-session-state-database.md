---
title: "Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server)"
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
ms.assetid: 9983054b-ed90-491a-ac1d-cf95204f0931
description: "Learn how to resolve the SharePoint Health Analyzer rule: Expired sessions are not being deleted from the ASP.NET Session State database, for SharePoint Server."
---

# Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Expired sessions are not being deleted from the ASP.NET Session State database. 
  
 **Summary:** If expired sessions are not deleted, the server that hosts the ASP.NET Session State database may run out of disk space and the SharePoint farm may cease to function. 
  
 **Cause:** One or more of the following might be causing this: 
  
- The SQL Server Agent service was stopped.
    
- SQL Server Express is installed.
    
    > [!IMPORTANT]
    > You cannot run the SQL Server Agent service on an instance of SQL Server Express. 
  
**Resolution: Start the SQL Server Agent service**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the database server that is hosting the ASP.NET Session State database.
    
2. In **SQL Server Configuration Manger**, start the **SQL Server Agent service**.
    

