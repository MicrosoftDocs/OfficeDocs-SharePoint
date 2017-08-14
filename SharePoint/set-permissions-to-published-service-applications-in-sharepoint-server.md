---
title: Set permissions to published service applications  in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: c598457b-38d9-434c-b715-3786109cd27e
---


# Set permissions to published service applications  in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Search Server 2013, SharePoint Foundation 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to configure permissions to the Application Discovery and Load Balancing Service Application and published service applications for the consuming farm in SharePoint Server 2016 and SharePoint 2013.In SharePoint Server, you must establish a relationship between the publishing farm and the consuming farm by giving the consuming farm permission to the Application Discovery and Load Balancing Service Application on the publishing farm. After doing this, the consuming farm can be given permission to other service applications.In this article:
-  [Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using Windows PowerShell](#section1)
    
  
-  [Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using Central Administration](#section2)
    
  
Before you begin this operation, review  [Share service applications across farms in SharePoint Server](html/share-service-applications-across-farms-in-sharepoint-server.md) for information about prerequisites.
> [!IMPORTANT:]

  
    
    


## Set permission to the Application Discovery and Load Balancing Service Application and any other service application for a consuming farm by using PowerShell
<a name="section1"> </a>

The first procedure explains how to set permission to the Application Discovery and Load Balancing Service Application. The second explains how to set permissions to any other service applications. **To set permission to the Application Discovery and Load Balancing Service Application for a consuming farm by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPFarm | Select Id
  ```


    For more information, see **Get-SPFarm**.
    
  
4. On a server in the publishing farm, access the SharePoint Management Shell and at the PowerShell command prompt, type the following commands:
    
  ```
  $security=Get-SPTopologyServiceApplication | Get-SPServiceApplicationSecurity
  ```


  ```
  $claimprovider=(Get-SPClaimProvider System).ClaimProvider
  ```


  ```
  $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
  ```


  ```
  Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights "Full Control"
  ```


  ```
  Get-SPTopologyServiceApplication | Set-SPServiceApplicationSecurity -ObjectSecurity $security
  ```


    Where  *Consumingfarmid*  is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in the Central Administration section.
    
    For more information, see the following:
    
  - **Get-SPTopologyServiceApplication**
    
  
  - **Set-SPServiceApplicationSecurity**
    
  
  - **Get-SPServiceApplicationSecurity**
    
  
  - **New-SPClaimsPrincipal**
    
  
  - **Get-SPClaimProvider**
    
  
  - **Grant-SPObjectSecurity**
    
  
 **To set permission to a published service application for a publishing farm by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPServiceApplication -Name <ServiceApplicationName> .Id
  ```


  ```
  $security=Get-SPServiceApplication <GUID> | Get-SPServiceApplicationSecurity
  ```


  ```
  $claimprovider=(Get-SPClaimProvider System).ClaimProvider
  ```


  ```
  $principal=New-SPClaimsPrincipal -ClaimType "http://schemas.microsoft.com/sharepoint/2009/08/claims/farmid" -ClaimProvider $claimprovider -ClaimValue <consumingfarmid>
  ```


  ```
  Grant-SPObjectSecurity -Identity $security -Principal $principal -Rights <NamedAccessRights>
  ```


  ```
  Set-SPServiceApplicationSecurity <GUID>  -ObjectSecurity $security
  ```


    Where:
    
     *<ServiceApplicationName>*  is the name of the service application for which you want to find the ID. If the service application name contains spaces, enclose the value in double-quotation marks.
    
     *<Consumingfarmid>*  is the GUID value of the consuming farm. This is the ID of the consuming farm that you need in Step 5 of the Central Administration section.
    
     *<GUID>*  is the ID of the published service application.
    
     *<NamedAccessRights>*  is the name of the access right from the Get-SPServiceApplicationSecurity <GUID>.NamedAccessRights.
    
    For more information, see the following:
    
  - **Get-SPServiceApplication**
    
  
  - **New-SPClaimsPrincipal**
    
  
  - **Get-SPServiceApplicationSecurity**
    
  
  - **Grant-SPObjectSecurity**
    
  
  - **Set-SPServiceApplicationSecurity**
    
  

## Set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration
<a name="section2"> </a>

This procedure explains how to set permission to any service application, but most specifically, the Application and Load Balancing Service Application.
> [!IMPORTANT:]

  
    
    

 **To set permission to the Application Discovery and Load Balancing Service Application and any other published service application for a consuming farm by using Central Administration**
1. On the server that hosts the SharePoint Central Administration website for the publishing farm, verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On Central Administration, click **Application Management**, and then click **Manage service applications**.
    
  
3. Click the row that contains **Application Discovery and Load Balancing Service Application**.
    
  
4. On the ribbon, click **Permissions**.
    
  
5. In the **Connection Permissions** dialog box, do the following:
    
1. Manually paste the ID of the consuming farm. You found the ID earlier in the PowerShell section when you used  *<consumingfarmid>*  .
    
  
2. Click **Add**.
    
  
3. Select the consuming farm ID, and then select the **Full Control** check box.
    
  
4. Click **OK**.
    
  
6. Repeat steps 2 through 5 for any published service applications for which you want to enable access from the consuming farm and assign the necessary permission.
    
  

> [!NOTE:]

  
    
    


# See also

#### 

 [Share service applications across farms in SharePoint Server](html/share-service-applications-across-farms-in-sharepoint-server.md)
  
    
    

  
    
    

