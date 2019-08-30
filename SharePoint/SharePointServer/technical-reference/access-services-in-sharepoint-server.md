---
title: "Access Services in SharePoint Server knowledge articles"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0f33d9cc-7b26-4418-b901-bf773abaf574
description: "Learn how to resolve alerts about Access Services in the SharePoint Server management pack for Systems Center Operations Manager (SCOM)."
---

# Access Services in SharePoint Server knowledge articles

[!INCLUDE[appliesto-2013-2016-xxx-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Learn how to resolve alerts about Access Services in the SharePoint Servers 2019, 2016 and 2013 management pack for Systems Center Operations Manager (SCOM).
  
The articles in this section are knowledge articles for Access Services in SharePoint Server. Typically, you would see these articles after clicking a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in Access Services in SharePoint Server.

> [!NOTE]
>  Access Services 2010 and 2013 are deprecated but will remain supported for SharePoint Server 2019. We recommend to explore Microsoft [PowerApps](https://powerapps.microsoft.com/) and [Flows](http://flow.microsoft.com/) as potential alternatives to Access Services 2010 and 2013.

Download and install:

- [System Center Management Pack for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57776)

- [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409) 

- [System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568) 

- [System Center Monitoring Pack for SharePoint Foundation 2013](https://go.microsoft.com/fwlink/p/?LinkId=272567)

Use the following information to resolve the Access Services error messages:
  
- [No application info from content database](#NoAppInfo)
    
- [WFE to ADS communication failure](#WFEADS)
    
- [No servers available for database creation](#NoServers)
    
- [Partitioned SSS communication failure](#SSSFail)
    
- [Unpartitioned SSS communication failure](#SSSFailUnpart)
    
- [Trigger for excessive failed SQL connections requests](#TrigSQLReq)
    
- [Excessive failed SQL connections](#SQLCon)
    
- [Trigger for excessive SQL connection retries](#TrigSQLRetries)
    
- [Excessive SQL connection retries](#SQLRetries)
    
- [Trigger for excessive SQL write failures](#TrigSQLWrite)
    
- [Excessive SQL write failures](#SQLWrite)
    
- [No available ADS servers](#NoADS)
    
- [No default proxy](#NoProxy)
    
- [Failed to register database server](#NoDBServ)
    
## No application info from content database
<a name="NoAppInfo"> </a>

 **Alert Name:** Access Services: No application info from content database 
  
 **Summary:** Access Data Services tries to retrieve application information from the SharePoint Content Database, but cannot find the relevant app's information. If this occurs, the application will not be available for use. 
  
### Cause

Someone creates a site that uses an Access template that is not actually an Access application.
  
### Resolution

Delete the site that is created incorrectly.
  
## WFE to ADS communication failure
<a name="WFEADS"> </a>

 **Alert Name:** Access Services: WFE to ADS communication failure 
  
 **Summary:** Access Data Services WFE (Web Front End) is unable to communicate with the ADS (Access Data Services) middle tier. 
  
### Cause

One or more of the following might be the cause:
  
- Network issues
    
- Hardware failure
    
- SharePoint service failure
    
- Disabled Access Database Services on the server
    
### Resolution

1. Ensure that network is healthy.
    
2. Ensure that ADS server is available.
    
3. Ensure that ADS server can be accessed from WFE.
    
4. Ensure IIS Process for ADS application pool is running.
    
5. Ensure that the ADS service is enabled on the failing ADS server.
    
## No servers available for database creation
<a name="NoServers"> </a>

 **Alert Name:** Access Services: No servers available for database creation 
  
 **Summary:** During application creation, Access Data services cannot find an available SQL Server to provision the new database. 
  
### Cause

No SQL database servers are configured for Access to provision new databases.
  
### Resolution

- If the creation failure occurs while creating from the Access client, check the Database Server group mappings to determine where the shortage has occurred:
    
  - Use  `Get-SPAccessServicesDatabaseServerGroupMapping` to determine whether there is a mapping from the Object Model to the Server Group. 
    
  - Use  `Get-SPAccessServicesDatabaseServerGroup` to determine whether the server group has at least one database. 
    
  - Use  `Get-SPAccessServicesDatabaseServer` to determine whether there is at least one database in the server group marked as "AvailableForCreate". 
    
- If the creation failure occurs while creating from the Corporate Catalog, check the Database Server group mappings to determine where the shortage has occurred:
    
  - Use  `Get-SPAccessServicesDatabaseServerGroupMapping` to determine whether there is a mapping from the Corporate Catalog to the Server Group. 
    
  - Use  `Get-SPAccessServicesDatabaseServerGroup` to determine whether the server group has at least one database. 
    
  - Use  `Get-SPAccessServicesDatabaseServer` to determine whether there is at least one database in the server group marked as "AvailableForCreate". 
    
### Related topics

[Get-SPAccessServicesDatabaseServerGroupMapping](/powershell/module/sharepoint-server/Get-SPAccessServicesDatabaseServerGroupMapping?view=sharepoint-ps)
  
[Get-SPAccessServicesDatabaseServerGroup](/powershell/module/sharepoint-server/Get-SPAccessServicesDatabaseServerGroup?view=sharepoint-ps)
  
[Get-SPAccessServicesDatabaseServer](/powershell/module/sharepoint-server/Get-SPAccessServicesDatabaseServer?view=sharepoint-ps)
  
## Partitioned SSS communication failure
<a name="SSSFail"> </a>

 **Alert Name:** Access Services: Partitioned SSS communication failure 
  
 **Summary:** Access Data Services tries to communicate with SharePoint partitioned Secure Store Service, but is unable to communicate with it. 
  
### Cause

Partitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.
  
### Resolution

1. Ensure partitioned Secure Store Service Application exists and is running.
    
2. Ensure Proxy for partitioned Secure Store Service exists and is in the default Proxy group.
    
### Related topics

[Configure the Secure Store Service in SharePoint Server](../administration/configure-the-secure-store-service.md)
  
## Unpartitioned SSS communication failure
<a name="SSSFailUnpart"> </a>

 **Alert Name:** Access Services: Unpartitioned SSS communication failure 
  
 **Summary:** Access Data Services tries to communicate with SharePoint unpartitioned Secure Store Service, but is unable to communicate with it. 
  
### Cause

Unpartitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.
  
### Resolution

1. Ensure unpartitioned Secure Store Service Application exists and is running.
    
2. Ensure Proxy for unpartitioned Secure Store Service exists and is in the default Proxy group.
    
### Related topics

[Configure the Secure Store Service in SharePoint Server](../administration/configure-the-secure-store-service.md)
  
## Trigger for excessive failed SQL connections requests
<a name="TrigSQLReq"> </a>

 **Alert Name:** Access Services: Trigger for excessive failed SQL connections requests 
  
 **Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the SQL Server Databases. 
  
### Cause

SQL Server database server is down, unavailable, or unreachable. 
  
### Resolution

- Check network health.
    
- Make sure that the SQL Server database server is available and healthy.
    
## Excessive failed SQL connections
<a name="SQLCon"> </a>

 **Alert Name:** Access Services: Excessive failed SQL connections 
  
 **Summary:** This tracks the number of failed SQL connections. 
  
### Cause

N/A
  
### Resolution

N/A
  
## Trigger for excessive SQL connection retries
<a name="TrigSQLRetries"> </a>

 **Alert Name:** Access Services: Trigger for excessive SQL connection retries 
  
 **Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the Application SQL Databases. 
  
### Cause

One or more of the following might be the cause:
  
- Network issues
    
- Application SQL databases are unavailable or unreachable.
    
### Resolution

1. Check network health.
    
2. Check Application SQL databases availability and healthy states.
    
## Excessive SQL connection retries
<a name="SQLRetries"> </a>

 **Alert Name:** Access Services: Excessive SQL connection retries 
  
 **Summary:** This monitors the number of SQL Database Server Connection retries. 
  
### Cause

N/A
  
### Resolution

N/A
  
## Trigger for excessive SQL write failures
<a name="TrigSQLWrite"> </a>

 **Alert Name:** Access Services: Trigger for excessive SQL write failures 
  
 **Summary:** This alert occurs if there are too many SQL Write failures. 
  
### Cause

Excessive number of SQL Write failures.
  
### Resolution

1. Check network health.
    
2. Check status of SQL Azure service.
    
3. Raise an incident with SQL Azure for resolution.
    
## Excessive SQL write failures
<a name="SQLWrite"> </a>

 **Alert Name:** Access Services: Excessive SQL write failures 
  
 **Summary:** Monitors the number of failed SQL Database Server writes 
  
### Cause

One or more of the following might be the cause:
  
- Application SQL Databases are unavailable or unreachable.
    
- Deadlock occurs on the server.
    
- Excessive server load makes the database server unresponsive.
    
### Resolution

Ensure that the Database server is available, is not overloaded, and has no deadlocks.
  
## No available ADS servers
<a name="NoADS"> </a>

 **Alert Name:** Access Services: No available ADS servers 
  
 **Summary:** There are no Access Data Services Servers or the available Access Data Services Servers are not healthy enough to serve the request. 
  
### Cause

One or more of the following might be the cause:
  
- Excessive memory consumption overloads your ADS Servers.
    
- Network problems
    
- A number of Access Database Server instances fail or are down.
    
### Resolution

1. Ensure that Access Database Services is enabled on at least one server in the farm.
    
2. Reboot Access Database Service instances to free memory.
    
3. Ensure Access Database Service instances are available and are configured correctly.
    
## No default proxy
<a name="NoProxy"> </a>

 **Alert Name:** Access Services: No default proxy 
  
 **Summary:** There is no Access Data Services Proxy in the Default Proxy group. 
  
### Cause

No default proxy is established during configuration, or there is a problem during provisions and a default proxy is not established.
  
### Resolution

Use  `new-SPAccessServicesApplicationProxy` to create a new default proxy. 
  
### Related topics

[New-SPAccessServicesApplication](/powershell/module/sharepoint-server/New-SPAccessServicesApplication?view=sharepoint-ps)
  
## Failed to register database server
<a name="NoDBServ"> </a>

 **Alert Name:** Access Services: Failed to register database server 
  
 **Summary:** During Database server configuration, a server fails to register. 
  
### Cause

One or more of the following might be the cause:
  
- Network issues connecting to the server
    
- Incorrect Database server version
    
- Server does not have required features or insufficient permissions
    
### Resolution

1. Check network health.
    
2. Update the database server version.
    
3. Install required features or update permissions.
    
> [!NOTE]
> App pool user must have DBCreator and SecurityAdmin permissions. 
  
## See also
<a name="NoDBServ"> </a>

#### Concepts

[Plan for monitoring in SharePoint Server](../administration/monitoring-planning.md)
  
#### Other Resources

[System Center Monitoring Pack for SharePoint Foundation](http://go.microsoft.com/fwlink/p/?LinkId=272567)
  
[System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568)
  
[System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409)

