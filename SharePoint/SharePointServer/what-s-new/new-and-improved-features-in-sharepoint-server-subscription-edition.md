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

Learn about the new features and updates to existing features in SharePoint Server Subscription Edition.

## List of new features and updates to existing features

The following table provides the list of new features and updates to existing features in SharePoint Server Subscription Edition.

|**Feature Group**|**Features**|**More info**|
|:-----|:-----|:-----|
|Authentication and Identity Management <br/> | <ul><li>Adds support for OpenID Connect (OIDC) 1.0</li><li>Enhanced People Picker for trusted identity providers</li><li>Improved Integrated Windows authentication over TLS</li></ul> | <ul><li>For more information, see [ODIC authentication 1.0](#ODIC).</li><li>For more information, see [People picker PowerShell cmdlet improvement for trusted authentication method](#people).</li><li>For more information, see [Improved Integrated Windows authentication over TLS](#IIW).</li></ul> | 
|Deployment and Upgrade <br/> | <ul><li>Adds support for Windows Server 2022</li><li>Adds support for Windows Server Core</li><li>Supports "N - 2" upgrading from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)</li><li>AppFabric Cache integration</li></ul> | <ul><li>For more information, see [Windows Server 2022](#server).</li><li>For more information, see [Windows Server Core](#core).</li><li>For more information, see [Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)](#upgrade).</li><li>For more information, see [AppFabric Cache integration](#cache).</li></ul> |
|Farm Administration <br/> | <ul><li>Adds support for host header bindings on Central Admin web application</li><li>Adds support for Server Name Indication (SNI) for host header bindings</li><li>Change web application bindings</li><li>Easier AAM configuration for Central Administration</li><li>Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and Subscription Edition)</li><li>Support for client certificate authentication to SMTP servers</li></ul> | <ul><li>For more information, see [Central Administration now supports host header bindings](#cenadmin).</li><li>For more information, see [Server Name Indication](#sni).</li><li>For more information, see [Change web application IIS bindings](#webiis).</li><li>For more information, see [Easier AAM configuration for Central Administration](#aamcon).</li><li>For more information, see [Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and 2022)](#fedral).</li><li>For more information, see [Client certificate authentication to SMTP servers](#client).</li></ul> |
|Hybrid <br/> | <ul><li>Better integration with Power Apps and Power Automate</li><li>Cloud SSA (Search) supports Microsoft 365 Multi-Geo</li><li>Improved hybrid search troubleshooting</li></ul> | <ul><li>For more information, see [PowerApps and Power Automate integration](#power).</li><li>For more information, see [Cloud SSA (Search) supports Microsoft 365 Multi-Geo](#ssa).</li><li>For more information, see [Improved hybrid search troubleshooting](#ihst).</li></ul> | 
|PowerShell <br/> | <ul><li>SharePoint PowerShell cmdlets converted from snap-in to module</li><li>Distributed Cache cmdlets</li><li>New-SPWebApplication creates web applications in Windows claims mode by default</li><li>Remove-SPConfigurationObject cmdlet</li><li>SharePoint Volume Shadow Copy Service writer cmdlets</li></ul> | <ul><li>For more information, see [SharePoint PowerShell cmdlets converted from snap-in to module](#snap).</li><li>For more information, see [Distributed Cache cmdlets](#dcc).</li><li>For more information, see [New-SPWebApplication PowerShell cmdlet](#spweb).</li><li>For more information, see [Introducing Remove-SPConfigurationObject PowerShell cmdlet](#resp).</li><li>For more information, see [SharePoint Volume Shadow Copy Service writer cmdlets](#vscs).</li></ul> |
|Search <br/> | <ul><li>Search result page modernization</li><li>Support for returning list content in modern results page</li><li>Thumbnails in modern search result page</li></ul> | <ul><li>For more information, see [Search result page modernization](#seres).</li><li>For more information, see [Support for returning list content in modern results page](#listmrp).</li><li>For more information, see [Thumbnails in modern search result page](#tmsr).</li></ul> |
|Security <br/> | <ul><li>SSL certificate management</li><li>Adds support for TLS 1.3</li><li>Strong TLS encryption by default</li><li>Improved ASP.NET view state security and key management</li></ul> | <ul><li>For more information, see [SSL certificate management](#sslcm).</li><li>For more information, see [TLS 1.3 support](#tlss).</li><li>For more information, see [Strong TLS encryption by default](#tlsed).</li><li>For more information, see [Improved ASP.NET view state security and key management](#aspnet).</li></ul> |
|Sites, Lists, and Libraries <br/> | <ul><li>Accessibility improvements</li><li>Brick layout for document library thumbnails and image gallery web part</li><li>Bulk check-in and check-out</li><li>Bulk download files from document libraries and OneDrive personal sites</li><li>Image and document thumbnails in document libraries and picture libraries</li><li>List and library modern web parts support adding/editing/deleting content</li><li>Modern document sets</li></ul> | <ul><li>For more information, see [Accessibility improvements across modern UX](#aiamu).</li><li>For more information, see [Brick layout for document library thumbnails and image gallery web part](#briclil).</li><li>For more information, see [Bulk check-in/check-out in modern Document library experience](#bulkinout).</li><li>For more information, see [Bulk download files from document libraries and OneDrive personal sites](#bulkdod).</li><li>For more information, see [Image and document thumbnails in document libraries and picture libraries](#idt).</li><li>For more information, see [List and library modern web parts support adding/editing/deleting content](#llmw).</li><li>For more information, see [Modern document sets](#mds).</li></ul> |
|Storage <br/> | <ul><li>New BLOB storage provider: Remote Share Provider</li><li>Remote Share Provider diagnostic tool</li></ul> | <ul><li>For more information, see [Remote Share Provider](#blob).</li><li>For more information, see [Remote Share Provider diagnostic tool](#rspdt).</li></ul> | 

## Detailed description of features

This section provides detailed descriptions of the new and updated features in SharePoint Server Subscription Edition.

### ODIC authentication 1.0
<a name="ODIC"> </a>

SharePoint Server Subscription Edition now supports OpenID Connect (OIDC) 1.0 authentication protocol. You can set up an OIDC enabled `SPTrustedIdentityTokenIssuer` that works with remote identity provider to enable OIDC authentication. Basic manual OIDC configuration through PowerShell is also enabled. It supports OIDC meta data discovery capability during configuration.
By using the metadata endpoint provided from OIDC identity provider, some of the following configurations are retrieved: 
 1.	Certificate
 2.	Issuer
 3.	Authorization Endpoint
 4.	SignoutURL
 
This simplifies the configuration of OIDC token issuer. 

SharePoint Server Subscription Edition also supports rotational signing certificates scenario for `id_token` validation. `ImportTrustCertificate` parameter of `New-SPTrustedIdentityTokenIssuer` is updated to support a list of certificate objects.

### People picker PowerShell cmdlet improvement for trusted authentication method
<a name="people"> </a>

In SharePoint Server Subscription Edition people picker is enchaned to search and pick user in UPA to help you avoid creating a customized claim provider. With the improved PowerShell cmdlet you can easily reconfigure `SPTrustedIdentityTokenIssuer` and `UPABackedClaimProvider`.

### Improved Integrated Windows authentication over TLS
<a name="IIW"> </a>

Internet Information Services (IIS) 10 advertises support for HTTP/2 during TLS negotiation, letting you know that you can use HTTP/2 once the Transport Layer Security (TLS) connection is complete. However, HTTP/2 and above are not compatible with Integrated Windows authentication protocols such as Negotiate (Kerberos) and New Technology LAN Manager (NTLM). 

If a server detects that a client is attempting to perform Kerberos or NTLM authentication over an HTTP/2 or HTTP/3 connection, it will notify the client to downgrade the connection to HTTP/1.1 and restart the attempt. This results in extra round trips between the client and the server during authentication, which increases latency. Even worse, some web browsers do not handle this notification well. Chromium-based web browsers such as **new** Edge and Chrome will show a connection error message to the end user for a few seconds before retrying the authentication over HTTP/1.1.

SharePoint Server Subscription Edition will avoid this increased latency and connection error messages described above by disabling HTTP/2 and QUIC (Quick UDP Internet Connections) in SharePoint IIS web sites when Negotiate (Kerberos) or NTLM are enabled. HTTP/2 and QUIC will continue to be available on SharePoint IIS web sites that aren't configured to use Negotiate (Kerberos) or NTLM.

### Windows Server 2022
<a name="server"> </a>

Windows Server 2022 includes a variety of new features and improvements in virtualization, networking, security, and more, such as:

 - Performance improvements in the Hyper-V virtual switch to reduce CPU load.
 
 - Performance improvements in both TCP and UDP networking to maximize bandwidth, minimizing packet loss, and reduce CPU load.
 
 - Support for TLS 1.3, the latest and strongest connection encryption standard.
 
 - Support for AES-256-GCM encryption in SMB file sharing, along with compressed file transfers over the network when using the `robocopy.exe` and `xcopy.exe` tools with the `/compress` parameter.

### Windows Server Core
<a name="core"> </a>

Windows Server Core is a leaner Windows Server deployment type compared to the classic Windows Server with Desktop Experience. Server Core minimizes the number of OS features and services that are installed and running to only those that are truly needed for a server. This reduces the demand on system resources (CPU, RAM, and disk space) as well as the potential attack surface for security vulnerabilities.

### Upgrading directly from SharePoint 2016 and SharePoint 2019 (and Project Server 2016 and 2019)
<a name="upgrade"> </a>

SharePoint Server Subscription Edition supports both **N - 1** and **N - 2** version-to-version upgrade. You can upgrade directly from the following SharePoint products using the standard database attach upgrade procedure:

 - SharePoint Server 2019 (including Project Server 2019)
 
 - SharePoint Server 2016 (including Project Server 2016)

SharePoint Server Subscription Edition doesn’t support upgrading directly from earlier versions of SharePoint such as SharePoint Server 2013, SharePoint Server 2010, etc. You need to first upgrade to SharePoint Server 2016 or SharePoint Server 2019 before you can upgrade to SharePoint Server Subscription Edition.

### AppFabric Cache integration
<a name="cache"> </a>

You no longer need to install a separate AppFabric Velocity Cache component. SharePoint Server Subscription Edition setup will automatically install all the necessary files, and SharePoint patches will update them.

### Central Administration now supports host header bindings
<a name="cenadmin"> </a>

You can now configure the SharePoint Central Administration web site to use a host header binding, which will allow it to share the same TCP port number as other web sites.  This would typically be used to let the SharePoint Central Administration site and your content web site to be hosted on the same TCP port, such as port 443 for SSL.

To configure this, specify the host header binding with the `-HostHeader` parameter of the `New-SPCentralAdministration` and `Set-SPCentralAdministration` cmdlets, or with the `-hostheader` parameter of the `psconfig.exe -cmd adminvs` command.

### Server Name Indication (SNI)
<a name="sni"> </a>

Server Name Indication (SNI) allows multiple IIS web sites with unique host headers and unique server certificates to share the same Secure Sockets Layer (SSL) port. The server examines the server name specified by the client during the SSL handshake to determine which server certificate should be used to complete the connection. Your IIS web site must have a host header and must use SSL to use Server Name Indication. If Server Name Indication isn't used, all IIS web sites sharing the same SSL port will share the same server certificate.

Server Name Indication can be configured by the **Use Server Name Indication** setting on the **Create New Web Application** and **Extend Web Application** pages in SharePoint Central Administration.  

It can also be configured by the following commands:

 - `psconfig.exe-adminvs-port<port number>-hostheader <host header>-ssl-usesni`
  
 - `New-SPCentralAdministration -Port <port number>-HostHeader<host header>-SecureSocketsLayer-UseServerNameIndication`
  
 - `Set-SPCentralAdministration -Port <port number>-HostHeader<host header>-SecureSocketsLayer-UseServerNameIndication` 
 
 - `New-SPWebApplication ...-Port <port number>-HostHeader<host header>-SecureSocketsLayer-UseServerNameIndication`
  
 - `Set-SPWebApplication ...-Port <port number>-HostHeader<host header>-SecureSocketsLayer-UseServerNameIndication`
  
 - `New-SPWebApplicationExtension ...-Port <port number>-HostHeader<host header>-SecureSocketsLayer-UseServerNameIndication` 

### Change web application IIS bindings
<a name="webiis"> </a>
  
You can change your web application IIS bindings in SharePoint Server Subscription Edition by using the `Set-SPWebApplication` cmdlet. This functionality is supported in all web application zones.

For example, you can run the following PowerShell command to change a SharePoint web application on HTTP port 80 to use a host header binding on SSL port 443:

 ```PowerShell
Set-SPWebApplication -Identity http://servername -Zone Default -Port 443 -SecureSocketsLayer -HostHeader sharepoint.contoso.com -Url https://sharepoint.contoso.com
```

You can also change the SharePoint web application IIS bindings through Central Administration. The SharePoint farm administrators can use the Edit button in the **Web Application Management** page in Central Administration, to edit/select a web application's zone. Here you can change the IIS bindings, SSL certificate, and public URL of this web application's zone. This functionality is only available to user’s who are a member of the local Administrators group on the server.

### Easier AAM configuration for Central Administration
<a name="aamcon"> </a>

You can now specify the public AAM URL directly in the Central Administration command line tools, bringing them to parity with the content web application command line tools.  This can be specified via the optional `-Url <String>` parameter in the following PowerShell cmdlets and `PSConfig.exe` command line utility:

 - `New-SPCentralAdministration`
 
 - `Set-SPCentralAdministration`
 
 - `PSConfig.exe -cmd adminvs`
  
### Federated service applications support "N - 2" content farms (SharePoint 2016, 2019, and 2022)
<a name="fedral"> </a>
  
In SharePoint Server, some service applications can be shared across server farms. In this Subscription Edition support is provided for SharePoint publishing service applications to be consumed by SharePoint Server Subscription Edition, the **N - 1** (2019) version of SharePoint, or by the **N - 2** (2016) version of SharePoint.

For more information, see [Share service applications across farms in SharePoint Server](https://docs.microsoft.com/sharepoint/administration/share-service-applications-across-farms).

### Client certificate authentication to SMTP servers
<a name="client"> </a>

You can now authenticate to Simple Mail Transfer Protocol (SMTP) servers using client certificates. You need to import a client certificate into your farm using our SSL certificate management, then assign that client certificate to the outgoing email settings within the SharePoint farm.

### PowerApps and Power Automate integration
<a name="power"> </a>

Two new commands have been added to the modern document library page and modern list page command bar:

  - Power Automate
  
  - Power Apps
  
These commands will take you directly to the Power Apps and Power Automate service pages. 

### Cloud SSA (Search) supports Microsoft 365 Multi-Geo
<a name="ssa"> </a>
  
You can use PowerShell scripts to configure SharePoint hybrid features on Windows Server Core.

### Improved hybrid search troubleshooting
<a name="ihst"> </a>

There are two improvements added to Search Crawler Log in Center Admin UX. 
  
  - A new column called **online ID** is introduced to crawler log for all contents when SharePoint Farm is configured with hybrid cloud SSA. This **online ID** is SharePoint online search index for On-Premises contents in SharePoint Server.
  
  - New **Warning breakdown** pivot is added next to **Error breakdown** tab in crawler log page. It provides capability to administrators to exam through search crawler warning with same user experience as **Error breakdown** tab by listing all warnings instead of errors. 
  
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

To improve the management of Distributed Cache in SharePoint Server Subscription Edition , the following new PowerShell cmdlets are introduced:

 - `New-SPCache`
 
 - `Get-SPCache`
 
 - `Get-SPCacheStatistics`
 
These cmdlets work similar to the `New-Cache`,`Get-Cache`, and `Get-CacheStatistics` cmdlets of AppFabric Cache in previous versions of SharePoint.

### New-SPWebApplication PowerShell cmdlet
<a name="spweb"> </a>
  
In previous versions of SharePoint, you had to specify the `AuthenticationProvider` parameter in the `New-SPWebApplication` and `New-SPWebApplicationExtension` PowerShell cmdlets to create web applications using Windows Claims authentication. If you didn't, the web application would have been created in the Windows Classic authentication mode and you would have received a warning. 

As the Windows Classic authentication mode is no longer supported, the behavior of these PowerShell cmdlets have changed when you don't specify the `AuthenticationProvider` parameter. In SharePoint Server Subscription Edition, the PowerShell cmdlet creates web applications in Windows claims mode by default and the warning message will no longer be displayed. The Central Administration web application will continue to use Windows Classic authentication.

### Introducing Remove-SPConfigurationObject PowerShell cmdlet
<a name="resp"> </a>
  
The `Remove-SPConfigurationObject` PowerShell cmdlet replaces the `stsadm.exe -o deleteconfigurationobject` command.  

Its parameters are:

 - `[-Identity] <guid>`: The GUID of the object in the SharePoint configuration database to delete.
   
 - `[-Force]`: Specifies that the object will be deleted without confirmation that you want to proceed. This can be used for scripts that don't support interactive confirmation prompts.

> [!WARNING]
> Improper usage of this cmdlet has the potential to destroy necessary data in a SharePoint configuration database, requiring a complete rebuild of the SharePoint farm. It should only be used as directed by Microsoft Support.

### SharePoint Volume Shadow Copy Service writer cmdlets
<a name="vscs"> </a>
  
To improve the management of the [SharePoint Volume Shadow Copy Service (VSS) writer](https://docs.microsoft.com/sharepoint/dev/general-development/overview-of-sharepoint-and-the-volume-shadow-copy-service), the following new PowerShell cmdlets are introduced:

 - `Register-SPVssWriter`
 
 - `Unregister-SPVssWriter`
 
These cmdlets perform the same actions as the [stsadm.exe -o registerwsswriter](https://docs.microsoft.com/previous-versions/office/sharepoint-2007-products-and-technologies/cc262819(v=office.12))and [stsadm.exe -o unregisterwsswriter](https://docs.microsoft.com/previous-versions/office/sharepoint-2007-products-and-technologies/cc262416(v=office.12)) commands.

### Search result page modernization
<a name="seres"> </a>
  
We're introducing more modern experiences to the search result page in SharePoint Server Subscription Edition from SharePoint in Microsoft 365 to make it more compelling, flexible, mobile, and easier to use. This will provide a closer look and feel to Microsoft 365.

The following features have been modernized and introduced into this release:

 - Centralized search bar.
 
 - Content type filters including **All**, **Files**, **Sites**, and **News**. **All** is introduced to have the results of **Files**, **Sites**, and **News**.
 
 - Duration filter. Filter content by time scope.
  
### Support for returning list content in modern results page
<a name="listmrp"> </a>
  
Lists and list items are now searchable in the modern UX. List item results will be included in the **All** category of the modern search result page.

### Thumbnails in modern search result page
<a name="tmsr"> </a>

Thumbnail is introduced in modern user experience of result page for **PowerPoint**, **Word**, **PDF**, images and etc.
  
### SSL certificate management
<a name="sslcm"> </a>
  
This allows SharePoint farm administrators to directly manage the deployment and lifecycle of SSL/TLS server certificates in their SharePoint on-prem farms.

This includes: 
  
  - Generating new/renewal certificate signing requests (CSRs) to submit to their certificate authorities.
  
  - Importing/exporting/reviewing certificates (with & without private keys) stored within SharePoint. 
  
  - Deploying/retracting certificates to each server in their SharePoint farm. 
  
  - Assigning/unassigning/reviewing certificates for SharePoint web applications (and potentially other features). 
  
  - Automated scanning and admin notification of certificates that will soon expire (or have already expired). 
  
  - Certificate management functionality exposed via PowerShell command line and Central Admin UI. 
  
### TLS 1.3 support
<a name="tlss"> </a>

Windows Server 2022’s .NET Framework 4.8 supports TLS 1.3. This allows you to unblock testing TLS 1.3 with SharePoint Server Subscription Edition.
  
> [!NOTE]
> The following components still don't support TLS 1.3 yet: </br>
> 1. SQL Server 2019 </br>
> 2. Workflow Manager 1.0 and Service Bus 1.1 </br>
  
### Strong TLS encryption by default
<a name="tlsed"> </a>

SharePoint Server Subscription Edition will use the advanced security capabilities of Windows Server 2022 to ensure that TLS connections made to the server only uses the strongest encryption.
SharePoint Server will configure itself to enforce the minimum TLS version and cipher suite requirements on its SSL bindings regardless of whether the connection ends up using HTTP/2. 

### Improved ASP.NET view state security and key management
<a name="aspnet"> </a> 

SharePoint now encrypts the `machineKey` section of its `web.config` files by default. This prevents attackers from reading your ASP.NET view state encryption and validation keys even if they gain access to those `web.config` files.

It can also change the ASP.NET view state decryption and validation keys of a SharePoint web application through two new PowerShell cmdlets. This allows you to rotate those keys in your farm.

### Accessibility improvements across modern UX
<a name="aiamu"> </a>
  
Screen reader announces the incorrect position for menu items save and close, discard changes, and publish. Screen reader announces the incorrect position for command bar controls in documents page. Screen reader announces the incorrect position for command bar controls in documents page. It ensures buttons have discernible text.

### Brick layout for document library thumbnails and image gallery web part
<a name="briclil"> </a>
  
Brick layout respects the aspect ratio of all images shown in 16:9, 1:1, 4:3, and so on. With the Brick layout, you can show several images of various sizes, automatically **layered** in a pattern like that of a brick wall.

We introduce Brick layout in modern Document library and Image Gallery web part. You can add brick layout as an option in Image Gallery web part and change the layout of modern document library from Grid layout into Brick layout.

### Bulk check-in/check-out in modern Document library experience
<a name="bulkinout"> </a>
  
If you want to make changes to a file in a SharePoint document library, but keep others from making changes at the same time, check the file out of the document library. Once you're done making changes to the file, check it in from the library to upload your changes. 
Instead of checking-in or checking-out one file at a time, now you can select multiple files and check them in/out.
  
### Bulk download files from document libraries and OneDrive personal sites
<a name="bulkdod"> </a>
  
SharePoint Server Subscription Edition now supports downloading multiple files at once from document libraries and OneDrive personal sites.
You can select multiple files and folders and then click **Download** in the command bar. SharePoint will compress the selected files and folders into a ZIP file and then download the ZIP file to the user. 

If users select a single file and click **Download** in the command bar, the file will continue to be directly downloaded to the user.

The following are limitation on the bulk download feature: 

 1.	Each single file can't exceed 10GB.
 
 2.	Total size of all the selected files can't exceed 20GB.
 
 3.	Maximum level of folders are limited to 100 levels.
 
 4.	No more than 10000 files can be downloaded at once.
  
For more information about this feature, see [Download files and folders from OneDrive or SharePoint](https://support.microsoft.com/office/download-files-and-folders-from-onedrive-or-sharepoint-5c7397b7-19c7-4893-84fe-d02e8fa5df05).
  
### Image and document thumbnails in document libraries and picture libraries
<a name="idt"> </a>

For SharePoint Server Subscription Edition, image thumbnail returns to picture library. You can explore pictures not only by their names but also by their thumbnail.
Image thumbnail is not only supported in picture library, but also in modern document library, if you deploy OSS farm, you can enjoy the thumbnail of Word/PowerPoint/PDF file in document library.
  
### List and library modern web parts support adding/editing/deleting content
<a name="llmw"> </a>

With SharePoint Server Subscription Edition, you can do the following to documents and list items in the web part:

 - Document library web part: create, upload, share, download, rename, delete, and edit documents and folders.
 
 - List web part: create, edit, and delete list items.
  
### Modern document sets
<a name="mds"> </a> 
  
In SharePoint Server Subscription Edition, the Document Sets is enhanced so that you can enjoy the same modern experience when using Document Sets in modern document library.

### Remote Share Provider
<a name="blob"> </a>  
  
SharePoint managed account object is no longer required. Instead, `PSCredential` object will be used to store SMB storage credential and this object needs to be provided as the parameter of the cmdlet `Register-SPRemoteShareBlobStore`.
  
### Remote Share Provider diagnostic tool
<a name="rspdt"> </a>
  
This new PowerShell cmdlet helps admin to validate the data consistency of content database which is remote share provider enabled. This makes it easier for admin to figure out what are the problems in the remote storage.

