---
title: "Remove a server from a farm in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/27/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 8a20a8f3-85bb-48be-b356-5c065623e205
description: "Learn how to remove a web server, application server, or database server from a SharePoint 2013 farm."
---

# Remove a server from a farm in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
There are three types of servers in a server farm running SharePoint 2013: web servers, application servers, and database servers. The method that you use to remove a server from a SharePoint farm varies depending on the type of server that you are removing from the farm.
  
## Removing a web server or application server from a SharePoint farm
<a name="removewebappserver"> </a>

For information about uninstallation procedures that SharePoint 2013 supports, see [Uninstall SharePoint 2013](uninstall-sharepoint-2013.md).
  
Removing a server that contains a search topology component can affect future search activities. The extent of that effect depends on the farm search topology. We recommend that you remove or relocate any search topology components from a server before removing the server from the farm.
  
If you remove a server that hosts a crawl component, no index files are lost. However, you might reduce or remove the capacity to crawl content.
  
You can lose index files in the following situations:
  
- The farm has only one query component, and you remove the server that hosts the query component.
    
- You have configured the index to be partitioned and you delete the last query component in one of the partitions. In this case, you will lose a portion of the index.
    
In either of these cases, a full crawl will have to be performed to re-create the index files.
  
You can deploy specific techniques to build fault tolerance into the search topology. If these techniques are followed, the deliberate or unplanned removal of a server from the topology can be absorbed without losing data and without affecting the ability to crawl or serve queries. (However, performance can still be affected.) For more information, see [Technical diagrams for SharePoint Server](../technical-reference/technical-diagrams.md).
  
Make sure that the server that you want to remove is not running any important site components. If important services or components (such as a custom Web Part) are running on the server and are not available on another server in the farm, removing the server can damage sites in the farm. For example, if the server that you want to remove is the only application server in the farm that is running the Business Data Connectivity service, removing the server can make any sites that rely on that service stop working correctly.
  
### Remove a web server or an application server from a farm by using Control Panel
<a name="removewebappCP"> </a>

You can remove a web server or an application server from the server farm by uninstalling SharePoint 2013 from the server through Control Panel. When you uninstall SharePoint 2013 by using Control Panel, you remove the program files and other information from the server.
  
 **To remove a web server or an application server from a farm by using Control Panel**
  
1. Verify that the user account that completes this procedure has the following credentials:
    
  - The user account that performs this procedure is a member of the Administrators group on the server.
    
2. Stop the services that are running on the server. For information about how to determine which services are running on a specific server and stopping services, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
3. On the server that you want to remove from the farm, click **Start**, click **Control Panel**, and then double-click **Programs and Features**.
    
4. In the list of currently installed programs, click **SharePoint 2013**, and then click **Uninstall**.
    
5. Click **Continue** at the confirmation prompt to uninstall the program. 
    
## Removing a database server from a SharePoint farm
<a name="RemoveDB"> </a>

To remove a database server from a farm without uninstalling SharePoint and therefore deleting the data that was stored in the database, you must first move any databases that are hosted by that server to another database server in the farm and then use Central Administration to remove the database server from the farm.
  
You cannot remove a database server if it is the only database server available in the farm, or if it is the database server that hosts the configuration database.
  
> [!CAUTION]
> If you uninstall SharePoint 2013 from the server that is running Central Administration, you will be unable to administer the server farm until you configure another server in the farm to host the Central Administration site. 
  
## Remove a database server, web server, or application server from a SharePoint farm by using Central Administration
<a name="RemoveAnyServer"> </a>

If a web server or application server is no longer available, or if uninstalling SharePoint 2013 from Control Panel is not possible, you can remove the web server or application server from the farm by using the SharePoint Central Administration website. Removing a server from the farm by using Central Administration does not uninstall SharePoint 2013 from the server, nor does it make any sites on that server inaccessible. We recommend that you use the process described in [Remove a web server or an application server from a farm by using Control Panel](#removewebappCP) to uninstall SharePoint 2013 instead of using Central Administration to remove the server. 
  
Removing the server from the farm by using Central Administration does not delete this information from the server. Use the Central Administration procedure for removing database servers only, or for removing a web server or an application server from the farm when the server is no longer available to uninstall through Control Panel.
  
You can follow these steps to remove a web server, application server, or database server from the farm. However, we recommend that you remove web servers and application servers from a farm by using Control Panel, instead of by using Central Administration. For information, see [Remove a web server or an application server from a farm by using Control Panel](#removewebappCP).
  
Before you remove a database server from a farm, make sure that you have moved any databases stored on that server to a different database server in your farm. 
  
 **To remove a database server, web server, or application server from a SharePoint farm by using Central Administration**
  
1. Verify that the user account that completes this procedure has the following credentials:
    
  - The user account that performs this procedure is a member of the Farm Administrators SharePoint group.
    
  - The user account that performs this procedure is a member of the Administrators group on the server.
    
2. Stop the services that are running on the server. For information about how to determine which services are running on a specific server and stopping services, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
3. On the SharePoint Central Administration website, in the **System Settings** section, click **Manage servers in this farm**.
    
4. On the **Servers in Farm** page, locate the row that contains the name of the server that you want to remove, and then click **Remove Server**. 
    
5. In the warning that appears, click **OK** to remove the server or click **Cancel** to stop the operation. 
    
    The page updates, and the server that you removed no longer appears in the list of servers.
    
## See also
<a name="RemoveAnyServer"> </a>

#### Other Resources

[Install for SharePoint 2013](../install/install-for-sharepoint-2013.md)

