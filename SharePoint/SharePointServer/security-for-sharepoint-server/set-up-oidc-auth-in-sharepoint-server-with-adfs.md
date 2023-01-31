---
title: "Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)"
ms.reviewer: 
ms.author: v-jmathew
author: jitinmathew
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)."
---

# Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

## Prerequisites

When you configure with AD FS OIDC, you need the following resources to perform the configuration:

1. A SharePoint Server farm.
2. AD FS in Windows Server 2016 or later, already created, with the public key of the AD FS signing certificate exported in a `.cer` file.

This article uses the following example values for AD FS OIDC setup:

| Value | Link |
|---------|---------|
| SharePoint site URL | `https://spsites.contoso.local/` |
| AD FS site URL     | `https://adfs.contoso.local/adfs/` |
| AD FS authentication endpoint | `https://adfs.contoso.local/adfs/oauth2/authorize` |
| RegisteredIssuerName URL | `https://adfs.contoso.local/adfs/` |
| AD FS SignoutURL  | `https://adfs.contoso.local/adfs/oauth2/logout` |
| Identity claim type | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| Windows site collection administrator | contoso\yvand |
| Email value of the federated (AD FS) site collection administrator | yvand@contoso.local |

## Step 1: Setup identity provider

Perform the following steps to set up OIDC with AD FS:

1. In AD FS Management, right-click on **Application Groups** and select **Add Application Group**.
2. Go to the **Welcome** page, enter **ADFSSSO** in the **Name** field and under **Client-Server applications**, select the **Web browser accessing a web application** template. Then, select **Next**.

    :::image type="content" source="../media/add-application-group-wizard.png" alt-text="Add Application Group Wizard":::

3. Go to the **Native Application** page and copy the **Client Identifier** value. It will be used later as the value for `DefaultClientIdentifier` parameter during SharePoint configuration.
4. Under the **Redirect URL** field, enter `https://spsites.contoso.local/` and select **Add**. Then, select **Next**.

    :::image type="content" source="../media/add-application-group-wizard-2.png" alt-text="Add Application Group Wizard 2":::

5. Go to the **Summary** page and select **Next**.

    :::image type="content" source="../media/add-application-group-wizard-3.png" alt-text="Add Application Group Wizard 3":::

6. Go to the **Complete** page and select **Close**.
7. Export **Token-signing** certificate from AD FS. This token-signing certificate will be used in SharePoint setup. The following images show how to export **Token-signing** certificate from AD FS:

    :::image type="content" source="../media/adfs-certificates.png" alt-text="AD FS Certificate Export 1":::

    :::image type="content" source="../media/adfs-certificate-export-2.png" alt-text="AD FS Certificate Export 2":::

    :::image type="content" source="../media/adfs-certificate-export-3.png" alt-text="AD FS Certificate Export 3":::

    :::image type="content" source="../media/adfs-certificate-export-4.png" alt-text="AD FS Certificate Export 4":::

8. Ensure that the required claim ID is included in the `id_token` from AD FS. Let’s consider email as an example:

    We assume that your AD FS has configured the rule that read identifier claim from attribute store, such as AD. Perform the following steps to create **Issuance Transform Rule** for this specific web application we created in AD FS previously:

    1. Open the web application you created and go to the **Issue Transformation Rule** tab.

        :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

    2. Select **Add Rule** and select **Send LDAP Attributes as Claims** from the option list.

        :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

        :::image type="content" source="../media/add-transform-claim-rule.png" alt-text="Add Transform Claim Rule":::

    3. Name your Claim rule as **AD** and select **Active Directory** from the **Attribute store** dropdown menu. Create two mappings using the drop-down boxes as shown:

        | Attribute | Value |
        |---------|---------|
        | E-Mail-Addresses | E-Mail Address |
        | Token-Groups - Qualified by Domain Name | Role |

        :::image type="content" source="../media/add-transform-claim-rule-2.png" alt-text="Add Transform Claim Rule 2":::

    4. Select **Finish** to close the Rule wizard and select **OK** to close the web application properties. Select **OK** one more time to complete the Rule.

If you're setting OIDC with SharePoint Server, nbf claim must be configured in AD FS server side in the web application you created. If nbf claim doesn’t exist in this web application, perform the following steps to create it:

1. Open the web application you created and go to the **Issue Transformation Rule** tab.

    :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

2. Select **Add Rule** and then select **Apply**. In the **Add Transform Claim Rule Wizard** select **Send Claims Using a Custom Rule** from the **Claim rule template** options.

    :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

    :::image type="content" source="../media/add-transform-claim-rule-3.JPG" alt-text="Add Transform Claim Rule 3":::

3. Select **Next** and input the following string in the **Custom rule** field:

    `c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"] => issue(Type = "nbf", Value = "0");`

    :::image type="content" source="../media/add-transform-claim-rule-4.JPG" alt-text="Add Transform Claim Rule 4":::

4. Select **Finish**.

## Step 2: Change SharePoint farm properties

In this step, you'll need to modify the SharePoint farm properties. Start the SharePoint Management Shell and run the following script:

> [!NOTE]
> Read the instructions mentioned in the following PowerShell script carefully.

```powershell
# Setup farm properties to work with OIDC
#Create a self-signed certificate in one SharePoint Server in the farm
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"

#if you have multiple SharePoint servers in the farm, you need to export certificate by Export-PfxCertificate and import certificate to all the SharePoint servers in the farm by Import-PfxCertificate. 

#After certificate is successfully imported to SharePoint Server, we will need to grant access permission to certificate private key.

$rsaCert = [System.Security.Cryptography.X509Certificates.RSACertificateExtensions]::GetRSAPrivateKey($cert)
$fileName = $rsaCert.key.UniqueName
$path = "$env:ALLUSERSPROFILE\Microsoft\Crypto\RSA\MachineKeys\$fileName"
$permissions = Get-Acl -Path $path
#please replace the <web application pool account> with real application pool account of your web application
$access_rule = New-Object System.Security.AccessControl.FileSystemAccessRule(<Web application pool account>, 'Read', 'None', 'None', 'Allow')
$permissions.AddAccessRule($access_rule)
Set-Acl -Path $path -AclObject $permissions

#Then we update farm properties
$f = Get-SPFarm
$f.Farm.Properties['SP-NonceCookieCertificateThumbprint']=$cert.Thumbprint
$f.Farm.Properties['SP-NonceCookieHMACSecretKey']='seed'
$f.Farm.Update()
```

## Step 3: Configure SharePoint to trust the identity providers

In this step, you'll create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AD FS as OIDC provider. Start the SharePoint Management Shell and run the following script to create it:

> [!NOTE]
> Read the instructions mentioned in the following PowerShell script carefully.

```powershell
# Define claim types
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

# Public key of the AD FS signing certificate
$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
# Set the AD FS URL where users are redirected to authenticate
$authendpointurl = "https://adfs.contoso.local/adfs/oauth2/authorize"
$registeredissuernameurl = "https://adfs.contoso.local/adfs"
$signouturl = "https://adfs.contoso.local/adfs/oauth2/logout"

#Please replace <Client Identifier> with the value you saved in step #3 of AD FS Setup section
$clientIdentifier = <Client Identifier>

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "Contoso.local" -Description "Contoso.local" -ImportTrustCertificate $signingCert -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -RegisteredIssuerName $registeredissuernameurl  -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -DefaultClientIdentifier $clientIdentifier
```

Here, `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is extended to support OIDC by using the following parameters:

| Parameter | Description |
|------------|-------------|
|Name     | Gives a name to the new token issuer. |
|Description     | Gives a description to the new token issuer. |
|ImportTrustCertificate     |  Imports a list of X509 Certificates, which will be used to validate `id_token` from OIDC identifier. If the OIDC IDP uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint will then validate `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A `SPClaimTypeMapping` object, which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifies the type of identifier. |
| RegisteredIssuerName | Specifies the issuer identifier, which issues the `id_token`. It will be used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifies the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifies the sign-out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specifies the `client_id` of SharePoint server, which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specifies the response type of IDP, which can be accepted by this token issuer. It can accept two strings: `id_token` and `code id_token`. If this parameter isn't provided, it will use `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store and there are two possible options to do this:
>
> - If the AD FS signing certificate is issued by a certificate authority (best practice for security reasons).
>
>     The public key of the issuer's certificate (and all the intermediates) must be added to the store. Start the SharePoint Management Shell and run the following script to add the certificate:
>
>     ```powershell
>     $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing issuer.cer")
>     New-SPTrustedRootAuthority -Name "adfs.contoso.local signing root authority" -Certificate $rootCert
>     ```
>
> - If the AD FS signing certificate is a self-signed certificate (not recommended for security reasons).
>
>     The public key of the AD FS signing certificate itself must be added to the store. Start the SharePoint Management Shell and run the following script to add the certificate:
>
>     ```powershell
>     $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
>     New-SPTrustedRootAuthority -Name "adfs.contoso.local signing certificate" -Certificate $rootCert
>     ```

## Step 4: Configure a SharePoint web application

In this step, you'll configure a web application in SharePoint to be federated with the AD FS OIDC, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

> [!IMPORTANT]
>
> - The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the search crawler.
> - SharePoint URL that will use AD FS OIDC federation must be configured with HTTPS.

You can do this configuration either by:

- Creating a new web application and using both Windows and AD FS OIDC authentication in the Default zone. To create a new web application, do the following:
  1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

        ```powershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
        $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

  2. Follow [Create a web application in SharePoint Server](/sharepoint/administration/create-a-web-application) to create a new web application enabling HTTPS/SSL named SharePoint - OIDC on contoso.local.
  3. Open the SharePoint Central Administration site.
  4. Open the web application you created and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers-3.jpg" alt-text="Authentication Providers 3":::

  5. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
  6. Filter the display with the new web application and confirm that you see the following information:

      :::image type="content" source="../media/alternate-access-mapping-collection.png" alt-text="Alternate Access Mapping Collection-1":::

- Extending an existing web application to set AD FS OIDC authentication on a new zone. To extend an existing web application, do the following:
    1. Start the SharePoint Management Shell and run the following script:

        ```powershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
        $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

    2. Open the SharePoint Central Administration site.
    3. Open the web application you want to extend OIDC authentication to and pick **contoso.local** as **Trusted Identity Provider**.

        :::image type="content" source="../media/authentication-providers-4.jpg" alt-text="Authentication Providers 4":::

    4. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
    5. Filter the display with the web application that was extended and confirm that you see the following information:

        :::image type="content" source="../media/alternate-access-mapping-collection-2.png" alt-text="Alternate Access Mapping Collection":::

## Step 5: Ensure the web application is configured with SSL certificate

Since OpenID Connect 1.0 authentication can only work with HTTPS protocol, a certificate must be set on the corresponding web application. Perform the following steps to set a certificate:

- Generate the site certificate:

    > [!NOTE]
    > You may skip this step if you have already generated the certificate.

    1. Open the SharePoint PowerShell console.
    2. Run the following script to generate a self-signed certificate and add it to the SharePoint farm:

        ```powershell
        New-SPCertificate -FriendlyName "Contoso SharePoint (2021)" -KeySize 2048 -CommonName spsites.contoso.local -AlternativeNames extranet.contoso.local, onedrive.contoso.local -OrganizationalUnit "Contoso IT Department" -Organization "Contoso" -Locality "Redmond" -State "Washington" -Country "US" -Exportable -HashAlgorithm SHA256 -Path "\\server\fileshare\Contoso SharePoint 2021 Certificate Signing Request.txt"
        Move-SPCertificate -Identity "Contoso SharePoint (2021)" -NewStore EndEntity
        ```

        > [!IMPORTANT]
        > Self-signed certificates are suitable only for test purposes. In production environments, we strongly recommend that you use certificates issued by a certificate authority instead.

- Set the certificate:

    You can use the following PowerShell cmdlet to assign the certificate to the web application:

    ```powershell
    Set-SPWebApplication -Identity https://spsites.contoso.local -Zone Default -SecureSocketsLayer -Certificate "Contoso SharePoint (2021)"
    ```

## Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (AD FS) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections**.
3. Type a Title, URL, and select the template Team Site.
4. In the **Primary Site Collection Administrator** section, select the book icon to open the People Picker dialog.
5. In the People Picker dialog, type the Windows administrator account, for example **yvand**.
6. Filter the list on the left by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people-3.png" alt-text="Select People 3":::

7. Go to the account and select **OK**.
8. In the **Secondary Site Collection Administrator** section, select the book icon to open the People Picker dialog.
9. In the People Picker dialog, type the exact email value of the AD FS administrator account, for example **yvand@contoso.local**.
10. Filter the list on the left by selecting **Contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-4.png" alt-text="Select People 4":::

11. Go to the account and select **OK**.
12. Select **OK** to create the site collection.

Once the site collection is created, you will be able to sign-in using either the Windows or the federated site collection administrator account.

## Step 7: Set up People Picker

In OIDC authentication, the People Picker doesn't validate the input, which can lead to misspellings or users accidentally selecting the wrong claim type. This can be addressed using the new UPA-backed claim provider in SharePoint Server.

Perform the following steps to help People Picker validate the input using the new UPA-backed claim provider:

### 1. Create a new claim provider

In the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-providers), you've already created an OIDC `SPTrustedIdentityTokenIssuer` by using `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet. In this step, you'll use the following PowerShell cmdlet to create a claim provider, which uses the User Profile Application service to search and resolve users and groups in the People Picker and specifies to use the OIDC `SPTrustedIdentityTokenIssuer`:

  ```powershell
  $claimprovider = New-SPClaimProvider -AssemblyName "Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c" -DisplayName 'OIDC Claim Provider' -Type "Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider" -TrustedTokenIssuer $tokenissuer -Description “OIDC Claim Provider” -Default:$false
  ```

Specify the following parameters:

| Parameter | Description |
|------------|-------------|
| AssemblyName | To be specified as `Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c`. |
| Type | To be specified as `Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider` so that this command creates a claim provider, which uses UPA as the claim source. |
| TrustedTokenIssuer | To be specified as the OIDC `SPTrustedIdentityTokenIssuer` created in the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-providers), which will use this claim provider. This is a new parameter the user needs to provide when the type of the claim provider is `Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider`. |
| Default | As we've created a claim provider by using this cmdlet, this cmdlet can only work with `SPTrustedIdentityTokenIssuer` and `Default` parameter must be set to false so that it won’t be used by any other authentication method assigned to the web application by default. |

### 2. Connect `SPTrustedIdentityTokenIssuer` with `SPClaimProvider`

In this step, the OIDC `SPTrustedIdentityTokenIssuer` uses the claim provider created in [step 1](#1-create-a-new-claim-provider) for searching and resolving users and groups:

  ```powershell
  Set-SPTrustedIdentityTokenIssuer <token issuer name> -ClaimProvider <claim provider object> -IsOpenIDConnect
  ```

Specify the following parameters:

| Parameter | Description |
|------------|-------------|
| token issuer name | The token issuer this People Picker will use. |
| -ClaimProvider | The `SPClaimProvider`, which will be used to generate claim. |
| -IsOpenIDConnect | Required when `SPTrustedIdentityTokenIssuer` is OIDC `SPTrustedIdentityTokenIssuer`. Without this parameter, OIDC `SPTrustedIdentityTokenIssuer` configuration will fail. |

An example of this command is:

  ```powershell
  $claimprovider = Get-SPClaimProvider -Identity "UPATest"
  Set-SPTrustedIdentityTokenIssuer "ADFS Provider" -ClaimProvider $claimprovider -IsOpenIDConnect
  ```

### 3. Synchronize profiles to user profile service application (UPSA)

Now, customers can start to synchronize profiles into the SharePoint UPSA from the identity provider used in the organization so that the newly created claim provider can work on the correct data set.

There are two ways to synchronize user profiles into the SharePoint UPSA:

- Create a new SharePoint Active Directory Import (AD Import) connection with **Trusted Claims Provider Authentication** as the **Authentication Provider Type** in the connection setting. To utilize AD Import, see [Manage user profile synchronization in SharePoint Server](/sharepoint/administration/manage-profile-synchronization).

    :::image type="content" source="../media/add-new-sync-connection-2.png" alt-text="Add New Synchronization Connections":::

- Use Microsoft Identity Manager (MIM). To utilize MIM, see [Microsoft Identity Manager in SharePoint Servers 2016 and 2019](/sharepoint/administration/microsoft-identity-manager-in-sharepoint-server-2016).
  - There should be two agents inside the MIM Synchronization Service Manager UX after MIM is set up. One agent is used to import user profiles from the source IDP to the MIM database. The other agent is used to export user profiles from the MIM database to the SharePoint UPSA.

During the synchronization, the following three properties must be provided to the UPSA:

- `SPS-ClaimID`
- `SPS-ClaimProviderID`
- `SPS-ClaimProviderType`

    1. `SPS-ClaimID`

        During the synchronization, you must pick which unique identity property in the source will be mapped to the `SPS-ClaimID` property in the UPSA. We suggest using **Email** or **User Principal Name** for the `SPS-ClaimID`. The corresponding **IdentifierClaim** value needs to be set when token issuer is created from the [New-SPTrustedIdentityTokenIssuer](/powershell/module/sharepoint-server/new-sptrustedidentitytokenissuer) cmdlet.

        For AD Import synchronization, **Central Administration > Application Management > Manage service applications > User Profile Service Application > Manage User Properties** will allow administrators to edit the `SPS-ClaimID` to indicate which property in the source identity provider should be synchronized to `SPS-ClaimID`. (The display name of this property is **Claim User Identifier** and it can be customized to other display names by the administrator.) For example, if email is to be used as the `SPS-ClaimID`, **Claim User Identifier** should be set to **Email**.

        :::image type="content" source="../media/SPS-ClaimID-1.png" alt-text="SPS-ClaimID":::
        :::image type="content" source="../media/SPS-ClaimID-2.png" alt-text="SPS-ClaimProviderID":::
        :::image type="content" source="../media/SPS-ClaimID-3.png" alt-text="SPS-ClaimProviderType":::

        MIM synchronization is done by mapping **Email** or **User Principal Name** to `SPS-ClaimID` in the MIM database to the SharePoint UPSA agent:
        - In the MIM Synchronization Service Manager, select the agent and open the **Configure Attribute Flow**. You can map **mail** to `SPS-ClaimID`.

            :::image type="content" source="../media/SPS-ClaimID-4.png" alt-text="SPS-ClaimID4":::

    2. `SPS-ClaimProviderID` and `SPS-ClaimProviderType`

        For AD Import synchronization, these properties can be modified in **User Profile Service Application > Configure Synchronization Connections > Create New Connection** when you create a new AD Import synchronization connection.

        - `SPS-ClaimProviderID` should be set to the provider name created in [step 1](#1-create-a-new-claim-provider) by the `New-SPClaimProvider` cmdlet.
        - `SPS-ClaimProviderType` should be set to `SPTrustedBackedByUPAClaimProvider`.

        For MIM synchronization, these properties can be set in the **Configure Attribute Flow** for the MIM database to SharePoint UPSA agent:

        - `SPS-ClaimProviderType` should be set to **Trusted** as Constant type.
        - `SPS-ClaimProviderID` should be set to the provider name created in [step 1](#1-create-a-new-claim-provider) by the `New-SPClaimProvider` cmdlet.

        :::image type="content" source="../media/configure-attribute-flow-2.png" alt-text="Configure Attribute Flow":::

### 4. Make groups searchable

Perform the following steps to enable the People Picker control to work with groups:

1. Group object must have a property named `SID` of type `groupid` in the identity provider.

    You can create a `ClaimTypeMapping` object by using [New-SPClaimTypeMapping](/powershell/module/sharepoint-server/new-spclaimtypemapping) and then provide this object to [New-SPTrustedIdentityTokenIssuer](/powershell/module/sharepoint-server/new-sptrustedidentitytokenissuer) cmdlet with `-ClaimsMappings` parameter.

    ```powershell
    $sidClaimMap = New-SPClaimTypeMapping -IncomingClaimType "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid" -IncomingClaimTypeDisplayName "SID" -SameAsIncoming 
    $tokenissuer = New-SPTrustedIdentityTokenIssuer -ClaimsMappings $sidClaimMap, $emailClaimMap
    ```

    This sample cmdlet first creates a `claimmap` object of type `groupsid` and indicates that it works with the `SID` property of the group and then creates a new identity issuer, which can understand this mapping.

2. Synchronize `SID` property of groups from the identity provider to the `SID` property in UPSA.
    1. For AD Import synchronization, `SID` will be synchronized automatically without additional setup from the source identity provider to the SharePoint UPSA.
    2. For MIM synchronization, the property mapping needs to be taken from the identity provider to MIM and then from MIM to the SharePoint UPSA so that MIM can synchronize the group `SID` from the identity provider to the SharePoint UPSA. This is similar to how we do user profile synchronization for the `SPS-ClaimID` property for user profiles.

3. For MIM synchronization, `sAMAccountName` should also be mapped to `accountName` from MIM to the SharePoint UPSA. If it doesn’t exist, admin should create mapping pair from `sAMAccountName` to `accountName` in MIM manually.

### 5. Enable fields being searchable in UPSA

To make People Picker work, the final step is to enable fields to be searchable in UPSA.

Users can set which properties are searched by the People Picker by following this sample PowerShell script:

  ```powershell
  #Get the property list of UPSA connected with the web application 
  $site = $(Get-SPWebApplication $WebApplicationName).Sites[0] 
  $context= Get-SPServiceContext $site 
  $psm = [Microsoft.Office.Server.UserProfiles.ProfileSubTypeManager]::Get($context) 
  $ps = 
  $psm.GetProfileSubtype([Microsoft.Office.Server.UserProfiles.ProfileSubtypeManager]::GetDefaultProfileName([Microsoft.Office.Server.UserProfiles.ProfileType]::User)) 
  $properties = $ps.Properties

  #Enable people picker search for property name 'FistName', 'LastName' and 'SPS-ClaimID' 
  $PropertyNames = 'FirstName', 'LastName', 'SPS-ClaimID'
  foreach ($p in $PropertyNames) { 
      $property = $properties.GetPropertyByName($p) 
      if ($property) { 
          $property.CoreProperty.IsPeoplePickerSearchable = $true 
          $property.CoreProperty.Commit() 
          $property.Commit() 
      } 
  } 
  ```
