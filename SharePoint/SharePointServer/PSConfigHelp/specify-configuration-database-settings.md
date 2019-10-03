---
title: "Specify configuration database settings"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c9038bd2-c314-48da-8745-7a64e530bad9
description: "Summary: Learn how to configure database settings in SharePoint Server."
---

# Specify configuration database settings

 **Summary:** Learn how to configure database settings in SharePoint Server. 
  
The configuration database is used to store configuration and site-mapping information for your server farm. There must be one configuration database for your server farm whether your server farm is one computer with everything on it, or several computers.
  
## Database Settings

You must provide connectivity settings to an existing database server through an existing user account.
  
### Database server

You must type the name for the computer that is running a supported version of the 64 bit edition of SQL Server 2014 SP1. You can type the name of the computer that is running SQL Server as either server or server\instance.
  
### Database name

If you are creating a new configuration database, you can either type the name of the database for the configuration wizard to create, or you can type the name of a database that has been provisioned in advance. If you want to use an existing database you must run Psconfig.exe from the command line to connect to that database, and it must not contain any tables, stored procedures, or other objects. 
  
If you are connecting to an existing configuration database, you can click **Retrieve Database Names**. The configuration databases that exist on the computer that is running SQL Server will be returned, and you can choose the appropriate configuration database.
  
### Database access account

You must enter the credentials for an existing user account that will always be used to connect to the configuration database. If the configuration database is hosted on a different computer, you must provide the credentials for a domain account.
  
Although you can enter either a local or a domain account in installations in which you are using a SQL Server installation, a local account will work only for single-server deployments. We recommend that you use a domain account so that you preserve the flexibility to later add more computers to the farm.
  
To deploy SharePoint products in a server farm environment, you will need a unique domain user account that you can specify as the SharePoint service account. This user account is used to access the configuration database. The database access account will be used for both initial database configuration, and ongoing connections from servers in this farm to the databases.
  
> [!IMPORTANT]
> Ensure that your domain does not have Group Policy that prohibits the account chosen as your database access account from running as a service. 
  
This account also acts as the application pool identity for the SharePoint Central Administration application pool and it is the account under which the SharePoint Timer service runs. The SharePoint 2016 Products Configuration Wizard adds this account to the SQL Server Logins, the SQL Server Database Creator server role, and the SQL Server Security Administrators server role. We recommend that you follow the principle of least privilege and do not make this user account a member of any particular security group on your web servers or your database servers. 
  
The database access account must have the following permissions: security administrator, database creator, and database owner (DBO) of all SharePoint databases. If you run Psconfig.exe from the command line to install and specify the account using SQL authentication, then permissions for this account must be configured in SQL Server. The configuration wizard does not perform this configuration when you run the Psconfig.exe file from the command line with the SQL authentication option.
  
The account that you specify for database access must have the following properties, at minimum:
  
- The ability to read from and write to the configuration database.
    
- Server-wide permissions (security administrator) in SQL Server.
    
- To create and add a schema, the account must have DBO permissions.
    
Additionally, if the configuration wizard is creating a new configuration database, the database access account must have the following permissions:
  
- Create Database
    
- Create Procedure
    
## Tasks

To create the configuration database, the configuration wizard performs the following tasks:
  
1. Validate that SQL Server meets minimum requirements.
    
2. Either create a new database or connect to an existing empty database.
    
3. Add database schema to a new configuration database.
    
4. Add current server to the topology.
    
5. Add database access account credentials to the configuration database.
    
6. Write database connection string to the registry on the local computer.
    
To disconnect from a configuration database, the configuration wizard performs the following tasks:
  
1. Remove the configuration database connection string.
    
2. Stop the job/task scheduling NT service running on the local computer.
    
3. Remove computer-specific data from the old configuration database.
    

