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
  
This article contains the information and procedures required to configure Workflow Manager in SharePoint Server.

> [!NOTE]
>There are two separate workflow engine products that power the SharePoint 2013 Workflow platform: Microsoft Workflow Manager and SharePoint Workflow Manager. Microsoft Workflow Manager is no longer available to be installed, whereas SharePoint Workflow Manager has been released to replace it. Hence, the instructions outlined in this document explain how to install SharePoint Workflow Manager.
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server. The SharePoint 2013 Workflow platform is not supported in SharePoint Foundation 2013. 
  
> [!NOTE]
> You can watch a video series that walks through the process of installing and configuring the SharePoint 2013 Workflow platform. To view the videos, see [Video series: Install and configure Workflow in SharePoint Server 2013](video-series-install-and-configure-workflow-in-sharepoint-server-2013.md).

Learn about [Workflows for SharePoint in Microsoft 365](../../SharePointOnline/extend-and-develop.md).
## Overview
<a name="section1"> </a>

A new option exists when you build a workflow for SharePoint Server. This option is called **Platform Type**. The figure shows the **Platform Type** option when you are creating a new workflow by using SharePoint Designer 2013. 
  
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
> Workflow Manager must be downloaded and installed separately from SharePoint Server. It does not install automatically when you install SharePoint Server.

## New installation of SharePoint Workflow Manager

SharePoint Workflow Manager may be installed on the same servers as SharePoint or on separate, dedicated servers. 
   
### Prerequisites

SharePoint Workflow Manager requires the server role of Web Server (IIS). If you are installing SharePoint Workflow Manager on a server without the IIS server role installed, the Workflow Manager Configuration Wizard will fail with messages like *Could not load file or assembly 'Microsoft.Web.Administration'*.

SharePoint Workflow Manager requires Azure Service Fabric, which must be installed before you run SharePoint Workflow Manager setup. If the Azure Service Fabric Runtime is not already installed, follow these steps below to install it:

1. The minimum version of Azure Service Fabric Runtime supported by SharePoint Workflow Manager is 9.1.1583.9590, and you can download it from [Azure Service Fabric Runtime](https://download.microsoft.com/download/b/8/a/b8a2fb98-0ec1-41e5-be98-9d8b5abf7856/MicrosoftServiceFabric.9.1.1583.9590.exe). Or you can find and download any higher version of its Windows Installer from [here](/azure/service-fabric/service-fabric-get-started#install-the-sdk-and-tools).

2. Open a PowerShell console as an elevated administrator and run the following command:

    `.\MicrosoftServiceFabric.9.1.1583.9590.exe /accepteula`

3. To verify the Azure Service Fabric is installed, you should be able to find it in the Programs and Features of the Control Panel.

> [!NOTE]
>SharePoint Workflow Manager supports the version 9.1 CU2 (9.1.1583.9590) of Azure Service Fabric and [higher versions](/azure/service-fabric/service-fabric-versions).  If you want to directly upgrade your Azure Service Fabric without uninstallation, note that there are [upgrade dependencies](/azure/service-fabric/service-fabric-versions). If **Windows Fabric** is already installed on your machine, you must uninstall it before installing Azure Service Fabric.

### Install SharePoint Workflow Manager

SharePoint Workflow Manager and SharePoint Workflow Manager Client can be downloaded from [here](https://www.microsoft.com/download/details.aspx?id=104867).
Install both SharePoint Workflow Manager and SharePoint Workflow Manager Client on all servers in the Workflow Manager farm.
Install only the SharePoint Workflow Manager Client on all servers in the SharePoint Server farm.

### Configure Workflow Manager farm and SharePoint Workflow Manager

To create a Workflow Manager farm and join your servers to the farm, you can configure SharePoint Workflow Manager through the Workflow Manager Configuration Wizard, see [Video series Install and configure Workflow](/SharePoint/governance/video-series-install-and-configure-workflow-in-sharepoint-server-2013#episode-3-install-and-configure-workflow-manager).

> [!NOTE]
> The SharePoint 2010 Workflow platform installs automatically when you install SharePoint Server. The SharePoint 2013 Workflow platform requires either Microsoft Workflow Manager or SharePoint Workflow Manager and must be installed separately and then configured to work with your SharePoint Server farm. To function correctly SharePoint 2013 Workflows require that the App Management Service and Site Subscription Service are provisioned. It is not required to set up a wildcard certificate and DNS registration but both instances need to be running. 

### Configure SharePoint Workflow Manager to work with the SharePoint Server farm
<a name="section5"> </a>

Consider the following two key factors before configuring SharePoint Workflow Manager to work with SharePoint Server.
  
- Is SharePoint Workflow Manager installed on a server that is part of the SharePoint farm?
    
- Will communication between SharePoint Workflow Manager and SharePoint Server use **HTTP** or **HTTPS** ? 
    
These factors translate into four scenarios. Each scenario configures a SharePoint Server farm to communicate and function with the SharePoint Workflow Manager farm. Follow the scenario that matches your circumstance.
  
|Scenario Number and Description|Scenario Number and Description|
|:-----|:-----|
|1: SharePoint Workflow Manager is installed on a server that is part of the SharePoint Server farm. Communication takes place by using HTTP.  <br/> |2: SharePoint Workflow Manager is installed on a server that is part of the SharePoint Server farm. Communication takes place by using HTTPS.  <br/> |
|3: SharePoint Workflow Manager is installed on a server that is NOT part of the SharePoint Server farm. Communication takes place by using HTTP.  <br/> |4: SharePoint Workflow Manager is installed on a server that is NOT part of the SharePoint Server farm. Communication takes place by using HTTPS.  <br/> |
   
> [!NOTE]
> For security reasons, we recommend HTTPS for a production environment. 
  
  
**To configure SharePoint Workflow Manager on a server that is part of the SharePoint Server farm and on which communication takes place by using HTTP**
  
1. Sign-in to the computer in the SharePoint Server farm where SharePoint Workflow Manager was installed.
    
2. Open the SharePoint Management Shell as an administrator by right-clicking the **SharePoint Management Shell** and choosing **Run as administrator**.
    
3. Run the **Register-SPWorkflowService** cmdlet. 
    
   **Example**:
    
   ```powershell
   Register-SPWorkflowService -SPSite "http://myserver/mysitecollection" -WorkflowHostUri "http://workflow.example.com:12291" -AllowOAuthHttp
   ```

4. Sign-in to each server in the SharePoint Server farm.
    
    Each server in the SharePoint Server farm must have the Workflow Manager Client installed.
    
    > [!NOTE]
    > When you install Workflow Manager on a server it automatically installs the Workflow Manager Client on that server. You will still need to install the Workflow Manager Client on any additional servers. For example, if you have a farm that contains five servers and you install SharePoint Workflow Manager on one of those servers you will still need to install the Workflow Manager Client on the four additional servers. 
  
5. Install the SharePoint Workflow Manager Client on each server in the SharePoint farm.
       
**To configure SharePoint Workflow Manager on a server that is part of the SharePoint Server farm and on which communication takes place by using HTTPS**
  
1. Determine if you need to install SharePoint Workflow Manager certificates in SharePoint.
    
    Under some circumstances, you have to obtain and install SharePoint Workflow Manager certificates. If your installation requires that you obtain and install these certificates, you must complete that step before continuing. To learn whether you need to install certificates, and for instructions, see [Install Workflow Manager certificates in SharePoint Server](install-workflow-manager-certificates-in-sharepoint-server.md).
    
2. Sign-in to the computer in the SharePoint Server farm where SharePoint Workflow Manager was installed.
    
3. Open the SharePoint Management Shell as an administrator by right-clicking the **SharePoint Management Shell** and choosing **Run as administrator**.
    
4. Run the **Register-SPWorkflowService** cmdlet. 
    
   **Example**:
    
   ```powershell
   Register-SPWorkflowService -SPSite "https://myserver/mysitecollection" -WorkflowHostUri "https://workflow.example.com:12290"
   ```

5. Sign-in to each server in the SharePoint Server farm.
    
    Each server in the SharePoint Server farm must have the Workflow Manager Client installed.
    
    > [!NOTE]
    > When you install SharePoint Workflow Manager on a server it automatically installs the Workflow Manager Client on that server. You will still have to install the SharePoint Workflow Manager Client on any additional servers. For example, if you have a farm that contains five servers and you install Workflow Manager on one of those servers you will still need to install the Workflow Manager Client on the four additional servers. 
  
6. Install the SharePoint Workflow Manager Client on each server in the SharePoint farm.
    
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
> You must install the SharePoint Workflow Manager Client on each server in the SharePoint farm before you run the pairing cmdlet. 

## Upgrade existing Microsoft Workflow Manager

In order to update Microsoft Workflow Manager to SharePoint Workflow Manager, SharePoint Workflow Manager cannot be placed on top of Microsoft Workflow Manager. Installing this build requires first uninstalling any prior versions of Workflow Manager (Client) and Service Bus.

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
7. If there is more than one server in your Workflow Manager farm, repeat the previous steps on all farm servers.
8. Run the Workflow Manager Configuration Wizard and rejoin the previous farm with the databases you noted in the previous steps on all servers in your Workflow Manager farm.
   > [!NOTE]
   >There is no need to delete the existing Workflow Service Application Proxy, and there is no need to re-register SPWorkflowService. If you encounter the invalidity of the Certificate Generation Key for SharePoint Workflow Manager and Service Bus, you may reset it, see [Reset Certificate Generation Key](https://joshroark.com/sharepoint-workflow-manager-rest-the-certificate-generation-key/).

9. Rerun the Workflow Manager Configuration Wizard, select **Upgrade Workflow Manager Farm**, and confirm subsequent steps until the end.
   > [!NOTE]
   >You only need to run this step once on any server in the Workflow Manager farm.

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

For security reasons, the Setup account cannot be used to create a workflow based on the SharePoint 2013 Workflow platform. If you try to create a workflow based on the SharePoint 2013 Workflow platform by using SharePoint Designer 2013, you receive a warning that the list of workflow actions do not exist, and the workflow is not created.
  
The user who deploys and runs a workflow must be added to the User Profile service. Check the User Profile service application page in Central Administration to confirm that the user you are using to validate workflow installation is in the User Profile service.
  
You can determine which ports SharePoint Server and Workflow Manager are using for both HTTP and HTTPS by using IIS Manager as shown in the figure.
  
**Figure: Use IIS Manager to view the ports used by SharePoint Workflow Manager**

![View ports in IIS Manager.](../media/WF15-.png)
  
Sharepoint Workflow Manager communicates by using TCP/IP or Named Pipes. Ensure that the appropriate communication protocol is enabled on the SQL Server instance that hosts the SharePoint Workflow Manager databases.
  
The SQL Browser Service must be running on the SQL Server instance that hosts the Workflow Manager databases.
  
The System Account cannot be used to develop a workflow.
  
To troubleshoot SharePoint Server, see [Troubleshooting SharePoint Server](../administration/troubleshoot.md).
