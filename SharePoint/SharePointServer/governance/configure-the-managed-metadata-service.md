---
title: "Configure the Managed Metadata service"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/13/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 76c08191-13da-4cdc-beee-82c30033b7dc
description: "Learn how to configure a Managed Metadata service application in SharePoint Server."
---

# Configure the Managed Metadata service

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In this article we cover how to configure a Managed Metadata service application in SharePoint Server. Be sure you've [planned your configuration](managed-metadata-planning.md) before you follow the procedures below. 
  
To configure a Managed Metadata service application, you perform the following steps:
  
1. Register a managed account in SharePoint Server to run the Managed Metadata service application pool.
    
2. Start the Managed Metadata Web Service (SharePoint Server 2013 only).
    
3. Create a Managed Metadata service application.
    
4. Configure the Managed Metadata service connection
    
## Start the Managed Metadata Web Service (SharePoint Server 2013 only)

If you are using SharePoint Server 2013, you must start the Managed Metadata Web Service on at least one server in your farm. (This service is started automatically in SharePoint Server 2016.)
  
 **To start the Managed Metadata Web Service**
  
1. On the SharePoint Central Administration Web site home page, click **Manage services on server**.
    
2. Click **Server** and then select the server where you want to start the Managed Metadata Web Service. 
    
3. In the **Service** list, click **Start** for the **Managed Metadata Web Service**.
    
## Configure a Managed Metadata service application in SharePoint Server
<a name="section1"> </a>

To run the application pool, you must have a standard domain account. No specific permissions are required for this account. Once the account has been created in Active Directory, follow these steps to register it with SharePoint Server.
  
 **To register a managed account**
  
1. On the SharePoint Central Administration Web site home page, in the left navigation, click **Security**.
    
2. On the Security page, in the **General Security** section, click **Configure managed accounts**.
    
3. On the Managed Accounts page, click **Register Managed Account**.
    
4. In the **User name** box, type the name of the account. 
    
5. In the **Password** box, type the password for the account. 
    
6. If you want SharePoint Server to handle changing the password for the account, select the **Enable automatic password change** box and specify the password change parameters that you want to use. 
    
7. Click **OK**.
    
Once you have configured the registered account, you must create a Managed Metadata service application. Use the following procedure to create the service application.
  
 **To create a Managed Metadata service application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click **New**, and then click **Managed Metadata Service**.
    
3. In the **Name** box, type a name for the service application (for example, Managed Metadata Service).
    
4. In the **Database Server** box, type the instance of SQL Server where you want to create the Managed Metadata database. 
    
5. In the **Database Name** box, type the name that you want to use for the Managed Metadata database. 
    
6. In the **Failover Database Server** box, type the name of your failover database server if you're using one. 
    
7. Select the **Create new application pool** option and type a name for the application pool in the text box. 
    
8. Select the **Configurable** option, and, from the drop-down list, select the account for which you created the managed account earlier. 
    
9. If you're configuring a Content Type Hub, type the URL for that site collection in the **Content Type Hub** box. 
    
10. Click **OK**.
    
The Managed Metadata service application has now been configured. The next step is to configure the settings for the Managed Metadata service connection.
  
## Configure the Managed Metadata service connection
<a name="section1"> </a>

Each managed metadata service application has an associated managed metadata service connection. Using the service connection, you can configure the following four options:
  
- **This service application is the default storage location for Keywords** - Determines if this service application is used as the default location for enterprise keywords. 
    
    If you are using more than one Managed Metadata service application, only select this option for one service application per web application.
    
    If you do not want to use the enterprise keywords functionality, make sure this check box is not selected for any of your Managed Metadata service connections.
    
- **This service application is the default storage location for column specific term sets** - Determines if this service application is used to store custom term sets that are created at the site collection level. 
    
    If you are using more than one Managed Metadata service application, only select this option for one service application per web application.
    
    If you do not want to allow custom term sets, make sure this check box is not selected for any of your Managed Metadata service connections.
    
- **Consumes content types from the content type gallery at http://\<site\>** - Determines if this service application makes the content types that are that are defined in the specified content type gallery available to users of sites in this web application. This option is available only if the service has a hub defined to share content types. 
    
- **Push-down Content Type Publishing updates from the Content Type Gallery to sub-sites and lists using the content type** - Determines if change in content types are published to sub-sites and lists that use the content type. 
    
Use the following procedure to set these options:
  
 **To configure a managed metadata service connection**
  
1. In Central Administration, under **Application Management**, click **Manage service applications**.
    
2. Find the managed metadata service connection for the service application that you want to configure. (Look for **Managed Metadata Service Connection** in the **Type** column.) 
    
3. Highlight that row, and then click **Properties**.
    
4. Select the check boxes for the options that you want to enable, and then click **OK**.
    

