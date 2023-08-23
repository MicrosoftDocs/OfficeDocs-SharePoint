---
ms.date: 05/20/2019
title: "Deploy SharePoint Server with Azure SQL Managed Instance"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn how to deploy SharePoint Servers 2016, 2019, and Subscription Edition with Azure SQL Managed Instance (MI)."
---

# Deploy SharePoint Server with Azure SQL Managed Instance

[!INCLUDE[appliesto-xxx-2016-2019-xxx-xxx-md](../includes/appliesto-xxx-2016-2019-SUB-xxx-md.md)]

SharePoint Server 2016, SharePoint Server 2019, and SharePoint Server Subscription Edition support Azure SQL Managed Instance (MI). SQL MI is a deployment option of Azure SQL Database and is compatible with the current version of SQL Server (on-premises), Enterprise Edition Database Engine. 

> [!IMPORTANT]
> SharePoint Server farms must be hosted in Microsoft Azure to support Azure SQL Managed Instance. The SharePoint Server farm and the managed instance must be hosted in the same Azure region. SharePoint Server farms don't support managed instances when hosted in customer data centers.

Deploying SharePoint Server with an Azure SQL Managed Instance lets you move your SQL Server on-premises application to the cloud with little or no application and database changes. The following procedure shows how to deploy SharePoint Servers 2016, 2019, or Subscription Edition with an Azure SQL Managed Instance.  


## Environment

1. Create a resource group with a vNet and then create two subnets. You can use the [SQL Managed Instance Virtual Network Environment](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.sql/sql-managed-instance-azure-environment) template to create an Azure Virtual Network with two subnets.
 
2. Create subnet 1 (Default) and then create two VMs. First, set up VM 1 as an Active Directory Directory Services domain controller and configure your domain. For more information, see [Step-By-Step: Setting up Active Directory in Windows Server 2016](/archive/blogs/canitpro/step-by-step-setting-up-active-directory-in-windows-server-2016).  

3. Install SharePoint Server 2016 or SharePoint Server 2019 or SharePoint Server Subscription Edition in VM 2:
       
   1. Run **`PrerequitsiteInstaller.exe`**.
         
   2. Run **`Setup.exe`**.
         
   3. If you're using SharePoint Server 2016 or SharePoint Server 2019, install the May 2019 (or newer) sts core patch for SharePoint Server 2016 ([KB 4464549](https://support.microsoft.com/help/4464549)) or for SharePoint Server 2019 ([KB 4464556](https://support.microsoft.com/help/4464556)).
         
   4. If you're using SharePoint Server 2016 or SharePoint Server 2019, Install the April 2019 (or newer) wssloc MUI/language pack patch for SharePoint Server 2016 ([KB 4461507](https://support.microsoft.com/help/4461507)) or for SharePoint Server 2019 ([KB 4462221](https://support.microsoft.com/help/4462221)).

   > [!NOTE]
   > You can join other VMs to Active Directory in subnet 1.
   >
   > No updates need to be installed for SharePoint Server Subscription Edition.

3. Create an Azure SQL Managed Instance in subnet 2, within this resource group (ManagedInstance).

   > [!IMPORTANT]
   > No other resources can reside in subnet 2 except for SQL MI.
   

4. Create or join the SharePoint farm, hosting the databases on SQL MI with SQL authentication.

   1. To create the SharePoint farm, open the **SharePoint Management Shell** and run the following Windows PowerShell commands:

      ```powershell
         $FarmCredential = Get-Credential -Message "Provide the user name and password for the SharePoint farm service account." 
         $DBCredential = Get-Credential -Message "Provide the user name and password for the Azure SQL Managed Instance database login." 
         $FarmPassphrase = Read-Host -AsSecureString -Prompt "Provide the SharePoint farm passphrase" 

         New-SPConfigurationDatabase -DatabaseServer <DBServer> -DatabaseName <ConfigDB> -FarmCredentials $FarmCredential -DatabaseCredentials $DBCredential -Passphrase $FarmPassphrase -LocalServerRole <ServerRole> 
      ```

   2. To join additional VMs to the SharePoint farm, open the **SharePoint Management Shell** on the additional VMs and run the following Windows PowerShell commands:
   
      ```powershell
         $DBCredential = Get-Credential -Message "Provide the user name and password for the Azure SQL Managed Instance database login." 
         $FarmPassphrase = Read-Host -AsSecureString -Prompt "Provide the SharePoint farm passphrase" 

         Connect-SPConfigurationDatabase -DatabaseServer <DBServer> -DatabaseName <ConfigDB> -DatabaseCredentials $DBCredential -Passphrase $FarmPassphrase -LocalServerRole <ServerRole> 
      ```

   Where:
   
   - _\<DBServer\>_ is the name you gave the Azure SQL Managed Instance in step 4.
   - _\<ConfigDB\>_ is the name of the SharePoint configuration database to be created.
   - _\<ServerRole\>_ is the SharePoint MinRole server role for this server in the SharePoint farm.

5. Run the **SharePoint Products Configuration Wizard** to complete the configuration. Next open Central Administration to complete the **Farm Configuration Wizard**.

> [!NOTE]
> SharePoint Server doesn't support connecting to databases hosted in Azure SQL Managed Instance using Windows authentication.

> [!NOTE]
> Access Services isn't supported with Azure SQL Managed Instance.


## See also
<a name="proc1"> </a>

#### Other Resources

[Azure SQL Database managed instance](/azure/sql-database/sql-database-managed-instance-index)

[SQL Server instance migration to Azure SQL Database managed instance](/azure/sql-database/sql-database-managed-instance-migrate)

[Quickstart: Create an Azure SQL Database managed instance](/azure/sql-database/sql-database-managed-instance-get-started)

[Quickstart: Configure Azure VM to connect to an Azure SQL Database Managed Instance](/azure/sql-database/sql-database-managed-instance-configure-vm)

[Quickstart: Restore a database to a Managed Instance](/azure/sql-database/sql-database-managed-instance-get-started-restore)
