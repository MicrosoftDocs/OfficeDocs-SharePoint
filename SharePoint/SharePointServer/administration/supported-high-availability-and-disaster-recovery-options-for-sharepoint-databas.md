---
title: "Supported high availability and disaster recovery options for SharePoint databases"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: 94a0dfe4-66e8-4503-9cc6-cfb438f4fbc8
description: "Learn about supported high availability and disaster recovery options for each SharePoint Server system and service application database."
---

# Supported high availability and disaster recovery options for SharePoint databases

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes the supported high availability and disaster recovery options for SharePoint Server databases. For detailed information about these databases, such as size and supported backup and recovery tools, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md). 
  
    
## Introduction
<a name="Intro"> </a>

The scope of this article is the supported high availability and disaster recovery solutions for each SharePoint Server system and service application database. These solutions address the database level, instead of the database instance or database server level and include the following: database mirroring, database availability groups, and log shipping.
  
When you evaluate a high availability or a disaster recovery option for SharePoint, you must understand that not all of the options are supported by each SharePoint database. This is because of design requirements and feature characteristics.
  
This article identifies the supported option for each SharePoint database. These databases are grouped by SKU and then by feature.
  
## SharePoint Server system databases
<a name="SystemDBs"> </a>

The Configuration, Central Administration Content, and Content databases are the databases that are automatically installed when you deploy any SharePoint 2013 edition, and any SharePoint Server 2016 and SharePoint Server 2019 server roles using the MinRole feature. For more information, see [Description of MinRole and associated services in SharePoint Servers 2016 and 2019](description-of-minrole-and-associated-services-in-sharepoint-server-2016.md).
  
The following tables provide the supported high availability and disaster recovery options for the SharePoint system databases.
  
**Configuration database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |SharePoint_Config  <br/> |
|Purpose  <br/> |The configuration database contains data about SharePoint databases, Internet Information Services (IIS) web sites, web applications, Trusted solutions, Web Part packages, and Site templates.  <br/> The configuration database also contains specific data for SharePoint Server farm settings, such as default quota settings and blocked file types.  <br/> |
|Supports SQL Server 2014 with Service Pack 1 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No. This is a farm specific database.  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No. This is a farm specific database.  <br/> |
   
**Central Administration content database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |SharePoint_AdminContent_\<GUID\>  <br/> |
|Purpose  <br/> |This database stores all configuration data for the Central Administration site collection. If SQL Server 2016 RTM, Power Pivot for SharePoint Server 2016 or SQL Server 2012 Power Pivot for SharePoint 2013 is installed the Central Administration content database also stores the Excel Online and Excel worksheets and Power Pivot data files that are used in the Power Pivot Management Dashboard.  <br/> **Note:** Power Pivot for SharePoint Server 2016 is only available with SQL Server 2016 RTM.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No. This is a farm specific database.  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No. This is a farm specific database.  <br/> |
   
**Content database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |WSS_Content  <br/> |
|Purpose  <br/> |Content databases store all content for a site collection. This includes site documents or files in document libraries, list data, Web Part properties, audit logs, and some **apps for SharePoint data** if the apps are installed, in addition to user names and rights.  <br/> Content databases also store user data for SQL Server 2016 CTP 3.1 or later, Power Pivot for SharePoint Server 2016 and SQL Server 2012 Power Pivot for SharePoint 2013, if you installed it in your SharePoint Server environment. Additionally Content databases also store the Project Server 2016 extensions in SharePoint Server 2016.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
## SharePoint Servers 2016 and 2019 service application databases
<a name="SAppDBsSPALL"> </a>

All SharePoint Servers 2016 and 2019 service applications store specific data and objects in either a unique database or a system database. These databases are created to support features that are used in SharePoint Server 2016 and 2019 farms.
  
The following sections describe the supported high availability and disaster recovery options for SharePoint Server 2016 and 2019 service application databases.
  
### App Management service application

The following table provides the supported high availability and disaster recovery options for the App Management database.
  
**App Management database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** AppMng_Service_DB_\<GUID\>  <br/> **2013:** AppManagement  <br/> |
|Purpose  <br/> |Stores app licenses and permissions that are downloaded from the SharePoint Store or App Catalog.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Business Data Connectivity service database

The following table describes the supported high availability and disaster recovery options for the Business Data Connectivity database.
  
**Business Data Connectivity service database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Bdc_Service_DB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores external content types and related objects.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Managed Metadata Service database

The following table describes the supported high availability and disaster recovery options for the Managed Metadata Service database.
  
**Managed Metadata Service database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** Managed Metadata Service_\<GUID\>  <br/> **2013:** Managed Metadata Service Application_Metadata_\<GUID\>  <br/> |
|Purpose  <br/> |Stores managed metadata and syndicated content types.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
> [!NOTE]
> The Managed Metadata Service is the Taxonomy service. This database cannot be attached to a Managed Metadata Service Application in read only mode.
  
### PerformancePoint Services database

The following table describes the supported high availability and disaster recovery options for the PerformancePoint Services database.
  
**PerformancePoint Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** PerformancePoint Service Application_\<GUID\>  <br/> **2013:** PerformancePoint Service_\<GUID\>  <br/> |
|Purpose  <br/> |Stores temporary objects and saved user comments and settings.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Power Pivot Service database

The following table describes the supported high availability and disaster recovery options for the Power Pivot Service database.
  
> [!NOTE]
> Power Pivot for SharePoint Server 2016 is only available with SQL Server 2016 CTP 3.1 or later. 
  
> [!NOTE]
> Power Pivot for SharePoint 2013 is only available with SQL Server 2012 SP1 Analysis Services (SSAS). 
  
**Power Pivot Service database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the Power Pivot for SharePoint Configuration Tool  <br/> |DefaultPowerPivotServiceApplicationDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores data refresh schedules, and workbook usage data for internal use by Power Pivot service applications.  <br/> |
|Supports SQL Server 2016 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes, but not recommended. Use AlwaysOn in Synchronous-Commit Mode instead.  <br/> |
|Supports SQL Server AlwaysOn Availability Group in Synchronous-Commit Mode for availability  <br/> |Yes, recommended.  <br/> |
|Supports SQL Server 2016 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Project Server database

> [!IMPORTANT]
> The Project Server service application database is only found in SharePoint Server 2013. Project Servers 2016 and 2019 don't create a database for SharePoint Servers 2016 and 2019 but use the Content database (WSS_Content). 
  
The following table describes the supported high availability and disaster recovery options for the Project Server database.
  
> [!NOTE]
> Project Server creates a separate database for each instance of Project Web App 
  
**Project Server database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |ProjectWebApp  <br/> |
|Purpose  <br/> | Each Project Web App database contains the following data:  <br/>  All Project and Portfolio Management (PPM) data  <br/>  Time tracking and Timesheet data  <br/>  Aggregated SharePoint project site data  <br/> |
|Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### SharePoint Search service databases

The SharePoint Search service application uses the following databases: 
  
- Search Administration
    
- Analytics Reporting
    
- Crawl
    
- Link
    
The following tables provide the supported high availability and disaster recovery options for the Search databases.
  
**Search Administration database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_DB_\<GUID\>  <br/> |
|Purpose  <br/> | Stores the Search application configuration and system access control list (SACL) for the crawl component.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No. Taking a copy of the Search Administration database and using it to re-create the Search service application is supported.  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No. Taking a copy of the Search Administration database and using it to re-create the Search service application is supported.  <br/> |
   
**Analytics Reporting database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_AnalyticsReportingStoreDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores the results for usage analysis reports and extracts information from the Link database when it is needed.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No  <br/> |
   
**Crawl database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_CrawlStoreDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores the state of the crawled data and the crawl history.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No  <br/> |
   
**Link database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Search_Service_Application_LinkStoreDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores the information that is extracted by the content processing component and click through information.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No  <br/> |
   
### Secure Store database

The following table provides the supported high availability and disaster recovery options for the Secure Store database.
  
**Secure Store database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |Secure_Store_Service_DB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores and maps credentials, such as account names and passwords.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### SharePoint Translation Services database

The following table describes the supported high availability and disaster recovery options for the Translation Services database.
  
**Translation Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** TranslationService_\<GUID\>  <br/> **2013:** SharePoint Translation Services_\<GUID\>  <br/> |
|Purpose  <br/> |Stores information about pending and completed batch document translations with enabled file name extensions.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### State Service database

The following table describes the supported high availability and disaster recovery options for the State Service database.
  
**State Service database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** StateService_\<GUID\>  <br/> **2013:** SessionStateService_\<GUID\>  <br/> |
|Purpose  <br/> |Stores temporary state information for InfoPath Forms Services, Exchange Server, the chart Web Part, and Visio Services.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |No  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No  <br/> |
   
### Subscription Settings service application

The following table provides the supported high availability and disaster recovery options for the Subscription Settings service application database.
  
**Subscription Settings database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2019:** Subscription  <br/> **2013/2016:** SettingsServiceDB  <br/> |
|Purpose  <br/> |Stores features and settings for hosted customers.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Usage and Health Data Collection database

The following table provides the supported high availability and disaster recovery options for the Usage and Health Data Collection database.
  
**Usage and Health Data Collection database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |**2016/2019:** WSS_Logging  <br/> **2013:** SharePoint_Logging  <br/> |
|Purpose  <br/> |Stores health monitoring and usage data temporarily, and can be used for reporting and diagnostics.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes, but not recommended  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> **Note:** It is not possible to run PSConfig, (SharePoint Products Configuration Wizard or Microsoft PowerShell) to apply SharePoint CUs when this database is a member of an Always On Availability Group.  <br/> |Yes, but not recommended  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes, but not recommended  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |No. This database is farm specific. However, you can copy it to a disaster recovery environment for data mining.  <br/> |
   
### User Profile Service databases

The User Profile Service application uses the following databases:
  
- Profile: The Profile database stores and manages users and associated information. It also stores information about a user's social network in addition to memberships in distribution lists and sites.
    
- Synchronization: The Synchronization database stores configuration and staging data for use when profile data is being synchronized with directory services such as Active Directory.
    
- Social Tagging: The Social Tagging database stores social tags and notes created by users, alongside their respective URLs.
    
The following tables describe the supported high availability and disaster recovery options for the User Profile service application databases.
  
**Profile database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_ProfileDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores and manages users and their associated information. It also stores information about a user's social network in addition to memberships in distribution lists and sites.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
**Synchronization database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_SyncDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores configuration and staging data for use when profile data is synchronized with directory services such as Active Directory.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
**Social Tagging database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |User Profile Service Application_SocialDB_\<GUID\>  <br/> |
|Purpose  <br/> |Stores social tags and notes created by users, alongside their respective URLs.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
### Word Automation Services database

The following table describes the supported high availability and disaster recovery options for the Word Automation Services database.
  
**Word Automation Services database**

|**Category**|**Description**|
|:-----|:-----|
|Default database name when it is installed with the SharePoint Products Configuration Wizard  <br/> |WordAutomationServices_\<GUID\>  <br/> |
|Purpose  <br/> |Stores information about pending and completed document conversions.  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM synchronous mirroring in a farm for availability  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 synchronous mirroring in a farm for availability  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with synchronous-commit for availability  <br/> |Yes  <br/> |
|Supports SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> Supports SQL Server 2008 R2 and SQL Server 2012 asynchronous mirroring or log-shipping to another farm for disaster recovery  <br/> |Yes  <br/> |
|Supports SQL Server AlwaysOn Availability Group with asynchronous-commit for disaster recovery  <br/> |Yes  <br/> |
   
## SQL Server System databases
<a name="SQLSysDbs"> </a>

SharePoint Server is built on SQL Server and uses the following SQL Server system databases: master, msdb, model, Resource, and tempdb. SQL Server provides a complete set of administrative tools that let users fully administer their system and manage all users and objects in a database. For more information about the SQL Server system databases, see [System Databases](http://go.microsoft.com/fwlink/?LinkID=733887&amp;clcid=0x409).
  
You can only mirror user databases, put them in a SQL Server AlwaysOn availability group or log ship them. You can't use these approaches to provide high availability or disaster recovery for the system databases.
  
## SQL Server Reporting Services databases
<a name="SQLRSDbs"> </a>

The following SQL Server Reporting Services databases can be used as part of a SharePoint Server deployment:
  
- Report Server Catalog (ReportingService_\<GUID\>) - Stores all report metadata including report definitions, report history and snapshots, and scheduling information. 
    
    > [!NOTE]
    > When Report Server Catalog is used, report documents are stored in SharePoint content databases. 
  
- ReportServerTempDB (ReportingService_\<GUID\>_TempDB) - Stores all the temporary snapshots while reports are running.
    
- Report Server Alerting (ReportingService_\<GUID\>_Alerting) - Stores all Data Alerts and runtime information.
    
A Reporting Services report server is a stateless server that stores application data, content, properties, and session information in two SQL Server relational databases. The best way to ensure the availability of Reporting Services functionality is to do the following:
  
- Use the high availability features of the SQL Server Database Engine to maximize the uptime of the report server databases. If you configure a Database Engine instance to run in a failover cluster, you can select that instance when you create a report server database.
    
- Use SQL Server AlwaysOn Availability Groups with the Reporting Services databases and for data sources where applicable.
    
- Configure multiple report servers to run in a scale-out deployment, where all the servers share a single report server database. Deploying multiple report server instances on different servers can help increase the level of uninterrupted service.
    
## See also
<a name="SQLRSDbs"> </a>

#### Concepts

[Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md)
#### Other Resources

[AlwaysOn Availability Groups (SQL Server): Interoperability and Coexistence with Other Database Engine Features](https://go.microsoft.com/fwlink/p/?LinkId=272808)
  
[Database Mirroring: Interoperability and Coexistence](https://msdn.microsoft.com/library/bb500117%28v=sql.120%29.aspx)

