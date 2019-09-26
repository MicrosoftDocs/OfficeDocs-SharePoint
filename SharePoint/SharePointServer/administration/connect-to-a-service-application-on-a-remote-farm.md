---
title: "Connect to service applications on remote farms in SharePoint Server"
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
ms.assetid: e8f2c08c-8e9f-40b4-b066-747d65dcb0e4
description: "Learn how to connect to and consume a published service application in SharePoint Server."
---

# Connect to service applications on remote farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In SharePoint Server, you can publish some service applications to make them available over remote connections. By publishing a service application, you can optimize resources and avoid redundancy, and provide enterprise-wide services without installing a dedicated enterprise services farm.
  
You can connect to a service application that has been shared by another farm if you know the address of the farm's discovery service or the address of the service application. Be aware that you can only connect to a service application on a remote farm if the farm administrator for the remote farm has published the service application.
  
    
Before you begin this operation, review [Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md) for information about prerequisites. 
  
## To connect to a service application on a remote farm by using Central Administration

1. Verify that you are a member of the Farm Administrators SharePoint group.
    
2. On a server in the consuming farm, on Central Administration, click **Application Management**, and then click **Manage service applications**.
    
3. On the ribbon, click **Connect**.
    
4. On the **Connect** drop-down menu, click the kind of service application to which you want to connect. 
    
5. On the Connect to a Remote Service Application page, type the appropriate URL in the **Farm or Service Application address** text box, and then click **OK**. 
    
    > [!NOTE]
    > You can obtain the URL from the administrator of the publishing farm. For more information, see [Publish service applications in SharePoint Server](publish-a-service-application.md). There are two kinds of URLs that you can use in this step: either the URL of the service application or the URL of the remote farm's topology service application. If you use the URL of the service application, only the corresponding service application will be listed in Step 6 of this procedure. If you use the URL of the topology service, all service applications in the farm will be listed in Step 6 of this procedure. 
  
6. The new **Connect to a Remote Service Application** dialog box displays the service applications that match the URL that you typed in Step 5. Click the row that contains the name of the service application, and then select the check box to add the service application connection to the farm's default list of service application connections (that is, the default proxy group). Click **OK**.
    
7. You are prompted to change the connection name. Type a new name into the **Connection Name** text box or leave the default name, and then click **OK**.
    
8. We recommend that you use the instructions in [Exchange trust certificates between farms in SharePoint Server](exchange-trust-certificates-between-farms.md) to establish trust between the two farms. 
    
9. After the new connection is created, you must click **OK** to complete the procedure. 
    
10. Associate the new service application connection with a local Web application. For information about how to do this, see [Add or remove service application connections from a web application in SharePoint Server](add-or-remove-a-service-application-connection-to-a-web-application.md).
    
## To connect to a service application on a remote farm by using PowerShell

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
   Receive-SPServiceApplicationConnectionInfo -FarmUrl <PublishingFarmTopologyURL>
   ```

   Where _\<PublishingFarmTopologyURL\>_ is the information that is retrieved by running the **Get-SPTopologyServiceApplication** cmdlet on the publishing farm. For more information, see [Publish service applications in SharePoint Server](publish-a-service-application.md).
    
4. At the PowerShell command prompt, type the following command: 
    
   ```powershell
   New-SPServiceApplicationProxy -Name " <ServiceApplicationProxyName>" -Url "<PublishingFarmTopologyURL>"
   ```

   Where:
    
   -  _\<ServiceApplicationProxyName\>_ is a unique name for a service application connection on the consuming farm. 
    
   -  _\<PublishingFarmTopologyURL\>_ is the service application topology URL that was also used in the previous command. 
    
   Each kind of service application has a specific PowerShell cmdlet that should be used instead of  _New-SPServiceApplicationProxy_. (These cmdlets are listed in the See Also section.) For example, the following command creates a new Managed Metadata service application proxy named "MetadataServiceProxy1" that connects to the service application located at the stated URL.
    
   ```powershell
   New-SPMetadataServiceApplicationProxy -Name "MetadataServiceProxy1" -Uri "
   urn:schemas-microsoft-com:sharepoint:service:9c1870b7ee97445888d9e846519cfa27#authority=urn:uuid:02a493b92a5547828e21386e28056cba&amp;authority=https://ua_powershell:32844/Topology/topology.svc  "
   ```

5. You must associate the new service application connection with a local Web application. For information about how to do this, see [Add or remove service application connections from a web application in SharePoint Server](add-or-remove-a-service-application-connection-to-a-web-application.md).
    
## See also

#### Other Resources

[New-SPBusinessDataCatalogServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPBusinessDataCatalogServiceApplicationProxy?view=sharepoint-ps)
  
[New-SPEnterpriseSearchServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPEnterpriseSearchServiceApplicationProxy?view=sharepoint-ps)
  
[New-SPMetadataServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPMetadataServiceApplicationProxy?view=sharepoint-ps)
  
[New-SPProfileServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPProfileServiceApplicationProxy?view=sharepoint-ps)
  
[New-SPSecureStoreServiceApplicationProxy](/powershell/module/sharepoint-server/New-SPSecureStoreServiceApplicationProxy?view=sharepoint-ps)

