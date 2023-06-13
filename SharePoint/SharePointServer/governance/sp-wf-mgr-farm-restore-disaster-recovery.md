---
title: "SharePoint Workflow Manager Farm Restore and Disaster Recovery"
description: "The steps that enable you move your SharePoint Workflow Manager (SPWFM) databases to a new SQL Server instance."
ms.reviewer: 
ms.author: v-smandalika
author: v-smandalika
manager: dansimp
ms.date: 6/13/2023
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- DiscoverySearchSyntaxTips
- WSSEndUser_DiscoverySearchSyntaxTips
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- tier1
- purview-compliance
- M365-collaboration
- ediscovery
---

# SharePoint Workflow Manager Farm Restore and Disaster Recovery - Overview

Use the steps in this article to move your SharePoint Workflow Manager (SPWFM) databases to a new SQL Server instance. This movement may be done as part of a disaster recovery (DR) effort, a migration, or if you simply must rename the SPWFM databases. These steps could also be used as an alternative method for upgrading or migrating from “Classic Workflow Manager” (WFM) to SharePoint Workflow Manager (SPWFM) on a new hardware. However, it's a bit more complex than the recommended procedure, detailed in [Upgrade from Workflow Manager to SharePoint Workflow Manager on a new farm](https://learn.microsoft.com/en-us/sharepoint/governance/update-to-spworkflow-manager-when-upgrading-farms). If you choose to use this "farm restore" procedure to upgrade/migrate, keep in mind that the SharePoint content databases and App Management Service Application database also need to be upgraded along the way to keep your existing workflows intact.

> [!IMPORTANT]
> The Workflow Configuration Wizard only prompts you for the database connection information, and for the names of the Service Bus Management and Workflow Management databases. The connection information for the other four Service Bus and Workflow databases are stored within those two management databases. Since that connection information isn't updated by the wizard, you can't use the wizard to change SQL servers or database names. In that case, you must use the procedures specified in [Scenario 1: Using an SQL alias](#scenario-1-using-an-sql-alias) and [Scenario 2: Without using a SQL alias (Farm Restore)](#scenario-2-without-using-a-sql-alias-farm-restore) to restore the workflow farm:

## Scenario 1: Using an SQL alias

If you're open to using an SQL alias, then moving SPWFM databases to a new SQL server is easy.

1. Stop all SPWFM services on all SPWFM servers, or if possible, shut down the servers to drop existing connections to the Workflow (WF) and Service Bus (SB) databases. SPWFM-related services include:

- Service Bus Gateway
- Service Bus Message Broker
- Service Bus Resource Provider
- Service Bus VSS
- Service Fabric Host Service
- Workflow Manager Backend
- World Wide Web Publishing Service

1. Move the WF and SB databases physically from the original SQL Server instance to the target SQL Server instance. Database backup and restore works well for that.

You need to keep the same database names for the 6 Service Bus and Workflow databases during the move. If you need to change database names, then you'll have to use [Scenario 2](#scenario-2-without-using-a-sql-alias-farm-restore).

1. Create an SQL alias using *cliconfg.exe* on **all** the SPWFM servers. For more information on creating the alias, see the [Create a SQL alias](update-to-spworkflow-manager-when-upgrading-farms.md#create-a-sql-alias).

1. Restart your SPWFM servers/services.
   Since we are using an SQL alias to map the "old" SQL server name to the "new" SQL server, SPWFM is unaware that there have been changes. The services should come up and connect to the databases on the new SQL server.

## Scenario 2: Without using a SQL alias (Farm Restore)

If for some reason you can't use an SQL alias, or if you need to change the names of the 6 Service Bus and Workflow databases, then you'll have to complete a Workflow "Farm Restore".  This process, while not too complicated, has many potential failure points. 

> [!TIP]
> As such, it's _strongly_ recommended to use an SQL alias and keep your database names the same, as described above in [Scenario 1](#scenario-1-using-an-sql-alias).

### Move the WFM and SB databases

- Using this procedure, we only need 4 out of the 6 WFM/SB databases. We do **NOT** need the WFManagementDB and SbManagementDB databases which will be created new as part of this procedure.
- Back up the 4 databases you need on the "old" SQL server and restore them to your "new" SQL server. In the following example, the databases have been restored with the default database names:

```powershell
SbGatewayDatabase
SBMessageContainer01
WFInstanceManagementDB
WFResourceManagementDB
```

### Restore the Workflow Farm

If you have multiple SPWFM servers, choose one on which you can run the restore-process. We'll refer to this server as "the SPWFM server" going forward.

On the SPWFM server, we need to run through some PowerShell to restore everything using the restored databases. In this PowerShell process, it's advised to run one step at a time and not just run everything as a single script. That way if one step fails, you can troubleshoot it thereby preventing it from going on to the next step and potentially making a mess.

> [!IMPORTANT]
> You're setting a new "**Certificate Generation Key**" in the restored farm. You'll want to store this value somewhere, as it's required any time you rejoin the farm or when you join additional servers to the farm.

Using your Administrator privileges, run PowerShell ISE on the SPWFM server and perform the following steps to restore the Workflow farm:

#### Step 1: Set the variables

The variables being referred to are the variables that the rest of the commands will use.  After setting these variables appropriately for your environment, you shouldn't have to make any changes within any of the subsequent commands.

```powershell
$wfmAcc = "CONTOSO\spfarm" # Account in services.msc used to run the SPWFM services
$newPass = "YourPWDHere" # Set the password of the SPWFM service account defined variable $wfmAcc
$certGenKeyPlain = "YourCertGenKeyHere" # A new Certificate Generation Key of your choosing  
$manageUsers = @("spfarm@contoso.local","sysadm@contoso.local") # Admin accounts. Use UPN form (user@domain). This should include the account that is running this script.
$adminGroup = "BUILTIN\Administrators" # The group that will have admin permissions for the SPWFM farm.  The local administrators group is common.  
$newSQL = "sql" # Set the SQL instance name of the target SQL server
$sbGatewayDB = "SbGatewayDatabase" # Restored Service Bus Gateway DB name 
$sbMessageDB = "SBMessageContainer01" # Restored Service Bus Message Container DB name
$sbManageDB = "SbManagementDB" # Name for the NEW Service Bus Management DB that will be created
$wfInstanceDB = "WFInstanceManagementDB" #  Restored Workflow Instance Management DB
$wfResourceDB = "WFResourceManagementDB" # Restored Workflow Resource Management DB
$wfManageDB = "WFManagementDB" # Name for the NEW Workflow Management DB DB that will be created
$logPath = "C:\temp\wfm-restore.log.txt" # A log file used for recording information during the restore

### You should not need to change anything below this line ###
# Set a few more variables automatically
$PrimarySymmetricKey = [Convert]::ToBase64String((1..32|%{[byte](Get-Random -Max 256)}))
$certGenKey = convertto-securestring $certGenKeyPlain -asplaintext -force
$myPassword = convertto-securestring $newPass -asplaintext -force
$restoreTime = Get-Date 
```

#### Step 2: Restore the Service Bus farm

```powershell
# Restore the Service Bus farm
# You'll get a warning about the Farm Encryption Token, but don't worry, we'll fix that in a later step
Restore-SBFarm -RunAsAccount $wfmAcc -GatewayDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbGatewayDB;Integrated Security=True;Encrypt=False" -SBFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbManageDB;Integrated Security=True;Encrypt=False" -AdminGroup $adminGroup -CertificateAutoGenerationKey $certGenKey -Verbose
```

> [!NOTE]
> You'll get a warning about the "Farm Encryption Token", but don't worry, we'll fix that in a later step.

#### Restore the Service Bus Message Container

```powershell
# Restore the Service Bus Message Container
Restore-SBMessageContainer -ContainerDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbMessageDB;Integrated Security=True;Encrypt=False" -SBFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbManageDB;Integrated Security=True;Encrypt=False" -Id 1 -Verbose
```

#### Restore the Service Bus Gateway

```powershell
# Restore the Service Bus Gateway
Restore-SBGateway -GatewayDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbGatewayDB;Integrated Security=True;Encrypt=False" -SBFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbManageDB;Integrated Security=True;Encrypt=False" -Verbose
```

> [!NOTE]
> If you get a "The operation has timed out" error, just ignore that and move on.

#### Upgrade the Service Bus Farm

```powershell
# Upgrade the Service Bus farm
Invoke-SBFarmUpgrade -SBFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbManageDB;Integrated Security=True;Encrypt=False" -CertificateAutoGenerationKey $certGenKey -Verbose
```

#### Add the local SPWFM server to the Service Bus

```powershell
# Add the local SPWFM server to the Service Bus farm
Add-SBHost -EnableFirewallRules $TRUE -RunAsPassword $myPassword -CertificateAutoGenerationKey $certGenKey -SBFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$sbManageDB;Integrated Security=True;Encrypt=False" -Verbose
``` 

#### Set the Service Bus namespace

```powershell
# Set the Service Bus namespace
Set-SBNamespace -Name "WorkflowDefaultNamespace" -PrimarySymmetricKey $PrimarySymmetricKey -ManageUsers $manageUsers -Verbose
```

#### Verify the Service Bus is happy

```powershell
# At this point, all SB services should be running and we should have a namespace of "WorkflowDefaultNamespace" defined.
# If not, you'll want to fix that before moving on.
Get-SBFarm
Get-SBFarmStatus
Get-SBNamespace -Name WorkflowDefaultNamespace
```

#### Restore the Workflow Manager Services Farm

```powershell
# Restore the Workflow Manager Services and Farm
Restore-WFFarm -RunAsAccount $wfmAcc -InstanceDBConnectionString "Data Source=$newSQL;Initial Catalog=$wfInstanceDB;Integrated Security=True;Asynchronous Processing=True;Encrypt=False" -ResourceDBConnectionString "Data Source=$newSQL;Initial Catalog=$wfResourceDB;Integrated Security=True;Asynchronous Processing=True;Encrypt=False" -WFFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$wfManageDB;Integrated Security=True;Encrypt=False" -InstanceStateSyncTime $restoreTime -ConsistencyVerifierLogPath $logPath -CertificateAutoGenerationKey $certGenKey -Verbose 
```

#### Add the local SPWFM server to the SPWFM farm

```powershell
# Add the local SPWFM server to the SPWFM farm
$SBClientConfiguration = Get-SBClientConfiguration -Namespaces "WorkflowDefaultNamespace" 
Add-WFHost -WFFarmDBConnectionString "Data Source=$newSQL;Initial Catalog=$wfManageDB;Integrated Security=True;Encrypt=False" -RunAsPassword $myPassword -EnableFirewallRules $TRUE -CertificateAutoGenerationKey $certGenKey -SBClientConfiguration $SBClientConfiguration –Verbose 
```

#### Upgrade SPWFM

```powershell
# Upgrade the SPWFM host
Invoke-WFHostUpgrade -Verbose
```

Alternatively, you can run the Workflow Manager Configuration Wizard and select **Upgrade Workflow Manager Farm**.

#### Check Status

After upgrade, give it a minute or two to start services; then check the status by running this PowerShell:  

`Get-WFFarm; Get-WFFarmStatus; Get-SBFarm; Get-SBFarmStatus` 
 
It should show that all the services are running, and that there are no errors.

#### Join other servers to workflow farm

At this point, if everything looks good, if you had additional servers in the SPWFM farm, you should be able to add them back to the farm by running the Workflow Manager Configuration wizard and choosing to join an existing farm.

The "Certificate Generation Key" was set in the script above, so you'll have to use that when joining the farm.

### Validate on the SharePoint side

#### Trust the SPWFM SSL certificate on the SharePoint servers

Because new SPWFM certificates were created as part of this procedure, the following steps must be implemented to ensure the SharePoint servers trust them:

1. Complete the steps in the [Trust the SPWFM SSL certificate on the SharePoint servers]( https://learn.microsoft.com/en-us/sharepoint/governance/update-to-spworkflow-manager-when-upgrading-farms#trust-the-spwfm-ssl-certificate-on-the-sharepoint-servers) section to trust the SPWFM endpoint certificate on all the SharePoint servers.
1. Refresh the SPWFM Outbound Certificate used in **SPTrustedSecurityTokenIssuer** by running the RefreshMetadataFeed timer job on any SharePoint server:

```powershell
 $tj = Get-SPTimerJob | ? {$_.name -match "RefreshMetadataFeed"} 
 Start-SPTimerJob $tj
```

#### Validate the SPWFM endpoint

On one of the SharePoint servers, sign in either as the SPWFM RunAs account or as a user that is a member of AdminGroup, as defined in the script above. Browse to the FQDN of the SPWFM endpoint, for example, `https://apps.contoso.local:12290/`. The result should look like as shown in the following screenshot:

:::image type="content" source="../media/validate-spwfm-endpoint.png" alt-text="The result of the SPWFM endpoint's validation process." lightbox="../media/validate-spwfm-endpoint.png":::

## Optional steps

### Register the SharePoint farm

If you used these steps to simply move Workflow (WF) and Service Bus (SB) databases to a new SQL server, then the SharePoint farm is already registered and you are **not** required to complete this step.

However, if you used these steps to migrate your SB and WF databases to a _new_ SPWFM farm, for example, as part of a SharePoint farm upgrade/migration, then you will need to run the following `Register-SPWorkflowService` command to connect the SharePoint farm with the SPWFM farm.

```powershell
$Scope = "SharePoint" # Use the Scope Name you were using previously
$site = "https://sp.contoso.local/" # Any site in the SharePoint web application
$wfURI = "https://spwfm.contoso.local:12290" # Get this value by running "Get-WFFarm | select endpoints" on the SPWFM server
Register-SPWorkflowService -SPSite $site -WorkflowHostUri $wfURI -ScopeName $Scope -Force
```

### Publish a New Workflow

If you used this procedure to upgrade/migrate, and if your SharePoint web application URLs have changed as part of this migration (for example, from `http://sp2013.contoso.local` to `https://spse.contoso.local`), workflows that were created prior to the workflow migration/farm restore won't at first. You'll need to publish a new workflow first.  For more information, see [Issue 1: Site URL is changed](/sharepoint/troubleshoot/workflows/upgrade-sharepoint-through-workflow-manager#issue-1-site-url-is-changed).
