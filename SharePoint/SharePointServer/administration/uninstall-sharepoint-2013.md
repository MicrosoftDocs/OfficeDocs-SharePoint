---
title: "Uninstall SharePoint 2013"
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
ms.assetid: 306f837a-3468-41e3-8a08-2323a8ac4c39
description: "SharePoint Server 2013 and SharePoint Foundation 2013 support a limited set of methods to uninstall."
---

# Uninstall SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
You remove SharePoint 2013 by uninstalling it from Control Panel. When you uninstall SharePoint 2013, most files and subfolders in the installation folders are removed. However, some files are not removed. Also, 
  
- Web.config files, index files, log files, and customizations that you might have are not automatically removed when you uninstall SharePoint 2013.
    
- SQL Server databases are detached but are not removed from the database server.
    
- If you uninstall a single server that has a built-in database, SQL Server Express is not removed.
    
- When you uninstall SharePoint 2013, all user data remains in the database files.
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, confirm that you have uninstalled all language packs that are on the server.
  
## Uninstall SharePoint 2013
<a name="begin"> </a>

Use this procedure to uninstall SharePoint 2013.
  
 **To uninstall SharePoint 2013**
  
1. Verify that you are a member of the Farm Administrators group or a member of the Administrators group on the local computer.
    
2. On the computer that runs SharePoint 2013, log on as a local or domain administrator.
    
3. Start Control Panel.
    
4. In the **Programs** area, click **Uninstall a program**.
    
5. In the **Uninstall or change a program** dialog box, click **Microsoft SharePoint Server 2013**.
    
6. Click **Change**.
    
7. On the **Change your installation of Microsoft SharePoint Server 2013** page, click **Remove**, and then click **Continue**.
    
    A confirmation message appears.
    
8. Click **Yes** to remove SharePoint 2013. 
    
    A warning message appears.
    
9. Click **OK** to continue. 
    
    A confirmation message appears.
    
10. Click **OK**.
    
    You might be prompted to restart the server.
    
> [!NOTE]
> If you did not remove the language template packs before you uninstalled and then reinstalled SharePoint 2013, you must run **Repair** from the SharePoint Products Configuration Wizard for each language template pack on the server. After the repair operation is complete, you must restart the server. Finally, complete the language template pack configuration by running the SharePoint Products Configuration Wizard. 
  
## See also
<a name="begin"> </a>

#### Other Resources

[Add web or application servers to farms in SharePoint 2013](../install/add-web-or-application-server-to-the-farm.md)
  
[Remove a server from a farm in SharePoint 2013](remove-a-server-from-a-farm-in-sharepoint-2013.md)
  
[Hardware and software requirements for SharePoint 2013](../install/hardware-and-software-requirements-0.md)
  
[Install SharePoint 2013 on a single server with a built-in database](../install/single-server-with-a-built-in-database.md)
  
[Install SharePoint 2013 on a single server with SQL Server](../install/single-server-with-sql-server.md)
  
[Install SharePoint 2013 across multiple servers for a three-tier farm](../install/multiple-servers-for-a-three-tier-farm.md)

