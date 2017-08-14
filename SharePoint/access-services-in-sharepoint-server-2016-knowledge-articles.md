---
title: Access Services in SharePoint Server 2016 knowledge articles
ms.prod: SHAREPOINT
ms.assetid: 0f33d9cc-7b26-4418-b901-bf773abaf574
---


# Access Services in SharePoint Server 2016 knowledge articles
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-09-16* Learn how to resolve alerts about Access Services in the SharePoint Server 2016 management pack for Systems Center Operations Manager (SCOM).The articles in this section are knowledge articles for UNRESOLVED_TOKEN_VAL(AccessServices_2nd_NoVerr) in SharePoint Server 2016. Typically, you would see these articles after clicking a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in Access Services in SharePoint Server 2016. Download and install  [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409).
-  [Access Services: No application info from content database](#NoAppInfo)
    
  
-  [Access Services: WFE to ADS communication failure](#WFEADS)
    
  
-  [Access Services: No servers available for database creation](#NoServers)
    
  
-  [Access Services: Partitioned SSS communication failure](#SSSFail)
    
  
-  [Access Services: Unpartitioned SSS communication failure](#SSSFailUnpart)
    
  
-  [Access Services: Trigger for excessive failed SQL connections requests](#TrigSQLReq)
    
  
-  [Access Services: Excessive failed SQL connections](#SQLCon)
    
  
-  [Access Services: Trigger for excessive SQL connection retries](#TrigSQLRetries)
    
  
-  [Access Services: Excessive SQL connection retries](#SQLRetries)
    
  
-  [Access Services: Trigger for excessive SQL write failures](#TrigSQLWrite)
    
  
-  [Access Services: Excessive SQL write failures](#SQLWrite)
    
  
-  [Access Services: No available ADS servers](#NoADS)
    
  
-  [Access Services: No default proxy](#NoProxy)
    
  
-  [Access Services: Failed to register database server](#NoDBServ)
    
  

## No application info from content database
<a name="NoAppInfo"> </a>

 **Alert Name:** Access Services: No application info from content database **Summary:** Access Data Services tries to retrieve application information from the SharePoint Content Database, but cannot find the relevant app's information. If this occurs, the application will not be available for use.
## Cause

Someone creates a site that uses an Access template that is not actually an Access application.
## Resolution

Delete the site that is created incorrectly.
## WFE to ADS communication failure
<a name="WFEADS"> </a>

 **Alert Name:** Access Services: WFE to ADS communication failure **Summary:** Access Data Services WFE (Web Front End) is unable to communicate with the ADS (Access Data Services) middle tier.
## Cause

One or more of the following might be the cause:
- Network issues
    
  
- Hardware failure
    
  
- SharePoint service failure
    
  
- Disabled Access Database Services on the server
    
  

## Resolution


1. Ensure that network is healthy.
    
  
2. Ensure that ADS server is available.
    
  
3. Ensure that ADS server can be accessed from WFE.
    
  
4. Ensure IIS Process for ADS application pool is running.
    
  
5. Ensure that the ADS service is enabled on the failing ADS server.
    
  

## No servers available for database creation
<a name="NoServers"> </a>

 **Alert Name:** Access Services: No servers available for database creation **Summary:** During application creation, Access Data services cannot find an available SQL Server to provision the new database.
## Cause

No SQL database servers are configured for Access to provision new databases.
## Resolution


- If the creation failure occurs while creating from the Access client, check the Database Server group mappings to determine where the shortage has occurred:
    
1. Use Get-SPAccessServicesDatabaseServerGroupMapping to determine whether there is a mapping from the Object Model to the Server Group.
    
  
2. Use Get-SPAccessServicesDatabaseServerGroup to determine whether the server group has at least one database.
    
  
3. Use Get-SPAccessServicesDatabaseServer to determine whether there is at least one database in the server group marked as "AvailableForCreate".
    
  
- If the creation failure occurs while creating from the Corporate Catalog, check the Database Server group mappings to determine where the shortage has occurred:
    
1. Use Get-SPAccessServicesDatabaseServerGroupMapping to determine whether there is a mapping from the Corporate Catalog to the Server Group.
    
  
2. Use Get-SPAccessServicesDatabaseServerGroup to determine whether the server group has at least one database.
    
  
3. Use Get-SPAccessServicesDatabaseServer to determine whether there is at least one database in the server group marked as "AvailableForCreate".
    
  

## Related topics

 **Get-SPAccessServicesDatabaseServerGroupMapping** **Get-SPAccessServicesDatabaseServerGroup** **Get-SPAccessServicesDatabaseServer**
## Partitioned SSS communication failure
<a name="SSSFail"> </a>

 **Alert Name:** Access Services: Partitioned SSS communication failure **Summary:** Access Data Services tries to communicate with SharePoint partitioned Secure Store Service, but is unable to communicate with it.
## Cause

Partitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.
## Resolution


1. Ensure partitioned Secure Store Service Application exists and is running.
    
  
2. Ensure Proxy for partitioned Secure Store Service exists and is in the default Proxy group.
    
  

## Related topics


## Unpartitioned SSS communication failure
<a name="SSSFailUnpart"> </a>

 **Alert Name:** Access Services: Unpartitioned SSS communication failure **Summary:** Access Data Services tries to communicate with SharePoint unpartitioned Secure Store Service, but is unable to communicate with it.
## Cause

Unpartitioned Secure Store Service in the farm is down or unreachable because of Network issues or incorrect configurations.
## Resolution


1. Ensure unpartitioned Secure Store Service Application exists and is running.
    
  
2. Ensure Proxy for unpartitioned Secure Store Service exists and is in the default Proxy group.
    
  

## Related topics


## Trigger for excessive failed SQL connections requests
<a name="TrigSQLReq"> </a>

 **Alert Name:** Access Services: Trigger for excessive failed SQL connections requests **Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the SQL Server Databases.
## Cause

SQL Server database server is down, unavailable, or unreachable. 
## Resolution


- Check network health.
    
  
- Make sure that the SQL Server database server is available and healthy.
    
  

## Excessive failed SQL connections
<a name="SQLCon"> </a>

 **Alert Name:** Access Services: Excessive failed SQL connections **Summary:** This tracks the number of failed SQL connections.
## Cause

N/A
## Resolution

N/A
## Trigger for excessive SQL connection retries
<a name="TrigSQLRetries"> </a>

 **Alert Name:** Access Services: Trigger for excessive SQL connection retries **Summary:** This alert occurs when Access Data services exceed the expected number of retries when the services connect to the Application SQL Databases.
## Cause

One or more of the following might be the cause:
- Network issues
    
  
- Application SQL databases are unavailable or unreachable.
    
  

## Resolution


1. Check network health.
    
  
2. Check Application SQL databases availability and healthy states.
    
  

## Excessive SQL connection retries
<a name="SQLRetries"> </a>

 **Alert Name:** Access Services: Excessive SQL connection retries **Summary:** This monitors the number of SQL Database Server Connection retries.
## Cause

N/A
## Resolution

N/A
## Trigger for excessive SQL write failures
<a name="TrigSQLWrite"> </a>

 **Alert Name:** Access Services: Trigger for excessive SQL write failures **Summary:** This alert occurs if there are too many SQL Write failures.
## Cause

Excessive number of SQL Write failures.
## Resolution


1. Check network health.
    
  
2. Check status of SQL Azure service.
    
  
3. Raise an incident with SQL Azure for resolution.
    
  

## Excessive SQL write failures
<a name="SQLWrite"> </a>

 **Alert Name:** Access Services: Excessive SQL write failures **Summary:** Monitors the number of failed SQL Database Server writes
## Cause

One or more of the following might be the cause:
- Application SQL Databases are unavailable or unreachable.
    
  
- Deadlock occurs on the server.
    
  
- Excessive server load makes the database server unresponsive.
    
  

## Resolution

Ensure that the Database server is available, is not overloaded, and has no deadlocks.
## No available ADS servers
<a name="NoADS"> </a>

 **Alert Name:** Access Services: No available ADS servers **Summary:** There are no Access Data Services Servers or the available Access Data Services Servers are not healthy enough to serve the request.
## Cause

One or more of the following might be the cause:
- Excessive memory consumption overloads your ADS Servers.
    
  
- Network problems
    
  
- A number of Access Database Server instances fail or are down.
    
  

## Resolution


1. Ensure that Access Database Services is enabled on at least one server in the farm.
    
  
2. Reboot Access Database Service instances to free memory.
    
  
3. Ensure Access Database Service instances are available and are configured correctly.
    
  

## No default proxy
<a name="NoProxy"> </a>

 **Alert Name:** Access Services: No default proxy **Summary:** There is no Access Data Services Proxy in the Default Proxy group.
## Cause

No default proxy is established during configuration, or there is a problem during provisions and a default proxy is not established.
## Resolution

Use new-SPAccessServicesApplicationProxy to create a new default proxy.
## Related topics

 **New-SPAccessServicesApplication**
## Failed to register database server
<a name="NoDBServ"> </a>

 **Alert Name:** Access Services: Failed to register database server **Summary:** During Database server configuration, a server fails to register.
## Cause

One or more of the following might be the cause:
- Network issues connecting to the server
    
  
- Incorrect Database server version
    
  
- Server does not have required features or insufficient permissions
    
  

## Resolution


1. Check network health.
    
  
2. Update the database server version.
    
  
3. Install required features or update permissions.
    
  

> [!NOTE:]

  
    
    


# See also

#### 

 [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409)
  
    
    

  
    
    

