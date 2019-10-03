---
title: "Delete a service application in SharePoint Server"
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
ms.assetid: ac2338f5-1b06-4a7c-9dc0-4751b6421cb3
description: "Learn how to delete a service application in SharePoint Server."
---

# Delete a service application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can delete a SharePoint Server service application by using the SharePoint Central Administration website or by using Microsoft PowerShell cmdlets. 
  
> [!CAUTION]
> The act of deleting a service application is permanent — you cannot undo this operation. 
  
Before you delete a service application, verify that its removal won't adversely affect users. We recommend, that you ensure that no web applications are currently consuming the service application that you are going to delete. For information about how to disconnect a service application from a web application, see [Add or remove service application connections from a web application in SharePoint Server](add-or-remove-a-service-application-connection-to-a-web-application.md).
  
When you delete a service application, you have the option of also deleting the service application database. Some service applications don't have databases. If you plan to create the service application again in the future, don't delete the service application database. If the service application is temporary, you'll most likely want to delete the database during this operation.
  
To ensure that the service application is available for potential future use, consider backing up the service application before you delete it. For more information, see [Back up service applications in SharePoint Server](back-up-a-service-application.md) and [Restore service applications in SharePoint Server](restore-a-service-application.md).
  
    
### To delete a service application by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. On the SharePoint Central Administration website, click **Application Management**, and then click **Manage service applications**.
    
3. On the **Manage Service Applications** page, click the row that contains the service application that you want to delete. The ribbon becomes available. 
    
4. On the ribbon, click **Delete**.
    
5. In the confirmation dialog box, select the check box next to **Delete data associated with the Service Applications** if you want to delete the service application database. If you want to retain the database, leave this check box cleared. 
    
6. Click **OK** to delete the service application, or click **Cancel** to stop the operation. 
    
## To delete a service application by using PowerShell

1. Verify that you meet the following minimum requirements:
    
   - You must have membership in the **securityadmin** fixed server role on the SQL Server instance 
    
   - You must have membership in the **db_owner** fixed database role on all databases that are to be updated. 
    
   - You must be a member of the Administrators group on the server on which you're running the PowerShell cmdlet.
    
   > [!NOTE]
   > If these permissions aren't satisfied, contact your Setup administrator or SQL Server administrator to request these permissions. 
  
   For additional information about PowerShell permissions, see [Permissions](/powershell/module/sharepoint-server/?view=sharepoint-ps#section3) and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps)
    
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following commands. 
    
4. To retrieve the service application that you want to delete, type the following command: 
    
   ```powershell
   $spapp = Get-SPServiceApplication -Name "<Service application display name>"
   ```

   Where  _\<Service application display name\>_ is the display name of the service application that you want to delete. 
    
   The service application information will be stored in the **$spapp** variable. 
    
   > [!IMPORTANT]
   > You have to type the display name within quotation marks, and you have to type the exact service application display name. This includes capitalization. We recommend that you don't create multiple service applications that have the same display name. If you do have this situation, you can use the **Get-SPServiceApplication** cmdlet to list all service applications. You can then use the service application GUID and the **-Identity** parameter to specify the service application that you want to delete. For more information, see [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps). 
  
5. To delete the selected service application, run either of the following commands. In both cases, you are prompted to confirm the deletion. 
    
   - To delete the selected service application without removing the service application database, type the following command:
    
   ```powershell
   Remove-SPServiceApplication $spapp
   ```

   - To delete the selected service application and also delete the service application database, type the following command:
    
   ```powershell
   Remove-SPServiceApplication $spapp -RemoveData
   ```

### Example

```powershell
$spapp = Get-SPServiceApplication -Name "Contoso BDC Service"
Remove-SPServiceApplication $spapp -RemoveData
```

In this example, the service application "Contoso BDC Service" information is stored in the **$spapp** variable. After the action is confirmed, the service application and its database are permanently deleted. 
  
For more information, see [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps) and [Remove-SPServiceApplication](/powershell/module/sharepoint-server/Remove-SPServiceApplication?view=sharepoint-ps).
  
## See also

#### Other Resources

[Remove-SPServiceApplicationProxyGroup](/powershell/module/sharepoint-server/Remove-SPServiceApplicationProxyGroup?view=sharepoint-ps)

