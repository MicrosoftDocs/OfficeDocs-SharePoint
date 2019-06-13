---
title: "Configure Excel Services data refresh by using embedded data connections in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 2be5291e-b6cc-4730-bc58-78b14ea1984b
description: "Configure Excel Services in SharePoint Server to use a Secure Store target application for external data refresh."
---

# Configure Excel Services data refresh by using embedded data connections in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Excel Services in SharePoint Server 2013 supports three methods of using Secure Store Service to connect to external data:
  
- You can specify a Secure Store target application in a workbook. (This is known as an embedded connection.) This article describes how to do this.
    
- You can use an unattended service account. For more information, see [Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2016](configure-the-unattended-service-account-0.md).
    
- You can use an Office Data Connection (ODC) file that specifies a Secure Store target application. For more information, see [Configure Excel Services data refresh by using external data connections](/SharePoint/administration/excel-services-overview).
    
To configure Excel Services data access to use embedded data connections, you use the following process:
  
1. [Configure a data access account](#part1)
    
2. [Create a Secure Store target application](#part2)
    
3. [Configure a workbook to use an embedded data connection](#ConfigureWorkbook)
    
## Configure a data access account
<a name="part1"> </a>

You must have an account that can be granted access to the data source to which you want to connect your Excel workbook. This can be a Windows Active Directory account, a SQL Server logon, or other set of credentials as required by your data source. This account will be stored in Secure Store.
  
Once you have created the account, the next step is to grant that account read access to the required data. (In this article, we use the example of accessing a SQL Server database through an Active Directory account. If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.)
  
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

You must create a target application in Secure Store that contains the credentials that you created for data access. This target application can then be specified in data-connected Excel workbooks and will be used by Excel Services when it refreshes data in the workbook.
  
When you create the target application, you have to specify which users will be authorized to use the credentials stored in Secure Store. You can list users individually, or you can use an Active Directory group. We recommend that you use an Active Directory group for ease of administration.
  
> [!NOTE]
> The users that you list in the target application do not have direct access to the stored credentials. Instead, Excel Services uses the credentials on their behalf to refresh data in data-connected workbooks that specify this target application. 
  
Use the following procedure to create a Secure Store target application.
  
 **To create a target application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. On the ribbon, click **New**.
    
4. In the **Target Application ID** box, type a unique identifier for this target application (for example, ExcelServicesDataAccess).
    
5. In the **Display Name** box, type a friendly name or short description. 
    
6. In the **Contact E-mail** box, type the e-mail address for a contact for this target application. 
    
7. In the **Target Application Type** drop-down list, select **Group**.
    
8. Click **Next**.
    
9. On the Credential Fields page, if you are using Windows credentials, leave the default credential fields. If you are using credentials other than Windows credentials, modify the **Field Type** drop-down lists to comply with the credentials that you are using. Click **Next**.
    
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
    
Once you have set the credentials for the target application, the target application is ready to use. The next step is to specify this target application in the Excel Services authentication settings in your data-connected Excel workbook.
  
## Configure a workbook to use an embedded data connection
<a name="ConfigureWorkbook"> </a>

You must configure the Excel Services Authentication Settings in the workbook before you publish it to SharePoint Server 2013. Doing so enables the workbook to use a Secure Store target application to refresh data that is rendered using Excel Services. Use the following procedure to configure the authentication settings.
  
 **To configure Excel Services authentication settings**
  
1. In a data-connected Excel workbook, on the **Data** tab, click **Connections**.
    
2. On the **Workbook Connections** dialog box, select the data connection that you want to update, and then click **Properties**.
    
3. On the **Connection Properties** dialog box, on the **Definition** tab, click **Authentication Settings**.
    
4. On the **Excel Services Authentication Settings** dialog box, select the **Use a stored account** option, type the Application ID of the target application in the text box, and then click **OK**.
    
    > [!NOTE]
    > If you are using Excel 2010, select the **SSS** option. 
  
5. On the **Connection Properties** dialog box, click **OK**.
    
    > [!NOTE]
    > If you see a warning that the link to the external connection file will be removed, click **Yes**. 
  
6. On the Workbook Connections dialog box, click **Close**.
    
With the target application specified in the Excel Services Authentication Settings, Excel Services uses the credentials associated with that target application to refresh the data in the workbook after you have published it to SharePoint Server 2013.
  
## See also
<a name="ConfigureWorkbook"> </a>

#### Concepts

[Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md)

