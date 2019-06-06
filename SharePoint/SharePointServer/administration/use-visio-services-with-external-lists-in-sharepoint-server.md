---
title: "Use Visio Services with external lists in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 06ad416d-8830-4b1d-96e5-854eda879b60
description: "Connect to an external list in Visio by using Microsoft Business Connectivity Services and render the diagram in a browser by using Visio Services."
---

# Use Visio Services with external lists in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This document describes the procedures necessary to connect a Visio diagram to an external list in SharePoint Server 2013 or SharePoint Server 2016.
  
An external list is a data source outside SharePoint Server (for example, a SQL Server table) that has been connected to a SharePoint list by using Microsoft Business Connectivity Services. The data connection and the external list are both created by using Visual Studio or SharePoint Designer 2013. The connection information is managed and stored by using the Business Data Connectivity service, a component of Business Connectivity Services in SharePoint Server.
  
## Before you begin

The following service applications must be running and configured on your SharePoint Server farm:
  
- Business Data Connectivity service 
    
- Visio Graphics Service 
    
- Secure Store Service 
    
You also need the following domain accounts:
  
- An account that has read access to your data source. This account is stored in Secure Store for use by Microsoft Business Connectivity Services.
    
- A user account that has Design permissions to the SharePoint site where you want to create the external list.
    
- An account that has Farm Administrator permissions to configure various settings on the SharePoint Central Administration website.
    
## Configure a Secure Store target application

The Business Data Connectivity service External Content Type uses credentials that are stored in Secure Store to access the data source. You must create a Secure Store target application for the External Content Type to use in accessing these credentials.
  
Use the following procedure to create the target application.
  
 **To create a Secure Store Target Application**
  
1. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
2. Click the Secure Store service application.
    
3. In the **Manage Target Applications** group on the ribbon, click **New**.
    
4. In the **Target Application ID** box, type a unique identifier for this target application. Note the name that you use here; you will need it when you create the External Content Type. 
    
5. Type a **Display Name** and **Contact E-Mail address**.
    
6. From the **Target Application Type** list, select **Group**.
    
7. Click **Next**.
    
8. On the Field Names page, keep the default settings and then click **Next**.
    
9. In the **Target Application Administrators** box, type the names of the users whom you want to be able to administer this target application. 
    
10. In the **Members** box, type the names of the users whom you want to allow to trigger data refresh. (That is, the users who will be viewing the Visio diagram that you create.) 
    
11. Click **OK**.
    
After the target application has been created, you must set the credentials that are to be associated with this target application. In this case, you must use a domain account that has read access to the data source that you want to connect to through Microsoft Business Connectivity Services.
  
 **To set the credentials for the target application**
  
1. On the Secure Store administration page, select the check box next to the target application that you just created.
    
2. In the **Credentials** group on the ribbon, click **Set**.
    
3. In the **Windows User Name** box, type the domain account that has access to your data source. 
    
4. Type and confirm the password for that account.
    
5. Click **OK**.
    
## Configure Business Data Connectivity service metadata store permissions

You must create the External Content Type with a user account that has permissions to the Business Data Connectivity service metadata store. Use the following procedure to grant a user permissions to the Business Data Connectivity service metadata store. (You can skip this step if you already have a user account that has these permissions.)
  
 **To grant a user permissions to the Business Data Connectivity service metadata store**
  
1. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
2. Click the Business Data Connectivity service service application.
    
3. In the **Permissions** section of the ribbon, click **Set Metadata Store Permissions**.
    
4. Type the user account to which you want to grant permissions, and then click **Add**.
    
5. Select the user account that you just added, and then select the **Edit** and **Execute** check boxes. 
    
6. Click **OK**.
    
Note that **Edit** is a highly privileged permission that is required to create or modify External Content Types in Business Data Connectivity service. We recommend that you set **Edit** permissions when the site is first designed or changed and then remove the **Edit** permissions for users who do not require it. **Execute** permissions are required to query the External Content Type. 
  
## Create an External Content Type

After your user account has permissions to the Business Data Connectivity service metadata store, you can create the External Content Type. To complete the procedures in this section, your account must also have **Design** permissions on the SharePoint site where you plan to create the external list. If you want to set permissions on the list (an optional step) you must have **Full Control** permissions on the site. 
  
External content types for Business Data Connectivity service are created and managed in SharePoint Designer 2013 or Visual Studio 2012. This example uses a SQL Server data source, and the external content type is created by using SharePoint Designer 2013.
  
The following procedures describe how to create and configure an External Content Type. Follow these procedures on a computer that is running SharePoint Designer 2013.
  
 **To create an External Content Type**
  
1. Log on to a computer by using an account that has **Design** permissions on the SharePoint site where you want to create the external list and permissions to the Business Data Connectivity service metadata store. 
    
2. Open SharePoint Designer 2013.
    
3. In the **Open SharePoint Site** section, click **Open Site**.
    
4. In the **Site name** box, type the URL of the site where you want to create the external list, and then click **Open**.
    
5. In the left navigation, click **External Content Types**.
    
6. In the **New** section of the ribbon, click **External Content Type**.
    
7. Type a **Name** and **Display Name** for the content type. 
    
8. Click **Click here to discover external data sources and define operations**.
    
9. Click **Add Connection**.
    
10. Select your data source type from the **Data Source Type** list. (This example assumes a SQL Server data source.) 
    
11. In the **SQL Server Connection** dialog box: 
    
  - In the **Database Server** box, type the name of your database server. 
    
  - In the **Database Name** box, type the name of your database. 
    
  - Select the **Connect with Impersonated Windows Identity** option. 
    
  - In the **Secure Store Application ID** box, type the ID of the Secure Store target application that you created. 
    
  - Click **OK**.
    
12. In the **Data Source Explorer**, find the table that you want to connect to.
    
13. Right-click the table and then click **Create All Operations**.
    
14. Complete the **All operations** wizard. 
    
15. When you have completed the wizard, on the **File** menu, click **Save**.
    
After you have created the External Content Type, the next step is to create an external list based on it.
  
 **To create an external list**
  
1. In SharePoint Designer, in the left navigation pane, click **External Content Types**. (If the External Content Type that you just created does not appear in the list, you may have to refresh the list.)
    
2. Right-click the External Content Type that you created, and then click **External List**.
    
3. Type a name for the list, and then click **OK**.
    
4. Optionally, click **Permissions for this list** to set list permissions. (By default, the list inherits permissions from the site.) 
    
## Configure Business Data Connectivity service object permissions

Users who will be using the external list in SharePoint or who will be viewing a Visio diagram connected to that list must have permissions to the External Content Type. Use the following procedure to grant the users permissions to the External Content Type in Business Data Connectivity service.
  
 **To grant a user permissions to the Business Data Connectivity service External Content Type**
  
1. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
2. Click the Business Data Connectivity service service application.
    
3. Click the External Content Type that you created.
    
4. In the **Permissions** group on the ribbon, click **Set Object Permissions**.
    
5. Type the user account or an Active Directory group to which you want to grant permissions, and then click **Add**.
    
6. Select the user account that you just added, and then select the Execute check box.
    
7. Click **OK**.
    
## Connect to the external list in Visio

The external list is now available on the SharePoint site. You can now connect to the list from Visio.
  
 **To connect to an external list in Visio**
  
1. In Visio, on the **Data** tab, click **Link Data to Shapes**.
    
2. Choose the **Microsoft SharePoint Foundation** list option, and then click **Next**.
    
3. On the **Select a site** page, type the URL for the SharePoint site where your external list is located, and then click **Next**.
    
4. On the **Select a list** page, choose the external list that you created, and then click **Finish**.
    
The data from the external list is now available in Visio and you can link it to your shapes. After you have linked the data to shapes, the next step is to save the file to a SharePoint document library.
  
 **To save a diagram to a SharePoint document library**
  
1. In Visio, click **File**, and then click **Save**.
    
2. Click **Computer**, and then click **Browse**.
    
3. Type the URL of the SharePoint document library in the location box at the top of the **Save As** dialog box, and then press Enter. 
    
4. Type a file name, and then click **Save**.
    
After the diagram has been saved to the SharePoint document library, you can go to the document library and click the Visio file to render it in a browser by using Visio Services.
  

