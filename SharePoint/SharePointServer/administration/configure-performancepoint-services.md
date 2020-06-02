---
title: "Configure PerformancePoint Services"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ae626fda-efc1-4b99-9909-829346b04b6f
description: "Configure PerformancePoint Services in SharePoint Server."
---

# Configure PerformancePoint Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to create and configure a PerformancePoint Services service application.
  
To properly configure PerformancePoint Services, do the following steps in the order listed: 
  
1. [Install ADOMD.NET from the SQL Server 2012 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkId=275448)
    
2. [Configure the PerformancePoint Services application pool account](configure-performancepoint-services.md#section1)
    
3. [Start the PerformancePoint service (SharePoint Server 2013 only)](#section2) (SharePoint Server 2013 only) 
    
4. [Create a PerformancePoint Services service application](configure-performancepoint-services.md#section3)
    
5. [Configure PerformancePoint service application associations](#section4)
    
## Configure the PerformancePoint Services application pool account
<a name="section1"> </a>

The application pool for the PerformancePoint Services service application requires a SharePoint Server managed account (generally an Active Directory account) to run. This account must have access to the content databases where PerformancePoint data will be stored.
  
If you run the service application using the same application pool account as the web application where the content databases are located, this required database access is configured automatically. However, we recommend that you use a different account for the PerformancePoint Services application pool, especially in a large or complex farm. This allows for greater control over data and resource access.
  
If you choose to use the same managed account for PerformancePoint Services as is being used for the web application, you can skip the procedures in this section. If you choose to create a new managed account, you must do the following:
  
1. Register a managed account in SharePoint Server. (You will need an Active Directory user account for this step. Have your Active Directory administrator create it.)
    
2. Grant access for this account to the content databases that will contain PerformancePoint data. This process includes running a Microsoft PowerShell script from the SharePoint 2016 Management Shell.
    
The first step is to register a managed account. Use the following procedure to register the Active Directory account that you want to use for the PerformancePoint Services application pool.
  
 **To register a managed account**
  
1. In the SharePoint Server Central Administration Web site, click **Security**.
    
2. In the **General Security** section, click **Configure managed accounts**.
    
3. Click **Register Managed Account**.
    
4. In the **Service account credentials** section, type the user name and password for the Active Directory account that you want to register. 
    
5. Optionally, if the account password is set to expire after a certain length of time, configure the automatic password change settings to have SharePoint Server change the password.
    
6. Click **OK**.
    
Once you have registered the managed account, you must grant that account access to the content databases where PerformancePoint data will be stored. Use the following procedure to grant database access to the account. Follow this procedure for each web application that contains a content database where PerformancePoint Services data will reside.
  
 **To grant content database access to an account**
  
1. Open the **SharePoint 2016 Management Shell** as administrator. 
    
2. At the Microsoft PowerShell command prompt, type the following, pressing Enter after each line:
    
  ```
  $w = Get-SPWebApplication -identity <web application>
  $w.GrantAccessToProcessIdentity("<service account>")
  ```

Once you have finished granting content database access to the managed account, the next step is to create a PerformancePoint Services service application.
  
## Start the PerformancePoint service (SharePoint Server 2013 only)
<a name="section2"> </a>

If you are using SharePoint Server 2013, you must start the PerformancePoint service on the application server where you want to run PerformancePoint Services. (In SharePoint Server 2016 this is handled automatically by MinRole.) You can start the service on multiple application servers for better performance, if you want, but the service must be started on at least one server. Use the following procedure to start the PerformancePoint service.
  
 **To start the PerformancePoint Service**
  
1. In Central Administration, in the **System Settings** section, click **Manage services on server**.
    
2. Note the server specified in the **Server** box. If you want to run the PerformancePoint service on a different server, click the current server, and then click **Change Server** and select the server that you want. 
    
3. Click **Start** next to **PerformancePoint Service**.
    
## Create a PerformancePoint Services service application
<a name="section3"> </a>

Use the following procedure to create the service application.
  
 **To create a PerformancePoint Services service application**
  
1. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
2. Click **New**, and then click **PerformancePoint Service Application**.
    
3. Type a name for the service application and select the **Add this service application's proxy to the farm's default proxy list** check box. 
    
4. Select the **Create new application pool** option and type a name for the application pool. 
    
5. Under the **Configurable** option, select the managed account to run the application pool. 
    
6. Click **Create**.
    
7. Click **OK**.
    
When you configure the service application in SharePoint Server 2016, the PerformancePoint Service will autoprovision on all servers in the farm that are running under the Front-end role.
  
## Configure PerformancePoint service application associations
<a name="section4"> </a>

For PerformancePoint Services to function, the PerformancePoint Services service application proxy must be associated with the default web application. Use the following procedure to confirm that the association is configured between the web application and the PerformancePoint Services proxy.
  
 **To configure service application associations**
  
1. In Central Administration, click **Application Management**.
    
2. In the **Service Applications** section, click **Configure service application associations**.
    
3. Under the **Application Proxy Group** column, click **default**.
    
4. Ensure that the **PerformancePoint Services** box is selected. 
    
5. Click **OK**.
    

