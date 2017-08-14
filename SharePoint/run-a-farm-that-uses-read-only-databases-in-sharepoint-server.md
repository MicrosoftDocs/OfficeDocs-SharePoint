---
title: Run a farm that uses read-only databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 8b91dc0a-c37d-4ec8-aa75-deb3f268fb97
---


# Run a farm that uses read-only databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to run a read-only SharePoint Server 2016 and SharePoint Server 2013 farm with some or all databases set as read-only.You can use Microsoft PowerShell or SQL Server tools to set your SharePoint Server databases to read-only. The tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Prepare users for the read-only experience](#proc1)
    
  -  [Sites that use read-only content databases](#sites)
    
  
  -  [Farms that use read-only service application databases](#farms)
    
  
-  [Set content databases to be read-only](#proc2)
    
  -  [To determine which content database is associated with a site collection by using Windows PowerShell](#PS)
    
  
  -  [To set content databases to read-only by using SQL Server](#SQL)
    
  
-  [Set service application databases to read-only](#proc3)
    
  -  [To set service application databases to read-only by using SQL Server](#setsrvc)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about the settings that make a read-only farm.A farm is considered read-only if one of the following is true: 
- All content databases are set to read-only.
    
  
- Service application databases are set to read-only.
    
    > [!NOTE:]
      
The functionality and user experience in a read-only farm depends on the databases that are set to read-only.
> [!NOTE:]

  
    
    


## Prepare users for the read-only experience
<a name="proc1"> </a>

If you plan to give users access to a read-only site or farm, you should set expectations for tasks that users can complete on the site and the behavior of the user interface (UI).
## Sites that use read-only content databases
<a name="sites"> </a>

The user experience of a site that uses a content database that is set to read-only is characterized by the following:
- A statement at the top of the home page states that the site is read-only.
    
  
- Common tasks that do not require writing to the content database are fully available.
    
  
- Common tasks that require writing to the content database are not available either because the UI for the task is not available or because the user cannot apply changes to complete the task.
    
  
- Some common tasks that require writing to the content database and that appear to be available return errors.
    
  

## Farms that use read-only service application databases
<a name="farms"> </a>

The user experience on a farm that uses service application databases that are set to read-only is characterized by the following:
- Common tasks that do not require writing to the service databases are fully available.
    
  
- All common tasks that require writing to the service databases and that appear to be available return errors.
    
  

## Set content databases to read-only
<a name="proc2"> </a>

Before you set content databases to read-only, you may need to determine the content database that is associated with a particular site collection. **To determine the content database that is associated with a site collection by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPContentDatabase -Site <Site URL>
  ```


    
    
    Where:
    
  -  *<Site URL>*  is the site collection URL for which you want to know the associated content database.
    
    The command returns the content database that is associated with the site.
    
  
For more information, see **Get-SPContentDatabase**.
> [!NOTE:]

  
    
    

You can follow these steps to set read/write content databases to be read-only by using SQL Server Management Studio. You can also use the Transact-SQL ALTER DATABASE statement to set content databases to be read-only. For more information, see [ALTER DATABASE (Transact-SQL)](http://go.microsoft.com/fwlink/p/?LinkID=717355&amp;clcid=0x409).
> [!IMPORTANT:]

  
    
    

 **To set content databases to read-only by using SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.
    
  
2. Start SQL Server Management Studio.
    
  
3. Right-click the content database that you want to make read-only, and then click **Properties**.
    
  
4. Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.
    
  
5. In the **Database Read-Only** row, click the arrow next to **False**, select **True**, and then click **OK**.
    
  
6. Repeat for all other content databases.
    
    > [!NOTE:]
      
The site collection that is associated with a read-only content database is automatically set to read-only if the locking status of the site collection was previously None, No Additions, or Read-Only. If the locking status of the site collection was previously No Access, it remains No Access when the database locking status is changed.
## Set service application databases to read-only
<a name="proc3"> </a>

It is possible to set any service application database to read-only. However, some service applications do not function when their databases are set to read-only, such as those that are associated with Search and Project Server. **To set service application databases to read-only by using SQL Server**
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.
    
  
2. Start SQL Server Management Studio.
    
  
3. Right-click the database that you want to make read-only, and then click **Properties**.
    
  
4. Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.
    
  
5. In the **Database Read-Only** row, click the arrow next to **False**, select **True**, and then click **OK**.
    
  
6. Repeat for other service application databases as appropriate. 
    
    > [!NOTE:]
      

