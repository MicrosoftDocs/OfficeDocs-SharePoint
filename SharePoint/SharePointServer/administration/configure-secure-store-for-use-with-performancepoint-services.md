---
title: "Configure Secure Store for use with PerformancePoint Services"
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
ms.assetid: 95e12c80-7a86-4655-ba11-a05b9587fee0
description: "Configure PerformancePoint Services to use a Secure Store target application for external data refresh."
---

# Configure Secure Store for use with PerformancePoint Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
PerformancePoint Services supports two methods of using Secure Store Service to connect to external data:
  
- You can specify a Secure Store target application in PerformancePoint Dashboard Designer. This article describes how to do this.
    
- You can use an unattended service account. For more information, see [Configure the unattended service account for PerformancePoint Services](configure-the-unattended-service-account-for-performancepoint-services.md).
    
To configure PerformancePoint Services data access to use a Secure Store target application, you use the following process:
  
1. [Configure a data access account](#part1)
    
2. [Create a Secure Store target application](#part2)
    
3. [Configure a data connection to use a Secure Store target application](configure-secure-store-for-use-with-performancepoint-services.md#ConfigureWorkbook)
    
## Configure a data access account
<a name="part1"> </a>

You must have a Windows Active Directory account that can be granted access to the data source to which you want to connect in Dashboard Designer. This account will be stored in Secure Store.
  
Once you have created the account, the next step is to grant that account read access to the required data. (In this article, we use the example of accessing a SQL Server database. If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.)
  
Follow these steps to create a SQL Server logon and grant Read access to the database.
  
 **To create a SQL Server logon for the data access account**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. In Object Explorer, expand **Security**.
    
3. Right-click **Logins**, and then click **New Login**.
    
4. In the **Login name** box, type the name of the Active Directory account that you created for data access. 
    
5. In the **Select a page** section, click **User Mapping**.
    
6. Select the **Map** check box for the database that you want to provide access to, and then, under **Database role membership for: \<database\>**, select the **db_datareader** check box. 
    
7. Click **OK**.
    
Now that you have created a data access account and granted it access to a data source, the next step is to create a Secure Store target application.
  
## Create a Secure Store target application
<a name="part2"> </a>

You must create a target application in Secure Store that contains the credentials that you created for data access. This target application can then be specified in the data source settings in Dashboard Designer.
  
When you create the target application, you have to specify which users will be authorized to use the credentials stored in Secure Store. You can list users individually, or you can use an Active Directory group. We recommend that you use an Active Directory group for ease of administration.
  
> [!NOTE]
> The users that you list in the target application do not have direct access to the stored credentials. Instead, Dashboard Designer uses the credentials on their behalf to connect to the database, and PerformancePoint Services uses the credentials on their behalf when refreshing data in a published dashboard. 
  
Use the following procedure to create a Secure Store target application.
  
 **To create a target application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. On the ribbon, click **New**.
    
4. In the **Target Application ID** box, type a unique identifier for this target application (for example, PerformancePointServicesDataAccess).
    
5. In the **Display Name** box, type a friendly name or short description. 
    
6. In the **Contact E-mail** box, type the e-mail address for a contact for this target application. 
    
7. In the **Target Application Type** drop-down list, select **Group**.
    
8. Click **Next**.
    
9. On the Credential Fields page, leave the default values of Windows User Name and Windows Password and click **Next**.
    
10. On the Specify the membership settings page:
    
  - In the **Target Application Administrators** box, type the account of the user who will administer this target application. 
    
    > [!NOTE]
    > You can specify multiple users or an Active Directory group. 
  
  - In the **Members** box, type the users to whom you want to grant the ability to refresh data. 
    
    > [!NOTE]
    > You can specify multiple users or an Active Directory group. 
  
11. Click **OK**.
    
Use the following procedure to set the credentials for the target application.
  
 **To set the credentials for the target application**
  
1. On the Secure Store Service Application page, in the **Target Application ID** column, point to the target application that you just created, click the arrow that appears, and then click **Set Credentials**.
    
2. Type the user name and password of the data access account.
    
3. Click **OK**.
    
Once you have set the credentials for the target application, the target application is ready to use. The next step is to specify this target application in Dashboard Designer as part of the data source settings.
  
## Configure a data connection to use a Secure Store target application
<a name="ConfigureWorkbook"> </a>

You must configure your PerformancePoint Services data connection to use the Secure Store. After doing so, you can connect to the external data source in Dashboard Designer and create your dashboard. Use the following procedure to configure a PerformancePoint Services data connection.
  
 **To configure a data connection to use a Secure Store target application**
  
1. In Dashboard Designer, on the Create tab, click Data Source.
    
2. On the **Select a Data Source Template** dialog, choose your data source and click OK. 
    
3. In the Data Source Settings section, choose the Use a stored account option.
    
4. In the Application ID box, type the target application ID of the Secure Store target application that you created.
    
5. In the Connection Settings section, connect to your external data source.
    
6. Click **Test Data Source** to test the connection. 
    
7. Create and publish your dashboard.
    
    > [!NOTE]
    > For detailed information about creating dashboards, see [Create Dashboards by using PerformancePoint Services (SharePoint Server 2016)](/SharePoint/administration/performancepoint-services-overview). 
  
With the target application specified in Dashboard Designer, PerformancePoint Services uses the credentials associated with that target application to refresh the data in the dashboard after you have published it to SharePoint Server.
  
## See also
<a name="ConfigureWorkbook"> </a>

#### Concepts

[Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md)

