---
title: Move content databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6aa16d9a-812a-4bbc-b421-1b4589452503
---


# Move content databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to move content databases in SharePoint Server 2016 and SharePoint Server 2013.This article describes how to move content databases between servers that are running SQL Server, between instances of SQL Server, or from one SharePoint Server web application to another.
> [!IMPORTANT:]

  
    
    

You can move content databases by using the SharePoint Central Administration website or Microsoft PowerShell, and SQL Server tools. Which tool that you use depends on what kind of environment you have deployed, what your schedule requires, and what service level agreements that you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Moving content databases by using Central Administration](#proc1)
    
  
-  [Moving content databases by using Windows PowerShell](#proc2)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, moving a content database, review the following tasks. Each task is a procedure that must be done in the order in which it is listed. Note that when you move content databases, you must use both SharePoint Server tools and SQL Server tools. You can use either Central Administration or Windows PowerShell 3.0 for this operation.
1. Record the content database name and the web application it is associated with.
    
  
2. Pause any service applications and services that might run against the content database, including timer jobs and search crawls.
    
  
3. Remove the SharePoint Server content database from the web application.
    
  
4. Detach the content database from the current SQL Server instance.
    
    > [!IMPORTANT:]
      
5. Copy or move the content database .mdf, .ndf, and .ldf files from the source location to the destination location using File Explorer.
    
  
6. Attach the content database to the new SQL Server instance.
    
  
7. Add the content database to the destination web application in SharePoint Server.
    
    > [!IMPORTANT:]
      
8. Restart all service applications and services that you paused in step 2.
    
  

## Moving content databases by using Central Administration
<a name="proc1"> </a>

Use the following procedure to move the content databases in your SharePoint Server farm by using Central Administration.
> [!NOTE:]
>  1. To record which content databases are associated with each web application ─ PowerShell>  4. To detach the content databases from SQL Server ─ SQL Server tools>  5. To move the content databases to a new location ─ File Explorer or Windows Explorer>  6. To attach the content databases to the new instance of SQL Server ─ SQL Server tools
  
    
    


> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

 **1. To record which content databases are associated with each web application**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPContentDatabase -WebApplication <http://SiteName>
  ```


    
    
    Where:
    
  -  *<http://SiteName>*  is the URL of the web application.
    
  

    > [!NOTE:]
      
 **2. To pause timer jobs by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. In Central Administration, in the **Monitoring** section, click **Check Job Status**.
    
  
3. For each scheduled job that runs against the content database that you are moving, click the job to open the **Edit Timer Job** page, click **Disable**, and then click **OK**.
    
  
 **3. To detach the content databases from a web application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage Content databases**.
    
  
3. On the **Manage Content Databases** page, click the content database that you want to move.
    
    The **Manage Content Database Settings** page opens.
    
    > [!NOTE:]
      
4. On the **Manage Content Database Settings** page, in the **Remove Content Database** section, select the **Remove content database** check box, and then click **OK**.
    
    > [!NOTE:]
      
5. Repeat steps 3 and 4 for each content database that you want to move.
    
  
 **4. To detach the content databases from SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role on the database server where each database is stored.
    
  
2. In SQL Server Management Studio, open the source SQL Server instance, and then expand the **Databases** node.
    
  
3. Right-click the content database, point to **Tasks**, and then click **Detach**. Repeat this step for each content database that you want to move.
    
    > [!NOTE:]
      
 **5. To move the content databases to a new location**
1. Verify that the user account that is performing this procedure has Write access to both the source and destination folders.
    
  
2. Using File Explorer, locate the .mdf, .ldf, and .ndf files for the content databases.
    
  
3. Select the .mdf, .ldf, and .ndf files for the database that you want to move and either copy or move them to the destination directory.
    
  
 **6. To attach the content databases to the new instance of SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **dbcreator** fixed server role on the database server where each database is stored.
    
  
2. In Management Studio, open the destination SQL Server instance.
    
  
3. Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.
    
  
4. In the **Attach Database** dialog box, browse to where you transferred the .mdf, .ldf, and .ndf files, select the .mdf file for the database that you want to attach, and then click **OK**.
    
  
5. Repeat for each content database that you are moving.
    
  
 **7. To attach the content databases to the web application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage Content databases**.
    
  
3. On the **Manage Content Databases** page, click **Add a content database**.
    
  
4. On the **Add Content Database** page, verify that the **Web Application** menu displays the correct web application.
    
  
5. In the **Server** box, specify the database server that hosts the database.
    
  
6. In the **Database Name** box, type the exact name of the transferred content database.
    
    > [!NOTE:]
      
7. Specify the authentication method for the database, and then click **OK**.
    
  
8. Repeat these steps for each database that you are adding. Be sure that you select the correct web application from the **Web Application** menu for each database.
    
  
 **8. To restart timer jobs by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Central Administration, in the **Monitoring** section, click **Check Job Status**.
    
  
3. For each scheduled job that you disabled previously, click the job to open the **Edit Timer Job** page, click **Enable**, and then click **OK**.
    
  

## Moving content databases by using PowerShell
<a name="proc2"> </a>

Use the following procedure to move the content databases in your SharePoint Server 2016 farm by using PowerShell.
> [!NOTE:]
>  4. To detach the content databases from SQL Server ─ SQL Server tools>  5. To move the content databases to a new location ─ File Explorer>  6. To attach the content databases to the new instance of SQL Server ─ SQL Server tools
  
    
    


> [!NOTE:]

  
    
    

 **1. To record which content databases are associated with each web application**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPContentDatabase -WebApplication <http://SiteName>
  ```


    
    
    Where:
    
  -  *<http://SiteName>*  is the URL of the web application.
    
  
For more information, see **Get-SPContentDatabase**
> [!NOTE:]

  
    
    

 **2. To pause timer jobs by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPTimerJob -webapplication <http://WebApplicationURL>  | select name | Out-File <c:\\timerjobfile.txt>  -Append -Encoding ascii

ForEach($tmrjob in (Get-Content <c:\\timerjobfile.txt> )) { Get-SPTimerJob -Identity $tmrjob | Disable-SPTimerjob }

  ```


    
    
    Where:
    
  -  *<http://WebApplicationURL>*  is the Web application associated with the content database that you are moving.
    
  
  -  *<c:\\timerjobfile.txt>*  is the location of the file that you are creating that lists all timer jobs associated with the Web application.
    
  
For more information, see **Get-SPTimerJob**, [Out-File](http://go.microsoft.com/fwlink/p/?LinkID=717317&amp;clcid=0x409),  [ForEach-Object](http://go.microsoft.com/fwlink/p/?LinkID=717315&amp;clcid=0x409),  [Get-Content](http://go.microsoft.com/fwlink/p/?LinkID=717318&amp;clcid=0x409), and **Disable-SPTimerJob**.
> [!NOTE:]

  
    
    

 **3. To detach content databases from a web application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Dismount-SPContentDatabase "<ContentDB> "
  ```


    
    
    Where:
    
  -  *<ContentDB>*  is the name of the content database.
    
  

    > [!NOTE:]
      

    For more information, see **Dismount-SPContentDatabase** and **Get-SPContentDatabase**.
    
    > [!NOTE:]
      
 **4. To detach the content databases from SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role on the database server where each database is stored.
    
  
2. In Management Studio, open the source SQL Server instance, and then expand the **Databases** node.
    
  
3. Right-click the content database, point to **Tasks**, and then click **Detach**. Repeat this step for each content database that you want to move.
    
    > [!NOTE:]
      
 **5. To move the content databases to a new location**
1. Verify that the user account that is performing this procedure has Write access to both the source and destination folders.
    
  
2. Using File Explorer, locate the .mdf, .ldf, and .ndf files for the content databases.
    
  
3. Select the .mdf, .ldf, and .ndf files for the database that you want to move and either copy or move them to the destination directory.
    
  
 **6. To attach the content databases to the new instance of SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **dbcreator** fixed server role on the database server where each database is stored.
    
  
2. In Management Studio, open the destination SQL Server instance.
    
  
3. Right-click the **Databases** node, point to **Tasks**, and then click **Attach**.
    
  
4. In the **Attach Database** dialog box, browse to where you transferred the .mdf, .ldf, and .ndf files, select the .mdf file for the database that you want to attach, and then click **OK**.
    
  
5. Repeat for each content database that you are moving.
    
  
 **7. To attach content databases from a web application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Mount-SPContentDatabase "<ContentDB> " -DatabaseServer "<DBServer> " -WebApplication <http://SiteName>
  ```


    
    
    Where:
    
  -  *<ContentDB>*  is the name of the content database to be attached.
    
  
  -  *<DBServer>*  is the name of the database server.
    
  
  -  *<http://SiteName>*  is the URL of the Web application to which the content database is being attached.
    
  

    For more information, see **Dismount-SPContentDatabase**.
    
    > [!NOTE:]
      
 **8. To restart timer jobs by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - The **dbcreator** and **securityadmin** fixed server roles on the destination server, in order to attach the database and configure SQL Server logins.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
ForEach($tmrjob in (Get-Content <c:\\timerjobfile.txt> )) {Get-SPTimerJob -Identity $tmrjob | Enable-SPTimerjob}

  ```


    
    
    Where:
    
  -  *<c:\\timerjobfile.txt>*  is the location of the file that you created that lists all of the timer jobs associated with the Web application.
    
  

     For more information, see **Get-SPTimerJob**, [ForEach-Object](http://go.microsoft.com/fwlink/p/?LinkID=717315&amp;clcid=0x409),  [Get-Content](http://go.microsoft.com/fwlink/p/?LinkID=717318&amp;clcid=0x409), and **Enable-SPTimerJob**.
    
    > [!NOTE:]
      

# See also

#### 

 [Move all databases in SharePoint Server](html/move-all-databases-in-sharepoint-server.md)
  
    
    

  
    
    

