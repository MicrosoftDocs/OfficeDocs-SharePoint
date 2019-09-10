---
title: "Configure trust for search between two SharePoint Server farms"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3ebcdcdf-593e-44bd-b60d-16efd5f07a16
description: "Configure a SharePoint Server content farm that receives search queries to trust the SharePoint Server farm that sends the queries."
---

# Configure trust for search between two SharePoint Server farms

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
To configure an on-premises SharePoint Server content farm to return results from its search index to a separate on-premises SharePoint Server farm, you must perform the following two main procedures:
  
1. In the farm that will receive the search queries, configure trust of the farm that will send the queries by doing the following:
    
  - Configure a server-to-server trust relationship by using the Open Authorization 2.0 (OAuth 2.0) web authorization protocol.
    
  - Enable the farm that receives the queries to return search results from all of its web applications that host content.
    
2. In the farm that will send the search queries, create a result source that does each of the following:
    
  - Specifies **Remote SharePoint** as the protocol. 
    
  - Specifies the address of any root site collection in the SharePoint Server farm that will receive the search queries.
    
  For more information, see [Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md).
  
  > [!NOTE]
  > After you create the result source, you expose the search results that it provides by using it in a Web Part or a query-rule action. In this way, users of the farm that is sending search queries can see results from the farm that is receiving the queries. For more information, see [Understanding result sources for search in SharePoint Server](understanding-result-sources-for-search.md). 
  
This article describes how to perform the first procedure in the list above: how to configure the farm that receives search queries to trust the farm that sends the queries.
  
For brevity in this article, the following terms are used:
  
|                   |                                                                                                                                                                                                                             |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SendingFarm**   | An on-premises SharePoint Server farm that has a search service that sends search queries to ReceivingFarm.                                                                                                                 |
| **ReceivingFarm** | An on-premises SharePoint Server content farm that has a search index that receives search queries from SendingFarm. In this article, it is assumed that ReceivingFarm has at least one web application that hosts content. |
   
In order for SendingFarm to be able to get search results from the search index in ReceivingFarm, the farms must have the following characteristics:
  
- Each farm is a SharePoint Server on-premises deployment.
    
- User profiles in the two farms are synchronized. For more information, see [Server-to-server authentication and user profiles in SharePoint Server](../security-for-sharepoint-server/server-to-server-authentication-and-user-profiles.md).
    
> [!NOTE]
>  Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: 
>-  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)
>-  [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines)
>-  [Accessibility features in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=246501)
>-  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)
>-  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)

**To configure ReceivingFarm to trust SendingFarm**
  
1. Verify that the account that performs this procedure is a member of the following groups:
    
  - Farm Administrators group in ReceivingFarm.
    
  - Administrators group on the server on which you are running Microsoft PowerShell cmdlets.
    
    An administrator of that server can use the **Add-SPShellAdmin** cmdlet to grant someone permission to use SharePoint Server cmdlets. When you run the **Add-SPShellAdmin** cmdlet, you must have membership in the **securityadmin** fixed server role on the SQL Server instances, and you must have membership in the **db_owner** fixed database role on all databases that are to be updated. For more information, see [Add-SPShellAdmin](/SharePoint/accessibility-guidelines). Contact your system administrator or SQL Server administrator to request these memberships if you do not have them.
    
2. On a server in ReceivingFarm, start the SharePoint Management Shell.
    
  - For Windows Server 2008 R2:
    
    In the SharePoint Server environment, on the **Start** menu, click **All Programs**, click **SharePoint 2016**, and then click **SharePoint Management Shell**.
    
  - For Windows Server 2012:
    
    - In the SharePoint Server environment, on the **Start** page, click **SharePoint Management Shell**.
    
    - If **SharePoint Management Shell** is not on the **Start** page, right-click **Computer**, click **All apps**, and then click SharePoint Management Shell.
    
    For more information about how to interact with Windows Server 2012, see [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
3. On a server in ReceivingFarm, run the following commands at a PowerShell command prompt. The commands use the OAuth 2.0 web authorization protocol to configure a server-to-server trust, so that ReceivingFarm will trust SendingFarm.
    
  ```
  # Create a trusted security token issuer
  $i = New-SPTrustedSecurityTokenIssuer -Name "SendingFarm" -IsTrustBroker:$false -MetadataEndpoint "https://<SendingFarm_web_application>/_layouts/15/metadata/json/1"
  # Configure trust of the token-signing certificate'
  # by adding the trust used to sign oAuth tokens'
  # to the list of trusted root authorities'
  # in ReceivingFarm
  New-SPTrustedRootAuthority -Name "SendingFarm" -MetadataEndPoint https://<SendingFarm_web_application>/_layouts/15/metadata/json/1/rootcertificate
  ```

    Where:
    
     _https://\<SendingFarm_web_application\>_ is any SSL-enabled web application in SendingFarm 
    
    > [!IMPORTANT]
    > Web applications that include server-to-server authentication endpoints for incoming server-to-server requests, or that make outgoing server-to-server requests, should be configured to use Secure Sockets Layer (SSL). For information about how to configure a web application to use SSL, see [Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14)). For information about how to configure HTTP support for server-to-server requests, see [Configure server-to-server authentication between SharePoint Server farms](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server#HTTP) in [Configure server-to-server authentication in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server). 
  
4. On a server in ReceivingFarm, at a PowerShell command prompt, run the following command:
    
  ```
  # Use $realm to store the string'
  # that comes after the "@" character'
  # in the value of $i.NameId
  $realm = $i.NameId.Split("@")
  ```

5. On a server in ReceivingFarm, at a PowerShell command prompt, run the following commands to enable all web applications in ReceivingFarm to return search results to SendingFarm:
    
  ```
  $s1 = Get-SPSite -Identity https://<ReceivingFarm_web_application>
  $sc1 = Get-SPServiceContext -Site $s1
  # Set up an authentication realm for'
  # a web application that hosts content in ReceivingFarm 
  Set-SPAuthenticationRealm -ServiceContext $sc1 -Realm $realm[1]
  # Get a reference to the application principal'
  # for that web application in Farm B
  $p = Get-SPAppPrincipal -Site https://<ReceivingFarm_web_application> -NameIdentifier $i.NameId
  # Grant rights to the application principal'
  # that SendingFarm will use'
  # when it sends queries to ReceivingFarm
  Set-SPAppPrincipalPermission -Site https://<ReceivingFarm_web_application> -AppPrincipal $p -Scope SiteCollection -Right FullControl
  ```

    Where:
    
     _https://\<ReceivingFarm_web_application\>_ is an SSL-enabled web application in ReceivingFarm. 
    
6. Repeat the previous step (step 5) for each web application in ReceivingFarm that hosts content that you want to search.
    
## See also


[Authentication overview for SharePoint Server](../security-for-sharepoint-server/authentication-overview.md)
  
[Plan for server-to-server authentication in SharePoint Server](../security-for-sharepoint-server/plan-server-to-server-authentication.md)
  
[Plan for server-to-server authentication in SharePoint Server](../security-for-sharepoint-server/plan-server-to-server-authentication.md)

[Configure server-to-server authentication in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server)
  
[Setting Up an oAuth Trust Between Farms in SharePoint 2013](https://blogs.technet.com/b/speschka/archive/2012/07/23/setting-up-an-oauth-trust-between-farms-in-sharepoint-2013.aspx)
  
[Getting a Full Result Set from a Remote SharePoint Index in SharePoint 2013](https://blogs.technet.com/b/speschka/archive/2013/01/24/getting-a-full-result-set-from-a-remote-sharepoint-index-in-sharepoint-2013.aspx)
  
[An Introduction to JavaScript Object Notation (JSON) in JavaScript and .NET](https://msdn.microsoft.com/en-us/library/bb299886.aspx)

