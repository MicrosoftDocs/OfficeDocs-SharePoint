---
title: "Add or remove service application connections from a web application in SharePoint Server"
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
ms.assetid: 6a7cfa97-f4b1-4b3f-9b98-303ee1e836c2
description: "Learn how to add or remove service application connections to a service application connection group in SharePoint Server."
---

# Add or remove service application connections from a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
When you create a service application in SharePoint Server, a service application connection is created. A service application connection is also referred to as an application proxy. A service application connection associates the service application to web applications via membership in a service application connection group (also referred to as application proxy group). 
  
> [!IMPORTANT]
> If you are creating a service application connection to a service application in a remote farm, you should read [Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md) to gain a full understanding of the requirements to successfully share service applications across farms. 
  
By default, a new service application connection is added to the farm's Default group of service application connections when you create the service application by using Central Administration. You can override this default membership. If a new service application is created by using Microsoft PowerShell instead of by using Central Administration, the new service application does not automatically become a member of the Default service application connections group unless the **default** parameter is supplied. 
  
> [!NOTE]
> For more information about how to create and configure service applications, see [Manage service applications in SharePoint Server](service-application-management.md). 
  
By default, all web applications are associated with the farm's Default group of service application connections, although you can change this setting. You can also create one custom connection group for each web application in the farm. You can change the service applications with which a web application is associated at any time, and you can change the service applications that are included in the Default service application connection group.
  
## Editing a service connection group
<a name="Section2"> </a>

You can add or remove service application connections to a service application connection group by using Central Administration or by using PowerShell cmdlets.
  
### To edit a service connection group by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start Central Administration.
    
3. On the Central Administration Home page, click **Application Management**.
    
4. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**. 
    
5. On the Service Application Associations page, select **Web Applications** from the **View** drop-down menu. 
    
6. In the list of Web applications, in the **Application Proxy Group** column, click the name of the service application connection group that you want to change. 
    
7. To add a service connection to the group, select the check box that is next to the service application that you want to add to the connection group. To remove a service application connection from the connection group, clear the check box next to the service application that you want to remove from the connection group. When you have made the changes that you want, click **OK**.
    
    > [!NOTE]
    > You can also change custom service application connection groups by clicking **Manage Web Applications** from the Central Administration Home page, selecting a listed Web application, and then clicking **Service Connections** on the ribbon. You cannot change the default service applications connection group through this page, however. 
  
### To add a service application connection to a service application connection group by using PowerShell

1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
   > [!NOTE]
   > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Add-SPServiceApplicationProxyGroupMember -Identity < the service application proxy group > -Member <members to add to the service application proxy group>
   ```

   For more information, see [Add-SPServiceApplicationProxyGroupMember](/powershell/module/sharepoint-server/Add-SPServiceApplicationProxyGroupMember?view=sharepoint-ps).
    
### To remove a service application connection from a service application connection group by using PowerShell

1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Add memberships that are required beyond the minimums above.
    
   An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
   > [!NOTE]
   > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Remove-SPServiceApplicationProxyGroupMember -Identity <SPServiceApplicationProxyGroupPipeBind> -Member <SPServiceApplicationProxyPipeBind >
   ```

   For more information, see [Remove-SPServiceApplicationProxyGroupMember](/powershell/module/sharepoint-server/Remove-SPServiceApplicationProxyGroupMember?view=sharepoint-ps).
    
## See also
<a name="Section2"> </a>

#### Concepts

[Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md)

