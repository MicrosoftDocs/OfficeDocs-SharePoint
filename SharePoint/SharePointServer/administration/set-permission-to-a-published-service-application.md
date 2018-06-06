---
title: "Set permissions to published service applications in SharePoint Server"
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
ms.assetid: c598457b-38d9-434c-b715-3786109cd27e
description: "Summary: Learn how to configure permissions to the Application Discovery and Load Balancing Service Application and published service applications for the consuming farm in SharePoint Server 2016 and SharePoint 2013."
---

# Set permissions to published service applications in SharePoint Server

 **Summary:** Learn how to configure permissions to the Application Discovery and Load Balancing Service Application and published service applications for the consuming farm in SharePoint Server 2016 and SharePoint 2013. 
  
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
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPFarm | Select Id
  ```

    For more information, see [Get-SPFarm](http://technet.microsoft.com/library/fe68fb39-f5dc-4e80-b7f2-ac203a71cc82.aspx).
    
4. On a server in the publishing farm, access the SharePoint Management Shell and at the PowerShell command prompt, type the following commands:
    
  ```
  $security=Get-SPTopologyServiceApplication | Get-SPServiceApplicationSecurity
  $claimprovider=(Get-SPClaimProvider System).ClaimProvider
  $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
  Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights "Full Control"
  Get-SPTopologyServiceApplication | Set-SPServiceApplicationSecurity -ObjectSecurity $security
  ```

    Where  _Consumingfarmid_ is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in the Central Administration section. 
    
    For more information, see the following:
    
  - [Get-SPTopologyServiceApplication](http://technet.microsoft.com/library/fc40e2b8-5710-4034-b37f-b4e61008410a.aspx)
    
  - [Set-SPServiceApplicationSecurity](http://technet.microsoft.com/library/8d769193-f126-43f7-8c1e-4bec75c8446d.aspx)
    
  - [Get-SPServiceApplicationSecurity](http://technet.microsoft.com/library/4f433fea-ddbf-4843-a11c-d936ce51c6bb.aspx)
    
  - [New-SPClaimsPrincipal](http://technet.microsoft.com/library/0831e64b-3ec0-4016-8128-639991530172.aspx)
    
  - [Get-SPClaimProvider](http://technet.microsoft.com/library/43aa9964-e7bb-48d3-b6ab-91a9c2edba88.aspx)
    
  - [Grant-SPObjectSecurity](http://technet.microsoft.com/library/496caa92-2ff4-4048-ab7d-57d8c835bf2b.aspx)
    
### To set permission to a published service application for a publishing farm by using PowerShell

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPServiceApplication .Id
  $security=Get-SPServiceApplication <GUID>| Get-SPServiceApplicationSecurity
  $claimprovider=(Get-SPClaimProvider System).ClaimProvider
  $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
  Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights <NamedAccessRights>
  Set-SPServiceApplicationSecurity <GUID> -ObjectSecurity $security
  ```

    Where:
    
    
     _\<Consumingfarmid\>_ is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in Step 5 of the Central Administration section. 
    
     _\<GUID\>_ is the ID of the published service application. 
    
     _\<NamedAccessRights\>_ is the name of the access right from the Get-SPServiceApplicationSecurity \<GUID\>.NamedAccessRights. 
    
    For more information, see the following:
    
  - [Get-SPServiceApplication](http://technet.microsoft.com/library/71a467dc-3b95-4b65-af93-0d0d6ebb8326.aspx)
    
  - [New-SPClaimsPrincipal](http://technet.microsoft.com/library/0831e64b-3ec0-4016-8128-639991530172.aspx)
    
  - [Get-SPServiceApplicationSecurity](http://technet.microsoft.com/library/4f433fea-ddbf-4843-a11c-d936ce51c6bb.aspx)
    
  - [Grant-SPObjectSecurity](http://technet.microsoft.com/library/496caa92-2ff4-4048-ab7d-57d8c835bf2b.aspx)
    
  - [Set-SPServiceApplicationSecurity](http://technet.microsoft.com/library/8d769193-f126-43f7-8c1e-4bec75c8446d.aspx)
    
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

