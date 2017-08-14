---
title: Overview of Microsoft Identity Manager Synchronization Service  in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: dee7c975-5738-494f-bf70-31b0e0bc8206
---


# Overview of Microsoft Identity Manager Synchronization Service  in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-03-13* ** Summary:** Learn about the MIM Synchronization service that is used in a SharePoint Server 2016 farm.
> [!IMPORTANT:]

  
    
    


## New to SharePoint Server 2016: MIM Synchronization service
<a name="BKMK_WhatIsMIM1"> </a>

Previous versions of SharePoint Server had a built-in copy of ForeFront Identity Manager (FIM) that ran inside SharePoint Server that allow user profile synchronization to occur. That version of FIM powered the User Profile Synchronization for products like SharePoint Server 2010 and SharePoint Server 2013. But in SharePoint Server 2016, FIM has been removed in favor of Microsoft Identity Manager, which is the successor to the FIM technology. Even though FIM has been removed, the basic architecture for MIM uses some of the same FIM technology. For addtional information on FIM technology, see  [FIM 2010 Technical Overview](https://go.microsoft.com/fwlink/?linkid=841840)MIM is a separate server technology (not built-in to SharePoint Server). That means, if you have MIM, specifically the MIM Synchronization Service, running in your company, more than one SharePoint Server 2016 farm can rely upon it.MIM consists of several logical components which are responsible for various functions. It has various components which provide functionalities in the areas of policy modeling, workflow, group management, password management, end-user self-service, reporting and RBAC.It's also important to note here, that Active Directory Import (sometimes called Active Directory Direct Import) is also included with SharePoint Server 2016, and is a User Profile Synchronization alternative that will not need a separate server installation. This means that SharePoint Server 2016 offers two options for User Profile Sync.Which option is right for you?
### 

 **Microsoft Identity Management server** <br/> **Active Directory Import** <br/> Pros  <br/>  Flexibility allows for customized import. <br/>  Can be customized for bidirectional flow. <br/>  Imports user profile photos automatically. <br/>  Supports non-Active Directory LDAP sources. <br/>  Multi-forest scenarios are supported. <br/>  Very fast performance. <br/>  Known to be reliable (used by Office 365). <br/>  Configurable inside of Central Administration. (Less complex). <br/> Cons  <br/>  A separate MIM server is recommended for use with your SharePoint farm. <br/>  The more customized the more complex the architecture, deployment, and management. <br/>  Import is unidirectional (changes go from Active Directory to SharePoint Server Profile). <br/>  Import from a single Active Directory forest only. <br/>  Does not import user photos. <br/>  Supports Active Directory LDAP only. <br/>  Multi-forest scenarios are supported. <br/> 
> [!TIP:]

  
    
    


## What is the MIM Synchronization Service?
<a name="BKMK_WhatIsMIM1"> </a>

The MIM Synchronization service imports and aggregates data in a central identity repository known as the metaverse, and implements a staging area referred to as the Connector Space (CS). The synchronization service is responsible for managing the connection with all managed identity systems by using Management Agents (MAs). This service also fulfills the provisioning and de-provisioning requests in the connected systems.
> [!NOTE:]

  
    
    

The description of the various components of the MIM Synchronization Service are listed here:
- **Management Agents** (MAs) are responsible for flowing data between a specific connected data source and the metaverse. They contain rules that govern how MIM connects to a data source and how objects and their attributes are synchronized with that data source. MAs can connect to identity stores through Connectors. MIM provides connector for the most common identity stores used in enterprises.
    
    The MIM Synchronization Service establishes connectivity with the MIM Service and associated database by the creation of a MIM Service MA. This MA imports data from the MIM Service via direct connectivity to the underlying SQL database. However, all exports to the MIM Service are made by using Web services to ensure all applicable policies and workflows are applied to changes initiated from the Synchronization Service. A single MIM Service MA will be established within the MIM Synchronization Service and given a name of MIM Service Management Agent. This MA will be responsible for mapping MIM Service objects to metaverse objects.
    
  
- **Connector Space** (CS) is a storage area or staging area that is used by the MAs to move data into and out of a connected identity store. Each connected identity store has its own connector space which contains the set of objects and attributes from that data source that are of interest to the synchronization engine. Connector Spaces are used to determine the changes that need to be synchronized between the connected identity store and the metaverse.
    
  
- **Metaverse** is the principal repository for MIM composed of a set of tables that contain the integrated ("joined") identity information imported from multiple data sources. User information from various systems is imported and aggregated in the metaverse to form a single identity for each user. The default installation of MIM implements a base schema which includes objects and attributes that are commonly leveraged as part of an identity management solution. To ensure full extensibility, MIM allows for the expansion of the schema by the creation of new objects types and attributes.
    
  
The MIM Synchronization Service uses a SQL Server back-end database to store the data that it manages as well as its own configuration. The metaverse and the connector spaces are located within this database.
## So what does a typical topology look like?
<a name="BKMK_WhatIsMIM1"> </a>

A typical SharePoint Server 2016 topology of a MIM implementation may look like the following diagram.The data is synchronized between Active Directory and the metaverse by using the Active Directory connector space (CS) by an Active Directory management agent (MA). Data is also synchronized between SharePoint and the metaverse by using the SharePoint connector space by a SharePoint management agent. Commonly as part of that synchronization, data is exported to the SharePoint User profile store.
  
    
    
![Displays the MIM Synchronization Service in SharePoint Server 2016](images/)
  
    
    

  
    
    

  
    
    

## How do I use these concepts ?
<a name="BKMK_WhatIsMIM1"> </a>

Now that you have a basic understanding of the general terms of what is an identity manager and how the MIM Synchronization Service works in SharePoint Server. The next thing you probably want to know is how do I install it and how do I get a MIM solution working in SharePoint Server.  [Installing Microsoft Identity Manager (MIM)](install-microsoft-identity-manager-for-user-profiles-in-sharepoint-server-2016.md#BKMK_InstallMIM) describes how to install MIM, and [Use a sample MIM solution in SharePoint Server 2016](html/use-a-sample-mim-solution-in-sharepoint-server-2016.md) shows how to use a sample MIM solution.
# See also

#### 

 [Deployment considerations for implementing Microsoft Identity Manager with SharePoint Server 2016](html/deployment-considerations-for-implementing-microsoft-identity-manager-with-share.md)
  
    
    

  
    
    

