---
title: Restrict or enable access to a service application in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: b81f80f1-182f-42eb-9546-8a621a4f069f
---


# Restrict or enable access to a service application in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to restrict access to a service application by adding and removing services accounts and reestablish local farm-wide access to a service application in SharePoint Server 2016 and SharePoint 2013.In SharePoint Server, you can restrict the access to a service application so that the service application is available to only specified web applications. By default, all service applications on the local farm are available to all web applications on the local farm. You might want to restrict access to a service application if you host multiple customers on the same farm, and you want to isolate one customer's service applications from another customer’s web application.If you restrict access to a service application and you later decide that you want to make it available to the whole farm, you can remove the restriction. In this article:
-  [Restrict access to a service application](#Section2)
    
  
-  [Restore farm-wide access to a service application](#Section3)
    
  
-  [Windows PowerShell code examples](#SectionEX)
    
  

## Restrict access to a service application
<a name="Section2"> </a>

To restrict access to a service application, remove service accounts from the service application. Conversely, to enable access to a service application, add service accounts to the service application. You can perform these tasks by using Central Administration or by using PowerShell.To restrict access to a service application, you must complete the following tasks:
1. Add a specific service account to the service application.
    
  
2. Remove the local farm ID from the service application.
    
  

> [!NOTE:]

  
    
    

Because the local farm ID provides local farm-wide access to the service application by default, it is redundant to also grant explicit local web application permissions to a service application unless you also remove the local farm ID. To grant permissions to a service application, you must retrieve and supply the appropriate service account. For a web application, this account is also known as an  *application pool identity account*  .After you grant permissions to a service account and remove the local farm ID from a service application, only web applications that are managed by the assigned service account can access the service application. You can assign multiple web applications (that have different managing service accounts) to the same service application by repeating these procedures and adding the various web application service accounts to the service application.
> [!WARNING:]

  
    
    

In this section:
-  [Restrict access to a service application by using Central Administration](#Section2CA)
    
  
-  [Restrict access to a service application by using Windows PowerShell](#Section2WPS)
    
  

## Restrict access to a service application by using Central Administration
<a name="Section2CA"> </a>

To restrict access to a service application by using the SharePoint Central Administration website, follow these steps: 
1. Retrieve the web application service account.
    
  
2. Add the web application service account to the service application.
    
  
3. Remove the local farm ID from the service application.
    
  
Procedures in this section:
-  [To retrieve a web application service account by using Central Administration ](#ProcCAGetWeb)
    
  
-  [To grant and remove permissions for service accounts to access a service application by using Central Administration](#ProcCAGrant)
    
  
 **To retrieve a web application service account by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On the Central Administration Home page, in the **Security** section, click **Configure service accounts**.
    
  
3. On the **Service Accounts** page, select the services and web application component from the first drop-down list.
    
    The service account is shown in the **Select an account for this component** list. Record the service account name because you'll use it in the next procedure.
    
  
4. Click **Cancel** to exit the **Service Accounts** page without making any changes.
    
  
 **To grant and remove permissions for service accounts to access a service application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On the Central Administration Home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the **Manage Service Applications** page, click the row that contains the service application for which you want to assign permissions.
    
    The ribbon becomes available.
    
  
4. In the **Sharing** group of the ribbon, click **Permissions**.
    
  
5. In the **Connection Permissions** dialog box, type the service account name that you retrieved in the previous procedure, and then click **Add**.
    
  
6. Ensure that the newly-added service account name is selected in the middle pane, and then click the appropriate check box in the bottom pane to supply the required permission level.
    
  
7. In the middle pane, click **Local Farm**, and then click **Remove**.
    
  
8. Verify that the **Connection Permissions** page now lists only the service account that you want to access the service application, and that the service account has the required permissions on the service application. Click **OK** to change the permissions, or click **Cancel** to end the task without making changes.
    
  
You can grant and remove permissions for any service account by using this procedure. To restore the local farm ID to the service application by using CentralAdmin_2nd requires an additional step that does not apply to other service accounts. For information about how to do this, see  [Restoring farm-level access to a service application](#Section3) later in this article.
#### Restrict access to a service application by using Microsoft PowerShell
<a name="Section2WPS"> </a>

All procedures in this section assume that you have the appropriate permissions and have opened the PowerShell Command Prompt window, as described in the  [To start a Windows PowerShell session](#ProcInitWPS) procedure later in this section.The process that restricts access to a service application by using PowerShell is more complex than performing the same task by using Central Administration. In PowerShell, you'll use some procedures to collect and store information for input into later procedures. After you have started PowerShell, the remaining steps to restrict access to a service application are as follows:
1. Retrieve the local farm ID.
    
  
2. Retrieve the web application service account.
    
  
3. Create a new claims principal that contains the web application service account.
    
  
4. Retrieve the security object of the service application.
    
  
5. Add the web application service account to the security object of the service application.
    
  
6. Remove the local farm ID from the security object of the service application.
    
  
7. Assign the updated security object to the service application.
    
  
8. Display and review updated permissions
    
  
In this section:
-  [To start a Windows PowerShell session ](#ProcInitWPS)
    
  
-  [To retrieve the local farm ID by using Windows PowerShell ](#ProcWPSGetFID)
    
  
-  [To retrieve a web application service account and create a new claims principal by using Windows PowerShell ](#ProcWPSGetWeb)
    
  
-  [To retrieve the security object of the service application](#ProcWPSGetSO)
    
  
-  [To update the service application security object by using the preferred permissions](#ProcWPSUpdateSO)
    
  
 **To start a Microsoft PowerShell session**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
 **To retrieve a web application service account and create a new claims principal by using Microsoft PowerShell**
1. At the PowerShell command prompt, type the following command to retrieve the service account (that is, the application pool identity account) of a web application: 
    
  ```
  
$webapp = Get-SPWebApplication <http://WebApplication>
$webApp.ApplicationPool.UserName

  ```


    Where  *<http://WebApplication>*  is the web application URL.
    
    The web application service account name displays at the command prompt.
    
  
2. To create a new claims principal, type the following command:
    
  ```
  
$principal = New-SPClaimsPrincipal <ServiceAccount>  -IdentityType WindowsSamAccountName
  ```


    Where  *<ServiceAccount>*  is the user name (in the form of jane@contoso.com or contoso\\jane) that was retrieved by running the previous command. The *$principal*  variable will contain the new claims principal.
    
  
 **To retrieve the security object of the service application**
1. To retrieve the security object of the service application, type the following commands. The  *$security*  variable will store the service application security object.
    
  ```
  $spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName> "
$spguid = $spapp.id
$security = Get-SPServiceApplicationSecurity $spguid

  ```


    Where  *<ServiceApplicationDisplayName>*  is the display name of the service application.
    
    > [!IMPORTANT:]
      
 **To update the service application security object by using the preferred permissions**
1. The first step to update the service application security object is to add the new claims principal  *$principal*  to the service application security object *$security*  . To do this, type the following command:
    
  ```
  
Grant-SPObjectSecurity $security $principal -Rights "<Rights> "
  ```


    Where  *<Rights>*  is the permissions that you want to grant. Typically, this will be Full Control. The available permissions can vary between service applications.
    
    > [!TIP:]
      
2. To remove the local farm ID (that is stored in the  *$farmID*  variable) from the service application security object *$security*  , type the following command:
    
  ```
  
Revoke-SPObjectSecurity $security $farmID
  ```

3. To assign the updated  *$security*  security object to the service application and confirm that the security object for the service application is appropriately updated, type the following commands:
    
  ```
  Set-SPServiceApplicationSecurity $spapp -ObjectSecurity $security (Get-SPServiceApplicationSecurity $spapp).AccessRules
  ```

You can add or remove any service account to a service application by using these procedures.
## Restore farm-wide access to a service application
<a name="Section3"> </a>

You can restore farm-wide access to a service application by adding the local farm ID to the service application. You can do this by using Central Administration or by using PowerShell commands. However, you must use PowerShell to obtain the local farm ID.In this section:
-  [To retrieve the local farm ID by using Windows Powershell ](#ProcWPSGetFID)
    
  
-  [To restore local farm-wide access to a service application by using Central Administration](#ProcCARestore)
    
  
-  [To restore local farm-wide access to a service application by using Windows Powershell](#ProcWPSRestore)
    
  
 **To retrieve the local farm ID by using PowerShell**
1. This procedure starts after step 4 of the  [To start a Windows PowerShell session ](#ProcInitWPS) procedure.
    
  
2. The following command retrieves the local farm ID, stores it in the  *$farmID*  variable, and displays the ID at the command prompt:
    
  ```
  $farmID = Get-SPFarm | select id
  ```


    If you want to restore farm-wide access by using Central Administration, copy this value into the clipboard for use in the following procedure. 
    
    If you want to restore farm-wide access to the service application by using PowerShell, type the following additional commands at the PowerShell command prompt. You'll use the retrieved information in the following procedure.
    


  ```
  $claimProvider = (Get-SPClaimProvider System).ClaimProvider
$principal = New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimProvider -ClaimValue $farmid
  ```

 **To restore local farm-wide access to a service application by using Central Administration**
1. Perform steps 1 through 3 of the procedure  [To grant and remove permissions for service accounts to access a service application by using Central Administration](#ProcCAGrant).
    
  
2. In the **Connection Permissions** dialog box, copy the local farm ID that you retrieved in the previous procedure, and then click **Add**.
    
  
3. Ensure that the local farm ID is selected in the middle pane. Click the **Full Control** check box in the bottom pane.
    
  
4. Click **OK** to restore farm-wide access to the service application, or click **Cancel** to end the task without making changes.
    
  
 **To restore local farm-wide access to a service application by using Microsoft PowerShell**
1. This procedure starts after step 2 of the procedure  [To retrieve the local farm ID by using Windows Powershell ](#ProcWPSGetFID).
    
  
2. To restore the retrieved local farm ID to the service application security object $security, type the following commands:
    
  ```
  
$spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName> "
$spguid = $spapp.id
$security = Get-SPServiceApplicationSecurity $spguid
Grant-SPObjectSecurity -Identity $security -Principal $Principal -Rights "Full Control"
Set-SPServiceApplicationSecurity $spguid -ObjectSecurity $security
  ```


    Where  *<ServiceApplicationDisplayName>*  is the display name of the service application.
    
    > [!IMPORTANT:]
      

## Microsoft PowerShell code examples
<a name="SectionEX"> </a>

In the following example, the administrator wants to restrict access to the "Contoso BDC" service application to the http://contoso/hawaii web application, which is managed by the service account "contoso\\jane." By adding "contoso\\jane" and removing the local farm service account from the service application, "Contoso BDC" is restricted to only those web applications that are managed by the service account "contoso\\jane" - in this case, http://contoso/hawaii.
```

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


```

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


# See also

#### 

 [Add or remove service application connections from a web application in SharePoint Server](html/add-or-remove-service-application-connections-from-a-web-application-in-sharepoi.md)
  
    
    
 [Account permissions and security settings in SharePoint Server 2016](html/account-permissions-and-security-settings-in-sharepoint-server-2016.md)
  
    
    

#### 

 **Create a web application in SharePoint Server**
  
    
    
 **Get-SPWebApplication**
  
    
    
 **New-SPClaimsPrincipal**
  
    
    
 **Get-SPServiceApplication**
  
    
    
 **Get-SPServiceApplicationSecurity**
  
    
    
 **Grant-SPObjectSecurity**
  
    
    
 **Revoke-SPObjectSecurity**
  
    
    
 **Set-SPServiceApplicationSecurity**
  
    
    
 **Get-SPFarm**
  
    
    
 **Get-SPClaimProvider**
  
    
    

  
    
    

