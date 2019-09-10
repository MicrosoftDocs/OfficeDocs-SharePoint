---
title: "Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/1/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0926f63d-8dae-44c0-9e91-51209aa4c3ef
description: "Learn how to add a server to an existing SharePoint Server farm."
---

# Add a server to a SharePoint Servers 2016 or 2019 farm

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]
  
    
## Before you add a server to a SharePoint farm
<a name="begin"> </a>

### Determine server role

To add a new server to the farm, you must know its intended role to plan for additional or specialized configurations and assess the potential effect of adding the server to a production environment.
  
In SharePoint Server 2016, the concept of server roles has changed from previous versions. Server role types are now defined by MinRole which allow for better deployment and health of the server in the farm. For additional information about the MinRole feature and a description for each server role type, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](overview-of-minrole-server-roles-in-sharepoint-server.md).
  
### Additional tasks

Before you start to install prerequisite software, you have to complete the following:
  
- Verify that the new server meets the hardware and software requirements described in [Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md).

- Verify that the new server meets the hardware and software requirements described in [Hardware and software requirements for SharePoint Server 2019](hardware-and-software-requirements-2019.md).
    
- Verify that you have the minimum level of permissions that are required to install and configure SharePoint Servers 2016 or 2019 on a new server. You must be a member of the Farm Administrators SharePoint group and the Administrators group on the local server to complete the procedures in this article. For more information, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
- Verify that you know the name of the database server on the farm to which you are connecting, and the name of the configuration database if you are adding the server by using Microsoft PowerShell commands.
    
- If you intend to use PowerShell commands to add the server, verify that you meet the following minimum memberships is installed.
    
- **Securityadmin** fixed server role on the SQL Server instance. 
    
- **db_owner** fixed database role on all databases that are to be updated. 
    
- Administrators group on the server on which you are running the PowerShell cmdlets.
    
- An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
> [!NOTE]
> If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
- Document the location of the SharePoint Server binary and log files on the existing farm servers. We recommend that the location of these files on the new server map to the locations used on the other servers in the farm.
    
> [!IMPORTANT]
> If you change the location of the trace log to a non-system drive, change the location on all the servers in the farm. Existing or new servers cannot log data if the location does not exist. In addition, you will be unable to add new servers unless the path that you specify exists on the new server. You cannot use a network share for logging purposes. 
  
## Install prerequisite software
<a name="prereq"> </a>

Before you can install SharePoint Server and add a server to the farm, you must check for and install all the prerequisite software on the new server. You do this by using the Microsoft SharePoint Products Preparation Tool, which requires an Internet connection to download and configure SharePoint Server prerequisites. If you do not have an Internet connection for the farm servers, you can still use the tool to determine the software that is required. You will have to obtain installable images for the required software.

 For download locations, see [Links to applicable software](hardware-and-software-requirements.md#section5) in "Hardware and software requirements (SharePoint Server 2016)." 

For download locations, see [Links to applicable software](hardware-and-software-requirements-2019.md#section5) in "Hardware and software requirements (SharePoint Server 2019)." 
  
> [!TIP]
> After you obtain a copy of the required software, we recommend that you create an installation point that you can use to store the images. You can use this installation point to install future software updates. 
  
For detailed instructions about how to install the prerequisites, see [Prepare the farm servers](install-sharepoint-server-2016-across-multiple-servers.md#PrepareServers) in the article, [Install SharePoint Servers 2016 or 2019 across multiple servers](install-sharepoint-server-2016-across-multiple-servers.md).
  
> [!TIP]
> If you decide to install prerequisites manually, you can still run the Microsoft SharePoint Products Preparation Tool to verify which prerequisites are required on each server. 
  
## Install the SharePoint software
<a name="installSP"> </a>

After you install the prerequisites, follow these steps to install SharePoint Servers 2016 or 2019 on the new server. For detailed instructions about how to install SharePoint Server, see [Install SharePoint Server on one server](install-sharepoint-server-2016-on-one-server.md).
  
 **To install SharePoint Server**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. From the product media or a file share that contains the SharePoint Server Products installation files, run Setup.exe.
    
3. On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.
    
4. Review and accept the Microsoft License Terms.
    
5. Accept the default file location where SharePoint Server will be installed or change the installation path in order to suit your requirements.
    
> [!TIP]
> As a best practice, we recommend that you install SharePoint Server on a drive that does not contain the operating system. 
  
6. Click **Install Now**.
    
7. When Setup finishes, a dialog box prompts you to run the **SharePoint Products Configuration Wizard**. You can start the wizard immediately or from the Windows command prompt later.
    
## Add the new SharePoint server to the farm
<a name="addserver"> </a>

You add the new server to the farm by using one of the following procedures:
  
- [To add a server by using the SharePoint Products Configuration Wizard](add-a-server-to-a-sharepoint-server-2016-farm.md)
    
- [To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using the PSConfig.exe command-line tool](#psconfig)
    
- [To add a server by using Microsoft PowerShell](add-a-server-to-a-sharepoint-server-2016-farm.md)
    
 **To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using the SharePoint Products Configuration Wizard**
  
Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
1. Start the **SharePoint Products Configuration Wizard**.
    
   
2. On the **Welcome to SharePoint Products** page, click **Next**.
    
3. On the **Connect to a server farm** page, click **Connect to an existing server farm.**
    
4. Click **Next**.
    
5. On the **Specify Configuration Database settings** page, type the name of the instance of SQL Server in the **Database server** box, and then click **Retrieve Database Names**. 
    
6. Select the name of the configuration database in the **Database name** list, and then click **Next**.
    
7. On the **Specify Farm Security Settings** page, type the name of the farm passphrase in the **Passphrase** box, and then click **Next**.
    
8. On the **Specify Server Role** page, choose the appropriate role, and then click **Next**.
    
> [!NOTE]
> The concept of server roles has changed staring with SharePoint Server 2016. You can't add a server to a farm if the farm currently contains a server assigned to the "Single Server Farm" role. > For additional information about MinRole, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](overview-of-minrole-server-roles-in-sharepoint-server.md). 
  
9. On the **Completing the SharePoint Products Configuration Wizard** page, click **Next**.
    
10. On the server that hosts Central Administration, click **Manage servers in this farm** to verify that the new server is part of the farm. 
    
> [!NOTE]
> You can also verify a successful server addition or troubleshoot a failed addition by examining the log files. These files are located on the drive on which SharePoint Server is installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder. 
  
11. On the **Servers in Farm** page, click the name of the new server. Use the list of available services on the **Services on Server** page to start the services that you want to run on the new server. 
    
> [!NOTE]
> This step should only apply if the Custom role is used. 
  
 <a name="psconfig"></a>**To add a new SharePoint Server server to the farm by using the PSConfig.exe command-line tool**

1. To create a farm by using the PSConfig.exe command-line tool, use the following syntax:
    
  ```
  psconfig.exe -cmd configdb -connect -server <SqlServerName> -database <ConfigDbName> -user <DOMAIN\FarmServiceAccount> -password <FarmServiceAccountPassword> -passphrase <FarmPassphrase> -admincontentdatabase <AdminContentDbName> -localserverrole <ServerRole> -cmd helpcollections -installall -cmd secureresources -cmd services -install -cmd installfeatures -cmd adminvs -provision -port <PortNumber> -windowsauthprovider onlyusentlm -cmd applicationcontent -install
  ```

Where \<ServerRole\> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom.
    
> [!NOTE]
> The SingleServerFarm cannot be used unless the SharePoint farm has zero servers in it. 
    
> [!NOTE]
> If SharePoint Server 2016 Feature Pack 2 has been applied, additional \<ServerRole> options are available: ApplicationWithSearch, WebFrontEndWithDistributedCache. These options are also available in SharePoint Server 2019.
  
> [!NOTE]
> The  `PSConfig.exe -cmd Services -Provision` syntax is deprecated, but not removed yet. Do not use the **Provision** parameter when you create or join a farm. Using this parameter will lead to failures. 
  
 **To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using PowerShell**
  
Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
> [!NOTE]
> If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps
1. Start the SharePoint Management Shell.
    
    
2. At the PowerShell command prompt, type the following command to connect the server to a configuration database: 
    
  ```
  Connect-SPConfigurationDatabase -DatabaseServer <SqlServerName> -DatabaseName <ConfigDbName> -Passphrase <FarmPassphrase>  -LocalServerRole <ServerRole>
  ```

  Where:
    
  -  _\<$DatabaseServer\>_ is the name of the server that hosts the configuration database 
    
  -  _\<DatabaseName\>_ is the name of the configuration database 
    
  -  _\<$Passphrase\>_ is the passphrase for the farm 
    
  -  _\<ServerRole\>_ is the server role type 
    
    Where \<ServerRole\> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom. 
    
> [!NOTE]
> If SharePoint Server 2016 Feature Pack 2 has been applied, additional \<ServerRole> options are available: ApplicationWithSearch, WebFrontEndWithDistributedCache. These options are also available in SharePoint Server 2019.
    
> [!NOTE]
> The concept of server roles has changed starting with SharePoint Server 2016. You can't add a server to a farm if the farm currently contains a server assigned to the "Single Server Farm" role. > For additional information about MinRole, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](overview-of-minrole-server-roles-in-sharepoint-server.md). 
  
3. At the PowerShell command prompt, type the following command to install the Help File Collections:
    
  ```
  Install-SPHelpCollection -All
  ```

4. At the PowerShell command prompt, type the following command to install the Security Resource for SharePoint Server:
    
  ```
  Initialize-SPResourceSecurity
  ```

5. At the PowerShell command prompt, type the following command to install the basic services: 
    
  ```
  Install-SPService
  ```

6. At the PowerShell command prompt, type the following command to install all the features:
    
  ```
  Install-SPFeature -AllExistingFeatures
  ```

7. At the PowerShell command prompt, type the following command to set the port number of the SharePoint Central Administration website:
    
  ```
  New-SPCentralAdministration -Port <PortNumber> -WindowsAuthProvider NTLM
  ```

> [!NOTE]
> If the SharePoint Central Administration website is already provisioned on an existing server in the farm, you can skip this step. 
  
8. At the PowerShell command prompt, type the following command to install application content:
    
  ```
  Install-SPApplicationContent
  ```

9. At the PowerShell command prompt, type the following command to start the Timer service:
    
  ```
  Start-Service SPTimerV4
  ```

10. At the PowerShell command prompt, type the following command to get a list of servers in the farm. 
    
  ```
  Get-SPServer
  ```

> [!NOTE]
> You can also verify a successful server addition or troubleshoot a failed addition by examining the log files. These files are located on the drive on which SharePoint Servers 2016 or 2019 is installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder.  

