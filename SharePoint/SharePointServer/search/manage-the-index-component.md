---
title: "Manage the index component in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 6c4f87aa-1004-4b87-aaca-2c262588fc46
description: "Learn how and when to use Windows PowerShell to scale out the search index in SharePoint Server by adding an index component to create an additional index replica or index partition."
---

# Manage the index component in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The procedures and the examples in this article assume that SharePoint Server and the Search service application are installed, that there is an existing search topology and that there are items in the SharePoint Server search index. If SharePoint Server and the Search service application are newly installed and there is no content in the SharePoint Server search index, follow the procedures outlined in [Change the default search topology in SharePoint Server](change-the-default-search-topology.md) to scale out the search topology. 
  
The procedures in this article apply to the index component. For information about how to manage the analytics processing component, the content processing component, the crawl component, the search administration component and the query processing component, see [Manage search components in SharePoint Server](manage-search-components.md).
  
You use the index component PowerShell cmdlet (New-SPEnterpriseSearchIndexComponent) to manage both index partitions and index replicas. Each index component in the search topology represents an index replica.
  
You divide the search index into discrete portions called **index partitions**. Each index partition is stored as a set of files on a local disk. To **scale out** the search index, you add a new index partition. 
  
To achieve **fault tolerance** for the SharePoint Server search index, you add an index replica of an existing index partition to the search topology. Each index replica contains the same information. 
  
    
## Before you begin
<a name="Search_Index_Before"> </a>

Before you begin, review the following prerequisites.
  
- SharePoint Server is installed and a Search service application with a search topology is created.
    
- The user account that is performing the procedures in this article is a member of the **Farm Administrators** group. 
    
- You have planned a target search topology and have planned on which servers that you want to host the index partitions and the index replicas.
    
- SharePoint Server is installed on all the servers that you want to host index components on. You can create new application servers or define application servers in an existing deployment. The servers are added to the farm and you are an administrator on all these servers.
    
## Add an index replica to an existing index partition
<a name="Search_Index_Repl"> </a>

You add an index replica to the search topology to achieve fault tolerance for an existing index partition. You place the index replicas on separate failure domains on separate servers. When you add an index replica, you add a new index component to the search topology and associate it with the index partition that you want to make a replica of.
  
> [!IMPORTANT]
> This procedure uses Microsoft PowerShell. You can run the Microsoft PowerShell commands on any server in the farm. However, you should use the same SharePoint Management Shell for all Microsoft PowerShell commands in this procedure so that you can share Microsoft PowerShell object references between commands. 
  
 **To add an index replica**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start a SharePoint Management Shell on one of the servers in the farm.
    
3. Start a search service instance on the server that you want to create the index replica on and create a reference to the search service instance Id. At the Microsoft PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $<host n > = Get-SPEnterpriseSearchServiceInstance -Identity "<Server name>"
    Start-SPEnterpriseSearchServiceInstance -Identity $<host n >
    ```

    Where:
    
    -  _$\<host n\>_ specifies the PowerShell object reference for the search service instance. 
    
    -  _\<Server name\>_ specifies the server on which you want to add an index component. The input must be a valid GUID, in the form  `12345678-90ab-cdef-1234-567890bcdefgh`; a valid name of a server (for example, **myserver1** ); or an instance of a valid **SearchServiceInstance** object. 
    
    For example:
    
    ```PowerShell
    $hostA = Get-SPEnterpriseSearchServiceInstance -Identity "myserver1"
    Start-SPEnterpriseSearchServiceInstance -Identity $hostA
    ```

4. Wait until the search service instance is running. At the Microsoft PowerShell command prompt, type the following command until the command returns the status **Online**: 
    
    ```PowerShell
    Get-SPEnterpriseSearchServiceInstance -Identity $<host n >
    ```

5. Clone the active search topology. At the Microsoft PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $ssa = Get-SPEnterpriseSearchServiceApplication
    $active = Get-SPEnterpriseSearchTopology -SearchApplication $ssa -Active
    $clone = New-SPEnterpriseSearchTopology -SearchApplication $ssa -Clone -SearchTopology $active
    ```

6. Add a new index component and associate it with a partition. At the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    New-SPEnterpriseSearchIndexComponent -SearchTopology $clone -SearchServiceInstance <host n > -IndexPartition <Index partition number>
    ```

    Where:
    
    -  _$clone_ is the cloned topology that you are changing. 
    
    -  _$\<host n\>_ is the PowerShell object reference to the running search service instance on the server that you want to add the index replica to. 
    
    -  _\<Index partition number\>_ is the number of the existing index partition that you are creating a replica of. For example, to create an index replica of index partition 0, choose "0" as the parameter value. 
    
    For example:
    
    ```PowerShell
    New-SPEnterpriseSearchIndexComponent -SearchTopology $clone -SearchServiceInstance $hostA -IndexPartition 0
    ```

7. Activate the clone topology. At the Microsoft PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    Set-SPEnterpriseSearchTopology -Identity $clone
    ```

8. Verify that your new topology is active and that the index component representing the new index replica is added. At the Microsoft PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    Get-SPEnterpriseSearchTopology -Active -SearchApplication $ssa
    ```

9. Monitor the distribution of the existing index to the new replica. The added index replica will have the state **Degraded** until the distribution is finished. At the Microsoft PowerShell command prompt, type the following command(s): 
    
    ```PowerShell
    Get-SPEnterpriseSearchStatus -SearchApplication $ssa -Text
    ```

   Repeat this command until all search components, including the new index component, output the state **Active**. For a large search index, this could take several hours. 
    
## Add a new index partition
<a name="Search_Index_Part"> </a>

When you add a new index partition, the search index has to be repartitioned. Depending on the size of the search index, this repartitioning can take several hours to complete.
  
To add an index partition and repartition the search index, you add a new index component to the search topology and associate this index component with a new index partition number. Adding an index partition and repartitioning the search index should be initiated as a separate process and should not be initiated while you are making other changes to the search topology.
  
You must add the same number of index replicas to the new index partition as you have for your existing partitions.
  
Before you add a new index partition to the search topology and start repartitioning the search index:
  
- Back up the Search service application and the existing search index. See [Back up Search service applications in SharePoint Server](../administration/back-up-a-search-service-application.md).
    
- Make sure that the current active topology is healthy. View the status of the search topology in the Search Administration page in Central Administration or run the Microsoft PowerShell cmdlet  `Get-SPEnterpriseSearchStatus`.
    
- Make sure that there is sufficient disk space available on the server where you will be adding the index partition. 
    
> [!CAUTION]
> The Search service application is paused during index repartitioning and cannot crawl or index content. Also, users will not be able to run queries. 
  
 **To add an index partition**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start a SharePoint Management Shell on one of the servers in the farm.
    
3. Start a search service instance on all the servers where you want to add an index replica for the new index partition. You create a PowerShell object reference to the search service instance that is used later in the procedure. For each server, at the Microsoft PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $<host n > = Get-SPEnterpriseSearchServiceInstance -Identity "<Server name>"
    Start-SPEnterpriseSearchServiceInstance -Identity $<host n >
    ```

    Where:
    
    -  _\<host n\>_ specifies the PowerShell object reference for the search service instance. 
    
    -  _\<Server name\>_ specifies the server on which you want to add an index component. The input must be a valid GUID, in the form  `12345678-90ab-cdef-1234-567890bcdefgh`; a valid name of a server (for example, **myserver1** ); or an instance of a valid **SearchServiceInstance** object. 
    
    For example:
    
    ```PowerShell
    $hostC = Get-SPEnterpriseSearchServiceInstance -Identity "myserver3"
    Start-SPEnterpriseSearchServiceInstance -Identity $hostC
    $hostD = Get-SPEnterpriseSearchServiceInstance -Identity "myserver4"
    Start-SPEnterpriseSearchServiceInstance -Identity $hostD
    ```

4. Wait until the search service instances are running. For each server, at the Microsoft PowerShell command prompt, type the following command until the command returns the status **Online**: 
    
    ```PowerShell
    Get-SPEnterpriseSearchServiceInstance -Identity $<host n >
    ```

5. Clone the active search topology. At the Microsoft PowerShell command prompt, type the following command(s):
   
    ```PowerShell
    $ssa = Get-SPEnterpriseSearchServiceApplication
    $active = Get-SPEnterpriseSearchTopology -SearchApplication $ssa -Active
    $clone = New-SPEnterpriseSearchTopology -SearchApplication $ssa -Clone -SearchTopology $active
    ```

    The command creates a clone search topology that can be referenced with  _$clone_ and returns information about the clone topology. Make a note of the topology Id of the cloned topology, in case you have to cancel the repartitioning process. 
    
6. Add a new index partition by adding one or more index components and associate them with the new index partition. We recommend that you create the same number of index replicas for the new index partition as you have for the existing partitions. For each new index component, at the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    New-SPEnterpriseSearchIndexComponent -SearchTopology $clone -SearchServiceInstance <host n > -IndexPartition <Index partition number>
    ```

    Where:
    
    -  _$clone_ is the cloned topology that you are changing. 
    
    -  _$\<host n\>_ specifies the PowerShell object reference for the search service instance. 
    
    -  _\<Index partition number\>_ is the number of the index partition that you are creating. By default, you have one index partition, which is called index partition 0. If you want to create a new index partition, enter the IndexPartition parameter value 1, followed by 2, then 3 and so forth. 
    
    For example, if you have an existing index partition 0 with index replicas on Host A and Host B, and you want to add a new index partition with index replicas on Host C and Host D:
    
    ```PowerShell
    New-SPEnterpriseSearchIndexComponent -SearchTopology $clone -SearchServiceInstance $hostC -IndexPartition 1
    New-SPEnterpriseSearchIndexComponent -SearchTopology $clone -SearchServiceInstance $hostD -IndexPartition 1
    ```

7. Verify that the Search service application is running. At the Microsoft PowerShell command prompt, type the following command(s):
   
    ```PowerShell
    $ssa.IsPaused() -ne 0
    ```

    - If this command returns **False**, the Search service application is running. Continue with step 9. 
    
    - If this command returns **True**, the Search service application is paused. Continue with step 8. 
    
8. If the Search service application is paused, find out why and if you have to wait for any operation to complete before you can continue with step 9. See [Manage a paused Search service application in SharePoint Server](manage-a-paused-search-service-application.md) for more information. 
    
9. Start the activation of the clone topology. This will start the activation of the topology that includes the new index replicas associated with the new index partition. This will start the index repartitioning process.
    
    > [!IMPORTANT]
    > The Search service application is paused during index repartitioning and cannot crawl or index content. Also, users will not be able to run queries. You will not be able to access the Windows PowerShell console where the activation command runs. 
  
    > [!NOTE]
    > The Search Administration page in Central Administration does not show that the Search service application has been paused for index repartitioning. However, because all query processing components are suspended when you pause the Search service application for repartitioning, the Search administration page will show errors for the query processing components during this process. 
  
    At the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $ssa.PauseForIndexRepartitioning()
    Set-SPEnterpriseSearchTopology -Identity $clone
    ```

10. Monitor the progress of the index repartitioning process. You can only monitor the progress of the repartitioning process on the primary index components of the existing topology. The following steps show you how to find the primary index components.
    
    > [!NOTE]
    > You will not be able to run any commands in the existing SharePoint Management Shell until the topology activation, including the index repartitioning process, is finished. Run the following commands in a second SharePoint Management Shell. 
  
    - Start a second SharePoint Management Shell.
    
    - Find the primary index replica for each of the existing index partitions. At the Windows PowerShell command prompt of the second SharePoint Management Shell, type the following command(s):
    
    ```PowerShell
    $ssa = Get-SPEnterpriseSearchServiceApplication
    Get-SPEnterpriseSearchStatus -SearchApplication $ssa -Text
    ```

    The command returns a list of index components and their properties. Make a note of the names of the primary index component(s). These are the index components that have the property **Primary: True**. 
  
    For example, the output could look like this. In this example, IndexComponent2 is the primary index component:
    
    ```
    Name      : IndexComponent1
    State     : Active
    Primary   : False
    Partition : 0
    Host      : MyMachine1
    Name      : Cell:IndexComponent1-SPd32cdffb08a2I.0.0
    State     : Active
    Primary   : False
    Partition : 0
    Name      : IndexComponent2
    State     : Active
    Primary   : True
    Partition : 0
    Host      : MyMachine2
    Name      : Cell:IndexComponent2-SPd32cdffb08a2I.1.0
    State     : Active
    Primary   : True
    Partition : 0
    ```

11. For each primary index component, monitor the index repartitioning progress. At the Windows PowerShell command prompt of the second SharePoint Management Shell, type the following command(s):
    
    ```PowerShell
    Get-SPEnterpriseSearchStatus -SearchApplication $ssa -Healthreport -Component <Index component name> | ? { ($_.name -match "repart") -or ( $_.name -match "splitting") } | ft -AutoSize Name, Message
    ```

    Where:
    
    -  _\<Index component name\>_ is the name of the primary index component that you want to monitor the progress of, for instance **IndexComponent2**. 
    
    Monitor the output of the command for each primary index component. The output of the command contains progress information about the repartitioning of the index.
    
    During the initial phase of the index repartitioning process, the output will look something like this:
    
    ```
    Name                                              Message
    ----                                              -------
    repartition_component_state[SP...]                Pending
    ```

    The index partitions are split during the main phase of the index repartitioning process. During this phase, the output will look something like this:
    
    ```
    Name                                              Message
    ----                                              -------
    index splitting: current fusion progress[SP...]   <Percentage value>
    index splitting: splitting state [SP...]          Index splitter running fusion, building: <Folder>
    repartition_component_state [SP...]               Splitting
    ```

    The percentage value in the output indicates the approximate progress of the repartitioning process.
    
    Repeat this command for all primary index components until the output of the commands no longer returns any values. That means that the index repartitioning process has completed and that the repartitioned index will now be replicated and distributed over the servers. This could take several hours.
    
12. Monitor the progress of the distribution of the index to the new index replicas. To do this, verify that your new topology is active, and that all search components are healthy. At the Windows PowerShell command prompt of the second SharePoint Management Shell, type the following command(s):
    
    ```PowerShell
    Get-SPEnterpriseSearchStatus -SearchApplication $ssa | ft -AutoSize Name, State, Details
    ```

    During the distribution of the index to the new index replicas, the added index replicas will return the state **Degraded**. The distribution is finished when all index components return the state **Active** in the output. This could take several hours. 
    
    > [!NOTE]
    > The query processing components are suspended because you have paused the Search service application for index repartitioning. In the output, the query processing components will be listed with the state **Unknown**.
  
13. In the SharePoint Management Shell that you used to start the topology activation process, verify that the search topology activation command has completed.
    
14. (Optional) Restart the SharePoint Search Host Controller service on all the servers that hosted index components (representing a primary index replica or any other index replica) prior to the repartitioning.
    
    Perform this step to get a correct document count and free up memory after repartitioning the search index. If you decide not to perform this step, it will take a few days and some indexing iterations for the memory usage to be gradually reduced and the document count (as returned by PowerShell cmdlets and in the Search Administration page in Central Administration) to be correct.
    
    > [!NOTE]
    > To avoid query outages, ensure that at least one index component returns the state **Running** for each index partition before you restart the SharePoint Search Host Controller service. 
  
    > [!IMPORTANT]
    > Do not use the Services on Server page on the SharePoint Server Central Administration Web site to restart this service. 
  
    - To restart the SharePoint Search Host Controller, open a command prompt window on each of the servers that host index components for existing index partitions.
    
    - To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
    - To restart the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
15. Resume the Search service application. At the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $ssa.ResumeAfterIndexRepartitioning()
    ```

## Cancel the repartitioning process
<a name="Search_Index_Cancel"> </a>

If you have to cancel an ongoing repartitioning process, use the following procedure.
  
 **To cancel the repartitioning process**
  
1. Start a new SharePoint Management Shell on the server where you ran the topology activation command.
    
2. Retrieve the activating topology Id. At the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $activating = Get-SPEnterpriseSearchTopology -Identity <Id of the activating topology> -SearchApplication $ssa
    ```

    Where:
    
    -  _\<Id of the activating topology\>_ is the identity (GUID) of the clone topology that you wrote down when you cloned the search topology. 
    
3. Cancel the topology activation. At the Windows PowerShell command prompt, type the following command(s):
    
    ```PowerShell
    $activating.CancelTopologyActivation()
    ```

## Remove an index component
<a name="Search_Index_Remove"> </a>

If you have more than one active index replica for an index partition, you can remove an index replica by performing the procedure **Remove a search component** in the article [Manage search components in SharePoint Server](manage-search-components.md).
  
You cannot remove the last index replica of an index partition using this procedure. If you have to remove all index replicas from the search topology, you must remove and re-create the Search service application and create a completely new search topology that has the reduced number of index partitions.
  
## Move an index component
<a name="Index_Comp_Move"> </a>

If you want to move an index replica from one server to another, we recommend that you add a new index component to the search topology before you remove the old index component.
  
 **To move an index component**
  
1. Add a new index component to the server that you want to move the index replica to. Clone the search topology, add a new index replica, wait for the index to be replicated to the new index replica and activate the search topology. See [Add an index replica to an existing index partition](manage-the-index-component.md#Search_Index_Repl).
    
2. Wait until the new index replica is ready to serve queries. View the status of the search topology in the Search Administration page in Central Administration or run the Windows PowerShell cmdlet  `Get-SPEnterpriseSearchStatus`. Before you proceed, the index replica that you have added must be **Active**. 
    
3. Clone the search topology again.
    
4. Remove the superfluous index replica by removing the index component. See the procedure **Remove a search component** in the article [Manage search components in SharePoint Server](manage-search-components.md).
    
5. Activate the search topology again.
    
This will ensure fault tolerance of the search index while you are moving the index replica.
  

