---
title: "Create the SharePoint Server 2016 farm for a database attach upgrade"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/30/2016
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 99684f0b-f617-4c10-8420-d4d0adea3687
description: "Create and configure a SharePoint Server 2016 farm so that you can upgrade databases from SharePoint 2013."
---

# Create the SharePoint Server 2016 farm for a database attach upgrade

 
  
When you upgrade from SharePoint Server 2013 to SharePoint Server 2016, you must use a database attach upgrade, which means that you upgrade only the content for your environment and not the configuration settings. Before you can upgrade the content, you must configure a new server or server farm by using SharePoint Server 2016. This article lists the items that you have to configure when you create that new environment.
  
**Phase 1 of the upgrade process: Create SharePoint Server 2016 farm**

![Phase 1 of the upgrade process: Create SharePoint 20136 farm](../media/SP15Upgrade_UpgradePhase1.png)

|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)|This is the first phase in the process to upgrade SharePoint Server 2013 data and sites to SharePoint Server 2016. The process includes the following phases that must be completed in order:  <br/> Create the SharePoint Server 2016 farm for a database attach upgrade (this phase) <br/> Copy databases to the new farm for upgrade to SharePoint Server 2016<br/>Upgrade service applications to SharePoint Server 2016Upgrade content databases to SharePoint Server 2016<br/>For an overview of the whole process, see [Overview of the upgrade process to SharePoint Server 2016](overview-of-the-upgrade-process.md).<br/>|

For an overview of the whole process, see [Overview of the upgrade process to SharePoint Server 2016](overview-of-the-upgrade-process.md).
   
## Before you begin
<a name="begin"> </a>

Before you create the SharePoint Server 2016 farm, review the following information and take any recommended actions.
  
- Make sure that the hardware and software that you are using meets the requirements in [Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md).
    
- Make sure that you have appropriately planned your logical and physical architecture to support the features and functionality that you want in the SharePoint Server 2016 farm. 
    
- Make sure that you have planned for sufficient performance and capacity for the SharePoint Server 2016 farm. 
    
- Ensure that you are prepared to set up the required accounts by using appropriate permissions. For detailed information, see [Initial deployment administrative and service accounts in SharePoint Server](../install/initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
## Collect information and settings
<a name="Before"> </a>

> [!IMPORTANT]
>  The section explains how to configure service applications, except for the Business Data Connectivity service application which applies to SharePoint Server 2016. 
  
Before you start to upgrade, you must collect information and settings about your existing environment. You have to know what is in your SharePoint Server 2013 environment before you can start to build your SharePoint Server 2016 environment. Gather information such as the following:
  
- Alternate access mappings
    
- Authentication providers and authentication modes that are being used
    
- Quota templates
    
- Managed paths
    
- Self-service site management settings
    
- Incoming and outgoing e-mail settings
    
- Customizations
    
You also have to turn off or remove services or components in the SharePoint Server 2013 with Service Pack 1 (SP1) environment that could cause errors in the upgrade process. The following services or components should be removed or stopped before you back up your databases:
  
- **PowerPoint Broadcast Sites** Office Online Server has changed into a separate server product which can serve multiple SharePoint farms for viewing and editing documents. Because of this change, PowerPoint Broadcast sites cannot be upgraded to SharePoint Server 2016. 
    
## Record the passphrase for the Secure Store service application
<a name="passphrase"> </a>

The Secure Store service application uses a passphrase to encrypt information. You have to know what this passphrase is so that you can use it in the new environment. Otherwise, you will not have access to the information in the Secure Store. If you do not know the passphrase, you can refresh the key, and then back up the Secure Store database. For more information, see **Work with encryption keys** in [ Configure the Secure Store Service in SharePoint 2013 ](/SharePoint/administration/configure-the-secure-store-service).
  
## Install SharePoint Server 2016 in a new environment
<a name="Install"> </a>

Before you can upgrade your databases, you must use SharePoint Server 2016 to configure a new server or server farm. The first step in creating your new environment is to install SharePoint Server 2016 and configure your new server or server farm. You must do the following: 
  
1. Run the Microsoft SharePoint Products Preparation Tool to install all required software.
    
2. Run Setup to install the product.
    
3. Install all language packs that you want in your environment.
    
    > [!NOTE]
    > For more information about how to install available language packs, see [Install or uninstall language packs for SharePoint Server 2016](../install/install-or-uninstall-language-packs-0.md). 
  
4. Run the SharePoint Products Configuration Wizard to configure your server or servers.
    
    > [!IMPORTANT]
    > Some service applications can be upgraded by using a service application database upgrade. If you want to upgrade these service applications by upgrading the service application databases, do not use the Farm Configuration Wizard to configure these service applications when you set up your new farm. 
  
For step-by-step instructions for these tasks, see [Install SharePoint Server 2016](../install/install-for-sharepoint-server-2016.md).
  
## Configure service applications
<a name="configfarm"> </a>

You must create the service applications on your new farm before you upgrade your content databases. There are some service applications that can be upgraded from SharePoint Server 2013 to SharePoint Server 2016. The steps in [Install SharePoint Server 2016](../install/install-for-sharepoint-server-2016.md) describe how to use the Farm Configuration Wizard to enable all service applications. However, you should not use the Farm Configuration Wizard to enable the service applications that you want to upgrade. 
  
The following service applications can be upgraded by performing a services database upgrade:
  
- Business Data Connectivity service
    
- Managed Metadata service
    
- PerformancePoint services
    
- Search
    
- Secure Store service
    
- User Profile service
    
For an overview of how to upgrade these service applications, see [Services upgrade overview for SharePoint Server 2016](overview-of-the-services-upgrade-process.md). For the specific steps to upgrade these service application databases see [Upgrade service applications to SharePoint Server 2016](upgrade-service-applications-to-sharepoint-server-2016.md).
  
## Configure farm settings
<a name="configfarmsettings"> </a>

The next step in creating the new environment is to apply general farm settings. You must manually reapply configuration settings from your SharePoint Server 2013 farm, such as the following:
  
- Incoming and outgoing e-mail settings
    
- All farm-level security and permission settings, such as adding user or group accounts to the Farm Administrators group
    
- Blocked file types
    
And you must configure all new farm-level settings that you want to use, such as the following:
  
- Usage and health data collection
    
- Diagnostic logging
    
- Settings and schedules for timer jobs
    
> [!IMPORTANT]
> If you had disabled the Workflow Auto Cleanup timer job in your SharePoint Server 2013 environment, make sure that you disable this timer job in your new environment also. If this timer job is enabled in the new environment and disabled in the SharePoint Server 2013 environment, you might lose workflow associations when you upgrade. . 
  
In a standard installation, the next step would be to create web applications. However, for upgrade, you create web applications later in the process, after you upgrade the service application databases. For more information, see [Create web applications](upgrade-content-databases.md#CreateWebApps).
  
|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)| This is the first phase in the process to upgrade SharePoint Server 2013 data and sites to SharePoint Server 2016.  <br/>  Next phase: [Copy databases to the new farm for upgrade to SharePoint Server 2016](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-server-2016.md) <br/>  For an overview of the whole process, see [Overview of the upgrade process to SharePoint Server 2016](overview-of-the-upgrade-process.md).  <br/> |
   

