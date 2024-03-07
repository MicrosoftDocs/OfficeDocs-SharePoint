---
ms.date: 07/11/2021
title: "Set up OIDC authentication in SharePoint Server with Microsoft Entra ID"
ms.reviewer: 
ms.author: serdars
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
description: "Learn how to set up OIDC authentication in SharePoint Server with Microsoft Entra ID."
---

# Set up OIDC authentication in SharePoint Server with Microsoft Entra ID

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

## Prerequisites

When you configure OpenID Connect (OIDC) with Microsoft Entra ID, you need the following resources:

1. A SharePoint Server Subscription Edition farm
2. Microsoft Entra Global Administrator role of the M365 tenant

This article uses the following example values for Microsoft Entra OIDC setup:

| Value | Link |
|---------|---------|
| SharePoint site Uniform Resource Locator (URL) | `https://spsites.contoso.local/` |
| OIDC site URL     | `https://sts.windows.net/<tenantid>/` |
| Microsoft Entra OIDC authentication endpoint     | `https://login.microsoftonline.com/<tenantid>/oauth2/authorize` |
| Microsoft Entra OIDC RegisteredIssuerName URL     | `https://sts.windows.net/<tenantid>/` |
| Microsoft Entra OIDC SignoutURL     | `https://login.microsoftonline.com/<tenantid>/oauth2/logout` |
| Identity claim type     | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| Windows site collection administrator     | contoso\yvand |
| Email value of the federated site collection administrator   | yvand@contoso.local |

## Step 1: Setup identity provider

Perform the following steps to set up OIDC with Microsoft Entra ID:

1. Browse to the [Entra ID admin portal](https://entra.microsoft.com/), and sign in with an account with the Global Administrator role.
1. Under Applications, select App Registrations.
1. Select **New Registration**.
2. Go to the **Register an application** page `https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps`.
1. Under the **Redirect URI** section, choose "Web" as the Platform, and enter your SharePoint Server web application URL, for example: `https://spsites.contoso.local/` and select **Register**.

    :::image type="content" source="../media/register-an-app.PNG" alt-text="Register an application":::

1. Save the **Directory (tenant) ID** value, as the tenant ID is used in subsequent steps. Also save the **Application (client) ID,** which we use as **DefaultClientIdentifier** in the SharePoint setup.

    :::image type="content" source="../media/sharepoint-onprem-oidc-connection.png" alt-text="Save Application":::

1. After you register the application, go to the **Authentication** tab, select the **ID tokens** check box, and select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-authentication.png" alt-text="Enable ID Tokens":::

1. Go to the **API permissions** tab and select Add a Permission. Choose **Microsoft Graph**, then **Delegated permissions.**  Select the add **email** and **profile** permissions, and select **Add permissions.**

    :::image type="content" source="../media/sharepoint-oidc-api-permissions.png" alt-text="API Permissions":::
   
1. Go to the **Token configuration** tab and select **Add optional claim**. For each token type (ID, Access, SAML), add **email**, and **upn** claims.

1. Also on the **Token configuration** tab, select **Add groups claim**. Security Groups is the most common, but the group types you select depends on which types of groups you want to use to give access to the SharePoint web application. For more information, see [Configure groups optional claims](/entra/identity-platform/optional-claims#configure-groups-optional-claims) and Configure group claims for applications by using Microsoft Entra ID.
:::image type="content" source="../media/sharepoint-oidc-token-configuration.png" alt-text="Token Configuration":::

8. Go to the **Manifest** tab, and manually change **replyUrlsWithType** from `https://spsites.contoso.local/` to `https://spsites.contoso.local/*`. Then select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-manifest.png" alt-text="Manifest":::

9. Get OIDC authentication information from OIDC discovery endpoint.

In Microsoft Entra ID, there are two versions of OIDC authentication endpoints. Therefore, there are two versions of OIDC discovery endpoints respectively:

- V1.0: `https://login.microsoftonline.com/<TenantID>/.well-known/openid-configuration`
- V2.0: `https://login.microsoftonline.com/<TenantID>/v2.0/.well-known/openid-configuration`

> [!NOTE]
> When using OIDC authentication with SharePoint Server, currently only the V1.0 endpoint is supported.
Replace TenantID with the **Directory (tenant) ID** saved in the third step mentioned previously and connect to the endpoint through your browser. Then, save the following information:

| Value | Link |
|---------|---------|
| authorization_endpoint | `https://login.microsoftonline.com/<tenantid>/oauth2/authorize` |
| end_session_endpoint   | `https://login.microsoftonline.com/<tenantid>/oauth2/logout` |
| issuer     | `https://sts.windows.net/<tenantid>/` |
| jwks_uri     | `https://login.microsoftonline.com/common/discovery/keys` |

Open jwks_uri (`https://login.microsoftonline.com/common/discovery/keys`) and save all the **x5c** certificate strings for later use in SharePoint setup.

:::image type="content" source="../media/sharepoint-setup-keys.png" alt-text="Discovery keys":::

## Step 2: Change SharePoint farm properties

In this step, you need to modify the SharePoint Server farm properties based on the version of your SharePoint Server.

> [!Note]
> Start the SharePoint Management Shell as a farm Administrator to run the following script. Read the instructions mentioned in the following PowerShell script carefully, and you will need to enter your own environment-specific values in certain places.

- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version 24H1, see [Configure SPSE Version 24H1 or higher version](#configure-sharepoint-server-subscription-edition-version-24h1-or-higher-versions).
- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version preceding 24H1, see [Configure SPSE prior to Version 24H1](#configure-sharepoint-server-subscription-edition-prior-to-version-24h1).

### Configure SharePoint Server Subscription Edition Version 24H1 or higher versions

Starting with SharePoint Server Subscription Edition Version 24H1, you can configure SharePoint Server farm properties by employing SharePoint Certificate Management to manage the nonce cookie certificate. The nonce cookie certificate is part of the infrastructure to ensure OIDC authentication tokens are secure. Run the following script to configure:

```powershell
# Setup farm properties to work with OIDC

# Create the Nonce certificate
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"

#Import certificate to Certificate Management
$certPath = <path to save the exported cert>
$certPassword = ConvertTo-SecureString -String <password> -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath $certPath -Password $certPassword
$nonceCert = Import-SPCertificate -Path $certPath -Password $certPassword -Store "EndEntity" -Exportable:$true

$farm = Get-SPFarm 
$farm.UpdateNonceCertificate($nonceCert,$true)
```

### Configure SharePoint Server Subscription Edition prior to Version 24H1

```powershell
# Setup farm properties to work with OIDC
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"
$rsaCert = [System.Security.Cryptography.X509Certificates.RSACertificateExtensions]::GetRSAPrivateKey($cert)
$fileName = $rsaCert.key.UniqueName

#if you have multiple SharePoint servers in the farm, you need to export certificate by Export-PfxCertificate and import certificate to all other SharePoint servers in the farm by Import-PfxCertificate. 

#After certificate is successfully imported to SharePoint Server, we will need to grant access permission to certificate private key.

$path = "$env:ALLUSERSPROFILE\Microsoft\Crypto\RSA\MachineKeys\$fileName"
$permissions = Get-Acl -Path $path

#Replace the <web application pool account> with real application pool account of your web application
$access_rule = New-Object System.Security.AccessControl.FileSystemAccessRule(<Web application pool account>, 'Read', 'None', 'None', 'Allow')
$permissions.AddAccessRule($access_rule)
Set-Acl -Path $path -AclObject $permissions

#Then we update farm properties
$farm = Get-SPFarm
$farm.Properties['SP-NonceCookieCertificateThumbprint']=$cert.Thumbprint
$farm.Properties['SP-NonceCookieHMACSecretKey']='seed'
$farm.Update()
```

## Step 3: Configure SharePoint to trust the identity provider

You can configure SharePoint to trust the identity provider in either of the following ways:

- Configure SharePoint to trust Microsoft Entra ID as the OIDC provider **manually**.
- Configure SharePoint to trust Microsoft Entra ID as the OIDC provider by using the **metadata endpoint**.
  - By using the metadata endpoint, several parameters you need in 'Configure SharePoint to trust Microsoft Entra ID as the OIDC provider manually' is automatically retrieved by metadata endpoint.

> [!NOTE]
> Follow either the manual configuration steps or the metadata endpoint steps, but not both.

### Configure SharePoint to trust Microsoft Entra ID as the OIDC provider manually

In this step, you create a `SPTrustedTokenIssuer` that stores the configuration that SharePoint needs to trust Microsoft Entra OIDC as the OIDC provider. Start the SharePoint Management Shell as a farm Administrator, and run the following script to create it:

> [!NOTE]
> Read the instructions mentioned in the following PowerShell script carefully. You will need to enter your own environment-specific values in certain places.  For example, replace \<tenantid\> with your own Directory (tenant) ID.
```powershell
# Define claim types
# In this example, we're using Email Address as the identity claim.
$emailClaimMap = New-SPClaimTypeMapping -IncomingClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "Email" -SameAsIncoming

# Public key of the AAD OIDC signing certificate. Please replace <x5c cert string> with the encoded cert string which you get from x5c certificate string of the keys of jwks_uri from Step #1
$encodedCertStrs = @()
$encodedCertStrs += <x5c cert string 1>
$encodedCertStrs += <x5c cert string 2>
...
$certificates = @()
foreach ($encodedCertStr in $encodedCertStrs) {
     $certificates += New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 @(,[System.Convert]::FromBase64String($encodedCertStr))
}

# Set the AAD OIDC URL where users are redirected to authenticate. Please replace <tenantid> accordingly
$authendpointurl = "https://login.microsoftonline.com/<tenantid>/oauth2/authorize"
$registeredissuernameurl = "https://sts.windows.net/<tenantid>/"
$signouturl = "https://login.microsoftonline.com/<tenantid>/oauth2/logout"

# Please replace <Application (Client) ID> with the value saved in step #3 in AAD setup section
$clientIdentifier = "<Application (Client)ID>"

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "contoso.local" -Description "contoso.local" -ImportTrustCertificate $certificates -ClaimsMappings emailClaimMap -IdentifierClaim $emailClaimMap.InputClaimType -RegisteredIssuerName $registeredissuernameurl -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -DefaultClientIdentifier $clientIdentifier -Scope "openid profile"
```

Here, `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is extended to support OIDC by using the following parameters:

| Parameter | Description |
|------------|-------------|
|Name     | Gives a name to the new token issuer. |
|Description     | Gives a description to the new token issuer. |
|ImportTrustCertificate     | Imports a list of X509 Certificates, which is used to validate `id_token` from OIDC identifier. If the OIDC identity provider (IDP) uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint validates `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A `SPClaimTypeMapping` object, which is used to identify which claim in the `id_token` is regarded as identifier in SharePoint. |
| IdentifierClaim | Specifies the type of identifier. |
| RegisteredIssuerName | Specifies the issuer identifier, which issues the `id_token`. It's used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifies the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifies the sign out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specifies the `client_id` of SharePoint server, which is assigned by OIDC identity provider. This is validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specifies the response type of IDP, which is accepted by this token issuer. It can accept two strings: `id_token` and `code id_token`. If this parameter isn't provided, it uses `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store:
>
> `New-SPTrustedRootAuthority -Name "AAD OIDC signing root authority" -Certificate $signingCert`

<a name='configure-sharepoint-to-trust-azure-ad-oidc-by-using-metadata-endpoint'></a>

### Configure SharePoint to trust Microsoft Entra OIDC by using metadata endpoint

SharePoint Server Subscription Edition now supports OIDC metadata discovery capability during configuration.

When you use the metadata endpoint provided by the OIDC identity provider, some of the configuration is retrieved from the OIDC provider metadata endpoint directly, including:

1. Certificate
2. Issuer
3. Authorization Endpoint
4. SignoutURL

This can simplify the configuration of the OIDC token issuer.

With the following PowerShell example, we can use metadata endpoint from Microsoft Entra ID to configure SharePoint to trust Microsoft Entra OIDC.

> [!NOTE]
> Read the instructions mentioned in the following PowerShell script carefully. You will need to enter your own environment-specific values in certain places.  For example, replace \<tenantid\> with your own Directory (tenant) ID.
```powershell
# Define claim types
# In this example, we're using Email Address as the Identity claim.
$emailClaimMap = New-SPClaimTypeMapping -IncomingClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "Email" -SameAsIncoming

# Set the AAD metadata endpoint URL. Please replace <TenantID> with the value saved in step #3 in the Entra ID setup section  
$metadataendpointurl = "https://login.microsoftonline.com/<TenantID>/.well-known/openid-configuration"

# Please replace <Application (Client) ID> with the value saved in step #3 in the Entra ID setup section
$clientIdentifier = "<Application (Client)ID>"

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "contoso.local" -Description "contoso.local" -ClaimsMappings $emailClaimMap -IdentifierClaim $emailClaimMap.InputClaimType -DefaultClientIdentifier $clientIdentifier -MetadataEndPoint $metadataendpointurl -Scope "openid profile"
```

| Parameter | Description |
|------------|-------------|
|Name     | Gives a name to the new token issuer. |
|Description     | Gives a description to the new token issuer. |
|ImportTrustCertificate     | A certificate that is used to validate `id_token` from OIDC identifier. |
| ClaimsMappings | A `SPClaimTypeMapping` object, which is used to identify which claim in the `id_token` is regarded as identifier in SharePoint. |
| IdentifierClaim | Specifies the type of identifier. |
| DefaultClientIdentifier | Specifies the `client_id` of SharePoint server, which is assigned by OIDC identity provider. This is validated against aud claim in `id_token`. |
| MetadataEndPoint | Specifies the well-known metadata endpoint from OIDC identity provider, which can be used to retrieve latest certificate, issuer, authorization endpoint, and sign out endpoint. |

## Step 4: Configure the SharePoint web application

In this step, you configure a web application in SharePoint to be federated with the Microsoft Entra OIDC, using the `SPTrustedIdentityTokenIssuer` created in the previous step.

> [!IMPORTANT]
>
> - The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler. 
> - The SharePoint URL that will use Microsoft Entra OIDC federation must be configured with Hypertext Transfer Protocol Secure (HTTPS).

You can complete this configuration either by:

- Creating a new web application and using both Windows and Microsoft Entra OIDC authentication in the default zone.
- Extending an existing web application to set Microsoft Entra OIDC authentication on a new zone.

To create a new web application, do the following:

1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

      ```powershell
      # This script creates a trusted authentication provider for OIDC
      
      $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
      $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
      ```

  2. Follow [Create a web application in SharePoint Server](../administration/create-a-web-application.md) to create a new web application enabling HTTPS/Secure Sockets Layer (SSL) named SharePoint - OIDC on contoso.local.
  3. Open the SharePoint Central Administration site.
  4. Open the web application you created and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers.jpg" alt-text="Authentication Providers":::

  5. In the SharePoint Central Administration site, navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.

  6. Filter the display with the new web application and confirm that you see the following information:

      :::image type="content" source="../media/new-web-application.png" alt-text="New web application":::

To extend an existing web application, do the following:

1. Start the SharePoint Management Shell and run the following script:

      ```powershell
      # This script creates a trusted authentication provider for OIDC
  
      $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
      $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
      ```

  2. Open the SharePoint Central Administration site.
  3. Open the web application you want to extend OIDC authentication to and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers-2.jpg" alt-text="Authentication Providers 2":::

  4. In the SharePoint Central Administration site, navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
  5. Filter the display with the web application that was extended and confirm that you see the following information:

      :::image type="content" source="../media/sharepoint-administration-site.png" alt-text="SharePoint Administration Site":::

## Step 5: Ensure the web application is configured with SSL certificate

Since OIDC 1.0 authentication can only work with HTTPS protocol, a certificate must be set on the corresponding web application. Perform the following steps to set the certificate:

1. Generate the site certificate:

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

2. Set the certificate:

    You can use the following PowerShell cmdlet to assign the certificate to the web application:

    ```powershell
    Set-SPWebApplication -Identity https://spsites.contoso.local -Zone Default -SecureSocketsLayer -Certificate "Contoso SharePoint (2021)"
    ```

## Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (Microsoft Entra ID) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections** > **Create site collections**.
3. Type a title, URL, and select the template Team Site.
4. In the **Primary Site Collection Administrator** section, select the :::image type="content" source="../media/Book-icon.png" alt-text="Book Icon People Picker"::: (book) icon to open the People Picker dialog.
5. In the People Picker dialog, type the Windows administrator account, for example **yvand**.
6. Filter the list on the left by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people.png" alt-text="Select people":::

7. Go to the account and select **OK**.
8. In the **Secondary Site Collection Administrator** section, select the book icon to open the People Picker dialog.
9. In the People Picker dialog, type the exact email value of the Microsoft Entra administrator account, for example **yvand@contoso.local**.
10. Filter the list on the left by selecting **contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-2.png" alt-text="Select people 2":::

11. Go to the account and select **OK** to close the People Picker dialog.
12. Select **OK** again to create the site collection.

Once the site collection is created, you're able to sign-in using either the Windows or the federated site collection administrator account.

## Step 7: Set up People Picker

In OIDC authentication, the People Picker doesn't validate the input, which can lead to misspellings or users accidentally selecting the wrong claim type. This can be addressed using the new UPA-backed claim provider in SharePoint Server.

To do this, perform the following steps:

### 1. Create a new claim provider

In the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-provider), you already created an OIDC `SPTrustedIdentityTokenIssuer` by using `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet. In this step, you use the following PowerShell cmdlet to create a claim provider, which uses the User Profile Application service to search and resolve users and groups in the People Picker and specifies to use the OIDC `SPTrustedIdentityTokenIssuer`:

  ```powershell
  $claimprovider = New-SPClaimProvider -AssemblyName "Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c" -DisplayName 'OIDC Claim Provider' -Type "Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider" -TrustedTokenIssuer $tokenissuer -Description “OIDC Claim Provider” -Default:$false
  ```

Specify the following parameters:

| Parameter | Description |
|------------|-------------|
| AssemblyName | To be specified as `Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c`. |
| Type | To be specified as `Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider` so that this command creates a claim provider, which uses UPA as the claim source. |
| TrustedTokenIssuer | To be specified as the OIDC `SPTrustedIdentityTokenIssuer` created in the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-provider), which uses this claim provider. This is a new parameter the user needs to provide when the type of the claim provider is `Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider`. |
| Default | As we create a claim provider by using this cmdlet, this cmdlet can only work with `SPTrustedIdentityTokenIssuer` and `Default` parameter must be set to false so that it zDFTRG5YU6HJIKL6;IOP{"
} any other authentication method assigned to the web application by default. |

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
| -IsOpenIDConnect | Required when `SPTrustedIdentityTokenIssuer` is OIDC `SPTrustedIdentityTokenIssuer`. Without this parameter, OIDC `SPTrustedIdentityTokenIssuer` configuration fails. |

An example of this command is:

  ```powershell
  $claimprovider = Get-SPClaimProvider -Identity "UPATest"
  Set-SPTrustedIdentityTokenIssuer "ADFS Provider" -ClaimProvider $claimprovider -IsOpenIDConnect
  ```

?
#., ## 3. Synchronize profiles to user profile service application

Now, customers can start to synchronize profiles into the SharePoint user profile service application (UPSA) from the identity provider used in the organization so that the newly created claim provider can work on the correct data set.

There are two ways to synchronize user profiles into the SharePoint UPSA:

- Create a new SharePoint Active Directory Import (AD Import) connection with **Trusted Claims Provider Authentication** as the **Authentication Provider Type** in the connection setting. To utilize AD Import, see [Manage user profile synchronization in SharePoint Server](../administration/manage-profile-synchronization.md).

    :::image type="content" source="../media/add-new-sync-connection-2.png" alt-text="Add New Synchronization Connections":::

- Use Microsoft Identity Manager (MIM). To utilize MIM, see [Microsoft Identity Manager in SharePoint Servers 2016 and 2019](../administration/microsoft-identity-manager-in-sharepoint-server.md).
  - There should be two agents inside the MIM Synchronization Service Manager UX after MIM is set up. One agent is used to import user profiles from the source IDP to the MIM database. The other agent is used to export user profiles from the MIM database to the SharePoint UPSA.

During the synchronization, the following three properties must be provided to the UPSA:

- `SPS-ClaimID`
- `SPS-ClaimProviderID`
- `SPS-ClaimProviderType`

    1. `SPS-ClaimID`

        During the synchronization, you must pick which unique identity property in the source is mapped to the `SPS-ClaimID` property in the UPSA. We suggest using **Email** or **User Principal Name** for the `SPS-ClaimID`. The corresponding **IdentifierClaim** value needs to be set when token issuer is created from the [New-SPTrustedIdentityTokenIssuer](/powershell/module/sharepoint-server/new-sptrustedidentitytokenissuer) cmdlet.

        For AD Import synchronization, **Central Administration > Application Management > Manage service applications > User Profile Service Application > Manage User Properties** allows administrators to edit the `SPS-ClaimID` to indicate which property in the source identity provider should be synchronized to `SPS-ClaimID`. (The display name of this property is **Claim User Identifier** and it can be customized to other display names by the administrator.) For example, if email is to be used as the `SPS-ClaimID`, **Claim User Identifier** should be set to **Email**.

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
    1. For AD Import synchronization, `SID` is synchronized automatically without other setup from the source identity provider to the SharePoint UPSA.
    2. For MIM synchronization, the property mapping needs to be taken from the identity provider to MIM and then from MIM to the SharePoint UPSA so that MIM can synchronize the group `SID` from the identity provider to the SharePoint UPSA. This is similar to how we do user profile synchronization for the `SPS-ClaimID` property for user profiles.

1. For MIM synchronization, `sAMAccountName` should also be mapped to `accountName` from MIM to the SharePoint UPSA. If it doesn’t exist, admin should create mapping pair from `sAMAccountName` to `accountName` in MIM manually.

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
