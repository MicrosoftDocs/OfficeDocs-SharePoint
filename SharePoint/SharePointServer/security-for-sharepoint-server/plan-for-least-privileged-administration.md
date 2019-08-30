---
title: "Plan for least-privileged administration in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/5/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ef4c6a39-24f8-469e-9b14-0abfadaa6c8b
description: "Learn about how to use least-privileged administration to configure and maintain a SharePoint Server farm and enhance security."
---

# Plan for least-privileged administration in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The concept of least-privileged administration is to assign users the minimum permissions that are required for users to complete authorized tasks. The goal of least-privileged administration is to configure and help maintain secure control of an environment. The result is that each account under which a service runs is granted access to only the resources that are absolutely necessary.
  
We recommend that you deploy SharePoint Server with least-privileged administration even though implementing least-privileged administration can result in increased operational costs because additional resources might be required to maintain this level of administration. Moreover, the ability to troubleshoot security problems can also be made more complex.
  
    
## Introduction
<a name="Introduction"> </a>

Organizations implement least-privileged administration to achieve better security than would be typically recommended. Only a small percentage of organizations require this heightened level of security because of the resource costs of maintaining least-privileged administration. Some deployments that might require this heightened level of security include governmental agencies, security organizations, and organizations in the financial services industry. The implementation of a least-privileged environment should not be confused with best practices. In a least-privileged environment, administrators implement best practices together with additional heightened levels of security.
  
## Least-privileged environment for accounts and services
<a name="AcctServices"> </a>

To plan for least-privileged administration, you must consider several accounts, roles, and services. Some apply to SQL Server and some apply to SharePoint Server. As administrators lock down additional accounts and services, daily operational costs are likely to increase.
  
### SQL Server roles
<a name="SQLRoles"> </a>

In a SharePoint Server environment, several accounts may be granted the following two SQL Server server-level roles. In a least-privileged SharePoint Server environment, we recommend that you only grant these privileges to the account under which the Microsoft SharePoint Foundation Workflow Timer Service runs. Typically, the timer service runs under the server farm account. For day-to-day operations, we recommend that you remove the following two SQL Server server-level roles from all other accounts that are used for SharePoint administration:
  
- **Dbcreator** - Members of the dbcreator fixed server role can create, alter, drop, and restore any database. 
    
- **Securityadmin** - Members of the securityadmin fixed server role manage logins and their properties. They can GRANT, DENY, and REVOKE server-level permissions. They can also GRANT, DENY, and REVOKE database-level permissions if they have access to a database. Additionally, they can reset passwords for SQL Server logins. 
    
    > [!SECURITY NOTE]
    > The ability to grant access to the database engine and to configure user permissions allows the securityadmin to assign most server permissions. You should treat the securityadmin role as equal to the sysadmin role. 
  
For additional information about SQL Server server-level roles, see [Server Level Roles](https://go.microsoft.com/fwlink/p/?LinkId=213450).
  
If you remove one or more of these SQL Server roles, you might receive "Unexpected" error messages in the Central Administration web site. In addition, you may receive the following message in the Unified Logging Service (ULS) log file:
  
 **System.Data.SqlClient.SqlException… \<operation type\> permission denied in database \<database\>. Table \<table\>**
  
Along with an error message that may be displayed, you may be unable to perform any of the following tasks:
  
- Restore a backup of a farm because you can't write to a database
    
- Provision a service instance or web application
    
- Configure managed accounts
    
- Change managed accounts for web applications
    
- Perform any action on any database, managed account, or service that requires the Central Administration web site
    
In certain situations, database administrators (DBAs) may want to operate independently from SharePoint Server administrators and create and manage all the databases. This is typical in IT environments where security requirements and company policies require a separation of administrator roles. The farm administrator provides SharePoint Server database requirements to the DBA, who then creates the necessary databases and sets up the logins that are required for the farm.
  
By default, the DBA has complete access to the SQL Server instance but requires additional permissions to access SharePoint Server. DBAs typically use Windows PowerShell 3.0 when they add, create, move, or rename SharePoint databases, so they must be a member of the following accounts:
  
- **Securityadmin** fixed server role on the SQL Server instance. 
    
- **Db_owner** fixed database role on all databases in the SharePoint farm. 
    
- Administrators group on the computer on which they run the PowerShell cmdlets.
    
Additionally, the DBA may have to be a member of the **SharePoint_Shell_Access** role to access the SharePoint content database. In some conditions, the DBA may want to add the Setup user account to the **db_owner** role. 
  
### SharePoint Server roles and services
<a name="SPRolesandServices"> </a>

In general, you should remove the ability to create new databases from SharePoint Server service accounts. Other than the account under which the timer service runs (typically the farm account), no SharePoint Server service account should have the sysadmin role on the SQL Server instance and no SharePoint Server service account should be a local Administrator on the server that runs SQL Server.
  
For more information about SharePoint Server accounts, see [Account permissions and security settings in SharePoint Server 2016](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md).
  
For account information in SharePoint Server 2013, see [Account permissions and security settings in SharePoint 2013](../install/account-permissions-and-security-settings-in-sharepoint-2013.md).
  
The following list provides information about locking down other SharePoint Server roles and services:
  
- **SharePoint_Shell_Access role**
    
    When you remove this SQL Server role, you remove the ability to write entries to the configuration and content database and the ability to perform any tasks by using Microsoft PowerShell. For additional information about this role, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
    
- **SharePoint Timer service (SPTimerV4)**
    
    We recommend that you do not limit the default permissions granted to the account under which this service runs and that you never disable this account. Instead, use a secure user account, for which the password is not widely known, and leave the service running. By default, this service is installed when you install SharePoint Server and maintains configuration cache information. If you set the service type to disabled you may experience the following behavior:
    
  - Timer jobs won't run
    
  - Health analyzer rules won't run
    
  - Maintenance and farm configuration will be out of date
    
- **SharePoint Administration service (SPAdminV4)**
    
    This service performs automated changes that require local administrator permission on the server. When the service is not running, you must manually process server-level administrative changes. We recommend that you do not limit the default permissions granted to the account under which this service runs and that you never disable this account. Instead, use a secure user account, for which the password is not widely known, and leave the service running. If you set the service type to disabled, you may experience the following behavior:
    
  - Administrative timer jobs won't run
    
  - Web configuration files won't be updated
    
  - Security and local groups won't be updated
    
  - Registry values and keys won't be written
    
  - Services may be unable to be started or restarted
    
  - Provisioning of services may be unable to be completed
    
- **SPUserCodeV4 Service**
    
    This service lets a site collection administrator upload sandboxed solutions to the Solutions gallery. If you are not using sandboxed solutions, you can disable this service.
    
- **Claims To Windows Token service (C2WTS)**
    
    By default, this service is disabled. The C2WTS service may be required for a deployment with Excel Services, PerformancePoint Servers, or SharePoint shared services that must translate between SharePoint security tokens and Windows-based identities. For example, you use this service when you configure Kerberos-constrained delegation for accessing external data sources. For more information about C2WTS, see [Plan for Kerberos authentication in SharePoint Server](kerberos-authentication-planning.md).
    
The following features may experience additional symptoms under certain circumstances:
  
- **Backup and restore**
    
    The ability to perform a restore from a backup may fail if you have removed database permissions.
    
- **Upgrade**
    
    The upgrade process starts correctly, but then fails if you do not have suitable permissions to databases. If your organization is already in a least-privileged environment, the workaround is to move to a best practices environment to complete the upgrade, and then move back to a least-privileged environment. 
    
- **Update**
    
    The ability to apply a software update to a farm will succeed for the schema of the configuration database, but fail on the content database and services.
    
### Additional things to consider for a least-privileged environment
<a name="additionalReq"> </a>

In addition to the previous considerations, you might have to consider more operations. The following list is incomplete. Selectively use the items at your own discretion:
  
- **Setup user account** - This account is used to set up each server in a farm. The account must be a member of the Administrators group on each server in the SharePoint Server farm. For additional information about this account, see [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
- **Synchronization account** - For SharePoint Server Server, this account is used to connect to the directory service. We recommend that you do not limit the default permissions granted to the account under which this service runs and that you never disable this account. Instead, use a secure user account, for which the password is not widely known, and leave the service running. This account also requires Replicate Directory Changes permission on AD DS which enables the account to read AD DS objects and to discover AD DS objects that were changed in the domain. The Grant Replicate Directory Changes permission does not enable an account to create, change or delete AD DS objects. 
    
- **My Site host application pool account** - This is the account under which the My Site application pool runs. To configure this account, you must be a member of the Farm Administrators group. You can limit privileges to this account. 
    
- **Built-in user group** - Removing the built-in user security group or changing the permissions may have unanticipated consequences. We recommend that you do not limit privileges to any built-in accounts or groups. 
    
- **Group permissions** - By default the **WSS_ADMIN_WPG** SharePoint group has read and write access to local resources. The following **WSS_ADMIN_WPG** file system locations,  _%WINDIR%\System32\drivers\etc\Hosts_ and  _%WINDIR%\Tasks_ are needed for SharePoint Server to work correctly. If other services or applications are running on a server, you might consider how they access the Tasks or Hosts folder locations. For additional information about account settings for SharePoint Server, see [Account permissions and security settings in SharePoint Server 2016](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md). 
    
    For account information in SharePoint Server 2013, see [Account permissions and security settings in SharePoint 2013](../install/account-permissions-and-security-settings-in-sharepoint-2013.md).
    
- **Change permission of a service** - A change of a permission of a service may have unanticipated consequences. For example, if the following registry key, HKLM\System\CurrentControlSet\Services\PerfProc\Performance\Disable Performance Counters, has the value of 0, the User Code Host service would be disabled which would cause sandboxed solutions to stop working. 
    
## See also
<a name="AcctServices"> </a>

#### Other Resources

[Least Privilege Configuration for Workflow Manager with SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=288780)

