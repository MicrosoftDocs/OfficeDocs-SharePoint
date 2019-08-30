---
title: "Upgrade service applications to SharePoint 2013"
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
ms.assetid: 9d70eb7f-9e84-4960-87a1-fce3c46114f1

description: "Upgrade service applications (Business Connectivity Services, Managed Metadata, Secure Store, User Profiles, Search) to SharePoint 2013."
---

# Upgrade service applications to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
When you upgrade from SharePoint 2010 Products to SharePoint 2013, you must use a database attach upgrade, which means that you upgrade only the content for your environment and not the configuration settings. After you have configured the SharePoint 2013 environment, and copied the content and service application databases, you can upgrade the service applications to SharePoint 2013. This article contains the steps that you take to upgrade the service applications.
  
**Phase 3 of the upgrade process: Upgrade service applications**

![Stages in upgrade process for SharePoint 2013](../media/77510e88-3b41-4f68-ab89-53e11566efeb.png)
  
|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)|This is the third phase in the process to upgrade SharePoint 2010 Products data and sites to SharePoint 2013. The process includes the following phases that must be completed in order:  <br/> Create the SharePoint 2013 farm for a database attach upgradeCopy databases to the new farm for upgrade to SharePoint 2013Upgrade service applications to SharePoint 2013  (this phase) Upgrade content databases from SharePoint 2010 to SharePoint 2013Upgrade a site collection to SharePoint 2013For an overview of the whole process, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md) and the Upgrade Process model [Download the upgrade process model](https://go.microsoft.com/fwlink/p/?LinkId=255047).  <br/> |
   
> [!IMPORTANT]
> Although this article applies to both SharePoint Foundation 2013 and SharePoint 2013, the sections about how to upgrade service applications apply only to SharePoint 2013. (The exception is the section about how to upgrade the Business Data Connectivity service application which applies to SharePoint Foundation 2013 and SharePoint 2013). 
  
**Watch the SharePoint 2013 Upgrade: Phase 3 video**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/9651647c-a16e-4d0c-8b5b-2b323cb6133f?autoplay=false]
## Before you begin
<a name="begin"> </a>

Before you create the SharePoint 2013 farm, review the following information and take any recommended actions.
  
- Make sure that you have configured a SharePoint 2013 farm, recorded the Secure Store passphrase, and backed up the User Profile Synchronization encryption key. For more information, see [Create the SharePoint 2013 farm for a database attach upgrade](create-the-sharepoint-2013-farm-for-a-database-attach-upgrade.md).
    
- Make sure that the account that you use to perform the steps in this article is a member of the Farm administrators group in Central Administration.
    
- Decide which service application pool to use for the upgraded service applications. The procedures below use the default application pool for service applications which is "SharePoint Web Services Default". You can view a list of available service application pools by using the **Get-SPServiceApplicationPool** cmdlet in PowerShell. Or you can create a service application pool by using the **New-SPServiceApplicationPool** cmdlet. For more information, see [Get-SPServiceApplicationPool](/powershell/module/sharepoint-server/Get-SPServiceApplicationPool?view=sharepoint-ps) and [New-SPServiceApplicationPool](/powershell/module/sharepoint-server/New-SPServiceApplicationPool?view=sharepoint-ps).
    
> [!TIP]
> Throughout this article, variables (such as $applicationPool, $sss, $upa, and so on) are used in the PowerShell cmdlets to save time and effort. You do not have to use these variables if you would prefer not to. However, if you do not use these variables, you must use IDs for the service applications and service application proxies when you specify the **identity** parameters. Each procedure has information about the variables used, or the alternate cmdlets to use to look up any IDs that are required. > Also, many procedures in this article include a step to set the $applicationPool variable. If you are performing all of these procedures in the same session of PowerShell, and you want to use the same application pool for all service applications, you do not have to repeat this step in each procedure. Instead, you can set this variable once at the beginning and use it throughout the procedures in this article. 
  
## About upgrading the service application databases
<a name="UpgradeServicesDBs"> </a>

To upgrade a service application database, you create a new service application and provide the name of the existing database to use for the new service application. As the service application is created, the database is upgraded. This process has several steps.
  
1. Start the service instances
    
    The first step is to start service instances for the five service applications that you can upgrade: the Business Data Connectivity service, Managed Metadata Web Service, PerformancePoint Services service, Secure Store service, User Profile service, and Search service. Most of these service instances can be started from Central Administration. However the SharePoint Server Search service instance must be started by using PowerShell. 
    
2. Create the service applications and upgrade the databases
    
    After you have started the service instances, the next step is to create the service applications and upgrade the databases. You must use PowerShell to restore the service application databases. 
    
3. Create proxies for the service applications
    
    After you have upgraded the service application databases, you create the proxies for the service applications and add them to the default proxy group. You must create proxies for the following service applications:
    
  - Managed Metadata service application
    
  - Search service application
    
  - Secure Store service application
    
  - PerformancePoint Services service application
    
  - User Profile service application
    
    The Business Data Connectivity service application automatically creates a proxy and assigns it to the default proxy group when you create the service application.
    
4. Verify that the proxies are in the default group
    
The following sections provide procedures to complete these steps.
  
> [!NOTE]
> The Business Data Connectivity service application is available for upgrade both from SharePoint Foundation 2010 to SharePoint Foundation 2013 and SharePoint Server 2010 to SharePoint 2013. The other service applications are available for upgrade only from SharePoint Server 2010 to SharePoint 2013. Although SharePoint Foundation 2013 includes search functionality, it is not the same Search service application that is in SharePoint 2013 and it cannot be upgraded. 
  
## Start the service instances
<a name="StartServiceInstances"> </a>

The following procedures start the service instances.
  
 **To start service application instances from Central Administration**
  
1. Start the SharePoint Central Administration website.
    
2. In Central Administration, on the **Application Management** page, in the **Service Applications** section, click **Manage Services on Server**.
    
3. Next to the **Business Data Connectivity service**, click **Start**.
    
4. Next to the **Managed Metadata Web Service**, click **Start**.
    
5. Next to the **PerformancePoint Services service**, click **Start**.
    
6. Next to the **Secure Store Service**, click **Start**.
    
7. Next to the **User Profile Service**, click **Start**.
    
The Search service instance must be started by using PowerShell because you cannot start it from Central Administration unless a Search Service application already exists.
  
 **To start the Search service instance by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. .
    
3. To start the Search service instance, at the Microsoft PowerShell command prompt, type the following commands and press **ENTER** after each one: 
    
  ```
  $SearchInst = Get-SPEnterpriseSearchServiceInstance
  # Stores the identity for the Search service instance on this server as a variable 
  ```

  ```
  Start-SPServiceInstance $SearchInst
  # Starts the service instance
  ```

For more information, see Get-SPEnterpriseSearchServiceInstance and Start-SPServiceInstance. 
  
## Upgrade the Secure Store service application
<a name="UpgradeSecureStore"> </a>

To upgrade the Secure Store service application, you create the new service application and upgrade the database, create a proxy and add it to the default proxy group, and then restore the passphrase from the previous environment.
  
 **To upgrade the Secure Store service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

    Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. This is the default service application pool. You can specify a different service application pool. 
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the Secure Store service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $sss = New-SPSecureStoreServiceApplication -Name 'Secure Store' -ApplicationPool $applicationPool -DatabaseName 'SecureStore_Upgrade_DB' -AuditingEnabled
  ```

  Where:
    
  -  _SecureStore_ is the name that you want to give the new Secure Store service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _SecureStore_Upgrade_DB_ is the name of the service application database that you want to upgrade. 
    
   This command sets a variable, $sss, that you use when you create the proxy later.
    
   For more information, see [New-SPSecureStoreApplication](/powershell/module/sharepoint-server/New-SPSecureStoreApplication?view=sharepoint-ps). 
    
5. Type the following command to create a proxy for the Secure Store service application:
    
  ```
  $sssp = New-SPSecureStoreServiceApplicationProxy -Name ProxyName -ServiceApplication $sss -DefaultProxyGroup
  ```

  Where:
    
  -  _ProxyName_ is the proxy name that you want to use. 
    
  - $sss is the variable that you set earlier to identify the new Secure Store service application.
    
    > [!TIP]
    > If you do not use the variable $sss, then you must use an ID to identify the Secure Store service application instead of a name. To find the ID, you can run the **Get-SPServiceApplication** cmdlet to return a list of all service application IDs. 
  
  -  _DefaultProxyGroup_ adds the Secure Store service application proxy to the default proxy group for the local farm. 
    
   This command sets a variable, $sssp, for the service application proxy that you use when you restore the passphrase.
    
   For more information, see [New-SPSecureStoreServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPSecureStoreServiceApplicationProxy?view=sharepoint-ps).
    
   After you create the Secure Store service application and the proxy, you have to refresh the encryption key. For information about how to refresh the encryption key, see [Refresh the Secure Store encryption key](../administration/configure-the-secure-store-service.md#refresh).
    
6. Type the following command to restore the passphrase for the Secure Store service application:
    
  ```
  Update-SPSecureStoreApplicationServerKey -Passphrase <Passphrase> -ServiceApplicationProxy $sssp
  ```

  Where:
    
  -  _\<Passphrase\>_ is the Passphrase for the Secure Store service application from your previous environment. 
    
  - $sssp is a variable that you set earlier to identify the new Secure Store service application proxy.
    
    > [!TIP]
    > If you do not use the variable $sssp, then you must use an ID to identify the Secure Store service application proxy instead of a name. To find the ID, you can run the **Get-SPServiceApplicationProxy** cmdlet to return a list of all service application proxy IDs. 
  
    For more information, see [Update-SPSecureStoreApplicationServerKey](/powershell/module/sharepoint-server/Update-SPSecureStoreApplicationServerKey?view=sharepoint-ps).
    
## Upgrade the Business Data Connectivity service application
<a name="UpgradeBDC"> </a>

To upgrade the Business Data Connectivity service application, you create the new service application and upgrade the database. You do not have to create a proxy for the Business Data Connectivity service application. The Business Data Connectivity service application automatically creates a proxy and assigns it to the default proxy group when you create the service application.
  
> [!NOTE]
> The Business Data Connectivity service application is available in both SharePoint Foundation 2013 and SharePoint 2013. 
  
 **To upgrade the Business Data Connectivity service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

  Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. 
    
   This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the Business Data Connectivity service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  New-SPBusinessDataCatalogServiceApplication -Name 'BDC Service' -ApplicationPool $applicationPool -DatabaseName 'BDC_Service_DB'
  ```

  Where:
    
  -  _BDC Service_ is the name that you want to give the new Business Data Connectivity service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _BDC_Service_DB_ is name of the service application database that you want to upgrade. 
    
   For more information, see [New-SPBusinessDataCatalogServiceApplication](/powershell/module/sharepoint-server/New-SPBusinessDataCatalogServiceApplication?view=sharepoint-ps). 
    
## Upgrade the Managed Metadata service application
<a name="UpgradeMetadata"> </a>

To upgrade the Managed Metadata service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. You must upgrade the Managed Metadata service application before you can upgrade the User Profile service application.
  
 **To upgrade the Managed Metadata service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/New-SPBusinessDataCatalogServiceApplication?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

  Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. 
    
   This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the Managed Metadata service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $mms = New-SPMetadataServiceApplication -Name 'Managed Metadata Service Application' -ApplicationPool $applicationPool -DatabaseName 'Managed Metadata Service_DB'
  ```

  Where:
    
  -  _Managed Metadata Service Application_ is the name that you want to give the new Managed Metadata service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _Managed Metadata Service_DB_ is name of the service application database that you want to upgrade. 
    
   This command sets a variable, $mms, that you use when you create the proxy later.
    
   For more information, see [New-SPMetadataServiceApplication](/powershell/module/sharepoint-server/New-SPMetadataServiceApplication?view=sharepoint-ps). 
    
5. At the Microsoft PowerShell command prompt, type the following command to create a proxy for the Managed Metadata service application:
    
  ```
  New-SPMetadataServiceApplicationProxy -Name ProxyName -ServiceApplication $mms -DefaultProxyGroup
  ```

  Where:
    
  -  _ProxyName_ is the proxy name that you want to use. 
    
  - $mms is the variable that you set earlier to identify the new Managed Metadata service application.
    
    > [!TIP]
    > If you do not use the variable $mms, then you must use an ID to identify the Managed Metadata service application proxy instead of a name. To find the ID, you can run the **Get-SPServiceApplication** cmdlet to return a list of all service application IDs. 
  
  -  _DefaultProxyGroup_ adds the Managed Metadata service application proxy to the default proxy group for the local farm. 
    
   For more information, see [New-SPMetadataServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPMetadataServiceApplicationProxy?view=sharepoint-ps).
    
## Upgrade the User Profile service application
<a name="UpgradeProfiles"> </a>

To upgrade the User Profile service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group and then start the User Profile Synchronization service. After you have created the User Profile Service service application, you must import the Microsoft Identity Integration Server Key (MIIS) encryption key.
  
> [!NOTE]
> You must upgrade the Managed Metadata service application before you can upgrade the User Profile service application. 
  
 **To upgrade the User Profile service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

  Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. 
    
   This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the User Profile service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $upa = New-SPProfileServiceApplication -Name 'User Profile Service Application' -ApplicationPool $applicationPool -ProfileDBName 'User Profile Service Application_ProfileDB' -SocialDBName 'User Profile Service Application_SocialDB' 
  -ProfileSyncDBName 'User Profile Service Application_SyncDB'
  ```

  Where:
    
  -  _User Profile Service Application_ is the name that you want to give the new User Profile service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _User Profile Service Application_ProfileDB_ is name of the User Profile service application Profile database that you want to upgrade. 
    
  -  _User Profile Service Application_SocialDB_ is name of the User Profile service application Social database that you want to upgrade. 
    
  -  _User Profile Service Application_SyncDB_ is name of the User Profile service application Sync database that you want to upgrade. 
    
    > [!NOTE]
    > The **SocialDBName** and **ProfileSyncDBName** parameters are optional. Use these parameters if you have Social and Sync databases that you want to upgrade. If you do not specify these parameters, new Social and Sync databases are created for you. 
  
   This command sets a variable, $upa, that you use when you create the proxy later.
    
   For more information, see [New-SPProfileServiceApplication](/powershell/module/sharepoint-server/New-SPProfileServiceApplication?view=sharepoint-ps). 
    
5. Type the following command to create a proxy for the User Profile service application:
    
  ```
  New-SPProfileServiceApplicationProxy -Name ProxyName -ServiceApplication $upa -DefaultProxyGroup
  ```

    Where:
    
  -  _ProxyName_ is the proxy name that you want to use. 
    
  - $upa is the variable that you set earlier to identify the new User Profile service application.
    
    > [!TIP]
    > If you do not use the variable $upa, then you must use an ID to identify the User Profile service application instead of a name. To find the ID, you can run the **Get-SPServiceApplication** cmdlet to return a list of all service application IDs. 
  
  -  _DefaultProxyGroup_ adds the User Profile service application proxy to the default proxy group for the local farm. 
    
   For more information, see [New-SPProfileServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPProfileServiceApplicationProxy?view=sharepoint-ps).
    
After you have created the User Profile Service service application, you can start the User Profile Synchronization service.
  
 **Start the User Profile Synchronization service**
  
1. Start the SharePoint Central Administration website.
    
2. In Central Administration, on the **System Settings** page, under Servers click **Manage services on Server**.
    
3. Next to the User Profile Synchronization Service, click **Start**.
    
4. In the **Select the User Profile Application** section, select the User Profile service application that you upgraded. 
    
5. In the **Service Account Name and Password**section, type the account name and password to use for the User Profile Synchronization service.
    
After you have started the User Profile Synchronization service, you must import the Microsoft Identity Integration Server Key (MIIS) encryption key. Import this key to the following directory: < _root directory drive_>\Program Files\Microsoft Office Servers\15.0\Synchronization Service\Bin.
  
 **To import the encryption key for User Profile service application**
  
1. Verify that you have the following memberships:
    
  - Administrators group on the server on which you are running the command.
    
2. Open the Command Prompt window, and then change to the following folder:
    
    %Program Files%\Microsoft Office Servers\15.0\Synchronization Service\Bin\
    
3. To import the key, type the following at the command prompt, and then press ENTER:
    
  ```
  miiskmu.exe /i Path {0E19E162-827E-4077-82D4-E6ABD531636E}
  ```

  Where:
    
  -  _Path_ is the path and file name for the key that you want to import. 
    
   You might also have to enter a user name and password. These are the credentials for the farm administrator.
    
> [!IMPORTANT]
> Use the GUID as specified. This GUID is fixed. 
  
For more information, see [Install a software update (SharePoint Server 2010)](/SharePoint/upgrade-and-update/install-a-software-update).
  
## Upgrade the PerformancePoint Services service application
<a name="UpgradePPS"> </a>

To upgrade the PerformancePoint Services service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. 
  
 **To upgrade the PerformancePoint Services service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

  Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. 
    
   This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the PerformancePoint Services service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $pps = New-SPPerformancePointServiceApplication -Name 'PerformancePoint Service' -ApplicationPool $applicationPool -DatabaseName 'PerformancePoint Service Application_DB'
  ```

    Where:
    
  -  _PerformancePoint Service_ is the name that you want to give the new PerformancePoint Services service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _PerformancePoint Service Application_DB_ is name of the PerformancePoint Services service application database that you want to upgrade. 
    
   This command sets a variable, $pps, that you use when you create the proxy later.
    
   For more information, see [New-SPProfileServiceApplication](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
    
5. Type the following command to create a proxy for the PerformancePoint Services service application:
    
  ```
  New-SPPerformancePointServiceApplicationProxy -Name ProxyName -ServiceApplication $pps -Default
  ```

  Where:
    
  -  _ProxyName_ is the proxy name that you want to use. 
    
  - $pps is the variable that you set earlier to identify the new PerformancePoint Services service application.
    
    > [!TIP]
    > If you do not use the variable $pps, then you must use an ID to identify the PerformancePoint Services service application instead of a name. To find the ID, you can run the **Get-SPServiceApplication** cmdlet to return a list of all service application IDs. 
  
  -  _Default_ adds the PerformancePoint Services service application proxy to the default proxy group for the local farm. 
    
   For more information, see [New-SPPerformancePointServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPPerformancePointServiceApplicationProxy?view=sharepoint-ps).
    
## Upgrade the Search service application
<a name="UpgradeSearch"> </a>

To upgrade the Search service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group.
  
> [!NOTE]
> This section applies to only SharePoint 2013. Although SharePoint Foundation 2013 includes search functionality, it is not the same Search service application that is in SharePoint 2013 and it cannot be upgraded. 
  
 **To upgrade the Search service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default'
  ```

  Where:
    
  -  _SharePoint Web Services default_ is the name of the service application pool that will contain the new service applications. 
    
   This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
4. To upgrade the Search service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  $searchInst = Get-SPEnterpriseSearchServiceInstance -local
  # Gets the Search service instance and sets a variable to use in the next command
  Restore-SPEnterpriseSearchServiceApplication -Name '<SearchServiceApplicationName>' -applicationpool $applicationPool -databasename '<SearchServiceApplicationDBName>' -databaseserver <ServerName> -AdminSearchServiceInstance $searchInst 
  ```

  Where:
    
  -  _SearchServiceApplicationName_ is the name of the Search service application. 
    
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP]
    > If you do not use the variable $applicationPool, then you must specify the name of an existing service application pool in the format ' _Application Pool Name_'. To view a list of service application pools, you can run the **Get-SPServiceApplicationPool** cmdlet. 
  
  -  _SearchServiceApplicationDBName_ is the name of the Search service application Administration database that you want to upgrade. 
    
  - $searchInst is the variable that you set to identify the new Search Service application instance.
    
    > [!NOTE]
    > A Search service application upgrade might fail because of an issue that occurs during upgrade, such as network or SQL Server latency. If an error message appears during the Search service application upgrade, do the following: 
  
    For more information, see [Restore-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Restore-SPEnterpriseSearchServiceApplication?view=sharepoint-ps). 
    
    You must follow several steps to create the Search service application proxy and add it to the default proxy group. You must complete separate actions to find the ID for the Search service application, create the new proxy, get the proxy ID, and then add the proxy to the default proxy group.
    
5. Type the following command to get the ID for the Search service application and store it as a variable:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  ```

   For more information, see [Get-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceApplication?view=sharepoint-ps).
    
6. Type the following command to create a proxy for the Search service application:
    
  ```
  New-SPEnterpriseSearchServiceApplicationProxy -Name ProxyName -SearchApplication $ssa 
  ```

  Where:
    
  -  _ProxyName_ is the proxy name that you want to use. 
    
  - $ssa is the variable that you set earlier to identify the new Search service application.
    
    > [!TIP]
    > If you do not use the variable $ssa, then you must use an ID to identify the Search service application instead of a name. To find the ID, you can run the **Get-SPServiceApplication** cmdlet to return a list of all service application IDs. 
  
    For more information, see [New-SPEnterpriseSearchServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPEnterpriseSearchServiceApplicationProxy?view=sharepoint-ps).
    
7. Type the following command to get the Search service application proxy ID for the proxy you just created and set it as the variable $ssap:
    
  ```
  $ssap = Get-SPEnterpriseSearchServiceApplicationProxy 
  
  ```

   For more information, see [Get-SPEnterpriseSearchServiceApplicationProxy](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceApplicationProxy?view=sharepoint-ps).
    
8. Type the following command to add the Search service application proxy to the default proxy group:
    
  ```
  Add-SPServiceApplicationProxyGroupMember -member $ssap -identity " "
  
  ```

  Where:
    
  - $ssap is the variable that you set earlier to identify the ID for the proxy you just created for the Search service application.
    
    > [!TIP]
    > If you do not use the variable $ssap, then you must use an ID to identify the Search service application proxy instead of a name. To find the ID, you can run the **Get-SPServiceApplicationProxy** cmdlet to return a list of all service application proxy IDs. 
  
  - You use an empty **identity** parameter (" ") to add it to the default group. 
    
    For more information, see [Add-SPServiceApplicationProxyGroupMember](/powershell/module/sharepoint-server/Add-SPServiceApplicationProxyGroupMember?view=sharepoint-ps).
    
## Verify that all of the new proxies are in the default proxy group
<a name="VerifyProxies"> </a>

Use the following procedure to verify that the steps to create the proxies and add them to the default proxy group worked.
  
 **To verify that all of the new proxies are in the default proxy group by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following commands:
    
  ```
  $pg = Get-SPServiceApplicationProxyGroup -Identity " "
  $pg.Proxies
  ```

  Where:
    
  - $pg is a variable you set to represent the default proxy group.
    
  - You use an empty **identity** parameter (" ") to specify the default proxy group. 
    
    This returns a list of all proxies in the default proxy group, their display names, type names, and IDs.
    
For more information, see Get-SPServiceApplicationProxyGroup.
  
Now that the service applications are upgraded, you can start the process to upgrade the content databases. The first step in that process is to create the web applications that are needed for each content database.
  
|||
|:-----|:-----|
|![123 steps](../media/mod_icon_howTo_numeric_M.png)| This is the third phase in the process to upgrade SharePoint 2010 Products data and sites to SharePoint 2013.  <br/>  Next phase: [Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md) <br/>  For an overview of the whole process, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md).  <br/> |
   
## See also
<a name="VerifyProxies"> </a>

#### Other Resources

[Checklist for database-attach upgrade (SharePoint 2013)](checklist-for-database-attach-upgrade-sharepoint-2013.md)
  
[Services upgrade overview from SharePoint 2010 to SharePoint Server 2013](services-upgrade-overview-from-sharepoint-2010-to-sharepoint-server-2013.md)
  
[Upgrade farms that share services (parent and child farms) to SharePoint 2013](upgrade-farms-that-share-services-parent-and-child-farmsto-sharepoint-2013.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)

