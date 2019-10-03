---
title: "Stsadm to Microsoft PowerShell mapping in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 27b19a11-5c60-4b5f-bd47-f98081d5493e

description: "Lists Stsadm operations and their equivalent PowerShell cmdlets."
---

# Stsadm to Microsoft PowerShell mapping in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 Where there is no one-to-one mapping between the operations and cmdlets, the table lists the specific PowerShell parameters you must use to get the same functionality. 
  
## 
|||
|:-----|:-----|
|**Stsadm operation**  |**Windows PowerShell cmdlet**  |
|**Activatefeature**  |[Enable-SPFeature](/powershell/module/sharepoint-server/Enable-SPFeature?view=sharepoint-ps)  |
|**Activateformtemplate**  |[Enable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Enable-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Addalternatedomain**  |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps)  |
|**Addcontentdb**  |[Mount-SPContentDatabase](/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps)  [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps)  |
|**Addexemptuseragent**  |[Add-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Add-SPInfoPathUserAgent?view=sharepoint-ps)  |
|**Addpath**  |[New-SPManagedPath](/powershell/module/sharepoint-server/New-SPManagedPath?view=sharepoint-ps)  |
|**Addpermissionpolicy**  |None   |
|**Addsolution**  |[Add-SPSolution](/powershell/module/sharepoint-server/Add-SPSolution?view=sharepoint-ps)  |
|**Addtemplate**  |None   |
|**Adduser**  |[New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps)  |
|**Addwppack**  |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps)  |
|**Addzoneurl**  |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps)  |
|**Allowuserformwebserviceproxy**  |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps)  Use the **AllowForUserForms** and **Identity** parameters.   |
|**Allowwebserviceproxy**  |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps)  Use the **AllowWebServiceProxy** and **Identity** parameters.   |
|**Authentication**  |[Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps)  Use the **AuthenticationMethod** or **AuthenticationProvider** parameters.   |
|**Backup**  |[Backup-SPConfigurationDatabase](/powershell/module/sharepoint-server/Backup-SPConfigurationDatabase?view=sharepoint-ps)  [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps)  [Backup-SPSite](/powershell/module/sharepoint-server/Backup-SPSite?view=sharepoint-ps)  |
|**Backuphistory**  |[Get-SPBackupHistory](/powershell/module/sharepoint-server/Get-SPBackupHistory?view=sharepoint-ps)  |
|**Binddrservice**  |None   |
|**Blockedfilelist**  |None   |
|**Canceldeployment**  |None   |
|**Changepermissionpolicy**  |None   |
|**Copyappbincontent**  |[Install-SPApplicationContent](/powershell/module/sharepoint-server/Install-SPApplicationContent?view=sharepoint-ps)  |
|**Createadminvs**  |[New-SPCentralAdministration](/powershell/module/sharepoint-server/New-SPCentralAdministration?view=sharepoint-ps)  |
|**Creategroup**  |None   |
|**Createsite**  |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps)  |
|**Createsiteinnewdb**  |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps) Use the **ContentDatabase** parameter.  [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps)  |
|**Createweb**  |[New-SPWeb](/powershell/module/sharepoint-server/New-SPWeb?view=sharepoint-ps)  |
|**Databaserepair**  |Use [Get-SPContentDatabaseOrphanedData](/powershell/module/sharepoint-server/Get-SPContentDatabaseOrphanedData?view=sharepoint-ps) to detect orphaned data, but note that it does not repair orphaned data.  |
|**Deactivatefeature**  |[Disable-SPFeature](/powershell/module/sharepoint-server/Disable-SPFeature?view=sharepoint-ps)  |
|**Deactivateformtemplate**  |[Disable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Disable-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Deleteadminvs**  |[Remove-SPCentralAdministration](/powershell/module/sharepoint-server/Remove-SPCentralAdministration?view=sharepoint-ps)  |
|**Deletealternatedomain**  |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps)  |
|**Deleteconfigdb**  |[Disconnect-SPConfigurationDatabase](/powershell/module/sharepoint-server/Disconnect-SPConfigurationDatabase?view=sharepoint-ps)  |
|**Deletecontentdb**  |[Dismount-SPContentDatabase](/powershell/module/sharepoint-server/Dismount-SPContentDatabase?view=sharepoint-ps)  |
|**Deletegroup**  |None   |
|**Deletepath**  |[Remove-SPManagedPath](/powershell/module/sharepoint-server/Remove-SPManagedPath?view=sharepoint-ps)  |
|**Deletepermissionpolicy**  |None   |
|**Deletesite**  |[Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps)  |
|**Deletesolution**  |[Remove-SPSolution](/powershell/module/sharepoint-server/Remove-SPSolution?view=sharepoint-ps)  |
|**Deletetemplate**  |None   |
|**Deleteuser**  |[Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps)  |
|**Deleteweb**  |[Remove-SPWeb](/powershell/module/sharepoint-server/Remove-SPWeb?view=sharepoint-ps)  |
|**Deletewppack**  |[Uninstall-SPWebPartPack](/powershell/module/sharepoint-server/Uninstall-SPWebPartPack?view=sharepoint-ps)  |
|**Deletezoneurl**  |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps)  |
|**Deploysolution**  |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps)  |
|**Deploywppack**  |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps)  |
|**Disablessc**  |None   |
|**Displaysolution**  |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps)  |
|**Editcontentdeploymentpath**  |[Set-SPContentDeploymentPath](/powershell/module/sharepoint-server/Set-SPContentDeploymentPath?view=sharepoint-ps)  |
|**Email**  |Use [Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps) with the -SMTPServer parameter set.  |
|**Enablessc**  |None   |
|**Enumallwebs**  |[Get-SPContentDatabaseOrphanedData](/powershell/module/sharepoint-server/Get-SPContentDatabaseOrphanedData?view=sharepoint-ps)  |
|**Enumalternatedomains**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps)  |
|**Enumcontentdbs**  |[Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps)  |
|**Enumdataconnectionfiledependants**  |[Get-SPDataConnectionFileDependent](/powershell/module/sharepoint-server/Get-SPDataConnectionFileDependent?view=sharepoint-ps)  |
|**Enumdataconnectionfiles**  |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps)  |
|**Enumdeployments**  |None   |
|**Enumexemptuseragents**  |[Get-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Get-SPInfoPathUserAgent?view=sharepoint-ps)  |
|**Enumformtemplates**  |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Enumgroups**  |None   |
|**Enumroles**  |None   |
|**Enumservices**  |[Get-SPServiceInstance](/powershell/module/sharepoint-server/Get-SPServiceInstance?view=sharepoint-ps)  |
|**Enumsites**  |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps) (To run this cmdlet, you must be a member of the Farm Administrators group.)   [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps) (To run this cmdlet, you must be a local administrator on the computer where SharePoint Server is installed.)   |
|**Enumsolutions**  |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps)  |
|**Enumsubwebs**  |[Get-SPWeb](/powershell/module/sharepoint-server/Get-SPWeb?view=sharepoint-ps)  |
|**Enumtemplates**  |[Get-SPWebTemplate](/powershell/module/sharepoint-server/Get-SPWebTemplate?view=sharepoint-ps)  |
|**Enumusers**  |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps)  |
|**Enumwppacks**  |[Get-SPWebPartPack](/powershell/module/sharepoint-server/Get-SPWebPartPack?view=sharepoint-ps)  |
|**Enumzoneurls**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps)  |
|**Execadmsvcjobs**  |[Start-SPAdminJob](/powershell/module/sharepoint-server/Start-SPAdminJob?view=sharepoint-ps)  |
|**Export**  |[Export-SPWeb](/powershell/module/sharepoint-server/Export-SPWeb?view=sharepoint-ps)  |
|**Extendvs**  |[New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps)  |
|**Extendvsinwebfarm**  |[New-SPWebApplicationExtension](/powershell/module/sharepoint-server/New-SPWebApplicationExtension?view=sharepoint-ps)  |
|**Forcedeletelist**  |None   |
|**Getadminport**  |[Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps)  Use the following syntax:  `Get-SPWebApplication -IncludeCentralAdministration | ? {$_.IsAdministrationWebApplication -eq $true}`|
|**Getdataconnectionfileproperty** property   |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps)  Use the following syntax:   `Get-SPDataConnectionFile | where {$_.Name -eq "dataConFileName"} | format-list`|
|**Getformtemplateproperty** property   |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps)  Use the following syntax:   `Get-SPInfoPathFormTemplate | where {$_.DisplayName -eq "formTemplateName"} | format-list`|
|**Getosearchsetting**  |None   |
|**Getproperty**  |[Get-SPFarmConfig](/powershell/module/sharepoint-server/Get-SPFarmConfig?view=sharepoint-ps)  [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps)  [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps)  [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps)  [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps)  [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps)  |
|**Getsitelock**  |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps)  |
|**Getsiteuseraccountdirectorypath**  |None   |
|**Geturlzone**  |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps)  |
|**Import**  |[Import-SPWeb](/powershell/module/sharepoint-server/import-spweb?view=sharepoint-ps)  |
|**Installfeature**  |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps)  |
|**Listlogginglevels**  |[Get-SPLogLevel](/powershell/module/sharepoint-server/Get-SPLogLevel?view=sharepoint-ps)  |
|**Listqueryprocessoroptions**  |None   |
|**Listregisteredsecuritytrimmers**  |[Get-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps)  |
|**Localupgradestatus**  |None   |
|**Managepermissionpolicylevel**  |None   |
|**Mergecontentdbs**  |[Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps)  |
|**Migrateuser**  |[Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps)  |
|**Osearch**  |For the **Osearch** parameters **farmcontactemail**, **farmperformancelevel**, **farmserviceaccount**, and **farmservicepassword**, use the [Get-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchService?view=sharepoint-ps) and [Set-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchService?view=sharepoint-ps) cmdlets.   For the **Osearch** parameters **start** and **stop**, use the [Start-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Start-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) and [Stop-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Stop-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) cmdlets, respectively.   For the **Osearch** parameter **defaultindexlocation**, use the [Get-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) cmdlet.   |
|**Osearchdiacriticsensitive**  |Use the [Get-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceApplication?view=sharepoint-ps) cmdlet to retrieve the specific Search service application, and then use **DiacriticSensitive** parameter from the [Set-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchServiceApplication?view=sharepoint-ps) cmdlet.   |
|**Profilechangelog**  |None.   However, you can use the Stsadm **profilechangelog** operation if you replace the Shared Services Provider (SSP) name with the service application (SA) name:   ```stsadm -o profilechangelog-title <SA name>-daysofhistory <number of days>-generateanniversaries```   |
|**Provisionservice**  |[Start-SPServiceInstance](/powershell/module/sharepoint-server/Start-SPServiceInstance?view=sharepoint-ps)  |
|**Quiescefarm**  |None   |
|**Quiescefarmstatus**  |None   |
|**Quiesceformtemplate**  |[Stop-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Stop-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Reconvertallformtemplates**  |[Update-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Update-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Refreshdms**  |None   |
|**Refreshsitedms**  |None   |
|**Registersecuritytrimmer**  |[New-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/New-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps)  |
|**Registerwsswriter**  |None   |
|**Removedataconnectionfile**  |[Uninstall-SPDataConnectionFile](/powershell/module/sharepoint-server/Uninstall-SPDataConnectionFile?view=sharepoint-ps)  |
|**Removedrservice**  |None   |
|**Removeexemptuseragent**  |[Remove-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Remove-SPInfoPathUserAgent?view=sharepoint-ps)  |
|**Removeformtemplate**  |[Uninstall-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Uninstall-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Removesolutiondeploymentlock**  |None   |
|**Renameserver**  |[Rename-SPServer](/powershell/module/sharepoint-server/Rename-SPServer?view=sharepoint-ps)  |
|**Renamesite**  |[Set-SPSite](/powershell/module/sharepoint-server/Set-SPSite?view=sharepoint-ps)  Use the **Url** parameter.   |
|**Renameweb**  |[Set-SPWeb](/powershell/module/sharepoint-server/Set-SPWeb?view=sharepoint-ps)  Use the **RelativeUrl** parameter.   |
|**Restore**  |[Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps)  [Restore-SPSite](/powershell/module/sharepoint-server/Restore-SPSite?view=sharepoint-ps)  |
|**Retractsolution**  |[Uninstall-SPSolution](/powershell/module/sharepoint-server/Uninstall-SPSolution?view=sharepoint-ps)  |
|**Retractwppack**  |None   |
|**Runcontentdeploymentjob**  |[Start-SPContentDeploymentJob](/powershell/module/sharepoint-server/Start-SPContentDeploymentJob?view=sharepoint-ps)  |
|**Scanforfeatures**  |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps)  Use the **Scanforfeatures** parameter.   |
|**Setadminport**  |[Set-SPCentralAdministration](/powershell/module/sharepoint-server/Set-SPCentralAdministration?view=sharepoint-ps)  |
|**Setapppassword**  |[Set-SPApplicationCredentialKey](/powershell/module/sharepoint-server/Set-SPApplicationCredentialKey?view=sharepoint-ps) [Remove-SPApplicationCredentialKey](/powershell/module/sharepoint-server/Remove-SPApplicationCredentialKey?view=sharepoint-ps)  |
|**Setconfigdb**  |[Connect-SPConfigurationDatabase](/powershell/module/sharepoint-server/Connect-SPConfigurationDatabase?view=sharepoint-ps)  |
|**Setcontentdeploymentjobschedule**  |[Set-SPContentDeploymentJob](/powershell/module/sharepoint-server/Set-SPContentDeploymentJob?view=sharepoint-ps)  |
|**Setdataconnectionfileproperty**  |[Set-SPDataConnectionFile](/powershell/module/sharepoint-server/Set-SPDataConnectionFile?view=sharepoint-ps)  |
|**Setformtemplateproperty**  |[Set-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Set-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Setlogginglevel**  |[Set-SPLogLevel](/powershell/module/sharepoint-server/Set-SPLogLevel?view=sharepoint-ps)  |
|**Setosearchsetting**  |None   |
|**Setproperty**  |[Set-SPFarmConfig](/powershell/module/sharepoint-server/Set-SPFarmConfig?view=sharepoint-ps)  [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps)  [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps)  [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps)  [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps)  [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps)  |
|**Setqueryprocessoroptions**  |None   |
|**Setsitelock**  |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps)  Use the **LockState** parameter.   |
|**Setsiteuseraccountdirectorypath**  |[Get-SPSiteSubscription](/powershell/module/sharepoint-server/Get-SPSiteSubscription?view=sharepoint-ps)  [New-SPSiteSubscription](/powershell/module/sharepoint-server/New-SPSiteSubscription?view=sharepoint-ps)  [Remove-SPSiteSubscription](/powershell/module/sharepoint-server/Remove-SPSiteSubscription?view=sharepoint-ps)  |
|**Setworkflowconfig**  |[Set-SPWorkflowConfig](/powershell/module/sharepoint-server/Set-SPWorkflowConfig?view=sharepoint-ps)  |
|**Siteowner**  |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps)  |
|**Sync**  |[Update-SPProfileSync](/powershell/module/sharepoint-server/Update-SPProfileSync?view=sharepoint-ps) [Clear-SPContentDatabaseSyncData](/powershell/module/sharepoint-server/Clear-SPContentDatabaseSyncData?view=sharepoint-ps) [Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps) (with the -DaysSinceLastProfileSync parameter)  |
|**Syncsolution**  |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps)  Use the **Synchronize** parameter.   |
|**Unextendvs**  |[Remove-SPWebApplication](/powershell/module/sharepoint-server/Remove-SPWebApplication?view=sharepoint-ps)  |
|**Uninstallfeature**  |[Uninstall-SPFeature](/powershell/module/sharepoint-server/Uninstall-SPFeature?view=sharepoint-ps)  |
|**Unquiescefarm**  |None   |
|**Unquiesceformtemplate**  |[Start-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Start-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Unregistersecuritytrimmer**  |[Remove-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Remove-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps)  |
|**Unregisterwsswriter**  |None   |
|**Updateaccountpassword**  |[Set-SPManagedAccount](/powershell/module/sharepoint-server/Set-SPManagedAccount?view=sharepoint-ps)  |
|**Updatealerttemplates**  |None   |
|**Updatefarmcredentials**  |None   |
|**Upgrade**  |None   |
|**Upgradeformtemplate**  |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Upgradesolution**  |[Update-SPSolution](/powershell/module/sharepoint-server/Update-SPSolution?view=sharepoint-ps)  |
|**Upgradetargetwebapplication**  |None   |
|**Uploadformtemplate**  |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps)  |
|**Userrole**  |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps)  [Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps)  [New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps)  [Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps)  [Set-SPUser](/powershell/module/sharepoint-server/Set-SPUser?view=sharepoint-ps)  |
|**Verifyformtemplate**  |[Test-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Test-SPInfoPathFormTemplate?view=sharepoint-ps)  |
   
## See also

#### Other Resources

[Index of Microsoft PowerShell cmdlets for SharePoint Server](/powershell/module/sharepoint-server/?view=sharepoint-ps)

