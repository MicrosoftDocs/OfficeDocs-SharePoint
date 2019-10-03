---
title: "Create the SharePoint 2013 farm for a database attach upgrade"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 7009bdd4-6745-49a3-a330-728d5985f584

description: "Create and configure a SharePoint 2013 farm so that you can upgrade databases from SharePoint 2010 products."
---

# Create the SharePoint 2013 farm for a database attach upgrade

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
When you upgrade from SharePoint 2010 Products to SharePoint 2013, you must use a database attach upgrade, which means that you upgrade only the content for your environment and not the configuration settings. Before you can upgrade the content, you must configure a new server or server farm by using SharePoint 2013. This article lists the items that you have to configure when you create that new environment.
  
**Phase 1 of the upgrade process: Create SharePoint 2013 farm**

![Stages in upgrade process for SharePoint 2013](../media/77510e88-3b41-4f68-ab89-53e11566efeb.png)
  
|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)|This is the first phase in the process to upgrade SharePoint 2010 Products data and sites to SharePoint 2013. The process includes the following phases that must be completed in order:  <br/> Create the SharePoint 2013 farm for a database attach upgrade  (this phase) Copy databases to the new farm for upgrade to SharePoint 2013Upgrade service applications to SharePoint 2013Upgrade content databases from SharePoint 2010 to SharePoint 2013Upgrade a site collection to SharePoint 2013For an overview of the whole process, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md) and the Upgrade Process model [Download the upgrade process model](https://go.microsoft.com/fwlink/p/?LinkId=255047)| .  <br/> |
   
> [!IMPORTANT]
>  Although this article applies to both SharePoint Foundation 2013 and SharePoint 2013, the following sections apply only to SharePoint 2013: >  The section explains how to export the encryption key for the User Profile service application. >  The section explains how to configure service applications, except for the Business Data Connectivity service application which applies to SharePoint Foundation 2013 and SharePoint 2013. 
  
**Watch the SharePoint 2013 Upgrade: Phase 1 video**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/08375e2a-bf70-44f9-b25e-569e4ac3e303?autoplay=false]
## Before you begin
<a name="begin"> </a>

Before you create the SharePoint 2013 farm, review the following information and take any recommended actions.
  
- Make sure that the hardware and software that you are using meets the requirements in [Hardware and software requirements for SharePoint 2013](../install/hardware-and-software-requirements-0.md).
    
- Make sure that you have appropriately planned your logical and physical architecture to support the features and functionality that you want in the SharePoint 2013 farm. 
    
- Ensure that you are prepared to set up the required accounts by using appropriate permissions. For detailed information, see [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
## Collect information and settings
<a name="Before"> </a>

Before you start to upgrade, you must collect information and settings about your existing environment. You have to know what is in your SharePoint 2010 Products environment before you can start to build your SharePoint 2013 environment. Gather information such as the following:
  
- Alternate access mappings
    
- Authentication providers and authentication modes that are being used
    
- Quota templates
    
- Managed paths
    
- Self-service site management settings
    
- Incoming and outgoing e-mail settings
    
- Customizations
    
You also have to turn off or remove services or components in the SharePoint 2010 Products environment that could cause errors in the upgrade process. The following services or components should be removed or stopped before you back up your databases:
  
- **Web Analytics** The architecture for the Web Analytics service application is different in SharePoint 2010 Products. The presence of SharePoint Server 2010 Web Analytics information in your content databases could cause an error during upgrade. Stop the Web Analytics service application before you back up the content databases. Features and web parts from Web Analytics in SharePoint Server 2010 will not exist in SharePoint 2013, even for a site collection in 2010 mode. Remove any Web Analytics web parts or features from SharePoint Server 2010 site collections before upgrade. 
    
    For more information about this change to Web Analytics, see [Changes from SharePoint 2010 to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff607742(v=office.14)).
    
- **PowerPoint Broadcast Sites** The Office Online have changed into a separate server product, Office Online Server, which can serve multiple SharePoint farms for viewing and editing documents. Because of this change, PowerPoint Broadcast sites cannot be upgraded to SharePoint 2013. For more information about how to install and use Office Online Server with SharePoint 2013, see [Deploy Office Web Apps (Installed on SharePoint 2010 Products)](/webappsserver/configure-office-web-apps-for-sharepoint-2013).
    
## Record the passphrase for the Secure Store service application
<a name="passphrase"> </a>

The Secure Store service application uses a passphrase to encrypt information. You have to know what this passphrase is so that you can use it in the new environment. Otherwise, you will not have access to the information in the Secure Store. If you do not know the passphrase, you can refresh the key, and then back up the Secure Store database. For more information, see [Working with encryption keys](/SharePoint/administration/configure-the-secure-store-service).
  
## Export the encryption key for the User Profile service application
<a name="ExportKey"> </a>

The User Profile Service service application requires an encryption key that is stored separately from the database and is needed if you want to upgrade the User Profile Sync database. You must export the Microsoft Identity Integration Server Key (MIIS) encryption key from your SharePoint Server 2010 environment. You will import this exported key to the SharePoint 2013 environment after you upgrade the User Profile service application databases. By default, the key is located on the server that is running SharePoint Server 2010 and that is hosting the Microsoft Forefront Identity Manager services in the following directory: < _root directory drive_>\Program Files\Microsoft Office Servers\14.0\Synchronization Service\Bin.
  
> [!IMPORTANT]
> This section applies only to SharePoint 2013, not SharePoint Foundation 2013. 
  
 **To export the encryption key for the User Profile service application**
  
1. Verify that you have the following memberships:
    
  - Administrators group on the server on which you are running the command.
    
2. Open the Command Prompt window, and then change to the following folder:
    
    %Program Files%\Microsoft Office Servers\14.0\Synchronization Service\Bin\
    
3. To export the key, type the following at the command prompt, and then press ENTER:
    
  ```
  miiskmu.exe
  ```

4. In the Microsoft Identity Integration Server Key Management Utility wizard, verify that **Export key** set is selected, and then click **Next**.
    
5. In the **Account Name** box, type the account name for the farm administrator. 
    
6. In the **Password** box, type the password for the farm administrator. 
    
7. In the **Domain** box, type the domain that contains the farm administrator account, and then click **Next**.
    
8. In the **Specify export file name and location** box, type or click browse to select the path and file name to use for the exported key, and then click **Next**.
    
    The key is exported as a file that has a .BIN file name extension.
    
9. Verify the information, and then click **Finish**.
    
    A message appears indicating that the key was successfully exported.
    
10. Click **Close** to close the Microsoft Identity Integration Server Key Management Utility. 
    
## Install SharePoint 2013 in a new environment
<a name="Install"> </a>

Before you can upgrade your databases, you must use SharePoint 2013 to configure a new server or server farm. The first step in creating your new environment is to install SharePoint 2013 or SharePoint Foundation 2013 and configure your new server or server farm. You must do the following: 
  
1. Run the Microsoft SharePoint Products Preparation Tool to install all required software.
    
2. Run Setup to install the product.
    
3. Install all language packs that you want in your environment.
    
    > [!NOTE]
    > For more information about how to install available language packs, see [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md). 
  
4. Run the SharePoint Products Configuration Wizard to configure your server or servers.
    
    > [!IMPORTANT]
    > Some service applications can be upgraded by using a service application database upgrade. If you want to upgrade these service applications by upgrading the service application databases, do not use the Farm Configuration Wizard to configure these service applications when you set up your new farm. 
  
For step-by-step instructions for these tasks, see [Install for SharePoint 2013](../install/install-for-sharepoint-2013.md).
  
## Configure service applications
<a name="configfarm"> </a>

You must create the service applications on your new farm before you upgrade your content databases. There are some service applications that can be upgraded from SharePoint 2010 Products to SharePoint 2013. The steps in [Install for SharePoint 2013](../install/install-for-sharepoint-2013.md) describe how to use the Farm Configuration Wizard to enable all service applications. However, you should not use the Farm Configuration Wizard to enable the service applications that you want to upgrade. 
  
The following service applications can be upgraded by performing a services database upgrade:
  
- Business Data Connectivity service 
    
- Managed Metadata service
    
- PerformancePoint services
    
- Search
    
- Secure Store service
    
- User Profile service
    
For an overview of how to upgrade these service applications, see [Services upgrade overview from SharePoint 2010 to SharePoint Server 2013](services-upgrade-overview-from-sharepoint-2010-to-sharepoint-server-2013.md). The steps that you must follow to upgrade these service application databases are included in the [Upgrade service applications to SharePoint 2013](upgrade-service-applications-to-sharepoint-2013.md) section. 
  
The following services in SharePoint 2013 also require additional steps to enable and configure when you upgrade:
  
- **Excel Services**
    
    You can use the Farm Configuration Wizard to enable this service, but you must make sure that you create all trusted data connections again. For more information, see [Configure Excel Services in SharePoint](/SharePoint/administration/configure-excel-services).
    
- **InfoPath Forms Service**
    
    This service is not part of the Farm Configuration Wizard. To use this service, use the **Configure InfoPath Forms Services** link on the **General Application Settings** page in Central Administration to configure it. To continue to use form templates from your previous environment, export all administrator-deployed form templates (.xsn files) and data connection files (.udcx files) from your SharePoint Server 2010 environment, and then import them to your new SharePoint 2013 environment. For more information, see [Configure InfoPath Forms Services (SharePoint Server 2010)](/previous-versions/office/sharepoint-server-2010/cc262263(v=office.14))
    
- **Office Web Apps**
    
    Office Online Server is a new stand-alone server product that delivers Office on the web functionality on your private network. You install and managed it separately from SharePoint 2013. It cannot be installed on the same server or virtual machine instance as SharePoint 2013. For more information, see [Deploy Office Web Apps Server 2013](/webappsserver/deploy-office-web-apps-server).
    
## Configure farm settings
<a name="configfarmsettings"> </a>

The next step in creating the new environment is to apply general farm settings. You must manually reapply configuration settings from your SharePoint 2010 Products farm, such as the following:
  
- Incoming and outgoing e-mail settings
    
    For more information, see [Configure incoming email for a SharePoint Server farm](../administration/incoming-email-configuration.md) and [Configure outgoing email for a SharePoint Server farm](../administration/outgoing-email-configuration.md).
    
- All farm-level security and permission settings, such as adding user or group accounts to the Farm Administrators group
    
- Blocked file types
    
    For more information, see [Types of files that cannot be added to a list or library](https://support.office.com/en-us/article/Types-of-files-that-cannot-be-added-to-a-list-or-library-30BE234D-E551-4C2A-8DE8-F8546FFBF5B3).
    
And you must configure all new farm-level settings that you want to use, such as the following:
  
- Usage and health data collection
    
    For more information, see [Configure usage and health data collection in SharePoint Server](../administration/configure-usage-and-health-data-collection.md).
    
- Diagnostic logging
    
    For more information, see [Configure diagnostic logging in SharePoint Server](../administration/configure-diagnostic-logging.md).
    
- Settings and schedules for timer jobs
    
> [!IMPORTANT]
> If you had disabled the Workflow Auto Cleanup timer job in your SharePoint 2010 Products environment, make sure that you disable this timer job in your new environment also. If this timer job is enabled in the new environment and disabled in the SharePoint 2010 Products environment, you might lose workflow associations when you upgrade. For more information about this timer job, see[Disable preservation of workflow history (SharePoint Server 2010)](https://go.microsoft.com/fwlink/?LinkId=403874)[Disable preservation of workflow history (SharePoint Server 2010)](/previous-versions/office/sharepoint-server-2010/ee662522(v=office.14)). 
  
In a standard installation, the next step would be to create web applications. However, for upgrade, you create web applications later in the process, after you upgrade the service application databases. For more information, see [Create web applications](upgrade-content-databases.md#CreateWebApps).
  
|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)| This is the first phase in the process to upgrade SharePoint 2010 Products data and sites to SharePoint 2013.  <br/>  Next phase: [Copy databases to the new farm for upgrade to SharePoint 2013](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-2013.md) <br/>  For an overview of the whole process, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md).  <br/> |
   
## See also
<a name="configfarmsettings"> </a>

#### Other Resources

[Checklist for database-attach upgrade (SharePoint 2013)](checklist-for-database-attach-upgrade-sharepoint-2013.md)
  
[Upgrade farms that share services (parent and child farms) to SharePoint 2013](upgrade-farms-that-share-services-parent-and-child-farmsto-sharepoint-2013.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)

