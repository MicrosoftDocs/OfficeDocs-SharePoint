---
title: "Set up and configure Access Services 2010 for web databases in SharePoint Server 2013"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f2d89390-aea4-4995-8b3f-b510c5d40247
description: "Learn how to use Access Services 2010 to modify and publish an Access web database in SharePoint Server 2013 that was previously created in SharePoint Server 2010."
---

# Set up and configure Access Services 2010 for web databases in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Access Services 2010 is a service application that allows users to modify and publish in SharePoint 2013 an Access web database that was previously created in SharePoint Server 2010. 
  
The Access client is not required to use the published web database. However, the Access client is required to make any changes to the database structure. 
  
    
## Set up SQL Server Reporting Services
<a name="section1"> </a>

You can update existing reports in an Access web database, but these reports require the installation and configuration of SQL Server Reporting Services Mode for SharePoint and the content database must be running SQL Server 2012. For more information, see [Install Reporting Services SharePoint Mode for SharePoint 2013](/sql/reporting-services/install-windows/install-the-first-report-server-in-sharepoint-mode?view=sql-server-2016) in SQL Server Books Online. 
  
## Start Access Database Service 2010
<a name="section2"> </a>

If for some reason Access Database Service 2010 has not been started, do the following:
  
1. On the SharePoint Central Administration website, under **System Settings**, click **Manage services on the server**.
    
2. On the same row as the **Access Database Service 2010** service, under **Action**, click **Start**.
    
## Create an Access Services 2010 service application
<a name="section3"> </a>

If for some reason an Access Services 2010 service application has not been created, do the following:
  
1. In Central Administration, under **Application Management**, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click **New**, and then click **Access Services 2010**.
    
3. In the **Access Services Application Name** section, type Access Services 2010 in the text box. 
    
4. Do one of the following:
    
  - Select the **Use existing application pool** option, and then select an **Application pool name** from the list. 
    
  - Select the **Create new application pool** option, and then type AccessServicesAppPool in the **Application pool name** text box. 
    
5. Select the **Configurable** option, and then from the drop-down list, select the Farm administrator account. 
    
6. Click **OK**.
    
## Configure Access Services 2010 settings
<a name="section4"> </a>

There are no additional settings required after the initial installation of Access Services 2010. The services are ready to use as soon as the SharePoint 2013 installation is complete. However, you can change the default configuration settings to suit your business need. The following table contains the configurable Access Services settings.
  
1. Verify that the user account that is performing this procedure is a site administrator for the Access Services 2010 service application and also has Designer permissions.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Access Services 2010 service application that you want to change.
    
4. On the Access Services 2010 settings page, change any of the settings shown in the following table.
    
|**Setting**|**Description**|
|:-----|:-----|
|**Lists and Queries** <br/> |**Settings for queries used against Microsoft SharePoint Foundation lists** <br/> |
|Maximum Columns per query  <br/> |The maximum number of columns that can be referenced in a query. Note that some columns may automatically be reference by the query engine and will be included in this limit.  <br/> Valid values: from 1 to 255  <br/> Default value: 40  <br/> |
|Maximum Rows per query  <br/> |The maximum number of rows that a list used in a query can have, or that the output of the query can have.  <br/> Valid values: from 1 to 200000  <br/> Default value: 25000  <br/> |
|Maximum Sources per query  <br/> |The maximum number of lists that may be used as input to one query.  <br/> Valid values: from 1 to 20  <br/> Default value: 12  <br/> |
|Maximum Calculated Columns per query  <br/> |The maximum number of inline calculated columns that can be included in a query, either in the query itself or in any sub-query on which it is based. Calculated columns in the underlying SharePoint Foundation list are not included.  <br/> Valid values: from 0 to 32  <br/> Default value: 10  <br/> |
|Maximum Order by Clauses per query  <br/> |The maximum number of Order By clauses in the query.  <br/> Valid values: from 0 to 8  <br/> Default value: 4  <br/> |
|Allow Outer Joins  <br/> |Allow left and right outer joins in a query. Inner Joins are always allowed.  <br/> Check box: selected or cleared for **Outer Joins allowed**.  <br/> |
|Allow Non Remote-able Queries  <br/> |Allow queries that cannot be remoted to the database tier to run.  <br/> Check box: selected or cleared for **Remotable Queries allowed**.  <br/> |
|Maximum Records Per Table  <br/> |The maximum number of records that a table in an application can contain.  <br/> Valid values: -1 (indicates no limit), any positive integer  <br/> Default value: 500000  <br/> |
|**Application Objects** <br/> |**Limitations on the types of objects an Access Services application can contain** <br/> |
|Maximum Application Log Size  <br/> |The maximum number of records for an Access Services Application Log list.  <br/> Valid values: -1 (indicates no limit), from 1 to any positive integer  <br/> Default value: 3000  <br/> |
|**Session Management** <br/> |**Behavior of Access Database Service sessions** <br/> |
|Maximum Request Duration  <br/> |The maximum duration (in seconds) allowed for a request from an application.  <br/> Valid values: -1 (indicates no limit), 1 through 2007360 (24 days)  <br/> Default value: 30  <br/> |
|Maximum Sessions Per User  <br/> |The maximum number of sessions allowed per anonymous user. If a user has this many sessions and starts a new session, the user's oldest session is deleted.  <br/> Valid values: -1 (no limit), from 1 to any positive integer  <br/> Default value: 10  <br/> |
|Maximum Sessions Per Anonymous User  <br/> |The maximum number of sessions allowed per user. If a user has this many sessions and starts a new session, the user's oldest session is deleted.  <br/> Valid values: -1 (no limit), from 1 to any positive integer  <br/> Default value: 25  <br/> |
|Cache Timeout  <br/> |The maximum time (in seconds) that a data cache can remain available, as measured from the end of each request for data in that cache.  <br/> Valid values: -1 (indicates no limit), 1 through 2007360 (24 days)  <br/> Default value: 1500  <br/> |
|Maximum Session Memory  <br/> |The maximum amount of memory (in MB) that a single session can use.  <br/> Valid values: 0 (disable) through 4095.  <br/> Default value: 64  <br/> |
|**Memory Utilization** <br/> |**Allocation of memory on Access Database Service** <br/> |
|Maximum Private Bytes  <br/> |The maximum number of private bytes (in MB) allocated by the Access Database Service process.  <br/> Valid values: -1 (the limit is set to 50% of physical memory on the computer), any positive integer  <br/> Default value: -1  <br/> |
|**Templates** <br/> |**Settings related to template management** <br/> |
|Maximum Template Size  <br/> |The maximum size (in MB) allowed for Access Templates (ACCDT).  <br/> Valid values: -1 (no limit), from 1 to any positive integer  <br/> Default value: 30  <br/> |
   
## See also
<a name="section4"> </a>

#### Concepts

[Set up and configure Access Services for Access apps in SharePoint Server 2013](set-up-and-configure-access-services-for-access-apps.md)

