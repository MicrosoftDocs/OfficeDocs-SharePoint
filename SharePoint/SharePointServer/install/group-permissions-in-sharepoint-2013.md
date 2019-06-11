---
title: "Group permissions in SharePoint 2013"
ms.reviewer: 
ms.author: 
author: 
manager: 
ms.date: 
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Learn what group permissions to use with a deployment of SharePoint."
---

# Group permissions in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]

This article describes SharePoint group permissions for the following areas: Microsoft SQL Server, the file system, file shares, and registry entries.

## Group permissions
<a name="Section1"> </a>

This section describes permissions of groups that the SharePoint Servers 2016 and 2019 setup and configuration tools create.

### WSS_ADMIN_WPG

WSS_ADMIN_WPG has read and write access to local resources. The application pool accounts for the Central Administration and Timer services are in *WSS_ADMIN_WPG*. The following table shows the WSS_ADMIN_WPG registry entry permissions.
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\VSS|Full control|Not Applicable|Not Applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office\15.0\Registration\{90150000-110D-0000-1000-0000000FF1CE}|Read, write|Not Applicable|Not Applicable|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server|Read|No|This key is the root of the SharePoint 2013 registry settings tree. If this key is altered, SharePoint 2013 functionality will fail.|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\15.0|Full control|No|This key is the root of the SharePoint 2013 registry settings.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Search|Full control|Not Applicable|Not Applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Search|Full control|Not Applicable|Not Applicable|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS|Full control|Yes|This key contains settings used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.|
   
The following table shows the WSS_ADMIN_WPG file system permissions.
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and the administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.|
|%ProgramFiles%\Microsoft Office Servers\15.0|Full control|No|This directory is the installation location for SharePoint 2013 binaries and data. The directory can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or removed after installation. Membership in the WSS_ADMIN_WPG Windows security group is required for some SharePoint 2013 services to be able to store data on disk.|
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices|Read, write|No|This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint 2013 features that depend on these services will fail if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Data|Full control|No|This directory is the root location where local data is stored, including search indexes. Search functionality will fail if this directory is removed or altered. WSS_ADMIN_WPG Windows security group permissions are required to enable search to save and secure data in this folder.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs|Full control|Yes|This directory is the location where the run-time diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Data\Office Server|Full control|Yes|Same as the parent folder.|
|%windir%\System32\drivers\etc\HOSTS|Read, write|Not Applicable|Not Applicable|
|%windir%\Tasks|Full control|Not Applicable|Not Applicable|
|%COMMONPROGRAMFILES%Microsoft Shared\Web Server Extensions\15|Modify|Yes|This directory is the installation directory for core SharePoint 2013 files. If the access control list (ACL) is modified, feature activation, solution deployment, and other features will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG|Full control|Yes|This directory contains files used to extend IIS Web sites with SharePoint 2013. If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS|Full control|No|This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|
|%systemdrive\program files\Microsoft Office Servers\15 folder on Index servers|Full control|Not Applicable|This permission is granted for a %systemdrive\program files\Microsoft Office Servers\15 folder on Index servers.|
   
### WSS_WPG

WSS_WPG has read access to local resources. All application pool and services accounts are in WSS_WPG. The following table shows *WSS_WPG* registry entry permissions.
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office Server\15.0|Read|No|This key is the root of the SharePoint 2013 registry settings.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Diagnostics|Read, write|No|This key contains settings for the SharePoint 2013 diagnostic logging. Altering this key will break the logging functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings|Read, write|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure|Read|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS|Read|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.|
   
The following table shows the WSS_WPG file system permissions.
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Read|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and the administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Read, execute|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.|
|%ProgramFiles%\Microsoft Office Servers\15.0|Read, execute|No|This directory is the installation location for the SharePoint 2013 binaries and data. It can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or moved after installation. WSS_WPG read and execute permissions are required to enable IIS sites to load SharePoint 2013 binaries.|
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices|Read|No|This directory is the root directory where back-end Web services are hosted, for example, Excel and Search. The SharePoint 2013 features that depend on these services will fail if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs|Read, write|Yes|This directory is the location where the runtime diagnostic logging is generated. Logging functionality will not function properly if this directory is removed or altered.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI|Read|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG|Read|Yes|This directory contains files used to extend IIS Web sites with SharePoint 2013. If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS|Modify|No|This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Read|Yes|This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering, and other deserialization operations may fail.|
|%windir%\System32\logfiles\SharePoint|Read|No|This directory is used by SharePoint Server usage logging. If this directory is modified, usage logging will not function correctly.The registry key applies only to SharePoint Server.|
|%systemdrive\program files\Microsoft Office Servers\15|Read, execute|Not Applicable|The permission is granted for %systemdrive\program files\Microsoft Office Servers\15 folder on Index servers.|
   
### Local service

The following table shows the local service registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LoadBalancerSettings|Read|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.|
   
The following table shows the local service file system permission:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\15.0\Bin|Read, execute|No|This directory is the installed location of the SharePoint 2013 binaries. All the SharePoint 2013 functionality will fail if this directory is removed or altered.|
   
### Local system

The following table shows the local system registry entry permissions:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\LauncherSettings|Read|No|This key contains settings for the document conversion service. Altering this key will break document conversion functionality.This registry key applies only to SharePoint Server.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS|Full control|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.|
   
The following table shows the local file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS Web site paths are provided for all IIS Web sites extended with SharePoint 2013.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG|Full control|Yes|If this directory or its contents are altered, Web Application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS|Full control|No|This directory contains setup and run-time tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint 2013 depends. If the access control list is modified, Web Part rendering, and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|
   
### Network service

The following table shows the network service registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Office Server\15.0\Search\Setup|Read|Not Applicable|Not Applicable|
   
### Administrators

The following table shows the administrators registry entry permissions:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure|Full control|No|This key contains the connection string and the ID of the configuration database to which the machine is joined. If this key is altered, the SharePoint 2013 installation on the machine will not function.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\WSS|Full control|Yes|This key contains settings that are used during setup. If this key is altered, diagnostic logging may fail and setup or post-setup configuration may fail.|
   
The following table shows the administrators file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%AllUsersProfile%\ Microsoft\SharePoint|Full control|No|This directory contains the file-system-backed cache of the farm configuration. Processes might fail to start and administrative actions might fail if this directory is altered or deleted.|
|C:\Inetpub\wwwroot\wss|Full Control|No|This directory (or the corresponding directory under the Inetpub root on the server) is used as the default location for IIS Web sites. SharePoint sites will be unavailable and administrative actions might fail if this directory is altered or deleted, unless custom IIS web site paths are provided for all IIS web sites that are extended with SharePoint 2013.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\ADMISAPI|Full control|Yes|This directory contains the SOAP services for Central Administration. If this directory is altered, remote site creation and other methods exposed in the service will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\CONFIG|Full control|Yes|If this directory or its contents are altered, web application provisioning will not function correctly.|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS|Full control|No|This directory contains setup and runtime tracing logs. If the directory is altered, diagnostic logging will not function correctly.|
|%windir%\temp|Full control|Yes|This directory is used by platform components on which SharePoint 2013 depends. If the ACL is modified, Web Part rendering, and other deserialization operations might fail.|
|%windir%\System32\logfiles\SharePoint|Full control|No|This directory is used by SharePoint Server for usage logging. If this directory is modified, usage logging will not function correctly.This registry key applies only to SharePoint Server.|
   
### WSS_RESTRICTED_WPG

*WSS_RESTRICTED_WPG* can read the encrypted farm administration credential registry entry. *WSS_RESTRICTED_WPG* is only used for encryption and decryption of passwords that are stored in the configuration database. The following table shows the WSS_RESTRICTED_WPG registry entry permission:
  
|**Key name**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|HKEY_LOCAL_MACHINE\Software\Microsoft\Shared Tools\Web Server Extensions\15.0\Secure\FarmAdmin|Full control|No|This key contains the encryption key that is used to store secrets in the configuration database. If this key is altered, service provisioning and other features will fail.|
   
### Users group

The following table shows the users group file system permissions:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%ProgramFiles%\Microsoft Office Servers\15.0|Read, execute|No|This directory is the installation location for SharePoint 2013 binaries and data. It can be changed during installation. All SharePoint 2013 functionality will fail if this directory is removed, altered, or moved after installation.|
|%ProgramFiles%\Microsoft Office Servers\15.0\WebServices\Root|Read, execute|No|This directory is the root directory where back-end root Web services are hosted. The only service initially installed on this directory is a search global administration service. Some search administration functionality that uses the server-specific Central Administration Settings page will not work if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Logs|Read, write|Yes|This directory is the location where the run-time diagnostic logging is generated. Logging will not function properly if this directory is removed or altered.|
|%ProgramFiles%\Microsoft Office Servers\15.0\Bin|Read, execute|No|This directory is the installed location of SharePoint 2013 binaries. All of the SharePoint 2013 functionality will fail if this directory is removed or altered.|
   
### All SharePoint 2013 service accounts

The following table shows the all SharePoint 2013 service accounts file system permission:
  
|**File system path**|**Permissions**|**Inherit**|**Description**|
|:-----|:-----|:-----|:-----|
|%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS|Modify|No|This directory contains setup and runtime tracing logs. If this directory is altered, diagnostic logging will not function correctly. All SharePoint 2013 service accounts must have write permission to this directory.|
