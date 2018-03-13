---
title: "Configure server-to-server authentication between publishing and consuming farms"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 9/6/2017
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: c77f5006-d023-463f-8256-e4570d32dd1e
description: "Summary: Learn how to configure server-to-server authentication when you share service applications across SharePoint Server 2016 and SharePoint 2013 publishing and consuming farms."
---

# Configure server-to-server authentication between publishing and consuming farms

 **Summary:** Learn how to configure server-to-server authentication when you share service applications across SharePoint Server 2016 and SharePoint 2013 publishing and consuming farms. 
  
To enable a web application or an application service to request a resource from a web application on another farm on behalf of a user, you must configure server-to-server authentication between the farms. A few examples of SharePoint Server processes that use server-to-server authentication are as follows:
  
- Follow a document on a Team Sites web application when a user's personal site is located on a My Sites web application. The Team Sites web application makes a request of the My Sites web application on behalf of the user.
    
- Create or reply to a site feed post for a site that is located on a Team Sites web application but performed through the user's My Site Newsfeed on the My Sites web application. The My Sites web application will make a request of the Team Sites web application on behalf of the user to write the post or the reply.
    
- A User Profile Service application task to repopulate the feed cache has to read from the personal site or team site. If the User Profile Service application is running in a different farm, the User Profile Service application sends a request to the My Sites web application or Team Sites web application to read the user or site feed data into the cache.
    
> [!NOTE]
> Web applications or application services that request resources from an application service on another farm do not require server-to-server authentication. 
  
## Before you begin
<a name="begin"> </a>

To understand the procedures in this article, you should be familiar with the basic concepts in the following articles:
  
[Authentication overview for SharePoint Server](../security-for-sharepoint-server/authentication-overview.md)
  
[Plan for server-to-server authentication in SharePoint Server](../security-for-sharepoint-server/plan-server-to-server-authentication.md)
  
## Configure server-to-server authentication between publishing and consuming farms
<a name="begin"> </a>

The following procedure describes how to configure server-to-server authentication between the publishing and consuming farms.
  
 **To configure server-to-server authentication between publishing and consuming farms**
  
1. Choose a realm name that will be common to both farms.
    
2. Verify that you are a member of the Administrators group on the server on which you are running PowerShell cmdlets.
    
  - **Securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
3. In the SharePoint Server environment on both the publishing and consuming farms, start the SharePoint Management Shell.
    
4. To configure the publishing farm for the common realm name, type the following command at the PowerShell command prompt on a server in the publishing farm:
    
  ```
  Set-SPAuthenticationRealm -realm <RealmName>
  ```

    Where:
    
     _RealmName_ is the name that you chose in step 1. 
    
5. To configure the Name ID for the SharePoint Security Token Service (STS) on the publishing farm to include the common realm name, type the following commands at the PowerShell command prompt on a server in the publishing farm:
    
  ```
  $sts=Get-SPSecurityTokenServiceConfig
  $Realm=Get-SpAuthenticationRealm
  $nameId = "00000003-0000-0ff1-ce00-000000000000@$Realm"
  Write-Host "Setting STS NameId to $nameId"
  $sts.NameIdentifier = $nameId
  $sts.Update()
  ```

6. To configure the consuming farm for the common realm name, type the following command at the PowerShell command prompt on a server in the consuming farm:
    
  ```
  Set-SPAuthenticationRealm -realm <RealmName>
  ```

    Where:
    
     _RealmName_ is the name that you chose in step 1. 
    
7. To configure the Name ID for the SharePoint STS on the consuming farm to include the common realm name, type the following commands at the PowerShell command prompt on a server in the consuming farm:
    
  ```
  $sts=Get-SPSecurityTokenServiceConfig
  $Realm=Get-SpAuthenticationRealm
  $nameId = "00000003-0000-0ff1-ce00-000000000000@$Realm"
  Write-Host "Setting STS NameId to $nameId"
  $sts.NameIdentifier = $nameId
  $sts.Update()
  ```

8. To configure the publishing farm for server-to-server authentication with the consuming farm, type the following command at the PowerShell command prompt on a server in the publishing farm:
    
  ```
  New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<ConsumeHostName>/_layouts/<15or16>/metadata/json/1" -Name "<ConsumeFriendlyName>"
  ```

    Where:
    
  -  _ConsumeHostName_ is the name and port of any SSL-enabled web application of the consuming farm. 
    
  -  _15or16_ is the directory for the SharePoint Server version. 
    
  -  _ConsumeFriendlyName_ is a friendly name for the consuming farm. 
    
    This creates the server-to-server authentication trust with the consuming farm.
    
9. To configure the consuming farm for server-to-server authentication with the publishing farm, type the following command at the PowerShell command prompt on a server in the consuming farm:
    
  ```
  New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<PublishHostName>/_layouts/<15or16>/metadata/json/1" -Name "<PublishFriendlyName>"
  ```

    Where:
    
  -  _PublishHostName_ is the name and port of any SSL-enabled web application of the publishing farm. 
    
  -  _15or16_ is the directory for the SharePoint Server version. 
    
  -  _PublishFriendlyName_ is a friendly name for the publishing farm. 
    
    This creates the server-to-server authentication trust with the publishing farm.
    
## See also
<a name="begin"> </a>

#### Concepts

[Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md)
#### Other Resources

[Get-SPAuthenticationRealm](http://technet.microsoft.com/library/7ec6c10c-283e-4533-addf-6bdd2d804c28.aspx)
  
[Set-SPAuthenticationRealm](http://technet.microsoft.com/library/d3d60059-4883-4591-a3a7-d3002c999e68.aspx)
  
[New-SPTrustedSecurityTokenIssuer](http://technet.microsoft.com/library/9ab7aac9-4c9a-4cba-8dd6-ffead217c2fa.aspx)

