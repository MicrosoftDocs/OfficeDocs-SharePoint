---
title: "Manage site collection upgrades to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/21/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: bfdcc03f-793f-41b1-96e7-5f7d7e445a38
description: "Learn how farm administrators can manage the upgrade queue and throttling settings and upgrade site collections to SharePoint 2013."
---

# Manage site collection upgrades to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Even though site collection administrators can now upgrade their own sites to SharePoint 2013, server farm administrators can still control when and whether a site collection is upgraded by managing the upgrade queue. You can also view and manage the upgrade throttling settings for a web application or content database to manage your farm's performance for site collection upgrades.
  
## Before you begin to upgrade site collections to SharePoint 2013
<a name="begin"> </a>

Farm administrators can control settings for site collection upgrade, such as notifications, throttling, and the upgrade queue, and can upgrade site collections by using PowerShell. Before you change these settings or upgrade a site collection, you should understand the settings and the implications for making changes. For more information about the settings for site collection upgrade, see [Plan for site collection upgrades in SharePoint 2013](plan-for-site-collection-upgrades-in-sharepoint-2013.md). For information about how to upgrade a site collection from the Site Settings page, see [Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md).
  
## Control upgrade notifications and self-service upgrade
<a name="UpgradeNotifications"> </a>

When a site collection is available to upgrade, site collection administrators see a status bar on their sites indicating that they can upgrade them. They can choose to upgrade the site collection then or be reminded later. You can control settings for these notifications and control whether site collection administrators can upgrade their site collections. For more information about these properties, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#Notifications).
  
 **To view the upgrade notification and self-service upgrade settings by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following commands to view the upgrade notification settings for a web application:
    
  ```
  $wa=Get-SPWebApplication <URL>
  $wa.UpgradeReminderDelay
  $wa.UpgradeMaintenanceLink
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to check. 
    
    This command returns the Upgrade reminder delay setting for the specified web application.
    
4. At the PowerShell command prompt, type the following command to view the self-service upgrade setting for a site collection:
    
  ```
  $site=Get-SPSite <URL>
  $site.AllowSelfServiceUpgrade=<Value>
  ```

  Where:
    
  -  _\<URL\>_ is URL for the site collection that you want to affect. 
    
  -  _\<Value\>_ is either 'true' to allow site collection administrators to upgrade the site, or 'false' to not show them the notification and not allow them to upgrade. 
    
For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps) and [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps).
  
 **To change the upgrade notification and self-service upgrade settings for a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command to change the upgrade notification settings for a web application:
    
  ```
  $wa=Get-SPWebApplication <URL>
  $wa.UpgradeReminderDelay=<Value>
  $wa.UpgradeMaintenanceLink='<LinkURL>'
  
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to affect. 
    
  -  _\<Value\>_ is the numeric value that you want to set for the delay (for example, 10 for 10 days). 
    
  -  _\<LinkURL\>_ is a link where the user can find more information. 
    
4. At the PowerShell command prompt, type the following command to change the self-service upgrade setting for a site collection:
    
  ```
  $site=Get-SPSite <URL>
  $site.AllowSelfServiceUpgrade=<Value>
  ```

  Where:
    
  -  _\<URL\>_ is URL for the site collection that you want to affect. 
    
  -  _\<Value\>_ is either 'true' to allow site collection administrators to upgrade the site, or 'false' to not show them the notification and not allow them to upgrade. 
    
For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps) and [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps).
  
## Control the compatibility range for site creation modes
<a name="UpgradeNotifications"> </a>

You can control which mode (2010 or 2013, or both) can be used when a user creates a site collection. The CompatibilityRange property on a web application controls the site modes available for a web application. You can view or change the settings for CompatibilityRange by using PowerShell.
  
 **To view the compatibility range for site creation modes for a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following commands to view the compatibility range settings for a web application:
    
  ```
  $wa=Get-SPWebApplication <URL>
  # Stores the web application at that URL as a variable 
  $wa.CompatibilityRange
  # Returns the CompatibilityRange for the specified web application
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to check. 
    
   This command returns the compatibility range for the specified web application. For example:
    
  ```
  MaxCompatibilityLevel   MinCompatibilityLevel  DefaultCompatibilityLevel   Singular
  ---------------------   ---------------------  -------------------------   --------
                  15                    14                           15         False
  
  ```

4. At the PowerShell command prompt, type the following commands to view the maximum, minimum, and default settings for a specific range:
    
  ```
  [Microsoft.SharePoint.SPCompatibilityRange]::<RangeName>
  ```

  Where:
    
  -  _RangeName_ is one of the following values: **OldVersions**, **NewVersion**, **AllVersions**. 
    
   This command returns the compatibility range for the specified value. For example, for **NewVersion**: 
    
  ```
  MaxCompatibilityLevel   MinCompatibilityLevel  DefaultCompatibilityLevel   Singular
  ---------------------   ---------------------  -------------------------   --------
                 15                     15                           15         True
  
  ```

For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps).
  
 **To change compatibility range for site creation modes for a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command to change the compatibility range settings to a specific range:
    
  ```
  $wa=Get-SPWebApplication <URL>
  # Stores the web application at that URL as a variable 
  $wa.CompatibilityRange = [Microsoft.SharePoint.SPCompatibilityRange]::<RangeName>
  # Specifies which range to use
  $wa.Update()
  # Updates the CompatibilityRange setting to use only the range you specified
  $wa.CompatibilityRange
  # Returns the new CompatibilityRange for the web application
  
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to change. 
    
  -  _RangeName_ is one of the following values: **OldVersions**, **NewVersion**, **AllVersions**. 
    
4. At the PowerShell command prompt, type the following command to change the values for the CompatibilityRange manually:
    
  ```
  $wa=Get-SPWebApplication <URL>
  # Stores the web application at that URL as a variable 
  $range = New-Object Microsoft.SharePoint.SPCompatibilityRange(<Integer>,<Integer>)
  # Creates a new compatibility range from <Integer> to <Integer>
  $wa.CompatibilityRange = $range
  # Specifies which range to use
  $wa.Update()
  #Updates the CompatibilityRange setting to use only the range you specified with $range
  $wa.CompatibilityRange
  # Returns the new CompatibilityRange for the web application
  
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to change. 
    
  -  _Integer_ is a number to use as the minimum or maximum value. For example, (14,15) would set the MinCompatibilityLevel to 14 (2010) and the MaxCompatibilityLevel to 15 (2013). The DefaultCompatibilityLevel is automatically set to the lower of the MaxCompatibilityLevel and the current major version (for example, 15). 
    
   This command sets and then returns the range that you specified. For example:
    
  ```
  MaxCompatibilityLevel   MinCompatibilityLevel   DefaultCompatibilityLevel   Singular
  ---------------------   ---------------------   -------------------------   --------
                  15                     14                           15         False
  
  ```

For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps).
  
## Control the queue for upgrades of sites to SharePoint 2013
<a name="Queue"> </a>

Every site that is set to upgrade is added to the queue, even if it is processed immediately. A site is removed from the queue after it is upgraded, or if it has encountered an error that must be addressed by a site collection or server administrator. If an unexpected failure occurs during the process (such as a power outage or service interruption), the site remains in the queue and the timer service will try the upgrade again automatically. Server farm administrators can manage the queue to remove a site from the queue, add a site to the queue, or upgrade a site manually.
  
Server farm administrators can manage the queue to do the following:
  
- Determine site collections that are in the upgrade queue.
    
    Each web application has its own upgrade queue. You can show the sites that are in the queue for a specific content database associated with that web application.
    
- See all sites that are currently being upgraded. 
    
    You can view the queue and filter it to show only the sites that are currently being upgraded for a specific content database.
    
- Add a site collection to the upgrade queue.
    
    If you want to upgrade a site collection, you can add it to the queue.
    
- Remove a site collection from the upgrade queue.
    
    You can remove a site collection from the upgrade queue. Stop the timer job, remove the site from the queue, and then restart the timer job to resume upgrade for the remaining sites in the queue. You cannot remove a site collection from the queue if it is currently being upgraded.
    
The following procedure contains steps to view and manage the site collection upgrade queue. 
  
 **To manage the upgrade queue by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. To view all site collections in the queue for a content database, at the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSiteUpgradeSessionInfo -ContentDatabase <DatabaseName> -ShowInProgress -ShowCompleted -ShowFailed |ft
  ```

  Where:
    
  -  _\<DatabaseName\>_ is name of the database that you want to check. You can also use the GUID for the database instead of the name. 
    
    For more information, see [Get-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Get-SPSiteUpgradeSessionInfo?view=sharepoint-ps). 
    
4. To see all sites that are currently being upgraded, at the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSiteUpgradeSessionInfo -ContentDatabase <DatabaseName> -ShowInProgress
  ```

  Where:
    
  -  _\<DatabaseName\>_ is name of the database that you want to check. You can also use the GUID for the database instead of the name. 
    
   For more information, see [Get-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Get-SPSiteUpgradeSessionInfo?view=sharepoint-ps). 
    
5. To see whether a particular site is in the queue, at the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSiteUpgradeSessionInfo -Site <http://site>
  ```

  Where:
    
  -  _\<http://site\>_ is URL for the site collection you want to add to the upgrade queue. 
    
    For more information, see [Get-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Get-SPSiteUpgradeSessionInfo?view=sharepoint-ps). 
    
6. To add a site collection to the upgrade queue, at the PowerShell command prompt, type the following command:
    
  ```
  Upgrade-SPSite <http://site> -VersionUpgrade -QueueOnly
  ```

  Where:
    
  -  _\<http://site\>_ is URL for the site collection you want to add to the upgrade queue. 
    
   For more information, see [Upgrade-SPSite](/powershell/module/sharepoint-server/Upgrade-SPSite?view=sharepoint-ps). 
    
7. To remove a site collection from the upgrade queue, at the PowerShell command prompt, type the following command:
    
  ```
  Remove-SPSiteUpgradeSessionInfo -Identity <URL>
  ```

    Where:
    
  -  _\<URL\>_ is URL for the site collection you want to add to the upgrade queue. 
    
   For more information, see [Remove-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Remove-SPSiteUpgradeSessionInfo?view=sharepoint-ps). 
    
## Control site throttle settings for upgrade to SharePoint 2013
<a name="Throttling"> </a>

You can view and change the upgrade throttle settings for a content database and web application by viewing and setting the **SPContentDatabase.ConcurrentSiteUpgradeSessionLimit** and **SPWebApplication.SiteUpgradeThrottleSettings** properties. For descriptions of the properties that control throttle levels and the default values, see [Plan for site collection upgrades in SharePoint 2013](plan-for-site-collection-upgrades-in-sharepoint-2013.md).
  
For more information about web application properties, see [SPWebApplication Properties](https://go.microsoft.com/fwlink/?LinkId=403893). For more information about content database properties, see [SPContentDatabase Properties](https://go.microsoft.com/fwlink/?LinkId=403892).
  
The following procedure provides steps to view upgrade throttling settings for a web application. 
  
 **To view the upgrade throttle settings for a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  $wa = Get-SPWebApplication <URL>
  $wa.SiteUpgradeThrottleSettings
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web application that you want to check. 
    
   This command returns the set of throttling settings for the specified web application. For example:
    
  ```
  AppPoolConcurrentUpgradeSessionLimit : 5
  UsageStorageLimit                    : 10
  SubwebCountLimit                     : 10
  Name                                 :
  TypeName                             : Microsoft.SharePoint.Administration.SPSiteUpgradeThrottleSettings
  DisplayName                          :
  Id                                   : ca76dda0-7050-4c6b-a126-05917da39f8a
  Status                               : Online
  Parent                               : SPWebApplication Name=SharePoint - 80
  Version                              : 8222
  Properties                           : {}
  Farm                                 : SPFarm Name=SharePoint_ConfigUpgradedPersistedProperties          : {}
  ```

For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps).
  
You can change the upgrade throttle settings for a web application. The following procedure provides steps to change the upgrade throttling settings for a web application. 
  
 **To change the upgrade throttle settings for a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  $wa=Get-SPWebApplication <URL>
  $wa.SiteUpgradeThrottleSettings.AppPoolConcurrentUpgradeSessionLimit=<Value>
  $wa.SiteUpgradeThrottleSettings.UsageStorageLimit=<Value>
  $wa.SiteUpgradeThrottleSettings.SubwebCountLimit=<Value>
  ```

  Where:
    
  -  _\<URL\>_ is URL for the web applications that you want to affect. 
    
  -  _Value_ is the numeric value that you want to set for that limit (for example, 8). 
    
   This command changes the throttling settings for a web application to the value that you supply. 
    
For more information, see [Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps). 
  
The following procedure provides steps to view upgrade throttling settings for a content database. 
  
 **To view the throttle settings for a content database by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  $db = Get-SPContentDatabase <DatabaseName> 
  # Stores the database name as a variable to use in the next command
  ```

  ```
  $db.ConcurrentSiteUpgradeSessionLimit
  # Returns the value for the limit for that database
  ```

  Where:
    
  -  _\<DatabaseName\>_ is name of the database that you want to check. You can also use the GUID for the database instead of the name. 
    
   This command returns the set of throttling settings for the specified content database.
    
For more information, see [Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps). 
  
You can change the upgrade throttle settings for a content database. The following procedure provides steps to change the upgrade throttling settings for a content database.
  
 **To change the throttle settings for a content database by using PowerShell**
  
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
  $db = Set-SPContentDatabase <DatabaseName>
  # Stores the database name as a variable to use in the next command
  ```

  ```
  $db.ConcurrentSiteUpgradeSessionLimit=<value>
  # Changes the limit to the value you specify.
  ```

  Where:
    
  -  _\<DatabaseName\>_ is name of the database that you want to affect. You can also use the GUID for the database instead of the name. 
    
  -  _\<value\>_ is a numeric value to set the property to, such as 9. 
    
   This command changes the throttling settings for the specified content database to the value that you supply.
    
For more information, see [Set-SPContentDatabase](/powershell/module/sharepoint-server/Set-SPContentDatabase?view=sharepoint-ps). 
  
## Create upgrade evaluation site collections by using PowerShell
<a name="CreateUpgradeEvalSite"> </a>

Site collection administrators can request a preview of their site collection. This preview site is called an upgrade evaluation site collection. Farm administrators can request an upgrade evaluation site collection by using PowerShell.
  
 **To request an upgrade evaluation site collection by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Either a site collection administrator or be granted full control (for repair mode) for the web application by policy. For more information about permission policies for web applications, see [Manage permission policies for a web application in SharePoint Server](../administration/manage-permission-policies-for-a-web-application.md).
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Request-SPUpgradeEvaluationSiteCollection -identity URL to site
  ```

  Where:
    
  -  _URL to site_ is the URL to a site collection in 2010 mode. 
    
For more information, see [Request-SPUpgradeEvaluationSite](/powershell/module/sharepoint-server/Request-SPUpgradeEvaluationSite?view=sharepoint-ps). 
  
## Upgrade site collections by using PowerShell
<a name="UpgradePowerShell"> </a>

You can upgrade a single site collection or all site collections in a specific database by using PowerShell. 
  
 **To upgrade a single site collection in a database by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Upgrade-SPSite <http://site> -VersionUpgrade [-Unthrottled]
  ```

  Where:
    
  -  _\<http://site\>_ is the URL for the site collection. 
    
  - Add the option **-Unthrottled** option to skip the site collection upgrade queue and start the upgrade immediately. 
    
This cmdlet upgrades the specific site collection to 2013 mode. For more information, see Upgrade-SPSite.
  
To upgrade all site collections in a database, use PowerShell. However, because sites can continue to run in 2010 mode in the SharePoint 2013 environment, this is not a necessary procedure for most environments. If you do choose to upgrade all site collections immediately, site collection owners do not have an opportunity to use an upgrade evaluation site to preview the new user interface or change their original site before upgrading. We do not recommend that you upgrade all site collections immediately as part of your initial upgrade. However, you might want to upgrade all site collections after some time has passed and all customizations were verified in 2013 mode.
  
 **To upgrade all site collections in a database by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSite -ContentDatabase <DBName> -Limit All | Upgrade-SPSite -VersionUpgrade -QueueOnly
  ```

  Where:
    
  -  _\<DBName\>_ is the name of the content database for which you want to upgrade all site collections. 
    
   The **QueueOnly** parameter adds the site collections to the upgrade queue. This allows the timer job to perform parallel upgrades when it is possible and can save time. The sites are upgraded in the order in which they are added to the queue. 
    
This cmdlet upgrades all site collections in the specific content database to 2013 mode.
  
## View upgrade status by using PowerShell
<a name="UpgradeStatus"> </a>

You can view upgrade status for all databases, for a single site collection, or for all site collections. 
  
 **To view upgrade status for a single site collection by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSiteUpgradeSessionInfo -Site <http://site>
  ```

  Where:
    
  -  _\<http://site\>_ is the URL of the site collection. 
    
   This cmdlet returns the upgrade status for the specified site collection together with information about the upgrade session and a link to the log files for more information. For more information, see [Get-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Get-SPSiteUpgradeSessionInfo?view=sharepoint-ps).
    
4. Or, you can use the following command to view the information about a specific site collection upgrade:
    
  ```
  $sc = Get-SPSite <http://site>
  # Sets a variable for the site collection
  $sc.CompatibilityLevel
  # Returns the compatibility level for the site collection (either 14 or 15 for 2010 or 2013 mode)
  $sc.UpgradeInfo
  # Returns the upgrade information for the site collection
  ```

  Where:
    
  -  _\<http://site\>_ is the URL of the site collection. 
    
   This command returns the compatibility level and upgrade information (such as a pointer to the log file) for the specified site collection. If the compatibility level is "15," then it has been upgraded to 2013 mode. For more information, see [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps).
    
 **To view upgrade status for a single database by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSiteUpgradeSessionInfo -ContentDatabase <DatabaseName> -ShowInProgress -ShowCompleted -ShowFailed
  ```

  Where:
    
  -  _\<DatabaseName\>_ is the name of the database that you want to check. 
    
   This cmdlet returns any site collections that have an upgrade in progress, completed, or failed and lists their status, plus a link to the log files for more information. You can use only one parameter to find only in progress, completed, or failed upgrades. For more information, see [Get-SPSiteUpgradeSessionInfo](/powershell/module/sharepoint-server/Get-SPSiteUpgradeSessionInfo?view=sharepoint-ps).
    
 **To view upgrade status for all site collections by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell. 
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSite -Limit All
  ```

This cmdlet returns the URL for all site collections in the environment and the compatibility level (14 or 15) for each site collection.
  
## See also
<a name="UpgradeStatus"> </a>

#### Other Resources

[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Run site collection health checks in SharePoint 2013](run-site-collection-health-checks-in-sharepoint-2013.md)
  
[Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md)

