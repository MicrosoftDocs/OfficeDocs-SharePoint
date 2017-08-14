---
title: Role conversion using MinRole in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: bcbddee7-1c77-4788-9a32-fb585c48ee37
---


# Role conversion using MinRole in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn about how to convert your server roles in a SharePoint farm deployment using **MinRole**. MinRole help administrators select the right server role when provisioning SharePoint Server 2016.
## Role Conversion

 **About Server Role Conversion**Servers can be converted to a different server role without having to disconnect them from your farm and then rejoining them using the different server role. Servers can be converted to dedicated roles, shared roles, the Custom server role, or the Single-Server Farm server role. Server role conversion can be performed through the the SharePoint Central Administration website or Microsoft PowerShell.
> [!NOTE:]

  
    
    

Before a server is converted to a different server role, SharePoint will perform a role conversion pre-validation check to ensure the server is ready for role conversion. If the pre-validation check determines that a server isn't ready for role conversion, it will block the role conversion and present a message explaining why the role conversion was blocked. It will also provide instructions to resolve the issue that blocked role conversion. Once the issue is resolved, you can rerun the role conversion.
> [!NOTE:]

  
    
    

 **Distributed Cache and role conversion**Role conversion can't automatically enable, disable, or reconfigure the Distributed Cache service. You must manually enable, disable, or reconfigure the Distributed Cache service before performing role conversion. If this step isn't performed before role conversion, role conversion pre-validation will block the role conversion.To enable the Distributed Cache service, the administrator runs the **Add-SPDistributedCacheServiceInstance** cmdlet on the target server, specifying the desired role with the **Role** parameter (that is,-Role <role name>). To disable the Distributed Cache service, the administrator runs the **Remove-SPDistributedCacheServiceInstance** cmdlet on the target server. **Search and role conversion**Role conversion can't convert a server from a role hosting Search to a role that doesn't host Search if the server is part of an active Search topology. You must remove the server from the active Search topology before performing role conversion. If this step isn't performed before role conversion, role conversion pre-validation will block the role conversion.
> [!NOTE:]

  
    
    


## How to change a server role
<a name="changerole"> </a>

 **To change a server role by using the Central Administration Website**
1. Verify that the user account that is performing this procedure is a member of the local Administrators group.
    
  
2. On the Central Administration web site, click **System Settings**.
    
  
3. On the **System Settings** page, click **Convert server role in this farm**.
    
  
4. On the **Role Conversion** page, in the **New Role** area, click the drop-down box to select the new server role for each server to ﻿change.
    
  
5. Click **Apply**.
    
  
 **To change a server role by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - local Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. On the **Start** menu, click **Microsoft SharePoint 2016 Products**.
    
  
3. Click **SharePoint 2016 Management Shell**.
    
  
4. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPServer -Identity <server name> -Role <server role>
  ```


    Where:
    
  - <server name> is the server to change.
    
  
  -  *<server role>*  is the name of the new server role, which includes the values: WebFrontEnd, Application, DistributedCache, Search, WebFrontEndWithDistributedCache, ApplicationWithSearch, SingleServerFarm, or Custom.
    
  
For more information about how to change a server role by using PowerShell_2nd_NoVer, see Set-SPServer.
