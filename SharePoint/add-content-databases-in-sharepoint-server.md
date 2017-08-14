---
title: Add content databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 0889004d-6820-4282-a63c-863f4796ff85
---


# Add content databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Search Server 2013, SharePoint Foundation 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-21* **Summary:** Learn how to add a content database to your SharePoint Server 2016 and SharePoint Server 2013 farm.You can add a content database to a SharePoint Server farm by using the SharePoint Central Administration website or Microsoft PowerShell. The tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Adding a content database to a SharePoint Server web application](#proc1)
    
  -  [To add a content database to a web application by using Central Administration](#CA)
    
  
  -  [To add a content database to a web application by using Windows PowerShell](#PS)
    
  

## Before you begin
<a name="begin"> </a>

You can add a new content database or attach an existing content database from a backup file.Before you begin this operation, review the following information about prerequisites:
- The user account that is performing this operation must be a member of the Farm Administrators SharePoint group.
    
  
- If you use Windows authentication to connect to SQL Server, the user account must be a member of the **dbcreator** fixed server role on the SQL Server instance where the database is to be created.
    
  

## Adding a content database to a SharePoint Server web application
<a name="proc1"> </a>

You can use the procedures that are described in this article to create a new content database and attach it to a web application. If you are using Windows authentication to connect to SQL Server, the user account must also be a member the SQL Server **dbcreator** fixed server role on the SQL Server instance where the database will be created. If you are using SQL authentication to connect to SQL Server, the SQL authentication account that you specify when you create the content database must have **dbcreator** permission on the SQL Server instance where the database will be created. **To add a content database to a web application by using Central Administration**
1. Verify that the user account that is performing this operation is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
  
3. On the SharePoint Central Administration website, click **Application Management**.
    
  
4. In the **Databases** section, click **Manage content databases**.
    
  
5. On the **Manage Content Databases** page, click **Add a content database**.
    
  
6. On the **Add Content Database** page:
    
1. Specify a web application for the new database.
    
  
2. Specify a database server to host the new database.
    
  
3. Specify the authentication method that the new database will use and supply an account name and password, if they are necessary.
    
    
    
    > [!IMPORTANT:]
      
4. Specify the name of the failover database server, if one exists.
    
  
5. Specify the number of top-level sites that can be created before a warning is issued. By default, this is 2,000.
    
  
6. Specify the total number of top-level sites that can be created in the database. By default, this is 5,000.
    
    
    
  
7. Click **OK**.
    
  
 **To add a content database to a web application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Open **SharePoint Management Shell**.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
New-SPContentDatabase -Name <ContentDbName>  -WebApplication <WebApplicationName>
  ```


    
    
    Where:
    
  -  *<ContentDbName>*  is the name of the content database to create.
    
  
  -  *<WebApplicationName>*  is the name of the web application to which the new database is attached.
    
  
For more information, see **New-SPContentDatabase**.
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


# See also

#### 

 [Attach or detach content databases in SharePoint Server](html/attach-or-detach-content-databases-in-sharepoint-server.md)
  
    
    
 [Move site collections between databases in SharePoint Server](html/move-site-collections-between-databases-in-sharepoint-server.md)
  
    
    

  
    
    

