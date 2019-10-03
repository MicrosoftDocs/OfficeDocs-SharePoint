---
title: "Machine Translation service in SharePoint Server knowledge articles"
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
ms.assetid: 38095e9b-5b48-4d2a-a787-3f7900b138e0
description: "Learn how to resolve alerts about the Machine Translation service in the SharePoint Server management pack for Systems Center Operations Manager (SCOM)."
---

# Machine Translation service in SharePoint Server knowledge articles

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

Learn how to resolve alerts about the Machine Translation service in the SharePoint Servers 2019, 2016, and 2013 management pack for Systems Center Operations Manager (SCOM).
  
The articles in this section are knowledge articles for the Machine Translation service in SharePoint Server. Typically, you would see these articles after clicking a link in an alert in the Operations Manager console. You can use these articles to help you troubleshoot and resolve problems that involve the Machine Translation service. 

Download and install:

- [System Center Management Pack for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57776)

- [System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409) 

- [System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568) 

- [System Center Monitoring Pack for SharePoint Foundation 2013](https://go.microsoft.com/fwlink/p/?LinkId=272567)

Use the following to resolve alerts about the Machine Translation service:
  
- [Machine Translation Service: Queue database not accessible ](#QueueDB)
    
- [Machine Translation Service: Machine translation failure ](#TransFail)
    
- [Machine Translation Service: Machine translation failure](#TransFail2)
    
- [Machine Translation Service not accessible ](#TransServ)
    
- [Machine Translation Service: Content not accessible ](#TransContent)
    
- [Machine Translation Service: Worker failure ](#TransWorker)
    
## Machine Translation Service: Queue database not accessible
<a name="QueueDB"> </a>

 **Alert Name:**Machine Translation Service: Queue database not accessible
  
 **Summary:** A critical state of this Monitor indicates that the Machine Translation Service cannot access content that it has to translate. 
  
Symptoms:
  
- New Jobs cannot be submitted successfully.
    
- Existing Job Items never complete or seem to "hang" and make no progress in the Job Queue.
    
### Cause

One or more of the following might be the cause:
  
- The queue database is not responsive enough because of activity on the network or physical SQL server.
    
- Permissions to access the custom database are no longer valid.
    
- The queue database is inaccessible.
    
### Resolution

Resolution 1: Verify the status of the SQL Server Machine Translation Service database:
  
1. On the **SharePoint Central Administration** website, in the **System Settings** section, from the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the **Machine Translation Service** database server, and the name and the version of the configuration database. 
    
3. Start SQL Server Management Studio and connect to the configuration database server.
    
4. If the configuration database does not exist, run the SharePoint Products and Technologies Configuration Wizard.
    
Resolution 2: Verify the SQL Server network connection:
  
1. On the **Central Administration** website, in the System Settings section, from the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the Machine Translation Service database server, and the name and the version of the configuration database information. 
    
3. Open a Command Prompt window and type ping to confirm the server connection.
    
4. Failure to contact the server indicates a problem with the network connection or another problem that prevents a response from the server.
    
5. Log on to the server and troubleshoot the issue.
    
## Machine Translation Service: Machine translation failure
<a name="TransFail"> </a>

 **Alert Name:**Machine Translation Service: Machine translation failure
  
 **Summary:** A critical state of this Monitor indicates that machine translation through the online translation service, is failing. 
  
Symptoms:
  
As long as a connection to the online translation service is not established, the service will function correctly but will fail every Translation Item that is processed.
  
### Cause

One or more of the following might be the cause:
  
- The Machine Translation Service is not connected to the Internet.
    
- The online translation service is down.
    
- The online translation service has experienced a certain amount of intermittent failures (beyond a set threshold).
    
### Resolution

Ensure the Machine Translation Service application has web access:
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the **Manage Service Applications** page, in the list of service applications, click **Machine Translation Service**.
    
4. In the **Online Translation Connection** section, in the web proxy server box, do one of the following: 
    
  - Click **Use default internet settings**. 
    
  - Click **Use the proxy specified**, and enter a web proxy server and a port number.
    
Validate the MachineTranslationAddress, MachineTranslationClientId, and MachineTranslationCategory for the Machine Translation Service application:
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In the PowerShell command prompt, type the following: 
    
     `Get-SPServiceApplication -Name "name" | ft MachineTranslationAddress, MachineTranslationClientId, MachineTranslationCategory`
    
    where "name" is the Name of your Machine Translation Service application.
    
3. Validate the values returned by comparing against any documentation or making a test call.
    
4. Correct any values based on validation. If a value cannot be validated, use the default value.
    
## Machine Translation Service: Machine translation failure
<a name="TransFail2"> </a>

 **Alert Name:**Machine Translation Service: Machine translation failure
  
 **Summary:**A critical state of this Monitor indicates that the Machine Translation Service Timer Job is failing.
  
Symptoms:
  
- New Jobs will successfully enter into the database. However, the translation items for that job will never start.
    
- The existing Jobs may not finish: Any translation items that are already assigned to application servers may still succeed, but translation items that are not assigned to application servers will not start. That leaves the Job perpetually incomplete.
    
### Cause

The Machine Translation Service's queue timer job is not running.
  
### Resolution

Resolution 1: Restart the Machine Translation Service
  
1. On the **Central Administration website**, in the **System Settings** section, from the reading pane, click **Manage servers in this farm.**
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate the **Machine Translation Service**. Click **Stop**, and then click **Start**.
    
Resolution 2: Create a new Machine Translation Service application
  
1. On the **Central Administration website**, in the **Application Management** section, from the reading pane, click **Manage service applications**.
    
2. In the **Type** column, click the name of the Machine Translation Service application that has the failing service instance. 
    
3. On the ribbon, click **Delete**.
    
4. In the **Delete Service Application** dialog box, click **OK**.
    
5. Create a new Machine Translation Service application.
    
## Machine Translation Service not accessible
<a name="TransServ"> </a>

 **Alert Name:**Machine Translation Service not accessible
  
 **Summary:** A critical state of this Monitor indicates that the Machine Translation Service is not accessible. 
  
Symptoms:If service calls are not working for the Machine Translation Service, no jobs can be submitted to the application server for immediate processing or submission to the Job Queue. That is, the service is inaccessible and does not function.
  
### Cause

One or more of the following might be the cause:
  
- The specified SharePoint Server application server is inaccessible.
    
- The specified application server is responding slowly because of heavy network activity or load on the specific server.
    
### Resolution

Resolution 1: Check the error logs:
  
- Open the Windows Event Viewer.
    
- Search for event ID 8049 in the Windows. Application Event log.
    
- In the event description, note the application server that is failing
    
Resolution 2: Verify the application server connection:
  
- From the failing application server, open the SharePoint Central Administration Web site.
    
- If you cannot access the Central Administration site from the failing server, check that the network settings are correct and that the server has appropriate permissions to join the SharePoint farm.
    
Resolution 3: Verify that the Machine Translation Service runs on the failing server:
  
1. On the **Central Administration** website, in the reading pane, in the **System Settings** section, click **Manage servers in this farm**.
    
2. Verify that the Machine Translation Service runs on the failing application server.
    
3. If there is a service application proxy for the failing service application, create a new service application.
    
Resolution 4: Restart the Machine Translation Service:
  
1. On the **Central Administration** website, in the reading pane, in the **System Settings** section, click **Manage servers in this farm**.
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate the **Machine Translation Service**, click **Stop**, and then click **Start**.
    
Resolution 5: Create a new Machine Translation Service application:
  
1. On the **Central Administration** website, in the reading pane, in the **Application Management** section, click **Manage service applications**.
    
2. In the **Type** column, click the name of the Machine Translation Service application that has the failing service instance. 
    
3. On the ribbon, click **Delete**.
    
4. In the **Delete Service Application** dialog box, click **OK**.
    
5. Create a new Machine Translation Service application.
    
## Machine Translation Service: Content not accessible
<a name="TransContent"> </a>

 **Alert Name:**Machine Translation Service: Content not accessible
  
 **Summary:** Critical state of this Monitor indicates that back-end to front-end CSOM calls are failing. 
  
Symptoms: No files can be retrieved for processing and items that are already being processed will not be written. That is, files are inaccessible and items will continuously fail.
  
### Cause

One or more of the following might be the cause:
  
- Server to server Authentication is configured incorrectly.
    
- The content database is not responsive enough because of activity on the network or physical SQL server.
    
- Permissions to access the content database are no longer valid.
    
- The content database is inaccessible.
    
### Resolution

Resolution 1: Verify the status of the SQL Server content database:
  
1. On the SharePoint Central Administration website, in the **System Settings** section from the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the content database server, and the name and the version of the configuration database. 
    
3. Start SQL Server Management Studio and connect to the content database server.
    
4. If the content database does not exist, run the SharePoint Products and Technologies Configuration Wizard.
    
Resolution 2: Verify the SQL Server network connection:
  
1. On the Central Administration website, in the **System Settings** section, from the reading pane, click **Manage Servers in this farm**.
    
2. In the **Farm Information** section, note the content database server and the name and the version of the content database information. 
    
3. Open a Command Prompt window and type ping to confirm the server connection.
    
    Failure to contact the server indicates a problem with the network connection or another problem that prevents a response from the server.
    
4. Log on to the server and troubleshoot the issue.
    
Resolution 3: Verify Server to Server Authentication is configured correctly:
  
See [Configure server-to-server authentication in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server).
  
## Machine Translation Service: Worker failure
<a name="TransWorker"> </a>

 **Alert Name:**Machine Translation Service: Worker failure
  
 **Summary:** A critical state of this Monitor indicates that the Machine Translation Service worker processes are failing. 
  
Symptoms:These errors have to be monitored so end-users are not seeing all the items fail over a certain span of time.
  
### Cause

One or more of the following might be the cause:
  
- Corrupt input file
    
- Translation worker crash
    
- Error of saving the file to the local store
    
### Resolution

Resolution 1: Check the error logs:
  
1. Open the Windows Event Viewer.
    
2. Search for event ID 8049 in the Windows Application Event log.
    
3. In the event description, note the application server that is failing.
    
Resolution 2: Verify the application server connection:
  
1. From the failing application server, open the **SharePoint Central Administration** website. 
    
2. If you cannot access the Central Administration website from the failing server, check that the network settings are correct and that the server has appropriate permissions to join the SharePoint farm.
    
Resolution 3: Verify that the Machine Translation Service runs on the failing server:
  
1. On the **Central Administration** website, in the reading pane, in the **System Settings** section, click **Manage servers in this farm**.
    
2. Verify that the Machine Translation Service runs on the failing application server.
    
3. If there is a service application proxy for the failing service application, create a new service application.
    
Resolution 4: Restart the Machine Translation Service:
  
1. On the **Central Administration** website, in the reading pane, in the **System Settings** section, click **Manage servers in this farm**.
    
2. In the **Server** column, click the name of the failing application server. The **Services on Server** page opens. 
    
3. In the **Service** column, locate the **Machine Translation Service**, click **Stop**, and then click **Start**.
    
Resolution 5: Create a new Machine Translation Service application
  
1. On the Central Administration website, from the reading pane, in the Application Management section, from the reading pane, click Manage service applications.
    
2. In the **Type** column, click the name of the Machine Translation Service application that has the failing service instance. 
    
3. On the ribbon, click **Delete**.
    
4. In the **Delete Service Application** dialog box, click OK. 
    
5. Create a new Machine Translation Service application.
    
## See also
<a name="TransWorker"> </a>

#### Concepts

[Plan for monitoring in SharePoint Server](../administration/monitoring-planning.md)
  
#### Other Resources

[System Center Monitoring Pack for SharePoint Foundation](http://go.microsoft.com/fwlink/p/?LinkId=272567)
  
[System Center Monitoring Pack for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=272568)
  
[System Center Monitoring Pack for SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkID=746863&amp;clcid=0x409)

