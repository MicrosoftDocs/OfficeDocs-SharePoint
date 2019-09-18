---
title: "Create web applications that use classic mode authentication in SharePoint Server"
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
ms.assetid: 57c6d1ee-e2b7-4b48-9865-354fe8cc8fe2
description: "Learn how to create a web application that uses classic mode (Windows-classic) authentication in SharePoint Server."
---

# Create web applications that use classic mode authentication in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In SharePoint Server, claims-based authentication is the default and preferred method of user authentication and is required to take advantage of server-to-server authentication and app authentication. In Central Administration, you can only configure claims-based authentication when you manage web applications. You can also use Microsoft PowerShell cmdlets. The use of classic mode authentication, also known as Windows classic authentication, is discouraged in SharePoint Server and you can only create or configure web applications for classic mode authentication with Microsoft PowerShell cmdlets.
  
> [!IMPORTANT]
> Office Online can be used only by SharePoint Server web applications that use claims-based authentication. Office Online rendering and editing will not work on SharePoint Server web applications that use classic mode authentication. If you migrate SharePoint 2010 web applications that use classic mode authentication to SharePoint Server 2016, you must migrate them to claims-based authentication to allow them to work with Office Online. For more information, see [Use Office Web Apps with SharePoint 2013](/webappsserver/use-office-web-apps-with-sharepoint-2013). 
  
To use Windows claims-based authentication instead (recommended), see [Create a web application that uses Windows-claims authentication](create-claims-based-web-applications.md). To convert a web application that uses classic mode to use claims-based authentication, see [Migrate from classic-mode to claims-based authentication in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server).
  
> [!IMPORTANT]
> The steps in this article apply to both SharePoint Foundation 2013 and SharePoint Server. 
  
## Before you begin
<a name="begin"> </a>

Before you perform this procedure, confirm the following:
  
- You have determined the design of your logical architecture.
    
    For additional information, see [Logical architecture components](/previous-versions/office/sharepoint-server-2010/cc263121(v=office.14)).
    
- You have planned authentication for your web application.
    
    For additional information, see [Plan for user authentication methods in SharePoint Server](/SharePoint/security-for-sharepoint-server/plan-user-authentication).
    
- If you use Secure Sockets Layer (SSL), you must associate the SSL certificate with the web application's IIS website after the IIS website is created. SSL is required by default for web applications that are used in server-to-server authentication and app authentication scenarios. 
    
- You understand host-named site collections.

    
## Create a web application that uses classic mode authentication with PowerShell
<a name="begin"> </a>

Perform the following procedure to use PowerShell to create a web application that uses classic mode authentication.
  
 **To create a web application that uses classic mode authentication with PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  New-SPWebApplication -Name <Name> -ApplicationPool <ApplicationPool> -AuthenticationMethod <WindowsAuthType> -ApplicationPoolAccount <ApplicationPoolAccount> -Port <Port> -URL <URL>
  ```

  Where:
    
  -  _\<Name\>_ is the name of the new web application. 
    
  -  _\<ApplicationPool\>_ is the name of the application pool. 
    
  -  _\< WindowsAuthType \>_ is either "NTLM" or "Kerberos". Kerberos is recommended. 
    
  -  _\<ApplicationPoolAccount\>_ is the user account that this application pool will run as. 
    
  -  _\<Port\>_ is the port on which the web application will be created in IIS. 
    
  -  _\<URL\>_ is the public URL for the web application. 
    
  - **Example**
    
  ```
  New-SPWebApplication -Name "Contoso Internet Site" -ApplicationPool "ContosoAppPool" -AuthenticationMethod "Kerberos" -ApplicationPoolAccount (Get-SPManagedAccount "CONTOSO\jdoe") -Port 80 -URL "https://www.contoso.com"
  ```

For more information, see New-SPWebApplication.PShell_stsadm_deprecated
  
After this procedure is complete, you can create one or more site collections for this web application. For more information, see [Create a site collection in SharePoint Server](/SharePoint/sites/create-a-site-collection).
  
After you successfully create the web application, when you open the Central Administration page, you see a health rule warning that indicates that one or more web applications is enabled with classic authentication mode. This is a reflection of our recommendation to use claims-based authentication instead of classic mode authentication.
  
## See also
<a name="begin"> </a>

#### Concepts

[Create a Web application that uses Windows-claims authentication)](create-claims-based-web-applications.md)
#### Other Resources

[Plan for user authentication methods in SharePoint Server](/SharePoint/security-for-sharepoint-server/plan-user-authentication)

