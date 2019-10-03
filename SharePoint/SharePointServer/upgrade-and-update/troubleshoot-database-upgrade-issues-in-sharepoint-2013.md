---
title: "Troubleshoot database upgrade issues in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: a7334c45-7741-41d6-b354-3e3c5631521e
description: "Learn how to address problems that may occur after you upgrade a database to SharePoint 2013."
---

# Troubleshoot database upgrade issues in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Even after you test the upgrade process to identify potential issues, you might experience unexpected issues during an upgrade from SharePoint 2010 Products to SharePoint 2013. If you experience issues after upgrade, the sooner you detect and fix them, the better the end-user experience will be. 
  
This article includes a list of common issues and describes general principles to help you identify and address upgrade issues. After you identify and address the issues, you can resume upgrade. For more information about how to resume upgrade, see [Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff382638(v=office.14)).
  
## General principles to identify issues
<a name="Principles"> </a>

Check the upgrade status to see where upgrade stopped (if it did stop), and check log files to find errors or warnings. Next, address the issues that you find before you resume the upgrade.
  
### First, check upgrade status and log files

Upgrade status indicators and log files indicate what went wrong during the upgrade process. We recommend that you carefully review all the errors that were logged in the upgrade log files. Warnings might not always indicate an issue, but you should review them all to determine whether any of them are likely to cause even more issues.
  
1. Review the Upgrade Status page in the SharePoint Central Administration website.
    
    For more information about how to check upgrade status, see [Verify database upgrades in SharePoint 2013](verify-upgrade.md).
    
2. Review the following log files:
    
  - The upgrade error log file and the upgrade log file (which contains more detailed information than the upgrade error log file).
    
  - ULS or trace log files. 
    
    These files are stored in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\LOGS folder and are named  _Servername__ _YYYYMMDD_- _MMSS_.log. 
    
  - The application event log file. 
    
    This file can be viewed by using the Event Viewer.
    
    For more information about the upgrade log files, see [Verify database upgrades in SharePoint 2013](verify-upgrade.md). For more information about the trace log file, see [Trace Logs](https://go.microsoft.com/fwlink/p/?LinkId=182380) on MSDN. 
    
### Then, address issues in order

Some issues have more effect than others. For example, a missing server-side file can cause many seemingly unrelated errors at the site level.
  
Address issues in the following order:
  
1. Missing server-side files or customizations, such as features or Web Parts.
    
    Be sure to install all server-side customizations, such as features, Web Parts, and so on. Be sure to install customizations to the correct location in your new farm. For example, additional style sheets that you must have for SharePoint 2010 Products should be installed in the /14 path, not the new /15 path so that site collections that you have not upgraded can use them. Also, make sure that that you transfer all unique settings from the Web.config files for each web application to the new servers.
    
2. Configuration issues in the server farm, web application, or service applications, such as managed paths or service applications that are not started.
    
3. Additional issues that you discover on a site-by-site basis, starting with high-profile or very important sites.
    
As you identify and fix the top-level issues, you can try to run upgrade again to see whether any issues that occurred later in the upgrade process have also been fixed.
  
## Common issues
<a name="Common"> </a>

Check to see whether any of the following issues cause an upgrade error or warning.
  
### Q: I want to upgrade from a pre-release version of SharePoint 2013

- **A:** Upgrade from a pre-release version of SharePoint 2013 to the release version of SharePoint 2013 is not supported. 
    
    Pre-release versions are intended for testing only and should not be used in production environments. Upgrading from one pre-release version to another is also not supported.
    
### Q: The log says I have missing templates, features, or other server-side customizations
<a name="Missing"> </a>

- **A:** Identify all server-side customizations and install them before you upgrade 
    
One common error during upgrade is missing server-side files — either files that were installed with SharePoint 2010 Products or customized files. When you prepared for upgrade, you should have created an inventory of the server-side customizations (such as site definitions, templates, features, Web Parts, assemblies) that your sites required. Check this inventory to make sure that all the files that are needed for your customizations are installed in your new environment.
  
You can use the **test-spcontentdatabase** Microsoft PowerShell cmdlet before you upgrade the database to identify missing files. You can also use the **enumallwebs** operation in Stsadm.exe to identify server-side customizations that are being used. 
  
In the upgrade log files, you may see errors such as the following:
  
- ERROR Found Reference Count web(s) using missing web template Site Template Identifier (lcid: Site Template Language Code) in ContentDatabase Content Database Name.
    
- ERROR Found a missing feature Id =  _[Feature Identifier]_
    
- WARNING File  _[Relative File Path]_ is referenced  _[Reference Count]_ times in the database, but is not installed on the current farm. 
    
- WARNING WebPart class  _[Web Part Identifier]_ is referenced  _[Reference Count]_ times in the database, but is not installed on the current farm. 
    
- WARNING Assembly  _[Assembly Path]_ is referenced in the database, but is not installed on the current farm. 
    
- WARNING Feature could not be upgraded. Exception: Feature definition id  _'Feature Identifier'_ could not be found. 
    
If you can obtain a missing server-side file or dependency, install it, and then run upgrade again for the affected sites. If the file or dependency (such as a Web Part) was deprecated, you have to investigate whether you want to rebuild the site, page, or Web Part to use a different template, feature, or Web Part. If you can redo the customization by using dependencies that were not deprecated, you can run upgrade again for the affected sites. If you cannot remove the dependency, you cannot upgrade the site.
  
After you install the missing file or dependency, use the **test-SPContentDatabase** Microsoft PowerShell cmdlet on a test server to determine whether any other files for that database are missing. If you only run upgrade again, the error might not appear in the log files, even though it might still be occurring. 
  
### Q: The log file says that something is not right with my farm, web application, or service application configuration settings
<a name="Settings"> </a>

- **A:** Verify your farm and web application settings. 
    
- **A:** Create and start missing service applications 
    
- **A:** Verify that managed paths (included paths) are configured correctly for each web application. 
    
In the upgrade log files, you may see errors such as the following:
  
- ERROR Template  _Template Id_: SPSite Id= _Site Id_ could not be accessed due to exception. Skipping SPWeb Id=  _Web Id_ for template upgrade. Exception: System.IO.FileNotFoundException: The site with the id  _Site Id_ could not be found. 
    
    This error indicates that a managed path is missing. Add the managed path for the site collection into the web application and restart upgrade for the content database that contains this site collection.
    
### Q: I see errors and warnings during upgrade about connectivity or corruption
<a name="Data"> </a>

- **A:** Verify your power connections and connection to the network and to SQL Server. Loss of connectivity to data sources can cause errors. If your servers cannot connect to the databases, they cannot be upgraded. 
    
### Q: I ran out of disk space
<a name="Space"> </a>

- **A:** Free some space, or increase the size of the transaction log file before you resume upgrade. If you run out of space (for example, for transaction log files on your database servers), upgrade cannot continue. 
    
    For more information, see [Managing the Size of the Transaction Log File](https://go.microsoft.com/fwlink/p/?LinkID=124882).
    
### Q: I see an error about authentication
<a name="fba"> </a>

- **A:** Make sure that the web application is using the right authentication method. 
    
A mismatch in authentication methods can cause problems when you upgrade. The following resources can help if you have a mismatch between authentication methods:
  
- **Classic-to-claims authentication**
    
    Make sure that the web applications that you created in SharePoint 2013 use the same authentication method that was used in SharePoint 2010 Products. Claims-based authentication is the default authentication method for web applications in SharePoint 2013. If the web application was using classic mode, you can either update it to claims before you upgrade the database, or create the web application in classic mode and then migrate it to claims. For more information about how to create a web application that uses classic mode, and then migrating to claims, see [Create web applications that use classic mode authentication in SharePoint Server]/previous-versions/office/sharepoint-server-2010/gg276326(v=office.14)) and [Migrate from classic-mode to claims-based authentication in SharePoint 2013](migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013.md)
    
- **Forms-based authentication**
    
    Additional steps are necessary if you are upgrading an environment that uses forms-based authentication. Follow the steps in [Configure forms-based authentication for a claims-based web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806890(v=office.14)) to upgrade forms-based authentication providers. 
    
### Q: SQL Server says I don't have permissions
<a name="Perms"> </a>

- **A:** If you receive an error about an unknown account, or if a database is not upgraded, check the permissions for the database. In particular, between instances of SQL Server, make sure that you verify that security is configured correctly. Check that the login accounts that you use have the appropriate fixed roles and permissions on the databases, and that they will still be valid if you upgrade across domains. 
    
- **A:** Make sure the account that you use to attach the databases is a member of the **db_owner** fixed database role for the databases that you want to upgrade. 
    
### Q: A database will not upgrade
<a name="Perms"> </a>

- **A: ** Verify that the database is not set to read-only. You cannot upgrade a database that is set to read-only. Make sure that you set the databases to read-write before you attach and upgrade the databases. 
    
### Q: I changed a database name during restore, but I cannot find the files that have that name
<a name="Perms"> </a>

- **A: ** When you rename a database at restore time, you must also rename the database and log file names in the file system (the MDF and LDF files) so that they match. 
    
### Q: I cannot back up the Search service application Administration database
<a name="Perms"> </a>

- **A: ** Before you can back up the Search service application Administration database, you must stop the Search service on your SharePoint Server 2010 farm. To stop the Search service, on the original farm, on the **Start** menu, click **Administrative Tools**, and then click **Services**. Right-click **SharePoint Server Search 14**, and then click **Stop**. Be sure to start the service again after you back up the database.
    
### Q: Trusted connections are not working for Excel Services after upgrade
<a name="Perms"> </a>

- **A: ** You must manually create all trusted data connections for Excel Services after upgrade. 
    
### Q: My workflows are no longer associated correctly
<a name="Perms"> </a>

- **A: ** Verify that the Workflow Auto Cleanup timer job is turned off. If you had disabled the Workflow Auto Cleanup timer job in your SharePoint 2010 Products environment, make sure that you disable this timer job in the new environment also. If this timer job is enabled in the new environment and disabled in the SharePoint 2010 Products environment, you might lose workflow associations when you upgrade. 
    
### Q: I migrated users from classic authentication to claims-based authentication after upgrade. But some users have information that is out of date
<a name="Perms"> </a>

- **A: ** For issues with user profiles, make sure that that the User Profile to SharePoint Full Synchronization job was run. 
    
    If you started the User Profile to SharePoint Full Synchronization job (either automatically or manually) before the migration process was complete, some users might not be migrated. You can run the following cmdlet in Microsoft PowerShell after the migration is complete to clear the sync data, and then you can run the User Profile to SharePoint Full Synchronization job again to include the additional users.
    
  ```
  $database = Get-SPContentDatabase "DatabaseName"
  [Microsoft.Office.Server.UserProfiles.WSSProfileSynch]::ClearSyncDataForContentDatabase($database)
  ```

    Where  _DatabaseName_ is the name of the content database for the site collection associated with the out-of-date user profile. 
    
- **A: ** Verify that the user exists in the Active Directory domain. 
    
    If the user does not exist, you can designate the user as deleted in the UserInfo table. If the user does exist, you can run the migration again. For more information, see [Migrate from classic-mode to claims-based authentication in SharePoint 2013](migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013.md).
    
## See also
<a name="Common"> </a>

#### Other Resources

[Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14))
  
[Verify database upgrades in SharePoint 2013](verify-upgrade.md)
  
[Review site collections upgraded to SharePoint 2013](review-site-collections-upgraded-to-sharepoint-2013.md)
  
[Restart a database-attach upgrade or a site collection upgrade to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff382638(v=office.14)

