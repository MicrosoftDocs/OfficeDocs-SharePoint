---
title: "Use EffectiveUserName in PerformancePoint Services"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: bd5f42e5-81a9-47bc-a17e-1f9574324961
description: "Learn how to use the EffectiveUserName option when it connects to an Analysis Services data from PerformancePoint Services Dashboard Designer."
---

# Use EffectiveUserName in PerformancePoint Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

EffectiveUserName is a SQL Server Analysis Services connection string property that contains the name of the user who is accessing a report or dashboard. In SharePoint Server, you can use this property together with PerformancePoint Services to pass the identity of the user who is viewing the report or dashboard to SQL Server Analysis Services. This enables per-user identity without the requirement to configure Kerberos delegation. 
  
- [Scenario overview](use-effectiveusername-with-excel-services-sharepoint-server-2013.md#overview)
    
- [Before you begin](use-effectiveusername-with-excel-services-sharepoint-server-2013.md#begin)
    
- [Configure PerformancePoint Services Application Settings](use-effectiveusername-in-performancepoint-services.md#configure)
    
- [Configure Analysis Services access](use-effectiveusername-with-excel-services-sharepoint-server-2013.md#ConfigureASAccess)
    
- [Create and publish a report](use-effectiveusername-with-excel-services-sharepoint-server-2013.md#CreateAndPublish)
    
## Scenario overview
<a name="overview"> </a>

Using the EffectiveUserName feature with PerformancePoint Services allows the identity of a user viewing a report to be passed to SQL Server Analysis Services. 
  
Using the EffectiveUserName option allows for passing the user's identity to SQL Server Analysis Services without the requirement to configure Secure Store or Kerberos delegation.
  
## Before you begin
<a name="begin"> </a>

Before starting, confirm that you have met the software and permission requirements.
  
- You have PerformancePoint Services configured on your farm.
    
- You have Farm Administrator access to the SharePoint Server farm and administrator access to SQL Server Analysis Services.
    
## Configure PerformancePoint Services Application Settings
<a name="configure"> </a>

Using the EffectiveUserName feature with PerformancePoint Services requires the following:
  
- The PerformancePoint Services application pool account must be an Analysis Services Administrator.
    
- The EffectiveUserName option in must be enabled in the **PerformancePoint Service Application Settings**.
    
- You must select the **Per-user Identity** option when you create the data source in PerformancePoint Dashboard Designer. 
    
This setting applies to all Analysis Services data sources configured for per user authentication. When this setting is enabled, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation. 
  
 **To enable EffectiveUserName in PerformancePoint Services**
  
1. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. Click the PerformancePoint Services service application.
    
3. Click **PerformancePoint Service Application Settings**.
    
4. Select the **Use the EffectiveUserName connection string property instead of Windows delegation** check box. 
    
5. Click **OK**.
    
> [!NOTE]
> The EffectiveUserName feature does not work with Power Pivot data sources. 
  
> [!IMPORTANT]
> If you use a connection string to create the data connection, and the connection string contains an effective user field, the EffectiveUserName feature will override the user-supplied effective user value with the system-supplied value. 
  
## Configure Analysis Services access
<a name="configure"> </a>

If you do not know what account is running the PerformancePoint Services application pool in your farm, follow these steps to determine the account. If you know the account, skip this procedure.
  
 **To determine the PerformancePoint Services application pool account**
  
1. On the SharePoint Central Administration website home page, click **Security**.
    
2. On the Security page, under **General Security**, click **Configure service accounts**.
    
3. On the Service Account page, in the **Credential Management** section, from the drop-down list, select the application pool that runs PerformancePoint Services Application. 
    
    When this option is selected, the name of the service application appears in the box underneath the drop-down list. The account shown in the **Select an account for this component** drop-down list is the Windows identity that you need to add as an Analysis Services administrator. 
    
4. Click **Cancel**.
    
You must add the PerformancePoint Services application pool account as an Analysis Services administrator. Use the following procedure to add this account as an administrator in Analysis Services.
  
 **To add an Analysis Services administrator**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Right click the Analysis Services top node, and then click **Properties**.
    
3. On the **Security** page, click **Add**.
    
4. Type the name of the account that runs the PerformancePoint Services application pool, and then click **OK**.
    
5. Click **OK**.
    
## Connect to an Analysis Services data source from Dashboard Designer
<a name="section1"> </a>

You can connect to an Analysis Services data source either by entering the name of the Analysis Services server, database, and cube name, or by typing a connection string and the cube name in Dashboard Designer.
  
 **To connect to an Analysis Services data source with the EffectiveUserName option enabled**
  
1. start Dashboard Designer.
    
2. Click the **Create** tab, and then click **Data Source**.
    
3. In the Category pane of the **Select a Data Source Template** dialog box, click **Multidimensional** and then click **Analysis Services**. Click **OK**.
    
4. In the left navigation pane (workspace browser), type the name of your data source.
    
5. In the **Formatting Dimension** drop-down list, select desired dimension formatting needed for the report. 
    
6. In the **Cache Lifetime** drop-down box, type the refresh rate (in minutes) for the cache. Data from this data source will update at this interval. 
    
7. In the center pane, click the **Editor** tab. In the **Connection Settings** section, select the method by which to connect to the data source. To use a standard connection: 
    
1. Select **Use standard connection**
    
2. Type the full path for the server to which you want to connect. This populates the options in the database list.
    
3. In the **Database** box, select a database name. 
    
4. (Optional) In the **Roles** box, type the name of the role, such as an administrator or database role. To specify multiple roles, type the names of the roles and separate them with commas. 
    
5. From the **Cube** drop-down list, select the specific cube that you want to use as the data source in the database. 
    
8. In the **Data Source Settings** section, select **Per-user identity** as the method by which to authenticate to the data source. 
    
9. Click **Test Data Source** to confirm your connection is configured correctly. 
    

