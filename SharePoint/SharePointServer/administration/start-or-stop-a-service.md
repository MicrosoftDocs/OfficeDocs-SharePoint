---
title: "Start or stop a service in SharePoint Server"
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
ms.assetid: 6641730b-7099-47c0-938f-783ea8ef8e62
description: "Learn how to start and stop a service in SharePoint Server."
---

# Start or stop a service in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
SharePoint Server includes services that reside on individual servers in the farm. In some cases, you can configure global service settings and start or stop a service. Services are managed directly in the SharePoint Central Administration website instead of through a separate administration site. You can also remotely monitor and manage services. Additionally, you can manage services by using Microsoft PowerShell. 
  
  
## Starting or stopping a service

You can manage services by using Central Administration or by using PowerShell.
  
 **To start or stop a service by using Central Administration**
  
1. Confirm that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group. 
    
2. On the Central Administration home page, click **System Settings**. 
    
3. On the System Settings page, in the **Servers** section, click **Manage services on server**.
    
4. To change the server on which you want to start or stop the service, on the **Server** menu, click **Change Server**, and then click the server name that you want. 
    
5. By default, only configurable services are displayed. To view all services, on the **View** menu, click **All**.
    
6. To start or stop a service, click **Restart** or **Stop** in the **Action** column of the relevant service. 
    
7. Click **OK** to start or stop the service. 
    
 **To start a service by using Microsoft PowerShell**
  
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
   Start-SPServiceInstance -Identity <ServiceGUID>
   ```

   Where _\<ServiceGUID\>_ is the GUID of the service. If you do not know the service GUID, you can retrieve a list of all services in the farm together with their GUIDs by using the **Get-SPServiceInstance** cmdlet. 
    
For more information, see [Start-SPServiceInstance](/powershell/module/sharepoint-server/start-spserviceinstance?view=sharepoint-ps).
  
 **To stop a service by using PowerShell**
  
1. Start the SharePoint Management Shell.
    
2. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Stop-SPServiceInstance -Identity <ServiceGUID>
   ```

    Where  _\<ServiceGUID\>_ is the GUID of the service. If you do not know the service GUID, you can retrieve a list of all services in the farm together with their GUIDs by using the **Get-SPServiceInstance** cmdlet. 
    
For more information, see [Stop-SPServiceInstance](/powershell/module/sharepoint-server/stop-spserviceinstance?view=sharepoint-ps). We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## See also

#### Concepts

[Administration of SharePoint Server](administration.md)
#### Other Resources

[Get-SPServiceInstance](/powershell/module/sharepoint-server/Get-SPServiceInstance?view=sharepoint-ps)

