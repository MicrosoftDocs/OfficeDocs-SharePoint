---
title: Upgrade service applications to SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 6de4e8e0-5d27-4b1b-a87f-bebd8b9d6e77
---


# Upgrade service applications to SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-27* **Summary: ** Upgrade service applications (Business Connectivity Services, Managed Metadata, Secure Store, and Search) to SharePoint Server 2016.When you upgrade from SharePoint Server 2013 with Service Pack 1 (SP1) to SharePoint Server 2016, you must use a database attach upgrade, which means that you upgrade only the content for your environment and not the configuration settings. After you have configured the SharePoint Server 2016 environment, and copied the content and service application databases, you can upgrade the service applications to SharePoint Server 2016. This article contains the steps that you take to upgrade the service applications. **Phase 3 of the upgrade process: Upgrade service applications**
  
    
    
![Phase 3 of the upgrade process: Upgrade service applications](images/)
  
    
    

### 

![123 steps](images/)This is the third phase in the process to upgrade SharePoint Server 2013 with Service Pack 1 (SP1) data and sites to SharePoint Server 2016. The process includes the following phases that must be completed in order:  <br/> 
Create the SharePoint Server 2016 farm for a database attach upgradeCopy databases to the new farm for upgrade to SharePoint Server 2016Upgrade service applications to SharePoint Server 2016 (this phase) Upgrade content databases to SharePoint Server 2016For an overview of the whole process, see  [Overview of the upgrade process to SharePoint Server 2016](html/overview-of-the-upgrade-process-to-sharepoint-server-2016.md).  <br/> 
## Before you begin
<a name="begin"> </a>

Before you upgrade the service applications, review the following information and take any recommended actions.
- Make sure that the account that you use to perform the steps in this article is a member of the Farm administrators group in Central Administration.
    
  
- Decide which service application pool to use for the upgraded service applications. The procedures below use the default application pool for service applications which is "SharePoint Web Services Default". You can view a list of available service application pools by using the **Get-SPServiceApplicationPool** cmdlet in PowerShell. Or you can create a service application pool by using the **New-SPServiceApplicationPool** cmdlet. For more information, see **Get-SPServiceApplicationPool** and **New-SPServiceApplicationPool**.
    
  

> [!TIP:]

  
    
    


> [!NOTE:]

  
    
    


## About upgrading the service application databases
<a name="UpgradeServicesDBs"> </a>

To upgrade a service application database, you create a new service application and provide the name of the existing database to use for the new service application. As the service application is created, the database is upgraded. This process has several steps.
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    


1. Start the service instances
    
    The first step is to start service instances for the five service applications that you can upgrade: the Business Data Connectivity service, Managed Metadata Web Service, PerformancePoint Services service, Secure Store service, and Search service. Most of these service instances can be started from Central Administration. However the SharePoint Server Search service instance must be started by using PowerShell.
    
  
2. Create the service applications and upgrade the databases
    
    After you have started the service instances, the next step is to create the service applications and upgrade the databases. You must use PowerShell to restore the service application databases.
    
  
3. Create proxies for the service applications
    
    After you have upgraded the service application databases, you create the proxies for the service applications and add them to the default proxy group. You must create proxies for the following service applications:
    
  - Managed Metadata service application
    
  
  - Search service application
    
  
  - Secure Store service application
    
  
  - PerformancePoint Services service application
    
  

    The Business Data Connectivity service application automatically creates a proxy and assigns it to the default proxy group when you create the service application.
    
  
4. Verify that the proxies are in the default group
    
  
The following sections provide procedures to complete these steps.
## Start the service instances
<a name="StartServiceInstances"> </a>

The following procedures start the service instances. **To start service application instances from Central Administration**
1. Start SharePoint 2016 Central Administration.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Central Administration**.
    
    If **SharePoint 2016 Central Administration** is not on the **Start** screen:
    
  

  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Central Administration**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
2. In SharePoint 2016 Central Administration, on the **Application Management** page, in the **Service Applications** section, click **Manage Services on Server**.
    
  
3. Next to the **Business Data Connectivity service**, click **Start**.
    
  
4. Next to the **Managed Metadata Web Service**, click **Start**.
    
  
5. Next to the **PerformancePoint Services service**, click **Start**.
    
  
6. Next to the **Secure Store Service**, click **Start**.
    
  
The Search service instance must be started by using PowerShell because you cannot start it from Central Administration unless a Search Service application already exists. **To start the Search service instance by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
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

To upgrade the Secure Store service application, you create the new service application and upgrade the database, create a proxy and add it to the default proxy group, and then restore the passphrase from the previous environment. **To upgrade the Secure Store service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default '
  ```


    
    
    Where:
    
  -  *SharePoint Web Services default*  is the name of the service application pool that will contain the new service applications. This is the default service application pool. You can specify a different service application pool.
    
  

    
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
  
4. To upgrade the Secure Store service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$sss = New-SPSecureStoreServiceApplication -Name 'Secure Store ' -ApplicationPool $applicationPool -DatabaseName 'SecureStore_Upgrade_DB ' -AuditingEnabled
  ```


    
    
    Where:
    
  -  *SecureStore*  is the name that you want to give the new Secure Store service application.
    
  
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP:]
      
  -  *SecureStore_Upgrade_DB*  is the name of the service application database that you want to upgrade.
    
  

    
    
    This command sets a variable, $sss, that you use when you create the proxy later.
    
    For more information, see **New-SPSecureStoreApplication**.
    
  
5. Type the following command to create a proxy for the Secure Store service application:
    
  ```
  
$sssp = New-SPSecureStoreServiceApplicationProxy -Name ProxyName  -ServiceApplication $sss -DefaultProxyGroup
  ```


    
    
    Where:
    
  -  *ProxyName*  is the proxy name that you want to use.
    
  
  - $sss is the variable that you set earlier to identify the new Secure Store service application.
    
    > [!TIP:]
      
  -  *DefaultProxyGroup*  adds the Secure Store service application proxy to the default proxy group for the local farm.
    
  

    
    
    This command sets a variable, $sssp, for the service application proxy that you use when you restore the passphrase.
    
    For more information, see **New-SPSecureStoreServiceApplicationProxy**.
    
    After you create the Secure Store service application and the proxy, you have to refresh the encryption key. For information about how to refresh the encryption key, see  [Refresh the encryption key](configure-the-secure-store-service-in-sharepoint-server.md#refresh).
    
  
6. Type the following command to restore the passphrase for the Secure Store service application:
    
  ```
  
Update-SPSecureStoreApplicationServerKey -Passphrase <Passphrase>  -ServiceApplicationProxy $sssp
  ```


    
    
    Where:
    
  -  *<Passphrase>*  is the Passphrase for the Secure Store service application from your previous environment.
    
  
  - $sssp is a variable that you set earlier to identify the new Secure Store service application proxy.
    
    > [!TIP:]
      

    For more information, see **Update-SPSecureStoreApplicationServerKey**.
    
  

## Upgrade the Business Data Connectivity service application
<a name="UpgradeBDC"> </a>

To upgrade the Business Data Connectivity service application, you create the new service application and upgrade the database. You do not have to create a proxy for the Business Data Connectivity service application. The Business Data Connectivity service application automatically creates a proxy and assigns it to the default proxy group when you create the service application. **To upgrade the Business Data Connectivity service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default '
  ```


    
    
    Where:
    
  -  *SharePoint Web Services default*  is the name of the service application pool that will contain the new service applications.
    
  

    
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
  
4. To upgrade the Business Data Connectivity service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
New-SPBusinessDataCatalogServiceApplication -Name 'BDC Service ' -ApplicationPool $applicationPool -DatabaseName 'BDC_Service_DB '
  ```


    
    
    Where:
    
  -  *BDC Service*  is the name that you want to give the new Business Data Connectivity service application.
    
  
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP:]
      
  -  *BDC_Service_DB*  is name of the service application database that you want to upgrade.
    
  

    
    
    For more information, see **New-SPBusinessDataCatalogServiceApplication**.
    
  

## Upgrade the Managed Metadata service application
<a name="UpgradeMetadata"> </a>

To upgrade the Managed Metadata service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. **To upgrade the Managed Metadata service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default '
  ```


    
    
    Where:
    
  -  *SharePoint Web Services default*  is the name of the service application pool that will contain the new service applications.
    
  

    
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
  
4. To upgrade the Managed Metadata service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$mms = New-SPMetadataServiceApplication -Name 'Managed Metadata Service Application ' -ApplicationPool $applicationPool -DatabaseName 'Managed Metadata Service_DB '
  ```


    
    
    Where:
    
  -  *Managed Metadata Service Application*  is the name that you want to give the new Managed Metadata service application.
    
  
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP:]
      
  -  *Managed Metadata Service_DB*  is name of the service application database that you want to upgrade.
    
  

    
    
    This command sets a variable, $mms, that you use when you create the proxy later.
    
    For more information, see **New-SPMetadataServiceApplication**.
    
  
5. At the Microsoft PowerShell command prompt, type the following command to create a proxy for the Managed Metadata service application:
    
  ```
  
New-SPMetadataServiceApplicationProxy -Name ProxyName  -ServiceApplication $mms -DefaultProxyGroup
  ```


    
    
    Where:
    
  -  *ProxyName*  is the proxy name that you want to use.
    
  
  - $mms is the variable that you set earlier to identify the new Managed Metadata service application.
    
    > [!TIP:]
      
  -  *DefaultProxyGroup*  adds the Managed Metadata service application proxy to the default proxy group for the local farm.
    
  

    
    
    For more information, see **New-SPMetadataServiceApplicationProxy**.
    
  

## Upgrade the PerformancePoint Services service application
<a name="UpgradePPS"> </a>

To upgrade the PerformancePoint Services service application, you create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. **To upgrade the PerformancePoint Services service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default '
  ```


    
    
    Where:
    
  -  *SharePoint Web Services default*  is the name of the service application pool that will contain the new service applications.
    
  

    
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
  
4. To upgrade the PerformancePoint Services service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$pps = New-SPPerformancePointServiceApplication -Name 'PerformancePoint Service ' -ApplicationPool $applicationPool -DatabaseName 'PerformancePoint Service Application_DB '
  ```


    
    
    Where:
    
  -  *PerformancePoint Service*  is the name that you want to give the new PerformancePoint Services service application.
    
  
  - $applicationpool is the variable that you set earlier to identify the service application pool to use.
    
    > [!TIP:]
      
  -  *PerformancePoint Service Application_DB*  is name of the PerformancePoint Services service application database that you want to upgrade.
    
  

    
    
    This command sets a variable, $pps, that you use when you create the proxy later.
    
    For more information, see **New-SPProfileServiceApplication**.
    
  
5. Type the following command to create a proxy for the PerformancePoint Services service application:
    
  ```
  
New-SPPerformancePointServiceApplicationProxy -Name ProxyName  -ServiceApplication $pps -Default
  ```


    
    
    Where:
    
  -  *ProxyName*  is the proxy name that you want to use.
    
  
  - $pps is the variable that you set earlier to identify the new PerformancePoint Services service application.
    
    > [!TIP:]
      
  -  *Default*  adds the PerformancePoint Services service application proxy to the default proxy group for the local farm.
    
  

    
    
    For more information, see **New-SPPerformancePointServiceApplicationProxy**.
    
  

## Upgrade the Search service application
<a name="UpgradeSearch"> </a>

Upgrade the User Profile service application and the Managed Metadata service application before you upgrade the Search service application.To upgrade the Search service application, you copy the search administration database in your SharePoint Server 2013 with Service Pack 1 (SP1) farm to your SharePoint Server 2016 farm and restore the Search service application from your SharePoint Server 2013 with Service Pack 1 (SP1) farm in your SharePoint Server 2016 farm. The restore triggers SharePoint Server 2016 to create a new Search service application in the SharePoint Server 2016 farm and point it to the copied search administration database. To complete the upgrade of the Search service application you create a proxy and add it to the default proxy group and you ensure that the new Links Database and the new search topology is configured the same way as in the SharePoint Server 2013 with Service Pack 1 (SP1) farm.SharePoint Server 2016 normally creates a new search topology with all the search components and databases when it creates a the new Search service application. During a **restore** of a Search service application, SharePoint Server 2016 creates a new search topology, but upgrades the restored Search Administration database instead of creating a new Search Administration database. The upgraded Search Administration database retains any additions or modifications made to the search schema, result sources and query rules from the SharePoint Server 2013 with Service Pack 1 (SP1) farm.
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    

 **To upgrade the Search service application by using PowerShell**
1. To copy the search administration database in the SharePoint Server 2013 with Service Pack 1 (SP1) farm to the SharePoint Server 2016 farm, follow these steps:
    
    > [!NOTE:]
      

    > [!IMPORTANT:]
      

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint Management Shell**.
    
    If **SharePoint Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. Set the Search Administration database to read-only. In the second phase of the process to upgrade SharePoint Server 2013 with Service Pack 1 (SP1) data and sites to SharePoint Server 2016, you set all the other databases to read-only. Follow  [the same instructions](https://technet.microsoft.com/en-us/library/jj839720%28v=office.16%29.aspx) now for the Search Administration database.
    
  
4. Pause the Search service application. At the Windows PowerShell command prompt, type the following command:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
Suspend-SPEnterpriseSearchServiceApplication -Identity $ssa
  ```


    Where:
    
  -  *SearchServiceApplicationName*  is the name of the Search service application you want to pause.
    
  

    > [!NOTE:]
      

    
    
  
5. Copy the search administration database in the SharePoint Server 2013 with Service Pack 1 (SP1) farm to the SharePoint Server 2016 farm, follow the procedures in  [Copy databases to the new farm for upgrade to SharePoint Server 2016](html/copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-server-2016.md) for the search administration database only.
    
  

    
    
    > [!IMPORTANT:]
      
2. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
3. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
4. To store the application pool that you want to use as a variable for this service application, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$applicationPool = Get-SPServiceApplicationPool -Identity 'SharePoint Web Services default '
  ```


    
    
    Where:
    
  -  *SharePoint Web Services default*  is the name of the service application pool that will contain the new service applications.
    
  

    
    
    This cmdlet sets the service application pool as a variable that you can use again in the cmdlets that follow. If you have multiple application pools and have to use a different application pool for a particular service application, repeat this step in the procedure to create each service application to use the appropriate application pool.
    
  
5. To restore the Search service application and upgrade the Search Administration database, at the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$searchInst = Get-SPEnterpriseSearchServiceInstance -local
# Gets the Search service instance and sets a variable to use in the next command

Restore-SPEnterpriseSearchServiceApplication -Name '<SearchServiceApplicationName> ' -applicationpool $applicationPool -databasename '<SearchServiceApplicationDBName> ' -databaseserver <ServerName>  -AdminSearchServiceInstance $searchInst 
  ```


    
    
    Where:
    
  -  *SearchServiceApplicationName*  is the name of the Search service application.
    
  
  - $applicationpool is the variable that you set to identify the service application pool to use.
    
    > [!TIP:]
      
  -  *SearchServiceApplicationDBName*  is the name of the search administration database that you want to upgrade, and that this Search service application shall use.
    
  
  - $searchInst is the variable that you set to identify the new Search Service application instance.
    
  

    
    
    > [!NOTE:]
      

    For more information, see **Restore-SPEnterpriseSearchServiceApplication**.
    
    You must follow several steps to create the Search service application proxy and add it to the default proxy group. You must complete separate actions to find the ID for the Search service application, create the new proxy, get the proxy ID, and then add the proxy to the default proxy group.
    
  
6. Type the following command to get the ID for the Search service application and store it as a variable:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication
  ```


    
    
    For more information, see **Get-SPEnterpriseSearchServiceApplication**.
    
  
7. Type the following command to create a proxy for the Search service application:
    
  ```
  
New-SPEnterpriseSearchServiceApplicationProxy -Name ProxyName  -SearchApplication $ssa 
  ```


    
    
    Where:
    
  -  *ProxyName*  is the proxy name that you want to use.
    
  
  - $ssa is the variable that you set earlier to identify the new Search service application.
    
    > [!TIP:]
      

    
    
    For more information, see **New-SPEnterpriseSearchServiceApplicationProxy**.
    
  
8. Type the following command to get the Search service application proxy ID for the proxy you just created and set it as the variable $ssap:
    
  ```
  
$ssap = Get-SPEnterpriseSearchServiceApplicationProxy 

  ```


    
    
    For more information, see **Get-SPEnterpriseSearchServiceApplicationProxy**.
    
  
9. Type the following command to add the Search service application proxy to the default proxy group:
    
  ```
  
Add-SPServiceApplicationProxyGroupMember -member $ssap -identity " "

  ```


    
    
    Where:
    
  - $ssap is the variable that you set earlier to identify the ID for the proxy you just created for the Search service application.
    
    > [!TIP:]
      
  - You use an empty **identity** parameter (" ") to add it to the default group.
    
  

    
    
    For more information, see **Add-SPServiceApplicationProxyGroupMember**.
    
  
10. If the SharePoint Server 2013 with Service Pack 1 (SP1) farm uses a Links Database that is partitioned, partition the Links Database in the SharePoint Server 2016 farm the same way. Learn how in **Move-SPEnterpriseSearchLinksDatabases**.
    
  
11. (Optional) Preserve search relevance settings from the SharePoint Server 2013 with Service Pack 1 (SP1) farm. Because the upgraded Search service application has a new, empty index, search analytics data from the SharePoint Server 2013 with Service Pack 1 (SP1) farm cannot be fully retained. Copy the Analytics Reporting database from the SharePoint Server 2013 with Service Pack 1 (SP1) farm and attach it to the new Search service application in the SharePoint Server 2016 farm:
    
  - In the SharePoint Server 2013 with Service Pack 1 (SP1) farm,  [backup](https://technet.microsoft.com/en-us/library/jj729803.aspx#Backup) the Analytics Reporting database.
    
  
  - In the SharePoint Server 2016 farm,  [restore the backed up database](https://technet.microsoft.com/en-us/library/jj729803.aspx#Restore) to the new database server.
    
  
  - In the SharePoint Server 2016 farm,  [attach the restored database](https://technet.microsoft.com/en-us/library/jj729803.aspx#PS) to the new Search service application.
    
  
12. Verify that the search topology on the new SharePoint Server 2016 farm is alike that of the SharePoint Server 2013 with Service Pack 1 (SP1) farm. If your requirements for search have changed, now is a good time to scale out the search topology of the new SharePoint Server 2016 farm.
    
    
    
  
13. Resume the Search service application in the SharePoint Server 2013 with Service Pack 1 (SP1) environment.
    
    At the Windows PowerShell command prompt, type the following command:
    


  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
$ssa.ForceResume(0x02)
  ```


    Where:
    
  -  *SearchServiceApplicationName*  is the name of the Search service application you want to resume.
    
  

    
    
  

## Verify that all of the new proxies are in the default proxy group
<a name="VerifyProxies"> </a>

Use the following procedure to verify that the steps to create the proxies and add them to the default proxy group worked. **To verify that all of the new proxies are in the default proxy group by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=478553).
    
  
3. At the PowerShell command prompt, type the following commands:
    
  ```
  
$pg = Get-SPServiceApplicationProxyGroup -Identity " "
$pg.Proxies
  ```


    
    
    Where:
    
  - $pg is a variable you set to represent the default proxy group.
    
  
  - You use an empty **identity** parameter (" ") to specify the default proxy group.
    
  

    
    
    This returns a list of all proxies in the default proxy group, their display names, type names, and IDs.
    
  
For more information, see Get-SPServiceApplicationProxyGroup.Now that the service applications are upgraded, you can start the process to upgrade the content databases. The first step in that process is to create the web applications that are needed for each content database.
## 
<a name="VerifyProxies"> </a>


### 

![123 steps](images/) This is the third phase in the process to upgrade SharePoint Server 2013 with Service Pack 1 (SP1) data and sites to SharePoint Server 2016. <br/>  Next phase: [Upgrade content databases to SharePoint Server 2016](html/upgrade-content-databases-to-sharepoint-server-2016.md) <br/>  For an overview of the whole process, see [Overview of the upgrade process to SharePoint Server 2016](html/overview-of-the-upgrade-process-to-sharepoint-server-2016.md).  <br/> 
# See also

#### 

 [Create the SharePoint Server 2016 farm for a database attach upgrade](html/create-the-sharepoint-server-2016-farm-for-a-database-attach-upgrade.md)
  
    
    
 [Copy databases to the new farm for upgrade to SharePoint Server 2016](html/copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-server-2016.md)
  
    
    
 [Upgrade content databases to SharePoint Server 2016](html/upgrade-content-databases-to-sharepoint-server-2016.md)
  
    
    
 [Services upgrade overview for SharePoint Server 2016](html/services-upgrade-overview-for-sharepoint-server-2016.md)
  
    
    

#### 

 **Checklist for database-attach upgrade (SharePoint 2013)**
  
    
    

  
    
    

