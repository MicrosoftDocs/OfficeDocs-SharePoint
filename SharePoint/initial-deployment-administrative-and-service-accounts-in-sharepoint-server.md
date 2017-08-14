---
title: Initial deployment administrative and service accounts in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 06765032-fedb-4b73-a019-f096b48cd2a8
---


# Initial deployment administrative and service accounts in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-03* **Summary:** Learn about the administrative and service accounts you need to initially install SharePoint Server 2013 and SharePoint Server 2016.This article provides information about the administrative and service accounts that you need for an initial SharePoint Server deployment. Additional accounts and permissions are required to fully implement all aspects of a production farm.
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    


## Required accounts in SharePoint Server

To deploy SharePoint Server on a server farm, you must provide credentials for several different accounts.The following table describes the accounts that you can use to install and configure SharePoint Server.
### 

AccountPurposeRequirementsSQL Server service account  <br/>  The SQL Server service account is used to run SQL Server. It is the service account for the following SQL Server services: <br/>  MSSQLSERVER <br/>  SQLSERVERAGENT <br/>  If you do not use the default SQL Server instance, in the Windows Services console, these services will be shown as the following: <br/>  MSSQL<InstanceName> <br/>  SQLAgent<InstanceName> <br/> Use either a Local System account or a domain user account.  <br/> If you plan to back up to or restore from an external resource, permissions to the external resource must be granted to the appropriate account. If you use a domain user account for the SQL Server service account, grant permissions to that domain user account. However, if you use the Network Service or the Local System account, grant permissions to the external resource to the machine account (<domain_name>\\<SQL_hostname>).  <br/> The instance name is arbitrary and was created when SQL Server was installed.  <br/> Setup user account  <br/>  The Setup user account is used to run the following: <br/>  Setup <br/>  SharePoint Products Configuration Wizard <br/>  Domain user account. <br/>  Member of the Administrators group on each server on which Setup is run. <br/>  SQL Server login on the computer that runs SQL Server. <br/>  Member of the following SQL Server roles: <br/> **securityadmin** fixed server role <br/> **dbcreator** fixed server role <br/>  If you run Windows PowerShell cmdlets that affect a database, this account must be a member of the **db_owner** fixed database role for the database. <br/> Server farm account or database access account  <br/>  The server farm account is used to perform the following tasks: <br/>  Configure and manage the server farm. <br/>  Act as the application pool identity for the SharePoint Central Administration website. <br/>  Run the Microsoft SharePoint Foundation Workflow Timer Service. <br/>  Domain user account. <br/>  Additional permissions are automatically granted for the server farm account on Web servers and application servers that are joined to a server farm. <br/>  The server farm account is automatically added as a SQL Server login on the computer that runs SQL Server. The account is added to the following SQL Server security roles: <br/> **dbcreator** fixed server role <br/> **securityadmin** fixed server role <br/> **db_owner** fixed database role for all SharePoint databases in the server farm <br/> 
> [!NOTE:]

  
    
    


