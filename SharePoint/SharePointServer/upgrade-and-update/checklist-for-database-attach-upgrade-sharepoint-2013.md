---
title: "Checklist for database-attach upgrade (SharePoint 2013)"
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
ms.assetid: 0ba93198-452f-4e84-9e48-e3f0e5ae8f5b

description: "Use this checklist as you upgrade from SharePoint 2010 Products to SharePoint 2013."
---

# Checklist for database-attach upgrade (SharePoint 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
This checklist helps you confirm that you follow all the steps that you must follow as you prepare for upgrade, perform the upgrade, and perform post-upgrade steps. This checklist applies only to upgrade of the content and service application databases. It does not apply to upgrade of My Sites or other site collections. For more information, see [Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md).
  
    
Some steps include notes about how long that step might take. These rough estimates only give you a relative idea of the duration of the step. To discover how much time each step will take for your environment, we recommend that you perform trial upgrades in a test environment. For more information, see [Use a trial upgrade to SharePoint 2013 to find potential issues](use-a-trial-upgrade-to-sharepoint-2013-to-find-potential-issues.md).
  
> [!IMPORTANT]
> The steps in this article apply to both SharePoint Foundation 2013 and SharePoint 2013, except for the steps about how to upgrade the service applications, which apply mostly to SharePoint 2013 (the Business Data Connectivity service application applies to both). 
  
## Prepare for upgrade
<a name="Prepare"> </a>

Follow these steps in order before you start an upgrade to SharePoint 2013:
  
**Pre-upgrade steps**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Create an inventory of server-side customizations in the environment** <br/> Create an inventory of the server-side customizations in your environment (solutions, features, Web Parts, event handlers, master pages, page layouts, CSS files, and so on). Record all customizations needed for your environment in the upgrade worksheet.  <br/> Detailed steps: [Identify and install customizations](use-a-trial-upgrade-to-sharepoint-2013-to-find-potential-issues.md#Customizations) in the "Use a trial upgrade to find potential issues" article.  <br/> |Complete this step for the whole environment. Check each web server to make sure that you don't miss any customizations. Keep the inventory up to date as you prepare for the upgrade.  <br/> |
|[ ]  <br/> |**Clean up your environment** <br/> Before you begin to upgrade, make sure that your environment is functioning in a healthy state and that you clean up any content that you do not have to upgrade. Clean up any orphaned sites or data, address any large lists and large ACLs, remove extraneous document versions, and remove any unused templates, features and Web Parts.  <br/> Detailed steps: [Clean up an environment before an upgrade to SharePoint 2013](clean-up-an-environment-before-an-upgrade-to-sharepoint-2013.md).  <br/> |Complete this step one time for the whole environment.  <br/> This process might take days or weeks to finish.  <br/> |
|[ ]  <br/> |**Test the upgrade process** <br/> Try out upgrade in a test environment to find any issues and determine how long your actual upgrade might take.  <br/> Detailed steps: [Use a trial upgrade to SharePoint 2013 to find potential issues](use-a-trial-upgrade-to-sharepoint-2013-to-find-potential-issues.md) <br/> |Perform this step multiple times, until you are prepared to perform the actual upgrade.  <br/> |
   
## Complete the database attach upgrade
<a name="During"> </a>

Follow these steps in order while you upgrade the content and service application databases for your environment. 
  
**Prepare the new environment**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Install and configure SharePoint 2013 and any language packs** <br/> Install the prerequisite software, and then install and configure SharePoint 2013.  <br/> |Complete these steps on each server in your farm.  <br/> This step might take one hour or more, depending on the number of servers are in your environment.  <br/> |
|[ ]  <br/> |**Configure service applications** <br/>  Enable and configure the services that you need in your new environment.  <br/>  Do not configure the following service applications - you will configure them while you upgrade their databases later in the process:  <br/>  Business Data Connectivity service  <br/>  Managed Metadata service  <br/>  PerformancePoint services  <br/>  Search  <br/>  Secure Store service  <br/>  User Profile service  <br/> |Complete this step one time for the whole environment.  <br/> |
|[ ]  <br/> |**Configure general farm settings** <br/> Reapply any general farm settings that you must have from your previous farm — such as blocked file types, e-mail setting, and quota settings — and add users or groups to the Farm Administrators group. Configure new settings such as usage and health data collection, diagnostic logging, and mobile accounts.  <br/> |Complete this step one time for the whole environment.  <br/> |
   
> [!IMPORTANT]
> If you had disabled the Workflow Auto Cleanup timer job in your SharePoint 2013 environment, make sure that you disable this timer job in your new environment also. If this timer job is enabled in the new environment and disabled in the previous version environment, you might lose workflow associations when you upgrade. For more information about this timer job, see [Disable preservation of workflow history (SharePoint Server 2010)](https://go.microsoft.com/fwlink/?LinkId=403874). 
  
Detailed steps for this phase: [Create the SharePoint 2013 farm for a database attach upgrade](create-the-sharepoint-2013-farm-for-a-database-attach-upgrade.md). 
  
**Back up and restore databases**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Record the passphrase for the Secure Store service application** <br/> The Secure Store service application uses a passphrase to encrypt information. You must record this passphrase so that you can use it in the new environment.  <br/> |Complete this step one time for each Secure Store service application in the environment.  <br/> |
|[ ]  <br/> |**Set the previous version databases to be read-only** <br/> If you want your original environment to remain available to users in a read-only state, set the databases to read-only before you back them up.  <br/> |Complete this step for each content database in your environment.  <br/> Depending on your organization, you might need a database administrator to complete this step.  <br/> |
|[ ]  <br/> |**Back up databases** <br/>  Back up all the content databases and the following service application databases before you begin the database attach upgrade process:  <br/>  Business Data Connectivity  <br/>  Managed Metadata  <br/>  PerformancePoint  <br/>  Search Administration  <br/>  Secure Store  <br/>  User Profile: Profile, Social, and Sync databases  <br/> |Complete this step for each content database and supported service application database in your environment.  <br/> This step can take an hour, several hours, or longer, depending on your dataset and your environment.  <br/> Depending on your organization, you might need a database administrator to complete this step.  <br/> |
|[ ]  <br/> |**Export the encryption key for the User Profile service application** <br/> The User Profile Service service application requires an encryption key that is stored separately from the database and is needed if you want to upgrade the User Profile Sync database.  <br/> |Complete this step one time for each User Profile service application in the environment.  <br/> |
|[ ]  <br/> |**Restore a backup copy of the databases** <br/> Restore the databases from the backup.  <br/> |Complete this step for each content database and supported service application database in your environment.  <br/> This step can take an hour or longer, depending on your dataset and your environment.  <br/> Depending on your organization, you might need a database administrator to complete this step.  <br/> |
|[ ]  <br/> |**Set the restored databases to be read-write** <br/> Before you can attach and upgrade the databases that you copied to the new environment, you must set them to read-write.  <br/> |Complete this step for each content database and supported service application database in your environment.  <br/> Depending on your organization, you might need a database administrator to complete this step.  <br/> |
   
Detailed steps for this phase: [Copy databases to the new farm for upgrade to SharePoint 2013](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-2013.md)
  
**Upgrade service application databases**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Start the service application instances** <br/>  Start the following service instances from Central Administration:  <br/>  Business Data Connectivity service  <br/>  Managed Metadata service  <br/>  PerformancePoint services  <br/>  Secure Store service  <br/>  User Profile service  <br/>  Start the instance of the Search service application by using PowerShell.  <br/> |Complete this step one time for the whole environment.  <br/> |
|[ ]  <br/> |**Upgrade the Secure Store service application** <br/> Use PowerShell to create the new service application and upgrade the database, create a proxy and add it to the default proxy group, and then restore the passphrase from the previous environment.  <br/> |Complete this step one time for each Secure Store service application in the previous environment.  <br/> |
|[ ]  <br/> |**Upgrade the Business Data Connectivity service application** <br/> Use PowerShell to create the new service application and upgrade the database. You do not have to create a proxy for the Business Data Connectivity service application.  <br/> > [!NOTE]> The Business Data Connectivity service application is available in both SharePoint Foundation 2013 and SharePoint 2013.           |Complete this step one time for each Business Data Connectivity service service application in the previous environment.  <br/> |
|[ ]  <br/> |**Upgrade the Managed Metadata service application** <br/> Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. You must upgrade the Managed Metadata service application before you can upgrade the User Profile service application.  <br/> |Complete this step one time for each Managed Metadata service application in the previous environment.  <br/> |
|[ ]  <br/> |**Upgrade the User Profile service application** <br/> Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. After you have created the User Profile service application, you must import the Microsoft Identity Integration Server Key (MIIS) encryption key. Finally, you can start the User Profile Synchronization service.  <br/> |Complete this step one time for each User Profile service application in the previous environment.  <br/> |
|[ ]  <br/> |**Upgrade the PerformancePoint Services service application** <br/> Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group.  <br/> |Complete this step one time for each PerformancePoint Services service application in the previous environment.  <br/> |
|[ ]  <br/> |**Upgrade the Search service application** <br/> Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group.  <br/> > [!NOTE]> This step applies to only SharePoint 2013. Although SharePoint Foundation 2013 includes search functionality, it is not the same Search service application that is in SharePoint 2013 and it cannot be upgraded.           |Complete this step one time for each Search service application in the previous environment.  <br/> |
|[ ]  <br/> |**Verify that all of the new proxies are in the default proxy group** <br/> Use the **Get-SPServiceApplicationProxyGroup** cmdlet to verify that all of the service application proxies are in the default proxy group.  <br/> |Complete this step one time for the whole environment.  <br/> |
   
Detailed steps for this phase: [Upgrade service applications to SharePoint 2013](upgrade-service-applications-to-sharepoint-2013.md).
  
**Create web applications**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Create and configure web applications** <br/> Create a web application for each web application that existed in the old environment.  If the desire is to use Windows Claims Authentication, create the new Web Applications in Windows Claims mode instead of Classic mode.<br/> |Complete this step one time for the whole environment.  <br/> |
|[ ]  <br/> |**Reapply server-side customizations** <br/> Manually transfer all server-side customizations to your new farm. Refer to the inventory that you created in the upgrade worksheet to make sure that you install all components that your sites depend on to work correctly. When you install solutions, make sure that you add it to the appropriate path (/14 or /15). If you want a solution to be available to both paths, install it two times, and the second time use the **CompatibilityLevel** parameter when you install it, and it will be installed to the /15 path.  <br/> |Make sure that you reapply customizations to all web servers in the farm.  <br/> |
|[ ]  <br/> |**Verify custom components** <br/> Use the **Test-SPContentDatabase** Microsoft PowerShell cmdlet to verify that you have all the custom components that you need for that database.  <br/> |Complete this step for each content database in your environment.  <br/> Running the cmdlet takes only a few minutes, but addressing issues might take longer.  <br/> |
   
Detailed steps for this phase: [Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md).
  
**Attach and upgrade content databases**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Attach a content database to a web application** <br/> Attach the content database that contains the root site collection first. For My Sites, attach the content database that contains the My Site host before attaching databases that contain the My Sites.  <br/> You must perform this action from the command line. Use the **Mount-SPContentDatabase** Microsoft PowerShell cmdlet.  <br/> |Complete this step for one content database in your environment.  <br/> This step might take several minutes or several hours, depending on your dataset and hardware on the web servers, database servers, and storage subsystem.  <br/> |
|[ ]  <br/> |**Verify upgrade for the first database** <br/> Verify that upgrade succeeded for the first database, and review the site to see whether there are any issues.  <br/> Detailed steps: [Verify database upgrades in SharePoint 2013](verify-upgrade.md).  <br/> |Complete this step for the content database that you just attached.  <br/> |
|[ ]  <br/> |****Attach remaining databases**** <br/> Attach and upgrade the remaining content databases in your environment. You must complete this action from the command line.  <br/> |Complete this step for each of the remaining content databases in your environment.  <br/> This step might take several minutes or several hours, depending on your dataset, whether you are upgrading multiple databases in parallel, and the hardware on the web servers, database servers, and storage subsystem.  <br/> |
|[ ]  <br/> |**Monitor upgrade progress** <br/> Use the Upgrade Status page in the SharePoint Central Administration website to monitor progress as your databases are upgraded.  <br/> Detailed steps: [Verify database upgrades in SharePoint 2013](verify-upgrade.md).  <br/> |Complete this step for each content database that you upgrade.  <br/> This step might take several minutes, an hour, several hours, or days, depending on your content.  <br/> |
|[ ]  <br/> |**Verify upgrade for the remaining database** <br/> Verify that upgrade succeeded for the remaining databases.  <br/> Detailed steps: [Verify database upgrades in SharePoint 2013](verify-upgrade.md).  <br/> |Complete this step for each of the remaining content databases in your environment.  <br/> This step might take several minutes, an hour, several hours, or days, depending on your content.  <br/> |
   
Detailed steps for this phase: [Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md).
  
## Complete post-upgrade steps
<a name="PostUpgrade"> </a>

Follow these steps in order after you perform a database-attach upgrade. 
  
**Post upgrade steps for database attach upgrade**

|**Step**|**Notes**|
|:-----|:-----|
|[ ]  <br/> |**Verify that site collections are working as expecting in 2010 mode** <br/> Review the site collections and make sure that they work in 2010 mode before you begin to upgrade any site collections. You can use a similar review list as the one provided for upgraded sites in [Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md) <br/> > [!NOTE]> If the SharePoint 2013 Web Application was created in Windows Claims mode, complete the next step prior to testing site collections.           |Complete this step one time for your whole environment.  <br/> |
|[ ]  <br/> |**Migrate user accounts to claims authentication, if it is necessary** <br/> By default, new web applications in SharePoint 2013 use claims authentication. If you were using classic authentication in the previous environment, you must migrate the users to claims authentication. For more information, see [Migrate from classic-mode to claims-based authentication in SharePoint 2013](migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013.md).  <br/> |Complete this step one time for every web application that has changed authentication methods.<br/> |
|[ ]  <br/> |**Update links that are used in any upgraded InfoPath form templates** <br/> For a database-attach upgrade, you exported and imported all InfoPath form templates in your environment when you created the new environment. After upgrade, you can now update the links that are used in those upgraded form templates to point to the correct URLs by using a Microsoft PowerShell cmdlet.  <br/> For more information, see [Configure InfoPath Forms Services (SharePoint Server 2010)](https://go.microsoft.com/fwlink/?LinkId=403876).  <br/> |Complete this step one time for your whole environment.  <br/> |
|[ ]  <br/> |**Configure your Search topology** <br/> The architecture for the Search service has changed for SharePoint 2013. Plan and configure your Search topology to suit your environment and the new architecture. For more information, see [Scale search for Internet sites in SharePoint Server](../search/scale-search-for-internet-sites.md) and [Manage the search topology in SharePoint Server](../search/manage-the-search-topology.md).  <br/> |Complete this step one time for your whole environment.  <br/> |
|[ ]  <br/> |**Start a full crawl** <br/> After all content is upgraded and all settings are configured, you can start a full search crawl of your content. For more information, see [Start, pause, resume, or stop a crawl in SharePoint Server](../search/start-pause-resume-or-stop-a-crawl.md).  <br/> |Complete this step one time for your whole environment.  <br/> A full crawl can take several hours or days to complete, depending on how much content is in your environment.  <br/> |
|[ ]  <br/> |**Back up your farm** <br/> Back up your farm so that you have a current backup of your upgraded environment before you start to upgrade site collections. For more information, see [Back up farms in SharePoint Server](../administration/back-up-a-farm.md).  <br/> |Complete this step one time for your whole environment.  <br/> |
   
## See also
<a name="PostUpgrade"> </a>

#### Other Resources

[Create the SharePoint 2013 farm for a database attach upgrade](create-the-sharepoint-2013-farm-for-a-database-attach-upgrade.md)
  
[Copy databases to the new farm for upgrade to SharePoint 2013](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-2013.md)
  
[Upgrade service applications to SharePoint 2013](upgrade-service-applications-to-sharepoint-2013.md)
  
[Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Test and troubleshoot an upgrade to SharePoint 2013](test-and-troubleshoot-an-upgrade-0.md)

