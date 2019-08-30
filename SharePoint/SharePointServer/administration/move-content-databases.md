---
title: "Move content databases in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 6aa16d9a-812a-4bbc-b421-1b4589452503
description: "Learn how to move content databases in SharePoint Server."
---

# Move content databases in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes how to move content databases between servers that are running SQL Server, between instances of SQL Server, or from one SharePoint Server web application to another.
  
> [!IMPORTANT]
> This article only describes how to move content databases. For information about how to move other kinds of databases that are associated with SharePoint Server, see [Move or rename service application databases in SharePoint Server](move-or-rename-service-application-databases.md) and [Move all databases in SharePoint Server](move-all-databases.md). 
  
You can move content databases by using the SharePoint Central Administration website or Microsoft PowerShell, and SQL Server tools. Which tool that you use depends on what kind of environment you have deployed, what your schedule requires, and what service level agreements that you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, moving a content database, review the following tasks. Each task is a procedure that must be done in the order in which it is listed. Note that when you move content databases, you must use both SharePoint Server tools and SQL Server tools. You can use either Central Administration or Windows PowerShell 3.0 for this operation.
  
1. Record the content database name and the web application it is associated with.
    
2. Pause any service applications and services that might run against the content database, including timer jobs and search crawls.
    
3. Remove the SharePoint Server content database from the web application.
    
4. Detach the content database from the current SQL Server instance.
    
    > [!IMPORTANT]
    > To move the content database file within the same instance SQL Server we recommend that you use the **FILENAME** clause of the **ALTER DATABASE** statement. For more information, see [Move User Databases](http://go.microsoft.com/fwlink/p/?LinkID=717306&amp;clcid=0x409). 
  
    > [!IMPORTANT]
    > To move a content database to another instance of SQL Server or to another server, we recommend that you use procedures found in [Database Detach and Attach (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717308&amp;clcid=0x409) or [Back Up and Restore of SQL Server Databases](http://go.microsoft.com/fwlink/p/?LinkID=717309&amp;clcid=0x409). 
  
5. Copy or move the content database .mdf, .ndf, and .ldf files from the source location to the destination location using File Explorer.
    
6. Attach the content database to the new SQL Server instance.
    
7. Add the content database to the destination web application in SharePoint Server.
    
    > [!IMPORTANT]
    > Use the identical name when you add the content database or SharePoint Server creates a new content database. 
  
8. Restart all service applications and services that you paused in step 2.
    
## Moving content databases by using Central Administration
<a name="proc1"> </a>

Use the following procedure to move the content databases in your SharePoint Server farm by using Central Administration. 
  
The procedures in this section use Central Administration to move content databases. However when you perform the following procedures, you must use the correct tool:
  
1. To record which content databases are associated with each web application ─ PowerShell
  
4. To detach the content databases from SQL Server ─ SQL Server tools
  
5. To move the content databases to a new location ─ File Explorer or Windows Explorer
  
6. To attach the content databases to the new instance of SQL Server ─ SQL Server tools
  
> [!NOTE]
> The procedures in this section use Central Administration to move content databases. However, the first procedure, must be performed by using PowerShell. 
  
> [!NOTE]
> If you are moving a content database to a different farm, you must make the server farm account a member of the Administrators group on the database server during the restore process. This enables the account to replicate the security setting for the databases. This access level can be removed after the content database is moved. For more information, see [Account permissions and security settings in SharePoint Server 2016](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md). 
  
The destination farm must be running the same version or a later version of SharePoint Server than the source farm is running. 
  
### 1. To record which content databases are associated with each web application

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPContentDatabase -WebApplication <http://SiteName>
  ```

    Where:  _\<http://SiteName\>_ is the URL of the web application. 
    
    > [!NOTE]
    > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### 2. To pause timer jobs by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. In Central Administration, in the **Monitoring** section, click **Check Job Status**.
    
3. For each scheduled job that runs against the content database that you are moving, click the job to open the **Edit Timer Job** page, click **Disable**, and then click **OK**.
    
### 3. To detach the content databases from a web application by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. In Central Administration, in the **Application Management** section, click **Manage Content databases**.
    
3. On the **Manage Content Databases** page, click the content database that you want to move. 
    
    The **Manage Content Database Settings** page opens. 
    
    > [!NOTE]
    > If the content database does not appear in the list, it might be associated with another web application. To select another web application, on the **Web Application** menu, click **Change Web Application**. 
  
4. On the **Manage Content Database Settings** page, in the **Remove Content Database** section, select the **Remove content database** check box, and then click **OK**.
    
    > [!NOTE]
    > Removing the content database does not delete the database. It only removes the association of the database with the web application. 
  
5. Repeat steps 3 and 4 for each content database that you want to move.
    
### 4. To detach the content databases from SQL Server

1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role on the database server where each database is stored. 
    
2. In SQL Server Management Studio, open the source SQL Server instance, and then expand the **Databases** node. 
    
3. Right-click the content database, point to **Tasks**, and then click **Detach**. Repeat this step for each content database that you want to move.
    
    > [!NOTE]
    > Use this procedure to move only content databases. Do not detach any other kinds of databases. 
  
### 5. To move the content databases to a new location

1. Verify that the user account that is performing this procedure has Write access to both the source and destination folders.
    
2. Using File Explorer, locate the .mdf, .ldf, and .ndf files for the content databases.
    
3. Select the .mdf, .ldf, and .ndf files for the database that you want to move and either copy or move them to the destination directory.
    
### 6. To attach the content databases to the new instance of SQL Server

1. Verify that the user account that is performing this procedure is a member of the **dbcreator** fixed server role on the database server where each database is stored. 
    
2. In Management Studio, open the destination SQL Server instance.
    
3. Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.
    
4. In the **Attach Database** dialog box, browse to where you transferred the .mdf, .ldf, and .ndf files, select the .mdf file for the database that you want to attach, and then click **OK**.
    
5. Repeat for each content database that you are moving.
    
### 7. To attach the content databases to the web application by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration, in the **Application Management** section, click **Manage Content databases**.
    
3. On the **Manage Content Databases** page, click **Add a content database**.
    
4. On the **Add Content Database** page, verify that the **Web Application** menu displays the correct web application. 
    
5. In the **Server** box, specify the database server that hosts the database. 
    
6. In the **Database Name** box, type the exact name of the transferred content database. 
    
    > [!NOTE]
    > Verify that the name is correct. If it is not, a new database will be created. 
  
7. Specify the authentication method for the database, and then click **OK**.
    
8. Repeat these steps for each database that you are adding. Be sure that you select the correct web application from the **Web Application** menu for each database. 
    
### 8. To restart timer jobs by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration, in the **Monitoring** section, click **Check Job Status**.
    
3. For each scheduled job that you disabled previously, click the job to open the **Edit Timer Job** page, click **Enable**, and then click **OK**.
    
## Moving content databases by using PowerShell
<a name="proc2"> </a>

Use the following procedure to move the content databases in your SharePoint Server farm by using PowerShell
  
The procedures in this section use PowerShell to move content databases. However when you perform the following procedures, you must use the correct tool:
  
4. To detach the content databases from SQL Server ─ SQL Server tools
  
5. To move the content databases to a new location ─ File Explorer
  
6. To attach the content databases to the new instance of SQL Server ─ SQL Server tools
  
> [!NOTE]
> If you are moving a content database to a different farm, you must make the server farm account a member of the Administrators group on the database server during the restore process. This enables the account to replicate the security setting for the databases. This access level can be removed after the content database is moved. 
  
The destination farm must be running the same version or a later version of SharePoint Server than the source farm is running. 
  
### 1. To record which content databases are associated with each web application

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPContentDatabase -WebApplication <http://SiteName>
  ```

    Where:  _\<http://SiteName\>_ is the URL of the web application. 
    
For more information, see [Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps)
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### 2. To pause timer jobs by using PowerShell

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPTimerJob -webapplication <http://WebApplicationURL> | select name | Out-File <c:\timerjobfile.txt> -Append -Encoding ascii
  ForEach($tmrjob in (Get-Content <c:\timerjobfile.txt>)) { Get-SPTimerJob -Identity $tmrjob | Disable-SPTimerjob }
  
  ```

    Where:
    
  -  _\<http://WebApplicationURL\>_ is the Web application associated with the content database that you are moving. 
    
  -  _\<c:\timerjobfile.txt\>_ is the location of the file that you are creating that lists all timer jobs associated with the Web application. 
    
For more information, see [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps), [Out-File](http://go.microsoft.com/fwlink/p/?LinkID=717317&amp;clcid=0x409), [ForEach-Object](http://go.microsoft.com/fwlink/p/?LinkID=717315&amp;clcid=0x409), [Get-Content](http://go.microsoft.com/fwlink/p/?LinkID=717318&amp;clcid=0x409), and [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### 3. To detach content databases from a web application by using PowerShell

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Dismount-SPContentDatabase "<ContentDB>"
  ```

    Where:  _\<ContentDB\>_ is the name of the content database. 
    
    > [!NOTE]
    > If you have multiple content databases that have the same name, you must use the content database GUID in this command instead of using the content database name. To retrieve the GUID of the content database, run the **Get-SPContentDatabase** cmdlet without arguments. 
  
    For more information, see [Dismount-SPContentDatabase](/powershell/module/sharepoint-server/Dismount-SPContentDatabase?view=sharepoint-ps) and [Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps). 
    
    > [!NOTE]
    > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### 4. To detach the content databases from SQL Server

1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role on the database server where each database is stored. 
    
2. In Management Studio, open the source SQL Server instance, and then expand the **Databases** node. 
    
3. Right-click the content database, point to **Tasks**, and then click **Detach**. Repeat this step for each content database that you want to move.
    
    > [!NOTE]
    > Use this procedure to move only content databases. Do not detach any other kinds of databases. 
  
### 5. To move the content databases to a new location

1. Verify that the user account that is performing this procedure has Write access to both the source and destination folders.
    
2. Using File Explorer, locate the .mdf, .ldf, and .ndf files for the content databases.
    
3. Select the .mdf, .ldf, and .ndf files for the database that you want to move and either copy or move them to the destination directory.
    
### 6. To attach the content databases to the new instance of SQL Server

1. Verify that the user account that is performing this procedure is a member of the **dbcreator** fixed server role on the database server where each database is stored. 
    
2. In Management Studio, open the destination SQL Server instance.
    
3. Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.
    
4. In the **Attach Database** dialog box, browse to where you transferred the .mdf, .ldf, and .ndf files, select the .mdf file for the database that you want to attach, and then click **OK**.
    
5. Repeat for each content database that you are moving.
    
### 7. To attach content databases from a web application by using PowerShell

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Mount-SPContentDatabase "<ContentDB>" -DatabaseServer "<DBServer>" -WebApplication <http://SiteName>
  ```

    Where:
    
  -  _\<ContentDB\>_ is the name of the content database to be attached. 
    
  -  _\<DBServer\>_ is the name of the database server. 
    
  -  _\<http://SiteName\>_ is the URL of the Web application to which the content database is being attached. 
    
    For more information, see [Mount-SPContentDatabase](/powershell/module/sharepoint-server/Dismount-SPContentDatabase?view=sharepoint-ps).
    
    > [!NOTE]
    > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### 8. To restart timer jobs by using PowerShell

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  ForEach($tmrjob in (Get-Content <c:\timerjobfile.txt>)) {Get-SPTimerJob -Identity $tmrjob | Enable-SPTimerjob}
  
  ```

    Where:  _\<c:\timerjobfile.txt\>_ is the location of the file that you created that lists all of the timer jobs associated with the Web application. 
    
     For more information, see [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps), [ForEach-Object](http://go.microsoft.com/fwlink/p/?LinkID=717315&amp;clcid=0x409), [Get-Content](http://go.microsoft.com/fwlink/p/?LinkID=717318&amp;clcid=0x409), and [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps).
    
    > [!NOTE]
    > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## See also
<a name="proc2"> </a>

#### Concepts

[Move all databases in SharePoint Server](move-all-databases.md)

