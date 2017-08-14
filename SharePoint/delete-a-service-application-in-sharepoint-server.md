---
title: Delete a service application in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: ac2338f5-1b06-4a7c-9dc0-4751b6421cb3
---


# Delete a service application in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to delete a service application in SharePoint Server 2016 and SharePoint Server 2013.You can delete a SharePoint Server service application by using the SharePoint Central Administration website or by using Microsoft PowerShell cmdlets. 
> [!CAUTION:]

  
    
    

Before you delete a service application, verify that its removal will not adversely affect users. We recommend, that you ensure that no web applications are currently consuming the service application that you are going to delete. For information about how to disconnect a service application from a web application, see  [Add or remove service application connections from a web application in SharePoint Server](html/add-or-remove-service-application-connections-from-a-web-application-in-sharepoi.md).When you delete a service application, you have the option of also deleting the service application database. Some service applications do not have databases. If you plan to create the service application again in the future, do not delete the service application database. If the service application is temporary, you will most likely want to delete the database during this operation.To ensure that the service application is available for potential future use, consider backing up the service application before you delete it. For more information, see  [Back up service applications in SharePoint Server](html/back-up-service-applications-in-sharepoint-server.md) and [Restore service applications in SharePoint Server](html/restore-service-applications-in-sharepoint-server.md).In this article:
-  [To delete a service application by using Central Administration](#ProcCA)
    
  
-  [To delete a service application by using Windows PowerShell](#ProcWPS)
    
  
 **To delete a service application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On the SharePoint Central Administration website, click **Application Management**, and then click **Manage service applications**.
    
  
3. On the **Manage Service Applications** page, click the row that contains the service application that you want to delete. The ribbon becomes available.
    
  
4. On the ribbon, click **Delete**.
    
  
5. In the confirmation dialog box, select the check box next to **Delete data associated with the Service Applications** if you want to delete the service application database. If you want to retain the database, leave this check box cleared.
    
  
6. Click **OK** to delete the service application, or click **Cancel** to stop the operation.
    
  

## 

 **To delete a service application by using PowerShell**
1. Verify that you meet the following minimum requirements:
    
  - You must have membership in the **securityadmin** fixed server role on the SQL Server instance
    
  
  - You must have membership in the **db_owner** fixed database role on all databases that are to be updated.
    
  
  - You must be a member of the Administrators group on the server on which you are running the PowerShell cmdlet.
    
  

    > [!NOTE:]
      

    For additional information about PowerShell permissions, see  [Permissions](ae4901b4-505a-42a9-b8d4-fca778abc12e.md#section3) and **Add-SPShellAdmin**
    
  
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following commands. 
    
  
4. To retrieve the service application that you want to delete, type the following command: 
    
  ```
  
$spapp = Get-SPServiceApplication -Name "<Service application display name> "
  ```


    Where  *<Service application display name>*  is the display name of the service application that you want to delete.
    
    The service application information will be stored in the **$spapp** variable.
    
    > [!IMPORTANT:]
      
5. To delete the selected service application, run either of the following commands. In both cases, you are prompted to confirm the deletion. 
    
  - To delete the selected service application without removing the service application database, type the following command:
    
  ```
  
Remove-SPServiceApplication $spapp
  ```

  - To delete the selected service application and also delete the service application database, type the following command:
    
  ```
  Remove-SPServiceApplication $spapp -RemoveData
  ```


## Example


```
$spapp = Get-SPServiceApplication -Name "Contoso BDC Service"
Remove-SPServiceApplication $spapp -RemoveData
```

In this example, the service application "Contoso BDC Service" information is stored in the **$spapp** variable. After the action is confirmed, the service application and its database are permanently deleted.For more information, see **Get-SPServiceApplication** and **Remove-SPServiceApplication**.
# See also

#### 

 **Remove-SPServiceApplicationProxyGroup**
  
    
    

  
    
    

