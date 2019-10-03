---
title: "Change the default search topology in SharePoint Server"
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
ms.assetid: 7fa9730a-2d11-4c78-b546-60179c5bb646
description: "Learn how to use Windows PowerShell to change from the default search topology with an empty search index in SharePoint Server to a new search topology."
---

# Change the default search topology in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article explains how to create and activate search components in a new search topology starting from the default search topology. The procedures and the examples in this article assume that SharePoint Server and the Search service application are newly installed and that there is no content in the SharePoint Server search index. You can also use the procedures and examples to manage the search topology in SharePoint Server when the topology is part of a cloud hybrid search solution.
  
If there are items in the SharePoint Server search index, follow the procedures in [Manage search components in SharePoint Server](manage-search-components.md) and [Manage the index component in SharePoint Server](manage-the-index-component.md).
  
    
## Before you begin
<a name="begin"> </a>

Before you begin, review the following prerequisites.
  
- SharePoint Server is installed on a single server and a Search service application with a default search topology is created. In the default search topology, all the search components are located on the server that hosts Central Administration.
    
- You are an administrator of the Search service application.
    
- You have planned a target search topology. [Plan enterprise search architecture in SharePoint Server 2016](plan-enterprise-search-architecture.md) gives step-by-step guidance for search in enterprises, including hardware requirements. For example farm architectures and search topologies for Internet sites, see the technical diagram [Internet sites search architectures for SharePoint Server 2016](https://download.microsoft.com/download/D/9/4/D947D942-6BB5-4F28-A51B-1FAE16334C51/SP_2016_Internet_Site_Search_Model.pdf). We recommend that you plan a target search topology based on the expected number of items in the search index for search in enterprises.
    
- SharePoint Server is installed on all the servers that you want to host search components on. The servers have been added to the farm and you are an administrator on all these servers. You can create new application servers or define application servers in an existing deployment.
    
## Overview: changing a search topology without content in the search index
<a name="Topology_OverviewDefault"> </a>

The following list provides an overview of the tasks involved to change from the default search topology, without any content in the SharePoint Server search index, to a new search topology.
  
- Ensure that no crawls have been started and that the SharePoint Server search index is empty.
    
- Start a search service instance on all the servers that you want to host search components on.
    
- Create a new empty search topology.
    
- Add search components to the new search topology.
    
- Activate the new search topology.
    
- Verify that the search topology is active.
    
## Example: Change from the default search topology to a small enterprise search topology
<a name="Topology_ExampleDefaultSmall"> </a>

The following procedures will create and activate a small enterprise search topology on multiple servers, as planned for in the table **Target search topology**. The small enterprise search topology uses virtual machines on physical application servers. All search components in this example are set up with fault tolerance, which means that all search components and index partitions are deployed across more than one physical machine on separate failure domains. 
  
You can follow the same procedures using different variables if you want to scale out to a larger enterprise search topology or to a search topology for Internet Sites.
  
**Target search topology**

|             **Virtual machine A (on physical application server X)   myserver1.example.com**              |   **Virtual machine B (on physical application server X)   myserver2.example.com**   |             **Virtual machine C (on physical application server Y)   myserver3.example.com**              |   **Virtual machine D (on physical application server Y)   myserver4.example.com**   |
| :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| Admin component 1   <br/><br/>Crawl component 1   <br/><br/>Content processing component 1   <br/><br/>Analytics processing component 1 | Query processing component 1   <br/><br/>Index component 1 (that belongs to index partition 0) | Admin component 2   <br/><br/>Crawl component 2   <br/><br/>Content processing component 2   <br/><br/>Analytics processing component 2 | Query processing component 2   <br/><br/>Index component 2 (that belongs to index partition 0) |
   
1. Ensure that no crawls have been started and that the search index is empty on the server that hosts Central Administration.
    
  - Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  - In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
  - On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
  - Verify that the search index is empty. On the **Search Administration** page, under **System Status**, verify that **Searchable items** displays "0". 
    
    > [!CAUTION]
    > If there are items in the SharePoint Server search index, do not continue with this procedure. 
  
  - Verify that no crawls have been started. On the **Search Administration** page, under **Crawling**, click **Content Sources**. On the **Manage Content Sources** page, verify that the **Status** column for any existing content source displays **Idle**.
    
2. Start a SharePoint Management Shell on one of the servers in the farm.
    
3. Specify the new servers you want to add search components to, start a search service instance (ssi) on these servers and create references to the search service instances. In this procedure we have used the example host names "myserver< *n*  >" for the servers as listed in the **Target search topology** table. At the Windows PowerShell command prompt, type the following command(s): 
    
  ```
  $hostA = Get-SPEnterpriseSearchServiceInstance -Identity "myserver1"
  $hostB = Get-SPEnterpriseSearchServiceInstance -Identity "myserver2"
  $hostC = Get-SPEnterpriseSearchServiceInstance -Identity "myserver3"
  $hostD = Get-SPEnterpriseSearchServiceInstance -Identity "myserver4"
  Start-SPEnterpriseSearchServiceInstance -Identity $hostA
  Start-SPEnterpriseSearchServiceInstance -Identity $hostB
  Start-SPEnterpriseSearchServiceInstance -Identity $hostC
  Start-SPEnterpriseSearchServiceInstance -Identity $hostD
  
  ```

4. Wait until all the search service instances are running. At the Windows PowerShell command prompt, type the following commands until the commands return the state "Online" for each of the search service instances:
    
  ```
  Get-SPEnterpriseSearchServiceInstance -Identity $hostA
  Get-SPEnterpriseSearchServiceInstance -Identity $hostB
  Get-SPEnterpriseSearchServiceInstance -Identity $hostC
  Get-SPEnterpriseSearchServiceInstance -Identity $hostD
  ```

5. Create a new search topology and a reference to the new search topology. At the Windows PowerShell command prompt, type the following command(s):
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  $newTopology = New-SPEnterpriseSearchTopology -SearchApplication $ssa
  
  ```

6. Add all the search components to the new search topology. The following Windows PowerShell commands will create the search components of the new topology and assign them to the new servers. In this small enterprise search topology there is one index partition, index partition 0. This is indicated with the parameter  `-IndexPartition` in the command  `New-SPEnterpriseSearchIndexComponent`. The index partition has one index replica on virtual machine B and one index replica on virtual machine D. Each index replica will contain the exact same search index and is hosted on a different physical server to achieve fault tolerance. At the Windows PowerShell command prompt, type the following command(s):
    
  ```
  New-SPEnterpriseSearchAdminComponent -SearchTopology $newTopology -SearchServiceInstance $hostA
  New-SPEnterpriseSearchCrawlComponent -SearchTopology $newTopology -SearchServiceInstance $hostA
  New-SPEnterpriseSearchContentProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostA
  New-SPEnterpriseSearchAnalyticsProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostA
  New-SPEnterpriseSearchQueryProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostB
  New-SPEnterpriseSearchIndexComponent -SearchTopology $newTopology -SearchServiceInstance $hostB -IndexPartition 0
  New-SPEnterpriseSearchAdminComponent -SearchTopology $newTopology -SearchServiceInstance $hostC
  New-SPEnterpriseSearchCrawlComponent -SearchTopology $newTopology -SearchServiceInstance $hostC
  New-SPEnterpriseSearchContentProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostC
  New-SPEnterpriseSearchAnalyticsProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostC
  New-SPEnterpriseSearchQueryProcessingComponent -SearchTopology $newTopology -SearchServiceInstance $hostD
  New-SPEnterpriseSearchIndexComponent -SearchTopology $newTopology -SearchServiceInstance $hostD -IndexPartition 0 
  
  ```

7. Activate the new search topology. At the Windows PowerShell command prompt, type the following command:
    
  ```
  Set-SPEnterpriseSearchTopology -Identity $newTopology
  ```

8. Verify that the new search topology is active. At the Windows PowerShell command prompt, type the following command:
    
  ```
  Get-SPEnterpriseSearchTopology -SearchApplication $ssa
  
  ```

    The command returns an overview of active and inactive topologies, in this example:
    
  ```
  TopologyId     : fce8507d-61c6-4498-8038-4fd2d0a62c6e
  CreationDate   : 1/30/2016 2:52:00 AM
  State          : Inactive
  ComponentCount : 6
  TopologyId     : b63d48b2-df5c-41be-a7f4-9abaee483611
  CreationDate   : 1/30/2016 4:30:00 AM
  State          : Active
  ComponentCount : 12
  ```

    The previous topology, the default topology in this example, is listed as inactive. The new active topology from this example will have a component count of twelve.
    
9. Verify that all components of the new search topology are running correctly. At the Windows PowerShell command prompt, type the following command:
    
  ```
  Get-SPEnterpriseSearchStatus -SearchApplication $ssa -Text
  ```

    This command should return a list of all the active search components. The state of the active search components should be displayed as **Active**. 
    

