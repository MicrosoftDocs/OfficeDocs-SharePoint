---
title: Manage search components in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 197ce911-c4f6-40a3-84c1-fb5999623b51
---


# Manage search components in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to use Windows PowerShell to manage search components in an existing search topology that has content in the SharePoint Server search index. Use these procedures to scale out or scale down the search topology of the Search service application.The procedures and the examples in this article assume that SharePoint ServerSharePoint Server 2016 and the Search service application are installed, and that there is an existing search topology and items in the SharePoint Server search index. If SharePoint Server and the Search service application are newly installed and there are no items in the SharePoint Server search index, follow the procedures in  [Change the default search topology in SharePoint Server](html/change-the-default-search-topology-in-sharepoint-server.md).The procedures in this article apply to the following search components:
- Analytics processing component
    
  
- Content processing component
    
  
- Crawl component
    
  
- Search administration component
    
  
- Query processing component
    
  
For information about procedures to manage the index component, see  [Manage the index component in SharePoint Server](html/manage-the-index-component-in-sharepoint-server.md).In this article:
-  [Before you begin](#begin)
    
  
-  [Start a search service instance on a server](#Search_Comp_SSI)
    
  
-  [Retrieve the active search topology](#Search_Comp_Retrieve)
    
  
-  [Clone the active search topology](#Search_Comp_Clone)
    
  
-  [Add a search component](#Search_Comp_Add)
    
  
-  [Remove a search component](#Search_Comp_Remove)
    
  
-  [Move a search component](#Search_Comp_Move)
    
  
-  [Activate a search topology](#Search_Comp_Activate)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin, review the following prerequisites.
- SharePoint Server is installed and a Search service application with a search topology is created. The Search service application is in a healthy state and is not paused for any reason.
    
  
- The user account that is performing the procedures in this article is a member of the **Farm Administrators** group.
    
  
- You have planned a target search topology.
    
  
- SharePoint Server is installed on all the servers that you want to host search components on. The servers have been added to the farm and you are an administrator on all these servers. You can create new application servers or define application servers in an existing deployment.
    
  

> [!IMPORTANT:]

  
    
    


## Start a search service instance on a server
<a name="Search_Comp_SSI"> </a>

Before you add search components to a new server, you must first start a search service instance on the server. The search service instance starts all the necessary Windows services that are used by the search service (OSearch16 and SPSearchHostController). **To start a search service instance**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell on one of the servers in the farm.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
$<host n > = Get-SPEnterpriseSearchServiceInstance -Identity "<Server name>"
Start-SPEnterpriseSearchServiceInstance -Identity $<host n >
  ```


    Where:
    
  - $ *<host n>*  specifies the PowerShell object reference for the search service instance.
    
  
  -  *<Server name>*  specifies the server on which you want to add an index component. The input must be a valid GUID, in the form12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a server (for example, **myserver1** ); or an instance of a valid **SearchServiceInstance** object.
    
  

    For example:
    


  ```
  
$hostA = Get-SPEnterpriseSearchServiceInstance -Identity "myserver1"
$hostB = Get-SPEnterpriseSearchServiceInstance -Identity "myserver2"
Start-SPEnterpriseSearchServiceInstance -Identity $hostA
Start-SPEnterpriseSearchServiceInstance -Identity $hostB 

  ```


    You use the references  *($<host n>)*  to specify the target server when you add search components.
    
  
4. Wait until all the search service instances are running. For each of the search service instances, at the Microsoft PowerShell command prompt, type the following command until the command returns the status **Online**:
    
  ```
  
Get-SPEnterpriseSearchServiceInstance -Identity $<host n >

  ```


    For example:
    


  ```
  
Get-SPEnterpriseSearchServiceInstance -Identity $hostA
TypeName    : SharePoint Server Search
Description : Index content and serve search queries
Id          : 82ce8815-ecbd-4cf3-a98e-33f20bd86039
Server      : SPServer Name=myserver1.example.com
Service     : SearchService Name=OSearch16
Role        : None
Status      : Online

  ```


## Retrieve the active search topology
<a name="Search_Comp_Retrieve"> </a>

To view the active search topology of the Search service application, you have to use Microsoft PowerShell. **To view the active search topology**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication
$active = Get-SPEnterpriseSearchTopology -Active -SearchApplication $ssa 
$active
  ```

The command returns information about the active topology, for example: TopologyId : 2d7bb046-1ad4-43a9-9984-754c4551a3ec CreationDate : 1/25/2016 3:06:00 AM State : Active ComponentCount : 6
## Retrieve a list of search components
<a name="proc2"> </a>

To view a list of search components in the active search topology with their properties, you have to use Microsoft PowerShell. One of the search component properties is the search component Id. You will only need the search component Id to remove a search component. **To view a list of all search components**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication
$active = Get-SPEnterpriseSearchTopology -SearchApplication $ssa -Active
Get-SPEnterpriseSearchComponent -SearchTopology $active
  ```


    The command returns a list of search components in the active search topology and their properties.
    
  

## Clone the active search topology
<a name="Search_Comp_Clone"> </a>

To make any changes to the search topology in a search installation that has items in the search index, you first have to create a new topology object. You modify this new topology object, a clone of the active topology, by adding or removing search components. After you have made the changes to the clone topology object, you make the clone the active topology. **To clone the active topology**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication
$active = Get-SPEnterpriseSearchTopology -SearchApplication $ssa -Active
$clone = New-SPEnterpriseSearchTopology -SearchApplication $ssa -Clone -SearchTopology $active
  ```


    The command creates a clone search topology that can be referenced with  *$clone*  if you continue to use the same SharePoint 2016 Management Shell to add or remove search components and to activate the search topology.
    
  
4. (Optional) If you have to remove search components from the search topology, you have to retrieve the search component Id. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
Get-SPEnterpriseSearchComponent -SearchTopology $clone
  ```


    The command returns a list of search components in the cloned search topology and their properties, including the search component Id.
    
  

## Add a search component
<a name="Search_Comp_Add"> </a>

You cannot change the active search topology directly. This procedure assumes that you have created a clone topology object as described in  [Clone the active search topology](#Search_Comp_Clone). You can use the following Microsoft PowerShell cmdlets for each search component:
- New-SPEnterpriseSearchAdminComponent
    
  
- New-SPEnterpriseSearchAnalyticsProcessingComponent
    
  
- New-SPEnterpriseSearchContentProcessingComponent
    
  
- New-SPEnterpriseSearchCrawlComponent
    
  
- New-SPEnterpriseSearchQueryProcessingComponent
    
  

> [!NOTE:]

  
    
    

 **To add a search component**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
New-SPEnterpriseSearch<SearchComponent> -SearchTopology $clone -SearchServiceInstance $<host n >
  ```


    Where:
    
  -  *<SearchComponent>*  is the name of the search component type that you are adding.
    
  
  -  *$clone*  is the cloned topology that you are changing. See [Clone the active search topology](#Search_Comp_Clone).
    
  
  -  *$<host n>*  is the PowerShell object reference to the running search service instance on the server that you want to add the search component to. See [Start a search service instance on a server](#Search_Comp_SSI).
    
  

    For example, the following command adds a content processing component to the clone topology on the server identified by the search service instance reference $hostA.
    


  ```
  
New-SPEnterpriseSearchContentProcessingComponent -SearchTopology $clone -SearchServiceInstance $hostA
  ```

4. Verify that the new search component was added to the clone topology. At the Microsoft PowerShell command prompt, type the command:
    
  ```
  
Get-SPEnterpriseSearchComponent -SearchTopology $clone
  ```


## Remove a search component
<a name="Search_Comp_Remove"> </a>

To remove a search component, you have to use Windows PowerShell. You cannot change the active search topology directly. This procedure assumes that you have created a clone topology object as described in  [Clone the active search topology](#Search_Comp_Clone).
> [!NOTE:]

  
    
    

 **To remove a search component**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. Make sure that the current active topology is healthy and that the search component that you are about to remove is **Active**. View the status of the search topology in the Search Administration page in Central Administration or run the Windows PowerShell cmdletGet-SPEnterpriseSearchStatus.
    
  
4. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
Remove-SPEnterpriseSearchComponent -Identity <Search component id> -SearchTopology $clone
  ```


    Where:
    
  -  *<Search component id>*  is the Id of the search component that you want to remove. Use the search component Id from the clone topology. To retrieve the search component Id, see step 4 in [Clone the active search topology](#Search_Comp_Clone).
    
  
  -  *$clone*  is the cloned topology that you are changing. See [Clone the active search topology](#Search_Comp_Clone).
    
  
5. When prompted, confirm that you want to remove the search component.
    
  

## Move a search component
<a name="Search_Comp_Move"> </a>

If you want to move a search component from one server to another, we recommend that you add a new search component to the search topology before you remove the old search component. **To move a search component**
1. Clone the active search topology. See  [Clone the active search topology](#Search_Comp_Clone).
    
  
2. Add a new search component to the server that you eventually want the search component to be hosted on. See  [Add a search component](#Search_Comp_Add).
    
  
3. Activate the search topology. This topology will have one superfluous search component. See  [Activate a search topology](#Search_Comp_Activate).
    
  
4. Make sure that the current active topology is healthy. View the status of the search topology in the Search Administration page in Central Administration or run the Windows PowerShell cmdlet Get-SPEnterpriseSearchStatus.
    
  
5. Clone the search topology again. See  [Clone the active search topology](#Search_Comp_Clone).
    
  
6. Remove the superfluous search component. See  [Remove a search component](#Search_Comp_Remove).
    
  
7. Activate the search topology again. See  [Activate a search topology](#Search_Comp_Activate).
    
  

## Activate a search topology
<a name="Search_Comp_Activate"> </a>

To activate a search topology, you have to use Windows PowerShell. **To activate a search topology**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell. If you already have an open SharePoint 2016 Management Shell in which you have created reusable Microsoft PowerShell object references, use the open shell instead.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
Set-SPEnterpriseSearchTopology -Identity $clone
  ```


    Where:
    
  -  *$clone*  is the cloned topology that you are changing. See [Clone the active search topology](#Search_Comp_Clone).
    
  
4. Verify that your new topology is active. At the Windows PowerShell command prompt, type the following command(s):
    
  ```
  
Get-SPEnterpriseSearchTopology -Active -SearchApplication $ssa
  ```


    The command returns an overview of active and inactive topologies, for example:
    


  ```
  
TopologyId     : fce8507d-61c6-4498-8038-4fd2d0a62c6e
CreationDate   : 1/30/2016 2:52:00 AM
State          : Inactive
ComponentCount : 6

TopologyId     : b63d48b2-df5c-41be-a7f4-9abaee483611
CreationDate   : 1/30/2016 4:30:00 AM
State          : Active
ComponentCount : 7
  ```


    You will see that the component count of the active topology reflects the changes that you have made.
    
  

