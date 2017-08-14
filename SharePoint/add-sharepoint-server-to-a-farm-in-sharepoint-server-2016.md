---
title: Add SharePoint server to a farm in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 0926f63d-8dae-44c0-9e91-51209aa4c3ef
---


# Add SharePoint server to a farm in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-01* **Summary:** Learn how to add a server to an existing SharePoint Server 2016 farm.In this article:
-  [Before you add a web or application server to a SharePoint farm](#begin)
    
  
-  [Install prerequisite software](#prereq)
    
  
-  [Install the SharePoint software ](#installSP)
    
  
-  [Add the new SharePoint server to the farm](#addserver)
    
  

## Before you add a server to a SharePoint farm
<a name="begin"> </a>


## Determine server role

To add a new server to the farm, you must know its intended role to plan for additional or specialized configurations and assess the potential effect of adding the server to a production environment.In SharePoint Server 2016, the concept of server roles has changed from previous versions. Server role types are now defined by MinRole which allow for better deployment and health of the server in the farm. For additional information about the MinRole feature and a description for each server role type, see  [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md).
## Additional tasks

Before you start to install prerequisite software, you have to complete the following:
- Verify that the new server meets the hardware and software requirements described in  [Hardware and software requirements for SharePoint Server 2016](html/hardware-and-software-requirements-for-sharepoint-server-2016.md).
    
  
- Verify that you have the minimum level of permissions that are required to install and configure SharePoint Server 2016 on a new server. You must be a member of the Farm Administrators SharePoint group and the Administrators group on the local server to complete the procedures in this article. For more information, see  [Initial deployment administrative and service accounts in SharePoint Server](html/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
  
- Verify that you know the name of the database server on the farm to which you are connecting, and the name of the configuration database if you are adding the server by using Microsoft PowerShell commands.
    
  
- If you intend to use PowerShell commands to add the server, verify that you meet the following minimum memberships is installed.
    
  
- **Securityadmin** fixed server role on the SQL Server instance.
    
  
- **db_owner** fixed database role on all databases that are to be updated.
    
  
- Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
- An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
- Document the location of the SharePoint Server 2016 binary and log files on the existing farm servers. We recommend that the location of these files on the new server map to the locations used on the other servers in the farm.
    
    > [!IMPORTANT:]
      

## Install prerequisite software
<a name="prereq"> </a>

Before you can install SharePoint Server 2016 and add a server to the farm, you must check for and install all the prerequisite software on the new server. You do this by using the Microsoft SharePoint Products Preparation Tool, which requires an Internet connection to download and configure SharePoint Server 2016 prerequisites. If you do not have an Internet connection for the farm servers, you can still use the tool to determine the software that is required. You will have to obtain installable images for the required software. For download locations, see  [Access to applicable software](hardware-and-software-requirements-for-sharepoint-server-2016.md#section5) in "Hardware and software requirements (SharePoint Server 2016)."
> [!TIP:]

  
    
    

For detailed instructions about how to install the prerequisites, see  [Prepare the farm servers](install-sharepoint-server-2016-across-multiple-servers.md#PrepareServers) in the article, [Install SharePoint Server 2016 across multiple servers](html/install-sharepoint-server-2016-across-multiple-servers.md).
> [!TIP:]

  
    
    


## Install the SharePoint software
<a name="installSP"> </a>

After you install the prerequisites, follow these steps to install SharePoint Server 2016 on the new server. For detailed instructions about how to install SharePoint Server 2016, see  [Install SharePoint Server 2016 on a single server with SQL Server](html/install-sharepoint-server-2016-on-a-single-server-with-sql-server.md). **To install SharePoint Server 2016**
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see  [Initial deployment administrative and service accounts in SharePoint Server](html/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
  
2. From the product media or a file share that contains the SharePoint Server 2016 Products installation files, run Setup.exe.
    
  
3. On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.
    
  
4. Review and accept the Microsoft License Terms.
    
  
5. Accept the default file location where SharePoint Server 2016 will be installed or change the installation path in order to suit your requirements.
    
    > [!TIP:]
      
6. Click **Install Now**.
    
  
7. When Setup finishes, a dialog box prompts you to run the **SharePoint Products Configuration Wizard**. You can start the wizard immediately or from the Windows command prompt later.
    
  

## Add the new SharePoint server to the farm
<a name="addserver"> </a>

You add the new server to the farm by using one of the following procedures:
-  [To add a server by using the SharePoint Products Configuration Wizard](#addserverconfigwiz)
    
  
-  [To add a new SharePoint Server 2016 server to the farm by using the PSConfig.exe command-line tool](#psconfig)
    
  
-  [To add a server by using Windows PowerShell](#addserverpowershell)
    
  
 **To add a new SharePoint Server 2016 server to the farm by using the SharePoint Products Configuration Wizard**
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see  [Initial deployment administrative and service accounts in SharePoint Server](html/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
  
2. Start the **SharePoint 2016 Products Configuration Wizard**.
    
  - For Windows Server 2012 R2:
    
  - On the new server, on the **Start** screen, click **SharePoint 2016 Products Configuration Wizard**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012 R2 and Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
  
4. On the **Connect to a server farm** page, click **Connect to an existing server farm.**
    
  
5. Click **Next**.
    
  
6. On the **Specify Configuration Database settings** page, type the name of the instance of SQL Server in the **Database server** box, and then click **Retrieve Database Names**.
    
  
7. Select the name of the configuration database in the **Database name** list, and then click **Next**.
    
  
8. On the **Specify Farm Security Settings** page, type the name of the farm passphrase in the **Passphrase** box, and then click **Next**.
    
  
9. On the **Specify Server Role** page, choose the appropriate role, and then click **Next**.
    
    > [!NOTE:]
      
10. On the **Completing the SharePoint Products Configuration Wizard** page, click **Next**.
    
  
11. On the server that hosts Central Administration, click **Manage servers in this farm** to verify that the new server is part of the farm.
    
    > [!NOTE:]
      
12. On the **Servers in Farm** page, click the name of the new server. Use the list of available services on the **Services on Server** page to start the services that you want to run on the new server.
    
    > [!NOTE:]
      
 **To add a new SharePoint Server 2016 server to the farm by using the PSConfig.exe command-line tool**
1. To create a farm by using the PSConfig.exe command-line tool, use the following syntax:
    
  ```
  
psconfig.exe -cmd configdb -connect -server <SqlServerName> -database <ConfigDbName> -user <DOMAIN\\FarmServiceAccount> -password <FarmServiceAccountPassword> -passphrase <FarmPassphrase> -admincontentdatabase <AdminContentDbName> -localserverrole <ServerRole> -cmd helpcollections -installall -cmd secureresources -cmd services -install -cmd installfeatures -cmd adminvs -provision -port <PortNumber> -windowsauthprovider onlyusentlm -cmd applicationcontent -install
  ```


    Where <ServerRole> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom.
    
    > [!NOTE:]
      

    > [!NOTE:]
      
 **To add a new SharePoint Server 2016 server to the farm by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012 R2 and Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
3. At the PowerShell command prompt, type the following command to connect the server to a configuration database: 
    
  ```
  
Connect-SPConfigurationDatabase -DatabaseServer <SqlServerName> -DatabaseName <ConfigDbName> -Passphrase <FarmPassphrase>  -LocalServerRole <ServerRole>
  ```


    Where:
    
  -  *<$DatabaseServer>*  is the name of the server that hosts the configuration database
    
  
  -  *<DatabaseName>*  is the name of the configuration database
    
  
  -  *<$Passphrase>*  is the passphrase for the farm
    
  
  -  *<ServerRole>*  is the server role type
    
    Where <ServerRole> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom. 
    
    > [!NOTE:]
      
4. At the PowerShell command prompt, type the following command to install the Help File Collections:
    
  ```
  
Install-SPHelpCollection -All
  ```

5. At the PowerShell command prompt, type the following command to install the Security Resource for SharePoint Server 2016:
    
  ```
  Initialize-SPResourceSecurity
  ```

6. At the PowerShell command prompt, type the following command to install the basic services: 
    
  ```
  Install-SPService
  ```

7. At the PowerShell command prompt, type the following command to install all the features:
    
  ```
  Install-SPFeature -AllExistingFeatures
  ```

8. At the PowerShell command prompt, type the following command to set the port number of the SharePoint Central Administration website:
    
  ```
  New-SPCentralAdministration -Port <PortNumber> -WindowsAuthProvider NTLM
  ```


    > [!NOTE:]
      
9. At the PowerShell command prompt, type the following command to install application content:
    
  ```
  
Install-SPApplicationContent
  ```

10. At the PowerShell command prompt, type the following command to get a list of servers in the farm. 
    
  ```
  Get-SPServer
  ```


    > [!NOTE:]
      

