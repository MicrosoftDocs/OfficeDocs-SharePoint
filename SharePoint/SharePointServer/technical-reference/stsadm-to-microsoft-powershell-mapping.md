---
title: "Stsadm to Microsoft PowerShell mapping in SharePoint Server"
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.date: 8/24/2017
ms.audience: ITPro
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
|**Stsadm operation** <br/> |**Windows PowerShell cmdlet** <br/> |
|**Activatefeature** <br/> |[Enable-SPFeature](/powershell/module/sharepoint-server/Enable-SPFeature?view=sharepoint-ps) <br/> |
|**Activateformtemplate** <br/> |[Enable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Enable-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Addalternatedomain** <br/> |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps) <br/> |
|**Addcontentdb** <br/> |[Mount-SPContentDatabase](/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps) <br/> [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps) <br/> |
|**Addexemptuseragent** <br/> |[Add-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Add-SPInfoPathUserAgent?view=sharepoint-ps) <br/> |
|**Addpath** <br/> |[New-SPManagedPath](/powershell/module/sharepoint-server/New-SPManagedPath?view=sharepoint-ps) <br/> |
|**Addpermissionpolicy** <br/> |None  <br/> |
|**Addsolution** <br/> |[Add-SPSolution](/powershell/module/sharepoint-server/Add-SPSolution?view=sharepoint-ps) <br/> |
|**Addtemplate** <br/> |None  <br/> |
|**Adduser** <br/> |[New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps) <br/> |
|**Addwppack** <br/> |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps) <br/> |
|**Addzoneurl** <br/> |[New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps) <br/> |
|**Allowuserformwebserviceproxy** <br/> |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps) <br/> Use the **AllowForUserForms** and **Identity** parameters.  <br/> |
|**Allowwebserviceproxy** <br/> |[Set-SPInfoPathWebServiceProxy](/powershell/module/sharepoint-server/Set-SPInfoPathWebServiceProxy?view=sharepoint-ps) <br/> Use the **AllowWebServiceProxy** and **Identity** parameters.  <br/> |
|**Authentication** <br/> |[Set-SPWebApplication](/powershell/module/sharepoint-server/Set-SPWebApplication?view=sharepoint-ps) <br/> Use the **AuthenticationMethod** or **AuthenticationProvider** parameters.  <br/> |
|**Backup** <br/> |[Backup-SPConfigurationDatabase](/powershell/module/sharepoint-server/Backup-SPConfigurationDatabase?view=sharepoint-ps) <br/> [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps) <br/> [Backup-SPSite](/powershell/module/sharepoint-server/Backup-SPSite?view=sharepoint-ps) <br/> |
|**Backuphistory** <br/> |[Get-SPBackupHistory](/powershell/module/sharepoint-server/Get-SPBackupHistory?view=sharepoint-ps) <br/> |
|**Binddrservice** <br/> |None  <br/> |
|**Blockedfilelist** <br/> |None  <br/> |
|**Canceldeployment** <br/> |None  <br/> |
|**Changepermissionpolicy** <br/> |None  <br/> |
|**Copyappbincontent** <br/> |None  <br/> |
|**Createadminvs** <br/> |[New-SPCentralAdministration](/powershell/module/sharepoint-server/New-SPCentralAdministration?view=sharepoint-ps) <br/> |
|**Creategroup** <br/> |None  <br/> |
|**Createsite** <br/> |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps) <br/> |
|**Createsiteinnewdb** <br/> |[New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps) Use the **ContentDatabase** parameter.  <br/> [New-SPContentDatabase](/powershell/module/sharepoint-server/New-SPContentDatabase?view=sharepoint-ps) <br/> |
|**Createweb** <br/> |[New-SPWeb](/powershell/module/sharepoint-server/New-SPWeb?view=sharepoint-ps) <br/> |
|**Databaserepair** <br/> |None  <br/> |
|**Deactivatefeature** <br/> |[Disable-SPFeature](/powershell/module/sharepoint-server/Disable-SPFeature?view=sharepoint-ps) <br/> |
|**Deactivateformtemplate** <br/> |[Disable-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Disable-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Deleteadminvs** <br/> |None  <br/> |
|**Deletealternatedomain** <br/> |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps) <br/> |
|**Deleteconfigdb** <br/> |[Remove-SPConfigurationDatabase](/powershell/module/sharepoint-server/Remove-SPConfigurationDatabase?view=sharepoint-ps) <br/> |
|**Deletecontentdb** <br/> |[Dismount-SPContentDatabase](/powershell/module/sharepoint-server/Dismount-SPContentDatabase?view=sharepoint-ps
) <br/> |
|**Deletegroup** <br/> |None  <br/> |
|**Deletepath** <br/> |[Remove-SPManagedPath](/powershell/module/sharepoint-server/Remove-SPManagedPath?view=sharepoint-ps) <br/> |
|**Deletepermissionpolicy** <br/> |None  <br/> |
|**Deletesite** <br/> |[Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps) <br/> |
|**Deletesolution** <br/> |[Remove-SPSolution](/powershell/module/sharepoint-server/Remove-SPSolution?view=sharepoint-ps) <br/> |
|**Deletetemplate** <br/> |None  <br/> |
|**Deleteuser** <br/> |[Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps) <br/> |
|**Deleteweb** <br/> |[Remove-SPWeb](/powershell/module/sharepoint-server/Remove-SPWeb?view=sharepoint-ps) <br/> |
|**Deletewppack** <br/> |[Uninstall-SPWebPartPack](/powershell/module/sharepoint-server/Uninstall-SPWebPartPack?view=sharepoint-ps) <br/> |
|**Deletezoneurl** <br/> |[Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps) <br/> |
|**Deploysolution** <br/> |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps) <br/> |
|**Deploywppack** <br/> |[Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps) <br/> |
|**Disablessc** <br/> |None  <br/> |
|**Displaysolution** <br/> |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps) <br/> |
|**Editcontentdeploymentpath** <br/> |[Set-SPContentDeploymentPath](/powershell/module/sharepoint-server/Set-SPContentDeploymentPath?view=sharepoint-ps) <br/> |
|**Email** <br/> |None  <br/> |
|**Enablessc** <br/> |None  <br/> |
|**Enumalternatedomains** <br/> |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps) <br/> |
|**Enumcontentdbs** <br/> |[Get-SPContentDatabase](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps) <br/> |
|**Enumdataconnectionfiledependants** <br/> |[Get-SPDataConnectionFileDependent](/powershell/module/sharepoint-server/Get-SPDataConnectionFileDependent?view=sharepoint-ps) <br/> |
|**Enumdataconnectionfiles** <br/> |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps) <br/> |
|**Enumdeployments** <br/> |None  <br/> |
|**Enumexemptuseragents** <br/> |[Get-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Get-SPInfoPathUserAgent?view=sharepoint-ps) <br/> |
|**Enumformtemplates** <br/> |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Enumgroups** <br/> |None  <br/> |
|**Enumroles** <br/> |None  <br/> |
|**Enumservices** <br/> |[Get-SPServiceInstance](/powershell/module/sharepoint-server/Get-SPServiceInstance?view=sharepoint-ps) <br/> |
|**Enumsites** <br/> |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps) (To run this cmdlet, you must be a member of the Farm Administrators group.)  <br/> [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps) (To run this cmdlet, you must be a local administrator on the computer where SharePoint Server is installed.)  <br/> |
|**Enumsolutions** <br/> |[Get-SPSolution](/powershell/module/sharepoint-server/Get-SPSolution?view=sharepoint-ps) <br/> |
|**Enumsubwebs** <br/> |[Get-SPWeb](/powershell/module/sharepoint-server/Get-SPWeb?view=sharepoint-ps) <br/> |
|**Enumtemplates** <br/> |[Get-SPWebTemplate](/powershell/module/sharepoint-server/Get-SPWebTemplate?view=sharepoint-ps) <br/> |
|**Enumusers** <br/> |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps) <br/> |
|**Enumwppacks** <br/> |[Get-SPWebPartPack](/powershell/module/sharepoint-server/Get-SPWebPartPack?view=sharepoint-ps) <br/> |
|**Enumzoneurls** <br/> |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps) <br/> |
|**Execadmsvcjobs** <br/> |[Start-SPAdminJob](/powershell/module/sharepoint-server/Start-SPAdminJob?view=sharepoint-ps) <br/> |
|**Export** <br/> |[Export-SPWeb](/powershell/module/sharepoint-server/Export-SPWeb?view=sharepoint-ps) <br/> |
|**Extendvs** <br/> |[New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps) <br/> |
|**Extendvsinwebfarm** <br/> |[New-SPWebApplicationExtension](/powershell/module/sharepoint-server/New-SPWebApplicationExtension?view=sharepoint-ps) <br/> |
|**Forcedeletelist** <br/> |None  <br/> |
|**Getadminport** <br/> |[Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps) <br/> Use the following syntax:  <br/> Get-SPWebApplication -IncludeCentralAdministration | ? {$_.IsAdministrationWebApplication -eq $true}|
|**Getdataconnectionfileproperty** property  <br/> |[Get-SPDataConnectionFile](/powershell/module/sharepoint-server/Get-SPDataConnectionFile?view=sharepoint-ps) <br/> Use the following syntax:  <br/> Get-SPDataConnectionFile | where {$_.Name -eq "dataConFileName"} | format-list|
|**Getformtemplateproperty** property  <br/> |[Get-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Get-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> Use the following syntax:  <br/> Get-SPInfoPathFormTemplate | where {$_.DisplayName -eq "formTemplateName"} | format-list|
|**Getosearchsetting** <br/> |None  <br/> |
|**Getproperty** <br/> |[Get-SPFarmConfig](/powershell/module/sharepoint-server/Get-SPFarmConfig?view=sharepoint-ps) <br/> [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps) <br/> [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps) <br/> [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps) <br/> [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps) <br/> [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps) <br/> |
|**Getsitelock** <br/> |[Get-SPSiteAdministration](/powershell/module/sharepoint-server/Get-SPSiteAdministration?view=sharepoint-ps) <br/> |
|**Getsiteuseraccountdirectorypath** <br/> |None  <br/> |
|**Geturlzone** <br/> |[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps) <br/> |
|**Import** <br/> |[Import-SPWeb](/powershell/module/sharepoint-server/import-spweb?view=sharepoint-ps) <br/> |
|**Installfeature** <br/> |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps) <br/> |
|**Listlogginglevels** <br/> |[Get-SPLogLevel](/powershell/module/sharepoint-server/Get-SPLogLevel?view=sharepoint-ps) <br/> |
|**Listqueryprocessoroptions** <br/> |None  <br/> |
|**Listregisteredsecuritytrimmers** <br/> |[Get-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps) <br/> |
|**Localupgradestatus** <br/> |None  <br/> |
|**Managepermissionpolicylevel** <br/> |None  <br/> |
|**Mergecontentdbs** <br/> |[Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps) <br/> |
|**Migrateuser** <br/> |[Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps) <br/> |
|**Osearch** <br/> |For the **Osearch** parameters **farmcontactemail**, **farmperformancelevel**, **farmserviceaccount**, and **farmservicepassword**, use the [Get-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchService?view=sharepoint-ps) and [Set-SPEnterpriseSearchService](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchService?view=sharepoint-ps) cmdlets.  <br/> For the **Osearch** parameters **start** and **stop**, use the [Start-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Start-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) and [Stop-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Stop-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) cmdlets, respectively.  <br/> For the **Osearch** parameter **defaultindexlocation**, use the [Get-SPEnterpriseSearchServiceInstance](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceInstance?view=sharepoint-ps) cmdlet.  <br/> |
|**Osearchdiacriticsensitive** <br/> |Use the [Get-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Get-SPEnterpriseSearchServiceApplication?view=sharepoint-ps) cmdlet to retrieve the specific Search service application, and then use **DiacriticSensitive** parameter from the [Set-SPEnterpriseSearchServiceApplication](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchServiceApplication?view=sharepoint-ps) cmdlet.  <br/> |
|**Profilechangelog** <br/> |None.  <br/> However, you can use the Stsadm **profilechangelog** operation if you replace the Shared Services Provider (SSP) name with the service application (SA) name:  <br/> ```stsadm -o profilechangelog-title <SA name>-daysofhistory <number of days>-generateanniversaries```  <br/> |
|**Provisionservice** <br/> |[Start-SPServiceInstance](/powershell/module/sharepoint-server/Start-SPServiceInstance?view=sharepoint-ps) <br/> |
|**Quiescefarm** <br/> |None  <br/> |
|**Quiescefarmstatus** <br/> |None  <br/> |
|**Quiesceformtemplate** <br/> |[Stop-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Stop-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Reconvertallformtemplates** <br/> |[Update-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Update-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Refreshdms** <br/> |None  <br/> |
|**Refreshsitedms** <br/> |None  <br/> |
|**Registersecuritytrimmer** <br/> |[New-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/New-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps) <br/> |
|**Registerwsswriter** <br/> |None  <br/> |
|**Removedataconnectionfile** <br/> |[Uninstall-SPDataConnectionFile](/powershell/module/sharepoint-server/Uninstall-SPDataConnectionFile?view=sharepoint-ps) <br/> |
|**Removedrservice** <br/> |None  <br/> |
|**Removeexemptuseragent** <br/> |[Remove-SPInfoPathUserAgent](/powershell/module/sharepoint-server/Remove-SPInfoPathUserAgent?view=sharepoint-ps) <br/> |
|**Removeformtemplate** <br/> |[Uninstall-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Uninstall-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Removesolutiondeploymentlock** <br/> |None  <br/> |
|**Renameserver** <br/> |[Rename-SPServer](/powershell/module/sharepoint-server/Rename-SPServer?view=sharepoint-ps) <br/> |
|**Renamesite** <br/> |[Set-SPSite](/powershell/module/sharepoint-server/Set-SPSite?view=sharepoint-ps) <br/> Use the **Url** parameter.  <br/> |
|**Renameweb** <br/> |[Set-SPWeb](/powershell/module/sharepoint-server/Set-SPWeb?view=sharepoint-ps) <br/> Use the **RelativeUrl** parameter.  <br/> |
|**Restore** <br/> |[Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps) <br/> [Restore-SPSite](/powershell/module/sharepoint-server/Restore-SPSite?view=sharepoint-ps) <br/> |
|**Retractsolution** <br/> |[Uninstall-SPSolution](/powershell/module/sharepoint-server/Uninstall-SPSolution?view=sharepoint-ps) <br/> |
|**Retractwppack** <br/> |None  <br/> |
|**Runcontentdeploymentjob** <br/> |[Start-SPContentDeploymentJob](/powershell/module/sharepoint-server/Start-SPContentDeploymentJob?view=sharepoint-ps) <br/> |
|**Scanforfeatures** <br/> |[Install-SPFeature](/powershell/module/sharepoint-server/Install-SPFeature?view=sharepoint-ps) <br/> Use the **Scanforfeatures** parameter.  <br/> |
|**Setadminport** <br/> |[Set-SPCentralAdministration](/powershell/module/sharepoint-server/Set-SPCentralAdministration?view=sharepoint-ps) <br/> |
|**Setapppassword** <br/> |None  <br/> |
|**Setconfigdb** <br/> |[Connect-SPConfigurationDatabase](/powershell/module/sharepoint-server/Connect-SPConfigurationDatabase?view=sharepoint-ps) <br/> |
|**Setcontentdeploymentjobschedule** <br/> |[Set-SPContentDeploymentJob](/powershell/module/sharepoint-server/Set-SPContentDeploymentJob?view=sharepoint-ps) <br/> |
|**Setdataconnectionfileproperty** <br/> |[Set-SPDataConnectionFile](/powershell/module/sharepoint-server/Set-SPDataConnectionFile?view=sharepoint-ps) <br/> |
|**Setformtemplateproperty** <br/> |[Set-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Set-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Setlogginglevel** <br/> |[Set-SPLogLevel](/powershell/module/sharepoint-server/Set-SPLogLevel?view=sharepoint-ps) <br/> |
|**Setosearchsetting** <br/> |None  <br/> |
|**Setproperty** <br/> |[Set-SPFarmConfig](/powershell/module/sharepoint-server/Set-SPFarmConfig?view=sharepoint-ps) <br/> [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps) <br/> [Disable-SPTimerJob](/powershell/module/sharepoint-server/Disable-SPTimerJob?view=sharepoint-ps) <br/> [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps) <br/> [Set-SPTimerJob](/powershell/module/sharepoint-server/Set-SPTimerJob?view=sharepoint-ps) <br/> [Start-SPTimerJob](/powershell/module/sharepoint-server/Start-SPTimerJob?view=sharepoint-ps) <br/> |
|**Setqueryprocessoroptions** <br/> |None  <br/> |
|**Setsitelock** <br/> |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps) <br/> Use the **LockState** parameter.  <br/> |
|**Setsiteuseraccountdirectorypath** <br/> |[Get-SPSiteSubscription](/powershell/module/sharepoint-server/Get-SPSiteSubscription?view=sharepoint-ps) <br/> [New-SPSiteSubscription](/powershell/module/sharepoint-server/New-SPSiteSubscription?view=sharepoint-ps) <br/> [Remove-SPSiteSubscription](/powershell/module/sharepoint-server/Remove-SPSiteSubscription?view=sharepoint-ps) <br/> |
|**Setworkflowconfig** <br/> |[Set-SPWorkflowConfig](/powershell/module/sharepoint-server/Set-SPWorkflowConfig?view=sharepoint-ps) <br/> |
|**Siteowner** <br/> |[Set-SPSiteAdministration](/powershell/module/sharepoint-server/Set-SPSiteAdministration?view=sharepoint-ps) <br/> |
|**Syncsolution** <br/> |[Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps) <br/> Use the **Synchronize** parameter.  <br/> |
|**Unextendvs** <br/> |[Remove-SPWebApplication](/powershell/module/sharepoint-server/Remove-SPWebApplication?view=sharepoint-ps) <br/> |
|**Uninstallfeature** <br/> |[Uninstall-SPFeature](/powershell/module/sharepoint-server/Uninstall-SPFeature?view=sharepoint-ps) <br/> |
|**Unquiescefarm** <br/> |None  <br/> |
|**Unquiesceformtemplate** <br/> |[Start-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Start-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Unregistersecuritytrimmer** <br/> |[Remove-SPEnterpriseSearchSecurityTrimmer](/powershell/module/sharepoint-server/Remove-SPEnterpriseSearchSecurityTrimmer?view=sharepoint-ps) <br/> |
|**Unregisterwsswriter** <br/> |None  <br/> |
|**Updateaccountpassword** <br/> |[Set-SPManagedAccount](/powershell/module/sharepoint-server/Set-SPManagedAccount?view=sharepoint-ps) <br/> |
|**Updatealerttemplates** <br/> |None  <br/> |
|**Updatefarmcredentials** <br/> |None  <br/> |
|**Upgrade** <br/> |None  <br/> |
|**Upgradeformtemplate** <br/> |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Upgradesolution** <br/> |[Update-SPSolution](/powershell/module/sharepoint-server/Update-SPSolution?view=sharepoint-ps) <br/> |
|**Upgradetargetwebapplication** <br/> |None  <br/> |
|**Uploadformtemplate** <br/> |[Install-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Install-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
|**Userrole** <br/> |[Get-SPUser](/powershell/module/sharepoint-server/Get-SPUser?view=sharepoint-ps) <br/> [Move-SPUser](/powershell/module/sharepoint-server/Move-SPUser?view=sharepoint-ps) <br/> [New-SPUser](/powershell/module/sharepoint-server/New-SPUser?view=sharepoint-ps) <br/> [Remove-SPUser](/powershell/module/sharepoint-server/Remove-SPUser?view=sharepoint-ps) <br/> [Set-SPUser](/powershell/module/sharepoint-server/Set-SPUser?view=sharepoint-ps) <br/> |
|**Verifyformtemplate** <br/> |[Test-SPInfoPathFormTemplate](/powershell/module/sharepoint-server/Test-SPInfoPathFormTemplate?view=sharepoint-ps) <br/> |
   
## See also

#### Other Resources

[Index of Microsoft PowerShell cmdlets for SharePoint Server](/powershell/module/sharepoint-server/?view=sharepoint-ps)

