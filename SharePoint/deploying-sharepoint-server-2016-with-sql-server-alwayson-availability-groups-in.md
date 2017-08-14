---
title: Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure
ms.prod: SHAREPOINT
ms.assetid: af7cf3e7-94b1-4a5d-8cb9-80c5a0b397f2
---


# Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-02-14* **Summary:** Get an overview of deploying SharePoint Server 2016 in Microsoft Azure with links to each phase of the deployment.Step through the deployment an intranet-only, high availability SharePoint Server 2016 farm in Azure with these virtual machines:
- Two SharePoint front end and distributed cache servers
    
  
- Two SharePoint application and search servers
    
  
- One cluster majority node server
    
  
- Two domain controllers
    
  
Here is the configuration, with placeholder names for each server. **An intranet-only, high availability SharePoint Server 2016 farm in Azure**
  
    
    
![Phase 4 of the SharePoint Server 2016 highly-available farm in Azure with SharePoint servers](images/)
  
    
    
Two virtual machines for each role ensure high availability. All of the virtual machines are in a single cross-premises Azure virtual network. Each group of virtual machines for a specific role is in its own subnet and availability set.
    
> [!NOTE:]

  
    
    


## Bill of materials

This baseline configuration requires the following set of Azure services and components:
- Nine virtual machines.
    
  
- Four availability sets.
    
  
- One cross-premises virtual network with five subnets.
    
  
- Nine storage accounts.
    
  
- One Azure subscription.
    
  
Here are the virtual machines and their default sizes for this configuration.
### 

ItemVirtual machine descriptionGallery imageDefault size1.  <br/> First domain controller  <br/> Windows Server 2016 Datacenter  <br/> D2  <br/> 2.  <br/> Second domain controller  <br/> Windows Server 2016 Datacenter  <br/> D2  <br/> 3.  <br/> First database server  <br/> Microsoft SQL Server 2016 Enterprise – Windows Server 2016  <br/> DS4  <br/> 4.  <br/> Second database server  <br/> Microsoft SQL Server 2016 Enterprise – Windows Server 2016  <br/> DS4  <br/> 5.  <br/> Majority node for the cluster  <br/> Windows Server 2016 Datacenter  <br/> D2  <br/> 6.  <br/> First SharePoint application and search server  <br/> Microsoft SharePoint Server 2016 Trial – Windows Server 2012 R2  <br/> DS4  <br/> 7.  <br/> Second SharePoint application and search server  <br/> Microsoft SharePoint Server 2016 Trial – Windows Server 2012 R2  <br/> DS4  <br/> 8.  <br/> First SharePoint front end and distributed cache server  <br/> Microsoft SharePoint Server 2016 Trial – Windows Server 2012 R2  <br/> DS4  <br/> 9.  <br/> Second SharePoint front end and distributed cache server  <br/> Microsoft SharePoint Server 2016 Trial – Windows Server 2012 R2  <br/> DS4  <br/> To compute the estimated costs for this configuration, see the  [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/). 
> [!NOTE:]

  
    
    


## Phases of deployment

You deploy this SharePoint Server 2016 farm with the following phases:
-  [SharePoint Intranet Farm in Azure Phase 1: Configure Azure](html/sharepoint-intranet-farm-in-azure-phase-1-configure-azure.md)
    
    Create resource groups, storage accounts, availability sets, and a cross-premises virtual network.
    
  
-  [SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers](html/sharepoint-intranet-farm-in-azure-phase-2-configure-domain-controllers.md)
    
    Create and configure replica Windows Server Active Directory (AD) domain controllers
    
  
-  [SharePoint Intranet Farm in Azure Phase 3: Configure SQL Server Infrastructure](html/sharepoint-intranet-farm-in-azure-phase-3-configure-sql-server-infrastructure.md)
    
    Create and configure the SQL Server virtual machines, prepare them for use with SharePoint, and create the cluster.
    
  
-  [SharePoint Intranet Farm in Azure Phase 4: Configure SharePoint servers](html/sharepoint-intranet-farm-in-azure-phase-4-configure-sharepoint-servers.md)
    
    Create and configure the four SharePoint server virtual machines.
    
  
-  [SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases](html/sharepoint-intranet-farm-in-azure-phase-5-create-the-availability-group-and-add.md)
    
    Prepare databases and create a SQL Server AlwaysOn availability group.
    
  
This configuration is a prescriptive, phase-by-phase guide for a predefined architecture to create a highly available intranet SharePoint Server 2016 farm in Azure infrastructure services. Keep the following in mind:
- If you are an experienced SharePoint implementer, feel free to adapt the instructions in phases 3 through 5 and build the farm that best suits your needs. 
    
  
- If you already have an existing Azure hybrid cloud deployment, feel free to adapt or skip the instructions in phases 1 and 2 and host the new SharePoint farm on the appropriate set of subnets. 
    
  
To build a dev/test environment or a proof-of-concept of this configuration, see  [Intranet SharePoint Server 2016 in Azure dev/test environment](html/intranet-sharepoint-server-2016-in-azure-dev-test-environment.md).
## Next step

Start the configuration with  [SharePoint Intranet Farm in Azure Phase 1: Configure Azure](html/sharepoint-intranet-farm-in-azure-phase-1-configure-azure.md).
> [!TIP:]

  
    
    


# See also

#### 

 [Install and configure SharePoint Server 2016](html/install-and-configure-sharepoint-server-2016.md)
  
    
    

#### 

 [SharePoint Server 2016 in Microsoft Azure](html/sharepoint-server-2016-in-microsoft-azure.md)
  
    
    
 [Designing a SharePoint Server 2016 farm in Azure](html/designing-a-sharepoint-server-2016-farm-in-azure.md)
  
    
    

  
    
    

