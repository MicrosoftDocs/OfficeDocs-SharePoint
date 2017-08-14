---
title: All State Service databases are paused for a State Service Application (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 8386d324-816a-42ee-aff2-ce135ca2f241
---


# All State Service databases are paused for a State Service Application (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "All State Service databases are paused for a State Service Application." **Rule Name:**    All State Service databases are paused for a State Service Application **Summary:**    All of the databases associated with a State Service service application are paused. This may result in errors when using some SharePoint Server 2016 components such as InfoPath Web browser forms and the Microsoft SharePoint Chart Web Part. **Cause:**    This might be caused by the administrator pausing all databases for the service application. **Resolution:   Resume the State Service service application databases by using Microsoft PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. To identify the paused database, type the following command at the PowerShell command prompt:
    
  ```
  
Get-SPStateServiceDatabase
  ```

4. If you want to resume a paused database, type the following command at the Windows PowerShell command prompt:
    
  ```
  Resume-SPStateServiceDatabase -Identity <DatabaseID>
  ```


    Where:
    
  -  *<DatabaseID>*  is the identifier for the State Service service application database as a GUID.
    
  
5. If you want to create a new database instead of using an existing database, type the following command at the Windows PowerShell command prompt:
    
  ```
  New-SPStateServiceDatabase -Name <DatabaseName>  -ServiceApplication <ID>  -DatabaseServer <ServerName>  [-DatabaseCredentials <Credential> ] 
  ```


    Where:
    
  -  *<DatabaseName>*  is name of the database as a string.
    
  
  -  *<ID>*  is the identifier for the affected State Service service application as a string or a GUID. If there is only one State Service service application, you do not have to specify this parameter.
    
  
  -  *<ServerName>*  is name of the database server.
    
  
  -  *<Credential>*  is SQL Server authentication credentials for the database server. If this parameter is not specified, Windows authentication will be used.
    
  
For more information, see Resume-SPStateServiceDatabase or New-SPStateServiceDatabase. 
