---
ms.date: 07/11/2018
title: Make an External List from a SQL Azure table with Business Connectivity Services and Secure Store
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 466f3809-fde7-41f2-87f7-77d9fdadfc95
description: Learn how to use SharePoint technologies to access data from a SQL Azure database without having to write code.
---

# Make an External List from a SQL Azure table with Business Connectivity Services and Secure Store

As a SharePoint Administrator or Global Administrator in Microsoft 365, you can use services in Microsoft SharePoint to access data from a Microsoft SQL Azure database. Because SQL Azure is a cloud-based relational database technology, the connection works completely in the cloud. This article describes how to use SharePoint technologies to access data from a SQL Azure database without having to write code.
  
To use data from a SQL Azure database, you have to create an External List by using Business Connectivity Services (BCS) and Secure Store. BCS connects SharePoint solutions to external data, and Secure Store enables user authentication for the data. By using an External List, you can display the contents of a table from SQL Azure in SharePoint. Users can read, edit, and update the data, all in SharePoint. 
  
For more information about how to use BCS to use external data, see [Introduction to external data](https://support.office.com/article/676e60e7-d99f-463f-a173-65e9d63538c0).
  
SQL Azure databases are cloud-based relational databases that are created by using SQL Server technology. To learn how to get started with these databases, see [Getting Started with Microsoft Azure SQL Database Using the Microsoft Azure Platform Management Portal](https://go.microsoft.com/fwlink/?linkid=2003465)
  
## Overview of steps in the process
<a name="__toc350352764"> </a>

To create an External List that enables you to access data from SQL Azure, you have to complete a sequence of separate steps. 
  
The following table lists the steps and the required software for that step.
  
|**What to do:**|**Where to do it:**|
|:-----|:-----|
|Step 1: Set permissions on the BCS Metadata Store  <br/> |SharePoint admin center   <br/> |
|Step 2: Create a Secure Store Mapping  <br/> |SharePoint admin center   <br/> |
|Step 3: Create an External Content Type (ECT)  <br/> |SharePoint Designer 2010 OR Visual Studio  <br/> |
|Step 4: Create an External List  <br/> |SharePoint admin center   <br/> |
|Step 5: Grant permissions to manage your ECT  <br/> |SharePoint admin center   <br/> |
   
## How BCS and Secure Store work together
<a name="__toc350352765"> </a>

Business Connectivity Services (BCS) connects to data in an external data store. You can display the data in an External List, and maintain the data elsewhere. BCS enables you to connect SharePoint solutions to two kinds of resources:
  
- A SQL Azure database
    
- A WCF web service that acts as an end-point for some other kind of data store 
    
BCS enables you to access an external data source by using the Secure Store. Secure Store keeps encrypted copies of credentials. It enables a SharePoint Administrator to associate a SharePoint group that uses a single SQL Azure account that can access the target database. When a SharePoint user browses the data in the External List, Secure Store uses the associated SQL Azure account to request the data from SQL.
  
To make this possible, a SharePoint Administrator defines an External Content Type (ECT) in SharePoint Designer or in Visual Studio. Then, someone with appropriate permissions creates an External List on a SharePoint site by referencing the ECT. Users who have appropriate permission can view or update the list. 
  
> [!NOTE]
>  SharePoint in Microsoft 365 doesn't support offline use of external lists. 
  
This illustration shows how the connections between the different elements occur:
  
![Diagram that shows the connectivity between a user, SharePoint, and an external data source in SQL Azure](media/4201a500-2932-4e53-867c-c911df2c729a.png)
  
The following list describes the steps in the connectivity process. Each step in this list corresponds to a number in the previous diagram.
  
1. The user signs in to SharePoint and opens an External List. The Business Data Connectivity (BDC) service in SharePoint queries External Content Type for that list in the BDC metadata store that contains the list. The query asks for the following information: how to access the external system, which operations are supported, and what credentials to use. 
    
2. The BDC service runtime sends the request (SOAP over HTTP) to the endpoint of the SQL Azure Windows Communication Foundation (WCF) service.
    
3. The SQL Azure service returns the data in a SOAP envelope.
    
4. The SharePoint site displays the external list in the user's browser. The user can then perform all the configured operations on the data source for which the user has permissions.
    
## Step 1: Set permissions on the BCS Metadata store
<a name="__toc350352766"> </a>

To do this step, follow the procedure in [Set permissions on the BCS Metadata Store for a Business Connectivity Services on-premises solution in SharePoint 2013](../SharePointServer/administration/deploy-an-on-premises-solution.md).
  
When you finish the steps in that procedure, return to this page and start Step 2: Create a Secure Store credentials mapping.
  
## Step 2: Create a Secure Store credentials mapping
<a name="__toc350352767"> </a>

Typically, when you create a credentials mapping in Secure Store, you map multiple SharePoint users to a single SQL Azure account. You might use a SharePoint group, or just list all the user names. The SQL Azure account has appropriate permissions to access the target database table. The database that you target in SQL Azure is known as the Secure Store Target Application, or just the Target Application. 
  
> [!TIP]
>  Make sure that you have SQL Azure credentials ready. You'll use these credentials when you create the mapping between SharePoint users and a SQL Azure account. 
  
### Create the Secure Store Target Application
<a name="__toc350352768"> </a>

To create a Secure Store Target Application, follow these steps.
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Secure store**, select **Open**.
    
3. On the ribbon, to open the page where you can specify settings for a Target Application, select **New**. 
    
4. In the **Target Application Settings** section, do the following: 
    
  - Under **Target Application ID**, specify a value for a unique ID. This ID maps the External Content type to credentials that are required to authenticate the user. You cannot change the Target Application ID once you create the Target Application.
    
  - Under **Display Name**, specify a user-friendly name for referring to the Target Application.
    
  - Under **Contact E-mail**, specify the email address that you want people to use when they have a question about the Target Application (external data system).
    
  - Under **Target Application Type**, verify that the value is set to **Group Restricted**. Group Restricted means that the Secure Store contains a mapping that connects a group of SharePoint users to a single, external data account that can act on their behalf. In addition, a Group Restricted application type is restricted to the specified external data system.
    
5. In **Credential Fields** section, enter the field names that you want to use for the user name and password of the external data system. By default, the Secure Store uses the **Windows User Name** and **Windows Password**. We recommend that you accept these values. You cannot edit these Field Types after you finish creating the application.
    
    ![Screenshot of the Credential Fields section of the Secure Store Target Application properties page. These fields allow you to specify the logon credentials for the target](media/404c21d4-8677-474c-ad01-5cdd8af06cbf.png)
  
6. In the **Target Application Administrators** section, in the **Target Application Administrators** field, enter the name of a group or a list of users who can edit this Target Application. You can also search for the name of a group in Microsoft Online Directory Server. Typically, this section usually contains the name of the SharePoint Administrator or Global Administrator. 
    
7. In the **Members** section, in the **Members** field, enter the name of the group that will use the Target Application. Generally, this is a group from the Microsoft Online Directory Service (MSODS). 
  
     If you are a Global Administrator, you can create groups in MSODS in the Microsoft 365 admin center. 
    
8. To create the Target Application, and return to the **Secure Store Service** page, select **OK**. 
    
### Store credentials for the Target Application
<a name="__toc350352769"> </a>

After you create the Target Application, you are ready to enter the credentials that Secure Store uses to access the external data. To set the credentials, follow these steps
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Secure store**, select **Open**.
  
3. Select the arrow next to the new Target Application, and then select **Set Credentials**. 
    
4. In the **Set Credentials for Secure Store Target Applications (Group)** dialog, enter the user name and password of the account. The account must have access to the target database. In the following image, the username is **Windows User Name**, and the password is **Windows Password**.
    
    > [!IMPORTANT]
    >  Keep a secure record of this information. After you set these credentials, an administrator cannot retrieve them. 
  
    ![Screenshot that shows the Credential Fields dialog that you use when you create a Secure Store Target Application. It shows the default values, Windows User Name and Windows Password.](media/37a315d6-63db-428b-9766-e3e94904be06.png)
  
## Step 3: Create the External Content Type
<a name="__toc350352770"> </a>

You can create an External Content Type (ECT) by using Microsoft Visual Studio, or by using Microsoft SharePoint Designer 2010. This procedure describes how to create an ECT in SharePoint Designer 2010. Microsoft SharePoint Designer 2010 is available as a [free download](https://www.microsoft.com/download/en/details.aspx?id=16573) from the Microsoft Download Center. 
  
You must be a SharePoint Administrator or Global Administrator in your organization to perform this task.
  
To create an ECT, follow these steps.
  
1. Start Microsoft SharePoint Designer.
    
2. To open the SharePoint team site at the root collection, select **Open Site**. The URL for the root collection will resemble this example URL: `https://tailspintoys.sharepoint.com`. SharePoint might display a prompt for valid credentials. 
    
    > [!NOTE]
    >  If SharePoint displays a prompt for you to add a new user, ensure the user account you use has sufficient permissions. The user account must be able to make and test BCS changes to the SharePoint site. Typically, a SharePoint or global admin performs these steps. <br> If you want to change to a different user, select **Add a new user**, select **Personal** or **Organization**, sign in to the site as the SharePoint Administrator or Global Administrator, and select **Sign In**. 
  
3. After the site opens, in the **Site Objects** tree on the left of the application window, select **External Content Types**.
    
4. Select the **External Content Types** tab, and in the ribbon, to begin the creation process, select **External Content Type**.
    
5. In the **External Content Type Information** section of the page, change the **Name** and **Display Name**. Make certain that the **Name** is descriptive. The **Display Name** is a friendly name for the ECT. 
    
6. To open the Operation Designer page, select the link **Click here to discover external data sources and define operations**. 
    
    ![Screenshot of the External Content Type Information panel, and the link Click here to discover external data sources and define operations, which is used to make a BCS connection.](media/9b6c66c9-9e95-40aa-8b99-459ec16070fd.png)
  
7. To open the **External Data Source Type Selection** dialog, select **Add Connection**. 
    
8. To access the SQL Azure database, select **SQL Server**. 
    
    ![Screenshot of the Add Connection dialog where you can choose a data source type. In this case, the type is SQL Server, which can be used to connect to SQL Azure.](media/0eaef7d3-8f67-403b-be39-a8c54922fd17.png)

    > [!NOTE]
    >  You cannot use on-premises data sources, such as .NET Type, with SharePoint in Microsoft 365. In addition, you cannot use a SQL Server data source that is on-premises with SharePoint in Microsoft 365. 
  
9. When you select SQL Server, specify the following:
    
    - **Database Server name**
    
    - **Database Name**
    
    - **Name**
    
    > [!IMPORTANT]
    >  The URL you use to access the database contains the Fully Qualified Server Name. For example, if you access the database via `https://aaapbj1mtc.database.windows.net` your Fully Qualified Server Name is **aaapbj1mtc.database.windows.net**. > If you log on at a higher level, such as the Management Portal for Microsoft Azure, you can discover the Fully Qualified Server Name. On the portal page, under **Subscriptions**, select the name of your subscription. Then, under **Fully Qualified Server Name**, expand your subscription and the server name. Names of databases appear under each server name. 
  
    ![Screenshot of the SQL Server Connection dialog where you can fill in the name of your SQL Azure database server and use Connect with Impersonated Custom ID to enter your Secure Store Application ID.](media/b99c06d1-046e-43c4-984f-c120d746e30a.png)
  
    In the **SQL Server Connection** dialog, select **Connect with Impersonated Custom Identity**. Then, in the **Secure Store Application ID** text box, type the Secure Store Application ID that stores credentials for the target database and then select **OK**.
    
10. If you see a prompt for credentials to access the external data source, to access the external data system, enter the correct **User name** and **Password** credentials. Then, to connect, select **OK**. 
    
    The **Data Source Explorer** tab, you can view a list of tables that are available from the SQL Azure database. To see a list of possible operations for this table, open the shortcut menu for the table. 
    
    You can select specific options such as New Read Item Operation and New Update Operation for the table. Or, you can just select **Create All Operations**.
    
    ![Screenshot that shows the Tailspintoys database in SharePoint Designer. If you right click on the table name, a menu appears where you can select operations to create.](media/e9d027a3-89f0-49fe-ac71-5bdbfd3af82c.png)
  
11. To open a wizard, select **Create All Operations**, and then select **Next**.
    
    On the **Operation Properties** page of the wizard, in the **Errors and Warnings** pane, read about any issues. It is important to resolve reported issues that you see. For example, you may have to choose a field to show in an external item picker control. For a customer table, you could choose the customer name. 
    
    ![Screenshot of the All Operations dialog, explaining you've chosen to create all properties needed for Create, Read Item, Update, Delete, and Read List rights.](media/2f68f9b6-2227-4ed8-9d0b-d36615ea7ae1.png)
  
    > [!IMPORTANT]
    >  The wizard may display a warning message if unique, required fields, such as 'CustomerID', exist in the target table. This is valid if the specified field is required and unique in the table, such as a primary key. 
  
    ![Screenshot 2 of the All Operations dialog in SharePoint Designer. This page shows warnings that explain settings for key properties on the list.](media/02428447-b2d2-4714-b585-71e195660ad8.png)
  
    > [!NOTE]
    >  For more information about how to define filters in external content types, see [How to: Define filters for External Item Picker controls](/previous-versions/office/developer/sharepoint-2010/ff798274(v=office.14)) . 
  
12. To accept the operations properties that you configured, select **Finish**. SharePoint Designer displays the operations as a list of ECT Operations. 
    
When this step is complete, you are ready to create an External List to use the data from the external source.
  
## Step 4: Create an External List
<a name="__toc350352771"> </a>

You can create an External List by using SharePoint Designer, or by adding an External List as an app on the SharePoint team site. This procedure describes how to create an External List from the team site in SharePoint.
  
### Create an External List by using SharePoint
<a name="__toc350352772"> </a>

1. Go to the home page of the SharePoint team site.
    
2. Select **Settings**![Microsoft 365 Settings button](media/a9a59c0f-2e67-4cbf-9438-af273b0d552b.png) \> **Add an app**.
    
3. On the **Your Apps** page, in the search dialog, enter **External List**, and search. 
    
4. To open the **Adding External List** dialog, double-click the **External List** tile. 
    
5. In the **Name** box, enter a name for the list. 
    
6. In the **External Content Type** box, enter the name that you want to use. For example, you might use the name of the ECT that you created in SharePoint Designer. Alternatively, you can select the database icon to browse for the name of an ECT. 
    
7. Select **Create**.
    
### Create an External List by Using SharePoint Designer 2010
<a name="__toc350352773"> </a>

1. In SharePoint Designer 2010, on the ribbon, select **Create Lists and Forms**.
    
     SharePoint Designer may display a message that states, "Creating lists and forms requires the external content type to be saved". select **Yes** to save the ECT. 
    
    In the **Create List and Forms for databasename Customers** dialog, in the **List Name** text box, enter a meaningful name for the External List. For example, if you created an ECT for the "Customers" database table, you might use "Tailspintoys Customers" in the list name. 
    
2. From the list of Operations, select a **Read Item Operation**. 
    
3. In the **System Instance** text box, enter the name of the SQL Azure database. 
    
    ![The Create List and Form dialog with the selection made to create an External List, with all four fields filled out.](media/ab3907e2-f802-4e6e-a2df-73b678e1bae8.png)
  
4. To create the External List in the SharePoint site, select **OK**, and then select **Save**. 
    
## Step 5: Grant permissions to manage the ECT
<a name="__toc350352774"> </a>
To finish setting up the External List, you have to grant permissions to the people who will use the list. To grant permissions, follow these steps.
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **BCS**, select **Open**.
    
3. Select **Manage BDC Models and External Content Types**. 
    
4. Select the check box next to the name of the ECT that you just created, and then select **Set Object Permissions**. 
    
    > [!IMPORTANT]
    >  You must manually assign permissions to manage the ECT to a Global Administrator or SharePoint Administrator by using the **Set Object Permissions** command. If you do not assign these permissions explicitly, the admins won't have permission to manage the ECT. 
  
    ![The Set Object Permissions button in the ribbon on the BCS page of the SharePoint admin center](media/719d5798-9ec7-45c0-951b-f3a2ba73a6bf.png)
  
5. In the **set object permissions** dialog, select the check boxes for all the permissions (( **Edit, Execute, Selectable in Clients, and Set Permissions**) that the SharePoint admin needs. 
    
    > [!NOTE]
    >  Make sure that at least one user or group has **Set Permissions** rights. If you don't assign someone this right, you might create an unmanageable BCS connection. 
  
    ![Screenshot of the SetObject Permissions dialog in SharePoint. Use this dialog to set permissions for a specified External Content Type.](media/5e760b77-b0cc-4be9-870e-217e902d9245.png)
  
6. Select **Propagate permissions to all methods of this external content type**. Doing this overwrites any existing permissions. 
    
    > [!NOTE]
    >  If you want to add a group that can use the External Lists, you must also give the group **Execute** rights. That enables users in the group to run a query to the external source, and view the results in SharePoint.

