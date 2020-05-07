---
title: "Use Secure Store with SQL Server Authentication"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 5dee7e15-3b81-40c5-978e-c10357bb7a3d
description: "Use Secure Store in SharePoint Server to store SQL Server credentials."
---

# Use Secure Store with SQL Server Authentication

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can use the Secure Store Service to store credentials for data sources that require SQL Server Authentication. You can then use these credentials to access data sources that require SQL Server Authentication (such as Azure SQL Database) through Excel Services in SharePoint Server 2013 or Visio Services.
  
> [!NOTE]
> Using SQL Server credentials stored in Secure Store is not supported in PerformancePoint Services. 
  
We recommend storing credentials in Secure Store over storing them in a workbook file or Office Data Connection file. When you store credentials in Secure Store, they are not stored in plain text and you can manage the credentials in a central location, which can be easier to update than credentials embedded in workbook files or ODC files.
  
Using Secure Store together with Excel Services or Visio Services to access data sources through SQL Server Authentication requires the following:
  
- A Secure Store target application containing the SQL Server credentials with access to the data source must be configured.
    
- The Unattended Service Account must be configured.
    
The procedures in this article assume that you have already deployed Secure Store and Excel Services or Visio Services. For more information about how to deploy Secure Store, Excel Services, and Visio Services, see the related links at the end of this article.
  
## Configure a Secure Store target application

To use Secure Store for SQL Server authentication, you must create a target application which contains the SQL Server login with data access (usually **db_datareader** permissions). Use the following procedure to create the target application. 
  
 **To create a target application for SQL Server Authentication**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Secure Store service application.
    
3. On the **Edit** tab, click **New**.
    
4. On the Target Application Settings page:
    
1. Type an application ID in the **Target Application ID** text box. 
    
2. Type a display name in the **Display Name** text box. 
    
3. Type an e-mail address in the **Contact E-mail** text box. 
    
4. From the **Target Application Type** drop-down list, choose **Group**.
    
5. Click **Next**.
    
5. On the Specify Credentials page:
    
1. Change the **Windows User Name** field name to **User ID** and change the associated **Field Type** from **Windows User Name** to **User Name**.
    
2. Change the **Windows Password** field name to **Password** and change the associated **Field Type** from **Windows Password** to **Password**.
    
3. Click **Next**.
    
6. On the Specify Membership page:
    
1. In the **Target Application Administrators** box, type the name of the user account that you want to administer this target application. 
    
2. In the **Members** box, type the names of or browse for the users or Active Directory groups to which you want to give data access. To give access to all users, type Everyone.
    
3. Click **OK**.
    
Once you have created the target application, you must set the credentials for the target application. These are the SQL Server credentials that have access to your data source. Use the following procedure to set the credentials for the target application.
  
 **To set credentials for the target application**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Secure Store service application.
    
3. On the Secure Store page, select the check box for the target application that you created for SQL Server Authentication, and then, in the **Credentials** section of the ribbon, click **Set**.
    
4. In the **User ID** text box, type the SQL Server account that has data access. 
    
5. In the **Password** and **Confirm Password** text boxes, type the password for the SQL Server account. 
    
6. Click **OK**.
    
## Configure a target application for the Unattended Service Account

Using Secure Store for SQL Server Authentication with Excel Services or Visio Services requires that the Unattended Service Account be configured. The Unattended Service Account requires no specific permissions for this scenario; it only has to exist in the system. If you currently have an Unattended Service Account configured, you can skip the procedures in this section.
  
> [!NOTE]
> You can determine if an unattended service account has been configured by checking the **External Data** settings in Excel Services or Visio Services Global Settings. 
  
If you have not configured the Unattended Service Account for Excel Services or Visio Services, you must first create a target application in Secure Store that can be used as the Unattended Service Account. Use the following procedure to create the target application.
  
 **To create a target application for the Unattended Service Account**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Secure Store service application.
    
3. On the **Edit** tab, click **New**.
    
4. On the Target Application Settings page:
    
1. Type an application ID in the **Target Application ID** text box. 
    
2. Type a display name in the **Display Name** text box. 
    
3. Type an e-mail address in the **Contact E-mail** text box. 
    
4. From the **Target Application Type** drop-down list, choose **Group**.
    
5. Click **Next**.
    
5. On the Specify Credentials page, click **Next**.
    
6. On the Specify Membership page:
    
1. In the **Target Application Administrators** box, type the name of the user account that you want to administer this target application. 
    
2. In the **Members** box, type the name of the Windows account that runs the application pool for Excel Services or Visio Services. 
    
3. Click **OK**.
    
Once the target application has been created, you must associate a set of Windows credentials with it. This must be a Windows domain account, but it requires no specific permissions for this scenario. Use the following procedure to set the credentials for the target application.
  
 **To set credentials for the target application**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Secure Store service application.
    
3. On the Secure Store page, select the check box for the target application that you created for the unattended services account, and then, in the **Credentials** section of the ribbon, click **Set**.
    
4. In the **Windows User Name** text box, type the user name of a Windows account. 
    
5. In the **Windows Password** and **Confirm Windows Password** text boxes, type the password for the Windows account. 
    
6. Click **OK**.
    
Once the credentials have been set for the target application, follow the Unattended Service Account configuration steps for Excel Services or Visio Services in the following sections.
  
## Configure Excel Services (SharePoint Server 2013 only)

If you are using Excel Services, use the procedures in this section to complete the necessary configuration steps.
  
If the Unattended Service Account has not already been configured for Excel Services, follow these steps to configure it.
  
 **To configure the Unattended Service Account**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Excel Services service application.
    
3. Click **Global Settings**.
    
4. In the **External Data** section, choose the **Use an existing Unattended Service Account** option, and then type the name of the target application that you created for the Unattended Service Account in the **Target Application ID** text box. 
    
5. Click **OK**.
    
In order to use Excel Services with Secure Store, you must specify a Secure Store target application in Excel before publishing the Excel workbook to a SharePoint site to be rendered with Excel Services. In this case, you must specify the Secure Store target application that you created that contains the SQL Server login credentials.
  
Use the following procedure to specify a Secure Store target application from Excel.
  
 **To configure Secure Store settings in Excel**
  
1. In Excel, on the **Data** tab, click **From Other Sources**, and then click **From SQL Server**.
    
2. On the Connect to Database Server page:
    
1. Type the name of the instance of SQL Server that you want to connect to in the **Server name** text box. 
    
2. Choose the **Use the following User Name and Password** option, and then type the user name and password of a SQL Server account that has access to your data source. 
    
3. Click **Next**.
    
3. On the Select Database and Table page, select the database and table that you want to connect to, and then click **Next**.
    
4. On the Save Data Connection File and Finish page, click **Authentication Settings**.
    
5. In the **Excel Services Authentication Settings** dialog, select the **Use a stored account** option, type the name of the Secure Store target application that you created to use for SQL Server Authentication, and then click **OK**.
    
6. On the Save Data Connection File and Finish page, type a name for the data connection file (or keep the default) in the **File Name** text box, and then click **Finish**.
    
7. In the **Import Data** dialog, choose one of the **PivotTable** options, and then click **OK**.
    
8. If a **SQL Server Login** dialog appears, type the password for the **Login ID**, and then click **OK**.
    
Once you have connected to the data source, you can complete your Excel workbook and publish it to a SharePoint site to be rendered with Excel Services. The connection information to the Secure Store target application will remain embedded in the file.
  
> [!NOTE]
> Excel connects to the database directly. It does not use Secure Store. Secure Store is only used by Excel Services when rendering a workbook from a SharePoint site. 
  
Optionally, you can export the Secure Store connection information as an ODC file and then use it to connect additional Excel workbooks to the same data source. This allows for easier management and distribution of data connections. Use the following procedure if you want to export the Secure Store connection as an ODC file.
  
> [!IMPORTANT]
> You must export the ODC file to a trusted data connection library. Trusted data connection libraries are specified in the Excel Services service application settings. For more information, [Manage Excel Services trusted data connection libraries (SharePoint Server 2013)](manage-excel-services-trusted-data-connection-libraries.md) see. 
  
 **To export the ODC file**
  
1. In Excel, on the **Data** tab, click **Connections**.
    
2. Select the connection that you are using and then click **Properties**.
    
3. In the **Connection Properties** dialog, click the **Definition** tab. 
    
4. On the **Definition** tab, click **Authentication Settings**.
    
5. Confirm that you have the **Use a stored account** option selected and the correct Secure Store target application is specified in the **Application ID:** text box, and then click **OK**.
    
6. Click **Export Connection File**.
    
7. Navigate to an appropriate Data Connection Library on the SharePoint site, type a file name, and then click **Save**.
    
Once you have exported the ODC file, you can choose to connect to it from any Excel workbook where you want to connect to that data source. If the data connection information changes, you only have to update the ODC file itself and all Excel workbooks referencing it will have the new connection information.
  
> [!NOTE]
> You must select the **Always use connection file** check box in the Excel connection properties to ensure that the Excel workbook will always use the connection file. 
  
## Configure Visio Services

If you are using Visio Services, use the procedures in this section to complete the necessary configuration steps.
  
If the Unattended Service Account has not already been configured for Visio Services, follow these steps to configure it.
  
 **To configure the Unattended Service Account**
  
1. On the SharePoint Central Administration home page, under **Application Management**, click **Manage Service Applications**.
    
2. Click the Visio Services service application.
    
3. Click **Global Settings**.
    
4. In the **External Data** section, in the **Application ID** text box, type the name of the target application that you created for the Unattended Service Account. 
    
5. Click **OK**.
    
In order to use Visio Services with Secure Store, you must specify a Secure Store target application in the Visio data connection wizard and export the connection file to SharePoint Server before publishing the Visio diagram to a SharePoint site to be rendered with Visio Services. In this case, you must specify the Secure Store target application that you created that contains the SQL Server login credentials.
  
Use the following procedure to specify a Secure Store target application from Visio.
  
 **To create a data-connected diagram for use with a Secure Store target application**
  
1. In Visio Professional 2016, open a diagram or create a new diagram.
    
2. On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.
    
3. On the Data Selector page, choose the **Microsoft SQL Server database** option, and then click **Next**.
    
4. On the Connect to Database Server page, type the name of your database server, choose the **Use the following User Name and Password** option, and then type your SQL Server username and password. 
    
5. Click **Next**.
    
6. On the Select Database and Table page, select the database to which you want to connect, and then click **Next**.
    
7. On the Save Data Connection File and Finish page:
    
1. Click **Authentication Settings**.
    
2. On the **Visio Services Authentication Settings** dialog, choose the **Use a stored account** option, type the application ID of the Secure Store target application that you created in the **Application ID** text box, and click **OK**.
    
3. Click Browse.
    
4. Browse to a data connection library.
    
    > [!NOTE]
    > Visio Services does not require that ODC files be saved to a data connection library. However, for easiest administration, we recommend using data connection libraries to store all your data connection files. 
  
5. Type a name for the ODC file, and then click **Save**.
    
6. Click **Finish**.
    
8. If the **Web File Properties** dialog appears, update the Title, Description, and Keywords if desired, and click **OK**.
    
9. On the Select Data Connection page, click **Finish**.
    
10. Connect the data to the shapes in your diagram.
    
11. When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.
    
12. Type a file name, and then click **Save**.
    
> [!NOTE]
> Visio connects to the database directly. It does not use Secure Store. Secure Store is only used by Visio Services when rendering a Visio diagram from a SharePoint site. 
  
Once you have published the diagram to a SharePoint document library, you can render it using Visio Services and Visio Services will use the SQL Server credentials stored in the Secure Store target application to refresh the data in the diagram.
  
## See also

#### Concepts

[Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md)
  
[Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md)
  
#### Other Resources

[Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14))
  
[Plan for Visio Services in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee663482(v=office.14))
  
[Visio Graphics Service administration in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ee524059(v=office.14))

