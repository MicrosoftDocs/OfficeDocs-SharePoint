---
title: "Configure AdventureWorks for Business Intelligence solutions"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 5e44cf6c-2271-4ff1-af7f-4e73849ffdf6
description: "Configure the AdventureWorks sample data for use with Excel, Excel Services in SharePoint Server 2013, and PerformancePoint Services business intelligence scenarios."
---

# Configure AdventureWorks for Business Intelligence solutions

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
The AdventureWorks sample data set provides a sample database, data warehouse, and OLAP cube. The subsequent articles in this section make use of this sample data to demonstrate Business Intelligence capabilities in Excel, Excel Services in SharePoint Server 2013, and PerformancePoint Services. This article describes how to install and configure the AdventureWorks sample data set and configure a Business Intelligence Center on your SharePoint Server 2013 farm.
  
> [!IMPORTANT]
> This scenario applies only to SharePoint Server 2013 Enterprise. 
  
    
## Scenario overview
<a name="overview"> </a>

Installing the AdventureWorks sample data set consists of downloading the sample data, attaching the sample databases in SQL Server Management Studio, and deploying the sample OLAP cube using the SQL Server Data Tools.
  
Creating a Business Intelligence Center consists of creating a new site collection with the Business Intelligence Center template using the SharePoint Central Administration website.
  
The procedures for completing both of these tasks, plus procedures for configuring the required user access and permissions are included in this article.
  
## Before you begin
<a name="begin"> </a>

Before starting, read the following information about permissions and software requirements:
  
- To deploy the AdventureWorks sample data, you must be a SQL Server and Analysis Services administrator.
    
- To create a Business Intelligence Center, you must be a farm administrator on the SharePoint Server 2013 farm.
    
The subsequent articles make use of Excel Services and PerformancePoint Services. It is assumed that these are configured on your farm. For information about deploying Excel Services, see [Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md) and [Configure Excel Services in SharePoint Server 2013](/SharePoint/administration/configure-excel-services). 
  
When using Excel Services or PerformancePoint Services, user access can be provided using Windows Authentication with Kerberos delegation, the Secure Store Service, or, with OLAP data sources, the EffectiveUserName feature. It is assumed that one or more of these options are configured on your farm. For information about configuring Secure Store, see [Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)) and [Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md). For information about configuring the EffectiveUserName feature for OLAP data sources, see [Use Analysis Services EffectiveUserName in SharePoint Server](use-analysis-services-effectiveusername-in-sharepoint-server.md).
  
## Video demonstration
<a name="VideoDemonstration"> </a>

This video shows the steps involved in installing and configuring the AdventureWorks sample data set, as described in this article.
  
**Video: Configure AdventureWorks for Business Intelligence solutions**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/f30286e4-f448-4480-ab49-99c014d88144?autoplay=false]
## Install the AdventureWorks sample data
<a name="InstallAdventureWorks"> </a>

The AdventureWorks sample data consists of:
  
- The AdventureWorks2012 database
    
- The AdventureWorksDW2012 database
    
- The AdventureWorksDW2012Multidimensional-EE OLAP cube
    
The following sections describe how to deploy each of these data sets.
  
### Deploy the AdventureWorks sample databases
<a name="InstallSampleDBs"> </a>

Each of the two AdventureWorks sample databases must be downloaded separately.
  
Use the following procedure to download and deploy the AdventureWorks2012 database.
  
 **To deploy the AdventureWorks2012 database**
  
1. Download [AdvetureWorks Database 2012](https://docs.microsoft.com/sql/samples/adventureworks-install-configure).
    
    > [!NOTE]
    > Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.) 
  
2. Copy AdventureWorks2012_Data.mdf to your default database directory (normally \Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA) or other location as designated by your database administrator.
    
3. Open SQL Server Management Studio.
    
4. Connect to the database engine.
    
5. Right-click **Databases**, and then click **Attach**.
    
6. On the **Attach Databases** dialog box, click **Add**.
    
7. Navigate to the location where you copied AdventureWorks2012_Data.mdf, select the file, and then click **OK**.
    
8. Under **"AdventureWorks2012" database details**, select the row where **File Type** is **Log**.
    
9. Click **Remove**.
    
10. Click **OK**.
    
Use the following procedure to download and deploy the AdventureWorksDW2012 data warehouse database.
  
 **To deploy the AdventureWorksDW2012 data warehouse**
  
1. Download [AdvetureWorks Database 2012](https://docs.microsoft.com/sql/samples/adventureworks-install-configure).
    
    > [!NOTE]
    > Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.) 
  
2. Copy AdventureWorksDW2012_Data.mdf to your default database directory (normally \Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA) or other location as designated by your database administrator.
    
3. Open SQL Server Management Studio.
    
4. Connect to the database engine.
    
5. Right-click **Databases**, and then click **Attach**.
    
6. On the **Attach Databases** dialog box, click **Add**.
    
7. Navigate to the location where you copied AdventureWorksDW2012_Data.mdf, select the file, and then click **OK**.
    
8. Under **"AdventureWorksDW2012" database details**, select the row where **File Type** is **Log**.
    
9. Click **Remove**.
    
10. Click **OK**.
    
### Deploy the AdventureWorks sample OLAP cube
<a name="InstallSampleDBs"> </a>

The following requirements must be met before you can deploy the sample OLAP cube. Procedures are provided to accomplish each of these tasks if they have not already been completed in your environment.
  
- The AdventureWorksDW2012 database must be deployed on the SQL Server database engine as covered in the section above.
    
- The SQL Server Data Tools must be installed as part of your SQL Server and Analysis Services deployment.
    
    > [!NOTE]
    > SQL Server Data Tools was known as Business Intelligence Developer Studio (BIDS) in previous versions of SQL Server. 
  
- The account running the Analysis Services service must have a login on the SQL Server database engine.
    
If you have not deployed the AdventureWorksDW2012 database, do so now before proceeding with the procedures in this section. 
  
If you have not deployed the SQL Server Data Tools, use the following procedure to deploy them.
  
> [!NOTE]
> You can determine if the SQL Server Data Tools are installed by clicking **Start**, **All Programs**, and then **Microsoft SQL Server 2012** on the computer running SQL Server. If the SQL Server Data Tools are installed, it will appear in the menu under **Microsoft SQL Server 2012**. 
  
 **To install the SQL Server Data Tools**
  
1. On the SQL Server 2012 DVD, run setup.exe.
    
2. In the SQL Server Installation Center, on the left pane, click **Installation**.
    
3. In the right pane, click **New SQL Server stand-alone installation or add features to an existing installation**.
    
4. On the Setup Support Rules page, click **OK**.
    
5. On the Product Updates page click **Next**.
    
6. On the Setup Support Rules page, click **Next**.
    
7. On the Installation Type page, select the **Add features to an existing instance of SQL Server 2012** option, and select the instance where you want to install the SQL Server Data Tools. 
    
8. Click **Next**.
    
9. On the Feature Selection page, select the **SQL Server Data Tools** check box, and then click **Next**.
    
10. On the Installation Rules page, click **Next**.
    
11. On the Disk Space Requirements page, click **Next**.
    
12. On the Error Reporting page, click **Next**.
    
13. On the Installation Configuration Rules page, click **Next**.
    
14. On the Ready to Install page, click **Install**.
    
15. When the installation completes, click **Close**.
    
Once the SQL Server Data Tools have been installed, the next step is to create a login for the account running Analysis Services if one does not already exist.
  
If you do not know what account is running Analysis Services, use the following procedure to determine the account.
  
 **To determine the Analysis Services service account**
  
1. On the computer running Analysis Services, click **Start**, click **All Programs**, click **Microsoft SQL Server 2012**, click **Configuration Tools**, and then click **SQL Server Configuration Manager**.
    
2. In the left pane, click **SQL Server Services**.
    
3. In the right pane, find the instance of Analysis Services that you will be using, and note the account listed in the **Log On As** column. This is the account for which you must add a logon in SQL Server. 
    
If you do not already have a SQL Server login for the account running Analysis Services, use the following procedure to create one.
  
 **To add a login for the Analysis Services service account**
  
1. Open SQL Server Management Studio.
    
2. Connect to the database engine.
    
3. Expand **Security**.
    
4. Right-click **Logins** and click **New Login**.
    
5. In the **Login name** text box, type the name of the account running the Analysis Services service. 
    
6. Click **OK**.
    
    > [!NOTE]
    > This login does not require any Server Roles other than the default role of Public. No User Mapping is necessary. 
  
Once you have configured the login for the Analysis Services service account, the next step is to download and deploy the AdventureWorks OLAP cube. Use the following procedure to download and deploy the cube.
  
 **To configure the AdventureWorks OLAP cube**
  
1. Download [AdventureWorks Multidimensional Models SQL Server 2012](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks)
    
    > [!NOTE]
    > Because this file was downloaded from the Internet, it may be blocked by Windows. Right-click the file, and then click **Properties**. Click the **Unblock** button if it is present, and then click **OK**. (If the **Unblock** button is not present, then the file is not blocked.) 
  
2. Unzip the file to a location on the computer running Analysis Services.
    
3. In the **Enterprise** folder, double-click AdventureWorksDW2012Multidimensional-EE.sln. 
    
4. If the **Choose Default Environment Settings** dialog box appears, choose the **Business Intelligence Settings** option, and then click **Start Visual Studio**.
    
5. In Visual Studio, at the top of the **Solution Explorer** window, right click **AdventureWorksDW2012Multidimensional-EE** and click **Deploy**.
    
6. Close Visual Studio without saving changes.
    
### Configure AdventureWorks user access
<a name="InstallSampleDBs"> </a>

Once the databases and the cube have been deployed, you must grant your users access to them. The following access is required:
  
- Users who will be creating reports or dashboards in the subsequent articles in this section must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube. 
    
- If you are using the unattended service account with Excel Services or PerformancePoint Services, that account must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube. 
    
- If you are using Secure Store to refresh data in Excel Services or PerformancePoint Services, the target application credentials must have **db_datareader** access to the AdventureWorks databases and **Read** access to the AdventureWorks cube. 
    
We recommend that you use an Active Directory group containing the users to whom you want to grant access.
  
Use the following procedure to grant access to the AdventureWorks databases. If you choose to grant access to each user individually instead of using an Active Directory group, you must create a separate login for each user.
  
 **To grant access to the AdventureWorks databases**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. Expand **Security**.
    
3. Right-click **Logins**, and then click **New Login**.
    
4. Click **Search**.
    
5. If you are using an Active Directory group, click **Object Types**, select the **Groups** check box, and then click **OK**.
    
6. On the **Select User or Group** dialog box, type the name of the Active Directory group or user to whom you want to grant database access, and then click **OK**.
    
7. Under **Select a page**, click **User Mapping**.
    
8. Select the **Map** check box for **AdventureWorks2012**, and then select the **db_datareader** database role membership check box. 
    
9. Select the **Map** check box for **AdventureWorksDW2012**, and then select the **db_datareader** database role membership check box. 
    
10. Click **OK**.
    
Use the following procedure to grant access to the AdventureWorks OLAP cube.
  
 **To grant access to the AdventureWorks OLAP cube**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Expand **Databases**, and then expand **AdventureWorksDW2012Multidimensional-EE**.
    
    > [!NOTE]
    > If the AdventureWorksDW2012Multidimensional-EE database is not present, then right-click **Databases** and click **Refresh**. 
  
3. Right-click **Roles** and then click **New Role**.
    
4. In the **Role name** text box, type a name for the role. 
    
5. In the **Select a page** pane, click **Membership**.
    
6. Click **Add**.
    
7. Type the name of the users or Active Directory group to whom you want to grant cube access.
    
    > [!NOTE]
    > If you will be using Secure Store or an unattended service account to access the cube, include those credentials here. 
  
8. On the **Select Users or Groups** dialog box, click **OK**.
    
9. In the **Select a page** pane, click **Cubes**.
    
10. In the right pane, in the **Access** column, click select **Read** from the dropdown list for **Adventure Works** and **Mined Customers**.
    
11. In the right pane, in the **Local Cube/Drillthrough Access** column, click select **Drillthrough** from the dropdown list for **Adventure Works** and **Mined Customers**.
    
12. Click **OK**.
    
## Create a Business Intelligence Center
<a name="CreateABICenter"> </a>

The subsequent articles in this section rely on a Business Intelligence Center site being present. If you have an existing Business Intelligence Center, you can use it. However, we recommend creating a new Business Intelligence Center that is not part of your production environment.
  
Use the following procedure to create a Business Intelligence Center.
  
 **To create a Business Intelligence Center**
  
1. On the SharePoint Central Administration website, under **Application Management**, click **Create site collections**.
    
2. On the Create Site Collection page:
    
1. Type a title in the **Title** text box. 
    
2. Type the URL that you want to use in the **URL** text box. 
    
3. Under **Select a template**, choose the **Enterprise** tab, and then select **Business Intelligence Center**.
    
4. In the **Primary Site Collection Administrator** section, type a name for the primary site collection administrator in the **User name** text box. 
    
5. Optionally, type a name for the secondary site collection administrator.
    
6. Optionally, select a quota template.
    
7. Click **OK**.
    
### Configure BI Center access
<a name="proc3"> </a>

The following table describes the permissions available in a Business Intelligence Center.
  
**Business Intelligence Center permissions**

|**Account**|**Permissions**|
|:-----|:-----|
|Visitors  <br/> |Read  <br/> Read permissions enable users to view information in the Business Intelligence Center.  <br/> |
|Members  <br/> |Contribute  <br/> Contribute permissions enable users to view and create items, such as reports, and save them to this site.  <br/> |
|Designers  <br/> |Design  <br/> Design permissions enable users to view, create, and publish items that include dashboards.  <br/> |
|Owners  <br/> |Full Control  <br/> Full Control permissions enable users to view, create, and publish dashboard content, and to view or edit user permissions  <br/> |
   
For the scenarios described in the subsequent articles in this section, users will need the following permissions.
  
- Users publishing workbooks to the Business Intelligence Center from Excel require Contribute permissions and must be added to the Members group.
    
- Users publishing dashboards from PerformancePoint Dashboard Designer require Design permissions and must be added to the Designers group.
    
- Users who are only viewing reports or dashboards in the Business Intelligence Center but not publishing only require Read permission and can be added to the Visitors group.
    
Use the following procedure to configure permissions for the Business Intelligence Center.
  
 **To set permissions in the Business Intelligence Center**
  
1. In the Business Intelligence Center, click **Share**.
    
2. Type the names of the users or groups to whom you want to grant access.
    
3. Click **Show Options**.
    
4. On the **Select a group or permission level** dropdown list, select the permission level that you want. 
    
5. Click **Share**.
    
## Scenarios that use this configuration
<a name="Scenarios"> </a>

The following scenarios use the AdventureWorks sample data and Business Intelligence Center as configured in this article:
  
> [Create an Excel Services dashboard using SQL Server Analysis Services data](create-an-excel-services-dashboard-using-sql-server-analysis-services-data.md)
    

