---
title: "Account permissions and security settings in SharePoint Servers 2016 and 2019"
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

# Account permissions and security settings in SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]

This article describes SharePoint administrative and services account permissions for the following areas: Microsoft SQL Server, the file system, file shares, and registry entries.

> [!IMPORTANT]
> Do not use service account names that contain the symbol $.


## About account permissions and security settings in SharePoint Servers 2016 and 2019
<a name="Section1"> </a>

The SharePoint Products Configuration Wizard (Psconfig) and the Farm Configuration Wizard, both of which are run during a complete installation, configure many of the SharePoint baseline account permissions and security settings.

## Service account recommendations
<a name="Section2"> </a>

The following sections describe recommendations on SharePoint Service accounts.

### Service account recommendations

Microsoft recommends using a minimal number of Service Application Pool accounts in the farm. This is to reduce memory usage and increase performance while maintaining the appropriate level of security.

- Use an elevated, personally identifiable account for SharePoint installation, maintenance, and upgrades. This account will hold the roles required as outlined by the **SharePoint Farm Administrator account** outlined below. Each SharePoint administrator should use a separate account to clearly identify activity performed by the administrator on the farm.

- If possible use a security group, **SharePoint Farm Administrators Groups**, to unify all individual SharePoint Farm Administrator accounts and grant permissions as outlined below. This simplify the management of the SharePoint Farm Administrator accounts significally.

- The **SharePoint Farm Service account** should only run the SharePoint Timer service, SharePoint Inights (if applicable), the IIS Application Pools for Central Administration, SharePoint Web Services System (used for the topology service), and SecurityTokenServiceApplicationPool (used for the Security Token Service).

- A single account should be used for all Service Applications, named **Service Application Pool account**. This allows the administrator to use a single IIS Application Pool for all Service Applications. In addition, this account should run the following Windows Services: SharePoint Search Host Controller, SharePoint Server Search, and Distributed Cache (AppFabric Caching Service).

- A single account should be used for all Web Applications, named **Web Application pool account**. This allows the administrator to use a single IIS Application Pool for all Web Applications. The exception is the Central Administration Web Application, which as noted above, is run by the SharePoint farm service account.

- With the exception of the Claims to Windows Token Service account, no Service Application Pool account should have Local Administrator access to any SharePoint server, nor any elevated SQL Server role, for example, the *sysadmin* fixed role. The SharePoint Farm Administrator account will require the *dbcreator* and *securityadmin* fixed roles unless you pre-provision SharePoint databases and manually assign permissions to each database.

- Service Application Pool accounts, with the exception of the account running the Claims to Windows Token Service, should have *Deny logon locally* and *Deny logon through Remote Desktop Services* in the Local *Security Policy\User Rights Assignment*. This is set via *secpol.msc*.

- Use separate accounts for the **Content access** (Search crawler), **Portal Super Reader**, **Portal Super User**, and **User Profile Service Application Synchronization**, if applicable.

- The Claims to Windows Token Service account is a highly privledged account on the farm. Prior to deploying this service, verify it is required. If required, use a separate account for this service.

### Service accounts recommendations overview

Service account name|What is it used for?|How many should be used?
----|----|----
SharePoint Farm Administrator account|Personally identifiable account for a SharePoint Administrator|1-n
SharePoint Farm Service Account| Timer Service, Insights, IIS App for CA, SP Web Services System, Security Token Service App Pool|1
Default content access account|search crawling internal and external sources SP2016|1-n
Content access accounts|search crawling internal and external sources SP2016 and SP2019|1-n
Web Application Pool account|All Web Applications without Central Administration|1
SharePoint Service Application Pool account|All Service Applications|1
Portal Super Reader|Object caching|1
Portal Super User|Object caching|1
User Profile Service Application Synchronization|Used for Active Directory Import|1-n




## SharePoint administrative accounts
<a name="Section3"> </a>

One of the following SharePoint components automatically configures most of the SharePoint administrative account permissions during the setup process:

- The SharePoint Products Configuration Wizard (Psconfig).

- The Farm Configuration Wizard.

- The SharePoint Central Administration website.

- Microsoft PowerShell.

### SharePoint Farm Administrator account

This account is used to set up each server in your farm by running the SharePoint Products Configuration Wizard, the initial Farm Configuration Wizard, and PowerShell. For the examples in this article, the SharePoint Farm Administrator account is used for farm administration, and you can use Central Administration to manage it. Some configuration options, for example, configuration of the SharePoint Server Search query server, require local administration permissions. The SharePoint Farm Administrator account requires the following permissions:

- It must have domain user account permissions.

- It must be a member of the local Administrators group on each server in the SharePoint farm.

- This account must have access to the SharePoint databases.

- If you use any PowerShell operations that affect a database, the SharePoint Farm Administrator account must be a member of the *db_owner* role.

- This account must be assigned to the *securityadmin* and *dbcreator* SQL Server security roles during setup and configuration.

> [!NOTE]
> The *securityadmin* and *dbcreator* SQL Server security roles might be required for this account during a complete version-to-version upgrade because new databases might have to be created and secured for services.

After you run the configuration wizards, machine-level permissions for the SharePoint Farm Administrator account include:

- Membership in the *WSS_ADMIN_WPG* Windows security group.


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
<a name="Section4"> </a>

This section describes the SharePoint Application Pool accounts that are set up by default during installation.

### Default content access account

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2016 only.

The default content access account is used within a specific service application to crawl content, unless a different authentication method is specified by a crawl rule for a URL or URL pattern. This account requires the following permission configuration settings:

- The default content access account must be a domain user account that has read access to external or secure content sources that you want to crawl by using this account.

- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites.

- This account must not be a member of the Farm Administrators group.

### Content access accounts

> [!IMPORTANT]
> Information in this section applies to SharePoint Servers 2016 and 2019 only.

Content access accounts are configured to access content by using the Search administration crawl rules feature. This type of account is optional, and you can configure it when you create a new crawl rule. For example, external content (such as a file share) might require this separate content access account. This account requires the following permission configuration settings:

- The content access account must have read access to external or secure content sources that this account is configured to access.

- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites.

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
<a name="Section5"> </a>

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
> The SPDataAccess role replaced the db_owner role in SharePoint Server 2016.

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
<a name="Section6"> </a>

This section describes permissions of groups that the SharePoint Servers 2016 and 2019 setup and configuration tools create.

### WSS_ADMIN_WPG

*WSS_ADMIN_WPG* has read and write access to local resources. The application pool accounts for the Central Administration and Timer services are in *WSS_ADMIN_WPG*. The following table shows the *WSS_ADMIN_WPG* registry entry permissions.

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\VSS|Full control|Not applicable|Not applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office\16.0\Registration\{90150000-110D-0000-1000-0000000FF1CE}|Read, write|Not applicable|Not applicable|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server|Read|No|This key is the root of the SharePoint Server registry settings tree. If this key is altered, SharePoint Server functionality will fail.|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\16.0|Full control|No|This key is the root of the SharePoint Server 2016 registry settings.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LoadBalancerSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LauncherSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\Search|Full control|Not applicable|Not applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Search|Full control|Not applicable|Not applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint Server installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\WSS|Full control|Yes|This key contains settings used during setup. If this key is altered, diagnostic logging might fail, and setup or post-setup configuration might fail.|

The following table shows the WSS_ADMIN_WPG file system permissions.

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start, and the administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable, and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint Server.|
|%ProgramFiles%\Microsoft Office Servers\16.0|Full control|No|This directory is the installation location for SharePoint Server 2016 binaries and data. The directory can be changed during installation. All SharePoint Server functionality will fail if this directory is removed, altered, or removed after installation. Membership in the WSS_ADMIN_WPG Windows security group is required for some SharePoint Server services to be able to store data on disk.|
|%ProgramFiles%\Microsoft Office Servers\16.0\WebServices|Read, write|No|This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint Server features that depend on these services will fail if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Data|Full control|No|This directory is the root location where local data is stored, including search indexes. Search functionality will fail if this directory is removed or altered. WSS_ADMIN_WPG Windows security group permissions are required to enable search to save and secure data in this folder.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Logs|Full control|Yes|This directory is the location where the run-time diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Data\Office Server|Full control|Yes|Same as the parent folder.|
|%windir%\System32\drivers\etc\HOSTS|Read, write|Not applicable|Not applicable|
|%windir%\Tasks|Full control|Not applicable|Not applicable|
|%COMMONPROGRAMFILES%Microsoft Shared\Web Server Extensions\16|Modify|Yes|This directory is the installation directory for core SharePoint Server files. If the access control list (ACL) is modified, feature activation, solution deployment, and other features will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\CONFIG|Full control|Yes|This directory contains files used to extend IIS Web sites with SharePoint Server. If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS|Full control|No|This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint Server depends. If the access control list is modified, Web Part rendering and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|
|%systemdrive\program files\Microsoft Office Servers\16 folder on Index servers|Full control|Not applicable|This permission is granted for a %systemdrive\program files\Microsoft Office Servers\16 folder on Index servers.|

### WSS_WPG

*WSS_WPG* has read access to local resources. All application pool and services accounts are in WSS_WPG. The following table shows *WSS_WPG* registry entry permissions.

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\16.0|Read|No|This key is the root of the SharePoint Server registry settings.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\Diagnostics|Read, write|No|This key contains settings for the SharePoint Server diagnostic logging. Altering this key will break the logging functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LoadBalancerSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LauncherSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure|Read|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint Server 2016 installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\WSS|Read|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging might fail and setup or post-setup configuration mightay fail.|

The following table shows the WSS_WPG file system permissions.

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Read|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and the administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Read, execute|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint Server.|
|%ProgramFiles%\Microsoft Office Servers\16.0|Read, execute|No|This directory is the installation location for the SharePoint Server  binaries and data. It can be changed during installation. All SharePoint Server functionality will fail if this directory is removed, altered, or moved after installation. WSS_WPG read and execute permissions are required to enable IIS sites to load SharePoint Server  binaries.|
|%ProgramFiles%\Microsoft Office Servers\16.0\WebServices|Read|No|This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint Server features that depend on these services will fail if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Logs|Read, write|Yes|This directory is the location where the runtime diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\ADMISAPI|Read|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\CONFIG|Read|Yes|This directory contains files used to extend IIS Web sites with SharePoint Server . If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS|Modify|No|This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Read|Yes|This directory is used by platform components on which SharePoint Server depends. If the access control list is modified, Web Part rendering, and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Read|No|This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.The registry key applies only to SharePoint Server.|
|%systemdrive\program files\Microsoft Office Servers\16|Read, execute|Not applicable|The permission is granted for %systemdrive\program files\Microsoft Office Servers\16 folder on Index servers.|

### Local service

The following table shows the local service registry entry permission:

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LoadBalancerSettings|Read|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|

The following table shows the local service file system permission:

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\16.0\Bin|Read, execute|No|This directory is the installed location of the SharePoint Server binaries. All the SharePoint Server functionality will fail if this directory is removed or altered.|

### Local system

The following table shows the local system registry entry permissions:

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\LauncherSettings|Read|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.This registry key applies only to SharePoint Server.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint Server  installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\WSS|Full control|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging might fail and setup or post-setup configuration might fail.|

The following table shows the local file system permissions:

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint Server.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\CONFIG|Full control|Yes|If this directory or its contents are altered, Web Application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS|Full control|No|This directory contains setup and run-time tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint Server depends. If the access control list is modified, Web Part rendering, and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|

### Network service

The following table shows the network service registry entry permission:

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\16.0\Search\Setup|Read|Not applicable|Not applicable|

### Administrators

The following table shows the administrators registry entry permissions:

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint Server installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\WSS|Full control|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging might fail and setup or post-setup configuration might fail.|

The following table shows the administrators file system permissions:

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full Control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS web site paths are provided for all IIS web sites that are extended with SharePoint Server .|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\CONFIG|Full control|Yes|If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS|Full control|No|This directory contains setup and run-time tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint Server depends. If the ACL is modified, Web Part rendering, and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|

### WSS_RESTRICTED_WPG

*WSS_RESTRICTED_WPG* can read the encrypted farm administration credential registry entry. *WSS_RESTRICTED_WPG* is only used for encryption and decryption of passwords that are stored in the configuration database. The following table shows the *WSS_RESTRICTED_WPG* registry entry permission:

|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\16.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|

### Users group

The following table shows the users group file system permissions:

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\16.0|Read, execute|No|This directory is the installation location for SharePoint Server binaries and data. It can be changed during installation. All SharePoint Server functionality will fail if this directory is removed, altered, or moved after installation.|
|%ProgramFiles%\Microsoft Office Servers\16.0\WebServices\Root|Read, execute|No|This directory is the root directory where back-end root Web services are hosted. The only service initially installed on this directory is a search global administration service. Some search administration functionality that uses the server-specific Central Administration Settings page will not work if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Logs|Read, write|Yes|This directory is the location where the run-time diagnostic logging is generated. Logging will not function properly if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\16.0\Bin|Read, execute|No|This directory is the installed location of SharePoint Server binaries. All of the SharePoint Server functionality will fail if this directory is removed or altered.|

### All SharePoint Server service accounts

The following table shows the all SharePoint Server service accounts file system permission:

|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS|Modify|No|This directory contains setup and run-time tracing logs. If this directory is altered, diagnostic logging will not function correctly. All SharePoint Server service accounts must have write permission to this directory.|

## See also
<a name="Section6"> </a>

#### Concepts

[Install SharePoint Server](install.md)
