---
title: "Create claims-based web applications in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/20/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 83496762-172a-44a4-bf57-1d7ea8008d7d

description: "Illustrates how to create SharePoint Server web applications that use claims-based authentication or classic-mode authentication."
---

# Create claims-based web applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Claims-based authentication is a requirement to enable the advanced functionality of SharePoint Server. This article explains how to use either Central Administration or PowerShell to create a SharePoint Server web application that uses claims-based authentication. Claims-based authentication is a requirement for web applications that are deployed in scenarios that support server-to-server authentication and app authentication. However, this article also provides guidance for using PowerShell to create classic-mode web applications if you have a specific scenario that cannot support claims-based authentication. Be aware that classic-mode authentication is deprecated in this release, and it will not be available in the next version. For more information, see [Plan for server-to-server authentication in SharePoint Server](/SharePoint/security-for-sharepoint-server/plan-server-to-server-authentication)
  
> [!IMPORTANT]
> Secure Sockets Layer (SSL) is a requirement for web applications that are deployed in scenarios that support server-to-server authentication and app authentication. 
  
You can create a web application by using the SharePoint Central Administration website or PowerShell. You typically use PowerShell to create a web application. If you want to automate the task of creating a web application, which is common in enterprises, use PowerShell. After you complete the procedure, you can create one or several site collections.
    
## Create a claims-based web application by using Central Administration
<a name="section1"> </a>

Use the procedure described in this section to create a new claims-based SharePoint Server web application using the Central Administration.
  
 **To create a claims-based web application by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
  - To create a web application, you must be a member of the Farm Administrators SharePoint group.
    
2. Start SharePoint 2016 Central Administration.
    
3. On the Central Administration Home page, click **Application Management**.
    
4. On the **Application Management** page, in the **Web Applications** section, click **Manage web applications**.
    
5. In the **Contribute** group of the ribbon, click **New**.
    
6. On the **Create New Web Application** page, in the **IIS Web Site** section, you can configure the settings for your new web application by selecting one of the following two options: 
    
  - Click **Use an existing IIS web site**, and then select the web site on which to install your new web application.
    
  - Click **Create a new IIS web site**, and then type the name of the web site in the **Name** box. 
    
  - In the **Port** box, type the port number you want to use to access the web application. If you are using an existing web site, this field contains the current port number. 
    
    > [!NOTE]
    > The default port number for HTTP access is 80, and the default port number for HTTPS access is 443. 
  
  - Optional: In the **IIS Web Site** section, in the **Host Header** box, type the host name (for example, www.contoso.com) that you want to use to access the web application. 
    
    > [!NOTE]
    > You do not need to populate this field unless you want to configure two or more IIS web sites that share the same port number on the same server, and DNS has been configured to route requests to the same server. 
  
  - In the **Path** box, type the path to the IIS web site home directory on the server. If you are creating a new web site, this field contains a suggested path. If you are using an existing web site, this field contains the current path of that web site. 
    
7. In the **Security Configuration** section, choose whether or not to **Allow Anonymous** access and whether or not to **Use Secure Sockets Layer (SSL)**.
    
    > [!IMPORTANT]
    > Secure Sockets Layer (SSL) is a requirement for web applications that are deployed in scenarios that support server-to-server authentication and app authentication. In general, we strongly recommend using SSL for web applications. 
  
  - In the **Security Configuration** section, click **Yes** or **No** for the **Allow Anonymous** options. If you choose to **Yes**, visitors can use the computer-specific anonymous access account (that is, IIS_IUSRS) to access the web site.
    
    > [!NOTE]
    > If you want users to be able to access any site content anonymously, you must enable anonymous access for the entire web application zone before you enable anonymous access at the SharePoint Server site level. Later, site owners can configure anonymous access for their sites. If you do not enable anonymous access at the web application level, site owners cannot enable anonymous access at the site level. 
  
  - In the **Security Configuration** section, click **Yes** or **No** for the **Use Secure Sockets Layer (SSL)** options. If you choose **Yes**, you must request and install an SSL certificate to configure SSL. 
    
8. In the **Claims Authentication Types** section, select the authentication method that you want to use for the web application. 
    
  - To enable Windows authentication, select **Enable Windows Authentication** and, in the drop-down menu, select **NTLM** or **Negotiate (Kerberos)**. We recommend using Negotiate (Kerberos).
    
    If you do not want to use Integrated Windows authentication, clear **Integrated Windows authentication**.
    
    > [!NOTE]
    > If you do not select Windows Authentication for at least one zone of this web application, crawling for this web application will be disabled. 
  
  - If you want users' credentials to be sent over a network in a nonencrypted form, select **Basic authentication (credentials are sent in clear text)**.
    
    > [!NOTE]
    > You can select basic authentication or integrated Windows authentication, or both. If you select both, SharePoint Server offers both authentication types to the client web browser. The client web browser then determines which type of authentication to use. If you only select Basic authentication, ensure that SSL is enabled. Otherwise, a malicious user can intercept credentials. 
  
  - To enable forms-based authentication, select **Enable Forms Based Authentication (FBA)**, and then enter the **ASP.NET Membership provider name** and the **ASP.NET Role manager name**.
    
    > [!NOTE]
    > If you select this option, ensure that SSL is enabled. Otherwise, a malicious user can intercept credentials. 
  
  - If you have set up Trusted Identity Provider authentication by using PowerShell, the **Trusted Identity provider** check box is selected. 
    
9. In the **Sign In Page URL** section, choose one of the following options to sign into SharePoint Server: 
    
  - Select **Default Sign In Page URL** to redirect users to a default sign-in web site for claims-based authentication. 
    
  - Select **Custom Sign In page URL** and then type the sign-in URL to redirect users to a customized sign-in web site for claims-based authentication. 
    
10. In the **Public URL** section, type the URL for the domain name for all sites that users will access in this web application. This URL will be used as the base URL in links that are shown on pages within the web application. The default URL is the current server name and port, and it is automatically updated to reflect the current SSL, host header, and port number settings on the page. If you deploy SharePoint Server behind a load balancer or proxy server, then this URL may need to be different than the SSL, host header, and port settings on this page. 
    
    The **Zone** value is automatically set to **Default** for a new web application. You can change the zone when you extend a web application. 
    
11. In the **Application Pool** section, do one of the following: 
    
  - Click **Use existing application pool**, and then select the application pool that you want to use from the drop-down menu.
    
  - Click **Create a new application pool**, and then type the name of the new application pool, or keep the default name.
    
  - Click **Predefined** to use a predefined security account for this application pool, and then select the security account from the drop-down menu. 
    
  - Click **Configurable** to specify a new security account to be used for an existing application pool. 
    
    > [!NOTE]
    > To create a new account, click the **Register new managed account** link. 
  
12. In the **Database Name and Authentication** section, choose the database server, database name, and authentication method for your new web application, as described in the following table. 
    
|**Item**|**Action**|
|:-----|:-----|
|**Database Server** <br/> |Type the name of the database server and SQL Server instance you want to use in the format < _SERVERNAME_\ _instance_>. You can also use the default entry.  <br/> |
|**Database Name** <br/> |Type the name of the database, or use the default entry.  <br/> |
|**Database Authentication** <br/> | Select the database authentication to use by doing one of the following:  <br/>  To use Windows authentication, leave this option selected. We recommend this option because Windows authentication automatically encrypts the password when it connects to SQL Server.  <br/>  To use SQL authentication, click **SQL authentication**. In the **Account** box, type the name of the account that you want the web application to use to authenticate to the SQL Server database, and then type the password in the **Password** box.  <br/> > [!NOTE]>  SQL authentication sends the SQL authentication password to SQL Server in an unencrypted format. We recommend that you only use SQL authentication if you force protocol encryption to SQL Server to encrypt your network traffic by using IPsec.           |
   
13. If you use database mirroring, in the **Failover Server** section, in the **Failover Database Server** box, type the name of a specific failover database server that you want to associate with a content database 
    
14. In the **Service Application Connections** section, select the service application connections that will be available to the web application. In the drop-down menu, click **default** or **[custom]**. You use the **[custom]** option to choose the service application connections that you want to use for the web application. 
    
15. In the **Customer Experience Improvement Program** section, click **Yes** or **No**.
    
16. Click **OK** to create the new web application. 
    
## Create a claims-based web application by using PowerShell
<a name="section2"> </a>

Use the procedure in this section to create a new claims-based SharePoint Server web application using PowerShell.
  
 **To create a claims-based web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 15 Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. To create a claims-based authentication provider, from the PowerShell command prompt, type the following:
    
  ```
  $ap = New-SPAuthenticationProvider
  ```

3. To create a claims-based web application, from the PowerShell command prompt, type the following:
    
  ```
  New-SPWebApplication -Name <Name> 
  -ApplicationPool <ApplicationPool> 
  -ApplicationPoolAccount <ApplicationPoolAccount> 
  -URL <URL> -Port <Port> -AuthenticationProvider $ap
  ```

  Where:
    
  -  _\<Name\>_ is the name of the new web application that uses claims-based authentication. 
    
  -  _\<ApplicationPool\>_ is the name of the application pool. 
    
  -  _\<ApplicationPoolAccount\>_ is the user account that this application pool will run as. 
    
  -  _\<URL\>_ is the public URL for this web application. 
    
  -  _\<Port\>_ is the port on which the web application will be created in IIS. 
    
    > [!NOTE]
    > For more information, see [New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps). 
  
    The following example creates an https claims-based web application, using the current user credentials and the current machine name:
    
  ```
  $ap = New-SPAuthenticationProvider
  New-SPWebApplication -Name "Contoso Internet Site" -URL "https://www.contoso.com"  -Port 80 
  -ApplicationPool "ContosoAppPool" 
  -ApplicationPoolAccount (Get-SPManagedAccount "DOMAIN\jdoe") 
  -AuthenticationProvider $ap -SecureSocketsLayer
  ```

    > [!NOTE]
    > After you have created the web site, you must configure SSL in IIS for this newly created web site. 
  
## Create a classic-mode web application by using PowerShell
<a name="section3"> </a>

Use the procedure in this section to create a new classic-mode SharePoint Server web application using PowerShell.
  
 **To create a classic-mode web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
2. From the PowerShell command prompt, type the following:
    
  ```
  New-SPWebApplication -Name <Name> 
  -ApplicationPool <ApplicationPool>
  -AuthenticationMethod <WindowsAuthType>
  -ApplicationPoolAccount <ApplicationPoolAccount>
  -Port <Port> -URL <URL>
  ```

  Where:
    
  -  _\<Name\>_ is the name of the new web application that uses classic-mode authentication. 
    
  -  _\<ApplicationPool\>_ is the name of the application pool. 
    
  -  _\<WindowsAuthType\>_ is either "NTLM" or "Kerberos". Kerberos is recommended. 
    
  -  _\<ApplicationPoolAccount\>_ is the user account that this application pool will run as. 
    
  -  _\<Port\>_ is the port on which the web application will be created in IIS. 
    
  -  _\<URL\>_ is the public URL for the web application. 
    
    > [!NOTE]
    > For more information, see [New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps). 
  
    > [!NOTE]
    > After you successfully create the web application, when you open the Central Administration page, you see a health rule warning that indicates that one or more web applications is enabled with classic authentication mode. This is a reflection of our recommendation to use claims-based authentication instead of classic mode authentication. 
  
## See also
<a name="section3"> </a>

#### Concepts

[Create a Web application that uses classic mode authentication in SharePoint 2013](create-web-applications-that-use-classic-mode-authentication.md)

