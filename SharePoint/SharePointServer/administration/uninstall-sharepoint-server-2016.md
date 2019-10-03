---
title: "Uninstall SharePoint Server 2016 or SharePoint Server 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 7ad523f5-db54-4169-81ba-3a7b60f218b7
description: "Learn about the limited set of supported methods to uninstall SharePoint Server."
---

# Uninstall SharePoint Servers 2016 or 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]
  
You remove SharePoint Server by uninstalling it from Control Panel. When you uninstall SharePoint Server, most files and subfolders in the installation folders are removed. However, some files are not removed. Also, 
  
- Web.config files, index files, log files, and customizations that you might have are not automatically removed when you uninstall SharePoint Server.
    
- SQL Server databases are detached but are not removed from the database server.
    
- When you uninstall SharePoint Server, all user data remains in the database files.
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, confirm that you have uninstalled all language packs that are on the server.
  
## Uninstall SharePoint Servers 2016 or 2019
<a name="begin"> </a>

Use this procedure to uninstall SharePoint Server 2016.
  
 **To uninstall SharePoint Servers 2016 or 2019**
  
1. Verify that you are a member of the Farm Administrators group or a member of the Administrators group on the local computer.
    
2. On the computer that runs SharePoint Server, log on as a local or domain administrator.
    
3. Start Control Panel.
    
  
4. In the **Programs** area, click **Uninstall a program**.
    
5. In the **Uninstall or change a program** dialog box, click **Microsoft SharePoint Server 2016** or **Microsoft SharePoint Server 2019**.
    
6. Click **Change**.
    
7. On the **Change your installation of Microsoft SharePoint Server** page, click **Remove**, and then click **Continue**.
    
    A confirmation message appears.
    
8. Click **Yes** to remove SharePoint Server 2016. 
    
    A warning message appears.
    
9. Click **OK** to continue. 
    
    A confirmation message appears.
    
10. Click **OK**.
    
    You might be prompted to restart the server.
    
> [!NOTE]
> If you did not remove the language template packs before you uninstalled and then reinstalled SharePoint Server, you must run **Repair** from the SharePoint Products Configuration Wizard for each language template pack on the server. After the repair operation is complete, you must restart the server. Finally, complete the language template pack configuration by running the SharePoint Products Configuration Wizard. 
  
## See also
<a name="begin"> </a>

#### Concepts

[Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm](../install/add-a-server-to-a-sharepoint-server-2016-farm.md)
  
[Remove a server from a farm in SharePoint Server 2016 or SharePoint Server 2019](remove-a-server-from-a-farm-in-sharepoint-server-2016.md)
  
[Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md)

[Hardware and software requirements for SharePoint Server 2019](../install/hardware-and-software-requirements-2019.md)
  
[Install SharePoint Servers 2016 or 2019 on one server](../install/install-sharepoint-server-2016-on-one-server.md)
  
[Install SharePoint Servers 2016 or 2019 across multiple servers](../install/install-sharepoint-server-2016-across-multiple-servers.md)

