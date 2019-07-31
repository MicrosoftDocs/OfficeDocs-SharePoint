---
title: "Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: d21f7d68-c18b-4253-af8b-0765c86a331b
description: "Configure Visio Services in SharePoint Server to refresh data by using the unattended service account."
---

# Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Configuring an unattended service account for Visio Services consists of the following steps:
  
1. Create an account to use for data access
    
2. Create a logon for the data access account on the data source
    
3. Create a Secure Store target application that uses the data access account credentials
    
4. Configure Visio Services to use the Secure Store target application for the unattended service account
    
5. Create an Office Data Connection (ODC) file by using Visio and publish it to a SharePoint data connection library
    
6. Use the ODC file as a data source in Visio
    
The first step is to create an account to use for data access. Have your domain administrator create an Active Directory account that you can use to access your data sources. 
  
> [!IMPORTANT]
> Visio Services requires an Active Directory account for the unattended service account. You cannot use a non-Windows account. 
  
Once the account has been created, follow these steps to create a logon for the data access account in SQL Server. (If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data read permissions for the data access account.)
  
 **To create a SQL Server logon for the data access account**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. In Object Explorer, expand **Security**.
    
3. Right-click **Logins**, and then click **New Login**.
    
4. In the **Login name** box, type the name of the Active Directory account that you created for data access. 
    
5. In the **Select a page** section, click **User Mapping**.
    
6. Select the **Map** check box for the database that you want to provide access to, and then in the **Database role membership for: \<database\>** section, select the **db_datareader** check box. 
    
7. Click **OK**.
    
After you have created a logon for the data access account and granted the account access to your data source, you must create a target application in Secure Store to contain the credentials for the data access account.
  
 **To create a target application for the unattended service account**
  
1. On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store Service service application.
    
3. On the ribbon, click **New**.
    
4. In the **Target Application ID** box, type an ID for the target application (for example, VisioServicesUnattended).
    
5. In the **Display Name** box, type a name for the target application. 
    
6. In the **Contact E-mail** box, type an email address. 
    
7. In the **Target Application Type** drop-down list, select **Group**.
    
8. Click **Next**.
    
9. Leave the default credential fields, and then click **Next**.
    
10. On the "Specify the membership settings" page:
    
1. In the **Target Application Administrators** box, type the account of the user who will administer this account. 
    
    > [!NOTE]
    > You can type multiple names or the name of an Active Directory group that contains the users whom you want to administer this target application. 
  
2. In the **Members** box, type Everyone.
    
    > [!NOTE]
    > The unattended service account is intended for granting broad database access. You can restrict the users who have access to the unattended service account to a specific Active Directory group if you want, but be aware that only one unattended service account can be created per Visio Services service application. 
  
3. Click **OK**.
    
After the target application has been created, you must set the target application to use the credentials for the data access account that you created. Use the following procedure to set the credentials.
  
 **To set the credentials for the target application**
  
1. On the Secure Store Service Application page, in the **Target Application ID** column, point to the target application that you just created, click the arrow that appears, and then click **Set Credentials**.
    
2. In the **Windows User Name** box, type the Active Directory account that you created for data access. 
    
3. Type and confirm the password for the account.
    
4. Click **OK**.
    
The target application configuration is now complete. The next step is to designate this target application for use as the unattended service account in Visio Services. Use the following procedure to configure the unattended service account in Visio Services Global Settings.
  
 **To configure Visio Services Global Settings**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Visio Services service application.
    
3. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
4. On the Visio Graphics Service Settings page, in the **External Data** section, in the **Application ID** box, type the ID of the Secure Store target application that you just created. 
    
5. Click **OK**.
    
Once you have configured the External Data setting in Visio Services Global Settings, the unattended service account is configured and ready to use. 
  
The next step is to create an ODC file that specifies the unattended service account. You can create the ODC file in Visio as part of your diagram creation process.
  
Use the following procedure to create an ODC file and create a data-connected drawing.
  
 **To create an ODC file and link data to shapes in Visio**
  
1. In Visio, open a diagram or create a new diagram.
    
2. On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.
    
3. On the Connect to Database Server page, type the name of your database server, and then click **Next**.
    
4. On the Select Database and Table page, select the database to which you want to connect, and then click **Next**.
    
5. On the Save Data Connection File and Finish page:
    
1. Click **Authentication Settings**.
    
2. On the **Visio Services Authentication Settings** dialog box, choose the **None** option and click **OK**.
    
3. Click **Browse**.
    
4. Browse to a data connection library.
    
    > [!NOTE]
    > Visio Services does not require that ODC files be saved to a data connection library. However, for easiest administration, we recommend using data connection libraries to store all your data connection files. 
  
5. Type a name for the ODC file, and then click **Save**.
    
6. Click **Finish**.
    
6. If the **Web File Properties** dialog box appears, click **Cancel**.
    
7. On the Select Data Connection page, click **Finish**.
    
8. Connect the data to the shapes in your diagram.
    
9. When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.
    
10. Type a file name, and then click **Save**.
    
Once the diagram has been published, it is available to view by using Visio Services. When the data in the diagram is refreshed, it uses the ODC file that you specified. The **None** option specified in the ODC file will cause Visio Services to use the unattended service account. 
  
Once the ODC file has been saved to the data connection library, you can connect directly to it when linking data to shapes in Visio. This allows you to share a single data connection file among multiple Visio diagrams.
  
Use the following procedure to connect to an existing ODC file.
  
 **To create a data-connected diagram by using an ODC file**
  
1. In Visio, open a diagram or create a new diagram.
    
2. On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.
    
3. On the Data Selector page of the wizard, click **Previously created connection**, and then click **Next**.
    
4. On the Select Data Connection page, click **Browse**.
    
5. On the **Existing Connections** dialog box, click **Browse for More**.
    
6. In the **Data Selector** dialog box, in the **URL** box, type the URL of the data connection library where you saved the ODC file, and then press Enter. 
    
7. Select the ODC file and then click **Open**.
    
8. On the Select Data Connection page, click **Finish**.
    
9. Connect the data to the shapes in your diagram.
    
10. When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.
    
11. Type a file name, and then click **Save**.
    
## See also

#### Concepts

[Configure Visio Services data refresh in SharePoint Server by using external data connections](configure-data-refresh-by-using-external-data-connections.md)

