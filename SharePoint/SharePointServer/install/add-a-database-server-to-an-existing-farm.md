---
title: "Add a database server to an existing farm in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0b35af11-ad5b-4a62-922d-125194d3f606
description: "Learn how to add a new database server to an existing SharePoint farm."
---

# Add a database server to an existing farm in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
You can add more database servers at any time to respond to business or operations requirements. Because a database server contains the farm content, which can consist of diverse types of data and can have a fast growing document collection, the size of the farm databases can grow quickly. Storage capacity is often the key reason to add more database servers. Other reasons can include adding new features, improving performance and high availability.
  
    
## Before you begin
<a name="begin"> </a>

Normally, all that is required to add a database server to an existing SharePoint farm is to set up and configure a new database server and join it to the farm by referencing the new server when you add a feature or move database content to the new server. SharePoint 2013 automatically allocates and assigns new database resources as necessary when they are required.
  
> [!NOTE]
> In the case of high availability, this is typically implemented as part of the initial farm topology design and deployment and is not included in this article. For more information about high availability for SQL Server 2008 R2 and SQL Server 2012, see [High Availability Solution Overview](https://go.microsoft.com/fwlink/p/?LinkId=264948) and [High Availability Solutions (SQL Server)](https://go.microsoft.com/fwlink/p/?LinkId=264949). 
  
The procedures in this article are intended to show how to configure a new database server for a specific task in SharePoint 2013.
  
## Prepare the new database server
<a name="proc1"> </a>

Before you can use the new database server, you must prepare it so that it can be used in a SharePoint 2013 farm. Use the following steps as guidance to provision the new server.
  
> [!IMPORTANT]
> IT policy may require a database administrator (DBA) to complete some or all steps in these procedures. 
  
 **To provision the database server**
  
1. Verify that the user account that is performing this procedure is a member of the SQL Server database **dbcreator** fixed server role, the Farm Administrators SharePoint group, and Administrators group on the server. 
    
2. Review [Hardware and software requirements for SharePoint 2013](hardware-and-software-requirements-0.md)
    
3. Install the operating system, and make sure that the following conditions are satisfied:
    
  - The disk configuration is the same as the existing server.
    
  - The operating system is updated to the same service pack or hotfix level as the existing server.
    
4. Install the same version of SQL Server that is installed on the existing farm database server. 
    
    For information about how to install and configure SQL Server 2008 R2 with Service Pack 1 (SP1) or SQL Server 2012 before you add them to an existing server farm, see [SQL Server Installation (SQL Server 2008 R2)](https://go.microsoft.com/fwlink/p/?LinkId=264940)or[Quick-Start Installation of SQL Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=264941).
    
5. Configure SQL Server, and confirm the following:
    
  - The database collation is LATIN1_General_CI_AS_KS_WS.
    
  - A logon account is created for the SharePoint 2013 Setup user account. This account will be the database owner for the new database.
    
6. Install the same SQL Server service packs and hotfixes that are installed on the existing database server.
    
## Configure and use the new database server
<a name="proc2"> </a>

Use the following procedures as a guide to configure a new database server to host specific SharePoint databases. This includes the following:
  
- Create a new web application.
    
- Move a site collection to the new server.
    
You can use either the SharePoint Central Administration website or Microsoft PowerShell to create a new web application. You must use PowerShell to move a site collection.
  
 **To create a new web application**
  
1. Verify that the user account that is performing this procedure is a member of the SQL Server database **dbcreator** fixed server role and the Farm Administrators SharePoint group. 
    
2. Use the Application Management page in the SharePoint Central Administration website to create a new web site.
    
3. Configure either classic mode authentication (Windows authentication) or claims-based authentication.
    
4. Configure IIS to use either the existing web site or create a new web site and configure the following settings:
    
  - Specify the port number that you want to use to access the web application.
    
  - Provide the URL you want to use to access the web application (optional).
    
  - Provide the path of the site directory on the server where the web site is hosted.
    
5. Configure authentication and encryption for your web by using the following options.
    
  - Negotiate (Kerberos) or NTLM authentication
    
  - Anonymous access to the web site
    
  - Secure Sockets Layer (SSL)
    
6. Provide a URL for the domain name for all sites that users will access in this web application.
    
7. Use the existing application pool or create a new one.
    
8. Configure security for the application pool (predefined or configurable).
    
9. Identify the database server, database name, and authentication method for your new web application.
    
For detailed instruction, see Create a web application (SharePoint 2013).
  
 **To move a site collection by using PowerShell**
  
1. The SharePoint 2013 content database stores all site content for a farm, this includes the site collection. Content databases can store more than one site collection. Whether you move a site collection between database servers or between databases the procedure is the same. If the site collection grows too large then it can be moved to a new content database using the same procedure.
    
2. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
3. Verify that the following conditions are true:
    
  - The destination content database exists.
    
  - The source content database and destination content database reside on the same instance of SQL Server.
    
  - The source content database and destination content database are attached to the same web application.
    
4. Determine the size of the source site collection and verify that the destination hard disk has at least three times more free space than is required for the site collection.
    
    Use the **Get-SPSiteAdministration** cmdlet to determine the size of a site collection. For more information, see [Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps)
    
5. Use the **Move-SPSite** cmdlet to move a site collection from the source content database to the new content database. For more information, see [Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps).
    
    For detailed instructions, see [Move site collections between databases in SharePoint Server](../administration/move-site-collections-between-databases.md).
    
## See also
<a name="proc2"> </a>

#### Other Resources

[Deploy Windows Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkID=166501)
  
[Install and Deploy Windows Server 2012](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831620(v=ws.11))
  
[SQL Server Installation (SQL Server 2008 R2)](https://go.microsoft.com/fwlink/p/?LinkID=264940)
  
[Install SQL Server 2012](https://go.microsoft.com/fwlink/p/?LinkID=141021)

