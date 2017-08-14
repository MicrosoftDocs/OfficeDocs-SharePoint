---
title: Uninstall SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 7ad523f5-db54-4169-81ba-3a7b60f218b7
---


# Uninstall SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn about the limited set of supported methods to uninstallSharePoint Server 2016.You remove SharePoint Server 2016 by uninstalling it from Control Panel. When you uninstall SharePoint Server 2016, most files and subfolders in the installation folders are removed. However, some files are not removed. Also, 
- Web.config files, index files, log files, and customizations that you might have are not automatically removed when you uninstall SharePoint Server 2016.
    
  
- SQL Server databases are detached but are not removed from the database server.
    
  
- When you uninstall SharePoint Server 2016, all user data remains in the database files.
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, confirm that you have uninstalled all language packs that are on the server.
## Uninstall SharePoint Server 2016
<a name="begin"> </a>

Use this procedure to uninstall SharePoint Server 2016. **To uninstall SharePoint Server 2016**
1. Verify that you are a member of the Farm Administrators group or a member of the Administrators group on the local computer.
    
  
2. On the computer that runs SharePoint Server 2016, log on as a local or domain administrator.
    
  
3. Start Control Panel.
    
  - For Windows Server 2012 R2:
    
  - On the **Start** screen, click **Control Panel**.
    
  

    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows Server 2012 R2 and Windows Server 2012](http://go.microsoft.com/p/fwlink/?prd=12364&amp;pver=1.0&amp;sbp=Windows Server 2012 R2&amp;plcid=0x409&amp;clcid=0x409&amp;ar=Windows Server 2012&amp;sar=Windows Server 2012 R2 Navigat).
    
  
4. In the **Programs** area, click **Uninstall a program**.
    
  
5. In the **Uninstall or change a program** dialog box, click **Microsoft SharePoint Server 2016**.
    
  
6. Click **Change**.
    
  
7. On the **Change your installation of Microsoft SharePoint Server 2016** page, click **Remove**, and then click **Continue**.
    
    A confirmation message appears.
    
  
8. Click **Yes** to remove SharePoint Server 2016.
    
    A warning message appears.
    
  
9. Click **OK** to continue.
    
    A confirmation message appears.
    
  
10. Click **OK**.
    
    You might be prompted to restart the server.
    
  

> [!NOTE:]

  
    
    


# See also

#### 

 [Add SharePoint server to a farm in SharePoint Server 2016](html/add-sharepoint-server-to-a-farm-in-sharepoint-server-2016.md)
  
    
    
 [Remove a server from a farm in SharePoint Server 2016](html/remove-a-server-from-a-farm-in-sharepoint-server-2016.md)
  
    
    
 [Hardware and software requirements for SharePoint Server 2016](html/hardware-and-software-requirements-for-sharepoint-server-2016.md)
  
    
    
 [Install SharePoint Server 2016 on a single server with SQL Server](html/install-sharepoint-server-2016-on-a-single-server-with-sql-server.md)
  
    
    
 [Install SharePoint Server 2016 across multiple servers](html/install-sharepoint-server-2016-across-multiple-servers.md)
  
    
    

  
    
    

