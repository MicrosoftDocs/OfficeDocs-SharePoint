---
title: Install and configure RBS with FILESTREAM  in a SharePoint Server farm
ms.prod: SHAREPOINT
ms.assetid: 4cf30b48-f908-4774-920c-d2f2916f2c1b
---


# Install and configure RBS with FILESTREAM  in a SharePoint Server farm
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how use the FILESTREAM provider to enable Remote BLOB Storage (RBS) in a SharePoint Server 2016 and SharePoint Server 2013 farm.SharePoint Server uses the RBS feature to store binary large objects (BLOBs) outside the content database. For more information about RBS, see  [Overview of RBS in SharePoint Server](html/overview-of-rbs-in-sharepoint-server.md).Unless otherwise specified, the information in this article is specific to RBS using the FILESTREAM provider. For guidance specific to another provider, contact the provider manufacturer.
> [!TIP:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Enable FILESTREAM on the database server](#enable)
    
  
-  [Provision a BLOB store for each content database](#provision)
    
  
-  [Install the RBS client library on each front-end or application server](#library)
    
  
-  [Enable RBS for each content database](#enableRBS)
    
  
-  [Assign db_owner permissions to the web application](#dbOwnPerm)
    
  
-  [Test the RBS installation](#testRBS)
    
  

## Before you begin
<a name="begin"> </a>

You only have to install and configure RBS with the FILESTREAM provider one time for the farm. However, if you want to enable RBS using different providers for specific content databases, you must configure RBS to use those providers. For more information about doing that, see  [Install and configure RBS with a 3rd party provider for SharePoint Server](html/install-and-configure-rbs-with-a-3rd-party-provider-for-sharepoint-server.md).Before you begin this operation, review the following information about prerequisites:
- The user account used to perform the steps in the  [Provision a BLOB store for each content database](#provision) section must be a member of the **db_owner** fixed database role on each database that you are configuring RBS for.
    
  
- The user account installing the client library in the steps in the  [Install the RBS client library on each web server](#library) section must be a member of the Administrators group on all of the computers where you are installing the library.
    
  
- The user account enabling RBS in the  [Enable RBS for each content database](#enableRBS) section must have sufficient permissions to run Microsoft PowerShell.
    
  

## Enable FILESTREAM on the database server
<a name="enable"> </a>

By default, the FILESTREAM feature is installed when you install SQL Server. But it is not enabled. You must enable and configure FILESTREAM on the computer that is running SQL Server that hosts the SharePoint Server databases. You must:
1. Enable FILESTREAM for Transact-SQL access
    
  
2. Enable FILESTREAM for file I/O streaming access.
    
  
3. Allow remote clients to have streaming access to FILESTREAM data if you need remote client access.
    
  
To enable FILESTREAM for file I/O and to allow clients access, follow the instructions in  [Enable and Configure FILESTREAM](http://go.microsoft.com/fwlink/p/?LinkID=717992&amp;clcid=0x409). You only have to configure these settings one time for each database server where you want to use RBS.
## Provision a BLOB store for each content database
<a name="provision"> </a>

After you have enabled and configured FILESTREAM, provision a BLOB store on the file system as described in the following procedure. You must provision a BLOB store for each content database that you want to use RBS with. **To provision a BLOB store**
1. Confirm that the user account performing these steps is a member of the **db_owner** fixed database role on each database that you are configuring RBS for.
    
  
2. Open **SQL Server Management Studio**.
    
  
3. Connect to the instance of SQL Server that hosts the content database.
    
  
4. Expand **Databases**.
    
  
5. Click the content database for which you want to create a BLOB store, and then click **New Query**.
    
  
6. Paste the following SQL queries in **Query** pane, and then execute them in the sequence listed. In each case, replace *[WSS_Content]*  with the content database name, and replace *c:\\BlobStore*  with the volume\\directory in which you want the BLOB store created. The provisioning process creates a folder in the location that you specify. Be aware that you can provision a BLOB store only one time. If you attempt to provision the same BLOB store multiple times, you'll receive an error.
    
    > [!TIP:]
      

  ```
  
use [WSS_Content]
if not exists 
(select * from sys.symmetric_keys 
where name = N'##MS_DatabaseMasterKey##')
create master key encryption by password = N'Admin Key Password !2#4'
  ```


  ```
  
use [WSS_Content]
if not exists 
(select groupname from sysfilegroups 
where groupname=N'RBSFilestreamProvider')
alter database [WSS_Content] 
add filegroup RBSFilestreamProvider contains filestream
  ```


  ```
  
use [WSS_Content]
alter database [WSS_Content] 
 add file (name = RBSFilestreamFile, filename = 
'c:\\Blobstore' ) 
to filegroup RBSFilestreamProvider
  ```


## Install the RBS client library on each front-end or application server
<a name="library"> </a>

You must install RBS client library on all Front-end or Application servers in the SharePoint farm. The RBS client library is installed only one time per server, but RBS is configured separately for each associated content database. The client library consists of a client-side dynamic link library (DLL) that is linked into a user application, and a set of stored procedures that are installed on SQL Server.
> [!WARNING:]

  
    
    

 **To install the RBS client library on the on the first front-end or application server**
1. Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.
    
  
2. On any Front-end or Application server, download the correct RBS client based on the SQL Server version and SharePoint level that you use. 
    
    > [!NOTE:]
      

    For SharePoint Server 2016, choose the correct install from the following list:
    
  -  [Microsoft SQL Server 2014 Feature Pack](http://go.microsoft.com/fwlink/p/?LinkID=733635&amp;clcid=0x409)
    
  
  -  [Microsoft SQL Server 2014 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=46696)
    
  
  -  [Microsoft SQL Server 2014 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=53164)
    
  
  -  [Microsoft SQL Server 2016 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=52676)
    
  
  -  [Microsoft SQL Server 2016 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=54279)
    
  

    For SharePoint 2013, choose the correct install from the following list:
    
  -  [Microsoft® SQL Server® 2008 R2 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkID=177388)
    
  
  -  [Microsoft SQL Server 2008 R2 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=26728)
    
  
  -  [Microsoft SQL Server 2008 R2 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=30440)
    
  
  -  [Microsoft SQL Server 2008 R2 SP3 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=44272)
    
  
  -  [Microsoft SQL Server 2012 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=29065)
    
  
  -  [Microsoft SQL Server 2012 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=35580)
    
  
  -  [Microsoft SQL Server 2012 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=43339)
    
  
  -  [Microsoft SQL Server 2012 SP3 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=49999)
    
  
  -  [Microsoft SQL Server 2014 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=42295)
    
  
  -  [Microsoft SQL Server 2014 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=46696)
    
  
  -  [Microsoft SQL Server 2014 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=53164)
    
  
3. Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content*  with the database name, and replace *DBInstanceName*  with the SQL Server instance name. You should run this command by using the specific database name and SQL Server instance name only one time. The action should finish within approximately one minute.
    
  ```
  
msiexec /qn /lvx* rbs_install_log.txt /i RBS_amd64.msi TRUSTSERVERCERTIFICATE=true FILEGROUP=PRIMARY DBNAME="WSS_Content " DBINSTANCE="DBInstanceName " FILESTREAMFILEGROUP=RBSFilestreamProvider FILESTREAMSTORENAME=FilestreamProvider_1
  ```

 **To install the RBS client library on all additional front-end and application servers**
1. Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.
    
  
2. On any web server, download the correct RBS client based on the SQL Server version and SharePoint level that you use. Use one of the following lists to choose the correct install. Run the self-extracting download package to create an installation folder for the X64 RBS.msi file.
    
    > [!NOTE:]
      

    For SharePoint Server 2016, choose the correct install from the following list:
    
  -  [Microsoft SQL Server 2014 Feature Pack](http://go.microsoft.com/fwlink/p/?LinkID=733635&amp;clcid=0x409)
    
  
  -  [Microsoft SQL Server 2014 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=46696)
    
  
  -  [Microsoft SQL Server 2014 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=53164)
    
  
  -  [Microsoft SQL Server 2016 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=52676)
    
  
  -  [Microsoft SQL Server 2016 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=54279)
    
  

    For SharePoint 2013, choose the correct install from the following list:
    
  -  [Microsoft® SQL Server® 2008 R2 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkID=177388)
    
  
  -  [Microsoft SQL Server 2008 R2 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=26728)
    
  
  -  [Microsoft SQL Server 2008 R2 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=30440)
    
  
  -  [Microsoft SQL Server 2008 R2 SP3 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=44272)
    
  
  -  [Microsoft SQL Server 2012 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=29065)
    
  
  -  [Microsoft SQL Server 2012 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=35580)
    
  
  -  [Microsoft SQL Server 2012 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=43339)
    
  
  -  [Microsoft SQL Server 2012 SP3 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=49999)
    
  
  -  [Microsoft SQL Server 2014 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=42295)
    
  
  -  [Microsoft SQL Server 2014 SP1 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=46696)
    
  
  -  [Microsoft SQL Server 2014 SP2 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=53164)
    
  
3. Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content*  with the database name, and replace *DBInstanceName*  with the name of the SQL Server instance. The action should finish within approximately one minute.
    
  ```
  
msiexec /qn /lvx* rbs_install_log.txt /i RBS_amd64.msi DBNAME="WSS_Content " DBINSTANCE="DBInstanceName " ADDLOCAL=Client,Docs,Maintainer,ServerScript,FilestreamClient,FilestreamServer
  ```


    > [!NOTE:]
      

    After receiving this error, copy and paste the following command into the Command Prompt window without the /qn switch. This opens the RBS installer window where you can change only the database name and then follow the default options. You will then see the RBS tables are created in the second database.
    


  ```
  
msiexec  /lvx* rbs_install_log.txt /i RBS.msi TRUSTSERVERCERTIFICATE=true FILEGROUP=PRIMARY DBNAME="WSS_Content_RBS" DBINSTANCE="SQL2012SERVER" FILESTREAMFILEGROUP=RBSFilestreamProvider FILESTREAMSTORENAME=FilestreamProvider
  ```

4. Repeat this procedure for all front-end servers and application servers in the SharePoint farm.
    
    > [!NOTE:]
      
 **To confirm the RBS client library installation**
1. The rbs_install_log.txt log file is created in the same location as the RBS_amd64.msi file. Open the rbs_install_log.txt log file by using a text editor and scroll toward the bottom of the file. Within the last 20 lines of the end of the file, an entry should read as follows: **Product: SQL Remote Blob Storage – Installation completed successfully**.
    
  
2. On the computer that is running SQL Server 2014 Service Pack 1 (SP1) or SQL Server 2008, verify that the RBS tables were created in the content database. Several tables should be listed under the content database that have names that are preceded by the letters "mssqlrbs". 
    
  

## Enable RBS for each content database
<a name="enableRBS"> </a>

You must enable RBS on one web server in the SharePoint farm. It is not important which web server that you select for this activity, as long as RBS was installed on it by using the previous procedure. You must perform this procedure one time for each content database.
> [!NOTE:]

  
    
    

 **To enable RBS by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
2. Start the SharePoint Management Shell.
    
  
3. At the Microsoft PowerShell command prompt, type the following command:
    
  ```
  
$cdb = Get-SPContentDatabase <ContentDatabaseName>
$rbss = $cdb.RemoteBlobStorageSettings
$rbss.Installed()
$rbss.Enable()
$rbss.SetActiveProviderName($rbss.GetProviderNames()[0])
$rbss
  ```


    
    
    Where:
    
  -  *<ContentDatabaseName>*  is the name of the content database.
    
  
For more information, see **Get-SPContentDatabase**.
## Assign db_owner permissions to the web application
<a name="dbOwnPerm"> </a>


> [!IMPORTANT:]

  
    
    


## Test the RBS installation
<a name="testRBS"> </a>

You should test the RBS installation on one front-end server in the SharePoint farm to make sure that the system works correctly. **To test the RBS data store**
1. On the computer that contains the RBS data store, click **Start**, and then click **Computer**.
    
  
2. Browse to the RBS data store directory.
    
  
3. Confirm that the folder is empty.
    
  
4. On the SharePoint farm, upload a file that is at least 100 kilobytes (KB) to a document library. 
    
  
5. On the computer that contains the RBS data store, click **Start**, and then click **Computer**.
    
  
6. Browse to the RBS data store directory.
    
  
7. Browse to the file list and open the file that has the most recent changed date. This should be the file that you uploaded.
    
  

# See also

#### 

 [Overview of RBS in SharePoint Server](html/overview-of-rbs-in-sharepoint-server.md)
  
    
    
 [Deciding to use RBS in SharePoint Server](html/deciding-to-use-rbs-in-sharepoint-server.md)
  
    
    

#### 

 [Remote Blob Store (RBS) (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=733607&amp;clcid=0x409)
  
    
    
 [Enable and Configure FILESTREAM](http://go.microsoft.com/fwlink/p/?LinkID=717992&amp;clcid=0x409)
  
    
    

  
    
    

