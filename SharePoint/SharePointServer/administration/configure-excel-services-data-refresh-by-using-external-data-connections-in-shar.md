---
title: "Configure Excel Services data refresh by using external data connections in SharePoint Server 2013"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 0853bed9-1084-413b-bf91-427dc643a5e5
description: "Configure Excel Services in SharePoint Server data refresh by using Secure Store and an external Office Data Connection (ODC) file."
---

# Configure Excel Services data refresh by using external data connections in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Excel Services in SharePoint Server 2013 provides three methods of using Secure Store Service to refresh the external data source in a workbook:
  
- You can use an unattended service account. For more information, see [Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013](configure-the-unattended-service-account-0.md).
    
- You can specify a Secure Store target application in a workbook. (This is known as an embedded connection.) For more information, see [Configure Excel Services data refresh by using embedded data connections](/SharePoint/administration/excel-services-overview).
    
- You can use an Office Data Connection (ODC) file that specifies a Secure Store target application. This article describes how to do this. 
    
By using an ODC file for your data connection, you separate your Excel workbooks from the data connection information. This allows you to share a single ODC file among multiple workbooks and also allows you to centrally manage your data connections.
  
Using Excel Services with an ODC file consists of the following steps:
  
1. [Configure a data access account](#part1)
    
2. [Create a Secure Store target application](/SharePoint/administration/excel-services-overview#part2)
    
3. [Create and publish an ODC file](#part3)
    
4. [Configure an Excel workbook to use the published ODC file as a data connection](/SharePoint/administration/excel-services-overview#part4)
    
## Configure a data access account
<a name="part1"> </a>

You must have an account that can be granted access to the data source to which you want to connect your Excel workbook. This can be an Active Directory account, a SQL Server logon, or other set of credentials as required by your data source. This account will be stored in Secure Store.
  
After you have created the account, the next step is to grant that account read access to the required data. (in this article, we use the example of accessing a SQL Server database through an Active Directory account. If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data read permissions for the data access account.)
  
Follow these steps to create a SQL Server logon and grant Read access to the database.
  
 **To create a SQL Server logon for the data access account**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. In Object Explorer, expand **Security**.
    
3. Right-click **Logins**, and then click **New Login**.
    
4. In the **Login name** box, type the name of the Active Directory account that you created for data access. 
    
5. In the **Select a page** section, click **User Mapping**.
    
6. Select the **Map** check box for the database that you want to provide access to, and then, in the **Database role membership for: \<database\>** section, select the **db_datareader** check box. 
    
7. Click **OK**.
    
Now that you have created a data access account and granted it access to a data source, the next step is to create a Secure Store target application.
  
## Create a Secure Store target application
<a name="part2"> </a>

You must create a target application in Secure Store that contains the credentials that you created for data access. This target application can then be specified in an ODC file and will be used by Excel Services when it refreshes data in the workbook.
  
When you create the target application, you have to specify which users will be authorized to use the credentials stored in Secure Store. You can list users individually, or you can use an Active Directory group. We recommend that you use an Active Directory group for ease of administration.
  
> [!NOTE]
> The users that you list in the target application do not have direct access to the stored credentials. Instead, Excel Services uses the credentials on their behalf to refresh data in data-connected workbooks that specify this target application. 
  
Use the following procedure to create a Secure Store target application.
  
 **To create a target application**
  
1. On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store Service service application.
    
3. On the ribbon, click **New**.
    
4. In the **Target Application ID** box, type a unique identifier for this target application (for example, ExcelServicesDataAccess).
    
5. In the **Display Name** box, type a friendly name or short description. 
    
6. In the **Contact E-mail** box, type the email address for a contact for this target application. 
    
7. In the **Target Application Type** drop-down list, select **Group**.
    
8. Click **Next**.
    
9. On the Credential Fields page, if you are using Windows credentials, leave the default credential fields. If you are using credentials other than Windows credentials, modify the **Field Type** drop-down list to comply with the credentials that you are using. Click **Next**.
    
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
    
Once you have set the credentials for the target application, the target application is ready to use. The next step is to create an ODC file that specifies this target application for Excel Services data refresh.
  
## Create and publish an ODC file
<a name="part3"> </a>

Now that the Secure Store target application is configured, the next step is to create the ODC file and publish it to a trusted data connection library. Use the following procedure to create an ODC file that specifies the target application that you just created.
  
> [!NOTE]
> The following procedures use Excel 2016. The procedures for Excel 2010 are similar. 
  
 **To create and publish an ODC file**
  
1. In Excel, on the **Data** tab, in the **Get External Data** section, click **From Other Sources**, and then select your data source.
    
2. Complete the wizard to create a data connection to your data source.
    
3. On the **Data** tab, click **Connections**.
    
4. On the **Workbook Connections** dialog box, select the connection that you just created, and then click **Properties**.
    
5. On the **Connection Properties** dialog box, on the **Definition** tab, click **Authentication Settings**.
    
6. On the **Excel Services Authentication Settings** dialog box, select the **Use a stored account** option, and in the **Application ID** box, type the Application ID of the Secure Store target application that you created. 
    
    > [!NOTE]
    > In Excel 2010, select the **SSS** option. 
  
7. Click **OK**.
    
8. On the **Connection Properties** dialog box, click **Export Connection File**.
    
9. Save the ODC file to a trusted data connection library on your farm.
    
## Configure an Excel workbook to use the published ODC file as a data connection
<a name="part4"> </a>

In order for a workbook to use the ODC file that you just created, you must connect to it as a data source. Once it is connected, you can publish the workbook to a SharePoint Server 2013 document library and it will maintain its connection to the ODC file. Excel Services then uses the connection information specified in the ODC file when it refreshes data in the workbook.
  
Use the following procedure to connect to the ODC file in Excel.
  
 **To use an ODC file as a data source in Excel**
  
1. In Excel, on the **Data** tab, in the **Get External Data** section, click **Existing Connections**.
    
2. On the **Existing Connections** dialog box, click **Browse for More**.
    
3. On the **Select Data Source** dialog box, in the URL box, type the URL for the trusted data connection library where you saved the ODC file, and then press Enter. 
    
    > [!NOTE]
    > It may take several moments for the list to refresh with content from the specified location. 
  
4. On the list of **Data Connections**, select the ODC file that you saved, and then click **Open**.
    
5. On the **Import Data** dialog box, select the **PivotTable Report** or **PivotChart and PivotTable Report** option, and then click **OK**.
    
6. On the **Data** tab, click **Connections**.
    
7. On the **Workbook Connections** dialog box, select the connection that you just opened, and then click **Properties**.
    
8. On the **Connection Properties** dialog box, on the **Definition** tab, select the **Always use connection file** check box, and then click **OK**.
    
    > [!NOTE]
    > This ensures that the connection file that you connected to will be used rather than the embedded connection information. 
  
9. Click **Close**.
    
Once you have completed the data connection wizard, you can create your report and then publish it to a document library. When the workbook is rendered using Excel Services, Excel Services uses the connection information specified in the ODC file to refresh the data.
  
> [!NOTE]
> You must publish the workbook to an Excel Services trusted file location. 
  
## See also
<a name="part4"> </a>

#### Concepts

[Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md)

