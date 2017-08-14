---
title: A State Service Application has no database defined (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: f2bd109d-83ce-4bf5-aec8-2c7df2ff5c3b
---


# A State Service Application has no database defined (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "A State Service Application has no database defined." **Rule Name:**    A State Service Application has no database defined **Summary:**    A State Service service application has no State Service database defined. This may result in errors when using some SharePoint components such as InfoPath Web browser forms and the Microsoft SharePoint Server Chart Web Part. **Cause:**    One or more of the following might be causing this:
- The farm administrator deleted all databases associated with the State Service service application.
    
  
- The farm administrator never created or associated a database with the State Service service application.
    
  
 **Resolution:   Create a new database or use an existing database for the State Service service application by using Microsoft PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. If no database already exists that you can use, type the following command at the PowerShell command prompt:
    
  ```
  
New-SPStateServiceDatabase -Name <DatabaseName>  -DatabaseServer <ServerName>  [-DatabaseCredentials <Credential> ] [-ServiceApplication <ID> ]
  ```


    Where:
    
  -  *<DatabaseName>*  is name of the database as a String.
    
  
  -  *<ServerName>*  is name of the database server.
    
  
  -  *<Credential>*  is SQL Server authentication credentials for the database. If this parameter is not used, Windows authentication will be used.
    
  
  -  *<ID>*  is the identifier for the State Service service application as a string or a GUID. If there is only one State Service service application, you do not have to specify this parameter.
    
  
4. In some environments, you must connect to an existing, empty SQL database. In this case, type the following command at the Windows PowerShell command prompt:
    
  ```
  Mount-SPStateServiceDatabase -Name <DatabaseName>  -DatabaseServer <ServerName>  [-DatabaseCredentials <Credential> ] [-ServiceApplication <ID> ]
  ```


    Where:
    
  -  *<DatabaseNname>*  is name of the database as a String.
    
  
  -  *<ServerName>*  is name of the database server.
    
  
  -  *<Credential>*  is the SQL Server authentication credentials for the database. If this parameter is not used, Windows authentication will be used.
    
  
  -  *<ID>*  is the identifier for the State Service service application as a string or a GUID. If there is only one State Service service application, you do not have to specify this parameter.
    
  
For more information, see Mount-SPStateServiceDatabase or New-SPStateServiceDatabase. 
