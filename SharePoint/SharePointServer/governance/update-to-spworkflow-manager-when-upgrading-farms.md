---
title: "Upgrade to SharePoint Workflow Manager when upgrading older SharePoint Server farms
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
ms.date: 05/16/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
description: "Learn how to upgrade from Workflow Manager to SharePoint Workflow Manager when upgrading older SharePoint Server farms."
---

# Update from Workflow Manager to SharePoint Workflow Manager on a new farm

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]


## Overview

When upgrading older SharePoint farms that are using Classic Workflow Manager (WFM) to a newer version of SharePoint, WFM will need to be upgraded to SharePoint Workflow Manager (SPWFM) as well. Since you're installing a fresh copy of SPWFM on new hardware and upgrading the existing WFM databases, this procedure is essentially a mix of the new install and upgrade procedures with some added steps.

>[!Note]
>As you are upgrading an existing WFM farm to a SPWFM farm, the WFM databases will be reused. Your existing registration and workflows should remain intact.

## Step 1: Prepare the old Workflow Manager farm

You'll need information from the "old" environment to properly configure the "new" environment. 

### Get the Certificate Generation Key
As the upgrade steps require that you join an existing workflow farm, you'll need the WFM "Certificate Generation Key" when rejoining. If you don't know what that key is and have no written record, [**reset the Certificate Generation Key**](
/sharepoint/governance/reset-certificate-generation-key-sharepoint-workflow-manager) for WFM and Service Bus before proceeding. You must join the existing workflow farm with the proper Certificate Generation Key.


### Check the Scope

You'll need to re-register the *SPWorkflowService* using the same scope name that was used in the old farm.

1. To check the scope name, run the following PowerShell on one of the SharePoint servers in the “old” farm:

```powershell

Add-PSSnapin *sharepoint*
$site = (Get-SPWebapplication -IncludeCentralAdministration | ?{$_.IsAdministrationWebApplication}).Sites[0]
$wfmProxy = Get-SPServiceApplicationProxy | ?{$_.TypeName -eq "Workflow Service Application Proxy"}
$wfmProxy.GetWorkflowServiceAddress($site)

```
2. An address will display similar to this:
*https://<span><span>apps.<span><span>contoso.<span><span>local:12290/SharePoint2013* 

The part after the port number is the **scope name**. In this example, it's "SharePoint2013”. **Write down the scope name and save it for later.** You'll need it when you run *Register-SPWorkflowService* in the new farm.  


### Check the service account and admin group

1. On the WFM server in the "old" farm, open PowerShell.
2. Run 

 ```powershell 

GET-wffarm | select runasaccount, admingroup 

```

Example:

:::image type="content" source="../media/sp-get-wffarm.png" alt-text="display after running get-wffarm command":::


Take note of the account and the group. When you rejoin the workflow farm in the new environment, you must supply the password for the *RunAsAccount*. Only users who are members of the AdminGroup will be able to browse the workflow endpoint URI and run the *Register-SPWorkflowService* command.


### Disjoin the old WFM farm

>[!Important]
>You must run the wizard and leave the workflow farm on the "old" WFM server. 
>You must do this for all nodes in the WFM farm so that the Workflow and Service Bus databases contain no hosts.
>
>If you skip this step, you will orphan the host entries in the Workflow and Service Bus databases, which will cause many problems in the new environment.

1. Sign in to the server hosting the WFM farm and open “Workflow Manager configuration”.
2. Select **Leave Workflow Manager farm** and run through the steps to leave the current farm.
3. If you have multiple nodes (hosts) in your WFM farm, repeat this step for each node.

>[!Note]
>SharePoint Workflow Manager will be installed on your new hardware on the new farm. There is no need to uninstall Workflow Manager and the Service Bus components from your old servers. 
>
>If you want your "old" WFM farm to remain functional during the migration, backup the Workflow and Service Bus databases as described below, then rerun the wizard to rejoin the farm. To prevent moving any node info to the new farm, ensure all nodes are disjoined at the time of the database backup.

## Step 2: Move the Databases

### Move the Content Databases

To maintain parity between the SharePoint sites and the workflows that run on them, you must move the content databases along with the App Management service and WFM databases. Upgrading SharePoint content is outside the scope of this document, but we'll refer to a few items related to upgrading WFM.

Using the database attach method, you can move SharePoint content databases from the old farm to the new farm.

>[!Note]
>If you are moving to a newer major version of SharePoint, you may have to complete an intermediate upgrade step. For example, only SharePoint 2016 and 2019 can be directly upgraded to SharePoint Server Subscription Edition (SPSE). SharePoint 2013 cannot. To upgrade a SharePoint 2013 content database to SPSE, you must first upgrade it to SharePoint 2016, then to SPSE.

Learn more at:

- [Upgrade to SharePoint Server Subscription Edition](/sharepoint/upgrade-and-update/upgrade-to-sharepoint-server-subscription-edition)
- [Upgrade to SharePoint Server 2019](/sharepoint/upgrade-and-update/upgrade-to-sharepoint-server-2019) 
- [Upgrade to SharePoint Server 2016](/sharepoint/upgrade-and-update/upgrade-to-sharepoint-server-2016) 

### Move the App Management database

Since workflows get their permission to SharePoint content through app principals stored in the *App Management database*, you must also upgrade/migrate this database to the new farm.

>[!Important]
>You must move the *App Management database* along with the content, WFM, and Service Bus databases. If you don't, *all workflows created before the migration will fail*.
>
>You will encounter [Issue 3: Workflows fail and return "Cannot get app principal permission information" error](/sharepoint/troubleshoot/workflows/upgrade-sharepoint-through-workflow-manager#issue-3-workflows-fail-and-return-cannot-get-app-principal-permission-information-error). While the problem can be corrected later, it is easier to avoid it by bringing the App Management database along during the upgrade/migration.


#### These are the basic steps:

- **Backup the App Management database** in the old farm using SQL Server backup.
- **Restore the App Management database** to the new SQL server.
- **Create a new App Management Service** In Central Administration in the new farm, go to Manage Service Applications and create a new App Management Service. In the Database section, enter the SQL server name and database name of the App Management database that you restored from the old farm. Basically, we're creating a new service app by reusing the old database. That should upgrade the database to the current SharePoint version.
- **Confirm the service is in the default proxy group**. Make sure that this new App Management Service is in the default proxy group, and that your web applications are using it.

>[!Note]
>Like the content databases, if you are moving to a newer major version of SharePoint, you may have to complete an intermediate upgrade step. For example, only SharePoint 2016 and 2019 can be directly upgraded to SharePoint Server Subscription Edition (SPSE). SharePoint 2013 cannot. To upgrade a SharePoint 2013 content database to SPSE, you must first upgrade it to SharePoint 2016, then to SPSE.

### Move the WFM and Service Bus databases

If the upgrade/migration includes moving databases to a new SQL server, you need to move all the WFM and Service Bus databases.

1. Backup the databases on the old SQL server:
-  SbGatewayDatabase
-  SbManagementDB
-  SBMessageContainer01
-  WFInstanceManagementDB
-  WFManagementDB
-  WFResourceManagementDB

2. Restore the databases on the new SQL server.


#### Restore the databases on the new SQL server

>[!Important]
>You must restore the 6 databases to the new SQL server using **the same database names** that were used previously.  If you change the database names, the workflow configuration wizard will time out when trying to start the Service Bus services.  

#### Create a SQL alias 

The workflow manager configuration wizard only prompts you to enter connection information for 2 of the 6 databases.  The connection strings for the other 4 databases are stored within the 2 databases that you specify.  This is why it's important to restore the databases with the same names that were used previously.  
To keep the previous DB connection strings working, you must also create a SQL alias on the new SPWFM server(s).
- Find the name of the "old" SQL server by running this SQL query against the "SbManagementDB" database:

```sql
select Name, Value as "SQLServerName" from store.serviceconfig where name = 'SBGatewayDatabaseServer'

```  

Example:  


:::image type="content" source="../media/sp-workflow-gatewaydatabaseserver.png" alt-text="example 1 in creating a sql alias":::

- On the SPWFM server, go to Start | Run and type in "cliconfg"  

:::image type="content" source="../media/sp-worflow-createalias.png" alt-text="Example on creating a sql alias":::![image.png](/.attachments/image-85d3556b-9bb2-43dc-8e86-3aade3498431.png)


- On the Alias tab, click Add.
- Choose TCP/IP for the Network library.
- In the "Server Alias" box, type in the name of the "old" SQL server. Example: "SQL"
- In the "Server name" box, type in the name of the "new" SQL server (Example: "New_SQL"), and click ok.

![image.png](/.attachments/image-d2e1ea83-9999-4af9-95b7-23590d176464.png)


>[!Note]
>WFM versions do not align with SharePoint versions, which means if you're doing a multi-version upgrade of SharePoint, you do NOT have to upgrade WFM on each step. 
>
>For example, when upgrading from SharePoint 2013 to SharePoint 2019, you must upgrade the content databases and App Management service application to SharePoint 2016 and then to 2019. But you do NOT have to upgrade WFM in the 2016 farm. Only a single upgrade from WFM (in the 2013 environment) to SPWFM (in the 2019 environment) is required.

## Step 3: Prepare the new SharePoint Workflow Manager server

### Verify the IIS Server Role

1. Check to see if you have the "Web Server (IIS)" server role installed on your new SPWFM server. Install it if it isn't on the server.

If you're installing SPWFM on a non-SharePoint server, it may not already have it installed. Unfortunately, there's nothing forcing you to install it, so if you don't, the Workflow Configuration Wizard will fail with the error, "*Could not load file or assembly 'Microsoft.Web.Administration*".

### Install Azure Service Fabric

SharePoint Workflow Manager requires Azure Service Fabric, which must be installed before you run SharePoint Workflow Manager setup. If the Azure Service Fabric Runtime is not already installed, follow these steps below to install it:

The minimum version of Azure Service Fabric Runtime supported by SharePoint Workflow Manager is 9.1.1583.9590, and you can download it from [Azure Service Fabric Runtime](https://download.microsoft.com/download/b/8/a/b8a2fb98-0ec1-41e5-be98-9d8b5abf7856/MicrosoftServiceFabric.9.1.1583.9590.exe). Or you can find and download any higher version of its Windows Installer from [here](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started#install-the-sdk-and-tools).

Open a PowerShell console as an elevated administrator and run the following command:

`.\MicrosoftServiceFabric.9.1.1583.9590.exe /accepteula`

To verify the Azure Service Fabric is installed, you should be able to find it in the Programs and Features of the Control Panel.

>[!Note] 
>SharePoint Workflow Manager supports the version 9.1.1583.9590 of Azure Service Fabric and [higher versions](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-versions). You can install higher versions than that. If you want to directly upgrade your Azure Service Fabric without uninstallation, note that there are [upgrade dependencies](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-versions). If **Windows Fabric** is already installed on your machine, you must uninstall it before installing Azure Service Fabric.


### Install SPWFM and the SPWFM client on the SPWFM server

1. On the SPWFM server, download and install the [SharePoint Workflow Manager Client and SharePoint Workflow Manager](/download/details.aspx?id=104867)

### Install the SPWFM Client on all SharePoint servers

1. [Download the installer for SharePoint Workflow Manager Client](/download/details.aspx?id=104867).
2. Install the **SharePoint Workflow Manager Client** on all the SharePoint servers in the farm.

### Configure App Management and Subscriptions Settings services

1. On the SharePoint server (if you haven't already) set up the **App Management** service using the upgraded App Management database from the old farm. See the “Move the App Management Database” step above.
2. Create a new Subscription Settings service. 

```powershell
$sa = New-SPSubscriptionSettingsServiceApplication -ApplicationPool 'SharePoint Web Services Default' -Name 'Subscriptions Settings Service Application' -DatabaseName 'Subscription'
New-SPSubscriptionSettingsServiceApplicationProxy -ServiceApplication $sa
```

3. Check the App Management and Subscription service apps. They should be in "Started" state.

:::image type="content" source="../media/sp-app-management-start-state.png" alt-text="confirm app management is in the start state":::

## Step 4: Rejoin the Workflow Farm and Upgrade

1. Run the SPWFM configuration wizard.
2. On the SPWFM server, open “Workflow Manager Configuration” and select **Join an existing Workflow Manager farm**.
3. Enter the SQL Server and database details that the previous WFM 'classic' install was using, and then run through the setup.

:::image type="content" source="../media/sp-workflow-management-wizard.png" alt-text="workflow manager configuration wizard":::

4. Enter the password for the service account and the Certificate Generation Key. 

:::image type="content" source="../media/sp-workflow-management-wizard2.png" alt-text="Workflow wizard with data":::

5. On the SPWFM server, open “Workflow Manager Configuration” again and select **Upgrade Workflow Manager Farm**, and let it run until finished.

 
### Trust the SPWFM SSL certificate on the SharePoint servers

Since SharePoint must contact the SPWFM service endpoint, the SharePoint servers must trust the certificate it's using.

#### Export the certificate

1. On the SPWFM server, open **IIS Manager**. Right-click on the **Workflow Management Site** and choose **Edit Bindings**. Select the HTTPS binding on port 12290 and choose Edit. Select the "View" button next to SSL certificate.

:::image type="content" source="../media/sp-workflow-iis-manager.png" alt-text="select iis manager":::

2. Select the Details tab and choose “Copy to File…”
3. Run through the Certificate Export Wizard to export the certificate without the private key as a**DER encoded binary X.509 (.CER)** certificate.
4. Copy the **.cer** file to the SharePoint Central Administration server.


#### Add the SPWFM certificate to the Farm Trust

1. In Central Administration, to go **Security > Manage Trust**.
2. Choose New, give it a name like “Workflow” or “SPWFM”.
3. Select **Choose File**, and then select the **.cer** file you copied to the computer. Select **OK**.

#### Add the SPWFM certificate to Trusted Root Authorities

1. On the Central Admin server, right-click on the **SPWFM certificate .cer** file and choose **Install Certificate**.
2. Using the Certificate Import Wizard, choose **Local Machine > Place all certificates in the following store > Browse > Trusted Root Certification Authorities**.
 
:::image type="content" source="../media/sp-workflow-certificate-store.png" alt-text="certificate store":::
 
>[!Important]
>You must repeat this certificate import step on all the SharePoint servers in the farm.

### Validate the SharePoint Workflow Manager endpoint


1. **Check from the SPWFM server first**. </br>
a.  Select **Workflow Management Site**. In the right-hand pane, choose **Browse *12290 (https)**. </br>
b.  A browser will open; navigate to https://localhost:12290. If you allowed connections over HTTP during setup, you'll have an HTTP endpoint on port 12291 and an HTTPS endpoint on port 12290. </br>
c. Test both the http and https endpoints.</br>

2. **Check from your SharePoint servers**. Ultimately it's your SharePoint servers that must connect to the SPWFM endpoint, so you must make confirm there's  connectivity from there as well. </br>
a. Sign in to one of your SharePoint Servers with either the **SPWFM RunAs** account, or as a user that is a member of AdminGroup. See “Check the service account and admin group” step above. </br>
b. Browse to the FQDN of the SPWFM endpoint. </br>

For example:

**https://<span>apps<span>.contoso<span><span>.local<span>:12290/**. The result should look like this:

:::image type="content" source="../media/sp-workflow-check-connectivity.png" alt-text="check connectivity":::
  
### Register the Service

1. Sign in to any SharePoint server as either the SPWFM RunAs account, or a user that is a member of AdminGroup. See “Check the service account and admin group” step above.
2. Run the **Register-SPWorkflowService** command to register the workflow service within SharePoint. You'll need the SPWFM endpoint URI, the name of the Scope you gathered in the “Check the scope” step above, and will need to include the -Force parameter. 

Example:

```powershell
Register-SPWorkflowService -SPSite http://www.contoso.local -WorkflowHostUri https://spwfm.contoso.local:12290 -ScopeName SharePoint2013 -Force
```

### Validate the Configuration

1. Check the Workflow Service Application proxy in the **Central Administration > Manage Service Applications**. Select the link for **Workflow Service Application Proxy**. It should show as connected. 

Example:

:::image type="content" source="../media/sp-workflow-status.png" alt-text="workflow status":::

2. **Test a new workflow**</br>
a. Sign in to a client computer, and then open **SharePoint Designer**.</br>
b. Open one of your sites and go to Workflows. </br>
c. Create a new workflow and make sure you can see the “SharePoint Workflow 2013” in the list of platforms to choose from. </br>
d. Create a basic "log to history" 2013-platform workflow and test to make sure it’s successful.</br>

3. **Test an old workflow**</br> 
a. Find a list that had a workflow assigned to it in the "old" farm. </br>
b. Launch a new instance of that workflow and verify that it works. If you included the App Management service app database during the migration, and ran the **Register-SPWorkflowService** using the correct "scope" name, workflows from the old farm should continue to work.</br>

