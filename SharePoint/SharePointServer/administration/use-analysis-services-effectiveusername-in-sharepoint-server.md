---
title: "Use Analysis Services EffectiveUserName in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: c3802be8-9c57-4b25-9666-c07b485aabf0
description: "Use the EffectiveUserName option in Excel Services or PerformancePoint Services for per-user authentication with Analysis Services data sources."
---

# Use Analysis Services EffectiveUserName in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
EffectiveUserName is a SQL Server Analysis Services connection string property that contains the name of the user who is accessing a report or dashboard. In SharePoint Server, you can use this property in conjunction with Excel Services or PerformancePoint Services to pass the identity of the user who is viewing the report or dashboard to SQL Server Analysis Services. This allows per-user identity without the need to configure Kerberos delegation. 
  
## Enable EffectiveUserName in Excel Services in SharePoint Server 2013

Using the EffectiveUserName feature with Excel Services requires the following:
  
- The Excel Services application pool account must be an Analysis Services Administrator.
    
- You must enable the EffectiveUserName option in Excel Services Global Settings.
    
- You must select the **Use the authenticated user's account** option in the Excel Services Authentication Settings in Excel. 
    
Use the following procedure to enable the EffectiveUserName feature in Excel Services.
  
 **To enable EffectiveUserName in Excel Services**
  
1. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Excel Services service application.
    
3. Click **Global Settings**.
    
4. On the Excel Services Application Settings page, in the **External Data** section, select the **Use the EffectiveUserName property** check box. 
    
5. Click **OK**.
    
For a more detailed look at using EffectiveUserName in Excel Services, see [Use EffectiveUserName with Excel Services (SharePoint Server 2013)](use-effectiveusername-with-excel-services-sharepoint-server-2013.md).
  
## Enable EffectiveUserName in PerformancePoint Services

Using the EffectiveUserName feature with PerformancePoint Services requires the following:
  
- The PerformancePoint Services application pool account must be an Analysis Services Administrator.
    
- You must enable the EffectiveUserName option in PerformancePoint Service Application Settings.
    
- You must select the **Per-user Identity** option when you create the data source in PerformancePoint Dashboard Designer. 
    
> [!NOTE]
> The EffectiveUserName feature does not work in conjunction with Power Pivot data sources. 
  
> [!NOTE]
> If you use a connection string to create the data connection, and the connection string contains an effective user field, the EffectiveUserName feature will override the user-supplied effective user value with the system-supplied value. 
  
Use the following procedure to enable the EffectiveUserName feature in PerformancePoint Services.
  
 **To enable EffectiveUserName in PerformancePoint Services**
  
1. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. Click the PerformancePoint Services service application.
    
3. Click **PerformancePoint Service Application Settings**.
    
4. On the PerformancePoint Service Application Settings page, select the **Use the EffectiveUserName connection string property instead of Windows delegation** check box. 
    
5. Click **OK**.
    
For a more detailed look at using EffectiveUserName in PerformancePoint Services, see [Use EffectiveUserName in PerformancePoint Services](use-effectiveusername-in-performancepoint-services.md).
  

