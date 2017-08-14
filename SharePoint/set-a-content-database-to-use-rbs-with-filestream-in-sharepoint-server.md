---
title: Set a content database to use RBS with FILESTREAM in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 83ee2a38-1b91-4c6a-83de-1e968db74611
---


# Set a content database to use RBS with FILESTREAM in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how to set a SharePoint Server 2016 and SharePoint Server 2013 content database to use Remote BLOB Storage (RBS) with FILESTREAM.This article describes how to set a content database to use Remote BLOB Storage (RBS) that uses the FILESTREAM provider. If you are using a third-party provider, these instructions might not apply. For more information, contact the manufacturer of the provider. These instructions assume that you have already installed RBS for use with SharePoint Server. To install and configure RBS, see  [Install and configure RBS with FILESTREAM in a SharePoint Server farm](html/install-and-configure-rbs-with-filestream-in-a-sharepoint-server-farm.md). In this article:
-  [Before you begin](#begin)
    
  
-  [Set a content database to use RBS](#proc1)
    
  

## Before you begin
<a name="begin"> </a>

You must perform this procedure on every content database that you want to set to use RBS.Before you begin this operation, review the following information about prerequisites:
- The user account that you use to perform this procedure is a member of the Administrators group on the Web.
    
  
- The user account that you use to perform this procedure is a member of the SQL Server **dbcreator** and **securityadmin** fixed server roles on the computer that is running SQL Server 2014 Service Pack 1 (SP1), SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, or SQL Server 2014.
    
  

## Set a content database to use RBS
<a name="proc1"> </a>

To set a content database to use RBS, you must provision a binary large object (BLOB) store in SQL Server, add the content database information to the RBS configuration on a front-end or application server, and then test the RBS data store. These instructions assume that you have installed SQL Server Management Studio on the database server. You can perform the following procedures on any front-end or application server or application server in the farm. 
> [!NOTE:]

  
    
    

 **To set a content database to use RBS**
1. Verify that the user account that you use to perform this procedure is a member of the Administrators group on the Web server, and is a member of the SQL Server **dbcreator** and **securityadmin** fixed server roles on the computer that is running SQL Server 2014 SP1, SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, or SQL Server 2014.
    
  
2. Open SQL Server Management Studio.
    
  
3. In the **Connect to Server** dialog box, specify the server type, server name, and authentication method of the database server that you want to connect to, and then click **Connect**.
    
  
4. Expand **Databases**.
    
  
5. Right-click the content database for which you want to create a BLOB store, and then click **New Query**.
    
  
6. In the **Query** pane, copy and execute the following SQL queries in the sequence that is provided.
    
  ```
  
use [ContentDbName]
if not exists (select * from sys.symmetric_keys where name = N'##MS_DatabaseMasterKey##')
create master key encryption by password = N'Admin Key Password !2#4'
  ```


  ```
  
use [ContentDbName]
if not exists (select groupname from sysfilegroups where groupname=N'RBSFilestreamProvider')
alter database [ContentDbName]  add filegroup RBSFilestreamProvider contains filestream

  ```


  ```
  
use [ContentDbName]
alter database [ContentDbName]  add file (name = RBSFilestreamFile, filename = 'c:\\RBSStore' ) to filegroup RBSFilestreamProvider
  ```


    Where  *[ContentDbName]*  is the content database name and *c:\\RBSStore*  is the volume\\directory that will contain the RBS data store. Be aware that you can provision a RBS store only one time. If you attempt to provision the same RBS data store multiple times, you will receive an error.
    
    > [!TIP:]
      
7. Right-click **Start**, click **Run**, type **cmd** into the **Run** text box, and then click **OK**.
    
  
8. Copy and paste the following command at the command prompt: 
    
  ```
  
msiexec /qn /i rbs.msi REMOTEBLOBENABLE=1 FILESTREAMPROVIDERENABLE=1 DBNAME=<ContentDbName>  FILESTREAMSTORENAME=FilestreamProvider_1 ADDLOCAL=EnableRBS,FilestreamRunScript DBINSTANCE=<DBInstanceName> >

  ```


    Where  *<ContentDbName>*  is the name of the content database, and *<DBInstanceName>*  is the name of the SQL Server. The operation should finish within approximately one minute.
    
  
 **To test the RBS data store**
1. Connect to a document library on any front-end or application server.
    
  
2. Upload a file that is at least 100 kilobytes (KB) to the document library.
    
  
3. On the computer that contains the RBS data store, click **Start**, and then click **Computer**.
    
  
4. Navigate to the RBS data store directory.
    
  
5. Locate the folder that has the most recent modification date, other than the $FSLOG folder. Open this folder and locate the file that has the most recent modification date. Verify that this file has the same size and contents as the file that you uploaded. If does not, make sure that RBS is installed and enabled correctly.
    
  

# See also

#### 

 [Overview of RBS in SharePoint Server](html/overview-of-rbs-in-sharepoint-server.md)
  
    
    
 [Migrate content into or out of RBS in SharePoint Server](html/migrate-content-into-or-out-of-rbs-in-sharepoint-server.md)
  
    
    

  
    
    

