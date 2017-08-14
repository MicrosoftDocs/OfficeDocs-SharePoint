---
title: Attach or detach content databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: bfa2f924-f411-4b13-8c24-bf251d7e4c91
---


# Attach or detach content databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-21* **Summary:** Learn how to attach and detach content databases to your SharePoint Server 2016 and SharePoint Server 2013 farm.You can attach or detach SharePoint Server content databases by using the SharePoint Central Administration website or Windows PowerShell 3.0In this article:
-  [Before you begin](#begin)
    
  
-  [Attaching and detaching content databases](#proc1)
    
  -  [To attach a content database by using Central Administration](#CA)
    
  
  -  [To detach a content database by using Central Administration](#detachCA)
    
  
  -  [To attach or detach a content database by using Windows PowerShell](#PS)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information:
- If you want to create a new content database while you attach it, the SharePoint farm service account must be a member of the SQL Server **dbcreator** fixed server role. To attach a content database to a web application, the SharePoint farm service account must have **db_owner** permission for the content database.
    
  
- If the database already exists, it must be the same version as the SharePoint Server 2016 farm or this operation will fail. To attach a content database that is a different version than the farm, use the  [To attach or detach a content database by using Windows PowerShell](#PS) procedure in the following section.
    
  

## Attaching and detaching content databases
<a name="proc1"> </a>

You might want to attach or detach content databases for the following reasons. You want to add a new content database for new site collections to keep content databases at a manageable size. You are restoring a content database from another farm and you want the sites that it contains to be accessed from a web application. You have archived site collections out of a content database and then detach the content database from the web application. For more information, see  [Move site collections between databases in SharePoint Server](html/move-site-collections-between-databases-in-sharepoint-server.md)The steps to add a database and to attach a database are very similar. For more information about how to add a database, see  [Add content databases in SharePoint Server](html/add-content-databases-in-sharepoint-server.md). **To attach a content database by using Central Administration**
1. Verify that the user account that is being used to perform this operation is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
  
3. On the SharePoint Central Administration website, click **Application Management**.
    
  
4. On the **Application Management** page, in the **Databases** section, click **Manage content databases**.
    
  
5. On the **Manage Content Databases** page, click **Add a content database**.
    
  
6. On the **Add Content Database** page:
    
1. Use the Web Application drop-down menu to select the web application to which you want to attach a content database.
    
  
2. Specify the database server that hosts the database.
    
  
3. Specify the database name. If the database does not already exist, it will be created. 
    
  
4. Specify the authentication method for the database, and supply an account name and password if you are using SQL authentication.
    
    
    
    > [!IMPORTANT:]
      

    
    
  
5. Click **OK**.
    
  
 **To detach a content database by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On the SharePoint Central Administration website, click **Application Management**.
    
  
3. On the **Application Management** page, in the **Databases** section, click **Manage content databases**.
    
  
4. Select the web application for which you want to detach a content database.
    
  
5. Click the content database that you want to detach.
    
  
6. On the **Manage Content Database Settings** page, select the **Remove content database** check box.
    
    If the content database contains data, you will receive a warning. Click **OK** to continue with the operation.
    
  
7. Click **OK** to confirm the detachment, or click **Cancel** to stop the operation without detaching the database.
    
    After detaching the content database in Central Administration, the content database still exists in SQL Server. If you want to permanently remove the content database, you must do so by using a SQL Server procedure.
    
  
 **To attach or detach a content database by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Open **SharePoint Management Shell**.
    
  
3. At the PowerShell command prompt, type the appropriate command
    
    **To attach an existing content database:**
    


  ```
  
Mount-SPContentDatabase "<ContentDb> " -DatabaseServer "<DbServer> " -WebApplication http://SiteName
  ```


    
    
    Where:
    
  -  *<ContentDb>*  is the content database to be attached.
    
  
  -  *<DbServer>*  is the name of the database server.
    
  
  -  *http://SiteName*  is the name of the web application to which the content database is being attached.
    
  

    
    
    **To detach a content database:**
    


  ```
  Dismount-SPContentDatabase "<ContentdBName> "
  ```


    
    
    Where  *<ContentdBName>*  is the name of the content database.
    
    > [!IMPORTANT:]
      

    The **Dismount-SPContentDatabase** cmdlet detaches the content database from the web application, but it does not delete the content database from SQL Server. After a content database is detached, you cannot delete it by using PowerShell. You can only remove it by using SQL Server tools. If you want to delete the content database from SQL Server while you detach it, use the **Remove-SPContentDatabase** cmdlet instead.
    
  
For more information, see **Dismount-SPContentDatabase** and **Mount-SPContentDatabase**.
> [!NOTE:]

  
    
    


# See also

#### 

 **Get-SPContentDatabase**
  
    
    
 **New-SPContentDatabase**
  
    
    
 **Remove-SPContentDatabase**
  
    
    

  
    
    

