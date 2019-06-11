---
title: "Account permissions and security settings in SharePoint Servers 2013, 2016 and 2019"
ms.reviewer: 
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.date: 9/8/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 55b99d80-3fa7-49f0-bdf4-adb5aa959019
description: "Learn about the permissions and security settings to use with a deployment of SharePoint Server."
---

# Account permissions and security settings in SharePoint Servers 2013, 2016 and 2019

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

This article describes SharePoint administrative and services account permissions for the following areas: Microsoft SQL Server, the file system, file shares, and registry entries.

> [!IMPORTANT]
> Do not use service account names that contain the symbol $.

## SharePoint Server account recommendations

> [!NOTE]
> For recommendations on SharePoint Server accounts, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md)

## SharePoint administrative accounts
<a name="Section1"> </a>

One of the following SharePoint components automatically configures most of the SharePoint administrative account permissions during the setup process:

- The SharePoint Products Configuration Wizard (Psconfig).

- The Farm Configuration Wizard.

- The SharePoint Central Administration website.

- Microsoft PowerShell.

### SharePoint Farm Administrator account

This account is used to set up each server in your farm by running the SharePoint Products Configuration Wizard, the initial Farm Configuration Wizard, and PowerShell. For the examples in this article, the SharePoint Farm Administrator account is used for farm administration, and you can use Central Administration to manage it. Some configuration options, for example, configuration of the SharePoint Server Search query server, require local administration permissions. The SharePoint Farm Administrator account requires the following permissions:

- It must have domain user account permissions.

- It must be a member of the local administrators group on each server in the SharePoint farm.

- This account must have access to the SharePoint databases.

- If you use any PowerShell operations that affect a database, the SharePoint Farm Administrator account must be a member of the *db_owner* role.

- This account must be assigned to the *securityadmin* and *dbcreator* SQL Server security roles during setup and configuration.

> [!NOTE]
> The *securityadmin* and *dbcreator* SQL Server security roles might be required for this account during a complete version-to-version upgrade because new databases might have to be created and secured for services.

After you run the configuration wizards, machine-level permissions for the SharePoint Farm Administrator account include:

- Membership in the *WSS_ADMIN_WPG* Windows security group.

- Membership in the IIS_WPG role. (SP2013)


After you run the configuration wizards, database permissions include:

- *db_owner* on the SharePoint server farm configuration database.

- *db_owner* on the SharePoint Central Administration content database.

> [!CAUTION]
> If the account that you use to run the configuration wizards does not have the appropriate special SQL Server role membership or access as *db_owner* on the databases, the configuration wizards will not run correctly.

### SharePoint Farm Service account

The SharePoint Farm service account, which is also referred to as the database access account, is used as the application pool identity for Central Administration and as the process account for the SharePoint Timer Service. The server farm account requires the following permissions:

- It must have domain user account permissions.

Additional permissions are automatically granted to the SharePoint Farm Service account on SharePoint servers that are joined to a server farm.

After you run Setup, machine-level permissions include:

- Membership in the *WSS_ADMIN_WPG* Windows security group for the SharePoint Timer Service.

- Membership in *WSS_RESTRICTED_WPG* for the Central Administration and Timer service application pools.

- Membership in *WSS_WPG* for the Central Administration application pool.

After you run the configuration wizards, SQL Server and database permissions include:

- *Dbcreator* fixed server role.

- *Securityadmin* fixed server role.

- *db_owner* for all SharePoint databases.

- Membership in the *WSS_CONTENT_APPLICATION_POOLS* role for the SharePoint server farm configuration database.

- Membership in the *WSS_CONTENT_APPLICATION_POOLS* role for the SharePoint_Admin content database.

## SharePoint Application Pool accounts
<a name="Section2"> </a>

This section describes the SharePoint Application Pool accounts that are set up by default during installation.

### Default content access account

The default content access account is used within a specific service application to crawl content, unless a different authentication method is specified by a crawl rule for a URL or URL pattern. This account requires the following permission configuration settings:

- The default content access account must be a domain user account that has read access to external or secure content sources that you want to crawl by using this account.

- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites.

- This account must not be a member of the Farm Administrators group.

### Content access accounts

Content access accounts are configured to access content by using the Search administration crawl rules feature. This type of account is optional, and you can configure it when you create a new crawl rule. For example, external content (such as a file share) might require this separate content access account. This account requires the following permission configuration settings:

- The content access account must have read access to external or secure content sources that this account is configured to access.

- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites.

### Excel Services unattended service account

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2013 only. Excel Services are deprecated in SharePoint Server 2016. 
  
Excel Services uses the Excel Services unattended service account to connect to external data sources that require a user name and password that are based on operating systems other than Windows for authentication. If this account is not configured, Excel Services will not attempt to connect to these types of data sources. Although account credentials are used to connect to data sources of operating systems other than Windows, if the account is not a member of the domain, Excel Services cannot access them. This account must be a domain user account.
  

### Web Application Pool account

The Web Application Pool account must be a domain user account. This account must not be a member of the Farm Administrators group.

This account should b used for all web applications without Central Administration.

The following machine-level permission is configured automatically: This account is a member of *WSS_WPG*.

The following SQL Server and database permissions are configured automatically:

- This account is assigned to the *WSS_CONTENT_APPLICATION_POOLS* role that is associated with the farm configuration database.

- This account is assigned to the *WSS_CONTENT_APPLICATION_POOLS* role that is associated with the SharePoint Admin content database.

- The application pool accounts for web applications are assigned to the *SPDataAccess* role for the content databases

### SharePoint Service Application Pool account

The SharePoint Service Application Pool account must be a domain user account. This account must not be a member of the Administrators group on any computer in the server farm.

The following machine-level permission is configured automatically: This account is a member of *WSS_WPG*.

The following SQL Server and database permissions are configured automatically:

- This account is assigned to the *SPDataAccess* role for the content databases.

- This account is assigned to the *SPDataAccess* role for search database that is associated with the web application.

- This account must have *read* and *write* access to the associated service application database.

- This account is assigned to the *WSS_CONTENT_APPLICATION_POOLS* role that is associated with the farm configuration database.

- This account is assigned to the *WSS_CONTENT_APPLICATION_POOLS* role that is associated with the SharePoint_Admin content database.

## SharePoint database roles
<a name="Section3"> </a>

This section describes the database roles that installation sets up by default or that you can configure optionally.

### WSS_CONTENT_APPLICATION_POOLS database role

The *WSS_CONTENT_APPLICATION_POOLS* database role applies to the application pool account for each web application that is registered in a SharePoint farm. This enables web applications to query and update the site map and have read-only access to other items in the configuration database. Setup assigns the *WSS_CONTENT_APPLICATION_POOLS* role to the following databases:

- The SharePoint Config database (the configuration database)

- The SharePoint Admin Content database

Members of the *WSS_CONTENT_APPLICATION_POOLS* role have the execute permission for a subset of the stored procedures for the database. In addition, members of this role have the select permission to the Versions table (dbo.Versions) in the SharePoint_AdminContent database. For other databases, the accounts planning tool indicates that access to read these databases is automatically configured. In some cases, limited access to write to a database is also automatically configured. To provide this access, permissions for stored procedures are configured.

#### SharePoint_SHELL_ACCESS database role

The secure *SharePoint_SHELL_ACCESS* database role on the configuration database replaces the need to add an administration account as a **db_owner** on the configuration database. By default, the setup account is assigned to the *SharePoint_SHELL_ACCESS* database role. You can use a PowerShell command to grant or remove memberships to this role. Setup assigns the *SharePoint_SHELL_ACCESS* role to the following databases:

- The SharePoint_Config database (the configuration database).

- One or more of the SharePoint Content databases. This is configurable by using the PowerShell command that manages membership and the object that is assigned to this role.

Members of the *SharePoint_SHELL_ACCESS* role have the execute permission for all stored procedures for the database. In addition, members of this role have the read and write permissions on all of the database tables.

#### SPREADONLY database role

The *SPREADONLY* role should be used for setting the database to read-only mode instead of using sp_dboption. This role as its name suggests should be used when only read access is required for data such as usage and telemetry data.

> [!NOTE]
> The sp_dboption stored procedure is not available in SQL Server 2012. For more information about sp_dboption, see [sp_dboption (Transact-SQL)](https://go.microsoft.com/fwlink/p/?LinkId=507398).

The *SPREADONLY* SQL role will have the following permissions:

- Grant SELECT on all SharePoint stored procedures and functions.

- Grant SELECT on all SharePoint tables.

- Grant EXECUTE on user-defined type where schema is dbo.

#### SPDataAccess database role

The *SPDataAccess* role is the default role for database access and should be used for all object model level access to databases. Add the application pool account to this role during upgrade or new deployments.

> [!NOTE]
> The SPDataAccess role replaced the db_owner role in SharePoint Server 2013.

The SPDataAccess role will have the following permissions:

- Grant EXECUTE or SELECT on all SharePoint stored procedures and functions.

- Grant SELECT on all SharePoint tables.

- Grant EXECUTE on User-defined type where schema is dbo.

- Grant INSERT on AllUserDataJunctions table.

- Grant UPDATE on Sites view.

- Grant UPDATE on UserData view.

- Grant UPDATE on AllUserData table.

- Grant INSERT and DELETE on NameValuePair tables.

- Grant create table permission.

## Group permissions
<a name="Section4"> </a>

Please see the following articles for details about the group permissions in SharePoint Server:
- SharePoint 2013: [Group permissions in SharePoint Servers 2013](group-permissions-sharepoint-2013.md)
- SharePoint Server 2016 and 2019: [Group permissions in SharePoint Servers 2016 and 2019](group-permissions-sharepoint-server.md)

## See also
<a name="Section5"> </a>

#### Concepts

[Install SharePoint Server](install.md)