---
title: "Disaster Recovery best practices for SharePoint Server and Access Services"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/10/2018
audience: ITPro
ms.topic: reference
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 52966fa3-1654-41b2-aea5-d1d5d007534e
description: "Learn how to apply a disaster recovery strategy for Access Services in SharePoint Server."
---

# Disaster Recovery best practices for SharePoint Server and Access Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The article explains how to successfully implement a disaster recovery (DR) strategy for Access Services service applications for SharePoint Server.
  
Thanks to Neil Hodgkinson, Microsoft Senior Program Manager for testing this disaster recovery strategy and providing the content for this article.
  
## Overview of Access Services and Disaster Recovery

SharePoint 2010 introduced the concept of Access Services as an integrated service application in [Introduction to Access Services](/previous-versions/office/sharepoint-server-2010/ee748634(v=office.14)). The data was held in SharePoint lists and could be accessed with a browser or the Microsoft Access 2010 Client. In SharePoint 2013 the Access Services architecture changed, and introduced the concept of Contained databases, moving the data out of SharePoint lists and instead into a SQL Server 2012 Application database. This architecture remains in place for the SharePoint Server 2016 release. 
  
There are multiple ways to configure your SharePoint Server farm for disaster recovery. The method you choose will depend entirely on your requirements for allowed data loss and minimum downtime in your organization. Microsoft has documented various approaches in [Choose a disaster recovery strategy for SharePoint Server](plan-for-disaster-recovery.md).
  
Regardless of your choice of technologies there are a few requirements and best-practices for configuring a disaster recovery farm to support Access Services. These are detailed below.
  
> [!IMPORTANT]
> Before you can use any of the Microsoft PowerShell cmdlets detailed in the steps below, verify that you meet all of the requirements in [Permissions](/powershell/module/sharepoint-server/?view=sharepoint-ps#section3). 
  
## Step 1: Setting up SharePoint Server for Disaster Recovery

The goal of this step is to create a smoother disaster recovery experience by removing potential points of failure. By matching Authentication Realms, and Database Server ReferenceIDs so they are the same in the disaster recovery farm as in the primary farm, you will be prepared for recovery. Likewise, it is essential to know which databases must be managed in order to recover successfully.
  
Let's drill into the details, below.
  
### a. Use the same Authentication Realm

Setting a new authentication realm blocks access for all SharePoint apps that use access tokens. Access Services applications rely on the app infrastructure. With this in mind it makes sense for a disaster recovery farm to use the same authentication realm as the primary farm. You should set the authentication realm as one of the initial setup steps when deploying the DR farm.
  
To get the authentication realm of the primary farm use thisPowerShell command:
  
```
 Get-SPAuthenticationRealm
```

 **Example:** A sample authentication realm is a GUID, so the returned value might look like this: 4a2cc8f8-51ab-4367-8a76-ab629c882a68. 
  
Using that GUID as our example, set it on the secondary farm using these PowerShell commands:
  
```
Set-SPAuthenticationRealm -Realm 4a2cc8f8-51ab-4367-8a76-ab629c882a68
Restart-Service sptimerv4
Restart-Service spadminv4
```

> [!IMPORTANT]
> Restarting the SharePoint Timer service and SharePoint Admin service is recommended after changing the Authentication Realm. You may need to schedule time during which you can perform an IISReset (SharePoint sites will be unavailable until the successful end of an IISReset). 
  
### b. Use the same Database Server ReferenceID

Access Services in SharePoint Server 2013 and SharePoint Server 2016 use a SQL Server to host the individual databases that support Access-based Apps. Internally, these database servers aren't referenced by name, but by a **ReferenceID**. 
  
> [!IMPORTANT]
> It's critical to the success of your disaster recovery strategy that the database servers in the secondary data center be registered as application server hosts using the exact same **ReferenceID** as their primary partner. This can only be done by registering the database servers by using PowerShell. 
  
#### Register the primary farm's Access Services database server

```
$serverGroupName = 'DEFAULT'
$ASapp = Get-SPAccessServicesApplication
$app = $Null
if ($ASapp.length -ne $Null) { $app = $ASapp[0] } else { $app = $ASapp }
$context = [Microsoft.SharePoint.SPServiceContext]::GetContext($app.ServiceApplicationProxyGroup, [Microsoft.SharePoint.SPSiteSubscriptionIdentifier]::Default)
$ServerRefID = [System.Guid]::NewGuid().toString()
$newdbserver = New-SPAccessServicesDatabaseServer -ServiceContext $context -DatabaseServerName "<PrimaryDatabaseServerName>" -DatabaseServerGroup $serverGroupName -ServerReferenceId $ServerRefID -AvailableForCreate $true

```

Write the ServerRefID to the screen for use when registering the secondary farm Access Services Database Server
  
```
 $ServerRefID
```

#### Register the secondary farm's Access Services database server

```
$serverGroupName = 'DEFAULT'
$DatabaseServerName = "<Secondary Access Database Server>"
$PrimaryServerRefID = "<Primary Server Reference ID>"
$ASapp = Get-SPAccessServicesApplication
$app = $Null
if ($ASapp.length -ne $Null) { $app = $ASapp[0] } else { $app = $ASapp }
$context = [Microsoft.SharePoint.SPServiceContext]::GetContext($app.ServiceApplicationProxyGroup, [Microsoft.SharePoint.SPSiteSubscriptionIdentifier]::Default)
$newdbserver = New-SPAccessServicesDatabaseServer -ServiceContext $context -DatabaseServerName $DatabaseServerName  -DatabaseServerGroup $serverGroupName -ServerReferenceId $PrimaryServerRefID -AvailableForCreate $true
```

You can reference as many Access Services Application Database Servers as you need. In this simple scenario we only have one. If you have many, make sure you track the registrations and ensure that, in recovery, the databases are recovered correctly to the matched server in the DR site.
  
### c. Know the databases that support the Access Services Service Application

Rather than having their own service application databases, Access Services in SharePoint Server have tight dependencies on multiple databases in a SharePoint farm.
  
These databases need to be managed as a part of your Disaster Recovery strategy.
  
|**Database**|**Description**|
|:-----|:-----|
|App Management database  <br/> |Contains Access app registrations and app principals.  <br/> |
|Subscription Settings database  <br/> |Manages the unique identities provided to Access apps to create the URL for the Access application.  <br/> |
|Secure Store database  <br/> |The Secure Store Service can be leveraged to provide alternate authentication methods for Access apps. The guide referred to earlier doesn't cover doing this, but we will add the Secure Store database to our strategy for completeness.  <br/> |
|SharePoint Content database  <br/> |These databases contain the site collections into which Access apps have been deployed.  <br/> |
|Access Services Application databases  <br/> |The databases containing the actual data you need to preserve for the Access Services application to function.  <br/> |
   
The chosen disaster recovery approach depends on your Recovery Time Objective (RTO) and Recovery Point Objective (RPO), how long can you be offline, and how much data can you afford to lose in the event of a disaster. Regardless of the selection, the recovery process for Access Services remains the same.
  
## Step 2: Recovery After Failover

After failing-over to the secondary datacenter, you need to use the five different databases listed in Step 1 to regenerate the Access Services app infrastructure on the disaster recovery farm.
  
> [!NOTE]
> This article only deals with the five database types listed in the table above. To successfully recover a full SharePoint Server farm after a data center failover, additional steps are needed and the reader is directed to review the steps in [Plan for high availability and disaster recovery for SharePoint Server](high-availability-and-disaster-recovery-concepts.md). 
  
For the test environment we discuss in this article, that means the following databases are recovered from the Primary SQL Server SQL01 to the Secondary SQL Server SQL02 in the DR site.
  
- App Management database
    
- Subscription Settings database
    
- Secure Store database
    
- SharePoint Content database
    
- Access Services App databases
    
We can use the techniques described here to recover these service applications and attach the content database.
  
### a. Recreate the service applications from the restored/recovered databases

Use the following PowerShell commands:
  
1. Application Management database and proxy:
    
  ```
  $AppPool = Get-SPServiceApplicationPool -Identity "<Services Application Pool Name> "
  $AppDatabasename = "<restored App Management database name>"
  $appman = New-SPAppManagementServiceApplication -Name "App Management" -DatabaseServer "<SecondaryDatabaseServerName>" -DatabaseName $AppDatabaseName -ApplicationPool $AppPool 
  $appmanproxy = New-SPAppManagementServiceApplicationProxy -Name "App Management Proxy" -ServiceApplication $appman
  ```

2. Subscription Settings database and proxy:
    
  ```
   $SubDatabasename = "<restored Subscription Settings database name>"
  $subset = New-SPSubscriptionSettingsServiceApplication -Name "Subscription Settings" -DatabaseServer "<SecondaryDatabaseServerName>" -DatabaseName $SubDatabaseName -ApplicationPool $AppPool
  $subsetproxy = New-SPSubscriptionSettingsServiceApplicationProxy -Name "Sub Settings Proxy" -ServiceApplication $subset
  ```

3. Secure Store database and proxy:
    
  ```
  $SecDatabasename = "<restored Secure Store database name>"
  $secstore = New-SPSecureStoreServiceApplication -DatabaseServer "<SecondaryDatabaseServerName>" -DatabaseName $SecDatabaseName -ApplicationPool $AppPool
  $secstoreproxy = New-SPSecureStoreServiceApplicationProxy -Name "Secure Store Proxy" -ServiceApplication $secstore
  ```

Also note that if you are using the secure store in the secondary farm you will need to generate a new secure store encryption key before you can leverage any Applications registered there.
  
### b. Attach the content database(s)

Mount the failover content databases can to the appropriate web application on the DR farm by using PowerShell:
  
Before you can use any of the Microsoft PowerShell cmdlets, verify that you meet all of the requirements in [Permissions](/powershell/module/sharepoint-server/?view=sharepoint-ps#section3).
  
```
 Mount-SPContentDatabase -WebApplication "<http://DRWebApp>"  -Name "<Database name>" -DatabaseServer "<SecondaryDatabaseServerName>"
```

### c. Recover the Access Services App Databases

Again as with the other databases your choice of technique depends on the RTO and RPO. However, to carry out the recovery all you need to do is restore, or recover, the databases to the secondary server that has been correctly registered in Access Services using the **ServerReferenceID** of the primary database server. This is detailed in [Configure hybrid OneDrive for Business](../hybrid/configure-hybrid-onedrive-for-business.md).
  
## Step 3: Configuration Actions Post Failover

At this point we have almost everything we need to support Access Services in Disaster Recovery conditions. The last two tasks we need to do are to:
  
- Set the app domain URLs
    
- Ensure the Access Services application database logins have been carried over from the Primary Site to the Secondary.
    
### a. Setup Apps Domains in the secondary site

The key elements to consider here are the domains you had specified in the primary site and the domains you intend to use in the secondary DR site. If you plan to use the same domains, repoint the CNAME record for the SP Apps domain to the secondary SharePoint server, for example repoint **\*.contosoapps.com** to the secondary SharePoint Server. 
  
Make sure you setup the App Urls in Central Administration on the DR site.
  
1. Open Central Administration, select **Apps**.
    
2. Select **Configure App URLs**.
    
Recovering the App Management Database does not preserve the App Domain even though it does preserve the App Prefix.
  
> [!IMPORTANT]
> Failing to set the App Domain will result in a DNS lookup failure and a site not found error in the browser. 
  
### b. Set up Access Database Logins for the secondary site

Access Services requires the Contained Databases feature of SQL Server, which supports contained database logins. However, Access Services in SharePoint 2013 and 2016 only partially leverages this feature, and so the database logins are actually stored in the Master DB, just like any other login. The downside to this is that on failover we need to regenerate any missing logins and ensure we set the same password for the account.
  
Fortunately, Microsoft has produced an easy way to do this documented right here (and we'll be using this article in step 1, below) [How to transfer logins and passwords between instances of SQL Server](https://support.microsoft.com/en-us/kb/918992).
  
The process has three key steps:
  
1. Use the script in [How to transfer logins and passwords between instances of SQL Server](https://support.microsoft.com/en-us/kb/918992) to generate two new stored procedures in the primary Access Services Database Server Master Database. 
    
2. Execute the Stored Procedure to generate a TSQL script that can be copied to the target secondary server, for example:
    
  ```
  Login: db_ _dbo
  CREATE LOGIN [db_63eb8501_29b0_401a_becd_9931ae72ea3d _dbo] WITH PASSWORD = *********** HASHED, SID = 0x0C3431F92F162D4EA913E07E1DAB3979 , DEFAULT_DATABASE = [master], CHECK_POLICY = OFF, CHECK_EXPIRATION = OFF — Login: db_63eb8501_29b0_401a_becd_9931ae72ea3d_custom
  CREATE LOGIN [db_63eb8501_29b0_401a_becd_9931ae72ea3d_custom] WITH PASSWORD = ***********  HASHED, SID = 0x8B68A3A203D6D14E88F13B504420BD7E, DEFAULT_DATABASE = [master], CHECK_POLICY = OFF, CHECK_EXPIRATION = OFF
  ```

3. Execute the TSQL on the target secondary database server to generate the logins.
    
After completing these actions, the Secondary Disaster Recovery Farm will be able to render the Access Services Apps from the Primary farm after failover.
  
## Summary

SharePoint Server 2013 has been tested in a disaster recovery scenario using SQL Server 2012 and as the Access Application Database Server Platforms.
  
SharePoint Server 2016 has been tested in a disaster recovery scenario using SQL Server 2016 as the Access Application Database Server Platforms.
  
In all scenarios we were able to successfully recover the Access Applications on the Secondary SharePoint farm and perform all CRUD operations post failover, after following the guidance in this document.
  
The key elements are : Ensure both server farms are setup with matching Authentication Realms. Ensure Access Services database servers are referenced with the same **ServerReferenceID**. Transfer SQL Logins from Production to DR SQL Servers. 
  
## See also


