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

description: "Summary: Lists Stsadm operations and their equivalent PowerShell cmdlets."
---

# Stsadm to Microsoft PowerShell mapping in SharePoint Server

 **Summary:** Lists Stsadm operations and their equivalent PowerShell cmdlets. 
  
 Where there is no one-to-one mapping between the operations and cmdlets, the table lists the specific PowerShell parameters you must use to get the same functionality. 
  
## 

|||
|:-----|:-----|
|**Stsadm operation** <br/> |**Windows PowerShell cmdlet** <br/> |
|**Activatefeature** <br/> |[Enable-SPFeature](http://technet.microsoft.com/library/9b68c192-b640-4cb8-8a92-a98008169b27.aspx) <br/> |
|**Activateformtemplate** <br/> |[Enable-SPInfoPathFormTemplate](http://technet.microsoft.com/library/0f487359-a8dd-4128-83f2-d575df1325c6.aspx) <br/> |
|**Addalternatedomain** <br/> |[New-SPAlternateUrl](http://technet.microsoft.com/library/450f057d-1cb8-4680-b28d-0db4d1b7e09c.aspx) <br/> |
|**Addcontentdb** <br/> |[Mount-SPContentDatabase](http://technet.microsoft.com/library/20d1bc07-805c-44d3-a278-e2793370e237.aspx) <br/> [New-SPContentDatabase](http://technet.microsoft.com/library/18cf18cd-8fb7-4561-be71-41c767f27b51.aspx) <br/> |
|**Addexemptuseragent** <br/> |[Add-SPInfoPathUserAgent](http://technet.microsoft.com/library/3870f83e-0f93-4c4f-9175-69aad8baad14.aspx) <br/> |
|**Addpath** <br/> |[New-SPManagedPath](http://technet.microsoft.com/library/5d30deac-e368-4137-89b5-a20c0785b2a4.aspx) <br/> |
|**Addpermissionpolicy** <br/> |None  <br/> |
|**Addsolution** <br/> |[Add-SPSolution](http://technet.microsoft.com/library/0c64c1ac-39c0-4d5e-923f-27d0c48b006a.aspx) <br/> |
|**Addtemplate** <br/> |None  <br/> |
|**Adduser** <br/> |[New-SPUser](http://technet.microsoft.com/library/b8d7f8df-d5df-4497-a55b-dbe56b1c6fbb.aspx) <br/> |
|**Addwppack** <br/> |[Install-SPWebPartPack](http://technet.microsoft.com/library/b4245f30-c369-4b91-b4bd-1048a2abd384.aspx) <br/> |
|**Addzoneurl** <br/> |[New-SPAlternateUrl](http://technet.microsoft.com/library/450f057d-1cb8-4680-b28d-0db4d1b7e09c.aspx) <br/> |
|**Allowuserformwebserviceproxy** <br/> |[Set-SPInfoPathWebServiceProxy](http://technet.microsoft.com/library/c4e4639e-cfc0-4bf2-8f6a-de3e09c3080c.aspx) <br/> Use the **AllowForUserForms** and **Identity** parameters.  <br/> |
|**Allowwebserviceproxy** <br/> |[Set-SPInfoPathWebServiceProxy](http://technet.microsoft.com/library/c4e4639e-cfc0-4bf2-8f6a-de3e09c3080c.aspx) <br/> Use the **AllowWebServiceProxy** and **Identity** parameters.  <br/> |
|**Authentication** <br/> |[Set-SPWebApplication](http://technet.microsoft.com/library/0dd61e54-0e77-44b3-86c5-fabc128efa7b.aspx) <br/> Use the **AuthenticationMethod** or **AuthenticationProvider** parameters.  <br/> |
|**Backup** <br/> |[Backup-SPConfigurationDatabase](http://technet.microsoft.com/library/28ddc176-1b7f-47dd-868f-39b7c403a900.aspx) <br/> [Backup-SPFarm](http://technet.microsoft.com/library/c37704b5-5361-4090-a84d-fcdd17bbe345.aspx) <br/> [Backup-SPSite](http://technet.microsoft.com/library/d4c31a1a-82a7-425f-b1bb-22e70bedd338.aspx) <br/> |
|**Backuphistory** <br/> |[Get-SPBackupHistory](http://technet.microsoft.com/library/bc3a96db-3cc8-4991-a602-10204371047d.aspx) <br/> |
|**Binddrservice** <br/> |None  <br/> |
|**Blockedfilelist** <br/> |None  <br/> |
|**Canceldeployment** <br/> |None  <br/> |
|**Changepermissionpolicy** <br/> |None  <br/> |
|**Copyappbincontent** <br/> |None  <br/> |
|**Createadminvs** <br/> |[New-SPCentralAdministration](http://technet.microsoft.com/library/b51e3b8d-b3de-4c35-bcb7-c0ade288c0e4.aspx) <br/> |
|**Creategroup** <br/> |None  <br/> |
|**Createsite** <br/> |[New-SPSite](http://technet.microsoft.com/library/ebdadc86-0cda-49b7-a84a-5cfc6b4506b3.aspx) <br/> |
|**Createsiteinnewdb** <br/> |[New-SPSite](http://technet.microsoft.com/library/ebdadc86-0cda-49b7-a84a-5cfc6b4506b3.aspx) Use the **ContentDatabase** parameter.  <br/> [New-SPContentDatabase](http://technet.microsoft.com/library/18cf18cd-8fb7-4561-be71-41c767f27b51.aspx) <br/> |
|**Createweb** <br/> |[New-SPWeb](http://technet.microsoft.com/library/1ea28725-5b75-49f9-b69c-5ff0edf31459.aspx) <br/> |
|**Databaserepair** <br/> |None  <br/> |
|**Deactivatefeature** <br/> |[Disable-SPFeature](http://technet.microsoft.com/library/c10fbc69-088c-4e49-9005-fde54c035f23.aspx) <br/> |
|**Deactivateformtemplate** <br/> |[Disable-SPInfoPathFormTemplate](http://technet.microsoft.com/library/1e8e306a-4a37-4fae-a9ef-551c0c9b8b72.aspx) <br/> |
|**Deleteadminvs** <br/> |None  <br/> |
|**Deletealternatedomain** <br/> |[Remove-SPAlternateUrl](http://technet.microsoft.com/library/25af02dd-ae9f-4ec0-a099-3c6cd38f2187.aspx) <br/> |
|**Deleteconfigdb** <br/> |[Remove-SPConfigurationDatabase](http://technet.microsoft.com/library/10bab257-a628-4632-8d2f-7bb48bff8a4a.aspx) <br/> |
|**Deletecontentdb** <br/> |[Dismount-SPContentDatabase](http://technet.microsoft.com/library/89eea901-8d3f-4d4d-9638-941a1cafe259.aspx) <br/> |
|**Deletegroup** <br/> |None  <br/> |
|**Deletepath** <br/> |[Remove-SPManagedPath](http://technet.microsoft.com/library/6b6daf4a-4102-4583-9da7-9f0433d87b19.aspx) <br/> |
|**Deletepermissionpolicy** <br/> |None  <br/> |
|**Deletesite** <br/> |[Remove-SPSite](http://technet.microsoft.com/library/f2c49315-8eed-49ec-8a32-dc15a008d0dc.aspx) <br/> |
|**Deletesolution** <br/> |[Remove-SPSolution](http://technet.microsoft.com/library/862985c6-480b-49e7-926b-8497235bcba2.aspx) <br/> |
|**Deletetemplate** <br/> |None  <br/> |
|**Deleteuser** <br/> |[Remove-SPUser](http://technet.microsoft.com/library/cc60e125-781c-45bb-8e91-896fe8a230c1.aspx) <br/> |
|**Deleteweb** <br/> |[Remove-SPWeb](http://technet.microsoft.com/library/c9bc8078-626a-4838-b12b-21f1bb832935.aspx) <br/> |
|**Deletewppack** <br/> |[Uninstall-SPWebPartPack](http://technet.microsoft.com/library/8103c7d5-3b5b-4281-b9b6-e5ad93d3e2ef.aspx) <br/> |
|**Deletezoneurl** <br/> |[Remove-SPAlternateUrl](http://technet.microsoft.com/library/25af02dd-ae9f-4ec0-a099-3c6cd38f2187.aspx) <br/> |
|**Deploysolution** <br/> |[Install-SPSolution](http://technet.microsoft.com/library/0133c53b-70c4-4dff-a2ae-3c94759ed25d.aspx) <br/> |
|**Deploywppack** <br/> |[Install-SPWebPartPack](http://technet.microsoft.com/library/b4245f30-c369-4b91-b4bd-1048a2abd384.aspx) <br/> |
|**Disablessc** <br/> |None  <br/> |
|**Displaysolution** <br/> |[Get-SPSolution](http://technet.microsoft.com/library/88111c7a-9d56-40da-a766-a8ea1945c697.aspx) <br/> |
|**Editcontentdeploymentpath** <br/> |[Set-SPContentDeploymentPath](http://technet.microsoft.com/library/e68331f6-1f2c-4559-a7ea-24ea033f8244.aspx) <br/> |
|**Email** <br/> |None  <br/> |
|**Enablessc** <br/> |None  <br/> |
|**Enumalternatedomains** <br/> |[Get-SPAlternateURL](http://technet.microsoft.com/library/ea38119d-a535-48a3-b498-9daa443399fb.aspx) <br/> |
|**Enumcontentdbs** <br/> |[Get-SPContentDatabase](http://technet.microsoft.com/library/a4a83bb0-0bab-4cad-9b59-0fd89a16f57b.aspx) <br/> |
|**Enumdataconnectionfiledependants** <br/> |[Get-SPDataConnectionFileDependent](http://technet.microsoft.com/library/41cb3e6e-aedd-47dd-945b-a72b800013a6.aspx) <br/> |
|**Enumdataconnectionfiles** <br/> |[Get-SPDataConnectionFile](http://technet.microsoft.com/library/3bb713ab-3824-4113-9086-0f9624f23544.aspx) <br/> |
|**Enumdeployments** <br/> |None  <br/> |
|**Enumexemptuseragents** <br/> |[Get-SPInfoPathUserAgent](http://technet.microsoft.com/library/fef7e923-ac38-4054-aa7b-cd1f143d487e.aspx) <br/> |
|**Enumformtemplates** <br/> |[Get-SPInfoPathFormTemplate](http://technet.microsoft.com/library/f35004e0-8ded-4ec5-8fec-1cbd5151c42b.aspx) <br/> |
|**Enumgroups** <br/> |None  <br/> |
|**Enumroles** <br/> |None  <br/> |
|**Enumservices** <br/> |[Get-SPServiceInstance](http://technet.microsoft.com/library/14bbe36e-c73c-428a-955c-2c1e4d8a1d83.aspx) <br/> |
|**Enumsites** <br/> |[Get-SPSiteAdministration](http://technet.microsoft.com/library/a05769b1-7559-4af4-8524-5cbcc1bd4f25.aspx) (To run this cmdlet, you must be a member of the Farm Administrators group.)  <br/> [Get-SPSite](http://technet.microsoft.com/library/f3422bf4-0f9b-4f22-94c8-2a0606a31b16.aspx) (To run this cmdlet, you must be a local administrator on the computer where SharePoint Server is installed.)  <br/> |
|**Enumsolutions** <br/> |[Get-SPSolution](http://technet.microsoft.com/library/88111c7a-9d56-40da-a766-a8ea1945c697.aspx) <br/> |
|**Enumsubwebs** <br/> |[Get-SPWeb](http://technet.microsoft.com/library/9bf9284f-e3b9-439d-8a5f-74020e1eccaf.aspx) <br/> |
|**Enumtemplates** <br/> |[Get-SPWebTemplate](http://technet.microsoft.com/library/dfd10bac-c304-4f3f-bea9-eb0af5f96df5.aspx) <br/> |
|**Enumusers** <br/> |[Get-SPUser](http://technet.microsoft.com/library/1ec026e1-2480-4c31-bc23-3d0692d51ef9.aspx) <br/> |
|**Enumwppacks** <br/> |[Get-SPWebPartPack](http://technet.microsoft.com/library/a002b0f1-0c9c-4be6-b8ff-cb42b7b1dc29.aspx) <br/> |
|**Enumzoneurls** <br/> |[Get-SPAlternateURL](http://technet.microsoft.com/library/ea38119d-a535-48a3-b498-9daa443399fb.aspx) <br/> |
|**Execadmsvcjobs** <br/> |[Start-SPAdminJob](http://technet.microsoft.com/library/a96146cd-9973-4680-9a0b-d91ec51200d5.aspx) <br/> |
|**Export** <br/> |[Export-SPWeb](http://technet.microsoft.com/library/cd85bf19-6f24-4f13-bd9c-37bbf279ea2b.aspx) <br/> |
|**Extendvs** <br/> |[New-SPWebApplication](http://technet.microsoft.com/library/eaeb5bed-81e7-4275-b005-aa7fc465e6d5.aspx) <br/> |
|**Extendvsinwebfarm** <br/> |[New-SPWebApplicationExtension](http://technet.microsoft.com/library/0c407f36-6e3d-4213-bdb9-8298fa0c761c.aspx) <br/> |
|**Forcedeletelist** <br/> |None  <br/> |
|**Getadminport** <br/> |[Get-SPWebApplication](http://technet.microsoft.com/library/11d6521f-f99c-433e-9ab5-7cf9e953457a.aspx) <br/> Use the following syntax:  <br/> Get-SPWebApplication -IncludeCentralAdministration | ? {$_.IsAdministrationWebApplication -eq $true}|
|**Getdataconnectionfileproperty** property  <br/> |[Get-SPDataConnectionFile](http://technet.microsoft.com/library/3bb713ab-3824-4113-9086-0f9624f23544.aspx) <br/> Use the following syntax:  <br/> Get-SPDataConnectionFile | where {$_.Name -eq "dataConFileName"} | format-list|
|**Getformtemplateproperty** property  <br/> |[Get-SPInfoPathFormTemplate](http://technet.microsoft.com/library/f35004e0-8ded-4ec5-8fec-1cbd5151c42b.aspx) <br/> Use the following syntax:  <br/> Get-SPInfoPathFormTemplate | where {$_.DisplayName -eq "formTemplateName"} | format-list|
|**Getosearchsetting** <br/> |None  <br/> |
|**Getproperty** <br/> |[Get-SPFarmConfig](http://technet.microsoft.com/library/83a26555-6b6e-4959-9a6a-bdef049de2a2.aspx) <br/> [Get-SPTimerJob](http://technet.microsoft.com/library/e2ec752d-7f04-457e-bc02-7213af5c14fe.aspx) <br/> [Disable-SPTimerJob](http://technet.microsoft.com/library/8d8d7ec5-3f09-4b7e-9124-8d0c0afeb637.aspx) <br/> [Enable-SPTimerJob](http://technet.microsoft.com/library/ca2ce54c-1a9a-46d5-8055-a1f87c30a99a.aspx) <br/> [Set-SPTimerJob](http://technet.microsoft.com/library/e40a6017-0bf0-4912-befb-3510084a0487.aspx) <br/> [Start-SPTimerJob](http://technet.microsoft.com/library/1cea3146-e267-476f-af0e-3b534ca14a80.aspx) <br/> |
|**Getsitelock** <br/> |[Get-SPSiteAdministration](http://technet.microsoft.com/library/a05769b1-7559-4af4-8524-5cbcc1bd4f25.aspx) <br/> |
|**Getsiteuseraccountdirectorypath** <br/> |None  <br/> |
|**Geturlzone** <br/> |[Get-SPAlternateURL](http://technet.microsoft.com/library/ea38119d-a535-48a3-b498-9daa443399fb.aspx) <br/> |
|**Import** <br/> |[Import-SPWeb](http://technet.microsoft.com/library/2ecc5b6e-1b23-4367-a966-b7bd3377db3a.aspx) <br/> |
|**Installfeature** <br/> |[Install-SPFeature](http://technet.microsoft.com/library/a1093d30-68a1-4c84-8454-967bda8d68b9.aspx) <br/> |
|**Listlogginglevels** <br/> |[Get-SPLogLevel](http://technet.microsoft.com/library/1bb57b3d-8bf3-4fb2-8ef2-dd3eafe3a899.aspx) <br/> |
|**Listqueryprocessoroptions** <br/> |None  <br/> |
|**Listregisteredsecuritytrimmers** <br/> |[Get-SPEnterpriseSearchSecurityTrimmer](http://technet.microsoft.com/library/60fd124a-e678-4440-9e37-852372a6d977.aspx) <br/> |
|**Localupgradestatus** <br/> |None  <br/> |
|**Managepermissionpolicylevel** <br/> |None  <br/> |
|**Mergecontentdbs** <br/> |[Move-SPSite](http://technet.microsoft.com/library/e3bf1b34-78b9-4643-b0dd-24444e3cffc5.aspx) <br/> |
|**Migrateuser** <br/> |[Move-SPUser](http://technet.microsoft.com/library/783cad23-5442-46b2-af98-79e0b8e4977d.aspx) <br/> |
|**Osearch** <br/> |For the **Osearch** parameters **farmcontactemail**, **farmperformancelevel**, **farmserviceaccount**, and **farmservicepassword**, use the [Get-SPEnterpriseSearchService](http://technet.microsoft.com/library/fcf865a8-b46b-44fb-89ba-f52e20876f6c.aspx) and [Set-SPEnterpriseSearchService](http://technet.microsoft.com/library/f8baccd0-21d2-40aa-b700-997ec7ca7011.aspx) cmdlets.  <br/> For the **Osearch** parameters **start** and **stop**, use the [Start-SPEnterpriseSearchServiceInstance](http://technet.microsoft.com/library/55060c1d-4024-438e-b31d-6854df8b00d5.aspx) and [Stop-SPEnterpriseSearchServiceInstance](http://technet.microsoft.com/library/985591b0-951f-4274-aead-a184398bba41.aspx) cmdlets, respectively.  <br/> For the **Osearch** parameter **defaultindexlocation**, use the [Get-SPEnterpriseSearchServiceInstance](http://technet.microsoft.com/library/309d98e8-a5fa-4cb5-b6e1-bf94380a8212.aspx) cmdlet.  <br/> |
|**Osearchdiacriticsensitive** <br/> |Use the [Get-SPEnterpriseSearchServiceApplication](http://technet.microsoft.com/library/b8030354-e62d-4723-a809-eb6cf8c301c5.aspx) cmdlet to retrieve the specific Search service application, and then use **DiacriticSensitive** parameter from the [Set-SPEnterpriseSearchServiceApplication](http://technet.microsoft.com/library/77868ee0-716d-48a4-81dc-016b28652710.aspx) cmdlet.  <br/> |
|**Profilechangelog** <br/> |None.  <br/> However, you can use the Stsadm **profilechangelog** operation if you replace the Shared Services Provider (SSP) name with the service application (SA) name:  <br/> ```stsadm -o profilechangelog-title <SA name>-daysofhistory <number of days>-generateanniversaries```  <br/> |
|**Provisionservice** <br/> |[Start-SPServiceInstance](http://technet.microsoft.com/library/fcb4a4f8-a95f-468e-918b-d9a2d736cd2d.aspx) <br/> |
|**Quiescefarm** <br/> |None  <br/> |
|**Quiescefarmstatus** <br/> |None  <br/> |
|**Quiesceformtemplate** <br/> |[Stop-SPInfoPathFormTemplate](http://technet.microsoft.com/library/b2795395-f293-4b17-aa1b-64ec46fb6856.aspx) <br/> |
|**Reconvertallformtemplates** <br/> |[Update-SPInfoPathFormTemplate](http://technet.microsoft.com/library/7095759f-3b6c-4279-a8b1-24a3174185e5.aspx) <br/> |
|**Refreshdms** <br/> |None  <br/> |
|**Refreshsitedms** <br/> |None  <br/> |
|**Registersecuritytrimmer** <br/> |[New-SPEnterpriseSearchSecurityTrimmer](http://technet.microsoft.com/library/493d9d19-ae43-43ce-b75f-916535881b35.aspx) <br/> |
|**Registerwsswriter** <br/> |None  <br/> |
|**Removedataconnectionfile** <br/> |[Uninstall-SPDataConnectionFile](http://technet.microsoft.com/library/5151855d-0051-4c98-8dc3-ce0843c5a69d.aspx) <br/> |
|**Removedrservice** <br/> |None  <br/> |
|**Removeexemptuseragent** <br/> |[Remove-SPInfoPathUserAgent](http://technet.microsoft.com/library/da48bb08-6aca-4138-b899-9f5a4be0a982.aspx) <br/> |
|**Removeformtemplate** <br/> |[Uninstall-SPInfoPathFormTemplate](http://technet.microsoft.com/library/da080f95-6bdf-415f-8c8b-f2fe927cd9cc.aspx) <br/> |
|**Removesolutiondeploymentlock** <br/> |None  <br/> |
|**Renameserver** <br/> |[Rename-SPServer](http://technet.microsoft.com/library/0e64ec82-f313-4af8-b3ca-c0f55e5d51f0.aspx) <br/> |
|**Renamesite** <br/> |[Set-SPSite](http://technet.microsoft.com/library/f8c7f0ac-52bf-4b79-a356-9d6e485a55aa.aspx) <br/> Use the **Url** parameter.  <br/> |
|**Renameweb** <br/> |[Set-SPWeb](http://technet.microsoft.com/library/7b21444f-7f4c-4155-8f0d-952b585e4524.aspx) <br/> Use the **RelativeUrl** parameter.  <br/> |
|**Restore** <br/> |[Restore-SPFarm](http://technet.microsoft.com/library/8e18ea80-0830-4ffa-b6b6-ad18a5a7ab3e.aspx) <br/> [Restore-SPSite](http://technet.microsoft.com/library/90f19a58-0455-470c-a8ee-3129fc341f62.aspx) <br/> |
|**Retractsolution** <br/> |[Uninstall-SPSolution](http://technet.microsoft.com/library/bc815ad1-cb94-4512-9ca2-891eb001f05b.aspx) <br/> |
|**Retractwppack** <br/> |None  <br/> |
|**Runcontentdeploymentjob** <br/> |[Start-SPContentDeploymentJob](http://technet.microsoft.com/library/d34e88ba-1f37-4611-92c8-1e67b41c5923.aspx) <br/> |
|**Scanforfeatures** <br/> |[Install-SPFeature](http://technet.microsoft.com/library/a1093d30-68a1-4c84-8454-967bda8d68b9.aspx) <br/> Use the **Scanforfeatures** parameter.  <br/> |
|**Setadminport** <br/> |[Set-SPCentralAdministration](http://technet.microsoft.com/library/a8bf87b6-18e6-4ba0-ada9-91ee9f4199ec.aspx) <br/> |
|**Setapppassword** <br/> |None  <br/> |
|**Setconfigdb** <br/> |[Connect-SPConfigurationDatabase](http://technet.microsoft.com/library/44ace210-aab1-4b4f-b133-0a302d89541b.aspx) <br/> |
|**Setcontentdeploymentjobschedule** <br/> |[Set-SPContentDeploymentJob](http://technet.microsoft.com/library/9dd46fa9-1110-4fd5-b890-6b0fc37dbe96.aspx) <br/> |
|**Setdataconnectionfileproperty** <br/> |[Set-SPDataConnectionFile](http://technet.microsoft.com/library/edca60a7-2028-4141-97e1-83125306fe3f.aspx) <br/> |
|**Setformtemplateproperty** <br/> |[Set-SPInfoPathFormTemplate](http://technet.microsoft.com/library/ba687ce1-4a54-4a27-ae22-5912e6b54e81.aspx) <br/> |
|**Setlogginglevel** <br/> |[Set-SPLogLevel](http://technet.microsoft.com/library/c8ede92a-f685-4140-8587-96700d1a45de.aspx) <br/> |
|**Setosearchsetting** <br/> |None  <br/> |
|**Setproperty** <br/> |[Set-SPFarmConfig](http://technet.microsoft.com/library/fc9fd625-0df1-467a-bd31-16b7e29fbca9.aspx) <br/> [Get-SPTimerJob](http://technet.microsoft.com/library/e2ec752d-7f04-457e-bc02-7213af5c14fe.aspx) <br/> [Disable-SPTimerJob](http://technet.microsoft.com/library/8d8d7ec5-3f09-4b7e-9124-8d0c0afeb637.aspx) <br/> [Enable-SPTimerJob](http://technet.microsoft.com/library/ca2ce54c-1a9a-46d5-8055-a1f87c30a99a.aspx) <br/> [Set-SPTimerJob](http://technet.microsoft.com/library/e40a6017-0bf0-4912-befb-3510084a0487.aspx) <br/> [Start-SPTimerJob](http://technet.microsoft.com/library/1cea3146-e267-476f-af0e-3b534ca14a80.aspx) <br/> |
|**Setqueryprocessoroptions** <br/> |None  <br/> |
|**Setsitelock** <br/> |[Set-SPSiteAdministration](http://technet.microsoft.com/library/35f784c0-f74b-49aa-b87d-3b7a3662dd1d.aspx) <br/> Use the **LockState** parameter.  <br/> |
|**Setsiteuseraccountdirectorypath** <br/> |[Get-SPSiteSubscription](http://technet.microsoft.com/library/d79fb60b-ba72-4187-bcb3-152d22368f71.aspx) <br/> [New-SPSiteSubscription](http://technet.microsoft.com/library/134f4d1a-28c0-4239-9e6e-4e886f877f1b.aspx) <br/> [Remove-SPSiteSubscription](http://technet.microsoft.com/library/ff9b0882-a5e1-40b4-bdd2-20d8f7dab1f8.aspx) <br/> |
|**Setworkflowconfig** <br/> |[Set-SPWorkflowConfig](http://technet.microsoft.com/library/876a4206-6c28-446e-9686-c8916c9bbfec.aspx) <br/> |
|**Siteowner** <br/> |[Set-SPSiteAdministration](http://technet.microsoft.com/library/35f784c0-f74b-49aa-b87d-3b7a3662dd1d.aspx) <br/> |
|**Syncsolution** <br/> |[Install-SPSolution](http://technet.microsoft.com/library/0133c53b-70c4-4dff-a2ae-3c94759ed25d.aspx) <br/> Use the **Synchronize** parameter.  <br/> |
|**Unextendvs** <br/> |[Remove-SPWebApplication](http://technet.microsoft.com/library/c9e9fca0-403a-4071-83ee-2cf7bdab0ed3.aspx) <br/> |
|**Uninstallfeature** <br/> |[Uninstall-SPFeature](http://technet.microsoft.com/library/2f3831e4-b964-4e0e-bcc5-02659fdc0bb7.aspx) <br/> |
|**Unquiescefarm** <br/> |None  <br/> |
|**Unquiesceformtemplate** <br/> |[Start-SPInfoPathFormTemplate](http://technet.microsoft.com/library/97fee306-a7b1-4761-8ce3-438f5f1814be.aspx) <br/> |
|**Unregistersecuritytrimmer** <br/> |[Remove-SPEnterpriseSearchSecurityTrimmer](http://technet.microsoft.com/library/5dd04c24-6a23-4092-b0ab-7a41f13831d9.aspx) <br/> |
|**Unregisterwsswriter** <br/> |None  <br/> |
|**Updateaccountpassword** <br/> |[Set-SPManagedAccount](http://technet.microsoft.com/library/320204fe-f72f-40c6-9b1f-e7a3ddb0aca3.aspx) <br/> |
|**Updatealerttemplates** <br/> |None  <br/> |
|**Updatefarmcredentials** <br/> |None  <br/> |
|**Upgrade** <br/> |None  <br/> |
|**Upgradeformtemplate** <br/> |[Install-SPInfoPathFormTemplate](http://technet.microsoft.com/library/b99f33e3-6f2b-43e0-9a35-1aea11337dfe.aspx) <br/> |
|**Upgradesolution** <br/> |[Update-SPSolution](http://technet.microsoft.com/library/7748591a-b137-48a2-84dd-fdd7727a938e.aspx) <br/> |
|**Upgradetargetwebapplication** <br/> |None  <br/> |
|**Uploadformtemplate** <br/> |[Install-SPInfoPathFormTemplate](http://technet.microsoft.com/library/b99f33e3-6f2b-43e0-9a35-1aea11337dfe.aspx) <br/> |
|**Userrole** <br/> |[Get-SPUser](http://technet.microsoft.com/library/1ec026e1-2480-4c31-bc23-3d0692d51ef9.aspx) <br/> [Move-SPUser](http://technet.microsoft.com/library/783cad23-5442-46b2-af98-79e0b8e4977d.aspx) <br/> [New-SPUser](http://technet.microsoft.com/library/b8d7f8df-d5df-4497-a55b-dbe56b1c6fbb.aspx) <br/> [Remove-SPUser](http://technet.microsoft.com/library/cc60e125-781c-45bb-8e91-896fe8a230c1.aspx) <br/> [Set-SPUser](http://technet.microsoft.com/library/a412b5e1-b330-4992-a10d-7593078684a7.aspx) <br/> |
|**Verifyformtemplate** <br/> |[Test-SPInfoPathFormTemplate](http://technet.microsoft.com/library/756307f4-2409-4059-9543-53979367f53e.aspx) <br/> |
   
## See also

#### Other Resources

[Index of Microsoft PowerShell cmdlets for SharePoint Server](https://technet.microsoft.com/en-us/library/ff678226%28v=office.16%29.aspx)

