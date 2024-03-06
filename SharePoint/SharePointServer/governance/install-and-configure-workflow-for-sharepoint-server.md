---
title: "Install and configure workflow for SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: serdars
ms.date: 3/14/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: b37c1d36-5bfe-4f76-bb03-2c5436c043a2

description: "Learn how to install and configure workflow in SharePoint Server."
---

# Install and configure workflow for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
This article contains the information and procedures required to configure SharePoint Workflow Manager (SPWFM) for SharePoint Server.

> [!NOTE]
>There are two separate workflow engine products that power the SharePoint 2013 Workflow platform: Microsoft Workflow Manager ("Classic WFM") and SharePoint Workflow Manager (SPWFM). Microsoft Workflow Manager is no longer available to be installed, whereas SharePoint Workflow Manager has been released to replace it. Hence, the instructions outlined in this document explain how to install SharePoint Workflow Manager.
  
 
## Overview
<a name="section1"> </a>

A new option exists when you build a workflow for SharePoint Server. This option is called **Platform Type**. The figure shows the **Platform Type** option when you're creating a new workflow by using SharePoint Designer 2013. 
  
**Figure: SharePoint Server includes three workflow platform options.**

![Three workflow platforms in SharePoint 2013.](../media/WF15-WorkflowInstall1.png)
  
The only platform available when you first install SharePoint Server is the SharePoint 2010 Workflow platform. The SharePoint 2013 Workflow platform and the Project Server platform require more steps. The three workflow platforms are outlined in the following table.
  
**Workflow Platform types available in SharePoint Server**

|**Platform Type**|**Platform Framework**|**Requirements**|
|:-----|:-----|:-----|
|**SharePoint 2010 Workflow** <br/> |Windows Workflow Foundation 3  <br/> |Installs automatically with SharePoint Server.  <br/> |
|**SharePoint 2013 Workflow** <br/> |Windows Workflow Foundation 4  <br/> |Requires SharePoint Workflow Manager or Microsoft Workflow Manager, and SharePoint Server.  <br/> |
|**SharePoint 2013 Workflow - Project Server** <br/> |Windows Workflow Foundation 4  <br/> |Requires SharePoint Workflow Manager or Microsoft Workflow Manager, and Project server.  <br/> |

> [!NOTE]
> SharePoint Workflow Manager must be downloaded and installed separately from SharePoint Server. It does not install automatically when you install SharePoint Server.

## New installation of SharePoint Workflow Manager

SharePoint Workflow Manager may be installed on the same servers as SharePoint or on separate, dedicated servers.  It's recommended that SharePoint Workflow Manager is installed on its own dedicated servers for performance and reliability reasons. 

> [!NOTE]
> SharePoint Workflow Manager is supported in farms having an odd number of hosts, for example, 1, 3, or 5.  A farm with 2 or 4 SharePoint Workflow Manager hosts is not supported.
   
### Prerequisites

SharePoint Workflow Manager requires the server role of Web Server (IIS). If you're installing SharePoint Workflow Manager on a server without the IIS server role installed, the Workflow Manager Configuration Wizard fails with a message like *Could not load file or assembly 'Microsoft.Web.Administration'*. In addition to the features that are installed by default, SharePoint Workflow Manager requires the following IIS features:

- Windows Authentication (under Security)
- .NET Extensibility 4.7 (under Application Development)
- ASP.NET 4.7 (under Application Development)

> [!NOTE] 
> SharePoint Workflow Manager might not be installed and configured correctly with only RODC (read-only domain controller) provided in the network environment, as it requires RWDC (read/write DC, full DC).

SharePoint Workflow Manager requires Azure Service Fabric, which must be installed before you run SharePoint Workflow Manager setup. If the Azure Service Fabric Runtime isn't already installed, follow these steps below to install it:

1. The minimum version of Azure Service Fabric Runtime supported by SharePoint Workflow Manager is 9.1.1583.9590, and you can download it from [Azure Service Fabric Runtime](https://download.microsoft.com/download/b/8/a/b8a2fb98-0ec1-41e5-be98-9d8b5abf7856/MicrosoftServiceFabric.9.1.1583.9590.exe). Or you can find and download any higher version of its Windows Installer from [here](/azure/service-fabric/service-fabric-get-started#install-the-sdk-and-tools).

2. Open a PowerShell console as an elevated administrator and run the following command:

    `.\MicrosoftServiceFabric.9.1.1583.9590.exe /accepteula`

3. To verify the Azure Service Fabric is installed, you should be able to find it in the Programs and Features of the Control Panel.

> [!NOTE]
> SharePoint Workflow Manager supports the version 9.1 CU2 (9.1.1583.9590) of Azure Service Fabric and [higher versions](/azure/service-fabric/service-fabric-versions). If **Windows Fabric** is already installed on your machine, you must uninstall it before installing Azure Service Fabric.
>  
> It’s been reported that Azure Service Fabric might generate a large number of logs, reducing the disk space.  This can occur regardless of the SharePoint Workflow Manager workload.  You can identify this issue by looking at the files generated in the `%ProgramData%\Microsoft Service Fabric\Log\Traces` directory.  You can't control the log size through the [cluster configuration](/azure/service-fabric/service-fabric-cluster-fabric-settings#diagnostics), with only Azure Service Fabric Runtime installed. You might need to delete expired logs manually, or for example, create a periodic task through the Windows Task Scheduler to do it.

### Install SharePoint Workflow Manager

SharePoint Workflow Manager and SharePoint Workflow Manager Client can be downloaded from [here](https://www.microsoft.com/download/details.aspx?id=104867).  The system requirements can be found on that page as well.

Install both SharePoint Workflow Manager and SharePoint Workflow Manager Client on all servers in the Workflow Manager farm. Install only the SharePoint Workflow Manager Client on all servers in the SharePoint Server farm.

> [!NOTE]
> Though it is supported to install SharePoint Workflow Manager on servers running SharePoint Server, it is recommended that SharePoint Workflow Manager is installed on its own dedicated servers for performance and reliability reasons.


### Configure App Management and Subscriptions Settings services
The App Management and Subscription Settings services are required in the SharePoint farm for SharePoint 2013-platform workflows to function.
On the SharePoint server, set up App Management and Subscription Settings service, service application and service application proxy, if not already set up in the farm. 

The App Managment service can be created using Central Administration.

You can use PowerShell to create a Subscription Settings Service application:

```powershell
$sa = New-SPSubscriptionSettingsServiceApplication -ApplicationPool 'SharePoint Web Services Default' -Name 'Subscriptions Settings Service Application' -DatabaseName 'Subscription'

New-SPSubscriptionSettingsServiceApplicationProxy -ServiceApplication $sa
```

### Configure SharePoint Workflow Manager farm

To create a SharePoint Workflow Manager farm and join your servers to the farm, you can configure SharePoint Workflow Manager through the Workflow Manager Configuration Wizard.

Logon to the SharePoint Workflow Manager server, click on “Workflow Manager Configuration” and click on “Configure Workflow Manager with Default settings” or “Configure Workflow Manager with Custom Settings”, depending on the requirements.

In this example, we will use the Default settings.

> [!NOTE] 
> If you want to use different ports, custom certificates, or custom database names, you'll want to use the "Configure Workflow Manager with Custom Settings" option.

Provide the necessary SQL and service account details in the workflow wizard.  

> [!NOTE] 
>  By default, only HTTPS (TLS / SSL) port 12290 is configured for the Workflow Management site.  If you'd like to also allow communication over unencrypted HTTP port 12291, you must select the "Allow Workflow Management over HTTP on this computer" check box.

If you are creating a multi-server SharePoint Workflow Manager farm, you must run the workflow configuration wizard on the other nodes and join the existing farm.


### Configure SharePoint Workflow Manager to work with the SharePoint Server farm
<a name="section5"> </a>

Consider the following key factors before configuring SharePoint Workflow Manager to work with SharePoint Server.
    
- Will communication between SharePoint Workflow Manager and SharePoint Server use **HTTP** or **HTTPS** ? 
    
> [!NOTE]
> For security reasons, we recommend HTTPS for a production environment. 
  

**To configure SharePoint Workflow Manager on a server that is NOT part of the SharePoint Server farm and on which communication takes place by using HTTP**
  
1. Sign-in to each server in the SharePoint Server farm.
    
2. Install the SharePoint Workflow Manager Client on each server in the SharePoint farm.
    
    Before you can run the workflow pairing cmdlet, you must install SharePoint Workflow Manager Client on each of the servers in the SharePoint farm.
    
3. Open the SharePoint Management Shell as an administrator by right-clicking the **SharePoint Management Shell** command and choosing **Run as administrator**.
    
4. Run the **Register-SPWorkflowService** cmdlet. The cmdlet should be run only once and can be run from any of the servers in the SharePoint farm. 
    
   **Example**:
    
   ```powershell
   Register-SPWorkflowService -SPSite "http://myserver/mysitecollection" -WorkflowHostUri "http://workflow.example.com:12291" -AllowOAuthHttp
   ```

> [!IMPORTANT]
> You must install the SharePoint Workflow Manager Client on each server in the SharePoint farm before you run the pairing cmdlet. 
  
**To configure SharePoint Workflow Manager on a server that is NOT part of the SharePoint Server farm and on which communication takes place by using HTTPS**
  
1. Determine whether you need to install SharePoint Workflow Manager certificates in SharePoint Server.
    
    Under some circumstances, you have to obtain and install SharePoint Workflow Manager certificates. If your installation requires that you obtain and install these certificates, you must complete that step before continuing. To learn whether you need to install certificates, and for instructions, see [Install Workflow Manager certificates in SharePoint Server](install-workflow-manager-certificates-in-sharepoint-server.md).
    
2. Sign-in to each server in the SharePoint Server farm.
    
3. Install the SharePoint Workflow Manager Client on each server in the SharePoint farm.
    
    Before you can run the workflow pairing cmdlet, you must install SharePoint Workflow Manager Client on each of the servers in the SharePoint farm.
    
4. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint Management Shell** command and choosing **Run as administrator**.
    
5. Run the **Register-SPWorkflowService** cmdlet. 
    
   **Example**:
    
   ```powershell
   Register-SPWorkflowService -SPSite "https://myserver/mysitecollection" -WorkflowHostUri "https://workflow.example.com:12290"
   ```

> [!IMPORTANT]
> You must install the SharePoint Workflow Manager Client on each server in the SharePoint farm before you run the Register-SPWorkflowService cmdlet. 

## Upgrade existing Microsoft Workflow Manager

In order to update Microsoft Workflow Manager (Classic WFM) to SharePoint Workflow Manager (SPWFM), SharePoint Workflow Manager can't be placed on top of Microsoft Workflow Manager. Installing this build requires first uninstalling any prior versions of Workflow Manager, Workflow Manager Client, and Service Bus.

You can upgrade to SharePoint Workflow Manager from any version of Microsoft Workflow Manager. 

Follow the steps below to uninstall Microsoft Workflow Manager and install SharePoint Workflow Manager:

1. Open Workflow Manager Configuration Wizard.
2. Select **Leave Workflow Manager Farm**.
3. Confirm the subsequent steps until the end.
   > [!NOTE]
   >Each database used by Workflow Manager and Service Bus will need to be specified when rejoining the farm with SharePoint Workflow Manager. For example, the SQL Server instance and database name for the Workflow Manager farm management database and the Service Bus farm management database.

4. Uninstall Microsoft Workflow Manager, Workflow Manager Client, Service Bus for Windows Server, and Windows Fabric if they're installed. You can uninstall them from the Control Panel. If Windows Fabric is installed, ensure you install Azure Service Fabric after uninstalling Windows Fabric.
5. If the folder *%ProgramFiles%\Workflow Manager\1.0* already exists, you must manually remove it for the next steps to succeed.
6. Install SharePoint Workflow Manager and SharePoint Workflow Manager Client.
7. If there's more than one server in your Workflow Manager farm, repeat the previous steps on all farm servers.
8. Run the Workflow Manager Configuration Wizard and rejoin the previous farm with the databases you noted in the previous steps on all servers in your Workflow Manager farm.
   > [!NOTE]
   >There is no need to delete the existing Workflow Service Application Proxy, and there is no need to re-register SPWorkflowService. If you encounter the invalidity of the Certificate Generation Key for SharePoint Workflow Manager and Service Bus, you may reset it, see [Reset Certificate Generation Key](/SharePoint/governance/reset-certificate-generation-key-sharepoint-workflow-manager).

9. Rerun the Workflow Manager Configuration Wizard, select **Upgrade Workflow Manager Farm**, and confirm subsequent steps until the end.
   > [!NOTE]
   > This step should be run on all servers in the SharePoint Workflow Manager farm.
   > The "Upgrade Workflow Manager Farm" option is always presented in the Workflow Manager Configuration Wizard, whether an upgrade is required or not.  There's no harm in running it multiple times.

10. Install SharePoint Workflow Management Client on each server in the SharePoint Server farm after uninstalling any previous versions.

## Validate the installation
<a name="section6"> </a>

Follow these steps to validate that you have successfully installed and configured the required components.
  
 **To validate the installation**
  
1. Add a user to your SharePoint site, and grant the user Site Designer permissions.   
2. Install SharePoint Designer 2013 and create a workflow based on the SharePoint 2013 Workflow platform. For more information, see [Creating a workflow by using SharePoint Designer 2013 and the SharePoint 2013 Workflow platform](/sharepoint/dev/general-development/creating-a-workflow-by-using-sharepoint-designer-and-the-sharepoint-wo).    
3. Run this workflow from the SharePoint user interface.
    
## Troubleshooting
<a name="section7"> </a>

For security reasons, the Setup account can't be used to create a workflow based on the SharePoint 2013 Workflow platform. If you try to create a workflow based on the SharePoint 2013 Workflow platform by using SharePoint Designer 2013, you receive a warning that the list of workflow actions don't exist, and the workflow isn't created.
  
The user who deploys and runs a workflow must be added to the User Profile service. Check the User Profile service application page in Central Administration to confirm that the user you're using to validate workflow installation is in the User Profile service.
  
You can determine which ports SharePoint Server and Workflow Manager are using for both HTTP and HTTPS by using IIS Manager as shown in the figure.
  
**Figure: Use IIS Manager to view the ports used by SharePoint Workflow Manager**

![View ports in IIS Manager.](../media/WF15-.png)
  
Sharepoint Workflow Manager communicates by using TCP/IP or Named Pipes. Ensure that the appropriate communication protocol is enabled on the SQL Server instance that hosts the SharePoint Workflow Manager databases.
  
The SQL Browser Service must be running on the SQL Server instance that hosts the Workflow Manager databases.
  
The System Account can't be used to develop a workflow.
  
To troubleshoot SharePoint Server, see [Troubleshooting SharePoint Server](../administration/troubleshoot.md).
