---
title: Install and configure RBS with a 3rd party provider for SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 7c877590-c6b4-48b2-aee3-330c5d42d44c
---


# Install and configure RBS with a 3rd party provider for SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how to install and configure Remote BLOB Storage (RBS) that uses a third-party RBS Provider for SharePoint Server 2016 and SharePoint Server 2013.SharePoint Server uses the RBS feature to store BLOBs outside the content database. For more information about RBS, see  [Overview of RBS in SharePoint Server](html/overview-of-rbs-in-sharepoint-server.md).
> [!IMPORTANT:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Install the RBS client library on each front-end or application server](#proc1)
    
  
-  [Install the third-party provider](#proc2)
    
  
-  [Enable RBS for each content database](#proc3)
    
  
-  [Test the RBS installation](#testRBS)
    
  

## Before you begin
<a name="begin"> </a>

You only have to install and configure RBS with the specific third-part provider one time for the farm. However, if you want to enable RBS using the FILESTREAM provider, use the procedure in  [Install and configure RBS with FILESTREAM in a SharePoint Server farm](html/install-and-configure-rbs-with-filestream-in-a-sharepoint-server-farm.md).Before you begin this operation, review the following information about prerequisites:
- The user account provisioning RBS stores must be a member of the **db_owner** fixed database role on each database that you are configuring RBS for.
    
  
- The user account installing the client library must be a member of the Administrators group on all of the computers where you are installing the library.
    
  
- The user account enabling RBS must have sufficient permissions to run PowerShell.
    
  

## Install the RBS client library on each front-end or application server
<a name="proc1"> </a>

You must install RBS client library on all Web servers in the SharePoint farm. The RBS client library is installed only one time per Web server, but RBS is configured separately for each associated content database. The client library consists of a client-side DLL that is linked into a user application, and also a set of stored procedures to be installed on SQL Server.
> [!WARNING:]

  
    
    

 **To install the RBS client library on the on the first front-end or application server**
1. Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.
    
  
2. On any front-end or application server, for SharePoint Server 2016, download the  [Microsoft SQL Server 2014 Feature Pack](http://go.microsoft.com/fwlink/p/?LinkID=733635&amp;clcid=0x409). Run the self-extracting download package to create an installation folder for the X64 RBS.msi file.
    
    For SharePoint Server 2013,  [download the RBS_amd64.msi file](https://go.microsoft.com/fwlink/p/?LinkId=271938).
    
  
3. Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content*  with the database name, and replace *DBInstanceName*  with the SQL Server instance name. You should run this command by using the specific database name and SQL Server instance name only one time. The operation should finish within approximately one minute.
    
  ```
  
msiexec /qn /lvx* rbs_install_log.txt /i RBS-x64.msi TRUSTSERVERCERTIFICATE=true FILEGROUP=PRIMARY DBNAME="WSS_Content " DBINSTANCE="DBInstanceName
  ```

 **To install the RBS client library on all additional front-end and application servers**
1. Confirm that the user account performing these steps is a member of the Administrators group on the computer where you are installing the library.
    
  
2. On any web server, for SharePoint Server 2016, download the  [Microsoft SQL Server 2014 Feature Pack](http://go.microsoft.com/fwlink/p/?LinkID=733635&amp;clcid=0x409). Run the self-extracting download package to create an installation folder for the X64 RBS.msi file.
    
    For SharePoint Server 2013,  [download the RBS_amd64.msi file](https://go.microsoft.com/fwlink/p/?LinkId=271938).
    
  
3. Copy and paste the following command into the Command Prompt window. Replace  *WSS_Content*  with the database name, and replace *DBInstanceName*  with the name of the SQL Server instance. The operation should finish within approximately one minute.
    
  ```
  msiexec /qn /lvx* rbs_install_log.txt /i RBS_x64.msi DBNAME="WSS_Content " DBINSTANCE="DBInstanceName " ADDLOCAL=Client,Docs,Maintainer,ServerScript,FilestreamClient,FilestreamServer
  ```

4. Repeat this procedure for all Web servers in the SharePoint farm.
    
  
5. Run the following command on each application server in the SharePoint farm: 
    
  ```
  Msiexec /qn /1vx* rbs_install_log.txt /I RBS_x64.msi ADDLOCAL="Client"
  ```

 **To confirm the RBS client library installation**
1. The rbs_install_log.txt log file is created in the same location as the RBS_x64.msi file. Open the rbs_install_log.txt log file by using a text editor and scroll toward the bottom of the file. Within the last 20 lines of the end of the file, an entry should read as follows: **Product: SQL Remote Blob Storage – Installation completed successfully**.
    
  
2. On the computer that is running SQL Server 2014 Service Pack 1 (SP1) or SQL Server 2008, verify that the RBS tables were created in the content database. Several tables should be listed under the content database that have names that are preceded by the letters "mssqlrbs". 
    
  

## Install the third-party provider
<a name="proc2"> </a>

The steps that you use to install the third-part provider will vary between manufacturers. Be sure to follow the instructions from the manufacturer of the provider.
## Enable RBS for each content database
<a name="proc3"> </a>

You must enable RBS on one front-end server in the SharePoint farm. It is not important which front-end server that you select for this activity, as long as RBS was installed on it by using the previous procedure. You must perform this procedure one time for each content database.
> [!NOTE:]

  
    
    

 **To enable RBS by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
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
    
  
For more information, see Get-SPContentDatabase.
## Test the RBS installation
<a name="testRBS"> </a>

You should test the RBS installation on one Web server in the SharePoint farm to make sure that that the system works correctly. **To test the RBS data store**
1. On the computer that contains the RBS data store, click **Start**, and then click **Computer**.
    
  
2. Browse to the RBS data store directory.
    
  
3. Confirm that the folder is empty.
    
  
4. On the SharePoint farm, upload a file to a document library. 
    
  
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
  
    
    

  
    
    

