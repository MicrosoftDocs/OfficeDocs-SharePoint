---
title: "Install SharePoint Servers 2016 or 2019 across multiple servers"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Critical
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid: 4982a861-ad5c-43e4-a49f-958afd4370aa
description: "Learn how to install SharePoint Servers to create a SharePoint server farm."
---

# Install SharePoint Servers 2016 or 2019 across multiple servers

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
The deployment sequence and configurations that are described in this article are based on recommended best practices. While the farm configuration is not complex, it provides a fundamental infrastructure to implement a SharePoint Server solution on similar — or more complex farms.
  
    
## Overview
<a name="Overview"> </a>

The basic steps in this deployment are as follows:
  
- Ensure that you have done all the planning and preparatory work, such as verifying hardware and software requirements.
    
- Install the required software updates on all servers that will be part of the farm.
    
- Install the SharePoint Server prerequisites on SharePoint servers.
    
- Install SharePoint Server on the SharePoint servers.
    
- Create and configure the SharePoint farm.
    
- Provision services.
    
- Complete post-deployment tasks as required.
    
### Topology overview

SharePoint Servers 2016 and 2019 support a new farm topology design called MinRole. This article will describe a simple multi-server farm topology with one server assigned to each MinRole server role. However, to take advantage of zero downtime patching, your farm topology must support high availability (HA) by having multiple servers assigned to each MinRole server role.
  
For additional information about MinRole, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](overview-of-minrole-server-roles-in-sharepoint-server.md).
  
### Before you install SharePoint Server on multiple servers

Before you begin to install and configure SharePoint Servers 2016 or 2019, do the following:
  
- Ensure that you are familiar with the operating-system guidelines described in [Performance Tuning Guidelines for Windows Server 2012 R2](https://msdn.microsoft.com/en-us/library/dn529133%28v=vs.85%29.aspx).
    
- Ensure that you have met all hardware and software requirements. For more information about these requirements, such as specific updates that you must install, see [Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md). For SharePoint Server 2019, see [Hardware and software requirements for SharePoint Server 2019](hardware-and-software-requirements-2019.md).
    
- Ensure that you perform a clean installation of SharePoint Server.
    
- Ensure that you are prepared to set up the required accounts by using appropriate permissions. For detailed information, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
#### Using the Microsoft SharePoint Products Preparation Tool

The Microsoft SharePoint Products Preparation Tool checks for the presence of prerequisites, and installs and configures all required programs. The Microsoft SharePoint Products Preparation Tool requires an Internet connection to download and configure SharePoint Server prerequisites. 
  
#### Database server

Ensure that SQL Server is updated to the required level and the TCP/IP protocol is enabled for the network configuration. 
  
Organizations whose database administrators operate independently from SharePoint administrators will have to make sure that the correct version of SQL Server is available and updated to the required level. In addition, you will have to request a DBA-created database. 
  
For additional information about DBA databases, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md), [Storage and SQL Server capacity planning and configuration (SharePoint Server)](../administration/storage-and-sql-server-capacity-planning-and-configuration.md).
  
Ensure the Max degree of parallelism is set to 1. For additional information about max degree of parallelism see, [Configure the max degree of parallelism Server Configuration Option](/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-2017).
  
#### Public updates and hotfix packages

Ensure that public updates and the required hotfix packages are installed for the operating system, SQL Server, and SharePoint Server. 
  
## Prepare the farm servers
<a name="PrepareServers"> </a>

Before you install SharePoint Server, you must check for and install all the prerequisites on the SharePoint servers by using the Microsoft SharePoint Products Preparation Tool.
  
> [!TIP]
> If you decide to install prerequisites manually, you can still run the Microsoft SharePoint Products Preparation Tool to verify which prerequisites are required on each server. 
  
Use the following procedure to install prerequisites on each server in the farm.
  
 **To run the Microsoft SharePoint Products Preparation Tool**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. In the SharePoint Server installation disc image, mount the ISO file, and then click the splash.hta file. The SharePoint Server 2016 splash screen is displayed..
    
3. Click **Install software prerequisites**. 
    
4. On the **Welcome to the SharePoint 2016 Products Preparation Tool** page, click **Next**.
    
    > [!NOTE]
    > The preparation tool may have to restart the local server to complete the installation of some prerequisites. The installer will continue to run after the server is restarted without manual intervention. However, you will have to log on to the server again. 
  
5. On the **License Terms for software products** page, review the terms, select the **I accept the terms of the License Agreement(s)** check box, and then click **Next**.
    
6. If you see the **Your system needs to restart to continue** page, click **Finish** to restart the computer, and then repeat steps 2-4. 
    
## Install SharePoint Server 2016 on the farm servers
<a name="InstallSP"> </a>

After the prerequisites are installed, follow these steps to install SharePoint Server 2016 on each farm server. 
  
The following procedure installs binaries, configures security permissions, and edits registry settings for SharePoint Server 2016. At the end of Setup, you can choose to start the SharePoint Products Configuration Wizard, which is described later in this article.
  
 **To run Setup**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. On the **SharePoint Server Start** page, click **Install SharePoint Server**.
    
3. On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.
    
4. On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.
    
5. Optional: To install SharePoint Server at a custom location, or to store search index files at a custom location, click the **File Location** tab, and then either type the custom location or click **Browse** to find the custom location. 
    
    > [!NOTE]
    > As a best practice, we recommend that you install SharePoint Server on a non-system drive. > If you intend to use this computer as a search server, we recommend that you store the search index files on a separate storage volume or partition. Any other search data that needs to be stored, is stored in the same location as the search index files. You can only set this location at installation time. 
  
6.  Click **Install Now**.
    
7. When the Setup program is finished, a dialog box prompts you to complete the configuration of your server. Clear the **Run the SharePoint Products and Technologies Configuration Wizard now** check box. 
    
    > [!NOTE]
    > For consistency of approach, we recommend that you do not run the configuration wizard until you have installed SharePoint Server 2016 on all SharePoint servers that will participate in the server farm. 
  
8. Click **Close** to finish Setup. 
    
## Create and configure the farm
<a name="CreateConfigure"> </a>

To configure the farm, you run the SharePoint Products Configuration Wizard. This wizard automates several configuration tasks, such as creating the configuration database, installing services, and creating the Central Administration website. We recommend that you run the SharePoint Products Configuration Wizard on the server that will host the SharePoint Central Administration website before you run the wizard on the other servers in the farm.
  
 **To run the SharePoint Products Configuration Wizard and configure the farm**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. On the server that will host Central Administration (the application server), click **Start**, point to **All Apps**, and then click **Microsoft SharePoint Products**, and then click **SharePoint Products Configuration Wizard**. If the **User Account Control** dialog box appears, click **Continue**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. In the dialog box that notifies you that some services might have to be restarted during configuration, click **Yes**.
    
5. On the **Connect to a server farm** page, click **Create a new server farm**, and then click **Next**.
    
6. On the **Specify Configuration Database Settings** page, do the following: 
    
1. In the **Database server** box, type the name of the computer that is running SQL Server. 
    
2. In the **Database name** box, type a name for your configuration database, or use the default database name. The default name is SharePoint_Config. 
    
3. In the **Username** box, type the user name of the server farm account in DOMAIN\user name format. 
    
    > [!IMPORTANT]
    > The server farm account is used to access your configuration database. It also acts as the application pool identity account for the SharePoint Central Administration application pool, and it is the account under which the SharePoint Timer service runs. The SharePoint Products Configuration Wizard adds this account to the SQL Server Login accounts, the SQL Server **dbcreator** server role, and the SQL Server **securityadmin** server role. The user account that you specify as the server farm account has to be a domain user account. However, it does not have to be a member of any specific security group on your SharePoint servers or your database servers. We recommend that you follow the principle of least-privilege, and specify a user account that is not a member of the Administrators group on your SharePoint servers or your database servers. 
  
4. In the **Password** box, type the user password. 
    
7. Click **Next**.
    
8. On the Specify Farm Security Settings page, type a passphrase, and then click **Next**.
    
    Although a passphrase resembles a password, it is usually longer to improve security. It is used to encrypt credentials of accounts that are registered in SharePoint Servers 2016 or 2019. For example, the SharePoint Server server farm account that you provide when you run the SharePoint Products Configuration Wizard. Ensure that you remember the passphrase, because you must use it every time that you add a server to the farm.
    
    Ensure that the passphrase meets the following criteria:
    
  - Contains at least eight characters
    
  - Contains at least three of the following four character groups:
    
  - English uppercase characters (from A through Z)
    
  - English lowercase characters (from a through z)
    
  - Numerals (from 0 through 9)
    
  - Nonalphabetic characters (such as !, $, #, %)
    
9. On the **Configure SharePoint Central Administration Web Application** page, do the following: 
    
1. Either select the **Specify port number** check box and type the port number that you want the SharePoint Central Administration web application to use, or leave the **Specify port number** check box cleared if you want to use the default port number. 
    
2. Click either **NTLM** or **Negotiate (Kerberos)**.
    
10. Click **Next**.
    
11. On the **Completing the SharePoint Products Configuration Wizard** page, review configuration settings, and then click **Next**.
    
12. On the **Configuration Successful** page, click **Finish**.
    
    > [!NOTE]
    > If the SharePoint Products Configuration Wizard fails, check the log files on the drive on which SharePoint Server 2016 is installed, which are located in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder. 
  
13. The Central Administration website will open in a new browser window.
    
    On the **Help Make SharePoint Better** page, click one of the following options and then click **OK**.
    
1. **Yes, I am willing to participate (Recommended).**
    
2. **No, I don't wish to participate.**
    
14. On the **Initial Farm Configuration Wizard** page, you have the option to use a wizard to configure services or you can decide to configure services manually. For the purpose of this article, we use the manual option. Click **Cancel**. 
    
    We recommend waiting until your SharePoint farm has at least one of each type of server role joined to it before you run the Farm Configuration Wizard.
    
    > [!IMPORTANT]
    > The Farm Configuration Wizard can't be used with DBA-created databases because the Farm Configuration Wizard will try to create its own databases. If you're using DBA-created databases, you must create each service application and web application manually so that you can specify the DBA-created database it should connect to. 
  
## Add SharePoint servers to the farm
<a name="AddWeb"> </a>

After you create the farm on the first server, you can add servers by following the same process described earlier in this topic for installing SharePoint Server on the server that hosts Central Administration. The only difference is that during the SharePoint Products Configuration Wizard, you choose to join an existing farm. Follow the wizard steps to join the farm.
  
For your content farm to be MinRole complaint, at a minimum you want to have at least one of each type of server role in the farm: **Application**, **Front-end**, **Distributed cache**, and **Search**. The order in which these roles are created does not matter. You can also combined roles by using shared roles. If you want to take full advantage of zero down time patching, then you need to make sure high availability is configured. 
  
For additional information about MinRole, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](overview-of-minrole-server-roles-in-sharepoint-server.md).
  
> [!NOTE]
> If this farm is not hosting Search services, then the Search role is not needed. 
  
For additional information about how to add servers to a farm, see [Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm](add-a-server-to-a-sharepoint-server-2016-farm.md). This article also provides detailed information for the steps in the following procedure.
  
## Post-installation steps
<a name="section4"> </a>

After you install and configure SharePoint Server, your browser window opens to the Central Administration web site of your new SharePoint site. Although you can start adding content to the site or customizing the site, we recommend that you first perform the following administrative tasks.
  
- **Configure usage and health data collection** You can configure usage and health data collection in your server farm. The system writes usage and health data to the logging folder and to the logging database. 
    
- **Configure diagnostic logging** You can configure diagnostic logging that might be required after initial installation or upgrade. The default settings are sufficient for most situations. Depending upon the business needs and life-cycle of the farm, you might want to change these settings. 
    
- **Configure incoming e-mail** You can configure incoming e-mail so that SharePoint sites accept and archive incoming e-mail. You can also configure incoming e-mail so that SharePoint sites can archive e-mail discussions as they occur, save e-mailed documents, and show e-mailed meetings on site calendars. In addition, you can configure the SharePoint Directory Management Service to provide support for e-mail distribution list creation and administration. 
    
- **Configure outgoing email** You can configure outgoing email so that your Simple Mail Transfer Protocol (SMTP) server sends email alerts to site users and notifications to site administrators. You can configure both the "From" email address and the "Reply" email address that appear in outgoing alerts. 
    
- **Configure Search settings** You can configure Search settings to crawl the content in SharePoint Servers 2016 or 2019. 
    

