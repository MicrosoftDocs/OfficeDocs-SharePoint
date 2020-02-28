---
title: "Designing a SharePoint Server 2016 farm in Azure"
ms.reviewer: 
ms.author: josephd
author: JoeDavies-MSFT
manager: laurawi
ms.date: 10/19/2017
audience: ITPro
f1.keywords:
- CSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.custom: Ent_Solutions
ms.assetid: f27522ca-6f78-4b97-b169-77066e965727
description: "Step through a process to design Microsoft Azure infrastructure services to host SharePoint Server farms."
---

# Designing a SharePoint Server 2016 farm in Azure

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
 
This article provides an overview of the support for SharePoint Server 2016 farms in Azure infrastructure services and a step-by-step process and recommendations and best practices for designing the Azure environment, including network, storage, and compute resources.
  
## SharePoint Server 2016 farms in Azure infrastructure services

Running SharePoint Server 2016 farms in any Infrastructure as a Service (IaaS) environment can take advantage of the following:
  
- Capacity on demand and the ability to scale virtual machines up (elasticity)
    
- Partial outsourcing
    
- Additional locations with minimal investment
    
- Cost savings
    
Here are the scenarios in which SharePoint farms should be run from an IaaS environment:
  
- Dev/test, pilot, or proof-of-concept farm
    
- Hybrid infrastructure
    
- Disaster recovery
    
- Production farm
    
### Supportability of SharePoint Server 2016 in Azure

Microsoft supports the following SharePoint Server 2016 deployment scenarios on Azure IaaS virtual machines (VMs):
  
- Non-production farms, such as those used for dev/test environments or for proof-of-concept
    
- As a disaster recovery target using log shipping, SQL Server AlwaysOn Availability Groups, or Azure Site Recovery
    
- Production farms, using Azure premium storage for servers running the search role
    
Production farms running SharePoint 2013 are also supported. SharePoint 2010 is no longer in mainstream support, however it can be installed on Azure VMs for testing and validation of migration scenarios.
  
As with other Microsoft workloads, licensing is handled with Licensing Mobility through Software Assurance. For more information, see [Licensing Microsoft server products for use in virtual environments](https://download.microsoft.com/download/3/d/4/3d42bdc2-6725-4b29-b75a-a5b04179958b/microsoftservervirtualization_licensemobility_vlbrief.pdf).
  
## The design process for SharePoint Server 2016 farms in Azure

The Azure infrastructure services environment is different than on-premises data centers and requires additional planning. The following design process steps you through determining the following elements of Azure infrastructure:
  
1. Resource groups
    
2. Connectivity
    
3. Storage
    
4. Identity
    
5. Security
    
6. Virtual machines
    
Each step includes best practices and recommendations specific to the requirements of SharePoint Server 2016 farms.
  
At the end of the design process, you will have determined the set of components in Azure infrastructure services that is ready for your SharePoint Server 2016 farm. 
  
> [!TIP]
> This process is based on [Design Azure infrastructure services to host a multi-tier LOB application](https://blogs.technet.microsoft.com/solutions_advisory_board/2016/12/05/design-azure-infrastructure-services-to-host-a-multi-tier-lob-application/). 
  
### Step 1: Resource groups

Resource groups are containers for multiple Azure elements that can be managed together. For example, you can create access control lists that allow only specific user accounts to modify the set of elements in a resource group.
  
You can place all of the resources for your SharePoint Server 2016 farm in the same resource group, but this is highly discouraged for production deployments. Instead, the recommendation is to use different resource groups for:
  
- Infrastructure and networking components
    
    For example, a resource group called Networking_RG that contains the virtual network (VNet), network security groups, and load balancers.
    
- The separate roles of the SharePoint farm
    
    For example, use separate resource groups for the front-end, search, application, distributed cache, data, and combined roles of a typical SharePoint Server 2016 farm. In each separate resource group, place the availability sets, network interfaces, and virtual machines of that role.
    
For your resource groups, fill in the following table before creating them, using as many rows as needed.
  
|**Resource group name**|**Azure location (region)**|
|:-----|:-----|
|||
|||
   
### Step 2: Connectivity

Connectivity includes:
  
- Access to the servers running in your SharePoint Server 2016 farm, both for administration and for the resources of the farm, from your intranet and the Internet.
    
- Access for the servers of the farm to each other, to the intranet, and to the Internet.
    
The elements of connectivity include virtual networks (VNets), the subnets within VNets, Domain Name System (DNS) for name registration and resolution, traffic distribution, and addressing for virtual machines.
  
#### VNets

The required container for virtual machines in Azure infrastructure services is the Azure VNet. There are two types of VNets:
  
- Cloud-only
    
    Has no connection to an on-premises network. Use this type of VNet when you are deploying an Internet-facing SharePoint farm that uses a standalone Windows Server Active Directory (AD) forest.
    
- Cross-premises
    
    Has a connection to an on-premises network and must be assigned a unique address space from your intranet. Use this type of VNet when you are deploying an intranet-based SharePoint farm that uses an on-premises Windows Server AD forest.
    
Although it is possible to place the VMs of a server role of a SharePoint farm in different VNets, this is highly discouraged because network traffic between VMs would have to travel across a VNet-to-VNet or VNet peering connection. The recommendation is to place all of the servers of a farm in a single VNet.
  
When you create the VNet, you must assign an address space to it, which can consist of one or multiple Classless Inter-Domain Routing (CIDR) blocks (also known as network prefixes). This is similar to assigning an address space to a new datacenter that will contain multiple subnets and IT workloads. The address space you choose depends on the type of VNet:
  
- Cloud-only
    
    Can have any address space from the private IPv4 address space (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), if it does not overlap with the address spaces of other interconnected VNets.
    
- Cross-premises
    
    Must be a unique, non-overlapping address space from your intranet address space, which can include public and private address spaces. 
    
For your VNet, fill in the following table.
  
|**VNet name**|**VNet type**|**Resource group name**|**Address space**|
|:-----|:-----|:-----|:-----|
|||||
   
 Place the VNet in the resource group for infrastructure or networking components. 
  
Note that you can use an existing VNet that hosts IT workloads on virtual machines in Azure or you can create a new VNet.
  
#### Subnets

Just like the subnets in your datacenter, subnets of an Azure VNet are logical divisions of the IPv4 address space to group and separate network nodes and their traffic. Azure supports three types of subnets:
  
- VM-hosting (required)
    
    Hosts the VMs of an IT workload. An example is all of the servers running the distributed cache service of a SharePoint Server 2016 farm.
    
- Gateway
    
    Hosts the Azure gateways for a cross-premises or VNet-to-VNet VPN connection. This subnet must be named "GatewaySubnet".
    
- Management (recommended)
    
    Hosts two or more VMs that provide remote desktop connections to the servers in the VNet and support network management functions.
    
Just like your on-premises datacenters, the recommendation in Azure is to use a separate VM-hosting subnet for each set or VMs providing the same server role for your farm. With separate subnets, you can use Azure network security groups to define the allowed inbound and outbound traffic and perform subnet isolation.
  
The address space for each subnet must be a portion of the VNet address space expressed as a single CIDR block, also known as a network prefix. Choose enough address space to accommodate the projected set of servers running that common server role.
  
|**Number of servers**|**Length of the network prefix**|
|:-----|:-----|
|1-3  <br/> |/29  <br/> |
|4-11  <br/> |/28  <br/> |
|12-27  <br/> |/27  <br/> |
|18-59  <br/> |/26  <br/> |
   
The recommendation for the GatewaySubnet is to use a /27 network prefix length and assign it from the last part of the VNet address space. For more information, see [Calculating the gateway subnet address space for Azure virtual networks](https://blogs.technet.microsoft.com/solutions_advisory_board/2016/12/01/calculating-the-gateway-subnet-address-space-for-azure-virtual-networks/).
  
For the subnets of your VNet, fill in the following table before creating them, using as many rows as needed.
  
|**Subnet name**|**Address space**|
|:-----|:-----|
|GatewaySubnet (if needed) ||
|||
|||
|||
   
#### DNS

All VMs in an Azure VNet by default are assigned a set of DNS servers to perform name registration and resolution. You can override this by assigning DNS servers to individual VM network interfaces.
  
For a SharePoint Server 2016 farm in Azure that uses [Azure Active Directory (AD) Domain Services](/azure/active-directory-domain-services/active-directory-ds-overview), assign the IP addresses of the service as the DNS servers.
  
For a SharePoint Server 2016 farm in Azure that contains a set of Windows Server AD domain controllers that are also acting as DNS servers, assign the IP addresses of the domain controllers as the DNS servers. For a cross-premises VNet, you need two sets of DNS servers:
  
- A set of DNS servers on your on-premises network that your domain controller VMs use when they join the domain and are promoted to domain controllers.
    
- After the VMs have become DNS servers, you reset the DNS servers to the IP addresses of the domain controllers.
    
For the DNS server IP addresses to assign to your VNet, fill in the following table using as many rows as needed.
  
|**DNS server IP addresses**|
|:-----|
||
||
   
#### Traffic distribution

Typical production SharePoint farms use load balancers to distribute traffic among the servers of a common role. Azure infrastructure services include a built-in load balancer that can be used in the following ways:
  
- **Internet-facing:** Used in conjunction with a public IP address to distribute incoming Internet traffic to the VM members of a load balanced set. 
    
- **Internal:** Used in conjunction with an IP address of a subnet in the VNet to distribute incoming Internet traffic to the VM members of a load balanced set. 
    
Here are the recommendations for using Azure load balancers in your SharePoint Server 2016 farm in Azure:
  
- Use the Azure load balancer or a load balancer network appliance for your front-end servers. If the SharePoint farm is designed to be accessible from the Internet, use an Internet-facing load balancer.
    
- Use an internal Azure load balancer or a load balancer network appliance for the set of servers running applications and for the SQL server cluster (using the listener IP address).
    
- Create the Azure load balancers or load balancer network appliances in the infrastructure or networking resource group.
    
- Increase idle connection timeout to handle long duration connections from SharePoint clients with the [Set-AzureLoadBalancedEndpoint -IdleTimeoutInMinutes 15](https://msdn.microsoft.com/library/azure/dn495126.aspx) Azure PowerShell command. 
    
- The VM health probe can either be an HTTP get message or an ICMP Echo Request (ping) message, unless the load balancing network appliance is operating at layer 4, in which case an HTTP get message should be used.
    
For the Azure load balancers, fill in the following table before creating them, using as many rows as needed.
  
|**Load balancer name**|**Purpose**|**Type (Internet-facing or internal)**|
|:-----|:-----|:-----|
||||
||||
   
#### Static addresses

You can assign static IP addresses to VM network interfaces from the available subnet address space. If you are using an internal Azure load balancer to distribute traffic among the servers of a common role, assign the load balancer a static IP address from the subnet containing the members of the load balanced set.
  
For a SharePoint Server 2016 farm in Azure, Microsoft recommends that you assign a static IP address for each server running SQL Server or SharePoint Server 2016.
  
For static IP addresses, fill in the following table, using as many rows as needed.
  
|**VM or load balancer name**|**Static IP address**|
|:-----|:-----|
|||
|||
|||
   
#### Public IP addresses

A public IP address allows access to a load balancer or VM from the Internet. To reduce the surface area for malicious attacks, Microsoft recommends that you use public IP addresses only for the following:
  
- For jumpbox VMs in a cloud-only network.
    
    A jumpbox VM is a VM from which you initiate remote desktop connections to remotely manage the other VMs in the VNet. You do not need public IP addresses for each VM.
    
- For an Internet-facing load balancer for externally-facing farms.
    
    The public IP address provides access to the servers in the front-end role of the farm.
    
For public IP addresses, fill in the following table, using as many rows as needed.
  
|**VM or load balancer name**|
|:-----|
||
||
   
Azure assigns public IP addresses at the time they are requested for the VM or load balancer.
  
### Step 3: Storage

Storage resources for VMs in Azure, which include the disks that each VM uses, are [managed disks](https://azure.microsoft.com/services/managed-disks/).
  
Azure supports [standard and premium types of storage](/azure/storage/common/storage-introduction). To be in a supported configuration, you must use premium storage for the servers running SharePoint Server 2016 that host the search role. Microsoft recommends that you use premium storage for all VMs running SQL Server or SharePoint Server 2016. Other VMs in the farm, such as domain controllers and the VMs on the management subnet, can use standard storage.
  
### Step 4: Identity

SharePoint Server 2016 requires Windows Server AD domain membership. Therefore, a SharePoint Server 2016 farm in Azure must have access to an Windows Server AD domain either with VMs acting as domain controllers or with [Azure Active Directory (AD) Domain Services](/azure/active-directory-domain-services/active-directory-ds-overview).
  
When using VMs acting as domain controllers:
  
- For an Internet-only farm in a cloud-only VNet, create a standalone Windows Server AD forest with at least two VMs for availability.
    
- For an intranet farm in a cross-premises VNet, you can use on-premises domain controllers. However, Microsoft recommends using at least two replica domain controllers for the on-premises Windows Server AD forest in the VNet containing the SharePoint farm.
    
### Step 5: Security

Use the following elements of Azure to provide security for the servers of the SharePoint farm:
  
- For cloud-only VNets, use a jumpbox VM for remote desktop connections and assign the only public IP address to the jumpbox VM. Jumpbox VMs are optional for cross-premises VNets because the VMs of the SharePoint farm can be reached directly from the intranet.
    
- Use subnet-based network security groups for subnet isolation. Network security groups and then the rules that define the traffic allowed into and out of the subnet. Place the network security groups in the resource group for infrastructure or networking components.
    
For the network security groups, fill in the following table before creating them, using as many rows as needed.
  
|**Network security group name**|**Subnet name**|**Rules**|
|:-----|:-----|:-----|
||||
||||
||||
   
### Step 6: Virtual machines

For the virtual machines of the SharePoint farm, do the following:
  
- Create an availability set for each set of VMs in a common role and place all of the VMs with the same server role in it.
    
- Create the availability set in the resource group for the server role.
    
- Use a minimum of two VMs for each server role.
    
- If you are using SQL Server AlwaysOn Availability Groups and plan to use only two SQL servers, you must also use minority node server for the cluster.
    
- Place the network interfaces and the VMs in the resource group for the server role.
    
Here are the minimum recommended VM sizes:
  
- Windows Server AD domain controllers: Standard_D2
    
- SQL Servers: Standard_DS4
    
- Minority node server: Standard_D2
    
- SharePoint servers: Standard_DS4
    
Addresses for network interfaces:
  
- Use static private IP addresses for all interfaces of VMs that are domain controllers or running SharePoint Server 2016 or SQL Server.
    
- Use a public IP address only for the jumpbox VM.
    
- Use a public IP address for the Internet-facing load balancer for the front-end servers if the farm is exposed to the Internet.
    
Each Azure VM includes an operating system disk. You can add extra disks when you create the VM or add them later. Use the following table for the minimum extra disks for the VMs in a SharePoint farm.
  
|**Type of server**|**Extra disks**|
|:-----|:-----|
|Windows Server AD domain controllers  <br/> |One 40 GB extra disk to store Windows Server AD information  <br/> |
|SQL Servers  <br/> |Three 1 TB extra disks for data, logs, and temporary data  <br/> |
|Application or search servers  <br/> |One 100 GB extra disk for logs, one 200 GB extra disk for the search index  <br/> |
|Front-end or distributed cache servers  <br/> |One 100 GB extra disk for logs  <br/> |
   
For the availability sets, fill in the following table before creating them, using as many rows as needed.
  
|**Availability set name**|**SharePoint farm role**|**Resource group**|
|:-----|:-----|:-----|
||||
||||
   
For the network interfaces of VMs, fill in the following table before creating them, using as many rows as needed.
  
|**Network interface name**|**Resource group**|**Subnet name**|**Static IP address**|**Load balancer instance (if needed)**|
|:-----|:-----|:-----|:-----|:-----|
||||||
||||||
   
For the VMs, fill in the following table before creating them, using as many rows as needed.
  
|**VM name**|**Purpose**|**Size**|**Availability set**|**Resource group**|**Network interface name**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|||||||
|||||||
   
## Next steps

If you are ready to create a proof-of-concept or dev/test configuration of an intranet SharePoint Server 2016 farm in Azure, see [Intranet SharePoint Server 2016 in Azure dev/test environment](intranet-sharepoint-server-2016-in-azure-dev-test-environment.md).
  
If you are ready to deploy a production-ready, high availability SharePoint Server 2016 farm in Azure, see [Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in.md).
  
## See also

#### Concepts

[SharePoint Server](../sharepoint-server.md)
  
[Install SharePoint Server](../install/install.md)
#### Other Resources

[SharePoint Server 2016 in Microsoft Azure](sharepoint-server-2016-in-microsoft-azure.md)

