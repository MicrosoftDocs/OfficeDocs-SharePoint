---
title: "Set permissions to published service applications in SharePoint Server"
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
ms.assetid: c598457b-38d9-434c-b715-3786109cd27e
description: "Learn how to configure permissions to the Application Discovery and Load Balancing Service Application and published service applications for the consuming farm in SharePoint Server."
---

# Set permissions to published service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In SharePoint Server, you must establish a relationship between the publishing farm and the consuming farm by giving the consuming farm permission to the Application Discovery and Load Balancing Service Application on the publishing farm. After doing this, the consuming farm can be given permission to other service applications.
  
    
Before you begin this operation, review [Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md) for information about prerequisites. 
  
> [!IMPORTANT]
> You must perform steps 1 through 5 in the PowerShell procedure to obtain the consuming farm ID, which you must have in order to complete either the PowerShell or Central Administration procedures. 
  
## Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using PowerShell
<a name="section1"> </a>

The first procedure explains how to set permission to the Application Discovery and Load Balancing Service Application. The second explains how to set permissions to any other service applications.
  
### To set permission to the Application Discovery and Load Balancing Service Application for a consuming farm by using PowerShell

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
   Get-SPFarm | Select Id
   ```

   For more information, see [Get-SPFarm](/powershell/module/sharepoint-server/Get-SPFarm?view=sharepoint-ps).
    
4. On a server in the publishing farm, access the SharePoint Management Shell and at the PowerShell command prompt, type the following commands:
    
   ```powershell
   $security=Get-SPTopologyServiceApplication | Get-SPServiceApplicationSecurity
   $claimprovider=(Get-SPClaimProvider System).ClaimProvider
   $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
   Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights "Full Control"
   Get-SPTopologyServiceApplication | Set-SPServiceApplicationSecurity -ObjectSecurity $security
   ```

   Where  _Consumingfarmid_ is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in the Central Administration section. 
    
    For more information, see the following:
    
  - [Get-SPTopologyServiceApplication](/powershell/module/sharepoint-server/Get-SPTopologyServiceApplication?view=sharepoint-ps)
    
  - [Set-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Set-SPServiceApplicationSecurity?view=sharepoint-ps)
    
  - [Get-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Get-SPServiceApplicationSecurity?view=sharepoint-ps)
    
  - [New-SPClaimsPrincipal](/powershell/module/sharepoint-server/New-SPClaimsPrincipal?view=sharepoint-ps)
    
  - [Get-SPClaimProvider](/powershell/module/sharepoint-server/Get-SPClaimProvider?view=sharepoint-ps)
    
  - [Grant-SPObjectSecurity](/powershell/module/sharepoint-server/Grant-SPObjectSecurity?view=sharepoint-ps)
    
### To set permission to a published service application for a consuming farm by using PowerShell

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
   $sa = Get-SPServiceApplication -Name '<Service Application DisplayName>'
   $security=Get-SPServiceApplication $sa | Get-SPServiceApplicationSecurity
   $claimprovider=(Get-SPClaimProvider System).ClaimProvider
   $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
   Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights <NamedAccessRights>
   Set-SPServiceApplicationSecurity $sa -ObjectSecurity $security
   ```

   Where:
    * \<Service Application DisplayName\> is the DisplayName value of the published Service Application from `Get-SPServiceApplication`.
    * \<Consumingfarmid\> is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in Step 5 of the Central  Administration section. 
    * \<NamedAccessRights\> is the name of the access right from `(Get-SPServiceApplicationSecurity $sa).NamedAccessRights`. 
    
    For more information, see the following:
    
  - [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps)
    
  - [New-SPClaimsPrincipal](/powershell/module/sharepoint-server/New-SPClaimsPrincipal?view=sharepoint-ps)
    
  - [Get-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Get-SPServiceApplicationSecurity?view=sharepoint-ps)
    
  - [Grant-SPObjectSecurity](/powershell/module/sharepoint-server/Grant-SPObjectSecurity?view=sharepoint-ps)
    
  - [Set-SPServiceApplicationSecurity](/powershell/module/sharepoint-server/Set-SPServiceApplicationSecurity?view=sharepoint-ps)
    
## Set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration
<a name="section2"> </a>

This procedure explains how to set permission to any service application, but most specifically, the Application and Load Balancing Service Application.
  
> [!IMPORTANT]
> You must perform steps 1 through 5 in the PowerShell procedure to obtain the consuming farm ID, which you must have in order to complete this procedure. 
  
### To set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration

1. On the server that hosts the SharePoint Central Administration website for the publishing farm, verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. On Central Administration, click **Application Management**, and then click **Manage service applications**.
    
3. Click the row that contains **Application Discovery and Load Balancing Service Application**.
    
4. On the ribbon, click **Permissions**.
    
5. In the **Connection Permissions** dialog box, do the following: 
    
   - Manually paste the ID of the consuming farm. You found the ID earlier in the PowerShell section when you used  _\<consumingfarmid\>_.
    
   - Click **Add**.
    
   - Select the consuming farm ID, and then select the **Full Control** check box. 
    
   - Click **OK**.
    
6. Repeat steps 2 through 5 for any published service applications for which you want to enable access from the consuming farm and assign the necessary permission.
    
> [!NOTE]
> To enable access to the User Profile service application, you must give the consuming farm's web application pool identity (that is, DOMAIN\Username) the permission instead of the consuming farm ID. 
  
## See also
<a name="section2"> </a>

#### Concepts

[Share service applications across farms in SharePoint Server](share-service-applications-across-farms.md)

