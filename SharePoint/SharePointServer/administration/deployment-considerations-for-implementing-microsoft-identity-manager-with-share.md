---
title: "Deployment considerations for implementing Microsoft Identity Manager with SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5020140d-24c4-4817-8bb4-05e1c225d1f2
description: "Learn about deployment considerations of a Microsoft Identity Manager (MIM) deployment in a SharePoint Server farm."
---

# Deployment considerations for implementing Microsoft Identity Manager with SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]
 
To increase your chances of a successful MIM deployment in SharePoint Server, follow these recommendations:
  
## Plan the migration from your test environment to your production environment

Plan, plan, and then plan some more. This step can't be overstated enough. Most failed synchronization can be attributed to a lack of planning.
  
Proper setup of the MIM Synchronization Service in your test lab and careful planning of your migration from test lab to production is essential to minimizing deployment problems. It is recommended that you use a small test environment, in order to not waste time processing thousands of objects when you test new rules.
  
## Back up your initial test environment

After the MIM is installed and your management agents are created, back up the MIM Synchronization database. Then, you can recreate a fresh test environment at any time by loading the backup database.
  
## Test your back up and restore procedures for MIM

Regular backup procedures are essential for protecting your data from accidental loss. It is also strongly recommended that you test your backup and restore procedures before an emergency occurs. To back up and restore MIM, use the backup tools provided with Windows Server 2012 R2 operating system and SQL Server 2014.
  
## Install MIM Synchronization Service and SQL Server in the same domain

During MIM Synchronization Setup, the remote database access depends on the access rights of the current logon account that you are using to run Setup. Ensure that the server running Windows Server 2012 R2 operating system that hosts MIM and the server that hosts SQL Server are in the same domain and that the account that you are using to run Setup has access rights to the server that hosts SQL Server.
  
## Set access rights if SQL Server is installed on a remote server

If you install SQL Server on a remote computer, that is, on a different computer than the one running MIM, be sure that the policy for the SQL Server service account allows users access to that computer from the network. If access is not allowed, MIM setup will fail.
  
> [!IMPORTANT]
> If you install SQL Server on a remote computer and allow network access to the remote computer, you will receive a security warning from MIM setup. For this scenario, the warning can be ignored. 
  
## Specify the TCP/IP port for a remote server running SQL Server

If the SQL Server instance that you specify during MIM Setup is on a remote computer, MIM Setup uses the default TCP/IP port. If you want to specify a different port, you must use the SQL Server Client Network Utility (Windows\System32\cliconfg.exe) and the Server Network Utility tools provided with SQL Server. For more information, see the SQL Server Books Online.
  
## Use Export Management Agent to backup management agents whenever you change management agent rules

After you use Export Management Agent, you can then use the **Import Management Agent** command to import a specific version of the individual management agent. You can also export and import management agents by using the **Export Server Configuration** and **Import Server Configuration** commands, but doing so imports all management agents in addition to the metaverse schema. For additional information on how to configure and import, see [Configuring Management Agents](https://go.microsoft.com/fwlink/?linkid=841830) and [Importing and Exporting a Server Configuration](https://go.microsoft.com/fwlink/?linkid=841831)
  
## Populate the displayName attribute in the metaverse to make search results easier to identify

When listing objects by using Metaverse Search, MIM returns results identified by the **displayName** attribute. If the **displayName** attribute is not populated, the search results are identified by the globally unique identifier (GUID). For additional information on how to use metaverse search, see [Using Metaverse Search](https://go.microsoft.com/fwlink/?linkid=841832)
  
## Design your flow rules to act upon the state of an object

Use the state of an object to determine the next step in synchronizing the object rather than using the event that caused the object state. 
  
> [!IMPORTANT]
> Do not rely on declarative rules or rules in a rules extension to be evaluated in a specified order when synchronizing an object. Rules are evaluated in an unordered fashion. 
  
## Disable provisioning when you migrate connected data sources to the metaverse for the first time

When you deploy MIM for the first time, it is recommended that you migrate and join all connected data sources before you enable provisioning. After you have verified that everything has been successfully migrated and joined, you can enable provisioning and run a Full Synchronization of the management agents to apply the provisioning rules to all connected objects. For additional information on how to configure provisioning rules, see [Provisioning Rules](https://go.microsoft.com/fwlink/?linkid=841833)
  
## Set a deletion threshold in your run profile steps to limit the number of accidental deletions

Use the deletion threshold setting to limit the number of accidental deletions that can occur during import or export. The deletion threshold will stop the management agent, or prevent it from starting, when the threshold limit is reached. For additional information, see [Configuring Management Agents](https://go.microsoft.com/fwlink/?linkid=841830).
  
## Use Search Connector Space to examine objects

With Search Connector Space, you can search for objects in the connector space for a management agent. You can locate objects by name or error status, or by the state of the object (that is, whether it is connected, disconnected, or waiting to be imported or exported). 
  
## Use Preview to test synchronizations and troubleshoot errors

With Preview, you can run test synchronizations and view the results without committing the changes to the metaverse. You can also use Preview to test new rules extensions and to troubleshoot synchronization errors due to join failures or schema violations.
  
## Schedule a recurring run profile using the Delta Synchronization step to process disconnectors automatically

Objects that fail to join are not reevaluated by the Delta Import and Delta Synchronization run profile step and might remain as disconnectors. Running a Delta Synchronization step on a regular basis will reevaluates and processes these disconnectors. For additional information on how to run profile steps, see [Configuring Management Agents](https://go.microsoft.com/fwlink/?linkid=841830).
  
## Save and clear the management agent run history in Operations regularly

Operations records a history of every management agent run. Each management agent run history is saved in the SQL Server database, and can cause the database to grow over time, affecting performance. The run history can be saved using Operations. For additional information on how to use Operations, see [Using Operations](https://go.microsoft.com/fwlink/?linkid=841835).
  
> [!NOTE]
> Deleting very large numbers of runs at once make take considerable time. it is recommended that you delete no more than 100 runs at a time. 
  
## Use multiple partitions in a management agent to control synchronization of single object types

To control synchronization of single object types in a file-based management agent, create a partition for each object type. For example, to synchronize the object types **mailbox** and **group**, create two partitions in the management agent, and assign **mailbox** to one partition and **group** to the other. Then, create a management agent run profile for each partition. With this configuration, you have one management agent with the flexibility to synchronize one or both of the selected object types. For additional information on how to use partitions, see [The Metaverse and the Connector Space](https://go.microsoft.com/fwlink/?linkid=841836)
  
## Capacity Planning

There are a number of variables that can affect the overall capacity and performance of MIM deployment.
  
Performance can be negatively impacted if all the databases in the system are created with a smaller size and set to auto-grow especially by small increments. A minimum of 16 GB of RAM for the SQL Servers is required but you will benefit from more memory. You should have at least 16 CPU cores on the SQL servers but additional cores will help overall performance.
  
Finally, it is recommended not to run MIM and SharePoint databases together on the same server.
  
## High Availability

The MIM solution is designed to be highly available to prevent any single point of failure. The following components should be considered for high availability: 
  
> [!NOTE]
> The information in this section are recommendations only. 
  
- **MIM Synchronization Service** - although clustering of the MIM Synchronization Service is not supported, a warm standby server could be deployed to assume the workload of the primary in the event of a failure. However, hardware failure should not be a concern as the MIM Synchronization Service will be running on a virtual machine hosted on multiple physical nodes. Also in case of a software failure, the virtual machine hosting the synchronization server could be quickly recovered from a previous backup or rebuilt from scratch. A down time of this service has no impact on end-user interactions with the solution. It would only delay the fulfillment of all access provisioning and deprovisioning requests. When the service is brought back online those operations would resume with no data loss. The warm standby of the MIM Synchronization Service will be connected to the same SQL Server database as the primary instance and will have to be activated through a script in case the primary instance goes down and cannot be restarted in a timely manner. Note that the MIM Management Agent used to synchronize data between the MIM Synchronization Service database and the MIM Service database will have to point to the local MIM Service instance. 
    
- **SQL Server** - A SQL Server cluster is required by the MIM solution to provide high-availability for the database layer. The MIM cluster will consist of two servers with specifications detailed in the previous paragraphs. Even though each SQL node has both SQL instances installed, only one of the two instances will be active at a given time. 
    
    The design takes into account the best use of the clustered virtual machines without oversubscribing each node and potentially causing both nodes to go down in case of failover.
    
    As the databases are hosted on a remote SQL Server the network connection between the MIM Servers and SQL Servers must be 1 Gbit. 100 Mbit network will not provide enough bandwidth and will degrade synchronization performance by 20 to 30 percent.
    
## Always use Active Directory Import as the sync setting in User Profile Administration

If you plan to use the MIM Synchronization service, do not select it. Instead select the **Use SharePoint Active Directory Import** option. There is a known issue with Audience compilation and Manager attribute if the **Enable External Identity Manager** option is selected. 
  
> [!NOTE]
> This issue is fixed in the February 2017 Public Update (PU), see [February 21, 2017, update for SharePoint Server 2016 (KB3141517)](https://support.microsoft.com/en-us/help/3141517/february-21-2017-update-for-sharepoint-server-2016-kb3141517)
  
## Do not switch between synchronization types

If you switch from one synchronization type to another by using the **Configure Synchronization Settings** in the the SharePoint Central Administration website, you will experience issues with no objects being returned when an import on the SharePoint Connector instance is started, and no results in the ULS logs. 
  
To recover from switching of types, in the **Recovery Steps** section, see [SharePoint 2016 : Issues due to Switching Between Synchronization Types in UPA AD Import / External Identity Manager (MIM)](https://blogs.msdn.microsoft.com/spses/2016/07/18/sharepoint-2016-issues-due-to-switching-between-synchronization-types-in-upa-ad-import-external-identity-manager-mim/)
  
## Picture export From SharePoint to Active Directory

There is no support of picture export from SharePoint to Active Directory, so you need to plan for this migration.
  
## No BCS Integration to support additional Profile Properties

There is no Business Connectivity Services integration to support profile properties in MIM. You can manually configure Connectors to achieve this.
  
## User Profile properties

New user profile properties can be created in SharePoint Server 2016, however the mappings are not created in SharePoint, but within MIM.
  
## NetBios name

If the External Identity Manager is selected, you should enable the **NetBIOSDomainNamesEnabled** property on the User Profile Application service application as soon as you create it to support scenarios where your domain's NetBIOS name differs from domain's Fully Qualified Domain Name (FQDN) name. 
  
## Perform synchronization operations over a secure channel

As synchronization will often include personally identifiable information, it is strongly recommended that sync runs are performed over a secure channel such as HTTPS or LDAPS.
  
## See also

#### Other Resources

[Overview of Microsoft Identity Manager Synchronization Service in SharePoint Server 2016](overview-of-microsoft-identity-manager-synchronization-service-in-sharepoint-ser.md)

