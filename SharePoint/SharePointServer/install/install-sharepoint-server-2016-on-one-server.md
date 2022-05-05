---
title: "Install SharePoint Servers 2016 or 2019 on one server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 07/24/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid: 356d3a0b-fc26-455c-9afb-6d2ffdceef84
description: "Learn how to install SharePoint Server on a single server."
---

# Install SharePoint Servers 2016 or 2019 on one server

[!INCLUDE[appliesto-xxx-2016-2019-xxx-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-xxx-md.md)] 
  
 You can install and configure SharePoint Servers 2016 or 2019 on a single server if you are hosting only a few sites for a limited number of users or if you want to create a trial or development environment. This configuration is also useful if you want to configure a farm to meet your needs first, and then add servers to the farm at a later stage. 
  
> [!NOTE]
> In previous versions of SharePoint, a single server installation automatically installed SQL Server Express. In SharePoint Servers 2016 and 2019, a single server installation contains only SharePoint. SQL Server can be installed on the same server or on a separate server; both scenarios are supported. For better performance we recommend installing SQL Server on a separate server. 
  
    
## Overview
<a name="section1"> </a>

After you have completed setup and the SharePoint Products Configuration Wizard, you will have installed binaries, configured security permissions, configured registry settings, configured the configuration database, configured the content database, and installed the SharePoint Central Administration web site. Next, you can choose to run the Farm Configuration Wizard to configure the farm, select the services that you want to use in the farm, and create the first site collection, or you can manually perform the farm configuration at your own pace.
  
## Before you install SharePoint Servers 2016 or 2019 on a single server
<a name="section2"> </a>

Before you begin to install and configure SharePoint Servers 2016 or 2019, do the following:
  
- For SharePoint Server 2016, ensure that you have met all hardware and software requirements. You must have a 64-bit version of Windows Server 2012 R2. To host SharePoint databases, you must also have a 64-bit version of SQL Server 2014 SP1. For more information about these requirements, such as specific updates that you must install, see [Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md).

- For SharePoint Server 2019, ensure that you have met all hardware and software requirements. You must have a 64-bit version of Windows Server 2016. To host SharePoint databases, you must also have a 64-bit version of SQL Server 2016 or 2017. For more information about these requirements, such as specific updates that you must install, see [Hardware and software requirements for SharePoint Server 2019](hardware-and-software-requirements-2019.md).
    
- Ensure that you perform a clean installation of SharePoint Servers 2016 or 2019.
    
- Ensure that you are prepared to set up the required accounts by using appropriate permissions. For detailed information, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
- Ensure the Max degree of parallelism is set to 1. For additional information about max degree of parallelism see, [Configure the max degree of parallelism Server Configuration Option](/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option).
    
 **Security note**: As a security best practice, we recommend that you install SharePoint Servers 2016 or 2019 by using least-privilege administration. 
  
> [!TIP]
> If you decide to install prerequisites manually, you can still run the Microsoft SharePoint Products Preparation Tool to verify which prerequisites are required on each server. 
  
## Install SharePoint Servers 2016 or 2019 on a single server
<a name="section3"> </a>

To install and configure SharePoint Server 2016 or 2019 on a single server, you will follow these steps:
  
1. Run the **Microsoft SharePoint Products and Technologies Preparation Tool,** which installs all prerequisites to use SharePoint Server. 
    
2. Run Setup, which installs binaries, configures security permissions, and edits registry settings for SharePoint Servers 2016 or 2019.
    
3. Run SharePoint Products Configuration Wizard, which installs and configures the configuration database, installs and configures the content database, and installs the SharePoint Central Administration web site.
    
4. Configure browser settings.
    
5. Run the Farm Configuration Wizard, which configures the farm, creates the first site collection, and selects the services that you want to use in the farm.
    
6. Perform post-installation steps.
    
> [!IMPORTANT]
> To complete the following procedures, the account that you use must be a member of the Administrators group on the computer on which you are installing SharePoint Server. For information about user accounts, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md). 
  
### Run the Microsoft SharePoint Products Preparation Tool

Because the prerequisite installer downloads components from the Microsoft Download Center, you must have Internet access on the computer on which you are running the installer. Use the following procedure to install software prerequisites for SharePoint Servers 2016 or 2019.
  
 **To run the Microsoft SharePoint Products Preparation Tool**
  
1. Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. In the SharePoint Server installation disc image software, mount the ISO file, and click the splash.hta file. The SharePoint Server splash screen is displayed.
    
3. Click **Install software prerequisites**. 
    
4. On the **Welcome to the SharePoint Products Preparation Tool** page, click **Next**.
    
5. On the **License Terms for software products** page, review the terms, select the **I accept the terms of the License Agreement(s)** check box, and then click **Next**.
    
6. On the **Your system needs to restart to continue** page, click **Finish** to restart the computer. 
    
7. Repeat steps 2-4.
    
8. On the **Installation Complete** page, click **Finish**.
    
### Run Setup

The following procedure installs binaries, configures security permissions, and edits registry settings for SharePoint Server. At the end of Setup, you can choose to start the SharePoint Products Configuration Wizard, which is described later in this section.
  
 **To run Setup**
  
1. Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. On the **SharePoint Server Start** page, click **Install SharePoint Server**.
    
3. On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.
    
4. On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.
    
5. Optional: To install SharePoint Server at a custom location, or to store search index files at a custom location, click the **File Location** tab, and then either type the custom location or click **Browse** to find the custom location. 
    
    > [!NOTE]
    > If you intend to use this computer as a search server, we recommend that you store the search index files on a separate storage volume or partition. Any other search data that needs to be stored is stored in the same location as the search index files. You can only set this location at installation time. 
  
6. Click **Install Now**.
    
7. When Setup finishes, a dialog prompts you to complete the configuration of your server. Ensure that the **Run the SharePoint Products Configuration Wizard now** check box is selected. 
    
8. Click **Close** to start the configuration wizard. 
    
> [!NOTE]
> If Setup fails, check log files in the Temp folder of the user account you used to run Setup. Ensure that you are logged in using the same user account and then type %temp% in the location bar in Windows Explorer. If the path in Windows Explorer resolves to a location that ends in a "1" or "2", you have to navigate up one level to view the log files. The log file name is SharePoint Server Setup (<  _time stamp_>). 
  
### Run the SharePoint Products Configuration Wizard

Use the following procedure to install and configure the configuration database and the content database, and to install the SharePoint Central Administration website.
  
 **To run the SharePoint Products Configuration Wizard**
  
1. Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. If you have closed the SharePoint Products Configuration Wizard, you can access it by clicking **Start**, point to **All Apps**, click **Microsoft SharePoint Products**, and then click **SharePoint Products Configuration Wizard**. If the **User Account Control** dialog appears, click **Continue**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. In the dialog that notifies you that some services might have to be restarted during configuration, click **Yes**.
    
5. On the **Connect to a server farm** page, click **Create a new server farm**, and then click **Next**.
    
6. On the **Specify Configuration Database Settings** page, do the following: 
    
1. In the **Database server** box, type the name of the computer that is running SQL Server. 
    
2. In the **Database name** box, type a name for your configuration database or use the default database name. The default name is SharePoint_Config. 
    
3. In the **Username** box, type the user name of the farm administrator service account. Ensure that you type the user name in the format DOMAIN\username. 
    
    **Security note**: The farm administrator service account is used to access your configuration database. It also acts as the application pool identity account for the SharePoint Central Administration application pool, and it is the account under which the Microsoft SharePoint Foundation Timer service runs. The SharePoint Products Configuration Wizard adds this account to the SQL Server Login accounts, the SQL Server **dbcreator** server role, and the SQL Server **securityadmin** server role. The user account that you specify as the farm administrator service account has to be a domain user account. However, it does not have to be a member of any specific security group on your SharePoint servers or your database servers. We recommend that you follow the principle of least-privilege and specify a user account that is not a member of the Administrators group on your SharePoint servers or your database servers. 
    
4. In the **Password** box, type the user password. 
    
7. Click **Next**.
    
8. On the **Specify Farm Security Settings** page, type a passphrase, and then click **Next**.
    
    Although a passphrase resembles a password, it is usually longer to improve security. It is used to encrypt credentials of accounts that are registered in SharePoint Server. For example, the SharePoint Server server farm administrator service account that you provide when you run the SharePoint Products Configuration Wizard. Ensure that you remember the passphrase, because you must use it every time that you add a server to the farm.
    
    Ensure that the passphrase meets the following criteria:
    
  - Contains at least eight characters
    
  - Contains at least three of the following four character groups:
    
  - English uppercase characters (from A through Z)
    
  - English lowercase characters (from a through z)
    
  - Numerals (from 0 through 9)
    
  - Nonalphabetic characters (such as !, $, #, %)
    
9. On the **Specify Server Role** page, choose the appropriate role, click **Next**.
    
    > [!NOTE]
    >  For a single server farm, we recommend choosing the **Single Server Farm** role, although you can select a **Custom** role if you want to individually manage the services instances that run on the server. You can change the role of a server later if you change your mind or want to expand your farm by adding additional servers. 
  
10. On the **Configure SharePoint Central Administration Web Application** page, do the following: 
    
  - Either select the **Specify port number** check box and type the port number that you want the SharePoint Central Administration web application to use, or leave the **Specify port number** check box cleared if you want to use the default port number. 
    
  - Click either **NTLM** or **Negotiate (Kerberos)**.
    
11. Click **Next**.
    
12. On the **Completing the SharePoint Products Configuration Wizard** page, review your configuration settings to verify that they are correct, and then click **Next**.
    
    > [!NOTE]
    > The **Advanced Settings** option is not available in SharePoint Servers 2016 and 2019. 
  
13. On the **Configuration Successful** page, click **Finish**. When the wizard closes, setup opens the web browser and connects to Central Administration.
    
    If the SharePoint Products Configuration Wizard fails, check the PSCDiagnostics log files, which are located on the drive on which SharePoint Servers 2016 and 2019 are installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder.
    
    If you are prompted for your user name and password, you might have to add the SharePoint Central Administration web site to the list of trusted sites and configure user authentication settings in Internet Explorer. You might also want to disable the Internet Explorer Enhanced Security settings. If you see a proxy server error message, you might have to configure proxy server settings so that local addresses bypass the proxy server. Instructions for configuring proxy server settings are provided in the following section. For more information about how to configure browser and proxy settings, see [Configure browser settings](install-sharepoint-server-2016-on-one-server.md#configurebrowser).
    
### Configure browser settings
<a name="configurebrowser"> </a>

After you run the SharePoint Products Configuration Wizard, you should confirm that SharePoint Server works correctly by configuring additional settings in Internet Explorer.
  
If you are not using Internet Explorer, you might have to configure additional settings for your browser. For information about supported browsers, see [Plan browser support in SharePoint Servers 2016 and 2019](browser-support-planning-2016-2019.md).
  
To confirm that you have configured browser settings correctly, log on to the server by using an account that has local administrative credentials. Next, connect to the SharePoint Central Administration web site. If you are prompted for your user name and password when you connect, perform the following procedures:
  
- Add the SharePoint Central Administration website to the list of trusted sites
    
- Disable Internet Explorer Enhanced Security settings
    
If you receive a proxy server error message, perform the following procedure:
  
- Configure proxy server settings to bypass the proxy server for local addresses
    
 **To add the SharePoint Central Administration website to the list of trusted sites**
  
1. Verify that the user account that completes this procedure has the following credentials:
    
  - The user account is a member of the Administrators group on the computer on which you are performing the procedure.
    
2. In Internet Explorer, on the **Tools** menu, click **Internet Options**.
    
3. On the **Security** tab, in the **Select a zone to view or change security settings** area, click **Trusted Sites**, and then click **Sites**.
    
4. Clear the **Require server verification (https:) for all sites in this zone** check box. 
    
5. In the **Add this web site to the zone** box, type the URL to your site, and then click **Add**.
    
6. Click **Close** to close the **Trusted Sites** dialog. 
    
7. Click **OK** to close the **Internet Options** dialog. 
    
 **To disable Internet Explorer Enhanced Security settings**
  
1. Verify that the user account that completes this procedure has the following credentials: 
    
  - The user account is a member of the Administrators group on the computer on which you are performing the procedure.
    
2. Click **Start**, point to **All Apps**, point to **Administrative Tools**, and then click **Server Manager**.
    
3. In **Server Manager**, select the root of **Server Manager**.
    
4. In the **Security Information** section, click **Configure IE ESC**.
    
    The **Internet Explorer Enhanced Security Configuration** dialog appears. 
    
5. In the **Administrators** section, click **Off** to disable the Internet Explorer Enhanced Security settings, and then click **OK**.
    
 **To configure proxy server settings to bypass the proxy server for local addresses**
  
1. Verify that the user account that completes this procedure has the following credentials: 
    
  - The user account is a member of the Administrators group on the computer on which you are performing the procedure.
    
2. In Internet Explorer, on the **Tools** menu, click **Internet Options**.
    
3. On the **Connections** tab, in the **Local Area Network (LAN) settings** area, click **LAN Settings**.
    
4. In the **Automatic configuration** area, clear the **Automatically detect settings** check box. 
    
5. In the **Proxy Server** area, click the **Use a proxy server for your LAN** check box. 
    
6. Type the address of the proxy server in the **Address** box. 
    
7. Type the port number of the proxy server in the **Port** box. 
    
8. Select the **Bypass proxy server for local addresses** check box. 
    
9. Click **OK** to close the **Local Area Network (LAN) Settings** dialog. 
    
10. Click **OK** to close the **Internet Options** dialog. 
    
### Run the Farm Configuration Wizard
<a name="configurebrowser"> </a>

You have now completed setup and the initial configuration of SharePoint Server. You have created the SharePoint Central Administration web site. You can now configure your farm and sites, and you can select services by using the Farm Configuration Wizard.
  
 **To run the Farm Configuration Wizard**
  
1. Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. On the SharePoint Central Administration home page, on the **Quick Launch**, click **Configuration Wizards**, and then click **Launch the Farm Configuration Wizard**.
    
3. On the **Help Make SharePoint Better** page, click one of the following options, and then click **OK**:
    
  - **Yes, I am willing to participate (Recommended.)**
    
  - **No, I don't want to participate.**
    
4. On the **Configure your SharePoint farm** page, next to **Yes, walk me through the configuration of my farm using this wizard**, click **Start the Wizard**.
    
5. On the **Service Applications and Services** page, in the **Service Account** section, click the service account option that you want to use to configure your services. 
    
    **Security note**: For security reasons, we recommend that you use a different account from the farm administrator account to configure services in the farm. 
    
    If you decide to use an existing managed account — that is, an account of which SharePoint Server 2016 is aware — make sure that you click that option before you continue.
    
6. In the **Services** section, review the services that you want to use in the farm, and then click **Next**.
  
7. On the **Create Site Collection** page, do the following: 
    
1. In the **Title and Description** section, in the **Title** box, type the name of your new site. 
    
2. Optional: In the **Description** box, type a description of what the site contains. 
    
3. In the **Web Site Address** section, select a URL path for the site. 
    
4. In the **Template Selection** section, in the **Select a template** list, select the template that you want to use for the top-level site in the site collection. 
    
    > [!NOTE]
    > To view a template or a description of a template, click any template in the **Select a template** list. 
  
8. Click **OK**.
    
9. On the **Configure your SharePoint farm** page, review the summary of the farm configuration, and then click **Finish**.
    
## Post-installation steps
<a name="section4"> </a>

After you install and configure SharePoint Server, your browser window opens to the Central Administration web site of your new SharePoint site. Although you can start adding content to the site or customizing the site, we recommend that you first perform the following administrative tasks.
  
- **Configure usage and health data collection** You can configure usage and health data collection in your server farm. The system writes usage and health data to the logging folder and to the logging database. 
    
- **Configure diagnostic logging** You can configure diagnostic logging that might be required after initial installation or upgrade. The default settings are sufficient for most situations. Depending upon the business needs and life-cycle of the farm, you might want to change these settings. 
    
- **Configure incoming e-mail** You can configure incoming e-mail so that SharePoint sites accept and archive incoming e-mail. You can also configure incoming e-mail so that SharePoint sites can archive e-mail discussions as they occur, save e-mailed documents, and show e-mailed meetings on site calendars. In addition, you can configure the SharePoint Directory Management Service to provide support for e-mail distribution list creation and administration. 
    
- **Configure outgoing email** You can configure outgoing email so that your Simple Mail Transfer Protocol (SMTP) server sends email alerts to site users and notifications to site administrators. You can configure both the "From" email address and the "Reply" email address that appear in outgoing alerts. 
    
- **Configure Search settings** You can configure Search settings to crawl the content in SharePoint Server. 
