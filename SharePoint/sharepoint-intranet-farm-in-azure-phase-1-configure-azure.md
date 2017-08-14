---
title: SharePoint Intranet Farm in Azure Phase 1 Configure Azure
ms.prod: SHAREPOINT
ms.assetid: f957e1ce-0a39-490c-b533-4ddab4f5bb7a
---


# SharePoint Intranet Farm in Azure Phase 1: Configure Azure
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-06* **Summary:** Configure the Microsoft Azure infrastructure to host a high-availability SharePoint Server 2016 farm.In this phase of deploying an intranet-only SharePoint Server 2016 farm in Azure, you build out the Azure infrastructure. You must complete this phase before moving on to  [SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers](html/sharepoint-intranet-farm-in-azure-phase-2-configure-domain-controllers.md). See  [Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](html/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in.md) for all of the phases.Azure must be provisioned with these basic components for networking and storage:
- Resource groups
    
  
- A cross-premises virtual network with subnets for hosting the Azure virtual machines
    
  
- Network security groups for performing subnet isolation
    
  
- Azure storage accounts to store VHD disk images and extra data disks for each virtual machine
    
  
- Availability sets
    
  
- Load balancer instances for the SharePoint front end and distributed cache and the SQL Server virtual machines
    
  

## Configure Azure components

Before you begin configuring Azure components, fill in the following tables. To assist you in the procedures for configuring Azure, print this section and write down the needed information or copy this section to a document and fill it in. For the settings of the Azure virtual network (VNet), fill in Table V.
### 

ItemConfiguration settingDescriptionValue1.  <br/> VNet name  <br/> A name to assign to the Azure Virtual Network (example SPFarmNet).  <br/> _______________________________  <br/> 2.  <br/> VNet location  <br/> The Azure datacenter that will contain the virtual network.  <br/> _______________________________  <br/> 3.  <br/> VPN device IP address  <br/> The public IPv4 address of your VPN device's interface on the Internet.  <br/> _______________________________  <br/> 4.  <br/> VNet address space  <br/> The address space for the virtual network. Work with your IT department to determine this address space.  <br/> _______________________________  <br/> 5.  <br/> IPsec shared key  <br/> A 32-character random, alphanumeric string that will be used to authenticate both sides of the site-to-site VPN connection. Work with your IT or security department to determine this key value. Alternately, see  [Create a random string for an IPsec preshared key](http://social.technet.microsoft.com/wiki/contents/articles/32330.create-a-random-string-for-an-ipsec-preshared-key.aspx).  <br/> _______________________________  <br/> **Table V: Cross-premises virtual network configuration**Next, fill in Table S for the subnets of this solution. All address spaces should be in Classless Interdomain Routing (CIDR) format, also known as network prefix format. An example is 10.24.64.0/20.For the first four subnets, specify a name and a single IP address space based on the virtual network address space. For the gateway subnet, determine the 27-bit address space (with a /27 prefix length) for the Azure gateway subnet through the following process:
1. Set the variable bits in the address space of the VNet to 1, up to the bits being used by the gateway subnet, then set the remaining bits to 0.
    
  
2. Convert the resulting bits to decimal and express it as an address space with the prefix length set to the size of the gateway subnet.
    
  
See  [Address space calculator for Azure gateway subnets](https://gallery.technet.microsoft.com/scriptcenter/Address-prefix-calculator-a94b6eed) for a PowerShell command block and C# console application that performs this calculation for you.Work with your IT department to determine these address spaces from the virtual network address space.
### 

ItemSubnet nameSubnet address spacePurpose1.  <br/> _______________________________  <br/> _______________________________  <br/> The subnet used by the Windows Server Active Directory (AD) VMs.  <br/> 2.  <br/> _______________________________  <br/> _______________________________  <br/> The subnet used by the VMs in the SQL Server cluster.  <br/> 3.  <br/> _______________________________  <br/> _______________________________  <br/> The subnet used by the SharePoint app and search servers.  <br/> 4.  <br/> _______________________________  <br/> _______________________________  <br/> The subnet used by the front end and distributed cache servers.  <br/> 5.  <br/> GatewaySubnet  <br/> _______________________________  <br/> The subnet used by the Azure gateway virtual machines.  <br/> **Table S: Subnets in the virtual network**Next, fill in Table I for the static IP addresses assigned to virtual machines and load balancer instances.
### 

ItemPurposeIP address on the subnetValue1.  <br/> Static IP address of the first domain controller  <br/> The fourth possible IP address for the address space of the subnet defined in Item 1 of Table S.  <br/> _______________________________  <br/> 2.  <br/> Static IP address of the second domain controller  <br/> The fifth possible IP address for the address space of the subnet defined in Item 1 of Table S.  <br/> _______________________________  <br/> 3.  <br/> Static IP address of the internal load balancer for the front end and distributed cache SharePoint servers  <br/> The sixth possible IP address for the address space of the subnet defined in Item 4 of Table S.  <br/> _______________________________  <br/> 4.  <br/> Static IP address of the internal load balancer for the listener address of the SQL server cluster  <br/> The fourth possible IP address for the address space of the subnet defined in Item 2 of Table S.  <br/> _______________________________  <br/> 5.  <br/> Static IP address of the first SQL server  <br/> The fifth possible IP address for the address space of the subnet defined in Item 2 of Table S.  <br/> _______________________________  <br/> 6.  <br/> Static IP address of the second SQL server  <br/> The sixth possible IP address for the address space of the subnet defined in Item 2 of Table S.  <br/> _______________________________  <br/> 7.  <br/> Static IP address of the minority node server  <br/> The seventh possible IP address for the address space of the subnet defined in Item 2 of Table S.  <br/> _______________________________  <br/> 8.  <br/> Static IP address of the first application and search SharePoint server  <br/> The fourth possible IP address for the address space of the subnet defined in Item 3 of Table S.  <br/> _______________________________  <br/> 9.  <br/> Static IP address of the second application and search SharePoint server  <br/> The fifth possible IP address for the address space of the subnet defined in Item 3 of Table S.  <br/> _______________________________  <br/> 10.  <br/> Static IP address of the first front end and distributed cache SharePoint server  <br/> The fourth possible IP address for the address space of the subnet defined in Item 4 of Table S.  <br/> _______________________________  <br/> 11.  <br/> Static IP address of the second front end and distributed cache SharePoint server  <br/> The fifth possible IP address for the address space of the subnet defined in Item 4 of Table S.  <br/> _______________________________  <br/> **Table I: Static IP addresses in the virtual network**For the two Domain Name System (DNS) servers in your on-premises network that you want to use when initially setting up the domain controllers in your virtual network, fill in Table D. Note that two blank entries are listed, but you can add more. Work with your IT department to determine this list.
### 

ItemDNS server friendly nameDNS server IP address1.  <br/> _______________________________  <br/> _______________________________  <br/> 2.  <br/> _______________________________  <br/> _______________________________  <br/> **Table D: On-premises DNS servers**To route packets from the cross-premises network to your organization network across the site-to-site VPN connection, you must configure the virtual network with a local network that contains a list of the address spaces (in CIDR notation) for all of the reachable locations on your organization's on-premises network. The list of address spaces that define your local network must be unique and must not overlap with the address space used for other virtual networks or other local networks.For the set of local network address spaces, fill in Table L. Note that three blank entries are listed but you will typically need more. Work with your IT department to determine this list of address spaces.
### 

ItemLocal network address space1.  <br/> _______________________________  <br/> 2.  <br/> _______________________________  <br/> 3.  <br/> _______________________________  <br/> **Table L: Address prefixes for the local network**Now let's begin building the Azure infrastructure to host your SharePoint farm.
> [!NOTE:]

  
    
    

First, start an Azure PowerShell prompt and login to your account.


```

Login-AzureRMAccount
```


> [!TIP:]

  
    
    

Get your subscription name using the following command.


```

Get-AzureRMSubscription | Sort SubscriptionName | Select SubscriptionName
```

Set your Azure subscription. Replace everything within the quotes, including the < and > characters, with the correct name.


```
$subscr="<subscription name>"
Get-AzureRmSubscription -SubscriptionName $subscr | Select-AzureRmSubscription
```

Next, create the new resource groups for your intranet SharePoint farm. To determine a unique set of resource group names, use this command to list your existing resource groups.


```

Get-AzureRMResourceGroup | Sort ResourceGroupName | Select ResourceGroupName
```

Fill in the following table for the set of unique resource group names.
### 

ItemResource group namePurpose1.  <br/> _______________________________  <br/> Domain controllers  <br/> 2.  <br/> _______________________________  <br/> Database cluster servers  <br/> 3.  <br/> _______________________________  <br/> App and search servers  <br/> 4.  <br/> _______________________________  <br/> Front end and distributed cache servers  <br/> 5.  <br/> _______________________________  <br/> Infrastructure elements  <br/> **Table R: Resource groups**Create your new resource groups with these commands.


```
$locName="<an Azure location, such as West US>"
$rgName="<Table R - Item 1 - Name column>"
New-AzureRMResourceGroup -Name $rgName -Location $locName
$rgName="<Table R - Item 2 - Name column>"
New-AzureRMResourceGroup -Name $rgName -Location $locName
$rgName="<Table R - Item 3 - Name column>"
New-AzureRMResourceGroup -Name $rgName -Location $locName
$rgName="<Table R - Item 4 - Name column>"
New-AzureRMResourceGroup -Name $rgName -Location $locName
$rgName="<Table R - Item 5 - Name column>"
New-AzureRMResourceGroup -Name $rgName -Location $locName

```

Next, create the new storage accounts for your intranet SharePoint farm. To determine a unique set of storage account names, use this command to list your existing storage accounts.


```

Get-AzureRMStorageAccount | Sort StorageAccountName | Select StorageAccountName
```

Fill in the following table for the set of storage account names. 
### 

ItemNamePurpose1.  <br/> _______________________________  <br/> First domain controller  <br/> 2.  <br/> _______________________________  <br/> Second domain controller  <br/> 3.  <br/> _______________________________  <br/> First SQL Server computer  <br/> 4.  <br/> _______________________________  <br/> Second SQL Server computer  <br/> 5.  <br/> _______________________________  <br/> Cluster majority node server  <br/> 6.  <br/> _______________________________  <br/> First application and search server  <br/> 7.  <br/> _______________________________  <br/> Second application and search server  <br/> 8.  <br/> _______________________________  <br/> First front end and distributed cache server  <br/> 9.  <br/> _______________________________  <br/> Second front end and distributed cache server  <br/> **Table ST: Storage accounts**You must pick a globally unique name for each storage account that contains  * **only lowercase letters and numbers*** . To test whether a proposed name is globally unique, use the following command:


```
Get-AzureRmStorageAccountNameAvailability "<proposed name>"
```

Create your new storage accounts with these commands.


```
$locName="<an Azure location, such as West US>"

# Storage accounts for the domain controllers
$rgName="<Table R - Item 1 - Resource group name column>"
$saName="<Table ST - Item 1 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Standard_LRS -Location $locName
$saName="<Table ST - Item 2 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Standard_LRS -Location $locName

# Storage accounts for the SQL cluster servers
$rgName="<Table R - Item 2 - Resource group name column>"
$saName="<Table ST - Item 3 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName
$saName="<Table ST - Item 4 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName
$saName="<Table ST - Item 5 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Standard_LRS -Location $locName

# Storage accounts for the app and search SharePoint servers
$rgName="<Table R - Item 3 - Resource group name column>"
$saName="<Table ST - Item 6 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName
$saName="<Table ST - Item 7 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName

# Storage accounts for the front end and distributed cache SharePoint servers
$rgName="<Table R - Item 4 - Resource group name column>"
$saName="<Table ST - Item 8 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName
$saName="<Table ST - Item 9 - Storage account name column>"
New-AzureRMStorageAccount -Name $saName -ResourceGroupName $rgName -Type Premium_LRS -Location $locName

```

Next, you create the Azure virtual network and its subnets that will host your intranet SharePoint farm.


```

$rgName="<Table R - Item 5 - Resource group name column>"
$locName="<Azure location>"
$locShortName="<the location of the resource group in lowercase with spaces removed, example: westus>"
$vnetName="<Table V - Item 1 - Value column>"
$vnetAddrPrefix="<Table V - Item 4 - Value column>"
$dnsServers=@( "<Table D - Item 1 - DNS server IP address column>", "<Table D - Item 2 - DNS server IP address column>" )

# Create the subnets
$spSubnet1Name="<Table S - Item 1 - Subnet name column>"
$spSubnet1Prefix="<Table S - Item 1 - Subnet address space column>"
$spSubnet1=New-AzureRMVirtualNetworkSubnetConfig -Name $spSubnet1Name -AddressPrefix $spSubnet1Prefix
$spSubnet2Name="<Table S - Item 2 - Subnet name column>"
$spSubnet2Prefix="<Table S - Item 2 - Subnet address space column>"
$spSubnet2=New-AzureRMVirtualNetworkSubnetConfig -Name $spSubnet2Name -AddressPrefix $spSubnet2Prefix
$spSubnet3Name="<Table S - Item 3 - Subnet name column>"
$spSubnet3Prefix="<Table S - Item 3 - Subnet address space column>"
$spSubnet3=New-AzureRMVirtualNetworkSubnetConfig -Name $spSubnet3Name -AddressPrefix $spSubnet3Prefix
$spSubnet4Name="<Table S - Item 4 - Subnet name column>"
$spSubnet4Prefix="<Table S - Item 4 - Subnet address space column>"
$spSubnet4=New-AzureRMVirtualNetworkSubnetConfig -Name $spSubnet4Name -AddressPrefix $spSubnet4Prefix
$gwSubnet5Prefix="<Table S - Item 5 - Subnet address space column>"
$gwSubnet=New-AzureRMVirtualNetworkSubnetConfig -Name "GatewaySubnet" -AddressPrefix $gwSubnet5Prefix

# Create the virtual network
New-AzureRMVirtualNetwork -Name $vnetName -ResourceGroupName $rgName -Location $locName -AddressPrefix $vnetAddrPrefix -Subnet $gwSubnet,$spSubnet1,$spSubnet2,$spSubnet3,$spSubnet4 -DNSServer $dnsServers

```

Next, you create network security groups for each subnet that contains virtual machines. To perform subnet isolation, you can add rules for the specific types of traffic allowed or denied to the network security group of a subnet.


```

# Create network security groups
$vnet=Get-AzureRMVirtualNetwork -ResourceGroupName $rgName -Name $vnetName

New-AzureRMNetworkSecurityGroup -Name $spSubnet1Name -ResourceGroupName $rgName -Location $locShortName
$nsg=Get-AzureRMNetworkSecurityGroup -Name $spSubnet1Name -ResourceGroupName $rgName
Set-AzureRMVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $spSubnet1Name -AddressPrefix $spSubnet1Prefix -NetworkSecurityGroup $nsg

New-AzureRMNetworkSecurityGroup -Name $spSubnet2Name -ResourceGroupName $rgName -Location $locShortName
$nsg=Get-AzureRMNetworkSecurityGroup -Name $spSubnet2Name -ResourceGroupName $rgName
Set-AzureRMVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $spSubnet2Name -AddressPrefix $spSubnet2Prefix -NetworkSecurityGroup $nsg

New-AzureRMNetworkSecurityGroup -Name $spSubnet3Name -ResourceGroupName $rgName -Location $locShortName
$nsg=Get-AzureRMNetworkSecurityGroup -Name $spSubnet3Name -ResourceGroupName $rgName
Set-AzureRMVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $spSubnet3Name -AddressPrefix $spSubnet3Prefix -NetworkSecurityGroup $nsg

New-AzureRMNetworkSecurityGroup -Name $spSubnet4Name -ResourceGroupName $rgName -Location $locShortName
$nsg=Get-AzureRMNetworkSecurityGroup -Name $spSubnet4Name -ResourceGroupName $rgName
Set-AzureRMVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $spSubnet4Name -AddressPrefix $spSubnet4Prefix -NetworkSecurityGroup $nsg

```

Next, use these commands to create the gateways for the site-to-site VPN connection.


```

$rgName="<Table R - Item 5 - Resource group name column>"
$locName="<Azure location>"
$vnetName="<Table V - Item 1 - Value column>"
$vnet=Get-AzureRMVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name "GatewaySubnet"

# Attach a virtual network gateway to a public IP address and the gateway subnet
$publicGatewayVipName="SPPublicIPAddress"
$vnetGatewayIpConfigName="SPPublicIPConfig"
New-AzureRMPublicIpAddress -Name $vnetGatewayIpConfigName -ResourceGroupName $rgName -Location $locName -AllocationMethod Dynamic
$publicGatewayVip=Get-AzureRMPublicIpAddress -Name $vnetGatewayIpConfigName -ResourceGroupName $rgName
$vnetGatewayIpConfig=New-AzureRMVirtualNetworkGatewayIpConfig -Name $vnetGatewayIpConfigName -PublicIpAddressId $publicGatewayVip.Id -Subnet $subnet

# Create the Azure gateway
$vnetGatewayName="SPAzureGateway"
$vnetGateway=New-AzureRMVirtualNetworkGateway -Name $vnetGatewayName -ResourceGroupName $rgName -Location $locName -GatewayType Vpn -VpnType RouteBased -IpConfigurations $vnetGatewayIpConfig

# Create the gateway for the local network
$localGatewayName="SPLocalNetGateway"
$localGatewayIP="<Table V - Item 3 - Value column>"
$localNetworkPrefix=@( <comma-separated, double-quote enclosed list of the local network address prefixes from Table L, example: "10.1.0.0/24", "10.2.0.0/24"> )
$localGateway=New-AzureRMLocalNetworkGateway -Name $localGatewayName -ResourceGroupName $rgName -Location $locName -GatewayIpAddress $localGatewayIP -AddressPrefix $localNetworkPrefix

# Define the Azure virtual network VPN connection
$vnetConnectionName="SPS2SConnection"
$vnetConnectionKey="<Table V - Item 5 - Value column>"
$vnetConnection=New-AzureRMVirtualNetworkGatewayConnection -Name $vnetConnectionName -ResourceGroupName $rgName -Location $locName -ConnectionType IPsec -SharedKey $vnetConnectionKey -VirtualNetworkGateway1 $vnetGateway -LocalNetworkGateway2 $localGateway

```

Next, record the public IPv4 address of the Azure VPN gateway for your virtual network from the display of this command:


```

Get-AzureRMPublicIpAddress -Name $publicGatewayVipName -ResourceGroupName $rgName
```

Next, configure your on-premises VPN device to connect to the Azure VPN gateway. For more information, see  [Configure your VPN device](https://docs.microsoft.com/azure/vpn-gateway/vpn-gateway-about-vpn-devices).To configure your on-premises VPN device, you will need the following:
- The public IPv4 address of the Azure VPN gateway.
    
  
- The IPsec pre-shared key for the site-to-site VPN connection (Table V – Item 5 – Value column).
    
  
Next, ensure that the address space of the virtual network is reachable from your on-premises network. This is usually done by adding a route corresponding to the virtual network address space to your VPN device and then advertising that route to the rest of the routing infrastructure of your organization network. Work with your IT department to determine how to do this.Next, define the names of four availability sets. Fill out Table A. 
### 

ItemPurposeAvailability set name1.  <br/> Domain controllers  <br/> _______________________________  <br/> 2.  <br/> SQL servers  <br/> _______________________________  <br/> 3.  <br/> Application and search servers  <br/> _______________________________  <br/> 4.  <br/> Front-end and distributed cache servers  <br/> _______________________________  <br/> **Table A: Availability sets**You will need these names when you create the virtual machines in phases 2, 3, and 4.Create your availability sets with these Azure PowerShell commands.


```
$locName="<the Azure location for your new resource group>"
$rgName="<Table R - Item 1 - Resource group name column>"
$avName="<Table A - Item 1 - Availability set name column>"
New-AzureRMAvailabilitySet -Name $avName -ResourceGroupName $rgName -Location $locName
$rgName="<Table R - Item 2 - Resource group name column>"
$avName="<Table A - Item 2 - Availability set name column>"
New-AzureRMAvailabilitySet -Name $avName -ResourceGroupName $rgName -Location $locName
$rgName="<Table R - Item 3 - Resource group name column>"
$avName="<Table A - Item 3 - Availability set name column>"
New-AzureRMAvailabilitySet -Name $avName -ResourceGroupName $rgName -Location $locName
$rgName="<Table R - Item 4 - Resource group name column>"
$avName="<Table A - Item 4 - Availability set name column>"
New-AzureRMAvailabilitySet -Name $avName -ResourceGroupName $rgName -Location $locName

```

This is the configuration resulting from the successful completion of this phase. **Phase 1: The Azure infrastructure for your high-availability SharePoint Server 2016 farm**
  
    
    
![Phase 1 of the SharePoint Server 2016 highly-available farm in Azure with the Azure infrastructure](images/)
  
    
    

  
    
    

  
    
    

## Next step

Use  [SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers](html/sharepoint-intranet-farm-in-azure-phase-2-configure-domain-controllers.md) to continue with the configuration of this workload.
# See also

#### 

 [Install and configure SharePoint Server 2016](html/install-and-configure-sharepoint-server-2016.md)
  
    
    

#### 

 [Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](html/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in.md)
  
    
    
 [SharePoint Server 2016 in Microsoft Azure](html/sharepoint-server-2016-in-microsoft-azure.md)
  
    
    
 [Designing a SharePoint Server 2016 farm in Azure](html/designing-a-sharepoint-server-2016-farm-in-azure.md)
  
    
    

  
    
    

