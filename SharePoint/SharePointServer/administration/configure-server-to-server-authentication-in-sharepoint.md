---
title: "Configure server-to-server authentication between publishing and consuming farms"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 9/6/2017
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: c77f5006-d023-463f-8256-e4570d32dd1e
description: "Summary: Learn how to configure server-to-server authentication when you share User Profile service application across SharePoint Server 2016 and SharePoint 2013 publishing and consuming farms."
---

# Configure Server-to-Server authentication between publishing and consuming farms

 **Summary:** Learn how to configure Server-to-Server authentication when you share the User Profile service application across SharePoint Server 2016 and SharePoint 2013 publishing and consuming farms. 
  
When a farm consumes the User Profile service application of a publishing farm, SharePoint issues requests using Server-to-Server authentication on behalf of the user for some features:
  
- Follow a document on a content web application when a user's personal site is located on a web application in an external farm. The content web application makes a OAuth request to the My Sites web application on behalf of the user.

- Create or reply to a site feed post for a site that is located on a content web application but performed through the user's My Site Newsfeed on the My Sites web application. The My Sites web application will make a request of the Team Sites web application on behalf of the user to write the post or the reply.

- A User Profile Service application task to repopulate the feed cache has to read from the personal site or team site. If the User Profile Service application is running in a different farm, the User Profile Service application sends a request to the My Sites web application or Team Sites web application to read the user or site feed data into the cache.
  
## Before you begin
<a name="begin"> </a>

This article requires that you already shared the User Profile service application between a consuming and a publishing farm. If you haven't done so, see [Share service applications across farms in SharePoint Server](/share-service-applications-across-farms) first to share the User Profile service application.

To understand the procedures in this article, you should be familiar with the basic concepts in the following articles:

[Authentication overview for SharePoint Server](../security-for-sharepoint-server/authentication-overview.md)

[Plan for server-to-server authentication in SharePoint Server](../security-for-sharepoint-server/plan-server-to-server-authentication.md)

Verify that you are a member of the Administrators group on the servers on which you are running PowerShell cmdlets.

  - **Securityadmin** fixed server role on the SQL Server instance.
  - **db_owner** fixed database role on all databases that are to be updated.
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.  
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 

## Configure server-to-server authentication between publishing and consuming farms
<a name="begin"> </a>

The following procedure describes how to configure server-to-server authentication and grant just the necessary permissions to allow social features to work. Each farm keeps its own, unique authentication realm.

### Authorize consuming farm to send OAuth requests to the publishing farm

1. In a SharePoint server in the publishing farm, start the SharePoint Management Shell.

2. Register the consuming farm as a trusted issuer:

```powershell
New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<ConsumeHostName>/_layouts/<15or16>/metadata/json/1" -Name "<ConsumeFriendlyName>"
```

    > [!NOTE]
    > This assumes that you already added the root certificate of the consuming farm to the trusted root authorities as explained in article [Exchange trust certificates between farms in SharePoint Server](/exchange-trust-certificates-between-farms).

3. Get the app principal and set required authorizations:

```powershell
# Get the app principal and set required authorizations
$mySiteHost = Get-SPWeb "http://<MySiteHostUrl/"
$appPrincipal = Get-SPAppPrincipal -Site $mySiteHost -NameIdentifier $trustedIssuer.NameId

# Grant permissions AppOnly and Write on the MySite host
Set-SPAppPrincipalPermission -EnableAppOnlyPolicy -Site $mySiteHost -AppPrincipal $appPrincipal -Scope SiteSubscription -Right Write

# Grant permissions Manage on the PrivateAPI and Read on the SocialPermissionProvider
$privateAPITypeId = New-Object -TypeName System.Guid ("a2ccc2e2-1703-4bd9-955f-77b2550d6f0d")
$socialPermissionProviderId = New-Object -TypeName System.Guid ("fcaec196-a98c-4f8f-b60f-e1a82272a6d2")
$mgr = New-Object -TypeName Microsoft.SharePoint.SPAppPrincipalPermissionsManager ($mySiteHost)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $privateAPITypeId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Manage)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $socialPermissionProviderId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Read)
```

### Authorize publishing farm to send OAuth requests to the consuming farm

1. In a SharePoint server in the consuming farm, start the SharePoint Management Shell.

2. Register the farm running User Profile service application as a trusted issuer:

```powershell
$trustedIssuer = New-SPTrustedSecurityTokenIssuer -MetadataEndpoint "https://<PublishingHostName>/_layouts/<15or16>/metadata/json/1" -Name "<PublishingFriendlyName>"
```

    > [!NOTE]
    > This assumes that you already added the root certificate of the consuming farm to the trusted root authorities as explained in article [Exchange trust certificates between farms in SharePoint Server](/exchange-trust-certificates-between-farms).

3. Get the app principal and set required authorizations:

```powershell
# Get the app principal
$centralAdminWeb = Get-SPWeb "http://sp:5000/"
$appPrincipal = Get-SPAppPrincipal -Site $centralAdminWeb -NameIdentifier $trustedIssuer.NameId

# Grant app only permission and Read on the SiteSubscription
Set-SPAppPrincipalPermission -EnableAppOnlyPolicy -AppPrincipal $appPrincipal -Site $centralAdminWeb -Scope SiteSubscription -Right Read

# Grant permissions Manage on the PrivateAPI
$privateAPITypeId = New-Object -TypeName System.Guid ("a2ccc2e2-1703-4bd9-955f-77b2550d6f0d")
$mgr = New-Object -TypeName Microsoft.SharePoint.SPAppPrincipalPermissionsManager ($centralAdminWeb)
$mgr.AddSiteSubscriptionPermission($appPrincipal, $privateAPITypeId, [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::Manage)
```

## See also
<a name="begin"> </a>

### Concepts

[Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md)

### Other Resources
  
[New-SPTrustedSecurityTokenIssuer](http://technet.microsoft.com/library/9ab7aac9-4c9a-4cba-8dd6-ffead217c2fa.aspx)
