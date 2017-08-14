---
title: Exchange trust certificates between farms in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6d8a9d37-d400-4d7c-b4f1-bf3c5643c98c
---


# Exchange trust certificates between farms in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to exchange trust certificates between the publishing farm and the consuming farm in SharePoint Server 2016 and SharePoint 2013.In SharePoint Server, a farm can connect to and consume a service application that is published on another SharePoint Server farm. For this to occur, the farms must exchange trust certificates. Both farms must participate in this exchange for service application sharing to work.For more information about how to share service applications across farms see  [Share service applications across farms in SharePoint Server](html/share-service-applications-across-farms-in-sharepoint-server.md).You must use Microsoft PowerShell commands to export and copy the certificates between farms. After the certificates are exported and copied, you can use either PowerShell commands or Central Administration to manage the trusts within the farm.The instructions here assume the following criteria:
- That the servers that are used for these procedures are running PowerShell.
    
  
- That the administrator will select and use the same server in each farm for all steps in the process.
    
  
- If User Account Control (UAC) is turned on, you must run the PowerShell commands with elevated privileges.
    
  
In this article:
-  [Exporting and copying certificates](#Section2)
    
  
-  [Managing trust certificates by using Windows Powershell](#Section2a)
    
  
-  [Managing trust certificates by using Central Administration](#Section4)
    
  
Before you begin this operation, review  [Share service applications across farms in SharePoint Server](html/share-service-applications-across-farms-in-sharepoint-server.md) for information about prerequisites.
## Exporting and copying certificates
<a name="Section2"> </a>

An administrator of the consuming farm must provide two trust certificates to the publishing farm: a root certificate and a security token service (STS) certificate. An administrator of the publishing farm must provide a root certificate to the consuming farm.You can only export and copy certificates by using Windows PowerShell 3.0 or later. **To export the root certificate from the consuming farm**
1. On a server that is running SharePoint Server on the consuming farm, verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
$rootCert = (Get-SPCertificateAuthority).RootCertificate
  ```


  ```
  $rootCert.Export("Cert") | Set-Content <C:\\ConsumingFarmRoot.cer>  -Encoding byte
  ```


    
    
    Where  *<C:\\ConsumingFarmRoot.cer>*  is the path of the root certificate.
    
  
 **To export the STS certificate from the consuming farm**
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
  
$stsCert = (Get-SPSecurityTokenServiceConfig).LocalLoginProvider.SigningCertificate
  ```


  ```
  $stsCert.Export("Cert") | Set-Content <C:\\ConsumingFarmSTS.cer>  -Encoding byte
  ```


    
    
    Where  *<C:\\ConsumingFarmSTS.cer>*  is the path of the STS certificate.
    
  
 **To export the root certificate from the publishing farm**
1. On a server that is running SharePoint Server on the publishing farm, verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
$rootCert = (Get-SPCertificateAuthority).RootCertificate
  ```


  ```
  $rootCert.Export("Cert") | Set-Content <C:\\PublishingFarmRoot.cer>  -Encoding byte
  ```


    
    
    Where  *<C:\\PublishingFarmRoot.cer>*  is the path of the root certificate.
    
  
 **To copy the certificates**
1. Copy the root certificate and the STS certificate from the server in the consuming farm to the server in the publishing farm. 
    
  
2. Copy the root certificate from the server in the publishing farm to a server in the consuming farm. 
    
  

## Managing trust certificates by using PowerShell
<a name="Section2a"> </a>

Managing trust certificates in a farm involves establishing trust. This section describes how to establish trust on both the consuming and publishing farms by using PowerShell commands.
## Establishing trust on the consuming farm
<a name="Section3"> </a>

To establish trust on the consuming farm, you must import the root certificate that was copied from the publisher farm and create a trusted root authority. **To import the root certificate and create a trusted root authority on the consuming farm**
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
  
$trustCert = Get-PfxCertificate <C:\\PublishingFarmRoot.cer>
  ```


  ```
  New-SPTrustedRootAuthority <PublishingFarm>  -Certificate $trustCert
  ```


    
    
    Where:
    
  -  *<C:\\PublishingFarmRoot.cer>*  is the path of the root certificate that you copied to the consuming farm from the publishing farm.
    
  
  -  *<PublishingFarm>*  is a unique name that identifies the publishing farm. Each trusted root authority must have a unique name.
    
  

## Establishing trust on the publishing farm
<a name="Section3"> </a>

To establish trust on the publishing farm, you must import the root certificate that was copied from the consuming farm and create a trusted root authority. You must then import the STS certificate that was copied from the consuming farm and create a trusted service token issuer. **To import the root certificate and create a trusted root authority on the publishing farm**
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
  
$trustCert = Get-PfxCertificate <C:\\ConsumingFarmRoot.cer>
  ```


  ```
  New-SPTrustedRootAuthority <ConsumingFarm>  -Certificate $trustCert
  ```


    
    
    Where:
    
  -  *<C:\\ConsumingFarmRoot.cer>*  is the name and location of the root certificate that you copied to the publishing farm from the consuming farm.
    
  
  -  *<ConsumingFarm>*  is a unique name that identifies the consuming farm. Each trusted root authority must have a unique name.
    
  
 **To import the STS certificate and create a trusted service token issuer on the publishing farm**
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
  
$stsCert = Get-PfxCertificate
<c:\\ConsumingFarmSTS.cer>
  ```


  ```
  
New-SPTrustedServiceTokenIssuer <ConsumingFarm>  -Certificate $stsCert
  ```


    Where:
    
  -  *<C:\\ConsumingFarmSTS.cer>*  is the path of the STS certificate that you copied to the publishing farm from the consuming farm.
    
  
  -  *<ConsumingFarm>*  is a unique name that identifies the consuming farm. Each trusted service token issuer must have a unique name.
    
  
Where:For more information about these PowerShell cmdlets, see the following articles:
- **Get-SPCertificateAuthority**
    
  
- **Get-SPSecurityTokenServiceConfig**
    
  
- **New-SPTrustedRootAuthority**
    
  
- **New-SPTrustedServiceTokenIssuer**
    
  
-  [Get-PfxCertificate](http://go.microsoft.com/fwlink/?LinkID=717913&amp;clcid=0x409)
    
  
For information about how to use a script to automate part of this process, see  [Exchange trust certificates between farms](https://go.microsoft.com/fwlink/p/?LinkId=230666).
## Managing trust certificates by using Central Administration
<a name="Section4"> </a>

You can manage trusts on a farm only after the relevant certificates have already been exported and copied to the farm. **To establish trust by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. On the SharePoint Central Administration website, click **Security**.
    
  
3. On the Security page, in the **General Security** section, click **Manage trust**.
    
  
4. On the Trust Relationship page, on the ribbon, click **New**.
    
  
5. On the Establish Trust Relationship page:
    
1. Supply a name that describes the purpose of the trust relationship. 
    
  
2. Browse to and select the Root Authority Certificate for the trust relationship. This must be the Root Authority Certificate that was exported from the other farm by using Microsoft PowerShell, as described in  [Exporting and copying certificates](#Section2). 
    
  
3. If you are performing this task on the publishing farm, select the check box for **Provide Trust Relationship**. Type in a descriptive name for the token issuer and browse to and select the STS certificate that was copied from the consuming farm, as described in [Exporting and copying certificates](#Section2).
    
  
4. Click **OK**.
    
  

    After a trust relationship is established, you can modify the Token Issuer description or the certificates that are used by clicking the trust, and then clicking **Edit**. You can delete a trust by clicking it, and then clicking **Delete**.
    
  

# See also

#### 

 [Plan for user authentication methods in SharePoint Server](html/plan-for-user-authentication-methods-in-sharepoint-server.md)
  
    
    

#### 

 **Create a web application in SharePoint Server**
  
    
    
 **Configure SAML-based claims authentication with AD FS in SharePoint Server**
  
    
    

  
    
    

