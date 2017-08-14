---
title: Configure trust for search between two SharePoint Server farms
ms.prod: SHAREPOINT
ms.assetid: 3ebcdcdf-593e-44bd-b60d-16efd5f07a16
---


# Configure trust for search between two SharePoint Server farms
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Configure a SharePoint Server 2016 or a SharePoint Server 2013 content farm that receives search queries to trust the SharePoint Server 2016 farm or SharePoint Server 2013 that sends the queries.To configure an on-premises SharePoint Server content farm to return results from its search index to a separate on-premises SharePoint Server farm, you must perform the following two main procedures:
1. In the farm that will receive the search queries, configure trust of the farm that will send the queries by doing the following:
    
  - Configure a server-to-server trust relationship by using the Open Authorization 2.0 (OAuth 2.0) web authorization protocol.
    
  
  - Enable the farm that receives the queries to return search results from all of its web applications that host content.
    
  
2. In the farm that will send the search queries, create a result source that does each of the following:
    
  - Specifies **Remote SharePoint** as the protocol.
    
  
  - Specifies the address of any root site collection in the SharePoint Server farm that will receive the search queries.
    
  

    For more information, see  [Configure result sources for search in SharePoint Server](html/configure-result-sources-for-search-in-sharepoint-server.md).
    
    > [!NOTE:]
      
This article describes how to perform the first procedure in the list above: how to configure the farm that receives search queries to trust the farm that sends the queries.For brevity in this article, the following terms are used:
### 

 **SendingFarm** <br/> An on-premises SharePoint Server farm that has a search service that sends search queries to ReceivingFarm.  <br/> **ReceivingFarm** <br/> An on-premises SharePoint Server content farm that has a search index that receives search queries from SendingFarm. In this article, it is assumed that ReceivingFarm has at least one web application that hosts content.  <br/> In order for SendingFarm to be able to get search results from the search index in ReceivingFarm, the farms must have the following characteristics:
- Each farm is a SharePoint Server on-premises deployment.
    
  
- User profiles in the two farms are synchronized. For more information, see  [Server-to-server authentication and user profiles in SharePoint Server](html/server-to-server-authentication-and-user-profiles-in-sharepoint-server.md).
    
  

> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    


## 

 **To configure ReceivingFarm to trust SendingFarm**
1. Verify that the account that performs this procedure is a member of the following groups:
    
  - Farm Administrators group in ReceivingFarm.
    
  
  - Administrators group on the server on which you are running Microsoft PowerShell cmdlets.
    
    An administrator of that server can use the **Add-SPShellAdmin** cmdlet to grant someone permission to use SharePoint Server 2016 cmdlets. When you run the **Add-SPShellAdmin** cmdlet, you must have membership in the **securityadmin** fixed server role on the SQL Server instances, and you must have membership in the **db_owner** fixed database role on all databases that are to be updated. For more information, see **Add-SPShellAdmin**. Contact your system administrator or SQL Server administrator to request these memberships if you do not have them.
    
  
2. On a server in ReceivingFarm, start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2008 R2:
    
    In the SharePoint Server environment, on the **Start** menu, click **All Programs**, click **SharePoint 2016**, and then click **SharePoint 2016 Management Shell**.
    
  
  - For Windows Server 2012:
    
  - In the SharePoint Server environment, on the **Start** page, click **SharePoint 2016 Management Shell**.
    
  
  - If **SharePoint 2016 Management Shell** is not on the **Start** page, right-click **Computer**, click **All apps**, and then click SharePoint 2016 Management Shell.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
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
    
     *https://<SendingFarm_web_application>*  is any SSL-enabled web application in SendingFarm
    
    > [!IMPORTANT:]
      
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
    
     *https://<ReceivingFarm_web_application>*  is an SSL-enabled web application in ReceivingFarm.
    
  
6. Repeat the previous step (step 5) for each web application in ReceivingFarm that hosts content that you want to search.
    
  

# See also

#### 

 [Authentication overview for SharePoint Server](html/authentication-overview-for-sharepoint-server.md)
  
    
    
 [Plan for server-to-server authentication in SharePoint Server](html/plan-for-server-to-server-authentication-in-sharepoint-server.md)
  
    
    
 [Plan for server-to-server authentication in SharePoint Server](html/plan-for-server-to-server-authentication-in-sharepoint-server.md)
  
    
    

#### 

 **Configure server-to-server authentication in SharePoint Server**
  
    
    
 [Setting Up an oAuth Trust Between Farms in SharePoint 2013](https://blogs.technet.com/b/speschka/archive/2012/07/23/setting-up-an-oauth-trust-between-farms-in-sharepoint-2013.aspx)
  
    
    
 [Getting a Full Result Set from a Remote SharePoint Index in SharePoint 2013](https://blogs.technet.com/b/speschka/archive/2013/01/24/getting-a-full-result-set-from-a-remote-sharepoint-index-in-sharepoint-2013.aspx)
  
    
    
 [An Introduction to JavaScript Object Notation (JSON) in JavaScript and .NET](https://msdn.microsoft.com/en-us/library/bb299886.aspx)
  
    
    

  
    
    

