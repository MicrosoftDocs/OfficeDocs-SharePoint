---
title: "Install SharePoint 2013 on a single server with a built-in database"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/27/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6e2bcaab-58d3-47cb-b97e-34548732dfb8
description: "Learn how to install SharePoint with a built-in database on a single server."
---

# Install SharePoint 2013 on a single server with a built-in database

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
You can quickly publish a SharePoint site by deploying SharePoint 2013 on a single server that has a built-in database. This configuration is useful if you want to evaluate SharePoint 2013 features and capabilities, such as collaboration, document management, and search. This configuration is also useful if you are deploying only a few websites and you want to minimize administrative overhead.
  
This article contains required information and procedures to install and configure SharePoint 2013 with a built-in database on a single server.
  
    
> [!IMPORTANT]
> The steps in this article apply to SharePoint Foundation 2013 and SharePoint Server 2013. The procedures in this topic install Microsoft SQL Server 2008 R2 SP1 Express Edition. However, User Profile synchronization does not work with the Express Edition. If you intend to use User Profile synchronization withSharePoint Server 2013, you must choose a different installation scenario. 
  
## Overview
<a name="section1"> </a>

When you deploy SharePoint 2013 on a single server that has a built-in database by using the default settings, Setup installs Microsoft SQL Server 2008 R2 SP1 Express Edition and the SharePoint product. The SharePoint Products Configuration Wizard creates the configuration database and content database for the SharePoint sites. Additionally, the SharePoint Products Configuration Wizard installs the SharePoint Central Administration website and creates your first SharePoint site collection.
  
> [!NOTE]
> This article does not describe how to install SharePoint 2013 in a farm environment, or how to upgrade from previous releases of SharePoint 2013. For more information about how to install SharePoint 2013 on a single-server farm, see [Install SharePoint 2013 on a single server with SQL Server](single-server-with-sql-server.md). For more information about how to install SharePoint 2013 on a multiple server farm, see [Install SharePoint 2013 across multiple servers for a three-tier farm](multiple-servers-for-a-three-tier-farm.md). For more information about upgrade, see [Upgrade from SharePoint 2010 to SharePoint 2013](../upgrade-and-update/upgrade-from-sharepoint-2010-to-sharepoint-2013.md). 
  
> [!NOTE]
> The Distributed Cache service gives you a complete social computing experience. For more information about the Distributed Cache service, see [Overview of microblog features, feeds, and the Distributed Cache service in SharePoint Server](/sharepoint/administration/administration), [Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md), [Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md), and [What's new in authentication for SharePoint Server 2013](/SharePoint/what-s-new/new-and-improved-features-in-sharepoint-server-2016)
  
Consider the following restrictions of this method of installation:
  
- You cannot use this method on a domain controller or in a workgroup environment.
    
- This method is not supported for production on a domain controller.
    
- If your computer is in a workgroup, you cannot install AppFabric for Windows Server.
    
- A Microsoft SQL Server 2008 R2 SP1 Express Edition database cannot be larger than 10 GB.
    
- You cannot use user profile synchronization in this type of installation. If you want to use user profile synchronization, you must use a server farm installation of SharePoint 2013. For more information, see [Install SharePoint 2013 on a single server with SQL Server](single-server-with-sql-server.md) or [Install SharePoint 2013 across multiple servers for a three-tier farm](multiple-servers-for-a-three-tier-farm.md), and [Synchronize user and group profiles in SharePoint Server 2013](../administration/configure-profile-synchronization.md).
    
## Before you begin
<a name="section2"> </a>

Before you begin installation, make sure that you have met all hardware and software requirements. For more information, see [Hardware and software requirements for SharePoint 2013](hardware-and-software-requirements-0.md). To make sure that you perform a clean installation of SharePoint 2013, you must first remove any earlier version of SharePoint 2013 and any pre-release prerequisites if installed.
  
## Install SharePoint 2013
<a name="section3"> </a>

To install and configure SharePoint 2013, follow these steps:
  
1. Run the Microsoft SharePoint Products Preparation Tool.
    
2. Run Setup, which installs Microsoft SQL Server 2008 R2 SP1 Express Edition and the SharePoint product.
    
3. Run the SharePoint Products Configuration Wizard, which installs and configures the configuration database, the content database, and installs the SharePoint Central Administration website. This wizard also creates your first SharePoint site collection.
    
4. Configure browser settings.
    
5. Perform post-installation steps.
    
> [!IMPORTANT]
> To complete the following procedures, you must be a member of the Administrators group on the computer on which you are installing SharePoint 2013. 
  
### Run the Microsoft SharePoint Products Preparation Tool

Because the prerequisite installer downloads components from the Microsoft Download Center, you must have Internet access on the computer on which you are running the installer. Use the following procedure to install software prerequisites for SharePoint 2013.
  
 **To run the Microsoft SharePoint Products Preparation Tool**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. In the folder where you downloaded the SharePoint 2013 software, locate and then run **prerequisiteinstaller.exe**.
    
3. On the **Welcome to the Microsoft SharePoint Products Preparation Tool** page, click **Next**.
    
4. On the **License Terms for software products** page, review the terms, select the **I accept the terms of the License Agreement(s)** check box, and then click **Next**.
    
5. On the **Installation Complete** page, click **Finish**.
    
6. After you complete the Microsoft SharePoint Products Preparation Tool, you must also install the following:
    
  - [KB 2554876](https://go.microsoft.com/fwlink/p/?LinkId=254221)
    
  - [KB 2708075](https://go.microsoft.com/fwlink/p/?LinkID=254222)
    
  - [KB 2759112](https://go.microsoft.com/fwlink/p/?LinkId=267536)
    
  - [KB 2765317](https://go.microsoft.com/fwlink/p/?LinkID=268725)
    
### Run Setup

The following procedure installs Microsoft SQL Server 2008 R2 SP1 Express Edition and the SharePoint product. At the end of Setup, you can choose to start the SharePoint Products Configuration Wizard, which is described later in this section.
  
 **To run Setup**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. On the **SharePoint Server 2013 or SharePoint Foundation 2013 Start** page, click **Install SharePoint Server** or **Install SharePoint Foundation**.
    
3. On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.
    
4. On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.
    
5. On the **Server Type** tab, click **Standalone**.
    
6. When Setup finishes, a dialog box prompts you to complete the configuration of your server. Ensure that the **Run the SharePoint Products Configuration Wizard now** check box is selected. 
    
7. Click **Close** to start the configuration wizard. 
    
    > [!NOTE]
    > If Setup fails, check log files in the Temp folder of the user account that you used to run Setup. Ensure that you are logged in using the same user account, and then type %temp% in the location bar in Windows Explorer. If the path in Windows Explorer resolves to a location that ends in a "1" or "2", you will have to navigate up one level to view the log files. The log file name is SharePoint Server Setup (<  _time stamp_>). 
  
### Run the SharePoint Products Configuration Wizard

Use the following procedure to install and configure the configuration database and the content database, and install the SharePoint Central Administration website. 
  
 **To run the SharePoint Products Configuration Wizard**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. If you have closed the SharePoint Products Configuration Wizard, you can access it by clicking **Start**, point to **All Programs**, click **SharePoint 2013 Products**, and then click **SharePoint 2013 Products Configuration Wizard**. If the **User Account Control** dialog box appears, click **Continue**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. In the dialog box that notifies you that some services might have to be restarted during configuration, click **Yes**.
    
5. On the **Configuration Successful** page, click **Finish**.
    
    > [!NOTE]
    > If the SharePoint Products Configuration Wizard fails, check the PSCDiagnostics log files, which are located on the drive on which SharePoint 2013 is installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS folder. 
  
6. On the **Template Selection** page, select one of the following options, and then click **OK**:
    
  - In the **Template Selection** section, click a predefined template. 
    
  - In the **Solutions Gallery** section, click **Solutions Gallery**, and customize your own site template.
    
7. On the **Set Up Groups for this Site** page, specify who should have access to your site, and then either create a new group or use an existing group for these users by doing one of the following: 
    
  - To create a new group, click **Create a new group**, and then type the name of the group and the members that you want to be part of this group.
    
  - To use an existing group, click **Use an existing group**, and then select the user group in the **Item** list. 
    
8. Click **OK**.
    
> [!NOTE]
> If you are prompted for your user name and password, you might have to add the SharePoint Central Administration website to the list of trusted sites and configure user authentication settings in Internet Explorer. You might also want to disable the Internet Explorer Enhanced Security settings. If you see a proxy server error message, you might have to configure proxy server settings so that local addresses bypass the proxy server. For more information about how to configure browser and proxy settings, see [Install SharePoint 2013 on a single server with a built-in database](/previous-versions/office/sharepoint-server-2010/cc263202(v=office.14)#configurebrowser). 
  
### Configure browser settings
<a name="configurebrowser"> </a>

After you run the SharePoint Products Configuration Wizard, you should confirm that SharePoint 2013 works correctly by configuring additional settings in Internet Explorer.
  
If you are not using Internet Explorer, you might have to configure additional settings for your browser. For information about supported browsers, see [Plan browser support in SharePoint 2013](browser-support-planning.md).
  
To confirm that you have configured browser settings correctly, log on to the server by using an account that has local administrative credentials. Next, connect to the SharePoint Central Administration website. If you are prompted for your user name and password when you connect, perform the following procedures:
  
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
    
6. Click **Close** to close the **Trusted Sites** dialog box. 
    
7. Click **OK** to close the **Internet Options** dialog box. 
    
 **To disable Internet Explorer Enhanced Security settings**
  
1. Verify that the user account that completes this procedure has the following credentials:
    
  - The user account is a member of the Administrators group on the computer on which you are performing the procedure.
    
2. Click **Start**, point to **All Programs**, point to **Administrative Tools**, and then click **Server Manager**.
    
3. In **Server Manager**, select the root of **Server Manager**.
    
4. In the **Security Information** section, click **Configure IE ESC**.
    
    The **Internet Explorer Enhanced Security Configuration** dialog box appears. 
    
5. In the **Administrators** section, click **Off** to disable the Internet Explorer Enhanced Security settings, and then click **OK**.
    
 **To configure proxy server settings to bypass the proxy server for local addresses**
  
1. Verify that the user account that completes this procedure has the following credentials:
    
  - The user account is a member of the Administrators group on the computer on which you are performing the procedure.
    
2. In Internet Explorer, on the **Tools** menu, click **Internet Options**.
    
3. On the **Connections** tab, in the **Local Area Network (LAN) settings** area, click **LAN Settings**.
    
4. In the **Automatic configuration** area, clear the **Automatically detect settings** check box. 
    
5. In the **Proxy Server** area, select the **Use a proxy server for your LAN** check box. 
    
6. Type the address of the proxy server in the **Address** box. 
    
7. Type the port number of the proxy server in the **Port** box. 
    
8. Select the **Bypass proxy server for local addresses** check box. 
    
9. Click **OK** to close the **Local Area Network (LAN) Settings** dialog box. 
    
10. Click **OK** to close the **Internet Options** dialog box. 
    
## Post-installation steps
<a name="section4"> </a>

After you install SharePoint 2013, your browser window opens to the SharePoint Central Administration website of your new SharePoint site. Although you can start to add content to the site or customize the site, we recommend that you first perform the following administrative tasks:
  
- **Configure usage and health data collection** You can configure usage and health data collection in your server farm. The system writes usage and health data to the logging folder and to the logging database. For more information, see [Configure usage and health data collection in SharePoint Server](../administration/configure-usage-and-health-data-collection.md).
    
- **Configure diagnostic logging** You can configure diagnostic logging that might be required after initial deployment or upgrade. The default settings are sufficient for most situations, but depending on the business needs and life cycle of the farm, you might want to change these settings. For more information, see [Configure diagnostic logging in SharePoint Server](../administration/configure-diagnostic-logging.md).
    
- **Configure incoming e-mail** You can configure incoming e-mail so that SharePoint sites accept and archive incoming e-mail. You can also configure incoming e-mail so that SharePoint sites can archive e-mail discussions as they occur, save e-mailed documents, and show e-mailed meetings on site calendars. In addition, you can configure the SharePoint Directory Management Service to provide support for e-mail distribution list creation and administration. For more information, see [Configure incoming email for a SharePoint Server farm](../administration/incoming-email-configuration.md).
    
- **Configure outgoing e-mail** You can configure outgoing e-mail so that your Simple Mail Transfer Protocol (SMTP) server sends e-mail alerts to site users and notifications to site administrators. You can configure both the "From" e-mail address and the "Reply" e-mail address that appear in outgoing alerts. For more information, see [Configure outgoing email for a SharePoint Server farm](../administration/outgoing-email-configuration.md).
    
- **Configure search settings** You can configure search settings to crawl the content in SharePoint 2013. 
    

