---
title: "Stsadm to Microsoft PowerShell mapping in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/24/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 27b19a11-5c60-4b5f-bd47-f98081d5493e

description: "Lists Stsadm operations and their equivalent PowerShell cmdlets."
---

# Stsadm to Microsoft PowerShell mapping in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 Where there is no one-to-one mapping between the operations and cmdlets, the table lists the specific PowerShell parameters you must use to get the same functionality. 
  

|&nbsp;|&nbsp;|
|:-----|:-----|
|**Stsadm operation**  |**Windows PowerShell cmdlet**  |
|**Activatefeature**  |[Enable-SPFeature](/powershell/module/sharepoint-server/Enable-SPFeature?view=sharepoint-ps&preserve-view=true)  |
|**Activateformtemplate**  |[Enable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Enable-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Addalternatedomain**  |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps&preserve-view=true)  |
|**Addcontentdb**  |[Mount-SPContentDatabase](/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps&preserve-view=true)  [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Addexemptuseragent**  |[Add-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Add-SPInfoPathUserAgent?view=sharepoint-ps&preserve-view=true)  |
|**Addpath**  |[New-SPManagedPath](/powershell/module/sharepoint-server/New-SPManagedPath?view=sharepoint-ps&preserve-view=true)  |
|**Addpermissionpolicy**  |None   |
|**Addsolution**  |[Add-SPSolution](/powershell/module/sharepoint-server/Add-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Addtemplate**  |None   |
|**Adduser**  |[New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps&preserve-view=true)  |
|**Addwppack**  |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps&preserve-view=true)  |
|**Addzoneurl**  |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps&preserve-view=true)  |
|**Allowuserformwebserviceproxy**  |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps&preserve-view=true)  Use the **AllowForUserForms** and **Identity** parameters.   |
|**Allowwebserviceproxy**  |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps&preserve-view=true)  Use the **AllowWebServiceProxy** and **Identity** parameters.   |
|**Authentication**  |[Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps&preserve-view=true)  Use the **AuthenticationMethod** or **AuthenticationProvider** parameters.   |
|**Backup**  |[Backup-SPConfigurationDatabase](/powershell/module/sharepoint-server/Backup-SPConfigurationDatabase?view=sharepoint-ps&preserve-view=true)  [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps&preserve-view=true)  [Backup-SPSite](/powershell/module/sharepoint-server/Backup-SPSite?view=sharepoint-ps&preserve-view=true)  |
|**Backuphistory**  |[Get-SPBackupHistory](/powershell/module/sharepoint-server/Get-SPBackupHistory?view=sharepoint-ps&preserve-view=true)  |
|**Binddrservice**  |None   |
|**Blockedfilelist**  |None   |
|**Canceldeployment**  |None   |
|**Changepermissionpolicy**  |None   |
|**Copyappbincontent**  |[Install-SPApplicationContent](/powershell/module/sharepoint-server/Install-SPApplicationContent?view=sharepoint-ps&preserve-view=true)  |
|**Createadminvs**  |[New-SPCentralAdministration](/powershell/module/sharepoint-server/New-SPCentralAdministration?view=sharepoint-ps&preserve-view=true)  |
|**Creategroup**  |None   |
|**Createsite**  |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps&preserve-view=true)  |
|**Createsiteinnewdb**  |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps&preserve-view=true) Use the **ContentDatabase** parameter.  [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Createweb**  |[New-SPWeb](/powershell/module/sharepoint-server/New-SPWeb?view=sharepoint-ps&preserve-view=true)  |
|**Databaserepair**  |Use [Get-SPContentDatabaseOrphanedData](/powershell/module/sharepoint-server/Get-SPContentDatabaseOrphanedData?view=sharepoint-ps&preserve-view=true) to detect orphaned data, but note that it does not repair orphaned data.  |
|**Deactivatefeature**  |[Disable-SPFeature](/powershell/module/sharepoint-server/Disable-SPFeature?view=sharepoint-ps&preserve-view=true)  |
|**Deactivateformtemplate**  |[Disable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Disable-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Deleteadminvs**  |[Remove-SPCentralAdministration](/powershell/module/sharepoint-server/Remove-SPCentralAdministration?view=sharepoint-ps&preserve-view=true)  |
|**Deletealternatedomain**  |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps&preserve-view=true)  |
|**Deleteconfigdb**  |[Disconnect-SPConfigurationDatabase](/powershell/module/sharepoint-server/Disconnect-SPConfigurationDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Deletecontentdb**  |[Dismount-SPContentDatabase](/powershell/module/sharepoint-server/Dismount-SPContentDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Deletegroup**  |None   |
|**Deletepath**  |[Remove-SPManagedPath](/powershell/module/sharepoint-server/Remove-SPManagedPath?view=sharepoint-ps&preserve-view=true)  |
|**Deletepermissionpolicy**  |None   |
|**Deletesite**  |[Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps&preserve-view=true)  |
|**Deletesolution**  |[Remove-SPSolution](/powershell/module/sharepoint-server/Remove-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Deletetemplate**  |None   |
|**Deleteuser**  |[Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps&preserve-view=true)  |
|**Deleteweb**  |[Remove-SPWeb](/powershell/module/sharepoint-server/Remove-SPWeb?view=sharepoint-ps&preserve-view=true)  |
|**Deletewppack**  |[Uninstall-SPWebPartPack](/powershell/module/sharepoint-server/Uninstall-SPWebPartPack?view=sharepoint-ps&preserve-view=true)  |
|**Deletezoneurl**  |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps&preserve-view=true)  |
|**Deploysolution**  |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Deploywppack**  |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps&preserve-view=true)  |
|**Disablessc**  |None   |
|**Displaysolution**  |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Editcontentdeploymentpath**  |[Set-SPContentDeploymentPath](/powershell/module/sharepoint-server/Set-SPContentDeploymentPath?view=sharepoint-ps&preserve-view=true)  |
|**Email**  |Use [Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps&preserve-view=true) with the -SMTPServer parameter set.  |
|**Enablessc**  |None   |
|**Enumallwebs**  |[Get-SPContentDatabaseOrphanedData](/powershell/module/sharepoint-server/Get-SPContentDatabaseOrphanedData?view=sharepoint-ps&preserve-view=true)  |
|**Enumalternatedomains**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps&preserve-view=true)  |
|**Enumcontentdbs**  |[Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Enumdataconnectionfiledependants**  |[Get-SPDataConnectionFileDependent](/powershell/module/sharepoint-server/Get-SPDataConnectionFileDependent?view=sharepoint-ps&preserve-view=true)  |
|**Enumdataconnectionfiles**  |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps&preserve-view=true)  |
|**Enumdeployments**  |None   |
|**Enumexemptuseragents**  |[Get-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Get-SPInfoPathUserAgent?view=sharepoint-ps&preserve-view=true)  |
|**Enumformtemplates**  |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Enumgroups**  |None   |
|**Enumroles**  |None   |
|**Enumservices**  |[Get-SPServiceInstance](/powershell/module/sharepoint-server/Get-SPServiceInstance?view=sharepoint-ps&preserve-view=true)  |
|**Enumsites**  |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps&preserve-view=true) (To run this cmdlet, you must be a member of the Farm Administrators group.)   [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps&preserve-view=true) (To run this cmdlet, you must be a local administrator on the computer where SharePoint Server is installed.)   |
|**Enumsolutions**  |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Enumsubwebs**  |[Get-SPWeb](/powershell/module/sharepoint-server/Get-SPWeb?view=sharepoint-ps&preserve-view=true)  |
|**Enumtemplates**  |[Get-SPWebTemplate](/powershell/module/sharepoint-server/Get-SPWebTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Enumusers**  |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps&preserve-view=true)  |
|**Enumwppacks**  |[Get-SPWebPartPack](/powershell/module/sharepoint-server/Get-SPWebPartPack?view=sharepoint-ps&preserve-view=true)  |
|**Enumzoneurls**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps&preserve-view=true)  |
|**Execadmsvcjobs**  |[Start-SPAdminJob](/powershell/module/sharepoint-server/Start-SPAdminJob?view=sharepoint-ps&preserve-view=true)  |
|**Export**  |[Export-SPWeb](/powershell/module/sharepoint-server/Export-SPWeb?view=sharepoint-ps&preserve-view=true)  |
|**Extendvs**  |[New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps&preserve-view=true)  |
|**Extendvsinwebfarm**  |[New-SPWebApplicationExtension](/powershell/module/sharepoint-server/New-SPWebApplicationExtension?view=sharepoint-ps&preserve-view=true)  |
|**Forcedeletelist**  |None   |
|**Getadminport**  |[Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps&preserve-view=true)  Use the following syntax:  `Get-SPWebApplication -IncludeCentralAdministration | ? {$_.IsAdministrationWebApplication -eq $true}`|
|**Getdataconnectionfileproperty** property   |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps&preserve-view=true)  Use the following syntax:   `Get-SPDataConnectionFile | where {$_.Name -eq "dataConFileName"} | format-list`|
|**Getformtemplateproperty** property   |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  Use the following syntax:   `Get-SPInfoPathFormTemplate | where {$_.DisplayName -eq "formTemplateName"} | format-list`|
|**Getosearchsetting**  |None   |
|**Getproperty**  |[Get-SPFarmConfig](/powershell/module/sharepoint-server/Get-SPFarmConfig?view=sharepoint-ps&preserve-view=true)  [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps&preserve-view=true)  |
|**Getsitelock**  |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps&preserve-view=true)  |
|**Getsiteuseraccountdirectorypath**  |None   |
|**Geturlzone**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps&preserve-view=true)  |
|**Import**  |[Import-SPWeb](/powershell/module/sharepoint-server/import-spweb?view=sharepoint-ps&preserve-view=true)  |
|**Installfeature**  |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps&preserve-view=true)  |
|**Listlogginglevels**  |[Get-SPLogLevel](/powershell/module/sharepoint-server/Get-SPLogLevel?view=sharepoint-ps&preserve-view=true)  |
|**Listqueryprocessoroptions**  |None   |
|**Listregisteredsecuritytrimmers**  |[Get-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps&preserve-view=true)  |
|**Localupgradestatus**  |None   |
|**Managepermissionpolicylevel**  |None   |
|**Mergecontentdbs**  |[Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps&preserve-view=true)  |
|**Migrateuser**  |[Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps&preserve-view=true)  |
|**Osearch**  |For the **Osearch** parameters **farmcontactemail**, **farmperformancelevel**, **farmserviceaccount**, and **farmservicepassword**, use the [Get-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchService?view=sharepoint-ps&preserve-view=true) and [Set-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchService?view=sharepoint-ps&preserve-view=true) cmdlets.   For the **Osearch** parameters **start** and **stop**, use the [Start-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Start-SPEnterpriseSearchServiceInstance?view=sharepoint-ps&preserve-view=true) and [Stop-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Stop-SPEnterpriseSearchServiceInstance?view=sharepoint-ps&preserve-view=true) cmdlets, respectively.   For the **Osearch** parameter **defaultindexlocation**, use the [Get-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceInstance?view=sharepoint-ps&preserve-view=true) cmdlet.   |
|**Osearchdiacriticsensitive**  |Use the [Get-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceApplication?view=sharepoint-ps&preserve-view=true) cmdlet to retrieve the specific Search service application, and then use **DiacriticSensitive** parameter from the [Set-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchServiceApplication?view=sharepoint-ps&preserve-view=true) cmdlet.   |
|**Profilechangelog**  |None.   However, you can use the Stsadm **profilechangelog** operation if you replace the Shared Services Provider (SSP) name with the service application (SA) name:   ```stsadm -o profilechangelog-title <SA name>-daysofhistory <number of days>-generateanniversaries```   |
|**Provisionservice**  |[Start-SPServiceInstance](/powershell/module/sharepoint-server/Start-SPServiceInstance?view=sharepoint-ps&preserve-view=true)  |
|**Quiescefarm**  |None   |
|**Quiescefarmstatus**  |None   |
|**Quiesceformtemplate**  |[Stop-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Stop-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Reconvertallformtemplates**  |[Update-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Update-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Refreshdms**  |None   |
|**Refreshsitedms**  |None   |
|**Registersecuritytrimmer**  |[New-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/New-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps&preserve-view=true)  |
|**Registerwsswriter**  |None   |
|**Removedataconnectionfile**  |[Uninstall-SPDataConnectionFile](/powershell/module/sharepoint-server/Uninstall-SPDataConnectionFile?view=sharepoint-ps&preserve-view=true)  |
|**Removedrservice**  |None   |
|**Removeexemptuseragent**  |[Remove-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Remove-SPInfoPathUserAgent?view=sharepoint-ps&preserve-view=true)  |
|**Removeformtemplate**  |[Uninstall-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Uninstall-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Removesolutiondeploymentlock**  |None   |
|**Renameserver**  |[Rename-SPServer](/powershell/module/sharepoint-server/Rename-SPServer?view=sharepoint-ps&preserve-view=true)  |
|**Renamesite**  |[Set-SPSite](/powershell/module/sharepoint-server/Set-SPSite?view=sharepoint-ps&preserve-view=true)  Use the **Url** parameter.   |
|**Renameweb**  |[Set-SPWeb](/powershell/module/sharepoint-server/Set-SPWeb?view=sharepoint-ps&preserve-view=true)  Use the **RelativeUrl** parameter.   |
|**Restore**  |[Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps&preserve-view=true)  [Restore-SPSite](/powershell/module/sharepoint-server/Restore-SPSite?view=sharepoint-ps&preserve-view=true)  |
|**Retractsolution**  |[Uninstall-SPSolution](/powershell/module/sharepoint-server/Uninstall-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Retractwppack**  |None   |
|**Runcontentdeploymentjob**  |[Start-SPContentDeploymentJob](/powershell/module/sharepoint-server/Start-SPContentDeploymentJob?view=sharepoint-ps&preserve-view=true)  |
|**Scanforfeatures**  |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps&preserve-view=true)  Use the **Scanforfeatures** parameter.   |
|**Setadminport**  |[Set-SPCentralAdministration](/powershell/module/sharepoint-server/Set-SPCentralAdministration?view=sharepoint-ps&preserve-view=true)  |
|**Setapppassword**  |[Set-SPApplicationCredentialKey](/powershell/module/sharepoint-server/Set-SPApplicationCredentialKey?view=sharepoint-ps&preserve-view=true) [Remove-SPApplicationCredentialKey](/powershell/module/sharepoint-server/Remove-SPApplicationCredentialKey?view=sharepoint-ps&preserve-view=true)  |
|**Setconfigdb**  |[Connect-SPConfigurationDatabase](/powershell/module/sharepoint-server/Connect-SPConfigurationDatabase?view=sharepoint-ps&preserve-view=true)  |
|**Setcontentdeploymentjobschedule**  |[Set-SPContentDeploymentJob](/powershell/module/sharepoint-server/Set-SPContentDeploymentJob?view=sharepoint-ps&preserve-view=true)  |
|**Setdataconnectionfileproperty**  |[Set-SPDataConnectionFile](/powershell/module/sharepoint-server/Set-SPDataConnectionFile?view=sharepoint-ps&preserve-view=true)  |
|**Setformtemplateproperty**  |[Set-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Set-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Setlogginglevel**  |[Set-SPLogLevel](/powershell/module/sharepoint-server/Set-SPLogLevel?view=sharepoint-ps&preserve-view=true)  |
|**Setosearchsetting**  |None   |
|**Setproperty**  |[Set-SPFarmConfig](/powershell/module/sharepoint-server/Set-SPFarmConfig?view=sharepoint-ps&preserve-view=true)  [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps&preserve-view=true)  [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps&preserve-view=true)  |
|**Setqueryprocessoroptions**  |None   |
|**Setsitelock**  |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps&preserve-view=true)  Use the **LockState** parameter.   |
|**Setsiteuseraccountdirectorypath**  |[Get-SPSiteSubscription](/powershell/module/sharepoint-server/Get-SPSiteSubscription?view=sharepoint-ps&preserve-view=true)  [New-SPSiteSubscription](/powershell/module/sharepoint-server/New-SPSiteSubscription?view=sharepoint-ps&preserve-view=true)  [Remove-SPSiteSubscription](/powershell/module/sharepoint-server/Remove-SPSiteSubscription?view=sharepoint-ps&preserve-view=true)  |
|**Setworkflowconfig**  |[Set-SPWorkflowConfig](/powershell/module/sharepoint-server/Set-SPWorkflowConfig?view=sharepoint-ps&preserve-view=true)  |
|**Siteowner**  |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps&preserve-view=true)  |
|**Sync**  |[Update-SPProfileSync](/powershell/module/sharepoint-server/Update-SPProfileSync?view=sharepoint-ps&preserve-view=true) [Clear-SPContentDatabaseSyncData](/powershell/module/sharepoint-server/Clear-SPContentDatabaseSyncData?view=sharepoint-ps&preserve-view=true) [Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps&preserve-view=true) (with the -DaysSinceLastProfileSync parameter)  |
|**Syncsolution**  |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps&preserve-view=true)  Use the **Synchronize** parameter.   |
|**Unextendvs**  |[Remove-SPWebApplication](/powershell/module/sharepoint-server/Remove-SPWebApplication?view=sharepoint-ps&preserve-view=true)  |
|**Uninstallfeature**  |[Uninstall-SPFeature](/powershell/module/sharepoint-server/Uninstall-SPFeature?view=sharepoint-ps&preserve-view=true)  |
|**Unquiescefarm**  |None   |
|**Unquiesceformtemplate**  |[Start-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Start-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Unregistersecuritytrimmer**  |[Remove-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Remove-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps&preserve-view=true)  |
|**Unregisterwsswriter**  |None   |
|**Updateaccountpassword**  |[Set-SPManagedAccount](/powershell/module/sharepoint-server/Set-SPManagedAccount?view=sharepoint-ps&preserve-view=true)  |
|**Updatealerttemplates**  |None   |
|**Updatefarmcredentials**  |None   |
|**Upgrade**  |None   |
|**Upgradeformtemplate**  |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Upgradesolution**  |[Update-SPSolution](/powershell/module/sharepoint-server/Update-SPSolution?view=sharepoint-ps&preserve-view=true)  |
|**Upgradetargetwebapplication**  |None   |
|**Uploadformtemplate**  |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
|**Userrole**  |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps&preserve-view=true)  [Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps&preserve-view=true)  [New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps&preserve-view=true)  [Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps&preserve-view=true)  [Set-SPUser](/powershell/module/sharepoint-server/Set-SPUser?view=sharepoint-ps&preserve-view=true)  |
|**Verifyformtemplate**  |[Test-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Test-SPInfoPathFormTemplate?view=sharepoint-ps&preserve-view=true)  |
   
## See also

#### Other Resources

[Index of Microsoft PowerShell cmdlets for SharePoint Server](/powershell/module/sharepoint-server/?view=sharepoint-ps&preserve-view=true)

