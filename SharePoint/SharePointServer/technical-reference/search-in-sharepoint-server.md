---
title: "Search in SharePoint Server knowledge articles"
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
ms.assetid: 3fdf9bcc-11c0-48af-b8c3-327902f53d73
description: "Learn how to resolve alerts about the search index, content processing, query processing, and other search issues in the SharePoint Server management pack for Systems Center Operations Manager (SCOM)."
---

# Search in SharePoint Server knowledge articles

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-xxx-xxx-md.md)]

Learn how to resolve alerts about the search index, content processing, query processing, and other search issues in the SharePoint Servers 2019, 2016, and 2013 management pack for Systems Center Operations Manager (SCOM). 
  
The articles in this section are knowledge articles for search services in SharePoint Server. Typically, these articles appear when you click a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in search. 

Download and install:

- [System Center Management Pack for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57776)

- [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409) 

- [System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568) 

- [System Center Monitoring Pack for SharePoint Foundation 2013](https://go.microsoft.com/fwlink/p/?LinkId=272567)

Use the following to resolve alerts about the search issues:
  
- [Analytics analysis: failed to start - search analytics](#SearchAnStart)
    
- [Analytics analysis: failed to start warning - search analytics](#SearchAnStartWarn)
    
- [Content Processing: Fallback word breaker did not load](#WordBreak)
    
- [Content Processing: Query classification dictionary exceeds size limit](#ClassDict)
    
- [Content Processing: Spelling dictionary exceeds size limit](#SpellDict)
    
- [Content Processing: Search Custom Dictionaries Update](#CustDict)
    
- [Content Processing: Spelling Dictionary Update](#SpellDictUp)
    
- [Content Processing: Gatherer Content Processing connector](#Gather)
    
- [Content Processing: flow failed to start](#Flow)
    
- [Content Processing: Query classification dictionary close to size limit](#ClassDictWarn)
    
- [Content Processing: Spelling dictionary close to size limit](#SpellDictWarn)
    
- [Crawler: Search Gatherer Host Unavailable](#GatherHost)
    
- [DocParsing: No More Parser Server Workers](#ParserWorkers)
    
- [DocParsing: Parser Server Worker Failed to Restart](#ParserRestart)
    
- [Index: Lost Generations](#LostGen)
    
- [Index: Missing partition](#IndPartition)
    
- [Index: Indexing Blocked](#IndexBlock)
    
- [Index: Journal IO Exception Read](#IORead)
    
- [Index: Journal IO Exception Write](#IOWrite)
    
- [Index Lookup: Schema service availability query processing](#Schema)
    
- [Index Lookup: Missing partition](#LoopupPartition)
    
- [Query Processing: Query classification dictionary update](#ClassDictUp)
    
- [Query Processing: Search Service Application Availability](#SSAAvail)
    
- [Query Processing: Component Availability - Query Processing](#QueryAvail)
    
- [Query processing: flow failed to start](#FailedFlow)
    
- [Query Processing: Fallback word breaker did not load](#WordBreakFail)
    
- [Query Processing: Query Component Get Configuration](#GetQueryConfig)
    
- [Query Processing: Query Normalization Schema Service Availability](#Nomalization)
    
- [Query Processing: Query Parsing Schema Service Availability](#ParsingSchema)
    
- [Query Processing: QueryParsing Scope Cache Availability](#ParsingScope)
    
- [Query Service: Service availability query processing](#QueryParseAvail)
    
- [Query Service: Start Service Availability - Query Processing](#QueryProc)
    
- [Query Service: Unable to stop query processing](#QueryProcStop)
    
- [Query URL Mapping: Alternate URL Mapping Service Availability - Query Processing](#AUMAvail)
    
- [Schema Reader: Schema Service Availability - Query Processing](#SchemaAvail)
    
- [Search Admin Platform Services: Repository Initialization Failed](#ReposInit)
    
- [Search Admin Platform Services: Repository Installation Failed](#ReposInstall)
    
- [Search Admin Platform Services: Repository Replication](#ReposRep)
    
- [Search Analytics: analysis run state Search Analytics](#AnaRunState)
    
- [Search analytics: Timer job cannot resolve Analytics Processing Engine (APE)](#TimerAPE)
    
- [Search Analytics: Timer job cannot resolve Link database](#TimerLink)
    
- [Search Analytics: analysis run state search analytics](#AnaRunstate2)
    
- [Search Gatherer: Disk Full Crawler](#DiskFull)
    
- [Search Usage Analytics: Analysis configuration failed](#AnaConfig)
    
- [Search Usage Analytics: Analysis failed to start](#AnaStart)
    
- [Search Usage Analytics: Feeding failure](#Feed)
    
- [Search Usage Analytics: Reporting API write failure](#APIWrite)
    
- [Search Usage Analytics: Store not available](#Store)
    
- [Search Usage Analytics: Usage analytics APE not available](#APEAvail)
    
- [Usage table exceeded max bytes limit](#Usagetable)
    
- [Usage table exceeded max bytes limit](#UsageTable2)
    
- [Services Host Controller](#SearchHost)
    
## Analytics analysis: failed to start - search analytics
<a name="SearchAnStart"> </a>

 **Alert Name:** Analytics analysis: failed to start - search analytics 
  
 **Summary:** At a preconfigured time interval (once every 24 hours) the timer job will try to start a run of the search analytics analysis. This alert is triggered when the timer job fails to start the analysis. 
  
Multiple problems can prevent the analysis from being started. If the timer job fails to start the analysis, the timer job will stop and retry later (in 10 minutes).
  
### Cause

- Analytics processing component is not available.
    
- Network outage.
    
- Server issues.
    
- Analysis configuration database not available.
    
### Resolution

Make sure these areas are functioning:
  
- The analytics processing component is functioning properly.
    
- There are no networking issues.
    
- There are no server issues.
    
- The analysis reporting database is available.
    
## Analytics analysis: failed to start warning - search analytics
<a name="SearchAnStartWarn"> </a>

 **Alert Name:** Analytics analysis: failed to start warning - search analytics 
  
 **Summary:** If a search analytics analysis is still running when the timer job is trying to start a new run of the same analysis, this new start has to be postponed. The system with try to restart the search analytics analysis as soon as the timer job detects that the running analysis has stopped. 
  
### Cause

One or more of the following might be the cause:
  
- Previous analysis run has not completed.
    
- Heavy load on servers or network leads to longer analysis run time.
    
### Resolution

Make sure these areas are functioning:
  
- Current running analysis does have progress. If not, investigate why there is no progress. There might be a networking or server issue. Resolve these. Do make sure that all databases are available (Link database, analytics reporting database, etc.).
    
- You might have to perform a manual stop of the analysis if it is running without any progress.
    
## Content Processing: Fallback word breaker did not load
<a name="WordBreak"> </a>

 **Alert Name:** Content Processing: Fallback word breaker did not load 
  
 **Summary:** The word breaker service could not load the fallback word breaker for the indicated word breaker language. 
  
### Cause

Installation error or another transient error that might be resolved by a content processing component restart or rebooting the server In an on-premises setting, it could also indicate an error caused by changing the word breaker configuration.
  
### Resolution

Restart the content processing component or restart the server. component. If a word breaker customization was tried, the logs could suggest more information to indicate a cause and resolution.
  
## Content Processing: Query classification dictionary exceeds size limit
<a name="ClassDict"> </a>

 **Alert Name:** Content Processing: Query classification dictionary exceeds size limit 
  
 **Summary:** The dictionary has grown too large and is exceeding the size limit. The current dictionary will still be used and no dictionary updates will occur until dictionary compilation succeeds again. The system will retry until the dictionary compiles again. But a reduction in data from the Term Store may be required. 
  
### Cause

The dictionary used for query classification rules has grown too large and is now exceeding the size limit.
  
### Resolution

Check the term sets used for query classification rules. Entries may need reducing to make the dictionary compile again. The recurring retries may otherwise create a high load on the content processing component.
  
## Content Processing: Spelling dictionary exceeds size limit
<a name="SpellDict"> </a>

 **Alert Name:** Content Processing: Spelling dictionary exceeds size limit 
  
 **Summary:** The query spelling correction dictionary has grown too large and is now exceeding the size limit. The current dictionary will still be used and no dictionary updates will occur until dictionary compilation succeeds again. The system will retry until the dictionary compiles again. But a reduction in data in the search index or a reconfiguration of the query spelling components may be required. 
  
### Cause

The dynamic query spelling correction dictionary has grown too large and is exceeding the size limit.
  
### Resolution

Check the size of the index. This error indicates that the index is very large and might need splitting soon. Also, consider lowering the number of dictionary terms allowed per organization by using the cmdlet  `Set-SPEnterpriseSearchQuerySpellingCorrection`. The recurring retries may otherwise create a high load on the content processing component.
  
## Content Processing: Search Custom Dictionaries Update
<a name="CustDict"> </a>

 **Alert Name:** Content Processing: Search Custom Dictionaries Update 
  
 **Summary:** The timer job "Search Custom Dictionaries Update" fails. 
  
### Cause

One or more of the following might be the cause:
  
- The Search service application or the term store is paused or not available. 
    
- An error occurred during the deployment of the custom entity extraction dictionary or while establishing a connection.
    
### Resolution

- Check the status of the Search service application and the term store, restart if it is necessary. 
    
- Check whether the custom entity extraction dictionary is deployed, and make sure that connection is present.
    
- Restart timer job if necessary.
    
## Content Processing: Spelling Dictionary Update
<a name="SpellDictUp"> </a>

 **Alert Name:** Content Processing: Spelling Dictionary Update 
  
 **Summary:** The timer job "Spelling Dictionary Update" fails. 
  
### Cause

One or more of the following might be the cause:
  
- The Search service application or the term store is paused or not available. 
    
- An error occurs during deployment or connection establishment.
    
### Resolution

- Check the status of the Search service application and the term store, restart if it is necessary.
    
- Make sure that connection is present.
    
- Restart timer job if it is necessary.
    
## Content Processing: Gatherer Content Processing connector
<a name="Gather"> </a>

 **Alert Name:** Content Processing: Gatherer Content Processing connector 
  
 **Summary:** The crawler could not connect to content processing. 
  
### Cause

This may be caused by intermittent loss of network connectivity, or the content processing component is not available.
  
### Resolution

If the problem persists, check network connectivity between the crawler and content Processing. Also, check the content processing component, and restart if it is necessary.
  
## Content Processing: flow failed to start
<a name="Flow"> </a>

 **Alert Name:** Content Processing: flow failed to start 
  
 **Summary:** The indicated processing flow is not started as expected. 
  
### Cause

The required services are not present, or the search index may be unavailable.
  
### Resolution

Check that the required search components and databases are running and restart these if necessary.
  
## Content Processing: Query classification dictionary close to size limit
<a name="ClassDictWarn"> </a>

 **Alert Name:** Content Processing: Query classification dictionary close to size limit 
  
 **Summary:** The dictionary has grown close to its size limit (at or beyond 80 percent of its size limit). 
  
### Cause

The number of terms in the corresponding dictionary used for query classification rules across all organizations is growing towards the limit.
  
### Resolution

Check the term sets used for query classification.
  
## Content Processing: Spelling dictionary close to size limit
<a name="SpellDictWarn"> </a>

 **Alert Name:** Content Processing: Spelling dictionary close to size limit 
  
 **Summary:** The query spelling correction dictionary has grown close to its size limit (at or beyond 80 percent of its size limit). 
  
### Cause

The number of terms relevant for the dynamic query spelling correction dictionary across all organizations is growing towards the limit.
  
### Resolution

Check the number of indexed documents. If the number of indexed documents is close to the system's limit, this warning can be discarded.
  
## Crawler: Search Gatherer Host Unavailable
<a name="GatherHost"> </a>

 **Alert Name:** Crawler: Search Gatherer Host Unavailable 
  
 **Summary:** As part of a search crawl, the servers that contain the crawl components communicate with content servers to retrieve the items for the crawl. Network communication problems between crawl server and content server will block this crawl. When SharePoint is crawling content from a specific content server and network communication problems exist, SharePoint might display the following symptoms: 
  
- The crawl of the specific content server does not progress and seems to stall.
    
- The crawl logs show no new crawled documents for the specific content server.
    
### Cause

Network issues might be preventing the communication. Check that the content server is online and can connect to the server that hosts the crawl component.
  
### Resolution

Check the status of the content server. If the content server is online and serves content to the crawl account, check for network connection issues.
  
## DocParsing: No More Parser Server Workers
<a name="ParserWorkers"> </a>

 **Alert Name:** DocParsing: No More Parser Server Workers 
  
 **Summary:** All parser server workers cannot restart. Therefore the pool has no more workers available. At this point, only format handlers that are not configured to run in a sandbox can run. 
  
### Cause

One or more of the following might be the cause:
  
- Broken pipe between the parser server and the content processing component.
    
- Excessive resource usage causing a time-out to obtain resources.
    
- Permission failure to any of the required directories. 
    
- External change in directory permission of either the parser process or the temporary directory that it writes to.
    
- Misplaced or corrupted configuration file.
    
### Resolution

- Check CPU and memory usage of the content processing component. 
    
- Check appropriate permissions to parserserver.exe and the related directories.
    
- Check the configuration file.
    
## DocParsing: Parser Server Worker Failed to Restart
<a name="ParserRestart"> </a>

 **Alert Name:** DocParsing: Parser Server Worker Failed to Restart 
  
 **Summary:** A parser server worker cannot restart. Therefore it is being removed from the pool. The pool still has the indicated number of workers available. This occurs when a worker inside the parser server pool could not restart. When this happens, the number of available workers in the pool is decreased, which reduces throughput. 
  
### Cause

One or more of the following might be the cause:
  
- Broken pipe between the parser server and the content processing component
    
- Excessive resource usage causing a time-out to obtain resources.
    
- Permission failure to any of the required directories; 
    
- External change in directory permission of either the parser process or the temporary directory that it writes to. 
    
- Misplaced or corrupted configuration file.
    
### Resolution

- Check CPU and memory usage of the content processing component. 
    
- Check appropriate permissions to parserserver.exe and the related directories. 
    
- Check the configuration file.
    
## Index: Lost Generations
<a name="LostGen"> </a>

 **Alert Name:** Index: Lost Generations 
  
 **Summary:** Data acknowledged as indexed is permanently lost. Potentially lost documents on the index system indicated, between the given generations. 
  
### Cause

This may be caused by the amount failures exceeding the fault-tolerance.
  
### Resolution

A full re-crawl may be required.
  
## Index: Missing partition
<a name="IndPartition"> </a>

 **Alert Name:** Index: Missing partition 
  
 **Summary:** Incomplete result set because of one or more missing partitions on the indicated index system. This may require resending of information if the related search components remain unavailable. That is, it continues to fail. 
  
### Cause

One or more of the following might be the cause:
  
- Missing injection from index component on the query processing component.
    
- Lost network connectivity.
    
- Index component fails.
    
### Resolution

- Lookup Service will restart automatically.
    
- Check index component. 
    
- Check communication issues.
    
## Index: Indexing Blocked
<a name="IndexBlock"> </a>

 **Alert Name:** Index: Indexing Blocked 
  
 **Summary:** Information flow from content processor to index is blocked; waiting for a checkpoint (time indicated). This is limiting index speed; indexing queues remain full for longer than expected. 
  
### Cause

One or more of the following might be the cause:
  
- Indexer not receiving enough resources.
    
- Information coming in too quickly.
    
### Resolution

Investigate resource usage on the index component, and possibly adjust the search topology to lower the feeding rate.
  
## Index: Journal IO Exception Read
<a name="IORead"> </a>

 **Alert Name:** Index: Journal IO Exception Read 
  
 **Summary:** Unable to read Journal file. This indicates a potential problem with recovery or replication. Indexing is stopped. 
  
### Cause

Journal file is stored on disk, external cause to indexer may be:
  
- Lock on file.
    
- Changes to file.
    
- Physical disk problem.
    
### Resolution

- Release lock on file.
    
- Revert changes.
    
- Fix disk.
    
This issue may require deleting the Journal and refeeding.
  
## Index: Journal IO Exception Write
<a name="IOWrite"> </a>

 **Alert Name:** Index: Journal IO Exception Write 
  
 **Summary:** Unable to write to Journal file. This indicates a potential problem with recovery or replication. Indexing is stopped. 
  
### Cause

Journal file is stored on disk. External cause to indexer may be:
  
- Lock on file.
    
- Changes to file.
    
- Physical disk problems.
    
### Resolution

- Release lock on file.
    
- Revert changes.
    
- Fix disk.
    
This issue may require deleting the Journal and refeeding.
  
## Index Lookup: Schema service availability query processing
<a name="Schema"> </a>

 **Alert Name:** Index Lookup: Schema service availability query processing 
  
 **Summary:** Index lookup could not work because the schema service was not available. 
  
### Cause

The indexer or the database, or both are unavailable.
  
### Resolution

Check, and restart, the Schema service or OM, if it is necessary.
  
## Index Lookup: Missing partition
<a name="LoopupPartition"> </a>

 **Alert Name:** Index Lookup: Missing partition 
  
 **Summary:** One or more partitions are missing on the index system indicated. This means that at least one content processing component has no connection to one primary index component. Therefore the system cannot feed for that particular connection. 
  
### Cause

Possible causes include the following: 
  
- Index component down.
    
- Missing injection from index component on the content processing component.
    
- Lost network connectivity.
    
### Resolution

The service will restart automatically; check index component; check communication issues, restart if it is necessary.
  
## Query Processing: Query classification dictionary update
<a name="ClassDictUp"> </a>

 **Alert Name:** Query Processing: Query classification dictionary update 
  
 **Summary:** The timer job Query Classification Dictionary fails. 
  
### Cause

One or more of the following might be the cause:
  
- The Search service application is paused or not available.
    
- An error occurred during deployment or connection establishment.
    
### Resolution

- Check the status of the Search service application, and restart if it is necessary. 
    
- Make sure that connection is present. 
    
- Restart timer job if it is necessary.
    
## Query Processing: Search Service Application Availability
<a name="SSAAvail"> </a>

 **Alert Name:** Query Processing: Search Service Application Availability 
  
 **Summary:** Query parsing could not work because the Search service application with the indicated ID is not available. The Search service application is down. Therefore service is interrupted. 
  
### Cause

The Search service application is not available.
  
### Resolution

Check, and restart, the Search service application if it is necessary.
  
## Query Processing: Component Availability - Query Processing
<a name="QueryAvail"> </a>

 **Alert Name:** Query Processing: Component Availability - Query Processing 
  
 **Summary:** The query processing component is stopped and is unavailable. 
  
### Cause

The query processing component is stopped under either expected or unexpected conditions.
  
### Resolution

If the issue persists, this indicates system issues. Check and restart the query processing component, if it is necessary.
  
## Query processing: flow failed to start
<a name="FailedFlow"> </a>

 **Alert Name:** Query processing: flow failed to start 
  
 **Summary:** The indicated processing flow is not started as expected. 
  
### Cause

The required services are not present, or the index may be unavailable.
  
### Resolution

Check that the required search components and databases are running and restart these if necessary.
  
## Query Processing: Fallback word breaker did not load
<a name="WordBreakFail"> </a>

 **Alert Name:** Query Processing: Fallback word breaker did not load 
  
 **Summary:** The word breaker service could not load the fallback word breaker, for the indicated word breaker language. 
  
### Cause

Installation error or another transient error that might be resolved by a component restart or rebooting the server. In an on-premises setting, it could also indicate an error caused by changing the word breaker configuration.
  
### Resolution

Restart the query processing component or restart the server. If a word breaker customization was tried, the logs could suggest more information to indicate a cause and resolution.
  
## Query Processing: Query Component Get Configuration
<a name="GetQueryConfig"> </a>

 **Alert Name:** Query Processing: Query Component Get Configuration 
  
 **Summary:** Unable to get the configuration for query processing component. So, the query service cannot start and is currently not working. 
  
### Cause

Corrupt or missing configuration.
  
### Resolution

Check settings for the query processing component.
  
## Query Processing: Query Normalization Schema Service Availability
<a name="Nomalization"> </a>

 **Alert Name:** Query Processing: Query Normalization Schema Service Availability 
  
 **Summary:** Query normalization could not work for the particular query because the schema service was not available. Query processing fails for particular queries. 
  
### Cause

The indexer is unavailable, or the search administration database is down, or both.
  
### Resolution

Check and restart the schema service or OM.
  
## Query Processing: Query Parsing Schema Service Availability
<a name="ParsingSchema"> </a>

 **Alert Name:** Query Processing: Query Parsing Schema Service Availability 
  
 **Summary:** Query parsing could not work for the particular query because the schema service related to the indicated Search service application was not available. Query parsing fails for particular queries. 
  
### Cause

The indexer is unavailable, or the search administration database is down, or both.
  
1. The query processing component has restarted and cannot access any index component. Check index components.
    
2. Indexers are available, but cannot provide the schema to query processing. 
    
### Resolution

Check and restart the schema service or OM.
  
## Query Processing: QueryParsing Scope Cache Availability
<a name="ParsingScope"> </a>

 **Alert Name:** Query Processing: QueryParsing Scope Cache Availability 
  
 **Summary:** Query parsing could not work for the particular query because the query rules for the indicated Search Service service Aapplication was not available. 
  
### Cause

Query rules are not available.
  
### Resolution

Check the query rules.
  
## Query Service: Service availability query processing
<a name="QueryParseAvail"> </a>

 **Alert Name:** Query Service: Service availability query processing 
  
 **Summary:** The query service that has the indicated service URI has stopped. 
  
### Cause

Query processing component is stopped under either expected or unexpected conditions. That leads to the shutdown of the WCF service it exposes.
  
### Resolution

If the issue persists, check and restart the query processing component.
  
## Query Service: Start Service Availability - Query Processing
<a name="QueryProc"> </a>

 **Alert Name:** Query Service: Start Service Availability - Query Processing 
  
 **Summary:** Unable to start the query service that has the indicated service URI because the query service is not working correctly. 
  
### Cause

Potential network communication service issues. For example, the WCF port is in use.
  
### Resolution

Restart the query processing component, the query service or WCF services if the WCF port is in use and has to be released.
  
## Query Service: Unable to stop query processing
<a name="QueryProcStop"> </a>

 **Alert Name:** Query Service: Unable to stop query processing 
  
 **Summary:** Unable to stop the query service that has the indicated service URI. 
  
### Cause

Potential network communication service issues. For example, the WCF port is in use.
  
### Resolution

Restart the query processing component, the query Service or WCF services if the WCF port is in use and has to be released.
  
## Query URL Mapping: Alternate URL Mapping Service Availability - Query Processing
<a name="AUMAvail"> </a>

 **Alert Name:** Query URL Mapping: Alternate URL Mapping Service Availability - Query Processing 
  
 **Summary:** The alternate URL mapping did not work because the mapping service was not available. Query or results processing fails. 
  
### Cause

The Alternate Access Mapping OM is unavailable.
  
### Resolution

Check, and restart, the Alternate Access Mapping service or OM if it is necessary.
  
## Schema Reader: Schema Service Availability - Query Processing
<a name="SchemaAvail"> </a>

 **Alert Name:** Schema Reader: Schema Service Availability - Query Processing 
  
 **Summary:** The schema reader cannot work for the particular query because the schema service is not available. Query processing fails for particular queries. 
  
### Cause

The Indexer is unavailable, or the search administration database is down, or both.
  
### Resolution

Check and restart the schema service or OM if it is necessary.
  
## Search Admin Platform Services: Repository Initialization Failed
<a name="ReposInit"> </a>

 **Alert Name:** Search Admin Platform Services: Repository Initialization Failed 
  
 **Summary:** The PackageManager service in each component will read the Default-manifest.txt on component startup to find the current status of the repository quickly. While running, the PackageManager in each component obtains updates about installs and uninstalls from the host controller. In this case, the repository could not be initialized. This means that there was a failure when the repository was initializing on host controller startup. For example, during a primary failover or during a repository reset. 
  
### Cause

The cause could be an ACL issue or a corrupted repository manifest file. If it is a corrupted repository with a good manifest file, initialization will try to rebuild the repository again. However, the same event is also sent when rebuild fails.
  
### Resolution

1. Check for potential ACL issues. 
    
2. Follow this procedure for fixing the repository on secondary (not primary) hosts:
    
  - Stop the host controller.
    
  - Delete the directory C:\Program Files\Microsoft Office Servers\15.0\Data\Office Server\Applications\Search\Repository.
    
  - Start the host controller. This will affect the host controller to create an empty repository with a GUID that does not match the primary. So, the secondary will immediately start to replicate the contents of the primary.
    
## Search Admin Platform Services: Repository Installation Failed
<a name="ReposInstall"> </a>

 **Alert Name:** Search Admin Platform Services: Repository Installation Failed 
  
 **Summary:** Repository installation fails for the file indicated. When dictionary installation fails for the primary, users should be aware that linguistic features such as query suggestions might get outdated. 
  
### Cause

The file may already be installed in the repository, or the related timer job may have failed.
  
### Resolution

Check the repository. Make sure that a dictionary compilation timer job has completed successfully after the event. You can manually trigger the timer job from Central Administration or by using Microsoft PowerShell in order to re-install.
  
## Search Admin Platform Services: Repository Replication
<a name="ReposRep"> </a>

 **Alert Name:** Search Admin Platform Services: Repository Replication 
  
 **Summary:** This situation occurs in secondary repositories. The repository in the local host controller has found that it has a lower repository version than the primary host controller (or lower version than other secondary host controllers if the primary is down). When this happens, the local repository attempts to obtain the latest version from the primary or a secondary based on how it is triggered. This indicates that something went wrong during the replication. 
  
### Cause

Connection to the remote repository which is being replicated can be lost due to a network issue or due to a remote repository (host controller) issue during replication. The local repository can be corrupted or have an ACL issue.
  
### Resolution

If persistent, a manual intervention might require to make it correct based on the problem (see cause). Except for the obvious resolutions on network and ACL and so on, remote host controller can be restarted. If the repository is corrupted, usually it is automatically rebuilt.
  
## Search Analytics: analysis run state Search Analytics
<a name="AnaRunState"> </a>

 **Alert Name:** Search Analytics: analysis run state Search Analytics 
  
 **Summary:** An analysis can encounter different problems. Hence the system cannot guarantee a successful run of search analytics analysis. The timer job, following the analysis failure model, will try to re-schedule a new analysis run to prevent from waiting until daily schedule is triggered. 
  
Symptoms: Monitor is triggered when unsuccessful analysis run is detected by the timer job.
  
### Cause

One or more of the following might be the cause:
  
- Analytics processing component(s) or some other farm components are not available.
    
- Databases (Link database, analytics reporting database, etc.) are not running or reachable.
    
- Network outage.
    
- Server issues.
    
### Resolution

Make sure these areas are functioning:
  
- The analytics processing component(s) and other farm components are functioning correctly.
    
- There are no networking issues.
    
- There are no server issues.
    
- The analytics databases are available and that the user can read or write to the databases.
    
## Search analytics: Timer job cannot resolve Analytics Processing Engine (APE)
<a name="TimerAPE"> </a>

 **Alert Name:** Search analytics: Timer job cannot resolve Analytics Processing Engine (APE) 
  
 **Summary:** After the timer job has successfully found the Search service application it will try to resolve the Analysis Processing Engine in the analytics processing component. This component is needed to be able to read or write the analysis configuration and to start, stop, suspend, or resume the analysis. Symptoms: If the system cannot locate or communicate with the Analysis Processing Engine, it will be unable to start a new run of the analysis. 
  
### Cause

One or more of the following might be the cause:
  
- Unable to connect to Search service application.
    
- Unable to connect to the search administration component.
    
- Unable to connect to System Manager.
    
- Unable to connect to the Analysis Processing Engine.
    
### Resolution

Ensure that the following components are up and running:
  
- Search service application.
    
- Search administration component.
    
- System Manager.
    
- Analysis Processing component.
    
## Search Analytics: Timer job cannot resolve Link database
<a name="TimerLink"> </a>

 **Alert Name:** Search Analytics: Timer job cannot resolve Link database 
  
 **Summary:** The timer job will check that all Link database partitions are available before it tries to start the search analytics analysis.Symptoms:If the Link database partitions are unavailable when it is time to start a new analysis run, the start try will be aborted. New Link database checks followed by a new start try will be performed in the next timer job polls (every 10 minutes). 
  
### Cause

One or more of the following might be the cause:
  
- Unable to resolve the Search service application.
    
- Link database connection timed out.
    
- Link database connection is refused.
    
- Link database is not available.
    
### Resolution

Verify that the Link database is available and reachable. Also verify that the user has access to read from the Link database.
  
## Search Analytics: analysis run state search analytics
<a name="AnaRunstate2"> </a>

 **Alert Name:** Search Analytics: analysis run state search analytics 
  
 **Summary:** The search analytics analysis is started by its timer job. The analysis will run until all its tasks are completed, and the analysis state will be set to Stopped. If some tasks cannot be completed, the analysis run will be stopped (after some retries) and the state set to Failed. Stopped before completion indicates that the analysis has reached the Stopped state, but all analysis tasks have NOT completed. Some of the work done by the analysis might have been sent to the index then, but to make sure nothing is lost and all of the work is processed again during next analysis run. 
  
### Cause

Analysis is stopped for the following reasons: 
  
- A manual stop on a running search analytics analysis was performed
    
- Or, system maintenance tasks require stopping a running search analytics analysis. 
    
### Resolution

Check the state of the search analytics analysis and any active system maintenance tasks.
  
## Search Gatherer: Disk Full Crawler
<a name="DiskFull"> </a>

 **Alert Name:** Search Gatherer: Disk Full Crawler 
  
 **Summary:** As the crawler crawls content, it creates files in a temporary location. This temporary location can grow over time. The disk where the temporary location is located is running out of space. SharePoint experiences the following symptoms when this happens: 
  
- The crawl does not progress and seems to stall.
    
- The crawl logs show no new crawled documents.
    
### Cause

The disk on which the crawler creates temporary files is running out of space.
  
### Resolution

- Free up space on the disk on which the crawler creates the temporary files. To free up disk space: Use Disk Cleanup to delete temporary files on the drive where the temporary index files are stored. Use the procedure following this one to determine the location of the index files.
    
    > [!NOTE]
    > If the temporary files are located on a drive other than the operating system drive (drive C), you must restart the search service to test the performance of the crawler after you delete the temporary files. 
  
- After Disk Cleanup is complete, test the performance of the crawler. 
    
- If the crawler is not crawling content, delete unnecessary files and folders on the selected drive.
    
- If you cannot clear any disk space, restart the search service. Restarting the search service recreates the Temp directory for crawled files. In a Command Prompt window, run the command  `net stop osearch15` to stop the search service. Run the command  `net start osearch15` to restart the search service. 
    
## Search Usage Analytics: Analysis configuration failed
<a name="AnaConfig"> </a>

 **Alert Name:** Search Usage Analytics: Analysis configuration failed 
  
 **Summary:**
  
1. If the system cannot get or set the analysis configuration, it will not schedule a new run of the analysis. The timer job will retry later.
    
2. Analysis run with wrong event configuration:
    
  - Wrong recommendations weight.
    
  - Wrong event rate weight.
    
3. When the deletion scopes are fetched, any errors from the API will result in an event. The analysis can still run without this. However, the quality or correctness of the result will deteriorate over time.
    
### Cause

One or more of the following might be the cause:
  
1. Analytics processing component not available. 
    
  - Network issues.
    
  - Time-out from API.
    
  - Analytics processing component throwing exceptions.
    
  - Analytics reporting database down.
    
  - Networking issues.
    
  - Errors in configuration.
    
2. Getting wrong event configuration from API. 
    
  - No configuration data is present in the system.
    
  - Networking problems causing API calls to fail.
    
  - API returning time-out.
    
3. Network issues causing failures when you are using the API.
    
  - The API returning errors.
    
### Resolution

1. Make sure these areas are functioning:
    
  - There is a Search service application in the system.
    
  - The Analytics processingcomponent is functioning correctly.
    
  - There are no networking issues.
    
2. Check configuration.
    
3. Verify that the component where the API is running is up and functioning.
    
  - Check for any network problems.
    
4. Verify that search analytics has run the last 30 days.
    
## Search Usage Analytics: Analysis failed to start
<a name="AnaStart"> </a>

 **Alert Name:** Search Usage Analytics: Analysis failed to start 
  
 **Summary:** Usage analytics analysis cannot start, or usage analytics analysis fails during execution. 
  
### Cause

One or more of the following might be the cause:
  
1. This can be caused by external dependencies like configuration, analytics processing component or Search service application dependencies or networking issues.
    
2. This monitor can also be triggered if the usage analytics analysis fails during execution.
    
3. This can be caused by failures in components usage analytics depend on, such as the analytics processing component or other networking issues.
    
4. There can also be something in the events being processed causing the analysis to fail.
    
### Resolution

Verify other System Center Operations Manager monitors and see whether any parent errors are present.
  
- The Search service application is up.
    
- The analytics processing database and link databases are running, and are in healthy state.
    
- There is no problem with the analytics processing component
    
- There is no problem with disk space.
    
- There is no metwork connectivity issue.
    
- The usage analytics timer job is running.
    
- The search analytics timer job is running.
    
- Verify the status of the search analytics analysis.
    
## Search Usage Analytics: Feeding failure
<a name="Feed"> </a>

 **Alert Name:** Search Usage Analytics: Feeding failure 
  
 **Summary:** This means the recommendations and statistics provided by usage analytics will be old or missing. Any recent analysis changes will not be visible. 
  
Symptom: usage analytics feeding required for the analysis was unsuccessful.
  
### Cause

One or more of the following might be the cause:
  
- The indexer is returning errors.
    
- The content processing component is not working.
    
- The component that the indexer is running on could be down.
    
### Resolution

- Verify that the index system is functioning correctly.
    
- Check for network errors.
    
- Make sure there are no errors on the analytics processing component.
    
## Search Usage Analytics: Reporting API write failure
<a name="APIWrite"> </a>

 **Alert Name:** Search Usage Analytics: Reporting API write failure 
  
 **Summary:** Background or symptoms: 
  
1. The information written to the reporting API or database is used if the cache files must be rebuilt. When usage analytics cannot write to the reporting API, this means that the recommendations and data is not updated. Counts presented to the user are therefore out of date, and old or wrong data will also be presented next time that the cache is rebuilt. 
    
2. The Reporting API could not be read so that no cache files could be created and the analysis will therefore not be run. Running the analysis in this state would in effect overwrite the current data.
    
Impact:
  
- There will be no usage analytics analysis run.
    
- Recommendations will not be updated for items in the system.
    
### Cause

One or more of the following might be the cause:
  
- Reporting API is returning an error saying database is down.
    
- Reporting API is responding that the wrong data is being sent (nothing is stored).
    
- The reporting API cannot be reached (networking issues).
    
- Reporting API is returning an error saying database is down
    
- Reporting API is returning empty (wrong data).
    
- The cache dumper is malfunctioning.
    
### Resolution

1. Verify that there are no database problems in the system, and make sure that the analytics reporting database is functioning.
    
2. Verify that analytics processing component is functioning. This means that analyses can run.
    
3. Check for any networking issues.
    
## Search Usage Analytics: Store not available
<a name="Store"> </a>

 **Alert Name:** Search Usage Analytics: Store not available 
  
 **Summary:** Background or symptoms: 
  
1. Usage analytics cannot communicate with the event store. The usage analysis will not be started, and usage analytics data in the analytics reporting database and the search index will be stale. 
    
2. During the first step of the usage, the system fetches the event data from the event store. This is the raw input to the analysis. It contains the actions for the users in the system. Without this data, the analysis cannot be run.
    
### Cause

One or more of the following might be the cause:
  
- Network outage, Event Store process is down, or the event store is returning errors in response to request. 
    
- The event store can be down. The event store is returning no data because the components registering events are not functioning correctly, or there are networking issues so that the event store cannot be reached.
    
### Resolution

- Ensure that the event store is up and running.
    
- Verify that the event store is functioning correctly.
    
- Check for networking errors.
    
- Make sure the databases in the system are running.
    
## Search Usage Analytics: Usage analytics APE not available
<a name="APEAvail"> </a>

 **Alert Name:** Search Usage Analytics: Usage analytics APE not available 
  
 **Summary:** Background or symptoms: 
  
1. Fails to retrieve Search service application, which means that no new analysis can be run, and recommendations cannot be updated.
    
2. Fails to retrieve Analysis Engine Service so that no new analysis can be started.
    
### Cause

Inability to connect to the Search service application may be caused by one or more of the following:
  
- Network issues.
    
- Search service application not created.
    
- User permissions mismatch. 
    
Inability to connect to the Analysis Engine Service can be caused by one or more of the following:
  
- Unable to connect to Search service application.
    
- Unable to connect to the search administration component.
    
- Unable to connect to System Manager.
    
- Network problems.
    
- User rights or WCF errors.
    
- Unable to connect to the Analytics processing component.
    
### Resolution

Check the following areas:
  
1. Check the following areas:
    
  - A Search service application does not exist.
    
  - Network problems.
    
  - User permissions or WCF errors.
    
2. Ensure that the following components are up and running:
    
  - Search service application.
    
  - Search administration component.
    
  - System Manager.
    
  - Analysis processing component
    
  - Networking is ok on host.
    
## Usage table exceeded max bytes limit
<a name="Usagetable"> </a>

 **Alert Name:** Usage table exceeded max bytes limit 
  
 **Summary:** This alert is to report that a usage table exceeds its quota. Usage data is stored in various tables. And each table has its quota. Once a table is full, new data cannot be inserted. 
  
### Cause

Too much usage data is generated in one day.
  
### Resolution

There are two ways to resolve this issue:
  
1. Extend the table quota defined in "configurations" table.
    
2. Disable the usage provider to stop generating data.
    
## Usage table exceeded max bytes limit
<a name="UsageTable2"> </a>

 **Alert Name:** Usage table exceeded max bytes limit 
  
 **Summary:** This alert is to report that a usage table exceeds its quota. Usage data is stored in various tables. And each table has its quota. Once a table is full, new data cannot be inserted. 
  
### Cause

Too much usage data is generated in one day.
  
### Resolution

There are two ways to resolve this issue:
  
1. Extend the table quota defined in the "configurations" table.
    
2. Disable the usage provider to stop generating data.
    
## Services Host Controller
<a name="SearchHost"> </a>

 **Alert Name:** Services Host Controller 
  
 **Summary:** The host controller service is currently unavailable. 
  
### Cause

This may indicate an issue internal to the host controller.
  
### Resolution

If persistent or recurring, check the host controller and restart if it is necessary.
  
## See also
<a name="SearchHost"> </a>

#### Concepts

[Plan for monitoring in SharePoint Server](../administration/monitoring-planning.md)
  
#### Other Resources

[System Center Monitoring Pack for SharePoint Foundation](http://go.microsoft.com/fwlink/p/?LinkId=272567)
  
[System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568)
  
[System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409)

