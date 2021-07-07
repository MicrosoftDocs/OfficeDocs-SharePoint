---
title: "New and improved features in SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-bshilpa
author: Benny-54
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server Subscription Edition."
---

# New and improved features in SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Learn about the new features and updates to existing features in SharePoint Server Subscription Edition.

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features in SharePoint Server Subscription Edition.

|**Feature Group**|**Features**|**More info**|
|:-----|:-----|:-----|
|Authentication and Identity Management <br/> | <ul><li>Adds support for OpenID Connect (OIDC) 1.0</li><li>Enhanced People Picker for trusted identity providers</li><li>Improved Integrated Windows authentication over TLS</li></ul> | <ul><li>For more information, see [OpenID Connect (OIDC) 1.0 authentication](#OIDCa).</li><li>For more information, see [People Picker improvement for trusted authentication methods](#people).</li><li>For more information, see [Reduced Integrated Windows authentication latency over TLS](#IIW).</li></ul> | 
|Deployment and Upgrade <br/> | <ul><li>Adds support for Windows Server 2022</li><li>Adds support for Windows Server Core</li><li>Supports "N - 2" upgrading from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)</li><li>AppFabric Cache integration</li></ul> | <ul><li>For more information, see [Windows Server 2022](#server).</li><li>For more information, see [Windows Server Core](#core).</li><li>For more information, see [Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)](#upgrade).</li><li>For more information, see [AppFabric Cache integration](#cache).</li></ul> |
|Farm Administration <br/> | <ul><li>Adds support for host header bindings on Central Admin web application</li><li>Adds support for Server Name Indication (SNI) for host header bindings</li><li>Change web application bindings</li><li>Easier AAM configuration for Central Administration</li><li>Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)</li><li>Support for client certificate authentication to SMTP servers</li></ul> | <ul><li>For more information, see [Central Administration now supports host header bindings](#cenadmin).</li><li>For more information, see [Server Name Indication](#sni).</li><li>For more information, see [Change web application IIS bindings](#webiis).</li><li>For more information, see [Easier AAM configuration for Central Administration](#aamcon).</li><li>For more information, see [Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)](#fedral).</li><li>For more information, see [Client certificate authentication to SMTP servers](#client).</li></ul> |
|Health and Monitoring <br/> | <ul><li>Certificate notification contacts haven't been configured</li><li>Upcoming SSL certificate expirations</li><li>SSL certificates are about to expire</li><li>SSL certificates have expired</li></ul> | <ul><li>For more information, see [Certificate notification contacts haven't been configured](#cncc).</li><li>For more information, see [Upcoming SSL certificate expirations](#usce).</li><li>For more information, see [SSL certificates are about to expire](#sslcate).</li><li>For more information, see [SSL certificates have expired](#sslche).</li></ul> |
|Hybrid <br/> | <ul><li>Better integration with Power Apps and Power Automate</li><li>Cloud SSA (Search) supports Microsoft 365 Multi-Geo</li><li>Improved hybrid search troubleshooting</li></ul> | <ul><li>For more information, see [Power Apps and Power Automate integration](#power).</li><li>For more information, see [Cloud SSA (Search) supports Microsoft 365 Multi-Geo](#ssa).</li><li>For more information, see [Improved hybrid search troubleshooting](#ihst).</li></ul> | 
|PowerShell <br/> | <ul><li>SharePoint PowerShell cmdlets converted from snap-in to module</li><li>Distributed Cache cmdlets</li><li>New-SPWebApplication creates web applications in Windows claims mode by default</li><li>New People Picker cmdlets</li><li>Remove-SPConfigurationObject cmdlet</li><li>SharePoint Volume Shadow Copy Service writer cmdlets</li></ul> | <ul><li>For more information, see [SharePoint PowerShell cmdlets converted from snap-in to module](#snap).</li><li>For more information, see [Distributed Cache cmdlets](#dcc).</li><li>For more information, see [New-SPWebApplication PowerShell cmdlet](#spweb).</li><li>For more information, see [New People Picker cmdlets](#nppc)</li><li>For more information, see [Introducing Remove-SPConfigurationObject PowerShell cmdlet](#resp).</li><li>For more information, see [SharePoint Volume Shadow Copy Service writer cmdlets](#vscs).</li></ul> |
|Search <br/> | <ul><li>Search result page modernization</li><li>Support for returning list content in modern results page</li><li>Thumbnails in modern search result page</li></ul> | <ul><li>For more information, see [Search result page modernization](#seres).</li><li>For more information, see [Support for returning list content in modern results page](#listmrp).</li><li>For more information, see [Thumbnails in modern search result page](#tmsr).</li></ul> |
|Security <br/> | <ul><li>SSL certificate management</li><li>Adds support for TLS 1.3</li><li>Strong TLS encryption by default</li><li>Improved ASP.NET view state security and key management</li></ul> | <ul><li>For more information, see [SSL certificate management](#sslcm).</li><li>For more information, see [TLS 1.3](#tlss).</li><li>For more information, see [Strong TLS encryption by default](#tlsed).</li><li>For more information, see [Improved ASP.NET view state security and key management](#aspnet).</li></ul> |
|Sites, Lists, and Libraries <br/> | <ul><li>Accessibility improvements</li><li>Brick layout for document library thumbnails and image gallery web part</li><li>Bulk check-in and check-out</li><li>Bulk download files from document libraries and OneDrive personal sites</li><li>Image and document thumbnails in document libraries and picture libraries</li><li>List and library modern web parts support adding/editing/deleting content</li><li>Modern document sets</li></ul> | <ul><li>For more information, see [Accessibility improvements across modern UX](#aiamu).</li><li>For more information, see [Brick layout for document library thumbnails and image gallery web part](#briclil).</li><li>For more information, see [Bulk check-in/check-out in modern Document library experience](#bulkinout).</li><li>For more information, see [Bulk download files from document libraries and OneDrive personal sites](#bulkdod).</li><li>For more information, see [Image and document thumbnails in document libraries and picture libraries](#idt).</li><li>For more information, see [List and library modern web parts support adding/editing/deleting content](#llmw).</li><li>For more information, see [Modern document sets](#mds).</li></ul> |
|Storage <br/> | <ul><li>New BLOB storage provider: Remote Share Provider</li><li>Remote Share Provider diagnostic tool</li></ul> | <ul><li>For more information, see [Remote Share Provider](#blob).</li><li>For more information, see [Remote Share Provider diagnostic tool](#rspdt).</li></ul> | 

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition.

## Authentication and Identity Management

### OpenID Connect (OIDC) 1.0 authentication
<a name="OIDCa"> </a>

SharePoint Server Subscription Edition adds support for the OpenID Connect (OIDC) 1.0 authentication protocol. OIDC is a modern authentication protocol that makes it easy to integrate applications and devices with your organization's identity and authentication management solutions to better meet your evolving security and compliance needs. For example, customers can enforce authentication policies such as multi-factor authentication (MFA), conditional access policies based on device compliance, and more.

SharePoint Server Subscription Edition supports OIDC authentication with identity providers such as Azure Active Directory (AAD), Active Directory Federation Services (AD FS) 2016 or higher, and third party identity providers that implement the OIDC 1.0 protocol.

### People Picker improvement for trusted authentication methods
<a name="people"> </a>

In previous versions of SharePoint Server, if a web application was configured to use a trusted identity provider with the built-in claims provider, then the People Picker would resolve all input as a valid user or group even if it wasn't. Customers had to implement a custom claims provider to ensure the People Picker would only resolve valid users and groups.

In SharePoint Server Subscription Edition, the People Picker has been enhanced to allow resolving users and groups based on their profiles in the User Profile Application (UPA). UPA must be configured to synchronize users and groups from the trusted identity provider membership store. This allows the People Picker to only resolve valid users and groups without requiring a custom claims provider.

### Reduced Integrated Windows authentication latency over TLS
<a name="IIW"> </a>

Internet Information Services (IIS) 10 advertises support for HTTP/2 during TLS negotiation, letting the client know that it can use HTTP/2 once the Transport Layer Security (TLS) connection is complete. However, HTTP/2 and above are not compatible with Integrated Windows authentication protocols such as Negotiate (Kerberos) and New Technology LAN Manager (NTLM). 

If a server detects that a client is attempting to perform Kerberos or NTLM authentication over an HTTP/2 or HTTP/3 connection, it will notify the client to downgrade the connection to HTTP/1.1 and restart the attempt. This results in extra round trips between the client and the server during authentication, which increases latency. 

SharePoint Server Subscription Edition reduces this authentication latency by disabling HTTP/2 and Quick UDP Internet Connections (QUIC) in SharePoint IIS web sites when Negotiate (Kerberos) or NTLM are enabled. HTTP/2 and QUIC will continue to be available on SharePoint IIS web sites that aren't configured to use Negotiate (Kerberos) or NTLM.

## Deployment and Upgrade

### Windows Server 2022
<a name="server"> </a>

Windows Server 2022 includes various new features and improvements in virtualization, networking, security, and more, such as:

 - Performance improvements in the Hyper-V virtual switch to reduce the CPU load of virtual machine network communication.
 
 - Performance improvements in both TCP and UDP networking to maximize bandwidth, minimizing packet loss, and reduce CPU load.
 
 - Support for TLS 1.3, the latest and strongest connection encryption standard.
 
 - Support for AES-256-GCM encryption in SMB file sharing, along with compressed file transfers over the network when using the `robocopy.exe` and `xcopy.exe` tools with the `/compress` parameter.
 
SharePoint Server Subscription Edition supports additional security features when deployed with Windows Server 2022 or higher such as support for TLS 1.3 and strong TLS encryption by default. These security features are not available when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server. Microsoft recommends deploying SharePoint Server Subscription Edition with Windows Server 2022 or higher.

### Windows Server Core
<a name="core"> </a>

Windows Server Core is a leaner Windows Server deployment type compared to the classic Windows Server with Desktop Experience. Server Core minimizes the number of OS features and services that are installed and running to only those that are truly needed for a server. This reduces the demand on system resources (CPU, RAM, and disk space) and the potential attack surface for security vulnerabilities.

SharePoint Server Subscription Edition adds support for the Windows Server Core deployment type with both Windows Server 2019 and Windows Server 2022. The Windows Server Desktop Experience deployment type remains supported with both Windows Server 2019 and Windows Server 2022.

### Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)
<a name="upgrade"> </a>

SharePoint Server Subscription Edition supports both **N - 1** and **N - 2** version-to-version upgrade. You can upgrade directly from the following SharePoint products using the standard database attach upgrade procedure:

 - SharePoint Server 2019 (including Project Server 2019)
 
 - SharePoint Server 2016 (including Project Server 2016)

> [!NOTE]
> Upgrade path from earlier versions of SharePoint such as SharePoint Server 2013, SharePoint Server 2010, and so on to SharePoint Server Subscription Edition is not supported. You must upgrade first to either SharePoint 2016 or SharePoint 2019 before upgrading to SharePoint Server Subscription Edition.

### AppFabric Cache integration
<a name="cache"> </a>

In previous versions of SharePoint Server, the Distributed Cache feature relied on Windows Server AppFabric, which was a separately installed component. Starting with SharePoint Server Subscription Edition, the AppFabric caching technology has been directly integrated into the Distributed Cache feature. Distributed Cache no longer relies on the external Windows Server AppFabric component and it will no longer be installed by the Microsoft SharePoint Products Preparation Tool.

## Farm Administration

### Central Administration now supports host header bindings
<a name="cenadmin"> </a>

You can now configure the SharePoint Central Administration website to use a host header binding, which will allow it to share the same TCP port number as other websites. This would typically be used to let the SharePoint Central Administration site and your content website to be hosted on the same TCP port, such as port 443 for SSL.

To configure this, specify the host header binding with the `-HostHeader` parameter of the `New-SPCentralAdministration` and `Set-SPCentralAdministration` cmdlets, or with the `-hostheader` parameter of the `psconfig.exe -cmd adminvs` command.

### Server Name Indication (SNI)
<a name="sni"> </a>

Server Name Indication (SNI) allows multiple IIS websites with unique host headers and unique server certificates to share the same Secure Sockets Layer (SSL) port. The server examines the server name specified by the client during the SSL handshake to determine which server certificate should be used to complete the connection. Your IIS website must have a host header and must use SSL to use Server Name Indication. If Server Name Indication isn't used, all IIS websites sharing the same SSL port will share the same server certificate.

Server Name Indication can be configured by the **Use Server Name Indication** setting on the **Create New Web Application** and **Extend Web Application** pages in SharePoint Central Administration.  

It can also be configured by the following commands:

 - `psconfig.exe -adminvs -port <port number> -hostheader <host header> -ssl -usesni`
  
 - `New-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
  
 - `Set-SPCentralAdministration -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication` 
 
 - `New-SPWebApplication ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
  
 - `Set-SPWebApplication ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication`
  
 - `New-SPWebApplicationExtension ... -Port <port number> -HostHeader <host header> -SecureSocketsLayer -UseServerNameIndication` 

### Change web application IIS bindings
<a name="webiis"> </a>
  
You can change your web application IIS bindings in SharePoint Server Subscription Edition without having to first delete and then recreate your web applications. This functionality is supported in all web application zones.

To change your web application IIS binding in PowerShell, use the `Set-SPWebApplication` cmdlet. For example, you can run the following PowerShell command to change a SharePoint web application at http://servername on HTTP port 80 to use a host header binding "sharepoint.contoso.com" on SSL port 443:

 ```PowerShell
Set-SPWebApplication -Identity http://servername -Zone Default -Port 443 -SecureSocketsLayer -HostHeader sharepoint.contoso.com -Url https://sharepoint.contoso.com
```

You can also change the SharePoint web application IIS bindings through Central Administration. The SharePoint farm administrators can use the Edit button in the **Web Application Management** page in Central Administration, to select a web application's zone. Here you can change the IIS bindings, SSL certificate, and public URL of this web application's zone. This functionality is only available to users who are a member of the local Administrators group on the server.

### Easier AAM configuration for Central Administration
<a name="aamcon"> </a>

You can now specify the public AAM URL directly in the Central Administration command-line tools, bringing them to parity with the content web application command-line tools.  This can be specified via the optional `-Url <String>` parameter in the following PowerShell cmdlets and `PSConfig.exe` command-line utility:

 - `New-SPCentralAdministration`
 
 - `Set-SPCentralAdministration`
 
 - `PSConfig.exe -cmd adminvs`
  
### Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)
<a name="fedral"> </a>
  
In SharePoint Server, some service applications can be shared across server farms. Microsoft supports service applications published by a SharePoint Server Subscription Edition farm being consumed by the following versions of SharePoint Server:

 - SharePoint Server Subscription Edition (N)

 - SharePoint Server 2019 (N - 1)

 - SharePoint Server 2016 (N - 2)

For more information, see [Share service applications across farms in SharePoint Server](https://docs.microsoft.com/sharepoint/administration/share-service-applications-across-farms).

### Client certificate authentication to SMTP servers
<a name="client"> </a>

You can now authenticate to Simple Mail Transfer Protocol (SMTP) servers using client certificates. You need to import a client certificate into your farm using our SSL certificate management, then assign that client certificate to the outgoing email settings within the SharePoint farm.

## Health and Monitoring

### Certificate notification contacts haven't been configured
<a name="cncc"> </a>

This health rule runs weekly to provide notifications through Central Administration when certificates are in use and no certificate notification contacts have been configured.

### Upcoming SSL certificate expirations
<a name="usce"> </a>

This health rule runs weekly to provide advanced notification through both Central Administration and email of upcoming certificate expirations.

### SSL certificates are about to expire
<a name="sslcate"> </a>

This health rule runs daily to provide advanced notification through both Central Administration and email when certificates are about to expire.

### SSL certificates have expired
<a name="sslche"> </a>

This health rule runs daily to provide notification through both Central Administration and email when certificates have expired.

## Hybrid

### Power Apps and Power Automate integration
<a name="power"> </a>

Two new commands will be available in the modern document library page and modern list page command bar when a SharePoint Server Subscription Edition farm is connected to a Microsoft 365 tenant through hybrid:

  - Power Apps
  
  - Power Automate
  
These commands will take you directly to the Power Apps and Power Automate service pages. 

### Cloud hybrid search (Cloud SSA) supports hybrid data residence on multiple regions
<a name="ssa"> </a>
  
The cloud hybrid search (cloud SSA) feature in SharePoint Server Subscription Edition supports hybrid data residence on multiple regions when Microsoft 365 multi-geo is enabled in your tenant. You can index your on-premises farms’ data on the different regions in Microsoft 365, or move your hybrid index from one region to another region in Microsoft 365.

### Improved hybrid search troubleshooting
<a name="ihst"> </a>

There are two improvements added to Search Crawler Log in Center Admin user experience:
  
  - A new column called **online ID** is introduced to crawler log for all contents when SharePoint Farm is configured with cloud hybrid search (cloud SSA). This **online ID** is SharePoint online search index for On-Premises contents in SharePoint Server.
  
  - A new Warning breakdown tab is added next to the Error breakdown tab in the crawler log page. It provides the ability for administrators to examine search crawler warnings with the same user experience as the Error breakdown tab by listing all of the warnings in the crawler log.

## PowerShell

### SharePoint PowerShell cmdlets converted from snap-in to module
<a name="snap"> </a>

SharePoint Server PowerShell cmdlets are now installed via a PowerShell module instead of a PowerShell snap-in. This follows the recommended packaging approach from PowerShell and allows us to better support the PowerShell experience.  
  
It includes the following benefits:
  
  - SharePoint Server cmdlets are now automatically available in all Windows PowerShell consoles.  You don't have to launch the SharePoint Management Shell or use the `Add-PSSnapin` cmdlet to access the SharePoint Server cmdlets.
  
  - PowerShell will be able to download updated SharePoint Server cmdlet help content over the Internet.
  
> [!NOTE]
> The SharePoint Management Shell will continue to be included in the product to provide a familiar PowerShell UI for managing SharePoint Server. The SharePoint Server PowerShell cmdlets will continue to require Windows PowerShell. These cmdlets will not be compatible with PowerShell Core.
  
### Distributed Cache cmdlets
<a name="dcc"> </a>
  
The following SharePoint cmdlets have been added to help manage Distributed Cache in SharePoint Server Subscription Edition. These cmdlets are equivalent to the direct Distributed Cache cmdlets that were available in the standalone AppFabric Distributed Cache product used with previous versions of SharePoint Server.
  
 - `Start-SPCacheCluster`: Starts the Caching Service on all cache hosts in the cluster.
   
 - `Stop-SPCacheCluster`: Stops the Caching Service on all cache hosts in the cluster.
   
 - `Import-SPCacheClusterConfig -Path <String>`: Imports the cache cluster configuration details from an XML file.
   
 - `Export-SPCacheClusterConfig -Path <String>`: Export cache cluster configuration details to an XML file.
   
 - `Get-SPCacheClusterHealth`: Returns statistics for all of the named caches in the cache cluster.
  
The `Get-SPCacheHost` PowerShell cmdlet is added to help manage the SharePoint Distributed Cache feature. It provides the same functionality as the `Get-CacheHost` cmdlet in previous versions of AppFabric Caching.

The `Stop-SPDistributedCacheServiceInstance` cmdlet is improved to better support graceful shutdowns. You can specify the `-Graceful` switch parameter with the cmdlet to ensure that the cached data in a Distributed Cache service instance is transferred to another Distributed Cache service instance before the first service instance shuts down. 

You can specify the time limit for a graceful shutdown data transfer to complete via the `-Timeout` parameter.  If the `-Timeout` parameter isn't specified, the default is 900 seconds (5 minutes). You can also specify the `-Force` switch parameter to force a Distributed Cache service instance to shut down, even if it isn’t able to complete a graceful shutdown before it times out.

To improve the management of Distributed Cache in SharePoint Server Subscription Edition, the following new PowerShell cmdlets are introduced:

 - `New-SPCache`
 
 - `Get-SPCache`
 
 - `Get-SPCacheStatistics`
 
These cmdlets work similar to the `New-Cache`,`Get-Cache`, and `Get-CacheStatistics` cmdlets of AppFabric Cache in previous versions of SharePoint.

### New-SPWebApplication PowerShell cmdlet
<a name="spweb"> </a>
  
In previous versions of SharePoint, you had to specify the `AuthenticationProvider` parameter in the `New-SPWebApplication` and `New-SPWebApplicationExtension` PowerShell cmdlets to create web applications using Windows Claims authentication. If you didn't, the web application would have been created in the Windows Classic authentication mode and you would have received a warning. 

As the Windows Classic authentication mode is no longer supported, the behaviors of these PowerShell cmdlets have changed when you don't specify the `AuthenticationProvider` parameter. In SharePoint Server Subscription Edition, the PowerShell cmdlet creates web applications in Windows claims mode by default and the warning message will no longer be displayed. The Central Administration web application will continue to use Windows Classic authentication.

### New People Picker cmdlets
<a name="nppc"> </a>

We've added the following PowerShell cmdlets to configure the People Picker and replace the stsadm.exe commands described in [Configure People Picker (SharePoint Server 2010)](https://docs.microsoft.com/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14)).

 - `Get-SPPeoplePickerConfig`

 - `Set-SPPeoplePickerConfig`

 - `Add-SPPeoplePickerSearchADDomain`

 - `Clear-SPPeoplePickerSearchADDomain`

 - `Get-SPPeoplePickerSearchADDomain`

 - `Remove-SPPeoplePickerSearchADDomain`

 - `Add-SPPeoplePickerDistributionListSearchDomain`

 - `Clear-SPPeoplePickerDistributionListSearchDomain`

 - `Get-SPPeoplePickerDistributionListSearchDomain`

 - `Remove-SPPeoplePickerDistributionListSearchDomain`

 - `Add-SPPeoplePickerServiceAccountDirectoryPath`

 - `Clear-SPPeoplePickerServiceAccountDirectoryPath`

 - `Remove-SPPeoplePickerServiceAccountDirectoryPath`

### Introducing Remove-SPConfigurationObject PowerShell cmdlet
<a name="resp"> </a>
  
The `Remove-SPConfigurationObject` PowerShell cmdlet replaces the `stsadm.exe -o deleteconfigurationobject` command.  

Its parameters are:

 - `[-Identity] <guid>`: The GUID of the object in the SharePoint configuration database to delete.
   
 - `[-Force]`: Specifies that the object will be deleted without confirmation that you want to proceed. This can be used for scripts that don't support interactive confirmation prompts.

> [!WARNING]
> Improper usage of this cmdlet has the potential to destroy necessary data in a SharePoint configuration database, requiring a complete rebuild of the SharePoint farm. Use it only under guidance with Microsoft Support.

### SharePoint Volume Shadow Copy Service writer cmdlets
<a name="vscs"> </a>
  
To improve the management of the [SharePoint Volume Shadow Copy Service (VSS) writer](https://docs.microsoft.com/sharepoint/dev/general-development/overview-of-sharepoint-and-the-volume-shadow-copy-service), the following new PowerShell cmdlets are introduced:

 - `Register-SPVssWriter`
 
 - `Unregister-SPVssWriter`
 
These cmdlets perform the same actions as the [stsadm.exe -o registerwsswriter](https://docs.microsoft.com/previous-versions/office/sharepoint-2007-products-and-technologies/cc262819(v=office.12))and [stsadm.exe -o unregisterwsswriter](https://docs.microsoft.com/previous-versions/office/sharepoint-2007-products-and-technologies/cc262416(v=office.12)) commands.

## Search

### Search result page modernization
<a name="seres"> </a>
  
We're bringing modern experiences from SharePoint in Microsoft 365 to the search result page in SharePoint Server Subscription Edition to make it more compelling, flexible, and easier to use. This will provide a closer look and feel to Microsoft 365.

The following features have been modernized and introduced into this release:

 - Centralized search bar.
 
 - Content type filters including **All**, **Files**, **Sites**, and **News**. **All** is introduced to have the results of **Files**, **Sites**, and **News**.
 
 - Duration filter. Filter content by time scope.
  
### Support for returning list content in modern results page
<a name="listmrp"> </a>
  
Lists and list items are now searchable in the modern UX. List item results will be included in the **All** category of the modern search result page.

### Thumbnails in modern search result page
<a name="tmsr"> </a>

The modern search result page will now show thumbnails for popular document and image file types such as PDF, Word, PowerPoint, PNG, JPEG, GIF, and more.

## Security

### SSL certificate management
<a name="sslcm"> </a>
  
SharePoint farm administrators can now directly manage the deployment and lifecycle of SSL/TLS certificates in their SharePoint Server farms. Certificate management is built on a modern and flexible infrastructure that supports both Elliptic Curve Cryptography (ECC) and classic RSA certificates.

Certificate management capabilities include:
  
  - Generating new/renewal certificate signing requests (CSRs) to submit to their certificate authorities.
  
  - Importing/exporting certificates, with or without private keys.

  - Viewing certificate properties.
  
  - Automatically deploy/retract certificates to each server in their SharePoint farm. 
  
  - Assigning/unassigning certificates to web applications. 
  
  - Automated scanning and notification of certificates that will soon expire or have already expired based on thresholds that can be configured by farm administrators. 
  
  - Certificate management functionality exposed via PowerShell command line and Central Admin UI. 
 
  - Administrative logging of all certificate management operations for auditing purposes

  - Public APIs allow external tools to integrate with the SharePoint certificate management feature.
  
### TLS 1.3 
<a name="tlss"> </a>

Transport Layer Security (TLS) is a cryptographic protocol that encrypts communication between two endpoints, such as between a web browser and an HTTPS web site. TLS 1.3 is the latest and most secure version of the TLS protocol.

SharePoint Server Subscription Edition supports TLS 1.3 by default when deployed with Windows Server 2022 or higher. TLS 1.3 is not available and is not supported when SharePoint Server Subscription Edition is deployed with earlier versions of Windows Server.
  
> [!NOTE]
> Not all applications in your software ecosystem may support TLS 1.3. Check with your software vendors to determine if your other applications support TLS 1.3. SharePoint Server Subscription Edition can fall back to earlier TLS protocol versions when connecting with systems that don't support TLS 1.3 unless the customer has disabled earlier TLS protocol versions.
  
### Strong TLS encryption by default
<a name="tlsed"> </a>

SharePoint Server Subscription Edition will use the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to SharePoint sites only use the strongest encryption by default. SharePoint Server will configure itself to enforce the minimum TLS version and cipher suite requirements of HTTP/2 on its SSL bindings regardless of whether the connection uses HTTP/2. Specifically:

 - The SSL/TLS protocol version negotiated must be TLS 1.2 or higher.

 - The TLS cipher suite negotiated must support forward secrecy and AEAD encryption modes such as GCM.

Customers can allow legacy encryption to be used if needed for backward compatibility with older software that doesn't support strong TLS protocol versions and cipher suites.

SharePoint Server Subscription Edition supports strong TLS encryption by default when deployed with Windows Server 2022 or higher. This capability is not available in earlier versions of Windows Server. 

### Improved ASP.NET view state security and key management
<a name="aspnet"> </a> 

SharePoint now encrypts the `machineKey` section of its `web.config` files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys even if they gain access to those `web.config` files.

Farm administrators can also change the ASP.NET view state decryption and validation keys of a SharePoint web application through two new PowerShell cmdlets. This allows you to rotate those keys in your farm.

## Sites, Lists, and Libraries

### Accessibility improvements across modern UX
<a name="aiamu"> </a>
  
SharePoint Server Subscription Edition includes a variety of accessibility improvements to the modern UX to ensure that all users can be productive with SharePoint.

### Brick layout for document library thumbnails and image gallery web part
<a name="briclil"> </a>
  
SharePoint Server Subscription Edition introduces the Brick layout as a layout option in modern document libraries and the image gallery web part. The Brick layout displays several images of various sizes, automatically arranged in a pattern similar to a brick wall. The Brick layout respects the aspect ratio of all images shown, including 16:9, 4:3, 1:1, and so on.

### Bulk check-in/check-out in modern document library experience
<a name="bulkinout"> </a>
  
Checking out a file from a document library allows you to make changes to a file while preventing others from making changes to that file. Once you're done making changes to the file, checking it in to the document library will allow others to see your changes.

Now with bulk check-out and check-in, you can select multiple files and perform the check-out and check-in operations on all of that at the same time. This saves you time by avoiding repetitive steps.
  
### Bulk download files from document library and OneDrive personal sites
<a name="bulkdod"> </a>
  
SharePoint Server Subscription Edition now supports downloading multiple files at once from document libraries and OneDrive personal sites.
You can select multiple files and folders and then click **Download** in the command bar. SharePoint will compress the selected files and folders into a ZIP file and then download the ZIP file to the user. 

If users select a single file and click **Download** in the command bar, the file will continue to be directly downloaded to the user.

The following are limitation on the bulk download feature: 

 1.	Each single file can't exceed 10 GB.
 
 2.	Total size of all the selected files can't exceed 20 GB.
 
 3.	Maximum level of folders is limited to 100 levels.
 
 4.	No more than 10000 files can be downloaded at once.
  
For more information about this feature, see [Download files and folders from OneDrive or SharePoint](https://support.microsoft.com/office/download-files-and-folders-from-onedrive-or-sharepoint-5c7397b7-19c7-4893-84fe-d02e8fa5df05).
  
### Image and document thumbnails in document libraries and picture libraries
<a name="idt"> </a>

SharePoint Server Subscription Edition can render thumbnails of files in the Tiles view of document libraries and picture libraries. SharePoint will render thumbnails of popular image file formats such as PNG, JPEG, GIF, and more. And if you've linked your SharePoint Server farm to an Office Online Server farm, SharePoint will also be able to render thumbnails of popular document formats such as PDFs, Word documents, PowerPoint documents, and Rich Text Files.
  
### List and library modern web parts support adding/editing/deleting content
<a name="llmw"> </a>

SharePoint Server Subscription Edition adds the ability to perform the following actions in modern document library and modern list web parts:

 - Document library web part: create, upload, share, download, rename, delete, and edit documents and folders.
 
 - List web part: create, edit, and delete list items.
  
### Modern document sets
<a name="mds"> </a> 
  
A Document Set is a group of related documents that you can manage as a single entity. In previous versions of SharePoint Server, document sets only supported the classic UX. Now in SharePoint Server Subscription Edition, Document Sets have been enhanced to support the modern experience in document libraries.

## Storage

### Remote Share Provider
<a name="blob"> </a>  
  
In SharePoint Server Subscription Edition, Remote Share Provider, a new Remote BLOB Storage (RBS) provider, is introduced to enable customer to offload BLOB storages from SQL server to low cost remote SMB system. 

By using this new technology, customer can shift data storage from costly SQL server to low cost SMB file storage. And also it can enlarge the total size of contents in same content database as BLOB is offload to remote system.
  
### Remote Share Provider diagnostic tool
<a name="rspdt"> </a>
  
To support new Remote Share Provider, SharePoint Server Subscription Edition provides a new PowerShell cmdlet tool to admin to validate the data consistency of content database which is remote share provider enabled. It provides an easy way for checking healthy of content database and remote storage, and for troubleshooting storage problem.

