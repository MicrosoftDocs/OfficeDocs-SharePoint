---
title: "Account permissions and security settings in SharePoint 2013"
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
ms.assetid: 1c52404b-9221-4486-a74b-f7e1330c21df
description: "Learn what permissions and security settings to use with a deployment of SharePoint."
---

# Account permissions and security settings in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
This article describes SharePoint administrative and services account permissions for the following areas: Microsoft SQL Server, the file system, file shares, and registry entries.
  
> [!IMPORTANT]
> Do not use service account names that contain the symbol $. 
  
    
## About account permissions and security settings
<a name="Section1"> </a>

The SharePoint Configuration Wizard (Psconfig) and the Farm Creation Wizard, both of which are run during a Complete installation, configure many of the SharePoint baseline account permissions and security settings.
  
## SharePoint administrative accounts
<a name="Section2"> </a>

One of the following SharePoint components automatically configures most of the SharePoint administrative account permissions during the setup process:
  
- The SharePoint Configuration Wizard (Psconfig).
    
- The Farm Creation Wizard.
    
- The SharePoint Central Administration web site.
    
- PowerShell.
    
### Setup user administrator account

This account is used to set up each server in your farm by running the SharePoint Configuration Wizard, the initial Farm Creation Wizard, and PowerShell. For the examples in this article, the setup user administrator account is used for farm administration, and you can use Central Administration to manage it. Some configuration options, for example, configuration of the SharePoint 2013 Search query server, require local administration permissions. The setup user administrator account requires the following permissions:
  
- It must have domain user account permissions.
    
- It must be a member of the local administrators group on each server in the SharePoint farm.
    
- This account must have access to the SharePoint databases.
    
- If you use any PowerShell operations that affect a database, the setup user administrator account must be a member of the **db_owner** role. 
    
- This account must be assigned to the **securityadmin** and **dbcreator** SQL Server security roles during setup and configuration. 
    
> [!NOTE]
> The **securityadmin** and **dbcreator** SQL Server security roles might be required for this account during a complete version-to-version upgrade because new databases might have to be created and secured for services. 
  
After you run the configuration wizards, machine-level permissions for the setup user administrator account include:
  
- Membership in the WSS_ADMIN_WPG Windows security group.
    
- Membership in the IIS_WPG role.
    
After you run the configuration wizards, database permissions include:
  
- **db_owner** on the SharePoint server farm configuration database. 
    
- **db_owner** on the SharePoint Central Administration content database. 
    
> [!CAUTION]
> If the account that you use to run the configuration wizards does not have the appropriate special SQL Server role membership or access as **db_owner** on the databases, the configuration wizards will not run correctly. 
  
### SharePoint farm service account

The server farm account, which is also referred to as the database access account, is used as the application pool identity for Central Administration and as the process account for the SharePoint Foundation 2013 Timer service. The server farm account requires the following permissions:
  
- It must have domain user account permissions.
    
Additional permissions are automatically granted to the server farm account on web servers and application servers that are joined to a server farm.
  
After you run Setup, machine-level permissions include:
  
- Membership in the WSS_ADMIN_WPG Windows security group for the SharePoint Foundation 2013 Timer service.
    
- Membership in WSS_RESTRICTED_WPG for the Central Administration and Timer service application pools.
    
- Membership in WSS_WPG for the Central Administration application pool.
    
After you run the configuration wizards, SQL Server and database permissions include:
  
- **Dbcreator** fixed server role. 
    
- **Securityadmin** fixed server role. 
    
- **db_owner** for all SharePoint databases. 
    
- Membership in the WSS_CONTENT_APPLICATION_POOLS role for the SharePoint server farm configuration database.
    
- Membership in the WSS_CONTENT_APPLICATION_POOLS role for the SharePoint_Admin content database.
    
## SharePoint service application accounts
<a name="Section3"> </a>

This section describes the service application accounts that are set up by default during installation.
  
### Application pool account

The application pool account is used for application pool identity. The application pool account requires the following permission configuration settings:
  
The following machine-level permission is configured automatically: The application pool account is a member of WSS_WPG.
  
The following SQL Server and database permissions for this account are configured automatically:
  
- The application pool accounts for Web applications are assigned to the SP_DATA_ACCESS role for the content databases.
    
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role associated with the farm configuration database.
    
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role associated with the SharePoint_Admin content database.
    
### Default content access account

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2016 only. 
  
The default content access account is used within a specific service application to crawl content, unless a different authentication method is specified by a crawl rule for a URL or URL pattern. This account requires the following permission configuration settings:
  
- The default content access account must be a domain user account that has read access to external or secure content sources that you want to crawl by using this account.
    
- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites.
    
- This account must not be a member of the Farm Administrators group.
    
### Content access accounts

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2016 only. 
  
Content access accounts are configured to access content by using the Search administration crawl rules feature. This type of account is optional and you can configure it when you create a new crawl rule. For example, external content (such as a file share) might require this separate content access account. This account requires the following permission configuration settings:
  
- The content access account must have read access to external or secure content sources that this account is configured to access.
    
- For SharePoint Server sites that are not part of the server farm, you have to explicitly grant this account full read permissions to the web applications that host the sites. 
    
### Excel Services unattended service account

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2016 only. 
  
Excel Services uses the Excel Services unattended service account to connect to external data sources that require a user name and password that are based on operating systems other than Windows for authentication. If this account is not configured, Excel Services will not attempt to connect to these types of data sources. Although account credentials are used to connect to data sources of operating systems other than Windows, if the account is not a member of the domain, Excel Services cannot access them. This account must be a domain user account.
  
### My Sites application pool account

> [!IMPORTANT]
> Information in this section applies to SharePoint Server 2016 only. 
  
The My Sites application pool account must be a domain user account. This account must not be a member of the Farm Administrators group. 
  
The following machine-level permission is configured automatically: This account is a member of WSS_WPG.
  
The following SQL Server and database permissions are configured automatically:
  
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role that is associated with the farm configuration database.
    
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role that is associated with the SharePoint_Admin content database.
    
- The application pool accounts for web applications are assigned to the SP_DATA_ACCESS role for the content databases
    
### Other application pool accounts

The other application pool account must be a domain user account. This account must not be a member of the Administrators group on any computer in the server farm.
  
The following machine-level permission is configured automatically: This account is a member of WSS_WPG.
  
The following SQL Server and database permissions are configured automatically:
  
- This account is assigned to the SP_DATA_ACCESS role for the content databases.
    
- This account is assigned to the SP_DATA_ACCESS role for search database that is associated with the web application.
    
- This account must have read and write access to the associated service application database.
    
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role that is associated with the farm configuration database.
    
- This account is assigned to the WSS_CONTENT_APPLICATION_POOLS role that is associated with the SharePoint_Admin content database.
    
## SharePoint database roles
<a name="Section4"> </a>

This section describes the database roles that installation sets up by default or that you can configure optionally.
  
### WSS_CONTENT_APPLICATION_POOLS database role

The WSS_CONTENT_APPLICATION_POOLS database role applies to the application pool account for each web application that is registered in a SharePoint farm. This enables web applications to query and update the site map and have read-only access to other items in the configuration database. Setup assigns the WSS_CONTENT_APPLICATION_POOLS role to the following databases:
  
- The SharePoint_Config database (the configuration database).
    
- The SharePoint_AdminContent database.
    
Members of the WSS_CONTENT_APPLICATION_POOLS role have the execute permission for a subset of the stored procedures for the database. In addition, members of this role have the select permission to the Versions table (dbo.Versions) in the SharePoint_AdminContent database. For other databases, the accounts planning tool indicates that access to read these databases is automatically configured. In some cases, limited access to write to a database is also automatically configured. To provide this access, permissions for stored procedures are configured. 
  
#### WSS_SHELL_ACCESS database role

The secure WSS_SHELL_ACCESS database role on the configuration database replaces the need to add an administration account as a **db_owner** on the configuration database. By default, the setup account is assigned to the WSS_SHELL_ACCESS database role. You can use a PowerShell command to grant or remove memberships to this role. Setup assigns the WSS_SHELL_ACCESS role to the following databases: 
  
- The SharePoint_Config database (the configuration database).
    
- One or more of the SharePoint Content databases. This is configurable by using the PowerShell command that manages membership and the object that is assigned to this role.
    
Members of the WSS_SHELL_ACCESS role have the execute permission for all stored procedures for the database. In addition, members of this role have the read and write permissions on all of the database tables.
  
#### SP_READ_ONLY database role

The **SP_READ_ONLY** role should be used for setting the database to read only mode instead of using sp_dboption. This role as its name suggests should be used when only read access is required for data such as usage and telemetry data. 
  
> [!NOTE]
> The sp_dboption stored procedure is not available in SQL Server 2012. For more information about sp_dboption see [sp_dboption (Transact-SQL)](https://go.microsoft.com/fwlink/?LinkId=507398). 
  
The SP_READ_ONLY SQL role will have the following permissions:
  
- Grant SELECT on all SharePoint stored procedures and functions
    
- Grant SELECT on all SharePoint tables
    
- Grant EXECUTE on user-defined type where schema is dbo
    
#### SP_DATA_ACCESS database role

The **SP_DATA_ACCESS** role is the default role for database access and should be used for all object model level access to databases. Add the application pool account to this role during upgrade or new deployments. 
  
> [!NOTE]
> The SP_DATA_ACCESS role replaces the db_owner role in SharePoint 2013. 
  
The SP_DATA_ACCESS role will have the following permissions:
  
- Grant EXECUTE or SELECT on all SharePoint stored procedures and functions
    
- Grant SELECT on all SharePoint tables
    
- Grant EXECUTE on User-defined type where schema is dbo
    
- Grant INSERT on AllUserDataJunctions table
    
- Grant UPDATE on Sites view
    
- Grant UPDATE on UserData view
    
- Grant UPDATE on AllUserData table
    
- Grant INSERT and DELETE on NameValuePair tables
    
- Grant create table permission
    
## Group permissions
<a name="Section5"> </a>

This section describes permissions of groups that the SharePoint 2013 setup and configuration tools create.
  
### WSS_ADMIN_WPG

WSS_ADMIN_WPG has read and write access to local resources. The application pool accounts for the Central Administration and Timer services are in WSS_ADMIN_WPG. The following table shows the WSS_ADMIN_WPG registry entry permissions.
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\VSS  <br/> |Full control  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office\15.0\Registration\{90150000-110D-0000-1000-0000000FF1CE}  <br/> |Read, write  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server  <br/> |Read  <br/> |No  <br/> |This key is the root of the SharePoint 2013 registry settings tree. If this key is altered, SharePoint 2013 functionality will fail.  <br/> |
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\15.0  <br/> |Full control  <br/> |No  <br/> |This key is the root of the SharePoint 2013 registry settings.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings  <br/> |Read, write  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings  <br/> |Read, write  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Search  <br/> |Full control  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Search  <br/> |Full control  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure  <br/> |Full control  <br/> |No  <br/> |This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS  <br/> |Full control  <br/> |Yes  <br/> |This key contains settings used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.  <br/> |
   
The following table shows the WSS_ADMIN_WPG file system permissions.
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and the administrative actions might fail if this directory is altered or deleted.  <br/> |
|C:\Inetpub\wwwroot\wss  <br/> |Full control  <br/> |No  <br/> |This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0  <br/> |Full control  <br/> |No  <br/> |This directory is the installation location for SharePoint 2013 binaries and data. The directory can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or removed after installation. Membership in the WSS_ADMIN_WPG Windows security group is required for some SharePoint 2013 services to be able to store data on disk.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices  <br/> |Read, write  <br/> |No  <br/> |This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint 2013 features that depend on these services will fail if this directory is removed or altered.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Data  <br/> |Full control  <br/> |No  <br/> |This directory is the root location where local data is stored, including search indexes. Search functionality will fail if this directory is removed or altered. WSS_ADMIN_WPG Windows security group permissions are required to enable search to save and secure data in this folder.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs  <br/> |Full control  <br/> |Yes  <br/> |This directory is the location where the run-time diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Data\Office Server  <br/> |Full control  <br/> |Yes  <br/> |Same as the parent folder.  <br/> |
|%windir%\System32\drivers\etc\HOSTS  <br/> |Read, write  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|%windir%\Tasks  <br/> |Full control  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
|%COMMONPROGRAMFILES%Microsoft Shared\Web Server Extensions\15  <br/> |Modify  <br/> |Yes  <br/> |This directory is the installation directory for core SharePoint 2013 files. If the access control list (ACL) is modified, feature activation, solution deployment, and other features will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI  <br/> |Full control  <br/> |Yes  <br/> |This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG  <br/> |Full control  <br/> |Yes  <br/> |This directory contains files used to extend IIS Web sites with SharePoint 2013. If this directory or its contents are altered, web application provisioning will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS  <br/> |Full control  <br/> |No  <br/> |This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.  <br/> |
|%windir%\temp  <br/> |Full control  <br/> |Yes  <br/> |This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering and other deserialization operations might fail.  <br/> |
|%windir%\System32\logfiles\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.  <br/> This registry key applies only to SharePoint Server.  <br/> |
|%systemdrive\program files\Microsoft Office Servers\15 folder on Index servers  <br/> |Full control  <br/> |Not Applicable  <br/> |This permission is granted for a %systemdrive\program files\Microsoft Office Servers\15 folder on Index servers.  <br/> |
   
### WSS_WPG

WSS_WPG has read access to local resources. All application pool and services accounts are in WSS_WPG. The following table shows WSS_WPG registry entry permissions.
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\15.0  <br/> |Read  <br/> |No  <br/> |This key is the root of the SharePoint 2013 registry settings.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Diagnostics  <br/> |Read, write  <br/> |No  <br/> |This key contains settings for the SharePoint 2013 diagnostic logging. Altering this key will break the logging functionality.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings  <br/> |Read, write  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings  <br/> |Read, write  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure  <br/> |Read  <br/> |No  <br/> |This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS  <br/> |Read  <br/> |Yes  <br/> |This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.  <br/> |
   
The following table shows the WSS_WPG file system permissions.
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint  <br/> |Read  <br/> |No  <br/> |This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and the administrative actions might fail if this directory is altered or deleted.  <br/> |
|C:\Inetpub\wwwroot\wss  <br/> |Read, execute  <br/> |No  <br/> |This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0  <br/> |Read, execute  <br/> |No  <br/> |This directory is the installation location for the SharePoint 2013 binaries and data. It can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or moved after installation. WSS_WPG read and execute permissions are required to enable IIS sites to load SharePoint 2013 binaries.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices  <br/> |Read  <br/> |No  <br/> |This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint 2013 features that depend on these services will fail if this directory is removed or altered.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs  <br/> |Read, write  <br/> |Yes  <br/> |This directory is the location where the runtime diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI  <br/> |Read  <br/> |Yes  <br/> |This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG  <br/> |Read  <br/> |Yes  <br/> |This directory contains files used to extend IIS Web sites with SharePoint 2013. If this directory or its contents are altered, web application provisioning will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS  <br/> |Modify  <br/> |No  <br/> |This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.  <br/> |
|%windir%\temp  <br/> |Read  <br/> |Yes  <br/> |This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering, and other deserialization operations may fail.  <br/> |
|%windir%\System32\logfiles\SharePoint  <br/> |Read  <br/> |No  <br/> |This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.  <br/> The registry key applies only to SharePoint Server.  <br/> |
|%systemdrive\program files\Microsoft Office Servers\15  <br/> |Read, execute  <br/> |Not Applicable  <br/> |The permission is granted for %systemdrive\program files\Microsoft Office Servers\15 folder on Index servers.  <br/> |
   
### Local service

The following table shows the local service registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings  <br/> |Read  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> |
   
The following table shows the local service file system permission:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\15.0\Bin  <br/> |Read, execute  <br/> |No  <br/> |This directory is the installed location of the SharePoint 2013 binaries. All the SharePoint 2013 functionality will fail if this directory is removed or altered.  <br/> |
   
### Local system

The following table shows the local system registry entry permissions:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings  <br/> |Read  <br/> |No  <br/> |This key contains settings for the document conversion service. Altering this key will break document conversion functionality.  <br/> This registry key applies only to SharePoint Server.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure  <br/> |Full control  <br/> |No  <br/> |This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin  <br/> |Full control  <br/> |No  <br/> |This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS  <br/> |Full control  <br/> |Yes  <br/> |This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.  <br/> |
   
The following table shows the local file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.  <br/> |
|C:\Inetpub\wwwroot\wss  <br/> |Full control  <br/> |No  <br/> |This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI  <br/> |Full control  <br/> |Yes  <br/> |This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG  <br/> |Full control  <br/> |Yes  <br/> |If this directory or its contents are altered, Web Application provisioning will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS  <br/> |Full control  <br/> |No  <br/> |This directory contains setup and run-time tracing logs. If the directory is altered, diagnostic logging will not function correctly.  <br/> |
|%windir%\temp  <br/> |Full control  <br/> |Yes  <br/> |This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering, and other deserialization operations might fail.  <br/> |
|%windir%\System32\logfiles\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.  <br/> This registry key applies only to SharePoint Server.  <br/> |
   
### Network service

The following table shows the network service registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Search\Setup  <br/> |Read  <br/> |Not Applicable  <br/> |Not Applicable  <br/> |
   
### Administrators

The following table shows the administrators registry entry permissions:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure  <br/> |Full control  <br/> |No  <br/> |This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin  <br/> |Full control  <br/> |No  <br/> |This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.  <br/> |
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS  <br/> |Full control  <br/> |Yes  <br/> |This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.  <br/> |
   
The following table shows the administrators file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.  <br/> |
|C:\Inetpub\wwwroot\wss  <br/> |Full Control  <br/> |No  <br/> |This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS web site paths are provided for all IIS web sites that are extended with SharePoint 2013.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI  <br/> |Full control  <br/> |Yes  <br/> |This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG  <br/> |Full control  <br/> |Yes  <br/> |If this directory or its contents are altered, web application provisioning will not function correctly.  <br/> |
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS  <br/> |Full control  <br/> |No  <br/> |This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.  <br/> |
|%windir%\temp  <br/> |Full control  <br/> |Yes  <br/> |This directory is used by platform components on which SharePoint 2013 depends. If the ACL is modified, Web Part rendering, and other deserialization operations might fail.  <br/> |
|%windir%\System32\logfiles\SharePoint  <br/> |Full control  <br/> |No  <br/> |This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.  <br/> This registry key applies only to SharePoint Server.  <br/> |
   
### WSS_RESTRICTED_WPG

WSS_RESTRICTED_WPG can read the encrypted farm administration credential registry entry. WSS_RESTRICTED_WPG is only used for encryption and decryption of passwords that are stored in the configuration database. The following table shows the WSS_RESTRICTED_WPG registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin  <br/> |Full control  <br/> |No  <br/> |This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.  <br/> |
   
### Users group

The following table shows the users group file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\15.0  <br/> |Read, execute  <br/> |No  <br/> |This directory is the installation location for SharePoint 2013 binaries and data. It can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or moved after installation.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices\Root  <br/> |Read, execute  <br/> |No  <br/> |This directory is the root directory where back-end root Web services are hosted. The only service initially installed on this directory is a search global administration service. Some search administration functionality that uses the server-specific Central Administration Settings page will not work if this directory is removed or altered.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs  <br/> |Read, write  <br/> |Yes  <br/> |This directory is the location where the run-time diagnostic logging is generated. Logging will not function properly if this directory is removed or altered.  <br/> |
|%ProgramFiles%\Microsoft Office Servers\15.0\Bin  <br/> |Read, execute  <br/> |No  <br/> |This directory is the installed location of SharePoint 2013 binaries. All of the SharePoint 2013 functionality will fail if this directory is removed or altered.  <br/> |
   
### All SharePoint 2013 service accounts

The following table shows the all SharePoint 2013 service accounts file system permission:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS  <br/> |Modify  <br/> |No  <br/> |This directory contains setup and runtime tracing logs. If this directory is altered, diagnostic logging will not function correctly. All SharePoint 2013 service accounts must have write permission to this directory.  <br/> |
   
## See also
<a name="Section5"> </a>

#### Concepts

[Install SharePoint Server](install.md)

