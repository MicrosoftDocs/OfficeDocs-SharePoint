---
title: "Assign or remove administrators of service applications in SharePoint Server"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 3/3/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4fceb168-753a-4227-8a23-ab415f9abce7
description: "Summary: Learn how to assign or remove service administrators to a service application in SharePoint Server 2016 and SharePoint 2013."
---

# Assign or remove administrators of service applications in SharePoint Server

 **Summary:** Learn how to assign or remove service administrators to a service application in SharePoint Server 2016 and SharePoint 2013. 
  
An administrator of a SharePoint Server service application can assign additional administrators to that service application. These users are granted security-trimmed access to the SharePoint Central Administration Web site and can manage settings related to the service application. An administrator of a SharePoint Server service application can also remove administrators from a service application.
  
> [!NOTE]
> By default, members of the Farm Administrators group have permissions to manage all service applications. 
  
You can assign or remove service application administrators by using the SharePoint Central Administration websiteor by using Microsoft PowerShell.
  
## To assign or remove administrators to a service application by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, select the row that contains the service application to which you want to add or remove administrators. The ribbon becomes available.
    
4. On the ribbon, click **Administrators**.
    
5. To add an administrator:
    
    1) In the first text box on the page, type the user accounts or groups that you want to add. You can click the **People** icon to validate a name. You can click the **Address book** icon to search for users to add. You can add multiple administrators into the text box. 
  
2) After you have added the administrators, click **OK**.
    
6. To remove an administrator:
    
    1) In the second text box on the page, select the administrator whom you want to remove. Note that this step does not remove the user from the system—it merely revokes the user's administrative permissions to the selected service application.
  
2) Click **Remove**.
  
3) After you have finished removing administrators, click **OK**.
    
## To assign or remove administrators to a service application by using PowerShell

1. Verify that you meet the following minimum requirements:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance 
    
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated. 
    
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
    > [!NOTE]
    > If these permissions are not satisfied, contact your Setup administrator or SQL Server administrator to request these permissions. 
  
    For additional information about PowerShell permissions, see [Permissions](http://technet.microsoft.com/library/ae4901b4-505a-42a9-b8d4-fca778abc12e.aspx#section3) and [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx)
    
2. Start the SharePoint Management Shell.
    
3. To create a claims principal, at the PowerShell command prompt, type the following command:
    
  ```
  $principal = New-SPClaimsPrincipal "<contoso\jane>" -IdentityType WindowsSamAccountName
  
  ```

    Where  _\<contoso\jane\>_ is the user name for which you want to assign administrative permissions. The user name should be entered in the form of **jane@contoso.com** or **contoso\jane**. The new claims principal is stored in the  _$principal_ variable. 
    
4. To retrieve the service application, type the following command:
    
  ```
  $spapp = Get-SPServiceApplication -Name "<ServiceApplicationDisplayName>"
  ```

    Where  _\<ServiceApplicationDisplayName\>_ is the display name of the service application. The service application identification is stored in the  _$spapp_ variable. 
    
    > [!IMPORTANT]
    > The display name must be enclosed in quotation marks, and it must exactly match the service application display name. This includes capitalization. If you have more than one service application that has the identical display name (we do not recommend this), you can use the **Get-SPServiceApplication** cmdlet to view all service applications. You can then identify the service application by its GUID. For more information, see [Get-SPServiceApplication](http://technet.microsoft.com/library/71a467dc-3b95-4b65-af93-0d0d6ebb8326.aspx). 
  
5. To retrieve the administrator security object for the service application, type the following command:
    
  ```
  $security = Get-SPServiceApplicationSecurity $spapp -Admin
  ```

    The retrieved administrator security object is stored in the  _$security_ variable. 
    
    > [!CAUTION]
    > It is important that you append the **-Admin** argument when you use this command. 
  
6. To assign or revoke administrative permissions for the user who is identified by the new claims principal  _$principal_ (created in step 6 of this procedure) to the service application administrator security object  _$security_ (obtained in step 8 of this procedure), use the appropriate command as shown in the following example: 
    
  - To assign administrative permissions, type the following command: 
    
  ```
  Grant-SPObjectSecurity $security $principal "Full Control"
  
  ```

  - To revoke administrative permissions, type the following command:
    
  ```
  Revoke-SPObjectSecurity $security $principal
  ```

7. To assign the updated  _$security_ security object to the service application, type the following command: 
    
  ```
  Set-SPServiceApplicationSecurity $spapp $security -Admin
  ```

    > [!CAUTION]
    > It is important that you append the **-Admin** argument when you use this command. 
  
8. To confirm that the service application's security object is updated appropriately, type the following command: 
    
  ```
  (Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
  
  ```

### Examples

In the following example, the service account user "contoso\jane" is added to the administrators security object for the service application named "Contoso Visio Graphics".
  
```
$principal = New-SPClaimsPrincipal "contoso\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Grant-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

In the following example, the service account user "contoso\jane" is removed from the administrators security object for the service application named "Contoso Visio Graphics".
  
```
$principal = New-SPClaimsPrincipal "contoso\jane" -IdentityType WindowsSamAccountName
$spapp = Get-SPServiceApplication -Name "Contoso Visio Graphics"
$security = Get-SPServiceApplicationSecurity $spapp -Admin
Revoke-SPObjectSecurity $security $principal "Full Control"
Set-SPServiceApplicationSecurity $spapp $security -Admin
(Get-SPServiceApplicationSecurity $spapp -Admin).AccessRules
```

For more information, see the following Microsoft PowerShell articles:
  
- [New-SPClaimsPrincipal](http://technet.microsoft.com/library/0831e64b-3ec0-4016-8128-639991530172.aspx)
    
- [Get-SPServiceApplication](http://technet.microsoft.com/library/71a467dc-3b95-4b65-af93-0d0d6ebb8326.aspx)
    
- [Get-SPServiceApplicationSecurity](http://technet.microsoft.com/library/4f433fea-ddbf-4843-a11c-d936ce51c6bb.aspx)
    
- [Grant-SPObjectSecurity](http://technet.microsoft.com/library/496caa92-2ff4-4048-ab7d-57d8c835bf2b.aspx)
    
- [Revoke-SPObjectSecurity](http://technet.microsoft.com/library/4e7583ab-5b8d-47c2-a9eb-2cf525ae07d8.aspx)
    
- [Set-SPServiceApplicationSecurity](http://technet.microsoft.com/library/8d769193-f126-43f7-8c1e-4bec75c8446d.aspx)
    
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  

