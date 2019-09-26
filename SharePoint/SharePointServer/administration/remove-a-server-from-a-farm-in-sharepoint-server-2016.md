---
title: "Remove a server from a farm in SharePoint Servers 2016 or 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: acb2d589-6c19-4b6b-9cd1-5e334ba4f2cd
description: "Learn how to remove a server from a SharePoint Server farm."
---

# Remove a server from a farm in SharePoint Servers 2016 or 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
    
## Removing a server from a SharePoint farm
<a name="removewebappserver"> </a>

For information about uninstallation procedures that SharePoint Servers 2016 or 2019 support, see [Uninstall SharePoint Servers 2016 or 2019](uninstall-sharepoint-server-2016.md).
  
Removing a server that contains a search topology component can affect future search activities. The extent of that effect depends on the farm search topology. We recommend that you remove or relocate any search topology components from a server before removing the server from the farm.
  
If you remove a server that hosts a crawl component, no index files are lost. However, you might reduce or remove the capacity to crawl content.
  
You can lose index files in the following situations:
  
- The farm has only one query component, and you remove the server that hosts the query component.
    
- You have configured the index to be partitioned and you delete the last query component in one of the partitions. In this case, you will lose a portion of the index.
    
In either of these cases, a full crawl will have to be performed to re-create the index files.
  
You can deploy specific techniques to build fault tolerance into the search topology. If these techniques are followed, the deliberate or unplanned removal of a server from the topology can be absorbed without losing data and without affecting the ability to crawl or serve queries. (However, performance can still be affected.) 
  
Make sure that the server that you want to remove is not running any important site components. If important services or components (such as a custom Web Part) are running on the server and are not available on another server in the farm, removing the server can impact sites in the farm. For example, if the server that you want to remove is the only server in the farm that is running the Business Data Connectivity service, removing the server can make any sites that rely on that service stop working correctly.
  
To remove a server from a farm, you must first move any databases that are hosted by that server to another database server in the farm and then use Central Administration to remove the database server from the farm.
  
You cannot remove a database server if it is the only database server available in the farm, or if it is the database server that hosts the configuration database.
  
> [!CAUTION]
> If you uninstall SharePoint Server 2016 or SharePoint Server 2019 from the server that is running Central Administration, you will be unable to administer the server farm until you configure another server in the farm to host the Central Administration site. 
  
### Remove a server from a SharePoint farm by using Microsoft PowerShell
<a name="RemoveByPowerShell"> </a>

Before you remove a database server from a farm, make sure that you have moved any databases stored on that server to a different database server in your farm. 
  
> [!NOTE]
> Using PowerShell is the recommended way to remove a server from the farm. 
  
 **To remove a server from a SharePoint farm by using PowerShell**
  
Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin). 
  
1. From a PowerShell command prompt, type the following command.
    
  ```
  Disconnect-SPConfigurationDatabase 
  ```

    > [!NOTE]
    > This cmdlet only removes the **local SharePoint server** from the SharePoint farm. It can't remove remote SharePoint servers or database servers from the SharePoint farm. 
  
#### Remove a server from a SharePoint farm by using the PSConfig.exe command-line tool
<a name="RemovePSConfig"> </a>

You can remove a server from the SharePoint farm by using the PSConfig.exe tool which is an alternative interface to perform several operations that control how SharePoint Server 2016 is configured. You must be a member of the Administrators group on the local computer to perform these operations. 
  
 **To remove a SharePoint server from a farm by using PSConfig**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PSConfig.exe tool. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. 
  
  - From a command prompt, type the following syntax.
    
  ```
  psconfig.exe -cmd configdb -disconnect
  ```

### Remove a server from a SharePoint farm by using Control Panel
<a name="removewebappCP"> </a>

You can remove a server from the farm by uninstalling SharePoint Server 2016 from the server through Control Panel. When you uninstall SharePoint Servers 2016 or 2019 by using Control Panel, you disconnect the server from the farm, and then remove the program files and other information from the server.
  
 **To remove a server from a SharePoint farm by using Control Panel**
  
Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which SharePoint Server 2016 is installed. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
1. On the server that you want to remove from the farm, click **Start**, click **Control Panel**, and then double-click **Programs and Features**.
    
2. In the list of currently installed programs, click **Microsoft SharePoint Server 2016** or **Microsoft SharePoint Server 2019** , and then click **Uninstall**.
    
3. Click **Continue** at the confirmation prompt to uninstall the program. 
    
## Remove a server from a SharePoint farm by using Central Administration
<a name="RemoveAnyServer"> </a>

If a server is no longer available, or if uninstalling SharePoint Server from Control Panel is not possible, you can remove the SharePoint server from the farm by using the SharePoint Central Administration website. Removing a server from the farm by using Central Administration does not uninstall SharePoint Server from the server.  
  
> [!IMPORTANT]
> This method of removing a server should only be used when you need to remove an orphaned server from the configuration database. > The recommended way of removing a server from the farm is PowerShell, see [Remove a server from a SharePoint farm by using Microsoft PowerShell](remove-a-server-from-a-farm-in-sharepoint-server-2016.md#RemoveByPowerShell). 
  
Removing the server from the farm by using Central Administration does not delete this information from the server. Use the Central Administration procedure for removing database servers only, or for removing a web server or an application server from the farm when the server is no longer available to uninstall through Control Panel.
  
You can follow these steps to remove a SharePoint or database server from the farm. However, we recommend that you remove web servers and application servers from a farm by using Windows PowerShell, instead of by using Central Administration. For information, see [Remove a server from a SharePoint farm by using Microsoft PowerShell](remove-a-server-from-a-farm-in-sharepoint-server-2016.md#RemoveByPowerShell).
  
Before you remove a database server from a farm, make sure that you have moved any databases stored on that server to a different database server in your farm. 
  
 **To remove a server from a SharePoint farm by using Central Administration**
  
Verify that the user account that completes this procedure has the following credentials:
    
  - The user account that performs this procedure is a member of the Farm Administrators SharePoint group.
    
  - The user account that performs this procedure is a member of the Administrators group on the server.
    
1. On the SharePoint Central Administration website, in the **System Settings** section, click **Manage servers in this farm**.
    
2. On the **Servers in Farm** page, locate the row that contains the name of the server that you want to remove, and then click **Remove Server**. 
    
3. In the warning that appears, click **OK** to remove the server or click **Cancel** to stop the operation. 
    
    The page updates, and the server that you removed no longer appears in the list of servers.
    
<a name="RemoveAnyServer"> </a>

