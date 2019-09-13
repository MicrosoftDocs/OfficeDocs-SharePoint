---
title: "SharePoint Intranet Farm in Azure Phase 4 Configure SharePoint servers"
ms.reviewer: 
ms.author: josephd
author: JoeDavies-MSFT
manager: laurawi
ms.date: 04/06/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.custom: Ent_Solutions
ms.assetid: 8c733fb9-18b9-4770-b90b-364bd7ab30d1
description: "Configure the SharePoint servers to host a high-availability SharePoint Server 2016 farm in Microsoft Azure."
---

# SharePoint Intranet Farm in Azure Phase 4: Configure SharePoint servers

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
In this phase of deploying an intranet-only SharePoint Server 2016 farm in Azure infrastructure services, you create the SharePoint Server 2016 servers and configure their roles with the SharePoint Configuration Wizard.
  
You must complete this phase before moving on to [SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases](sharepoint-intranet-farm-in-azure-phase-5-create-the-availability-group-and-add.md). See [Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](/SharePoint/administration/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in) for all of the phases. 
  
## Create the SharePoint server virtual machines in Azure

There are four SharePoint server virtual machines:
  
- Two SharePoint server virtual machines are the front-end and distributed cache servers
    
- Two are for search and the administration and hosting of SharePoint applications
    
Two SharePoint servers for each set of server roles provide high availability.
  
Use the following blocks of PowerShell commands to create the components in Azure. Specify the values for the variables, removing the \< and \> characters. Note that these PowerShell command blocks use values from the following tables:
  
- Table R, for your resource groups
    
- Table V, for your virtual network settings
    
- Table S, for your subnet
    
- Table I, for your static IP addresses
    
- Table M, for your virtual machines
    
- Table A, for your availability sets
    
Recall that you defined Table M in [SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers](sharepoint-intranet-farm-in-azure-phase-2-configure-domain-controllers.md) and Tables R, V, S, I, and A in [SharePoint Intranet Farm in Azure Phase 1: Configure Azure](sharepoint-intranet-farm-in-azure-phase-1-configure-azure.md).
  
First, you configure internal load balancing so that Azure distributes the client traffic evenly among the two front end and distributed caching servers.
  
> [!NOTE]
> The following command sets use the latest version of Azure PowerShell. See [Get started with Azure PowerShell cmdlets](/powershell/azure/overview?view=azurermps-6.13.0). 
  
When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell Integrated Script Environment (ISE) on your local computer.
  
  
```
# Set up key variables
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 4 - Subnet name column>"
$privIP="<Table I - Item 3 - Value column>"
$rgName="<Table R - Item 5 - Resource group name column>"
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$frontendIP=New-AzLoadBalancerFrontendIpConfig -Name "SharePointWebServers-LBFE" -PrivateIPAddress $privIP -Subnet $subnet
$beAddressPool=New-AzLoadBalancerBackendAddressPoolConfig -Name "SharePointWebServers-LBBE"
# This example assumes unsecured (HTTP-based) web traffic to the front end servers.
$healthProbe=New-AzLoadBalancerProbeConfig -Name "WebServersProbe" -Protocol "TCP" -Port 80 -IntervalInSeconds 15 -ProbeCount 2
$lbrule=New-AzLoadBalancerRuleConfig -Name "WebTraffic" -FrontendIpConfiguration $frontendIP -BackendAddressPool $beAddressPool -Probe $healthProbe -Protocol "TCP" -FrontendPort 80 -BackendPort 80
# To use TCP 443, comment the previous line and un-comment the next line
# $lbrule=New-AzLoadBalancerRuleConfig -Name "WebTraffic" -FrontendIpConfiguration $frontendIP -BackendAddressPool $beAddressPool -Probe $healthProbe -Protocol "TCP" -FrontendPort 443 -BackendPort 443
New-AzLoadBalancer -ResourceGroupName $rgName -Name "SharePointWebServers" -Location $locName -LoadBalancingRule $lbrule -BackendAddressPool $beAddressPool -Probe $healthProbe -FrontendIpConfiguration $frontendIP

```

Next, add a DNS address record to your organization's internal DNS infrastructure that resolves the fully qualified domain name of the SharePoint farm (such as spfarm.corp.contoso.com) to the IP address assigned to the internal load balancer (the value of Table I - Item 3).
  
Use the following block of Azure PowerShell commands to create the virtual machines for the two SharePoint application and search servers. When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell ISE on your local computer.
  
```
# Set up variables common to both virtual machines
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 3 - Subnet name column>"
$avName="<Table A - Item 3 - Availability set name column>"
$rgNameTier="<Table R - Item 3 - Resource group name column>"
$rgNameInfra="<Table R - Item 5 - Resource group name column>"
$rgName=$rgNameInfra
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$rgName=$rgNameTier
$avSet=Get-AzAvailabilitySet -Name $avName -ResourceGroupName $rgName
# Create the first application/search server
$vmName="<Table M - Item 6 - Virtual machine name column>"
$vmSize="<Table M - Item 6 - Minimum size column>"
$staticIP="<Table I - Item 8 - Value column>"
$diskStorageType="<Table M - Item 6 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName +"-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $subnet -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$diskSize=200
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPSearchData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPSearchData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 2
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the first application server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
# Create the second application server
$vmName="<Table M - Item 7 - Virtual machine name column>"
$vmSize="<Table M - Item 7 - Minimum size column>"
$staticIP="<Table I - Item 9 - Value column>"
$diskStorageType="<Table M - Item 7 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName +"-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $subnet -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$diskSize=200
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPSearchData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPSearchData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 2
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the second application server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm

```

Use the following block of Azure PowerShell commands to create the virtual machines for the two SharePoint front end and distributed cache servers. When you have supplied all the correct values, run the resulting block at the Azure PowerShell command prompt or in the PowerShell ISE on your local computer.
  
```
# Set up variables common to both virtual machines
$locName="<Azure location of your SharePoint farm>"
$vnetName="<Table V - Item 1 - Value column>"
$subnetName="<Table S - Item 4 - Subnet name column>"
$avName="<Table A - Item 4 - Availability set name column>"
$rgNameTier="<Table R - Item 4 - Resource group name column>"
$rgNameInfra="<Table R - Item 5 - Resource group name column>"
$rgName=$rgNameInfra
$vnet=Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
$subnet=Get-AzVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name $subnetName
$backendSubnet=Get-AzVirtualNetworkSubnetConfig -Name $subnetName -VirtualNetwork $vnet
$webLB=Get-AzLoadBalancer -ResourceGroupName $rgName -Name "SharePointWebServers" 
$rgName=$rgNameTier
$avSet=Get-AzAvailabilitySet -Name $avName -ResourceGroupName $rgName
# Create the first front end  and distributed cache server virtual machine
$vmName="<Table M - Item 8 - Virtual machine name column>"
$vmSize="<Table M - Item 8 - Minimum size column>"
$staticIP="<Table I - Item 10 - Value column>"
$diskStorageType="<Table M - Item 8 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName + "-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $backendSubnet -LoadBalancerBackendAddressPool $webLB.BackendAddressPools[0] -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the first front end and distributed cache server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm
# Create the second front end and distributed cache server virtual machine
$vmName="<Table M - Item 9 - Virtual machine name column>"
$vmSize="<Table M - Item 9 - Minimum size column>"
$staticIP="<Table I - Item 11 - Value column>"
$diskStorageType="<Table M - Item 9 - Storage type column>"
$nic=New-AzNetworkInterface -Name ($vmName + "-NIC") -ResourceGroupName $rgName -Location $locName -Subnet $backendSubnet -LoadBalancerBackendAddressPool $webLB.BackendAddressPools[0] -PrivateIpAddress $staticIP
$vm=New-AzVMConfig -VMName $vmName -VMSize $vmSize -AvailabilitySetId $avset.Id
$vm=Set-AzVMOSDisk -VM $vm -Name ($vmName +"-OS") -DiskSizeInGB 128 -CreateOption FromImage -StorageAccountType $diskStorageType
$diskSize=100
$diskConfig=New-AzDiskConfig -AccountType $diskStorageType -Location $locName -CreateOption Empty -DiskSizeGB $diskSize
$dataDisk1=New-AzDisk -DiskName ($vmName + "-SPLogData") -Disk $diskConfig -ResourceGroupName $rgName
$vm=Add-AzVMDataDisk -VM $vm -Name ($vmName + "-SPLogData") -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
$cred=Get-Credential -Message "Type the name and password of the local administrator account for the second front end and distributed cache server." 
$vm=Set-AzVMOperatingSystem -VM $vm -Windows -ComputerName $vmName -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
$vm=Set-AzVMSourceImage -VM $vm -PublisherName MicrosoftSharePoint -Offer MicrosoftSharePointServer -Skus 2016 -Version "latest"
$vm=Add-AzVMNetworkInterface -VM $vm -Id $nic.Id
New-AzVM -ResourceGroupName $rgName -Location $locName -VM $vm

```

> [!NOTE]
> Because these virtual machines are for an intranet application, they are not assigned a public IP address or a DNS domain name label and exposed to the Internet. However, this also means that you cannot connect to them from the Azure portal. The Connect option is unavailable when you view the properties of the virtual machine. Use the Remote Desktop Connection accessory or another Remote Desktop tool to connect to the virtual machine using its private IP address or intranet DNS name. 
  
Do the following for each of the SharePoint servers:
  
1. Use the remote desktop client of your choice and create a remote desktop connection. Use its intranet DNS or computer name and the credentials of the local administrator account.
    
2. Join it to the appropriate Active Directory domain with these commands at the Windows PowerShell prompt on the connected virtual machine.
    
  ```
  $domName="<Active Directory domain name to join, such as corp.contoso.com>"
  Add-Computer -DomainName $domName
  Restart-Computer
  
  ```
   Note that you must supply domain account credentials after running the **Add-Computer** command. 
    
3. After the virtual machine restarts, create a Remote Desktop connection using the \<your domain>\sp_farm_db account credentials four times, once for each SharePoint server. You created these credentials in [SharePoint Intranet Farm in Azure Phase 2: Configure domain controllers](sharepoint-intranet-farm-in-azure-phase-2-configure-domain-controllers.md).
    
> [!NOTE]
> The SharePoint servers are created from the SharePoint Server 2016 Trial image. You need to convert the installation to use a Retail or Volume License key for either the Standard or Enterprise edition of SharePoint Server 2016. For more information, see [SharePoint 2016 Licensing](https://products.office.com/en-us/sharepoint/sharepoint-licensing-overview). 
  
Next, you need to add the extra data disks to each SharePoint server. 
  
For the first and second front end and distributed cache servers, run these commands at an administrator-level Windows PowerShell prompt to initialize the F: drive.
  
```
Get-Disk | Where PartitionStyle -eq "RAW" | Initialize-Disk -PartitionStyle MBR -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -NewFileSystemLabel "SPLogData"
md F:\Logs

```

For the first and second application and search servers, run these commands at an administrator-level Windows PowerShell prompt to initialize the F: and G: drives.
  
```
$newDisks=Get-Disk | Where Partitionstyle -eq "RAW"
ForEach ($d in $newDisks) {
$diskNum=$d.Number - 1
Get-Disk $d.Number | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -NewFileSystemLabel "DataDisk$diskNum"
}
md F:\Logs
md G:\Index

```

## Configure the SharePoint farm

Before the farm can be created, the build version of SharePoint must be updated to at least the November 2016 PU. This PU contains feature pack one that enables support for shared roles. Without this update, the servers can only be configured for single role use.
  
1. Download and install the latest [SharePoint Server 2016 update](/officeupdates/sharepoint-updates#BKMK_2016) (at least the November 2016 PU). 
    
    > [!NOTE]
    > Each monthy update contains two downloadable files. You should download and install both to ensure the server farm is correctly updated. Install the Server Patch first, then the MUI/Language patch. 
  
2. Once downloaded follow the instructions in [Install a software update for SharePoint Server 2016](/SharePoint/upgrade-and-update/install-a-software-update) to install the updates and upgrade the SharePoint server virtual machines. You need to complete this on all four servers. 
    
Use these steps to configure the first SharePoint application and search server (Table M - Item 6) as the first server in the farm:
  
1. Create a remote desktop connection to the first SharePoint application and search server.
    
2. From the Start screen, type **SharePoint**, and then click **SharePoint 2016 Products Configuration Wizard**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. A **SharePoint Products Configuration Wizard** dialog appears, warning that services (such as IIS) will be restarted or reset. Click **Yes**.
    
5. On the **Connect to a server farm** page, select **Create a new server farm**, and then click **Next**.
    
6. On the **Specify Configuration Database Settings** page: 
    
  - In **Database server**, type the name of your first SQL server virtual machine.
    
  - In **Username**, type \<your domain>**\sp_farm_db**.
    
  - In **Password**, type the sp_farm_db account password.
    
    Note the value in the **Database name** field (default is SharePoint_Config). You will need this database name for the additional servers in the farm. 
    
7. Click **Next**.
    
8. On the **Specify Farm Security Settings** page, type a passphrase twice. Record the passphrase and store it in a secure location for future reference. Click **Next**.
    
9. On the **Specify Server Role** page, in **Shared Roles,** click **Application with Search,** and then click **Nex**t.
    
10. On the **Configure SharePoint Central Administration Web Application** page, click **Next**.
    
11. The **Completing the SharePoint Products Configuration Wizard** page appears. Click **Next.**
    
12. The **Configuring SharePoint Products** page appears. Wait until the configuration process completes. 
    
13. On the **Configuration Successful** page, click **Finish**. The new administration website starts.
    
14. On the **Help Make SharePoint Better** page, click your choice to participate in the Customer Experience Improvement Program, and then click **OK**.
    
15. On the Welcome page, click **Start the Wizard.**
    
16. On the **Service Applications and Services** page, in **Service Account**, click **Use existing managed account**, and then click **Next**. It can take a few minutes to display the next page.
    
17. On the **Create Site Collection** page, type a site name in **Title**, and then click **OK**.
    
18. On the **This completes the Farm Configuration Wizard** page, click **Finish**. The SharePoint Central Administration web page displays.
    
19. Open a new tab in Internet Explorer, type **http://**\<name of the first SharePoint application server>/ in the Address bar, and then press Enter. You should see the default team site.
    
Perform the following procedure on the second SharePoint application and search server (Table M - Item 7):
  
1. Create a remote desktop connection to the second SharePoint application and search server.
    
2. From the Start screen, type **SharePoint**, and then click **SharePoint 2016 Products Configuration Wizard**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. A **SharePoint Products Configuration Wizard** dialog appears, warning that services (such as IIS) will be restarted or reset. Click **Yes**.
    
5. On the **Connect to a server farm** page, select **Connect to an existing server farm**, and then click **Next**.
    
6. On the **Specify Configuration Database Settings** page: 
    
  - In **Database server**, type the name of your first SQL server virtual machine, and then click **Retrieve Database Names**.
    
  - In **Database name**, select the name of the SharePoint database from step 6 of the previous procedure.
    
7. Click **Next**.
    
8. On the **Specify Farm Security Settings** page, in **Passphrase**, type the passphrase from step 8 of the previous procedure. Click **Next**.
    
9. On the **Specify Server Role** page, in **Shared Roles**, click **Application with Search**, and then click **Next**.
    
10. The **Completing the SharePoint Products Configuration Wizard** page appears. Click **Next**.
    
11. The **Configuring SharePoint Products** page appears. Wait until the configuration process completes. 
    
12. On the **Configuration Successful** page, click **Finish**.
    
13. On the **Initial Farm Configuration** page, click **Cancel**. You should see the **Central Administration** page. 
    
Perform the following procedure on the two front-end and distributed cache servers (Table M - Items 8 and 9):
  
1. Create a remote desktop connection to the SharePoint front-end and distributed cache server.
    
2. From the Start screen, type **SharePoint**, and then click **SharePoint 2016 Products Configuration Wizard**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. A **SharePoint Products Configuration Wizard** dialog appears, warning that services (such as IIS) will be restarted or reset. Click **Yes**.
    
5. On the **Connect to a server farm** page, select **Connect to an existing server farm**, and then click **Next**.
    
6. On the **Specify Configuration Database Settings** page: 
    
  - In **Database server**, type the name of your first SQL server virtual machine, and then click **Retrieve Database Names**.
    
  - In **Database name**, select the name of the SharePoint database.
    
7. Click **Next**.
    
8. On the **Specify Farm Security Settings** page, in **Passphrase**, type the farm passphrase.
    
9. On the **Specify Server Role** page, in **Shared Roles**, click **Front-end with Distributed Cache**, and then click **Next**.
    
10. The **Completing the SharePoint Products Configuration Wizard** page appears. Click **Next**.
    
11. The **Configuring SharePoint Products** page appears. Wait until the configuration process completes. 
    
12. On the **Configuration Successful** page, click **Finish**.
    
13. On the **Initial Farm Configuration** page, click **Cancel**. You should see the **Central Administration** page. 
    
When SharePoint creates the farm, it configures a set of server logins on the primary SQL Server virtual machine. The database itself stores all the database metadata and user information, and a user who is defined in this database does not need to have a corresponding login. The information in this database is replicated by the availability group and is available after a failover. For more information, see [Contained database](https://msdn.microsoft.com/en-us/library/ff929071.aspx).
  
However, by default, SharePoint databases are not contained databases. Therefore, you will need to manually configure the secondary database server so that it has the same set of logins for SharePoint farm accounts as the primary database server. You can perform this synchronization from SQL Server Management Studio by connecting to both servers at the same time.
  
Here is the configuration that results from the successful completion of this phase. 
  
**Phase 4: The SharePoint servers for your high-availability SharePoint Server 2016 farm**

![Phase 4 of the SharePoint Server 2016 highly-available farm in Azure with SharePoint servers](../media/8f421518-773f-4b4d-8084-005d8a50c38e.png)
  
## Next step

Use [SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases](sharepoint-intranet-farm-in-azure-phase-5-create-the-availability-group-and-add.md) to continue configuring this workload. 
  
## See also

#### Other Resources

[Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](/SharePoint/administration/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in)
  
[SharePoint Server 2016 in Microsoft Azure](/SharePoint/administration/sharepoint-server-2016-in-microsoft-azure)
  
[Designing a SharePoint Server 2016 farm in Azure](/SharePoint/administration/designing-a-sharepoint-server-2016-farm-in-azure)
  
[Install SharePoint Server](/SharePoint/install/install)

