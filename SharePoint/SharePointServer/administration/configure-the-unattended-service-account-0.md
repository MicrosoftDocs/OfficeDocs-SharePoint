---
title: "Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013"
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
ms.assetid: fcfdb2ad-9d0e-43ca-8bfa-45064eeca5af
description: "Configure Excel Services in SharePoint Server to use the unattended service account for authentication to external data."
---

# Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Excel Services in SharePoint Server 2013 provides three methods of using Secure Store Service to refresh the external data source in a workbook:
  
- You can use an unattended service account. This article describes how to do this. 
    
- You can specify a Secure Store target application in a workbook. (This is known as an embedded connection.) For more information, see [Configure Excel Services data refresh by using embedded data connections](/SharePoint/administration/excel-services-overview). 
    
- You can use an Office Data Connection (ODC) file that specifies a Secure Store target application. For more information, see [Configure Excel Services data refresh by using external data connections](/SharePoint/administration/excel-services-overview).
    
Using the unattended service account involves configuring an Active Directory account and granting it access to your data, storing the credentials for this account in Secure Store, and configuring Excel Services to use the stored credentials when it needs to refresh the data in a workbook.
  
The following steps are required to configure the unattended service account in Excel Services.
  
1. [Configure a data access account](#section1)
    
2. [Configure Excel Services Global Settings](#section3)
    
3. [Configure a workbook to use the unattended service account](#section4)
    
## Configure a data access account
<a name="section1"> </a>

The unattended service account requires an Active Directory account for data access. Have your domain administrator create an Active Directory account that you can use for data access. 
  
After the account has been created, you must grant this account read access to the data source that you will be using in your data-connected Excel workbook. Use the following procedure to create a logon for the data access account in SQL Server. (If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.)
  
 **To create a SQL Server logon for the data access account**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. In Object Explorer, expand **Security**.
    
3. Right-click **Logins**, and then click **New Login**.
    
4. In the **Login name** box, type the name of the Active Directory account that you created for data access. 
    
5. In the **Select a page** section, click **User Mapping**.
    
6. Select the **Map** check box for the database that you want to provide access to, and then, in the **Database role membership for: \<database\>** section, select the **db_datareader** check box. 
    
7. Click **OK**.
    
Now that you have created a logon for the data access account and granted the account access to your data source, you must create a target application in Secure Store to contain the credentials for the data access account.
  
## Configure Excel Services Global Settings
<a name="section3"> </a>

The unattended service account configuration is part of the Excel Services Global Settings. Use the following procedure to configure the unattended service account in Excel Services.
  
 **To configure Excel Services Global Settings**
  
1. On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application.
    
3. On the Manage the Excel Services page, click **Global Settings**.
    
4. On the Excel Services Settings page, in the **External Data** section: 
    
  - Select the **Create a new Unattended Service Account** option. 
    
  - Type the user name and password of the account that you created for data access.
    
5. Click **OK**.
    
With the Excel Services Global Settings configured, setup of the unattended service account is complete. The next section describes how to configure the Excel Services authentication settings in a data-connected Excel workbook to refresh the data with the unattended service account after the workbook has been published to a SharePoint document library.
  
## Configure a workbook to use the unattended service account
<a name="section4"> </a>

You must configure the Excel Services Authentication Settings in the workbook before you publish it to SharePoint Server 2013. Doing so enables the workbook to use the unattended service account to refresh data when the workbook is rendered in Excel Services. Use the following procedure to configure the authentication settings.
  
 **To configure Excel Services authentication settings**
  
1. In a data-connected Excel workbook, on the **Data** tab, click **Connections**.
    
2. On the **Workbook Connections** dialog box, select the data connection that you want to update, and then click **Properties**.
    
3. On the **Connection Properties** dialog box, on the **Definition** tab, click **Authentication Settings**.
    
4. On the **Excel Services Authentication Settings** dialog box, select the **None** option, and then click **OK**.
    
5. On the **Connection Properties** dialog box, click **OK**.
    
    > [!NOTE]
    > If you see a warning that the link to the external connection file will be removed, click **Yes**. 
  
6. On the **Workbook Connections** dialog box, click **Close**.
    
With the Excel Services Authentication Settings set to **None**, Excel Services uses the unattended service account to refresh the data in the workbook after you have published it to SharePoint Server 2013.
  
## See also
<a name="section4"> </a>

#### Concepts

[Use Excel Services with Secure Store Service in SharePoint Server 2016](use-excel-services-with-secure-store.md)

