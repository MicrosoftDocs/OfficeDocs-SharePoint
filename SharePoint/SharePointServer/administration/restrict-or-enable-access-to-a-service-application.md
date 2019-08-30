---
title: "Restrict or enable access to a service application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: b81f80f1-182f-42eb-9546-8a621a4f069f
description: "Learn how to restrict access to a service application by adding and removing services accounts and reestablish local farm-wide access to a service application in SharePoint Server."
---

# Restrict or enable access to a service application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In SharePoint Server, you can restrict the access to a service application so that the service application is available to only specified web applications. 
  
By default, all service applications on the local farm are available to all web applications on the local farm. You might want to restrict access to a service application if you host multiple customers on the same farm, and you want to isolate one customer's service applications from another customer's web application.
  
If you restrict access to a service application and you later decide that you want to make it available to the whole farm, you can remove the restriction. 
  
    
## Restrict access to a service application
<a name="Section2"> </a>

To restrict access to a service application, remove service accounts from the service application. Conversely, to enable access to a service application, add service accounts to the service application. You can perform these tasks by using Central Administration or by using PowerShell.
  
To restrict access to a service application, you must complete the following tasks:
  
1. Add a specific service account to the service application.
    
2. Remove the local farm ID from the service application.
    
The procedures in this article describe how to restrict or restore access to a service application. However, you can follow the steps in the procedures to add any service account to any service application or to remove any service account from any service application.
  
For example, the [To restore local farm-wide access to a service application by using Central Administration](#ProcCARestore) procedure explicitly describes how to add the local farm ID to a service application. You can use the same procedure to add any other service account to a service application. To do this, you provide the appropriate service account instead of the local farm ID. 
  
Because the local farm ID provides local farm-wide access to the service application by default, it is redundant to also grant explicit local web application permissions to a service application unless you also remove the local farm ID. 
  
To grant permissions to a service application, you must retrieve and supply the appropriate service account. For a web application, this account is also known as an application pool identity account. 
  
After you grant permissions to a service account and remove the local farm ID from a service application, only web applications that are managed by the assigned service account can access the service application. You can assign multiple web applications (that have different managing service accounts) to the same service application by repeating these procedures and adding the various web application service accounts to the service application.
  
> [!CAUTION]
> If you remove the local farm ID from a service application and do not assign any other service account to that service application, the service application becomes unavailable to all web applications. 
  

    
### Restrict access to a service application by using Central Administration
<a name="Section2CA"> </a>

To restrict access to a service application by using the SharePoint Central Administration website, follow these steps: 
  
1. Retrieve the web application service account.
    
2. Add the web application service account to the service application.
    
3. Remove the local farm ID from the service application.
    

    
### To retrieve a web application service account by using Central Administration
<a name="Section2CA"> </a>

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. On the Central Administration Home page, in the **Security** section, click **Configure service accounts**.
    
3. On the **Service Accounts** page, select the services and web application component from the first drop-down list. 
    
    The service account is shown in the **Select an account for this component** list. Record the service account name because you'll use it in the next procedure. 
    
4. Click **Cancel** to exit the **Service Accounts** page without making any changes. 
    
### To grant and remove permissions for service accounts to access a service application by using Central Administration
<a name="Section2CA"> </a>

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. On the Central Administration Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the **Manage Service Applications** page, click the row that contains the service application for which you want to assign permissions. 
    
    The ribbon becomes available.
    
4. In the **Sharing** group of the ribbon, click **Permissions**.
    
5. In the **Connection Permissions** dialog box, type the service account name that you retrieved in the previous procedure, and then click **Add**. 
    
6. Ensure that the newly-added service account name is selected in the middle pane, and then click the appropriate check box in the bottom pane to supply the required permission level.
    
7. In the middle pane, click **Local Farm**, and then click **Remove**. 
    
8. Verify that the **Connection Permissions** page now lists only the service account that you want to access the service application, and that the service account has the required permissions on the service application. Click **OK** to change the permissions, or click **Cancel** to end the task without making changes. 
    
You can grant and remove permissions for any service account by using this procedure. To restore the local farm ID to the service application by using CentralAdmin_2nd requires an additional step that does not apply to other service accounts. For information about how to do this, see [Restore farm-wide access to a service application](#Section3) later in this article. 
  
### Restrict access to a service application by using Microsoft PowerShell
<a name="Section2WPS"> </a>

All procedures in this section assume that you have the appropriate permissions.
  
The process that restricts access to a service application by using PowerShell is more complex than performing the same task by using Central Administration. In PowerShell, you'll use some procedures to collect and store information for input into later procedures. 
  
After you have started PowerShell, the remaining steps to restrict access to a service application are as follows:
  
1. Retrieve the local farm ID.
    
2. Retrieve the web application service account.
    
3. Create a new claims principal that contains the web application service account.
    
4. Retrieve the security object of the service application.
    
5. Add the web application service account to the security object of the service application.
    
6. Remove the local farm ID from the security object of the service application.
    
7. Assign the updated security object to the service application.
    
8. Display and review updated permissions
    

    
### <a name="Section2SWPS"> </a>To start a Microsoft PowerShell session

1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
### To retrieve a web application service account and create a new claims principal by using Microsoft PowerShell
<a name="Section2WPS"> </a>

1. At the PowerShell command prompt, type the following command to retrieve the service account (that is, the application pool identity account) of a web application: 
    
   ```powershell
   $webapp = Get-SPWebApplication <http://WebApplication>
   $webApp.ApplicationPool.UserName
   ```

   Where _\<http://WebApplication\>_ is the web application URL. 
    
   The web application service account name displays at the command prompt.
    
2. To create a new claims principal, type the following command:
    
   ```powershell
   $principal = New-SPClaimsPrincipal <ServiceAccount> -IdentityType WindowsSamAccountName
   ```

   Where _\<ServiceAccount\>_ is the user name (in the form of jane@contoso.com or contoso\jane) that was retrieved by running the previous command. The  _$principal_ variable will contain the new claims principal. 
    
### To retrieve the security object of the service application
<a name="Section2WPS"> </a>

1. To retrieve the security object of the service application, type the following commands. The  _$security_ variable will store the service application security object. 
    
   ```powershell
   $spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName>"
   $spguid = $spapp.id
   $security = Get-SPServiceApplicationSecurity $spguid
   ```

   Where _\<ServiceApplicationDisplayName\>_ is the display name of the service application.
    
    > [!IMPORTANT]
    > You must enclose the display name in quotation marks, and it must exactly match the service application display name. This includes capitalization. If you have more than one service application that has the same display name (we do not recommend this), you can run the **Get-SPServiceApplication** cmdlet without arguments to view all service applications. You can then identify the service application directly by its GUID.

   ```powershell
   Get-SpServiceApplication
   ```

   All service applications are listed. 

   ```powershell
   $spapp = Get-SpserviceApplication -Identity <GUID>
   $spguid = $spapp.id
   ```

   Where _\<GUID\>_ is the GUID for the service application for which you want to update permissions. 
    
### To update the service application security object by using the preferred permissions
<a name="Section2WPS"> </a>

1. The first step to update the service application security object is to add the new claims principal  _$principal_ to the service application security object  _$security_. To do this, type the following command: 
    
   ```powershell
   Grant-SPObjectSecurity $security $principal -Rights "<Rights>"
   ```

   Where _\<Rights\>_ is the permissions that you want to grant. Typically, this will be Full Control. The available permissions can vary between service applications. 
    
   If you do not want to grant Full Control permissions, and you do not know what permissions can be granted to the service application, you can run the following commands to return the available permissions strings:

   ```powershell
   $rightslist = Get-SPServiceApplicationSecurity $spapp
   $rightslist.NamedAccessRights
   ```

2. To remove the local farm ID (that is stored in the  _$farmID_ variable) from the service application security object  _$security_, type the following command:
    
   ```powershell
   Revoke-SPObjectSecurity $security $farmID
   ```

3. To assign the updated  _$security_ security object to the service application and confirm that the security object for the service application is appropriately updated, type the following commands: 
    
   ```powershell
   Set-SPServiceApplicationSecurity $spapp -ObjectSecurity $security (Get-SPServiceApplicationSecurity $spapp).AccessRules
   ```

   You can add or remove any service account to a service application by using these procedures.
  
## Restore farm-wide access to a service application
<a name="Section3"> </a>

You can restore farm-wide access to a service application by adding the local farm ID to the service application. You can do this by using Central Administration or by using PowerShell commands. However, you must use PowerShell to obtain the local farm ID.

    
### <a name="ProcWPSGetFID"></a>To retrieve the local farm ID by using PowerShell

1. This procedure starts after step 4 of the [To start a Microsoft PowerShell session ](#Section2SWPS) procedure. 
    
2. The following command retrieves the local farm ID, stores it in the  _$farmID_ variable, and displays the ID at the command prompt: 
    
   ```powershell
   $farmID = Get-SPFarm | select id
   ```

   If you want to restore farm-wide access by using Central Administration, copy this value into the clipboard for use in the following procedure. 
    
   If you want to restore farm-wide access to the service application by using PowerShell, type the following additional commands at the PowerShell command prompt. You'll use the retrieved information in the following procedure.
    
   ```powershell
   $claimProvider = (Get-SPClaimProvider System).ClaimProvider 
   $principal = New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimProvider -ClaimValue $farmid
   ```

### <a name="ProcCARestore"></a>To restore local farm-wide access to a service application by using Central Administration

1. Perform steps 1 through 3 of the procedure [To grant and remove permissions for service accounts to access a service application by using Central Administration](#Section2CA).
    
2. In the **Connection Permissions** dialog box, copy the local farm ID that you retrieved in the previous procedure, and then click **Add**. 
    
3. Ensure that the local farm ID is selected in the middle pane. Click the **Full Control** check box in the bottom pane. 
    
4. Click **OK** to restore farm-wide access to the service application, or click **Cancel** to end the task without making changes. 
    
### To restore local farm-wide access to a service application by using Microsoft PowerShell

1. This procedure starts after step 2 of the procedure [To retrieve the local farm ID by using Windows Powershell ](#ProcWPSGetFID).
    
2. To restore the retrieved local farm ID to the service application security object $security, type the following commands:
    
   ```powershell
   $spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName>"
   $spguid = $spapp.id
   $security = Get-SPServiceApplicationSecurity $spguid
   Grant-SPObjectSecurity -Identity $security -Principal $Principal -Rights "Full Control"
   Set-SPServiceApplicationSecurity $spguid -ObjectSecurity $security
   ```

   Where _\<ServiceApplicationDisplayName\>_ is the display name of the service application.
    
    > [!IMPORTANT]
    > You must enclose the display name in quotation marks, and it must exactly match the service application display name. This includes capitalization. If you have more than one service application that has the same display name (we do not recommend this), you can run the **Get-SPServiceApplication** cmdlet without arguments to view all service applications. You can then identify the service application directly by its GUID. 
  
## Microsoft PowerShell code examples
<a name="SectionEX"> </a>

In the following example, the administrator wants to restrict access to the "Contoso BDC" service application to the http://contoso/hawaii web application, which is managed by the service account "contoso\jane." By adding "contoso\jane" and removing the local farm service account from the service application, "Contoso BDC" is restricted to only those web applications that are managed by the service account "contoso\jane" - in this case, http://contoso/hawaii.
  
```powershell
$farmid = Get-SPFarm | select id
$claimProvider = (Get-SPClaimProvider System).ClaimProvider 
$farmappId = New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimProvider -ClaimValue $farmid 
webapp = get-spwebapplication http://contoso
$webapp.applicationpool
$principal = New-SPClaimsPrincipal contoso/jane -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso BDC"
$spguid = $spapp.id
$security = Get-SPServiceApplicationSecurity $spguid
Grant-SPObjectSecurity $security $principal -Rights "Full Control"
Revoke-SPObjectSecurity $security $farmappId
Set-SPServiceApplicationSecurity $spguid -ObjectSecurity $security
(Get-SPServiceApplicationSecurity $spguid).AccessRules
```

In the following example, access to the service application "Contoso BDC" is restored to all web applications in the local farm. 
  
```powershell
$farmid = Get-SPFarm | select id
$claimProvider = (Get-SPClaimProvider System).ClaimProvider 
$farmappId = New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimProvider -ClaimValue $farmid 
$spapp = Get-SPServiceApplication -Name "Contoso BDC"
$spguid = $spapp.id
$security = Get-SPServiceApplicationSecurity $spguid
Grant-SPObjectSecurity -Identity $security -Principal $farmappId -Rights "Full Control"
Set-SPServiceApplicationSecurity $spguid -ObjectSecurity $security
(Get-SPServiceApplicationSecurity $spguid).AccessRules
```

## See also
<a name="SectionEX"> </a>

#### Concepts

[Add or remove service application connections from a web application in SharePoint Server](add-or-remove-a-service-application-connection-to-a-web-application.md)
  
[Account permissions and security settings in SharePoint Servers 2016 and 2019](../install/account-permissions-and-security-settings-in-sharepoint-server-2016.md)
#### Other Resources

[Create a web application in SharePoint Server](/SharePoint/administration/create-a-web-application)
  
[Get-SPWebApplication](/SharePoint/administration/create-a-web-application)
  
[New-SPClaimsPrincipal](/powershell/module/sharepoint-server/New-SPClaimsPrincipal?view=sharepoint-ps)
  
[Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps)
  
[Get-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/get-spserviceapplicationsecurity?view=sharepoint-ps)
  
[Grant-SPObjectSecurity](/powershell/module/sharepoint-server/Grant-SPObjectSecurity?view=sharepoint-ps)
  
[Revoke-SPObjectSecurity](/powershell/module/sharepoint-online/revoke-spobjectsecurity)
  
[Set-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Set-SPServiceApplicationSecurity?view=sharepoint-ps)
  
[Get-SPFarm](/powershell/module/sharepoint-server/Get-SPFarm?view=sharepoint-ps)
  
[Get-SPClaimProvider](/powershell/module/sharepoint-server/Get-SPClaimProvider?view=sharepoint-ps)

