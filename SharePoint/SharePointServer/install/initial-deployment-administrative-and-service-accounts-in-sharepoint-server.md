---
title: "Initial deployment administrative and service accounts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/3/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 06765032-fedb-4b73-a019-f096b48cd2a8
description: "Learn about the administrative and service accounts you need to initially install SharePoint Server."
---

# Initial deployment administrative and service accounts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article provides information about the administrative and service accounts that you need for an initial SharePoint Server deployment. Additional accounts and permissions are required to fully implement all aspects of a production farm.
  
> [!NOTE]
> For a complete list of permissions for SharePoint Servers 2016 and 2019, see [Account permissions and security settings in SharePoint Servers 2016 and 2019](account-permissions-and-security-settings-in-sharepoint-server-2016.md). > For a complete list of permissions for SharePoint Server 2013, see [Account permissions and security settings in SharePoint 2013](account-permissions-and-security-settings-in-sharepoint-2013.md). 
  
> [!IMPORTANT]
> Do not use service account names that contain the symbol $ with the exception of using a Group Managed Service Account for SQL Server.
  
## Required accounts in SharePoint Server

To deploy SharePoint Server on a server farm, you must provide credentials for several different accounts.
  
The following table describes the accounts that you can use to install and configure SharePoint Server.
  
|**Account**|**Purpose**|**Requirements**|
|:-----|:-----|:-----|
|SQL Server service account  <br/> | The SQL Server service account is used to run SQL Server. It is the service account for the following SQL Server services:  <br/>  MSSQLSERVER  <br/>  SQLSERVERAGENT  <br/>  If you do not use the default SQL Server instance, in the Windows Services console, these services will be shown as the following:  <br/>  MSSQL\<InstanceName\>  <br/>  SQLAgent\<InstanceName\>  <br/> |Use either a domain user account or preferably, a [Group Managed Service Account](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview).  <br/> If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account or Group Managed Service Account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant permissions to the external resource to the machine account (\<domain_name\>\\<SQL_hostname\>).  <br/> The instance name is arbitrary and was created when SQL Server was installed.  <br/> |
|Farm administrator user account  <br/> | The farm administrator user account is a uniquely identifiable account assigned to a SharePoint administrator. It is used to run the following:  <br/>  Setup  <br/>  SharePoint Products Configuration Wizard  <br/> | Domain user account.  <br/>  Member of the Administrators group on each SharePoint server in the farm.  <br/>  Member of the following SQL Server role (optional): **sysadmin** fixed server role.  <br/>  If you run Windows PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database or a member of the **sysadmin** fixed server role on SQL.  <br/> |
|Farm service account <br/> | The farm service account is used to perform the following tasks:  <br/>  Act as the application pool identity for the SharePoint Central Administration website.  <br/>  Run the Microsoft SharePoint Foundation Workflow Timer Service.  <br/> | Domain user account.  <br/>  Additional permissions are automatically granted for the server farm account on Web servers and application servers that are joined to a server farm.  <br/>  The server farm account is automatically added as a SQL Server login on the computer that runs SQL Server. The account is added to the following SQL Server security roles:  <br/> * **dbcreator** fixed server role  <br/> * **securityadmin** fixed server role  <br/> * **db_owner** fixed database role for all SharePoint databases in the server farm  <br/> This account should not be used interactively by an administrator. |
   
> [!NOTE]
> We recommend that you install SharePoint Server by using least-privilege administration.
