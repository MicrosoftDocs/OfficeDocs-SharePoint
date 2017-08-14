---
title: Configure Visio Services data refresh in SharePoint Server by using external data connections
ms.prod: SHAREPOINT
ms.assetid: 067783ba-e22f-41a8-9a1b-38a89c3a30c2
---


# Configure Visio Services data refresh in SharePoint Server by using external data connections
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:** Configure Visio Services to refresh data using an external Office Data Connection (ODC) file and a Secure Store Service target application.You can map a specific group of users to a specific data source by using group mappings and an external data connection file in Secure Store. This provides more fine-grained security than using the unattended service account. Creating a group mapping with an external data connection file consists of the following steps:
1. Create an account to use for data access
    
  
2. Create a logon for the data access account on the data source
    
  
3. Create a Secure Store target application that uses the data access account credentials
    
  
4. Create an Office Data Connection (ODC) file by using Visio and publish it to a SharePoint data connection library
    
  
5. Use the ODC file as a data source in Visio
    
  
The first step is to create an account to use for data access. Have your administrator create an Active Directory account that you can use to access your data sources.
> [!NOTE:]

  
    
    

Once the account has been created, follow these steps to create a logon for the data access account in SQL Server. (If you are using a data source other than SQL Server, see the instructions for your data source to create a logon with data-read permissions for the data access account.) **To create a SQL Server logon for the data access account**
1. In SQL Server Management Studio, connect to the database engine.
    
  
2. In Object Explorer, expand **Security**.
    
  
3. Right-click **Logins**, and then click **New Login**.
    
  
4. In the **Login name** box, type the name of the Active Directory account that you created for data access.
    
  
5. Under **Select a page**, click **User Mapping**.
    
  
6. Select the **Map** check box for the database that you want to provide access to, and then, in the **Database role membership for: <database>** section, select the **db_datareader** check box.
    
  
7. Click **OK**.
    
  
Once you have created a logon for the data access account and granted the account access to your data source, you must create a target application in Secure Store to contain the credentials for the data access account. This target application will be used to map the data access account to the users to whom you want to grant data access.When you create the target application, you will be able to specify individual users to whom you want to grant data access, or you can specify an Active Directory group. For ease of administration, we recommend that you use an Active Directory group. This allows you to update the user list in the future without having to update the target application.Use the following procedure to create the target application. **To create a target application**
1. On the the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
  
2. Click the Secure Store Service service application.
    
  
3. On the ribbon, click **New**.
    
  
4. In the **Target Application ID** box, type an ID for the target application (for example, **VisioServicesDataAccess** ).
    
  
5. In the **Display Name** box, type a name for the target application.
    
  
6. In the **Contact E-mail** box, type an email address.
    
  
7. In the **Target Application Type** drop-down list, select **Group**.
    
  
8. Click **Next**.
    
  
9. Leave the default credential fields, and then click **Next**.
    
  
10. On the "Specify the membership settings" page:
    
1. In the **Target Application Administrators** box, type the account of the user who will administer this account.
    
    > [!NOTE:]
      
2. In the **Members** box, type the names of the users to whom you want to give data access or the name of the Active Directory group that contains those users.
    
  
3. Click **OK**.
    
  
Once the target application has been created, you must set the target application to use the credentials for the data access account that you created. Use the following procedure to set the credentials. **To set the credentials for the target application**
1. On the Secure Store Service Application page, in the **Target Application ID** column, point to the target application that you just created, click the arrow that appears, and then click **Set Credentials**.
    
  
2. In the **Windows User Name** box, type the Active Directory account that you created for data access.
    
  
3. Type and confirm the password for the account.
    
  
4. Click **OK**.
    
  
The next step is to create an ODC file that references the Secure Store target application that you just created. You can create the ODC file in Visio as part of your diagram creation process.Use the following procedure to create an ODC file and create a data-connected diagram. **To create an ODC file and link data to shapes in Visio**
1. In Visio, open a diagram or create a new diagram.
    
  
2. On the ribbon, click the **Data** tab, and then click **Link Data to Shapes**.
    
  
3. On the Data Selector page, choose the **Microsoft SQL Server database** option, and then click **Next**.
    
  
4. On the Connect to Database Server page, type the name of your database server, and then click **Next**.
    
  
5. On the Select Database and Table page, select the database to which you want to connect, and then click **Next**.
    
  
6. On the Save Data Connection File and Finish page:
    
1. Click **Authentication Settings**.
    
  
2. On the **Visio Services Authentication Settings** dialog box, choose the **Use a stored account** option, type the application ID of the Secure Store target application that you created in the **Application ID** text box, and click **OK**.
    
  
3. Click Browse.
    
  
4. Browse to a data connection library.
    
    > [!NOTE:]
      
5. Type a name for the ODC file, and then click **Save**.
    
  
6. Click **Finish**.
    
  
7. If the **Web File Properties** dialog box appears, click **OK**.
    
  
8. On the Select Data Connection page, click **Finish**.
    
  
9. Connect the data to the shapes in your diagram.
    
  
10. When you are ready to save the drawing, click **File**, click **Save**, and then browse to a SharePoint document library.
    
  
11. Type a file name, and then click **Save**.
    
  
Once the diagram has been published, it is available to view by using Visio Services. When the data in the diagram is refreshed, it uses the ODC file that you specified and the Secure Store target application specified within.Once the ODC file has been saved to the data connection library, you can connect directly to it when linking data to shapes in Visio. This allows you to share a single data connection file among multiple Visio diagrams.Use the following procedure to connect to an existing ODC file. **To create a data-connected diagram by using an ODC file**
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
    
  

# See also

#### 

 [Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account](html/configure-visio-services-data-refresh-in-sharepoint-server-2016-by-using-the-una.md)
  
    
    

  
    
    

