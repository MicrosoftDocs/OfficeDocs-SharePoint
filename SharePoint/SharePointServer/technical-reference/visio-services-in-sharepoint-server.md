---
title: "Visio Services in SharePoint Server knowledge articles"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e8eb4d14-cb99-4f43-b845-0cc0963fab47
description: "Resolve alerts in Visio Services in SharePoint Server: symptoms, causes, and possible resolutions."
---

# Visio Services in SharePoint Server knowledge articles

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Resolve alerts in Visio Services in SharePoint Servers 2019, 2016, and 2013: symptoms, causes, and possible resolutions.

> [!NOTE]
> The Microsoft Silverlight-based rendering will no longer be supported as of October 12, 2012. This means that, Silverlight-based rendering will no longeer be supported in SharePoint Server 2019. Visio Services will only render Visio diagrams using the PNG-based technology.
  
The articles in this section are knowledge articles for Visio Services in SharePoint Servers 2019 and 2016. Typically, you would see these articles after clicking a link in an alert in the Systems Center Operations Manager console. You can use these articles to help you troubleshoot and resolve problems in Visio Services. 

Download and install:

- [System Center Management Pack for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57776)

- [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409) 

- [System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568) 

- [System Center Monitoring Pack for SharePoint Foundation 2013](https://go.microsoft.com/fwlink/p/?LinkId=272567)
  
In this section:
  
- [Visio Graphics Service failed to initialize the rasterizer ](#Rasterizer)
    
- [Visio Graphics Service failed to initialize the rasterizer](#Rasterizer2)
    
- [Visio Graphics Service cannot find the configuration manager ](#VisioConfig)
    
- [Visio Graphics Service unable to connect to the application server returned by the application proxy ](#VisioApp)
    
## Visio Graphics Service failed to initialize the rasterizer
<a name="Rasterizer"> </a>

 **Alert Name:**Visio Graphics Service failed to initialize the rasterizer
  
 **Summary:** Visio Services in SharePoint Server requires a rasterizer to render a Visio diagram. When the rasterizer is not initialized by Visio Services, VSDX and VSDM diagrams will not render.Symptoms: One or more of the following symptoms might appear: 
  
- Visio Services might not render diagrams. 
    
- This event appears in the event log: Event ID: 8076 Description: Rasterizer initialization failed.
    
### Cause

The rasterizer, an internal component of Visio Graphics Services, is not running or was not initialized correctly.
  
### Resolution

Restart Visio Services:
  
1. On the **Central Administration** page, in the **System Settings** section, from the reading pane, click **Manage servers in this farm**.
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate **Visio Graphics Service**. Click **Stop**, and then click **Start**.
    
## Visio Graphics Service failed to initialize the rasterizer
<a name="Rasterizer2"> </a>

 **Alert Name:**Visio Graphics Service failed to initialize the rasterizer
  
 **Summary:** Visio Services in SharePoint Server requires a rasterizer to render a Visio diagram. When the rasterizer is not initialized by Visio Services, VSDX and VSDM diagrams will not render. This rule is triggered when the Visio Graphics Services failed to initialize the rasterizer. 
  
### Cause

Symptoms: One or more of the following symptoms might appear:
  
- Visio Services might not render diagrams. 
    
- This event appears in the event log: Event ID: 8076 Description: Rasterizer initialization failed.
    
### Resolution

Restart Visio Services:
  
1. On the **Central Administration** page, in the **System Settings** section, from the reading pane, click **Manage servers in this farm**.
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate **Visio Graphics Service**. Click **Stop**, and then click **Start**.
    
## Visio Graphics Service cannot find the configuration manager
<a name="VisioConfig"> </a>

 **Alert Name:**Visio Graphics Service cannot find the configuration manager
  
 **Summary:** Visio Services in SharePoint Server stores its application settings in the configuration-a12-n database. Access to this database is extremely important for the service to function. 
  
This rule is triggered when the Visio Graphics Service cannot find configuration manager. 
  
Symptoms: One or more of the following symptoms might appear:
  
- Visio Services might not render diagrams.
    
- This event appears in the event log: Event ID: 8040 Description: Can't find configuration manager.
    
### Cause

One or more of the following might be the cause: 
  
- The configuration database is inaccessible.
    
- The configuration database is responding slowly because of heavy network activity or load on the Microsoft SQL Server.
    
### Resolution

Resolution 1: Verify the status of the SQL Server configuration database:
  
1. On the **SharePoint Central Administration** website, in the **System Settings** section in the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the Configuration database server and the name and the version of the configuration database. 
    
3. Start **SQL Server Management Studio** and connect to the configuration database server. 
    
4. If the configuration database does not exist, run the SharePoint Products and Technologies Configuration Wizard.
    
Resolution 2: Verify the SQL Server network connection:
  
1. On the **Central Administration** website, in the **System Settings** section, from the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the Configuration database server and the name and the version of the configuration database information. 
    
3. Open a Command Prompt window and type ping to confirm the server connection.
    
    Failure to contact the server indicates a problem with the network connection or another problem that prevents a response from the server
    
4. Log on to the server and troubleshoot the issue.
    
## Visio Graphics Service unable to connect to the application server returned by the application proxy
<a name="VisioApp"> </a>

 **Alert Name:**Visio Graphics Service unable to connect to the application server returned by the application proxy
  
 **Summary:** The application for Visio Services in SharePoint Server uses a proxy to abstract communication between the front-end service and back-end service. This proxy also provides a load-balancing mechanism between servers. For Visio Services to function, the front-end service must be connected to the application server that is returned by the application proxy. This rule is triggered when the Visio Graphics Service cannot connect to the application server. 
  
Symptoms: One or more of the following symptoms might appear:
  
- Visio Services in SharePoint might not render diagrams.
    
- This event appears in the event log: Event ID: 8049 Description: Application proxy invalid endpoint for \<descriptive text\>.
    
### Cause

One or more of the following might be the cause: 
  
- The specified SharePoint Server application server is inaccessible.
    
- The specified application server is responding slowly because of heavy network activity or load on the specific server.
    
### Resolution

Resolution 1: Check the error logs:
  
1. Open the Windows Event Viewer.
    
2. Search for event ID 8049 in the Windows Application Event log.
    
3. In the event description, note the application server that is failing.
    
Resolution 2: Verify the application server connection:
  
1. From the failing application server, open the SharePoint Central Administration website.
    
2. If you cannot access the Central Administration site from the failing server, make sure that the network settings are correct and that the server has appropriate permissions to join the SharePoint farm.
    
Resolution 3: Verify that Visio Services runs on the failing server:
  
1. On the Central Administration website, in the **System Settings** section, from the reading pane, click **Manage servers in this farm**.
    
2. Verify that Visio Services runs on the failing application server.
    
If there is a service application proxy for the failing service application, create a new service application.
  
Resolution 4: Restart Visio Services:
  
1. On the **Central Administration** page, in the reading pane, in the **System Settings** section, click **Manage servers in this farm**.
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate **Visio Graphics Service**, click **Stop**, and then click **Start**.
    
Resolution 5: Create a new Visio Services application:
  
1. On the **Central Administration** website, in the **Application Management** section, from the reading pane, click **Manage service applications**.
    
2. In the **Type** column, click the name of the Visio Services application that has the failing service instance. 
    
3. On the ribbon, click **Delete**.
    
4. In the **Delete Service Application** dialog box, click **OK**.
    
5. Create a new Visio Services application.
    
## See also
<a name="VisioApp"> </a>

#### Concepts

[Plan for monitoring in SharePoint Server](../administration/monitoring-planning.md)
#### Other Resources

[Plan for Visio Services in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee663482(v=office.14))
  
[System Center Monitoring Pack for SharePoint Foundation](http://go.microsoft.com/fwlink/p/?LinkId=272567)
  
[System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409)
  
[System Center Monitoring Pack for SharePoint Foundation](https://go.microsoft.com/fwlink/p/?LinkId=272567)
  
[System Center Monitoring Pack for SharePoint Server](https://go.microsoft.com/fwlink/p/?LinkId=272568)

