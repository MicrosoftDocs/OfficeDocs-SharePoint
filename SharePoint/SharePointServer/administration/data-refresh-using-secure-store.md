---
title: "Configure scheduled data refresh for Power Pivot by using Secure Store (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: c8209ecc-59e4-4568-a7e6-782a6b0ab02f
description: "Learn to configure scheduled data refresh in Power Pivot for SharePoint by using Secure Store."
---

# Configure scheduled data refresh for Power Pivot by using Secure Store (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
> [!IMPORTANT]
> This scenario applies only to SharePoint Server 2013. 
  
In this article, we'll take a look at configuring scheduled data refresh in SQL Server 2012 Power Pivot for SharePoint 2013 by using the Secure Store Service.
  
By using Secure Store, you can store your data access credentials in an encrypted database and Power Pivot for SharePoint can use these credentials to refresh the data in your reports on a schedule that you set up.
  
## Before you begin
<a name="begin"> </a>

Before starting, you will need:
  
- An Active Directory account that you can use to access the data sources used in your report. We'll refer to this as the data access account. We'll look at how to configure the account for access to your data sources in this article, so you just need the account itself to get started.
    
- An Active Directory group that contains all users who will trigger data refresh, either by setting the data refresh schedule or by manually starting a data refresh outside the normal schedule. We'll refer to this group as the data refresh users group.
    
- Contribute access to the SharePoint document library that you will be using.
    
Additionally, be sure that [Excel Services](excel-services-overview.md) and [Secure Store](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)) are configured in your SharePoint Server 2013 farm. 
  
## Video demonstration
<a name="VideoDemonstration"> </a>

This video shows the steps involved in configuring scheduled data refresh in SQL Server 2012 Power Pivot for SharePoint 2013 by using the Secure Store Service, as described in this article.
  
**Video: Configure scheduled data refresh for Power Pivot by using Secure Store**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/2d579215-2069-4537-a7ed-33be05a35ab1?autoplay=false]
## Configure access to your data source
<a name="proc1"> </a>

The first step in setting up scheduled data refresh by using Secure Store is to ensure that the data access account has the proper access to the data source used in your report. We'll take a look at SQL Server and Analysis Services data sources.
  
### Use a SQL Server data source

If you're using SQL Server for your data source, you'll need to make sure that your data access account has read permissions to the SQL Server database where your data resides.
  
 **To set read permission on a SQL Server database**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. Expand **Security**.
    
3. Right-click **Logins**, and then choose **New Login**.
    
4. In the **Login name** box, type the domain and user name of the account to which you want to grant database access. 
    
5. On the **User Mapping** page, select the **Map** check box for the database to which you want to grant access. 
    
6. Select the **db_datareader** check box. 
    
7. Choose **OK**.
    
If you're also using Analysis Services, see the next section for information about how to set up access to Analysis Services data sources. If you're not using Analysis Services, skip ahead to [Store your data access account in Secure Store](data-refresh-using-secure-store.md#StoreAccountInSecureStore).
  
### Use an Analysis Services data source

If you're using Analysis Services, you'll need to make sure that your data access account is a member of the proper Analysis Services role and that the role has read access to the Analysis Services cube.
  
 **To set read permission on an Analysis Services cube**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Expand **Databases**, and expand the database to which you want to grant access.
    
3. Right-click **Roles**, and then choose **New Role**.
    
4. Type a name for the role.
    
5. On the **Membership** page: 
    
1. Click **Add**.
    
2. Type your data access account, and then choose **OK**.
    
6. On the **Cubes** page, select **Read** access for the cubes to which you want to grant access. 
    
7. Choose **OK**.
    
## Store your data access account in Secure Store
<a name="StoreAccountInSecureStore"> </a>

Once the data access account has been granted access to your data source, the next step is to store this account in Secure Store. First, we'll create a Secure Store target application for the data access account. A target application is basically a way of defining some things about the account, like what kind of account it is and who's allowed to use it.
  
 **To create a Secure Store target application**
  
1. In Central Administration, under **Application Management**, choose **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. On the ribbon, on the **Edit** tab, choose **New**.
    
4. Type a **Target Application ID**.
    
    > [!NOTE]
    > You'll need this value when you configure the refresh schedule for your Power Pivot workbook. 
  
5. Type a **Display Name** and **Contact E-mail**.
    
6. For **Target Application Type**, choose **Group**.
    
7. Choose **Next**.
    
8. Keep the default credential settings, and choose **Next**.
    
9. Specify a user to administer the target application, such as your farm administrator, in the **Target Application Administrators** box. 
    
10. In the **Members** box, include: 
    
  - The account that runs the application pool for the Power Pivot for SharePoint service application.
    
  - The data refresh group that contains the users who will schedule or start a data refresh in Power Pivot for SharePoint.
    
11. Choose **OK**.
    
Once the target application has been created, the next step is to associate your data access account with it.
  
 **To associate the data access account with the target application**
  
1. On the Secure Store management page, select the check box for the target application for which you want to set the credentials.
    
2. On the ribbon, in the **Credentials** section, choose **Set**.
    
3. Type the user name and password of your access account.
    
4. Choose **OK**.
    
Secure Store setup is now complete. The next step is to set up a data refresh schedule in Power Pivot for SharePoint.
  
## Set up a data refresh schedule in Power Pivot for SharePoint
<a name="ver"> </a>

Now that everything is configured, we can set up the refresh schedule and other settings in Power Pivot for SharePoint. We'll start by building a test workbook with a data model in Excel and publishing it to a document library in a site collection where Power Pivot for SharePoint is enabled. Then, we can configure the refresh settings.
  
 **To create a test workbook**
  
1. In Excel, on the **Data** tab, choose **From Other Sources**, and then choose **From SQL Server**.
    
2. Type the name of the instance of SQL Server where your data resides.
    
3. Follow the wizard through to connect to the table that contains your data.
    
4. When the wizard completes, you should see the **Import Data** dialog. Choose the **Only Create Connection** option, and then select the **Add this data to the Data Model** check box. 
    
5. Choose **OK**.
    
6. On the **Power Pivot** tab, choose **Manage**.
    
7. On the **Power Pivot** ribbon, choose **PivotTable**.
    
8. On the **Insert Pivot** dialog, choose the **Existing Worksheet** option, and then choose **OK**.
    
9. Select the fields that you want in the PivotTable report.
    
10. Save the workbook to a document library on the site collection where you enabled Power Pivot.
    
Now that the workbook has been saved to a SharePoint document library, let's configure the refresh settings.
  
 **To configure refresh settings for a workbook**
  
1. In the document library where your Excel workbook is stored, choose the ellipsis (...) control twice, and then choose **Manage Power Pivot Data Refresh**.
    
    ![Screenshot of controls in document library.](../media/PowerPivotDocLibraryControls.png)
  
2. On the Manage Data Refresh page, select the **Enable** check box. 
    
3. In the **Schedule Details** section, choose the schedule options that you want for refreshing the data in this workbook. 
    
4. Optionally, if you want the workbook to refresh right away, select the **Also refresh as soon as possible** check box. 
    
5. In the **Credentials** section, choose the **Connect using the credentials saved in Secure Store Service** option. 
    
6. Type the ID of the Secure Store target application that you created in the **ID** box. 
    
7. Choose **OK**.
    
You can test if data refresh is working properly by making some changes to your data, and then setting the workbook to refresh right away by using the **Also refresh as soon as possible** option. 
  
## See also
<a name="ver"> </a>

#### Concepts

[Configure Power Pivot for SharePoint 2013](configure-power-pivot-for-sharepoint-2013.md)
  
[Configure scheduled data refresh for Power Pivot by using a specified account (SharePoint Server 2013)](data-refresh-using-a-specified-account.md)
  
[Configure scheduled data refresh for Power Pivot by using the unattended data refresh account (SharePoint Server 2013)](data-refresh-using-the-unattended-data-refresh-account.md)

