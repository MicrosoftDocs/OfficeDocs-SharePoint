---
title: "Migrate from classic-mode to claims-based authentication in SharePoint 2013"
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
ms.assetid: 85d03a6f-83ec-498d-b8a5-775b2c4fe74e
description: "Convert SharePoint 2010 Products or SharePoint 2013 classic-mode web applications to claims-based authentication or create new claims-based web applications in SharePoint 2013."
---

# Migrate from classic-mode to claims-based authentication in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Claims-based authentication is an essential component to enable the advanced functionality of SharePoint 2013. To move classic-mode web applications from SharePoint 2010 Products to SharePoint 2013, you can convert them to claims-based web applications within SharePoint 2010 Products, and then migrate them to SharePoint 2013. The procedures in this article illustrate various supported scenarios.
  
The PowerShell **Convert-SPWebApplication** cmdlet in SharePoint 2013 converts classic-mode web applications to claims-based web applications. 
  
> [!CAUTION]
> After you convert a web application to claims-based authentication, you cannot revert it to classic-mode authentication. 
  
## Convert SharePoint 2010 Products classic-mode web applications to claims-based authentication in SharePoint 2010 Products and then upgrade to SharePoint 2013
<a name="section1"> </a>

In SharePoint 2010 Products, complete the following procedure to convert an existing web application to claims-based authentication. After you convert the web application to claims-based authentication, complete the additional step to migrate the web application to SharePoint 2013. To complete this procedure, you need the following information:
  
- The URL of the web application that you are converting:  _http://yourWebAppUrl_
    
- A user account to set as a site administrator:  _yourDomain\yourUser_
    
 **To convert a SharePoint 2010 Products web application to claims-based authentication**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050) (https://go.microsoft.com/fwlink/p/?LinkId=193050). 
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. From the PowerShell command prompt, type the following to set the specified user account as an administrator for the site:
    
  ```
  $WebAppName = "http://<yourWebAppUrl>"
  $wa = get-SPWebApplication $WebAppName
  $wa.UseClaimsAuthentication = $true
  $wa.Update()
  ```

  Where:
    
  -  _\<yourWebAppUrl\>_ is the URL of the web application. 
    
3. From the PowerShell command prompt, type the following to configure the policy to enable the user to have full access:
    
  ```
  $account = "yourDomain\yourUser"
  $account = (New-SPClaimsPrincipal -identity $account -identitytype 1).ToEncodedString()
  $wa = get-SPWebApplication $WebAppName
  $zp = $wa.ZonePolicies("Default")
  $p = $zp.Add($account,"PSPolicy")
  $fc=$wa.PolicyRoles.GetSpecialRole("FullControl")
  $p.PolicyRoleBindings.Add($fc)
  $wa.Update()
  ```

   For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps). 
    
4. From the PowerShell command prompt, type the following to perform user migration:
    
  ```
  $wa.MigrateUsers($true)
  ```

5. After user migration completes, type the following from the PowerShell command prompt to perform provisioning:
    
  ```
  $wa.ProvisionGlobally()
  ```

   For more information, see [New-SPClaimsPrincipal](/powershell/module/sharepoint-server/New-SPClaimsPrincipal?view=sharepoint-ps).
    
After you complete the previous procedures, you might experience one or more of the following issues:Users who submit valid credentials when accessing the migrated web application might be notified that they do not have permissions. If this occurs, the portalsuperuseraccount property and the portalsuperreaderaccount property of the web application were probably configured prior to migration. If this is the case, update the portalsuperuseraccount property and the portalsuperreaderaccount property to use the new claims-based account name. After migration, you can find the new claims-based account name in the web application policy for the migrated web application.If existing alerts are not invoked after migration, you might have to delete and recreate the alerts.If Search crawl does not function on the web application after migration, make sure that the Search crawl account lists the new converted account name. If the new converted account name is not listed, you must manually create a new policy for the crawl account.
  
 **To migrate a claims-based SharePoint 2010 Products web application to SharePoint 2013**
  
1. In SharePoint 2013, create a claims-based web application. For more information, see [Create claims-based web applications in SharePoint Server](/SharePoint/security-for-sharepoint-server/create-claims-based-web-applications).
    
2. Attach the two existing SharePoint 2010 Products content databases to the newly created SharePoint 2013 claims-based web application. For more information, see [Attach or detach content databases in SharePoint Server](../administration/attach-or-detach-content-databases.md).
    
    > [!NOTE]
    > When you attach the SharePoint 2010 Products content databases to the SharePoint 2013 claims-based web application, the databases will be upgraded to the SharePoint 2013 database format but will not be claims-enabled.
  
## Convert SharePoint 2010 Products classic-mode web applications to SharePoint 2013 claims-based web applications
<a name="section1"> </a>

In SharePoint 2013, complete the following procedure to convert an existing SharePoint 2010 Products classic-mode web application to a SharePoint 2013 web application that uses claims-based authentication.
  
 **To convert a SharePoint 2010 Products classic-mode web application to a SharePoint 2013 claims-based authentication**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050) (https://go.microsoft.com/fwlink/p/?LinkId=193050). 
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/SharePoint/security-for-sharepoint-server/create-claims-based-web-applications). 
  
2. In the SharePoint 2013 environment, on the **Start** menu, click **All Programs**.
    
3. Click **SharePoint 2013**.
    
4. Click **SharePoint 2013 Management Shell**.
    
5. Change to the directory where you saved the file.
    
6. At the PowerShell command prompt, type the following command:
    
  ```
  $ap = New-SPAuthenticationProvider -UseWindowsIntegratedAuthentication -DisableKerberos
  New-SPWebApplication -name "ClaimsWebApp" -Port 80 -ApplicationPool "ClaimsAuthAppPool" -ApplicationPoolAccount (Get-SPManagedAccount "<domainname>\<user>") -AuthenticationMethod NTLM -AuthenticationProvider $ap
  ```

  Where:
    
  -  _\<domainname\>_\ _\<user\>_ is the domain to which the server belongs and the name of the user account. 
    
7. Attach the two existing SharePoint 2010 Products content databases to the new SharePoint 2013 claims-mode web application. For more information, see [Attach or detach content databases in SharePoint Server](../administration/attach-or-detach-content-databases.md).
    
    > [!NOTE]
    > When you attach the SharePoint 2010 Products content databases to the SharePoint 2013 claims-mode web application, the databases are upgraded to the SharePoint 2013 database format. You have to verify that the content databases work correctly after you have attached them. 
  
8. From the PowerShell command prompt, type the following:
    
  ```
  Convert-SPWebApplication -Identity <yourWebAppUrl> -From Legacy -To Claims -RetainPermissions [-Force]
  ```

  Where:
    
  -  _\<yourWebAppUrl\>_ is the URL of the web application. 
    
   > [!NOTE]
   > **Convert-SPWebApplication** converts the content databases to claims-based authentication. You have to verify that the users can access the web application after you have converted the content databases. 
  
9. If necessary, attach a third SharePoint 2010 Products content database to the new SharePoint 2013 claims-mode web application, and verify that the content database working correctly after you have attached it.
    
10. From the PowerShell command prompt, type the following:
    
  ```
  Convert-SPWebApplication -Identity <yourWebAppUrl> -From Legacy -To Claims -RetainPermissions [-Force]
  ```

Verify that users can access the web application after you have converted the content databases to claims-based authentication. For more information, see New-SPWebApplication, Get-SPManagedAccount, and Convert-SPWebApplication.
  
## Convert SharePoint 2013 classic-mode web applications to claims-based web applications
<a name="section1"> </a>

In SharePoint 2013, complete the following procedures to first create a classic-mode Web application, and then convert it to claims-based authentication.
  
 **To create a classic-mode Web application in SharePoint 2013**
  
- Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050) (https://go.microsoft.com/fwlink/p/?LinkId=193050). 
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
- From the PowerShell command prompt, type the following:
    
  ```
  New-SPWebApplication -Name <Name> -ApplicationPool <ApplicationPool> -AuthenticationMethod <WindowsAuthType> -ApplicationPoolAccount <ApplicationPoolAccount> -Port <Port> -URL <URL>
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
  
 **To convert a SharePoint 2013 classic-mode web application to claims-based authentication**
  
- From the PowerShell command prompt, type the following:
    
  ```
  Convert-SPWebApplication -Identity "http:// <servername>:port" -From Legacy -To Claims -RetainPermissions [-Force]
  ```

    Where:
    
  -  _\<servername\>_ is the name of the server. 
    
Verify that users can access the web application after you have converted it to claims-based authentication.For more information, see New-SPWebApplication, Get-SPManagedAccount, and Convert-SPWebApplication.
  
## Migrate SharePoint 2010 Products classic-mode web applications to SharePoint 2013 classic-mode web applications
<a name="section1"> </a>

In SharePoint 2013, complete the following procedure to create a classic-mode web application, and then migrate an existing SharePoint 2010 Products classic-mode Web application to SharePoint 2013.
  
 **To migrate a SharePoint 2010 Products classic-mode web application to SharePoint 2013**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050) (https://go.microsoft.com/fwlink/p/?LinkId=193050). 
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. From the PowerShell command prompt, type the following:
    
  ```
  New-SPWebApplication -name "ClassicAuthApp" -Port 100 -ApplicationPool "ClassicAuthAppPool" -ApplicationPoolAccount (Get-SPManagedAccount "<domainname>\<user>")
  ```

  Where:
    
  -  _\<domainname\>_\ _\<user\>_ is the domain to which the server belongs and the name of the user account. 
    
3. Attach the two existing SharePoint 2010 Products content databases to the new SharePoint 2013 classic-mode web application. Verify that the content databases work correctly after you have attached them. For more information, see [Attach or detach content databases in SharePoint Server](../administration/attach-or-detach-content-databases.md).
    
For more information, see [New-SPWebApplication](/powershell/module/sharepoint-server/New-SPWebApplication?view=sharepoint-ps) and [Get-SPManagedAccount](/powershell/module/sharepoint-server/Get-SPManagedAccount?view=sharepoint-ps).
  
## See also
<a name="section1"> </a>

#### Other Resources

[Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14))
  
[Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14))

