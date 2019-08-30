---
title: "Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn how to deploy Azure SQL Managed Instance (MI) with SharePoint Servers 2016 and 2019."
---

# Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]

SharePoint Servers 2016 and 2019 now support Azure SQL Managed Instance (MI). SQL MI is a deployment option of Azure SQL Database and is compatible with the current version of SQL Server (on-premises), Enterprise Edition Database Engine. 

> [!IMPORTANT]
> SharePoint Server farms must be hosted in Microsoft Azure to support Azure SQL Managed Instance. The SharePoint Server farm and the managed instance must be hosted in the same Azure region. SharePoint Server farms don't support managed instances when hosted in customer datacenters.

Deploying a managed instance with SharePoint Server lets you move your SQL Server on-premises application to the cloud with little or no application and database changes. The following procedure shows how to deploy an Azure SQL Database Managed Instance with SharePoint Servers 2016 and 2019.  

## Environment

1. Create a resource group with a vNet and then create two subnets. You can use the [SQL Managed Instance Virtual Network Environment](https://github.com/Azure/azure-quickstart-templates/tree/master/101-sql-managed-instance-azure-environment) template to create an Azure Virtual Network with two subnets.
 
2. Create subnet 1 (Default) and then create two VMs. First, set up VM 1 as an Active Directory Directory Services domain controller and configure your domain. For more information, see [Step-By-Step: Setting up Active Directory in Windows Server 2016](https://blogs.technet.microsoft.com/canitpro/2017/02/22/step-by-step-setting-up-active-directory-in-windows-server-2016/).  

3. Install SharePoint Server 2016 or SharePoint Server 2019 in VM 2:
       
    -  Run **PrerequitsiteInstaller.exe**
         
    - Run **Setup.exe**
         
    - Install the May 2019 sts core patch for SharePoint Server 2016, [KB 4464549](http://www.microsoft.com/downloads/details.aspx?familyid=ca8d6a39-efbc-4ae5-ad61-39a8c7236919) or SharePoint Server 2019, [KB 4464556](https://support.microsoft.com/en-us/help/4464556)
         
    - Install the April 2019 wssloc MUI/language pack patch for SharePoint Server 2016, [KB 4461507](https://support.microsoft.com/en-us/help/4461507) or for SharePoint Server 2019, [KB 4462221](https://support.microsoft.com/en-us/help/4462221)

   > [!NOTE]
   > You can join other VMs to Active Directory in subnet 1.

3. Create an Azure SQL Managed Instance in subnet 2, within this resource group (ManagedInstance).

   > [!IMPORTANT]
   > No other resources can reside in subnet 2 except for SQL MI.

4. Create the SharePoint farm, hosting the databases on SQL MI with SQL authentication. Open the **SharePoint Management Shell** and run the following Windows PowerShell commands:

   ```powershell
      $FarmCredential = Get-Credential -Message "Provide the user name and password for the SharePoint farm service account." 
      $DBCredential = Get-Credential -Message "Provide the user name and password for the Azure SQL Managed Instance database login." 
      $FarmPassphrase = Read-Host -AsSecureString -Prompt "Provide the SharePoint farm passphrase" 

      New-SPConfigurationDatabase -DatabaseServer <DBServer> -DatabaseName <ConfigDB> -FarmCredentials $FarmCredential -DatabaseCredentials $DBCredential -Passphrase $FarmPassphrase -LocalServerRole <ServerRole> 
   ```

    Where:
    
   - _\<DBServer\>_ is the name you gave the Azure SQL Managed Instance in step 4.
   - _\<ConfigDB\>_ is the name of the SharePoint configuration database to be created.
   - _\<ServerRole\>_ is the SharePoint MinRole server role for this server in the SharePoint farm.

5. Run the **SharePoint Products Configuration Wizard** to complete the configuration. Next open Central Administration to complete the **Farm Configuration Wizard**.

> [!NOTE]
> Access Services isn't supported with Azure SQL Managed Instances.


## See also
<a name="proc1"> </a>

#### Other Resources

[Azure SQL Database managed instance](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-index)

[SQL Server instance migration to Azure SQL Database managed instance](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-migrate)

[Quickstart: Create an Azure SQL Database managed instance](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-get-started)

[Quickstart: Configure Azure VM to connect to an Azure SQL Database Managed Instance](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-configure-vm)

[Quickstart: Restore a database to a Managed Instance](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-managed-instance-get-started-restore)
