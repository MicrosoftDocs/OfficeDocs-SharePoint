---
title: "SharePoint Intranet Farm in Azure Phase 5 Create the availability group and add the SharePoint databases"
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
ms.assetid: 62d0b8d3-e8ea-4523-a69f-62623fb340fb
description: "Configure the SQL Server availability group for your high-availability SharePoint Server 2016 farm in Microsoft Azure."
---

# SharePoint Intranet Farm in Azure Phase 5: Create the availability group and add the SharePoint databases

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
In this final phase of deploying an intranet-only SharePoint Server 2016 farm in Azure infrastructure services, you create a new SQL Server AlwaysOn Availability Group with the databases of the SharePoint farm, create the availability group listener, and then complete the SharePoint farm configuration.
  
See [Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](/SharePoint/administration/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in) for all of the phases. 
  
## Configure the availability group

SharePoint creates two databases as part of the initial configuration. Those databases must be prepared with the following steps:
  
1. Database Recovery Model must be set to FULL.
    
2. Take a full backup and a transaction log backup of the database on the primary machine. Restore the full and log backups on the backup machine.
    
Once the databases have been both backed up and restored, they can be added to the availability group. SQL Server allows only databases that have been backed up (at least once), and restored on another machine, to be in the group.
  
Make the backup files (.bak) accessible from the secondary SQL Server virtual machine with these steps:
  
1. Connect to the primary SQL Server virtual machine with the \<your domain>**\sp_farm_db** account credentials. 
    
2. Open File Explorer and navigate to the **H:** disk. 
    
3. Right-click the **Backup** folder, click **Share with**, and then click **Specific people**.
    
4. In the **File sharing** dialog, type \<your domain name>**\sqlservice**, and then click **Add**.
    
5. Click the **Permission Level** column for the **sqlservice** account name, and then click **Read/Write**.
    
6. Click **Share**, and then click **Done**.
    
Perform the previous procedure on the secondary SQL Server host, except grant the **sqlservice** account **Read** permission for the **H:\Backup** folder in step 5. 
  
Perform the following steps for every database that you are adding to the availability group:
  
1. From the primary SQL Server virtual machine, click **Start**, type **SQL Studio**, and then click **SQL Server Management Studio**.
    
2. Click **Connect**.
    
3. In the left pane, expand the **Databases** node. 
    
4. Right-click a database and select properties.
    
5. Select the **Options** item from the left navigation. 
    
6. Ensure that **Recovery Model** is set to **FULL**. If it is not, change it to support AlwaysOn Functionality.
    
The following procedures must be repeated for every database that needs to be added to the availability group. Some SharePoint Server 2016 databases do not support SQL Server AlwaysOn Availability Groups. For more information, see [Supported high availability and disaster recovery options for SharePoint databases](/SharePoint/administration/supported-high-availability-and-disaster-recovery-options-for-sharepoint-databas).
  
 **To back up a database**
  
1. Connect to the first SQL Server virtual machine.
    
2. Click **Start**, type **SQL Studio**, and then click **SQL Server Management Studio**.
    
3. Click **Connect**.
    
4. In the left pane, expand the **Databases** node. 
    
5. Right-click a database to back up, point to **Tasks**, and then click **Back up**.
    
6. In the **Destination** section, click **Remove to remove the default file path for the backup file**.
    
7. Click **Add.** In **File name**, type **\\**\<machineName>**\backup**\<databaseName> **.bak**, where machineName is the name of the primary SQL Server computer and databaseName is the name of the database. Click **OK**, and then click **OK** again after the message about the successful backup. 
    
8. In the left pane, right-click \<databaseName>, point to **Tasks**, and then click **Back Up**.
    
9. In **Backup type**, select **Transaction Log**, and then click **OK** twice. 
    
Keep the Remote Desktop session to the first SQL Server virtual machine open.
  
 **To restore a database**
  
1. Connect to the secondary SQL Server virtual machine with the \<your domain>**\sp_farm_db** account credentials. 
    
2. From the secondary SQL Server virtual machines, click **Start**, type **SQL Studio**, and then click **SQL Server Management Studio**.
    
3. Click **Connect**.
    
4. In the left pane, right-click **Databases**, and then click **Restore Database**.
    
5. In the **Source** section, select **Device**, and then click the ellipsis ( **…**) button.
    
6. In **Select backup devices**, click **Add**.
    
7. In **Backup file location,** type **\\**\<machine name>**\backup**, press Enter, select \<databaseName>**.bak**, and then click **OK** twice. You should now see the full backup and the log backup in the **Backup sets to restore** section. 
    
8. Under **Select a page**, click **Options**. In the **Restore options** section, in **Recovery state**, select **RESTORE WITH NORECOVERY**, and then click **OK**.
    
9. Click **OK** when prompted. 
    
After at least one database is prepared (using the backup and restore method), you create an availability group with these steps:
  
1. Return to the Remote Desktop session for the first SQL Server virtual machine.
    
2. In **SQL Server Management Studio**, in the left pane, right-click **AlwaysOn High Availability**, and then click **New Availability Group Wizard**.
    
3. On the **Introduction** page, click **Next**.
    
4. On the **Specify Availability Group Name** page, type the name of your availability group in **Availability group name** (example: AG1), and then click **Next**.
    
5. On the **Select Databases** page, select the databases for the SharePoint farm that were backed up, and then click **Next**. These databases meet the prerequisites for an availability group because you have taken at least one full backup on the intended primary replica.
    
6. On the **Specify Replicas** page, click **Add Replica**.
    
7. In **Connect to Server**, type the name of the secondary SQL Server virtual machine, and then click **Connect**.
    
8. On the **Specify Replicas** page, the secondary SQL Server virtual machine is listed in **Availability Replicas**. For both instances, set the following option values:
    
|**Initial role**|**Option**|**Value**|
|:-----|:-----|:-----|
|Primary  <br/> |Automatic Failover (Up to 2)  <br/> |Selected  <br/> |
|Secondary  <br/> |Automatic Failover (Up to 2)  <br/> |Selected  <br/> |
|Primary  <br/> |Synchronous Commit (Up to 3)  <br/> |Selected  <br/> |
|Secondary  <br/> |Synchronous Commit (Up to 3)  <br/> |Selected  <br/> |
|Primary  <br/> |Readable Secondary  <br/> |Yes  <br/> |
|Secondary  <br/> |Readable Secondary  <br/> |Yes  <br/> |
   
9. Click **Next**.
    
10. On the **Select Initial Data Synchronization** page, click **Join only**, and then click **Next**. Data synchronization is executed manually by taking the full and transaction backups on the primary server, and restoring it on the backup. You can instead choose to select **Full** to let the New Availability Group Wizard perform data synchronization for you. However, Microsoft does not recommend **Full automatic synchronization** for large databases that are found in some enterprises. 
    
11. On the **Validation** page, click **Next**. There is a warning for a missing listener configuration because an availability group listener is not configured. We will do this step manually in a later procedure in this article.
    
12. On the **Summary** page, click **Finish**. Once the wizard is finished, inspect the **Results** page to verify that the availability group is successfully created. If so, click **Close** to exit the wizard. 
    
13. Click **Start**, type **Failover**, and then click **Failover Cluster Manager**. In the left pane, open the name of your cluster, and then click **Roles**. A new role with the name of your availability group should be present.
    
## Configure the availability group listener

The Availability Group listener is an IP address and DNS name that the SQL Server Availability Group listens on. Use these steps to create the Availability Group listener for the SQL Server cluster:
  
1. Determine the Cluster Network Resource Name with these steps.
    
  - Click **Start**, type **Failover**, and then click **Failover Cluster Manager**.
    
  - Click the **Networks** node and note the cluster network name. You will need this name for the **$ClusterNetworkName** variable in the PowerShell command block in step 6 of this procedure. 
    
2. The client access point is the network name that applications use to connect to the databases in an availability group. Add the client access point with these steps.
    
  - From Failover Cluster Manager, expand the cluster name, and then click **Roles**.
    
  - In the **Roles** pane, right-click the Availability Group name and then select **Add Resource \> Client Access Point**.
    
  - In **Name**, specify a name for this new listener.
    
    The name for the new listener is the network name that applications use to connect to databases in the SQL Server Availability Group.
    
  - Click **Next** twice, and then click **Finish**. Do not bring the listener or resource online at this time.
    
3. Configure the IP resource for the Availability Group with these steps:
    
  - Click the **Resources** tab, then expand the client access point you created. The client access point is offline. 
    
  - Right-click the IP resource, and then click **Properties**. Note the name of the IP address. You will need this name for the **$IPResourceName** variable in the PowerShell command block in step 6 of this procedure. 
    
  - Under **IP Address**, click **Static IP Address**. Set the IP address to the value of Table I - Item 4.
    
4. Make the SQL Server availability group resource dependent on the client access point with these steps:
    
  - In Failover Cluster Manager, click **Roles**, and then click your Availability Group.
    
  - On the **Resources** tab, right-click the availability resource group under **Server Name**, and then click **Properties**.
    
  - On the **Dependencies** tab, add the name resource. This resource is the client access point. 
    
  - Click **OK**.
    
5. Make the client access point resource dependent on the IP address with these steps:
    
  - In Failover Cluster Manager, click **Roles**, and then click your Availability Group.
    
  - On the **Resources** tab, right-click the client access point resource under **Server Name**, and then click **Properties**.
    
  - Click the **Dependencies** tab. Set a dependency on the listener resource name. If there are multiple resources listed, verify that the IP addresses have **OR**, not **AND**, dependencies. Click **OK**.
    
  - Right-click the listener name and click **Bring Online**.
    
6. Set the cluster parameters with these steps:
    
  - Connect to one of the SQL Server virtual machines with the \<domain name>**\sp_farm_db** account credentials. 
    
  - Open an administrator-level PowerShell command prompt, specify the variable values, and then run these commands:
    
  ```
  $ClusterNetworkName = "<MyClusterNetworkName>"
  $IPResourceName = "<IPResourceName>"
  $ILBIP = "<Table I - Item 4 - Value column>"
  [int]$ProbePort = <nnnnn>
  Import-Module FailoverClusters
  Get-ClusterResource $IPResourceName | Set-ClusterParameter -Multiple @{"Address"="$ILBIP";"ProbePort"=$ProbePort;"SubnetMask"="255.255.255.255";"Network"="$ClusterNetworkName";"EnableDhcp"=0}
  
  ```

  
Use these steps to configure the listener port:
  
1. Connect to the first SQL Server virtual machine, launch SQL Server Management Studio, and connect to the local computer.
    
2. Navigate to **AlwaysOn High Availability \> Availability Groups \> Availability Group Listeners**.
    
    You should now see the listener name that you created in Failover Cluster Manager.
    
3.  Right-click the listener name, and then click **Properties**.
    
4. In the **Port** box, specify the port number for the availability group listener by using the $ProbePort you used earlier (1433 was the default), then click **OK**.
    
Use these steps to test the connection to the listener:
  
1. Connect to the second SQL Server virtual machine and open an administrator-level command prompt.
    
2. Use the **sqlcmd** tool to test the connection. For example, the following command establishes a sqlcmd connection to the primary replica through the listener with Windows authentication: 
    
  ```
  sqlmd -S <listenerName> -E
  ```

  If the listener is using a port other than the default port (1433), specify the port in the connection string. For example, the following sqlcmd command connects to a listener at port 1435: 
    
  ```
  sqlcmd -S <listenerName>,1435 -E
  ```

  The sqlcmd connection automatically connects to whichever instance of SQL Server hosts the primary replica. 
    
You use the health dashboard to check the AlwaysOn Availability Group for successful operation with these steps:
  
1. On the first SQL Server virtual machines, in the left pane of SQL Server Management Studio, expand **AlwaysOn High Availability \> Availability Groups**.
    
2. Right-click your Availability Group, and then click **Show Dashboard**.
    
    The dashboard status should show all green for **Synchronization State**.
    
## Complete the SharePoint farm configuration

Now that the SharePoint configuration and admin content databases have been added to the Availability Group and are synchronizing correctly, the next step is to ensure they are accessible in the event of a SQL Server node failure. To do this, the SQL Server database connection string for the SharePoint farm needs to be updated to match the DNS name of the SQL cluster internal load balancer.
  
> [!NOTE]
> With an on-premises SQL Server AlwaysOn deployment, the Availability Groups would use Listeners to present a connection point to the SharePoint Servers. In Azure IaaS there are network limitations which prevent this and so the internal load balancer DNS name must be used instead. Because of this situation, the SharePoint PowerShell cmdlets for managing availability group membership cannot be used. You must use database object method calls instead. 
  
Use these steps to update the SharePoint database connection strings:
  
1. Connect to one of the SharePoint servers in the farm and launch an administrator-level PowerShell command prompt.
    
2. Check the current connection string settings for each database in the farm with these commands:
    
  ```
  Add-psnappin Microsoft.SharePoint.PowerShell -EA 0
  Get-Spdatabase | select name, server
  
  ```

  The display of the **Get-Spdatabase** command shows the database name and the server property value from the connection string. 
    
3. For each database in an availability group having a server property that matches a SQL node in the cluster, you must update this property value to match the load balancer DNS name with PowerShell. This example is for the SharePoint_Config Database.
    
  ```
  Get-SPDatabase  #Lists all available SharePoint Databases
  $agName = "<Availability Group Listener DNS name>"
  $db = Get-SPDatabase -Name "Sharepoint_Config"
  $db.ChangeDatabaseInstance("$agName")
  $db.update()
  
  ```

After completing this task for each database in the availability group, you can conduct a failover test.
  
Use these steps to conduct a failover of the SQL Server Availability Group to ensure that the Central Administration Web Site remains operational:
  
1. Connect to one of the SharePoint servers in the farm.
    
2. Launch SharePoint Central Administration and browse around the web site and ensure that you get no errors.
    
3. Connect to the first SQL Server virtual machine and launch SQL Server Management Studio.
    
4. Expand the **Availability Groups** node, right-click on the Availability Group name, and then click **Failover**.
    
5. The Availability Group Failover wizard starts. Click **Next**.
    
6. On the **Select new primary replica for this availability group** page, select the second SQL Server virtual machine, and then click **Next**.
    
7. Click on **Connect to authenticate against the secondary node**, and then click **Next**.
    
8. Click **Finish** to verify the action and manual failover will start. 
    
9. Review the failover wizard summary information for errors or warnings.
    
10. Return to the SharePoint server where you were browsing the Central Administration website and ensure you can still browse the site without error.
    
Your high availability SharePoint Server 2016 farm in Azure is complete.
  
![Phase 4 of the SharePoint Server 2016 highly-available farm in Azure with SharePoint servers](../media/8f421518-773f-4b4d-8084-005d8a50c38e.png)
  
## See also

#### Other Resources

[Deploying SharePoint Server 2016 with SQL Server AlwaysOn Availability Groups in Azure](/SharePoint/administration/deploying-sharepoint-server-2016-with-sql-server-alwayson-availability-groups-in)
  
[SharePoint Server 2016 in Microsoft Azure](/SharePoint/administration/sharepoint-server-2016-in-microsoft-azure)
  
[Designing a SharePoint Server 2016 farm in Azure](/SharePoint/administration/designing-a-sharepoint-server-2016-farm-in-azure)
  
[Install SharePoint Server](/SharePoint/install/install)

