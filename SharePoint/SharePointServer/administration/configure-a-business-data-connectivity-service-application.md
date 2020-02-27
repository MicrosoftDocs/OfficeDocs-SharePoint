---
title: "Configure a Business Data Connectivity service application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 41ec2552-43cd-471a-ba22-1962297758c0
description: "Learn how to create a Microsoft Business Connectivity Services service application in SharePoint Server."
---

# Configure a Business Data Connectivity service application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Microsoft Business Connectivity Services is a SharePoint Server service application. You must create it if it was not created during your farms initial configuration.
  
## Configure the Business Connectivity Services application pool account
<a name="section1"> </a>

The application pool for the Business Connectivity Services service application requires a SharePoint Server managed account (generally an Active Directory account) to run. This account must have access to the content databases containing the sites where Business Connectivity Services will be used.
  
If you run the service application using the same application pool account as the web application where the content databases are located, this required database access is configured automatically. However, we recommend that you use a different account for the Business Connectivity Services application pool, especially in a large or complex farm. This allows for greater control over data and resource access.
  
If you choose to use the same managed account for Business Connectivity Services as is being used for the web application, you can skip the procedures in this section. If you choose to create a new managed account, you must do the following:
  
1. Register a managed account in SharePoint Server. (You will need an Active Directory user account for this step. Have your Active Directory administrator create it.)
    
2. Grant access for this account to the content databases that contain the sites where Business Connectivity Services will be used. This process includes running a Microsoft PowerShell script from the SharePoint 2016 Management Shell.
    
The first step is to register a managed account. Use the following procedure to register the Active Directory account that you want to use for the Business Connectivity Services application pool.
  
 **To register a managed account**
  
1. In the SharePoint Server Central Administration Web site, click **Security**.
    
2. In the **General Security** section, click **Configure managed accounts**.
    
3. Click **Register Managed Account**.
    
4. In the **Service account credentials** section, type the user name and password for the Active Directory account that you want to register. 
    
5. Optionally, if the account password is set to expire after a certain length of time, configure the automatic password change settings to have SharePoint Server change the password.
    
6. Click **OK**.
    
Once you have registered the managed account, you must grant that account access to the content databases containing the sites where you'll use Business Connectivity Services. Use the following procedure to grant database access to the account. Follow this procedure for each web application that contains a content database where you plan to use Business Connectivity Services.
  
 **To grant content database access to an account**
  
1. Open the **SharePoint 2016 Management Shell** as administrator. 
    
2. At the Microsoft PowerShell command prompt, type the following, pressing Enter after each line:
    
  ```
  $w = Get-SPWebApplication -identity <web application>
  $w.GrantAccessToProcessIdentity("<service account>")
  ```

Once you have finished granting content database access to the managed account, the next step is to create a Business Connectivity Services service application.
  
## Create a Business Data Connectivity Services service application
<a name="section1"> </a>

If you're using SharePoint Server 2013, you must start the Business Data Connectivity service on at least one server in your farm. (If you're using SharePoint Server 2016, service provisioning is handled automatically by MinRole.)
  
 **Start the Business Data Connectivity service (SharePoint Server 2013 only)**
  
1. Open the SharePoint Central Administration website for the server farm that contains your BCS solution.
    
2. On the Quick Launch, click **System Settings**. 
    
3. On the **System Settings** page, under **Servers**, click **Manage services on server**.
    
4. Check the value in the **Server** field. If the server name shown there is not the server that you want running the **Business Data Connectivity Service** on, click on the down arrow, click **Change Server** and select the correct server. 
    
5. If necessary, next to Business Data Connectivity Service, under the **Action** column, click **Start**.
    
Use the following procedure to create a Business Connectivity Services service application.
  
 **To create a Business Data Connectivity Services service application**
  
1. Open the SharePoint Central Administration website for with a farm administrator account.
    
2. Under **Application Management**, choose **Manage service applications**.
    
3. Click **New** and then click **Business Data Connectivity Service**.
    
4. Configure the setting in the **Create New Business Data Connectivity Service Application** configuration page as follows: 
    
1. In the **Service Application Name** box type a name for the service application. 
    
2. In the **Database** area, leave the prepopulated values for **Database Server**, **Database Name**, and **Database authentication**, which is **Windows authentication (recommended)** unless you have specific design needs to change them. 
    
3. If you have SQL Server database mirroring configured and you want to include the Business Data Connectivity Service database in mirroring, provide the name of the failover database server in the **Failover Database Server** box. 
    
4. Type a name for a new application pool in the **Application pool name** box. 
    
5. Select the managed account that you registered from the drop down list.
    
5. Click **OK** to create the new Business Data Connectivity Service Application and click **OK** again. 
    
6. Select the row that the **Business Data Connectivity Service Application** is in, not the proxy row. 
    
7. Click **Administrators** in the **Operations** area and add any accounts that you want to be able to administer the Business Data Connectivity service application granting them full control. When these individuals open Central Administration they will be able to administer the Business Data Connectivity service application. 
    

