---
title: Assign or remove administrators of service applications in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 4fceb168-753a-4227-8a23-ab415f9abce7
---


# Assign or remove administrators of service applications in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to assign or remove service administrators to a service application in SharePoint Server 2016 and SharePoint Server 2013.An administrator of a SharePoint Server service application can assign additional administrators to that service application. These users are granted security-trimmed access to the SharePoint Central Administration Web site and can manage settings related to the service application. An administrator of a SharePoint Server service application can also remove administrators from a service application.
> [!NOTE:]

  
    
    

You can assign or remove service application administrators by using the SharePoint Central Administration websiteor by using Microsoft PowerShell. **To assign or remove administrators to a service application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the Central Administration Home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, select the row that contains the service application to which you want to add or remove administrators. The ribbon becomes available.
    
  
4. On the ribbon, click **Administrators**.
    
  
5. To add an administrator:
    
1. In the first text box on the page, type the user accounts or groups that you want to add. You can click the **People** icon to validate a name. You can click the **Address book** icon to search for users to add. You can add multiple administrators into the text box.
    
  
2. After you have added the administrators, click **OK**.
    
  

    
    
  
6. To remove an administrator:
    
1. In the second text box on the page, select the administrator whom you want to remove. Note that this step does not remove the user from the system—it merely revokes the user’s administrative permissions to the selected service application. 
    
  
2. Click **Remove**.
    
  
3. After you have finished removing administrators, click **OK**.
    
  
 **To assign or remove administrators to a service application by using PowerShell**
1. Verify that you meet the following minimum requirements:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance
    
  
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated.
    
  
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
  

    > [!NOTE:]
      

    For additional information about PowerShell permissions, see  [Permissions](ae4901b4-505a-42a9-b8d4-fca778abc12e.md#section3) and **Add-SPShellAdmin**
    
  
2. Start the SharePoint Management Shell.
    
  
3. To create a claims principal, at the PowerShell command prompt, type the following command:
    
  ```
  
$principal = New-SPClaimsPrincipal "<contoso\\jane> " -IdentityType WindowsSamAccountName

  ```


    Where  *<contoso\\jane>*  is the user name for which you want to assign administrative permissions. The user name should be entered in the form of **jane@contoso.com** or **contoso\\jane**. The new claims principal is stored in the *$principal*  variable.
    
  
4. To retrieve the service application, type the following command:
    
  ```
  
$spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName> "
  ```


    Where  *<ServiceApplicationDisplayName>*  is the display name of the service application. The service application identification is stored in the *$spapp*  variable.
    
    > [!IMPORTANT:]
      
5. To retrieve the administrator security object for the service application, type the following command:
    
  ```
  
$security = Get-SPServiceApplicationSecurity $spapp -Admin
  ```


    The retrieved administrator security object is stored in the  *$security*  variable.
    
    > [!WARNING:]
      
6. To assign or revoke administrative permissions for the user who is identified by the new claims principal  *$principal*  (created in step 6 of this procedure) to the service application administrator security object *$security*  (obtained in step 8 of this procedure), use the appropriate command as shown in the following example:
    
1. To assign administrative permissions, type the following command: 
    
  ```
  
Grant-SPObjectSecurity $security $principal "Full Control"

  ```

2. To revoke administrative permissions, type the following command:
    
  ```
  
Revoke-SPObjectSecurity $security $principal
  ```

7. To assign the updated  *$security*  security object to the service application, type the following command:
    
  ```
  Set-SPServiceApplicationSecurity $spapp $security -Admin
  ```


    > [!WARNING:]
      
8. To confirm that the service application’s security object is updated appropriately, type the following command: 
    
  ```
  
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules

  ```


## Examples

In the following example, the service account user "contoso\\jane" is added to the administrators security object for the service application named "Contoso Visio Graphics".
```

$principal = New-SPClaimsPrincipal "contoso\\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Grant-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

In the following example, the service account user "contoso\\jane" is removed from the administrators security object for the service application named "Contoso Visio Graphics".


```

$principal = New-SPClaimsPrincipal "contoso\\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Revoke-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

For more information, see the following Microsoft PowerShell articles:
- **New-SPClaimsPrincipal**
    
  
- **Get-SPServiceApplication**
    
  
- **Get-SPServiceApplicationSecurity**
    
  
- **Grant-SPObjectSecurity**
    
  
- **Revoke-SPObjectSecurity**
    
  
- **Set-SPServiceApplicationSecurity**
    
  

> [!NOTE:]

  
    
    


