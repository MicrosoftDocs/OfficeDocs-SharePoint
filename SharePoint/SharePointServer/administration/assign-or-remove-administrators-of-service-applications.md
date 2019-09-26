---
title: "Assign or remove administrators of service applications in SharePoint Server"
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
ms.assetid: 4fceb168-753a-4227-8a23-ab415f9abce7
description: "Learn how to assign or remove service administrators to a service application in SharePoint Server."
---

# Assign or remove administrators of service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
An administrator of a SharePoint Server service application must be a member of the Farm Administrators group to assign or remove additional administrators to that service application. Service application administrators are granted security-trimmed access to the SharePoint Central Administration Web site and can manage settings related to the service application but must be a member of the Farm Administrators group to add and remove other service application administrators.
  
> [!NOTE]
> By default, members of the Farm Administrators group have permissions to manage all service applications. 
  
You can assign or remove service application administrators by using the SharePoint Central Administration websiteor by using Microsoft PowerShell.
  
## To assign or remove administrators to a service application by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, select the row that contains the service application to which you want to add or remove administrators. The ribbon becomes available.
    
4. On the ribbon, click **Administrators**.
    
5. To add an administrator:
    
   - In the first text box on the page, type the user accounts or groups that you want to add. You can click the **People** icon to validate a name. You can click the **Address book** icon to search for users to add. You can add multiple administrators into the text box.
   - After you have added the administrators, click **OK**.
    
6. To remove an administrator:
    
   - In the second text box on the page, select the administrator whom you want to remove. Note that this step does not remove the user from the system—it merely revokes the user's administrative permissions to the selected service application.
   - Click **Remove**.
   - After you have finished removing administrators, click **OK**.
    
## To assign or remove administrators to a service application by using PowerShell

1. Verify that you meet the following minimum requirements:
    
   - You must have membership in the **securityadmin** fixed server role on the SQL Server instance 
    
   - You must have membership in the **db_owner** fixed database role on all databases that are to be updated. 
    
   - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
   > [!NOTE]
   > If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions. 
  
   For additional information about PowerShell permissions, see [Permissions](/powershell/module/sharepoint-server/?view=sharepoint-ps#section3) and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps)
    
2. Start the SharePoint Management Shell.
    
3. To create a claims principal, at the PowerShell command prompt, type the following command:
    
   ```powershell
   $principal = New-SPClaimsPrincipal "<contoso\jane>" -IdentityType WindowsSamAccountName
  
   ```


   Where  _contoso\jane_ is the user name for which you want to assign administrative permissions. The user name should be entered in the form of jane@contoso.com or **contoso\jane**. The new claims principal is stored in the  _$principal_ variable. 
    
4. To retrieve the service application, type the following command:
    
   ```powershell
   $spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName>"
   ```


   Where  _ServiceApplicationDisplayName_ is the display name of the service application. The service application identification is stored in the  _$spapp_ variable. 
    
   > [!IMPORTANT]
   > The display name must be enclosed in quotation marks, and it must exactly match the service application display name. This includes capitalization. If you have more than one service application that has the identical display name (we do not recommend this), you can use the **Get-SPServiceApplication** cmdlet to view all service applications. You can then identify the service application by its GUID. For more information, see [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps). 
  
5. To retrieve the administrator security object for the service application, type the following command:
    
   ```powershell
   $security = Get-SPServiceApplicationSecurity $spapp -Admin
   ```

   The retrieved administrator security object is stored in the  _$security_ variable. 

   > [!CAUTION]
   > It is important that you append the **-Admin** argument when you use this command. 
  
6. To assign or revoke administrative permissions for the user who is identified by the new claims principal  _$principal_ (created in step 6 of this procedure) to the service application administrator security object  _$security_ (obtained in step 8 of this procedure), use the appropriate command as shown in the following example: 
    
   - To assign administrative permissions, type the following command: 
    
   ```powershell
   Grant-SPObjectSecurity $security $principal "Full Control"
  
   ```

   - To revoke administrative permissions, type the following command:
    
   ```powershell
   Revoke-SPObjectSecurity $security $principal
   ```

7. To assign the updated  _$security_ security object to the service application, type the following command: 
    
   ```powershell
   Set-SPServiceApplicationSecurity $spapp $security -Admin
   ```

   > [!CAUTION]
   > It is important that you append the **-Admin** argument when you use this command. 

8. To confirm that the service application's security object is updated appropriately, type the following command: 
    
   ```powershell
   (Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
  
   ```

### Examples

In the following example, the service account user "contoso\jane" is added to the administrators security object for the service application named "Contoso Visio Graphics".
  
```powershell
$principal = New-SPClaimsPrincipal "contoso\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Grant-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

In the following example, the service account user "contoso\jane" is removed from the administrators security object for the service application named "Contoso Visio Graphics".
  
```powershell
$principal = New-SPClaimsPrincipal "contoso\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Revoke-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

For more information, see the following Microsoft PowerShell articles:
  
- [New-SPClaimsPrincipal](/powershell/module/sharepoint-server/New-SPClaimsPrincipal?view=sharepoint-ps)
    
- [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps)
    
- [Get-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Get-SPServiceApplicationSecurity?view=sharepoint-ps)
    
- [Grant-SPObjectSecurity](/powershell/module/sharepoint-server/Grant-SPObjectSecurity?view=sharepoint-ps)
    
- [Revoke-SPObjectSecurity](/powershell/module/sharepoint-online/revoke-spobjectsecurity)
    
- [Set-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Set-SPServiceApplicationSecurity?view=sharepoint-ps)
    
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  

