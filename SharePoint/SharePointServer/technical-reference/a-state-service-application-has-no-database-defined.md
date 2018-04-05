---
title: "A State Service Application has no database defined (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 2/22/2018
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f2bd109d-83ce-4bf5-aec8-2c7df2ff5c3b
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleA State Service Application has no database defined."
---

# A State Service Application has no database defined (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "A State Service Application has no database defined." 
  
 **Rule Name:** A State Service Application has no database defined 
  
 **Summary:** A State Service service application has no State Service database defined. This may result in errors when using some SharePoint components such as InfoPath Web browser forms and the Microsoft SharePoint Server Chart Web Part. 
  
 **Cause:** One or more of the following might be causing this: 
  
- The farm administrator deleted all databases associated with the State Service service application.
    
- The farm administrator never created or associated a database with the State Service service application.
    
**Resolution: Create a new database or use an existing database for the State Service service application by using Microsoft PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
    For more information about how to interact with Windows Server 2012, see [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
3. If no database already exists that you can use, type the following command at the PowerShell command prompt:
    
  ```
  New-SPStateServiceDatabase -Name <DatabaseName> -DatabaseServer <ServerName> [-DatabaseCredentials <Credential>] [-ServiceApplication <ID>]
  ```

    Where:
    
  -  _\<DatabaseName\>_ is name of the database as a String. 
    
  -  _\<ServerName\>_ is name of the database server. 
    
  -  _\<Credential\>_ is SQL Server authentication credentials for the database. If this parameter is not used, Windows authentication will be used. 
    
  -  _\<ID\>_ is the identifier for the State Service service application as a string or a GUID. If there is only one State Service service application, you do not have to specify this parameter. 
    
4. In some environments, you must connect to an existing, empty SQL database. In this case, type the following command at the Windows PowerShell command prompt:
    
  ```
  Mount-SPStateServiceDatabase -Name <DatabaseName> -DatabaseServer <ServerName> [-DatabaseCredentials <Credential>] [-ServiceApplication <ID>]
  ```

    Where:
    
  -  _\<DatabaseNname\>_ is name of the database as a String. 
    
  -  _\<ServerName\>_ is name of the database server. 
    
  -  _\<Credential\>_ is the SQL Server authentication credentials for the database. If this parameter is not used, Windows authentication will be used. 
    
  -  _\<ID\>_ is the identifier for the State Service service application as a string or a GUID. If there is only one State Service service application, you do not have to specify this parameter. 
    
For more information, see [Mount-SPStateServiceDatabase](http://technet.microsoft.com/library/bd559347-c8f9-4ecf-9fbc-17821ae0afc4.aspx) or [New-SPStateServiceDatabase](http://technet.microsoft.com/library/221e439c-c501-4d4c-9d8a-171a01e67e25.aspx). 
  

