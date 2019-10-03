---
title: "Document farm configuration settings in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 73d7f970-c378-4b31-92d5-48cdeb8075e6
description: "Learn how to document farm configuration settings in SharePoint Server."
---

# Document farm configuration settings in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can document your farm configuration settings in SharePoint Server by using PowerShell. 
  
Documenting configuration settings is important both so that you can create scripted deployments for your environment and so that you can quickly re-create a set of configurations if a failure were to occur.
  
    
## Using PowerShell to document farm configuration settings in SharePoint Server
<a name="proc1"> </a>

The following procedure describes how to create and run a PowerShell script for SharePoint Server. You can then use this script to restore the farm configuration settings if a failure were to occur.
  
 **To document SharePoint Server configuration settings by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050) (https://go.microsoft.com/fwlink/p/?LinkId=193050). 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Use a text editor, such as Notepad, to create a text file by pasting the following code into the file. The commands in the example create XML files that document the configurations of the Web applications and service applications in the current farm. Choose only those commands that are relevant to your environment.
    
  ```
  ##
  ## Common SharePoint configuration settings
  ##
  #Retrieve Web Application information. The default depth of 2 does not return much detail--we recommend that you use a depth of 4 for this cmdlet.
  Get-SPWebApplication | Export-Clixml .\WebAppFilename.xml -depth 4
  #Retrieve custom layout information. 
  Get-SPWebApplication | Get-SPCustomLayoutsPage | Export-Clixml .\Get-SPCustomLayoutsPage.xml
  #Determine how SharePoint designer access is configured.
  Get-SPWebApplication | Get-SPDesignerSettings  | Export-Clixml .\Get-SPDesignerSettings.xml
  #Retrieve information about alternate access mapping
  Get-SPAlternateURL  | Export-Clixml .\Get-SPAlternateURL.xml
  #Retrieve information about content databases
  Get-SPContentDatabase  | Export-Clixml .\Get-SPContentDatabase.xml
  #Retrieve database properties for each database
  Get-SPDatabase  | Export-Clixml .\Get-SPDatabase.xml
  #Retrieve information about all SharePoint Products installed in the farm, and the versions of all updates installed for each product.
  Get-SPProduct  | Export-Clixml .\Get-SPProduct.xml
  #Retrieve farm information
  Get-SPFarm  | Export-Clixml .\Get-SPFarm.xml
  Get-SPFarmConfig  | Export-Clixml .\Get-SPFarmConfig.xml
  #Retrieve information about the servers in the farm
  Get-SPServer  | Export-Clixml .\Get-SPServer.xml
  #Retrieve information about installed features
  Get-SPFeature  | Export-Clixml .\Get-SPFeature.xml
  #Retrieve information about globally-installed site templates
  Get-SPWebTemplate  | Export-Clixml .\Get-SPWebTemplate.xml
  #Retrieve information about deployed solutions
  Get-SPSolution  | Export-Clixml .\Get-SPSolution.xml
  #Retrieve information about sandboxed solutions deployed in a site collection
  Get-SPSite | Get-SPUserSolution  | Export-Clixml .\Get-SPUserSolution.xml
  #Retrieve information about claims authentication
  Get-SPTrustedIdentityTokenIssuer  | Export-Clixml .\Get-SPTrustedIdentityTokenIssuer.xml
  Get-SPTrustedServiceTokenIssuer  | Export-Clixml .\Get-SPTrustedServiceTokenIssuer.xml
  Get-SPTrustedRootAuthority  | Export-Clixml .\Get-SPTrustedRootAuthority.xml
  #Retrieve information about installed Help
  Get-SPHelpCollection  | Export-Clixml .\Get-SPHelpCollection.xml
  #Retrieve information about the logging levels that have been set
  Get-SPLogLevel  | Export-Clixml .\Get-SPLogLevel.xml
  #Retrieve information about the sites in the farm
  Get-SPSite  | Export-Clixml .\Get-SPSite.xml
  Get-SPSiteAdministration  | Export-Clixml .\Get-SPSiteAdministration.xml
  Get-SPSiteSubscription  | Export-Clixml .\Get-SPSiteSubscription.xml
  #Retrieve ULS logging information
  Get-SPDiagnosticConfig  | Export-Clixml .\Get-SPDiagnosticConfig.xml
  Get-SPDiagnosticsPerformanceCounter  | Export-Clixml .\Get-SPDiagnosticsPerformanceCounter.xml
  Get-SPDiagnosticsProvider  | Export-Clixml .\Get-SPDiagnosticsProvider.xml
  #Retrieve information about accounts registered in the configuration database
  Get-SPManagedAccount  | Export-Clixml .\Get-SPManagedAccount.xml
  Get-SPProcessAccount  | Export-Clixml .\Get-SPProcessAccount.xml
  Get-SPShellAdmin  | Export-Clixml .\Get-SPShellAdmin.xml
  #Retrieve specific information about the certificate authority
  Get-SPCertificateAuthority  | Export-Clixml .\Get-SPCertificateAuthority.xml
  Get-SPClaimProvider  | Export-Clixml .\Get-SPClaimProvider.xml
  Get-SPClaimProviderManager  | Export-Clixml .\Get-SPClaimProviderManager.xml
  #Retrieve information about content deployment jobs
  Get-SPContentDeploymentJob | Export-Clixml .\Get-SPContentDeploymentJob.xml
  Get-SPContentDeploymentPath | Export-Clixml .\Get-SPContentDeploymentPath.xml
  #Retrieve information about the Mobile Messaging account.
  Get-SPWebApplication | Get-SPMobileMessagingAccount  | Export-Clixml .\Get-SPMobileMessagingAccount.xml
  ##
  ##Common service infrastructure settings
  ##
  #Retrieve information about the service applications in the farm
  Get-SPServiceApplication  | Export-Clixml .\Get-SPServiceApplication.xml
  Get-SPServiceApplicationPool  | Export-Clixml .\Get-SPServiceApplicationPool.xml
  Get-SPServiceApplicationProxy  | Export-Clixml .\Get-SPServiceApplicationProxy.xml
  Get-SPServiceApplicationProxyGroup  | Export-Clixml .\Get-SPServiceApplicationProxyGroup.xml
  Get-SPServiceApplication | Get-SPServiceApplicationEndpoint  | Export-Clixml .\Get-SPServiceApplicationEndpoint.xml
  #Retrieve information about the services running in the farm
  Get-SPServiceInstance  | Export-Clixml .\Get-SPServiceInstance.xml
  #Retrieve information about InfoPath form services
  Get-SPInfoPathFormsService  | Export-Clixml .\Get-SPInfoPathFormsService.xml
  Get-SPInfoPathFormTemplate  | Export-Clixml .\Get-SPInfoPathFormTemplate.xml
  ###WARNING: The following cmdlet requires  run as administrator rights. 
  Get-SPInfoPathUserAgent  | Export-Clixml .\Get-SPInfoPathUserAgent.xml
  #Retrieve information about common Web service settings
  Get-SPServiceHostConfig  | Export-Clixml .\Get-SPServiceHostConfig.xml
  ##
  ## Common service application settings
  ##
  #Access Services
  #Retrieve specific information for the Access Services service application
  Get-SPAccessServiceApplication  | Export-Clixml .\Get-SPAccessServiceApplication.xml
  #Application Discovery and Load Balancer Service Application 
  Get-SPTopologyServiceApplication  | Export-Clixml .\Get-SPTopologyServiceApplication.xml
  Get-SPTopologyServiceApplicationProxy  | Export-Clixml .\Get-SPTopologyServiceApplicationProxy.xml
  #Business Data Connectivity Service
  #Retrieve information about data connection files. ###WARNING: The following cmdlet requires  run as administrator rights
  Get-SPDataConnectionFile | Export-Clixml .\Get-SPDataConnectionFile.xml
  ###WARNING: The following cmdlet requires  run as administrator rights
  Get-SPDataConnectionFile | Get-SPDataConnectionFileDependent  | Export-Clixml .\Get-SPDataConnectionFileDependent.xml
  #Excel Services Application
  #Note: An Excel service application must be provisioned for the following cmdlets to succeed. 
  Get-SPExcelServiceApplication | Get-SPExcelBlockedFileType  | Export-Clixml .\Get-SPExcelBlockedFileType.xml
  Get-SPExcelServiceApplication | Get-SPExcelDataConnectionLibrary  | Export-Clixml .\Get-SPExcelDataConnectionLibrary.xml
  Get-SPExcelServiceApplication | Get-SPExcelDataProvider  | Export-Clixml .\Get-SPExcelDataProvider.xml
  Get-SPExcelServiceApplication | Get-SPExcelFileLocation  | Export-Clixml .\Get-SPExcelFileLocation.xml
  Get-SPExcelServiceApplication | Export-Clixml .\Get-SPExcelServiceApplication.xml
  Get-SPExcelServiceApplication | Get-SPExcelUserDefinedFunction  | Export-Clixml .\Get-SPExcelUserDefinedFunction.xml
  Get-SPWebApplication | Get-SPInfoPathWebServiceProxy  | Export-Clixml .\Get-SPInfoPathWebServiceProxy.xml
  Get-SPWebApplication | Get-SPManagedPath  | Export-Clixml .\Get-SPManagedPath.xml
   
  #Managed Metadata Service
  #Note: A Managed Metadata service application must be provisioned for the following cmdlets to succeed. 
  Get-SPServiceApplication | ?{$_.TypeName -eq "Managed Metadata Service"} | %{$id = $_.Id;Get-SPMetadataServiceApplication -Id $_ | Export-Clixml .\Get-SPMetadataServiceApplication-$id.xml}
  Get-SPServiceApplicationProxy | ?{$_.TypeName -eq "Managed Metadata Service Connection"} | %{$id = $_.Id;Get-SPMetadataServiceApplicationProxy -Id $_ | Export-Clixml .\Get-SPMetadataServiceApplicationProxy-$id.xml}
  Get-SPSite | Get-SPTaxonomySession  | Export-Clixml .\Get-SPTaxonomySession.xml
  #PerformancePoint Service Application
  #Note: A PerformancePoint service application must be provisioned for the following cmdlets to succeed. 
  Get-SPPerformancePointServiceApplication | Export-Clixml .\Get-SPPerformancePointServiceApplication.xml
  Get-SPPerformancePointServiceApplication | Get-SPPerformancePointServiceApplicationTrustedLocation  | Export-Clixml .\Get-SPPerformancePointServiceApplicationTrustedLocation.xml
  #Search 
  #Retrieve search information
  #Note:  A Search service application must be provisioned for the following cmdlets to succeed. 
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchAdministrationComponent  | Export-Clixml .\Get-SPEnterpriseSearchAdministrationComponent.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlContentSource  | Export-Clixml .\Get-SPEnterpriseSearchCrawlContentSource.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlCustomConnector  | Export-Clixml .\Get-SPEnterpriseSearchCrawlCustomConnector.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlDatabase  | Export-Clixml .\Get-SPEnterpriseSearchCrawlDatabase.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlExtension  | Export-Clixml .\Get-SPEnterpriseSearchCrawlExtension.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlMapping  | Export-Clixml .\Get-SPEnterpriseSearchCrawlMapping.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchCrawlRule  | Export-Clixml .\Get-SPEnterpriseSearchCrawlRule.xml
  $searchApp = Get-SPEnterpriseSearchServiceApplication; Get-SPEnterpriseSearchExtendedClickThroughExtractorJobDefinition -SearchApplication $searchApp | Export-Clixml .\Get-SPEnterpriseSearchExtendedClickThroughExtractorJobDefinition.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchExtendedConnectorProperty  | Export-Clixml .\Get-SPEnterpriseSearchExtendedConnectorProperty.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchExtendedQueryProperty  | Export-Clixml .\Get-SPEnterpriseSearchExtendedQueryProperty.xml
  ###WARNING: The following command generates a 120MB file that records the out of the box settings###
  #Note: The Get-SPEnterpriseSearchQueryAuthority and Get-SPEnterpriseSearchQueryDemoted cmdlets require the Owner and SearchApplication parameters#
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchLanguageResourcePhrase  | Export-Clixml .\Get-SPEnterpriseSearchLanguageResourcePhrase.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchMetadataCategory  | Export-Clixml .\Get-SPEnterpriseSearchMetadataCategory.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchMetadataCrawledProperty  | Export-Clixml .\Get-SPEnterpriseSearchMetadataCrawledProperty.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchMetadataManagedProperty  | Export-Clixml .\Get-SPEnterpriseSearchMetadataManagedProperty.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchMetadataMapping  | Export-Clixml .\Get-SPEnterpriseSearchMetadataMapping.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchQueryAuthority  | Export-Clixml .\Get-SPEnterpriseSearchQueryAuthority.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchQueryDemoted  | Export-Clixml .\Get-SPEnterpriseSearchQueryDemoted.xml
   Get-SPEnterpriseSearchQueryAndSiteSettingsService  | Export-Clixml .\Get-SPEnterpriseSearchQueryAndSiteSettingsService.xml
  Get-SPEnterpriseSearchQueryAndSiteSettingsServiceInstance  | Export-Clixml .\Get-SPEnterpriseSearchQueryAndSiteSettingsServiceInstance.xml
  Get-SPEnterpriseSearchQueryAndSiteSettingsServiceProxy  | Export-Clixml .\Get-SPEnterpriseSearchQueryAndSiteSettingsServiceProxy.xml
  Get-SPEnterpriseSearchService  | Export-Clixml .\Get-SPEnterpriseSearchService.xml
  Get-SPEnterpriseSearchServiceInstance  | Export-Clixml .\Get-SPEnterpriseSearchServiceInstance.xml
  ###WARNING: The following command generates a file per site collection###
  #Note: The Get-SPEnterpriseSearchQuerySuggestionCandidates and Get-SPEnterpriseSearchRankingModel cmdlets require the Owner and SearchApplication parameters#
  Get-SPSite | %{$id = $_.Id;Get-SPEnterpriseSearchQueryKeyword -Site $_ | Export-Clixml .\Get-SPEnterpriseSearchQueryKeyword-$id.xml}
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchQueryScope  | Export-Clixml .\Get-SPEnterpriseSearchQueryScope.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchQueryScope | Get-SPEnterpriseSearchQueryScopeRule  | Export-Clixml .\Get-SPEnterpriseSearchQueryScopeRule.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchQuerySuggestionCandidates  | Export-Clixml .\Get-SPEnterpriseSearchQuerySuggestionCandidates.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchRankingModel  | Export-Clixml .\Get-SPEnterpriseSearchRankingModel.xml
  Get-SPEnterpriseSearchServiceApplication | Get-SPEnterpriseSearchSecurityTrimmer  | Export-Clixml .\Get-SPEnterpriseSearchSecurityTrimmer.xml
  Get-SPEnterpriseSearchServiceApplication | Export-Clixml .\Get-SPEnterpriseSearchServiceApplication.xml
  Get-SPEnterpriseSearchServiceApplicationProxy  | Export-Clixml .\Get-SPEnterpriseSearchServiceApplicationProxy.xml
  Get-SPEnterpriseSearchSiteHitRule  | Export-Clixml .\Get-SPEnterpriseSearchSiteHitRule.xml
  #Security Token Service Application
  #Retrieve information about the security token service used for incoming SOAP messages.
  Get-SPSecurityTokenServiceConfig  | Export-Clixml .\Get-SPSecurityTokenServiceConfig.xml
  #State Service
  #Retrieve information about the State Service.
  Get-SPSessionStateService  | Export-Clixml .\Get-SPSessionStateService.xml
  Get-SPStateServiceApplication  | Export-Clixml .\Get-SPStateServiceApplication.xml
  Get-SPStateServiceApplicationProxy  | Export-Clixml .\Get-SPStateServiceApplicationProxy.xml
  Get-SPStateServiceDatabase  | Export-Clixml .\Get-SPStateServiceDatabase.xml
  #Usage and Health data collection
  #Retrieve information about the Usage and Health Data Collection service application.
  Get-SPUsageApplication  | Export-Clixml .\Get-SPUsageApplication.xml
  Get-SPUsageDefinition  | Export-Clixml .\Get-SPUsageDefinition.xml
  Get-SPUsageService  | Export-Clixml .\Get-SPUsageService.xml
  #Visio Service
  #A Visio service application must be provisioned for the following cmdlets to succeed.
  Get-SPVisioServiceApplication | Get-SPVisioExternalData  | Export-Clixml .\Get-SPVisioExternalData.xml
  Get-SPVisioServiceApplication | Get-SPVisioPerformance  | Export-Clixml .\Get-SPVisioPerformance.xml
  Get-SPVisioServiceApplication | Get-SPVisioSafeDataProvider  | Export-Clixml .\Get-SPVisioSafeDataProvider.xml
  Get-SPVisioServiceApplication | Export-Clixml .\Get-SPVisioServiceApplication.xml
  Get-SPVisioServiceApplicationProxy  | Export-Clixml .\Get-SPVisioServiceApplicationProxy.xml
  #Web Analytics Service Application
  A Web Analytics service application must be provisioned for the following cmdlets to succeed.
  Get-SPServiceApplication | ?{$_.TypeName -eq "Web Analytics Service Application"} | %{$id = $_.Id;Get-SPWebAnalyticsServiceApplication -Id $_ | Export-Clixml .\Get-SPWebAnalyticsServiceApplication-$id.xml}
  Get-SPServiceApplicationProxy | ?{$_.TypeName -eq "Web Analytics Service Application Proxy"} | %{$id = $_.Id;Get-SPWebAnalyticsServiceApplicationProxy -Id $_ | Export-Clixml .\Get-SPWebAnalyticsServiceApplicationProxy-$id.xml}
  Get-SPWebApplication | Get-SPWebApplicationHttpThrottlingMonitor  | Export-Clixml .\Get-SPWebApplicationHttpThrottlingMonitor.xml
  Get-SPWebPartPack  | Export-Clixml .\Get-SPWebPartPack.xml
  #Word Automation Services
  ###Note: These cmdlets are commented out because you are unlikely to want to run them. ###
  #Get-SPSite | %{$web=Get-SPWeb $_.Url;$webid=$web.Id;$web | Get-SPUser | Export-Clixml .\Get-SPUser-$webid.xml}
  # Get-SPSite | %{$web=Get-SPWeb $_.Url;$webid=$web.Id;$web | Export-Clixml .\Get-SPWeb-$webid.xml}
  
  ```

3. Save the file and add the .ps1 extension, such as SuggestedNameOfFile.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
4. Start the SharePoint Management Shell.
    
5. Change to the directory where you saved the file.
    
6. At the PowerShell command prompt, type the following command:
    
  ```
  ./SuggestedFileName.ps1
  ```

For more information, see [Export-Clixml](http://go.microsoft.com/fwlink/p/?LinkID=733400&amp;clcid=0x409), [Get-SPWebApplication](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps), [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Example of using a cmdlet in SharePoint Server
<a name="proc2"> </a>

This section provides an example of ways that you can use one of the recommended cmdlets.
  
The  `Get-SPAlternateURL` cmdlet provides information about alternate access mapping. Piping the cmdlet to the  `Export-Clixml` cmdlet writes the information to an XML file. 
  
```
Get-SPAlternateURL | Export-Clixml .\Get-SPAlternateURL.xml
```

The following section lists the content of the Get-SPAlternateURL.xml file. Some sections are collapsed.
  
```
- <Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
+ <Obj RefId="0">
- <Obj RefId="7">
  <TNRef RefId="0" /> 
  <ToString>Microsoft.SharePoint.Administration.SPAlternateUrl</ToString> 
- <Props>
  <S N="IncomingUrl">http://servername</S> 
  <URI N="Uri">http://servername/</URI> 
+ <Obj N="UrlZone" RefId="8">
- <Obj N="Collection" RefId="9">
  <TNRef RefId="2" /> 
- <IE>
- <Obj RefId="10">
  <TNRef RefId="0" /> 
  <ToString>Microsoft.SharePoint.Administration.SPAlternateUrl</ToString> 
+ <Props>
- <MS>
  <S N="Zone">Default</S> 
  <S N="PublicUrl">http://servername</S> 
  </MS>
  </Obj>
  </IE>
- <Props>
  <I32 N="Count">1</I32> 
  <B N="IsReadOnly">false</B> 
  <S N="TypeName">Alternate Access Mapping Collection</S> 
  <S N="DisplayName">SharePoint - 80</S> 
  <U64 N="DiskSizeRequired">0</U64> 
  <B N="CanSelectForBackup">false</B> 
  <B N="CanRenameOnRestore">false</B> 
  <B N="CanSelectForRestore">false</B> 
  <S N="Name">SharePoint - 80</S> 
  <G N="Id">5b65a69a-222d-4fe0-904b-0fb928bc7a89</G> 
  <S N="Status">Online</S> 
  <S N="Parent">SPFarm Name=SERVERNAME_SharePoint_Configuration_Database</S> 
  <I64 N="Version">3661</I64> 
+ <Obj N="Properties" RefId="12">
  <TNRef RefId="3" /> 
  <DCT /> 
  </Obj>
  <S N="Farm">SPFarm Name=SERVERNAME_SharePoint_Configuration_Database</S> 
  <Ref N="UpgradedPersistedProperties" RefId="11" /> 
  </Props>
  </Obj>
  <Ref N="UpgradedPersistedProperties" RefId="11" /> 
  </Props>
+ <MS>
+ <Obj N="Zone" RefId="13">
  <TNRef RefId="1" /> 
  <ToString>Default</ToString> 
  <I32>0</I32> 
  </Obj>
  <S N="PublicUrl">http://servername</S> 
  </MS>
  </Obj>
  </Objs>
```

This example imports the output from the XML file so that you can see its contents more easily.
  
```
Import-Clixml .\Get-SPAlternateURL.xml

```

Once an XML file is imported, you can use the objects in the pipeline as if they were real objects of the given type.
  
```
Import-Clixml .\Get-SPAlternateURL.xml | %{$_.Uri}
```

You can also pipe the objects as part of the cmdlet, and view all of the expected properties, methods, and TypeNames. The following example pipes URIs.
  
```
Import-Clixml .\Get-SPAlternateURL.xml | %{$_.Uri | Get-Member}

```

## See also
<a name="proc2"> </a>

#### Other Resources

[Export-Clixml](http://go.microsoft.com/fwlink/p/?LinkID=733400&amp;clcid=0x409)
  
[Import-Clixml](http://go.microsoft.com/fwlink/p/?LinkID=733402&amp;clcid=0x409)
  
[Get-SPAlternateURL](/powershell/module/sharepoint-server/Get-SPAlternateURL?view=sharepoint-ps)
  
[ForEach-Object](/previous-versions//dd347608(v=technet.10))
  
[Get-Member](/powershell/module/Microsoft.PowerShell.Utility/Get-Member?view=powershell-5.1)

