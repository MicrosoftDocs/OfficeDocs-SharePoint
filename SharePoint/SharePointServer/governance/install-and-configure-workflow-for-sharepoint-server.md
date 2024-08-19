---
title: "Install and configure workflow for SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: serdars
ms.date: 4/22/2024
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

SharePoint Workflow Manager requires the server role of Web Server (IIS). If you're installing SharePoint Workflow Manager on a server without the IIS server role installed, the Workflow Manager Configuration Wizard fails with a message like *Could not load file or assembly 'Microsoft.Web.Administration'*. In addition to the features that are installed by default with the Web Server role, SharePoint Workflow Manager requires the following Web Server features:

- Windows Authentication (under Security)
- .NET Extensibility 4.7 (under Application Development)
- ASP.NET 4.7 (under Application Development)

:::image type="content" source="media/install-and-configure-workflow-for-sharepoint-server/iis-features-required.png" alt-text="A screenshot of the Web Server features that are required for SharePoint Workflow Manager.":::
> [!NOTE]
> SharePoint Workflow Manager may not be installed and configured correctly with only RODCs (read-only domain controllers) available in the network environment.  It requires a RWDC (read/write domain controller).
SharePoint Workflow Manager requires Azure Service Fabric, which must be installed before you run SharePoint Workflow Manager setup. If the Azure Service Fabric Runtime isn't already installed, follow these steps below to install it:

1. The minimum version of Azure Service Fabric Runtime supported by SharePoint Workflow Manager is 9.1.1583.9590, and you can download it from [Azure Service Fabric Runtime](https://download.microsoft.com/download/b/8/a/b8a2fb98-0ec1-41e5-be98-9d8b5abf7856/MicrosoftServiceFabric.9.1.1583.9590.exe). Or you can find and download any higher version of its Windows Installer from [here](/azure/service-fabric/service-fabric-get-started#install-the-sdk-and-tools).

2. Open a PowerShell console as an elevated administrator and run the following command:

    `.\MicrosoftServiceFabric.9.1.1583.9590.exe /accepteula`

3. To verify the Azure Service Fabric is installed, you should be able to find it in the Programs and Features of the Control Panel.
> [!NOTE]
> SharePoint Workflow Manager supports the version 9.1 CU2 (9.1.1583.9590) of Azure Service Fabric and [higher versions](/azure/service-fabric/service-fabric-versions). 
> 
> If **Windows Fabric** is already installed on your machine, you must uninstall it before installing Azure Service Fabric.
> 
> It’s been reported that Azure Service Fabric might generate a large number of logs, reducing the disk space.  This can occur regardless of the SharePoint Workflow Manager workload.  You can identify this issue by looking at the files generated in the `%ProgramData%\Microsoft Service Fabric\Log\Traces` directory.  You can't control the log size through the [cluster configuration](/azure/service-fabric/service-fabric-cluster-fabric-settings#diagnostics), with only Azure Service Fabric Runtime installed. You might need to delete expired logs manually, or for example, create a periodic task through the Windows Task Scheduler to do it.
### Install SharePoint Workflow Manager

SharePoint Workflow Manager and SharePoint Workflow Manager Client can be downloaded from [here](https://www.microsoft.com/download/details.aspx?id=104867).  The system requirements can be found on that page as well.

Install **both** SharePoint Workflow Manager and SharePoint Workflow Manager Client on all servers in the **Workflow Manager** farm. 

Install **only** the SharePoint Workflow Manager **Client** on all servers in the **SharePoint Server** farm.
> [!NOTE]
> Though it is supported to install SharePoint Workflow Manager on servers running SharePoint Server, it is recommended that SharePoint Workflow Manager is installed on its own dedicated servers for performance and reliability reasons.

### Configure SharePoint Workflow Manager farm

To create a SharePoint Workflow Manager farm and join your servers to the farm, you can configure SharePoint Workflow Manager through the Workflow Manager Configuration Wizard.

Logon to the SharePoint Workflow Manager server, click on “Workflow Manager Configuration” and click on “Configure Workflow Manager with Default settings” or “Configure Workflow Manager with Custom Settings”, depending on the requirements. If you want to use different ports, custom certificates, or custom database names, you'll want to use the "Configure Workflow Manager with Custom Settings" option.

In this example, we will use the Default Settings option.

:::image type="content" source="media/install-and-configure-workflow-for-sharepoint-server/configure-with-default-settings.png" alt-text="A screenshot showing the Configure Workflow Manager with Default settings selection in the SharePoint Workflow Manager configuration wizard.":::  
> [!NOTE]
>  By default, only HTTPS (TLS / SSL) port 12290 is configured for the Workflow Management site.  If you'd like to also allow communication over unencrypted HTTP port 12291, you must select the "Allow Workflow Management over HTTP on this computer" check box.  This is a factor when running the Register-SPWorkflowService cmdlet later.
Provide the necessary SQL Server and service account details in the workflow wizard.  

:::image type="content" source="media/install-and-configure-workflow-for-sharepoint-server/configuration-wizard-details.png" alt-text="A screenshot showing the configuration options in the SharePoint Workflow Manager configuration wizard.":::

The configuration wizard will provide a summary of your choices before they are committed.  

:::image type="content" source="media/install-and-configure-workflow-for-sharepoint-server/configuration-wizard-summary.png" alt-text="A screenshot showing the summary page of the SharePoint Workflow Manager configuration wizard.":::  
> [!NOTE]
> Some of the values are selected for you when you use the “Configure Workflow Manager with Default settings” option.  If they are not correct for your environment, you may have to start the wizard over and choose “Configure Workflow Manager with Custom Settings”.

The configuration wizard should complete successfully.  If it fails, please select the "View Log" link, find the problem and correct it before running the wizard again.

:::image type="content" source="media/install-and-configure-workflow-for-sharepoint-server/configuration-wizard-completed.png" alt-text="A screenshot showing the SharePoint Workflow Manager configuration wizard completing successfully.":::

If you are creating a multi-server SharePoint Workflow Manager farm, you must run the workflow configuration wizard on the other nodes and chose the "Join an Existing Workflow Manager Farm" option.


### Configure App Management and Subscriptions Settings services in the SharePoint farm
The App Management and Subscription Settings services are required in the SharePoint farm for SharePoint 2013-platform workflows to function.
If not already set up in the SharePoint farm, on the SharePoint server, set up App Management and Subscription Settings services, service applications and service application proxies. 

The App Managment service can be created using Central Administration.

You can use PowerShell to create a Subscription Settings Service application:

```powershell
$sa = New-SPSubscriptionSettingsServiceApplication -ApplicationPool 'SharePoint Web Services Default' -Name 'Subscriptions Settings Service Application' -DatabaseName 'Subscription'

New-SPSubscriptionSettingsServiceApplicationProxy -ServiceApplication $sa
```

### Configure SharePoint Workflow Manager to work with the SharePoint Server farm
<a name="section5"> </a>

Consider the following key factors before configuring SharePoint Workflow Manager to work with SharePoint Server.
    
- Will communication between SharePoint Workflow Manager and SharePoint Server use **HTTP** or **HTTPS** ?   
> [!NOTE]
> For security reasons, we recommend HTTPS for a production environment. 
  
**To configure SharePoint Workflow Manager in an environment where communication takes place using HTTP**  
> [!NOTE]
>  By default, only HTTPS (TLS / SSL) port 12290 is configured for the Workflow Management site. In order to configure the use of HTTP, the "Allow Workflow Management over HTTP on this computer" check box should have been selected when running the “Workflow Manager Configuration” wizard in an earlier step.

1. Sign-in to each server in the SharePoint Server farm.

1. Install the SharePoint Workflow Manager **Client** on each server in the SharePoint farm.  
   > [!IMPORTANT]
   > You must install the SharePoint Workflow Manager Client on each server in the SharePoint farm before you run the Register-SPWorkflowService cmdlet. 
    
3. On one SharePoint server, open the SharePoint Management Shell as an administrator by right-clicking the **SharePoint Management Shell** command and choosing **Run as administrator**.
    
1. Run the **Register-SPWorkflowService** cmdlet to connect the SharePoint farm with the SharePoint Workflow Manager farm. The cmdlet should be run only once and can be run from any of the servers in the SharePoint farm.   
   > [!NOTE] 
   > The value for the -SPSite parameter can be any valid site collection within the SharePoint farm.
   > The correct value for the -WorkflowHostUri parameter can be found by running PowerShell `Get-WFFarm | select endpoints` on the SharePoint Workflow Manager server.

   **Example**:
   ```powershell
   Register-SPWorkflowService -SPSite "http://myserver/mysitecollection" -WorkflowHostUri "http://workflow.example.com:12291" -AllowOAuthHttp
   ```

**To configure SharePoint Workflow Manager in an environment where communication takes place using HTTPS**
  
1. Determine whether you need to install SharePoint Workflow Manager certificates on the SharePoint servers.
    
    Under some circumstances, you must obtain and install SharePoint Workflow Manager certificates. If your installation requires that you obtain and install these certificates, you must complete that step before continuing. To learn whether you need to install certificates, and for instructions, see [Install Workflow Manager certificates in SharePoint Server](install-workflow-manager-certificates-in-sharepoint-server.md).
    
2. Sign-in to each server in the SharePoint Server farm.
    
1. Install the SharePoint Workflow Manager **Client** on each server in the SharePoint farm.  
   > [!IMPORTANT]
   > You must install the SharePoint Workflow Manager Client on each server in the SharePoint farm before you run the Register-SPWorkflowService cmdlet. 
    
4. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint Management Shell** command and choosing **Run as administrator**.
    
1. Run the **Register-SPWorkflowService** cmdlet to connect the SharePoint farm with the SharePoint Workflow Manager farm. The cmdlet should be run only once and can be run from any of the servers in the SharePoint farm.  
   > [!NOTE] 
   > The value for the -SPSite parameter can be any valid site collection within the SharePoint farm.
   > The correct value for the -WorkflowHostUri parameter can be found by running PowerShell `Get-WFFarm | select endpoints` on the SharePoint Workflow Manager server.

   **Example**:
   ```powershell
   Register-SPWorkflowService -SPSite "https://myserver/mysitecollection" -WorkflowHostUri "https://workflow.example.com:12290"
   ```

## Upgrade existing Microsoft Workflow Manager

Microsoft Workflow Manager cannot be upgraded in-place, and SharePoint Workflow Manager can't be placed on top of Microsoft Workflow Manager. In order to update Microsoft Workflow Manager (Classic WFM) to SharePoint Workflow Manager (SPWFM), you must uninstall any prior versions of Workflow Manager, Workflow Manager Client, and Service Bus.

> [!NOTE]
> You can upgrade to SharePoint Workflow Manager from any version of Microsoft Workflow Manager. 
> Because you are upgrading an existing "Classic WFM" farm to SPWFM, the WFM databases will be reused, and your existing registration and workflows should remain intact.

Follow the steps below to uninstall Microsoft Workflow Manager and install SharePoint Workflow Manager:

> [!IMPORTANT]
> Because the upgrade steps require that you disjoin and then rejoin an existing WFM farm, you will need the WFM "Certificate Generation Key", when rejoining. If you are not sure what that key is, and have not documented it somewhere, you may need to [Reset Certificate Generation Key](/SharePoint/governance/reset-certificate-generation-key-sharepoint-workflow-manager) before proceeding. 
> You will not be able to join the existing workflow farm without a valid Certificate Generation Key.

1. Run the Workflow Manager Configuration Wizard.

1. Select **Leave Workflow Manager Farm**.
1. Confirm the subsequent steps until the end of the wizard.

1. Repeat this step on every Microsoft Workflow Manager server in the workflow farm.  
   > [!NOTE]
   > Each database used by Workflow Manager and Service Bus will need to be specified when rejoining the farm with SharePoint Workflow Manager. For example, the SQL Server instance and database name for the Workflow Manager farm management database and the Service Bus farm management database.
1. Uninstall Microsoft Workflow Manager, Workflow Manager Client, Service Bus for Windows Server, and Windows Fabric if they're installed. You can uninstall them from the Control Panel. If Windows Fabric is installed, ensure you install Azure Service Fabric after uninstalling Windows Fabric.  
   > [!IMPORTANT]
   > If you are installing SharePoint Workflow Manager on a SharePoint server, you may see both "Windows Fabric" and "AppFabric 1.1 for Windows Server" installed. Be sure to only uninstall Windows Fabric. **Do not uninstall AppFabric 1.1**. It is a different service, and is required for SharePoint Distributed Cache.
1. If the folders "*%ProgramFiles%\Workflow Manager\1.0"*  or *"%Program Files%\Service Bus\1.0"* already exist, you must manually remove them for the next steps to succeed.

1. Reboot the SharePoint Workflow Manager server.

1. If it's not already installed, use the steps from the [Prerequisites section above](/SharePoint/governance/install-and-configure-workflow-for-sharepoint-server#prerequisites) to install Azure Service Fabric.

1. Install SharePoint Workflow Manager and SharePoint Workflow Manager Client. SharePoint Workflow Manager and SharePoint Workflow Manager Client can be downloaded from [here](https://www.microsoft.com/download/details.aspx?id=104867).  The system requirements can be found on that page as well.

1. Run the Workflow Manager Configuration Wizard and choose the "Join an Existing Workflow Manager Farm" to rejoin the previous farm.  Use the database, service account, and Certificate Generation Key information used in the previous "Classic WFM" farm.  
   > [!NOTE]
   > When upgrading, there is typically no need to delete the existing Workflow Service Application Proxy and reconnect using the Register-SPWorkflowService cmdlet. If you encounter the invalidity of the Certificate Generation Key for SharePoint Workflow Manager and Service Bus, you may need to reset it, see [Reset Certificate Generation Key](/SharePoint/governance/reset-certificate-generation-key-sharepoint-workflow-manager).
1. Rerun the Workflow Manager Configuration Wizard, select **Upgrade Workflow Manager Farm**, and confirm subsequent steps until the end.  
   > [!NOTE]
   > This step should be run on all servers in the SharePoint Workflow Manager farm.
   > The "Upgrade Workflow Manager Farm" option is always presented in the Workflow Manager Configuration Wizard, whether an upgrade is required or not.  There's no harm in running it multiple times, or when there's no upgrade pending.
1. If there's more than one server in your Workflow Manager farm, repeat the previous steps on all workflow farm servers.

1. Install the SharePoint Workflow Manager **Client** on each server in the SharePoint Server farm after uninstalling any previous versions.

## Validate the installation
<a name="section6"> </a>

Follow these steps to validate that you have successfully installed and configured the required components.
  
 **To validate the installation**
  
1. Add a user to your SharePoint site and grant the user Site Designer permissions.   
2. Install SharePoint Designer 2013 on a client machine and create a workflow based on the SharePoint 2013 Workflow platform. For more information, see [Creating a workflow by using SharePoint Designer 2013 and the SharePoint 2013 Workflow platform](/sharepoint/dev/general-development/creating-a-workflow-by-using-sharepoint-designer-and-the-sharepoint-wo).    
3. Run this workflow from the SharePoint user interface.
    
## Troubleshooting
<a name="section7"> </a>

For security reasons, the Setup account can't be used to create a workflow based on the SharePoint 2013 Workflow platform. If you try to create a workflow based on the SharePoint 2013 Workflow platform by using SharePoint Designer 2013, you receive a warning that the list of workflow actions don't exist, and the workflow isn't created.
  
The user who deploys and runs a workflow must be added to the User Profile service. Check the User Profile service application page in Central Administration to confirm that the user you're using to validate workflow installation is in the User Profile service.
  
You can determine which ports SharePoint Server and Workflow Manager are using for both HTTP and HTTPS by using IIS Manager as shown in the figure.
  
**Figure: Use IIS Manager to view the ports used by SharePoint Workflow Manager**

![View ports in IIS Manager.](../media/WF15-.png)
  
SharePoint Workflow Manager communicates by using TCP/IP or Named Pipes. Ensure that the appropriate communication protocol is enabled on the SQL Server instance that hosts the SharePoint Workflow Manager databases.

The SQL Browser Service must be running on the SQL Server instance that hosts the Workflow Manager databases.
  
The System Account can't be used to develop a workflow.
  
To troubleshoot SharePoint Server, see [Troubleshooting SharePoint Server](../administration/troubleshoot.md).


