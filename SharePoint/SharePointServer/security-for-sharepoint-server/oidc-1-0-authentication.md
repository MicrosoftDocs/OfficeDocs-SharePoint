---
title: "OpenID Connect 1.0 authentication"
ms.reviewer: 
ms.author: v-jmathew
author: jitinmathew
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to setup OIDC authentication in SharePoint Server."
---

# OpenID Connect 1.0 authentication

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

SharePoint Server Subscription Edition now supports OpenID Connect (OIDC) 1.0 authentication protocol. OIDC 1.0 is a modern authentication protocol that makes it easy to integrate applications and devices with your organization's identity and authentication management solutions to better meet your evolving security and compliance needs.

In SharePoint 2019 and prior versions, SharePoint Server supported three types of authentication methods:

1. Windows authentication (NTLM, Kerberos, etc.)
2. Forms-based authentication
3. SAML 1.1-based authentication

With this new capability, you can now set up an OIDC-enabled `SPTrustedIdentityTokenIssuer` that works with a remote identity provider to enable OIDC authentication.

## Setup OIDC authentication in SharePoint Server with AAD

### Prerequisites

To perform the configuration, you need the following resources when you configure with Azure Active Directory (AAD) OIDC:

1. A SharePoint Server Subscription Edition farm
2. AAD Global Administrator role of the M365 tenant

This article uses the following values for AAD OIDC setup:

| Value | Link |
|---------|---------|
| SharePoint site URL | `https://spsites.contoso.local/` |
| OIDC site URL     | `https://sts.windows.net/<tenantid>/` |
| AAD OIDC authentication endpoint     | `https://login.microsoftonline.com/<tenantid>/oauth2/authorize` |
| AAD OIDC RegisteredIssuerName URL     | `https://sts.windows.net/<tenantid>/` |
| AAD OIDC SignOut URL     | `https://login.microsoftonline.com/<tenantid>/oauth2/logout` |
| Identity claim type     | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| Windows site collection administrator     | contoso\yvand |
| Email value of the federated (AD FS) site collection administrator     | yvand@contoso.local |

### Step 1: Setup Identity Provider

If you choose to use AAD as federated identity provider, perform the following steps to set up AAD OIDC:

1. Go to the **App Registration** page `https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps`.
2. Enter the following for Redirect URL: `https://spsites.contoso.local/` and select **Register**.

    :::image type="content" source="../media/register-an-app.PNG" alt-text="Register an application":::

3. Save **Directory (tenant) ID** as the tenant ID we will use in the future and save **Application (client) ID** which will be used as **DefaultClientIdentifier** in SharePoint setup.

    :::image type="content" source="../media/sharepoint-onprem-oidc-connection.png" alt-text="Save Application":::

4. After registering, go to the **Authentication** tab and enable **ID tokens**, then select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-authentication.png" alt-text="Enable ID Tokens":::

5. Go to the **API permissions** tab and add **email** and **profile** permissions.

    :::image type="content" source="../media/sharepoint-oidc-api-permissions.png" alt-text="API Permissions":::

6. Go to the **Token configuration** tab and add **email**, **groups** and **upn** optional claims.

    :::image type="content" source="../media/sharepoint-oidc-token-configuration.png" alt-text="Token Configuration":::

7. Go to the **Manifest** tab, and manually change **replyUrlsWithType.url** from `https://spsites.contoso.local/` to `https://spsites.contoso.local/*`. Then select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-manifest.png" alt-text="Manifest":::

8. Get OIDC authentication information from OIDC discovery endpoint.

In AAD, there are two versions of OIDC authentication endpoints. Therefore, there are two versions of OIDC discovery endpoints, respectively:

- V1.0: `https://login.microsoftonline.com/<TenantID>/.well-known/openid-configuration`
- V2.0: `https://login.microsoftonline.com/<TenantID>/v2.0/.well-known/openid-configuration`

> [!NOTE]
> For OIDC authentication, both endpoints are supported but we recommend using V2.0.

Replace TenantID with the **Directory (tenant) ID** saved in the third step mentioned above and connect to the endpoint through your browser. Then, save the following information:

| Value | Link |
|---------|---------|
| authorization_endpoint | `https://login.microsoftonline.com/<tenantid>/oauth2/authorize` |
| end_session_endpoint   | `https://login.microsoftonline.com/<tenantid>/oauth2/logout` |
| issuer     | `https://sts.windows.net/<tenantid>/` |
| jwks_uri     | `https://login.microsoftonline.com/common/discovery/keys` |

Open jwks_uri (`https://login.microsoftonline.com/common/discovery/keys`), and save the **x5c** certificate string of the first key for later use in SharePoint setup (if the first key doesn’t work, try the second or third key).

:::image type="content" source="../media/sharepoint-setup-keys.png" alt-text="Discovery keys":::

### Step 2: Change SharePoint Farm properties

In this step, you will need to modify farm properties. Start the SharePoint Management Shell and run the following script:

```powershell
# Setup farm properties to work with OIDC
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"
$rsaCert = [System.Security.Cryptography.X509Certificates.RSACertificateExtensions]::GetRSAPrivateKey($cert)
$fileName = $rsaCert.key.UniqueName

#if you have multiple SharePoint servers in the farm, you need to export certificate by Export-PfxCertificate and import certificate to all other SharePoint servers in the farm by Import-PfxCertificate. 

#After certificate is successfully imported to SharePoint Server, we will need to grant access permission to certificate private key.

$path = "$env:ALLUSERSPROFILE\Microsoft\Crypto\RSA\MachineKeys\$fileName"
$permissions = Get-Acl -Path $path

#Please replace the <web application pool account> with real application pool account of your web application
$access_rule = New-Object System.Security.AccessControl.FileSystemAccessRule(<Web application pool account>, 'Read', 'None', 'None', 'Allow')
$permissions.AddAccessRule($access_rule)
Set-Acl -Path $path -AclObject $permissions

#Then we update farm properties
$f = Get-SPFarm
$f.Farm.Properties['SP-NonceCookieCertificateThumbprint']=$cert.Thumbprint
$f.Farm.Properties['SP-NonceCookieHMACSecretKey']='seed'
$f.Farm.Update()
```

### Step 3: Configure SharePoint to trust the Identity Provider

You can configure SharePoint to trust the Identity provider in the following two ways:

- Configure SharePoint to trust AAD as the OIDC provider manually
- Configure SharePoint to trust AAD as the OIDC provider by using metadata endpoint
  - By using metadata endpoint, a lot of parameters you need in 'Configure SharePoint to trust AAD as the OIDC provider manually' can be automatically retrieved by metadata endpoint.

#### Configure SharePoint to trust AAD as the OIDC provider manually

In this step, you create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AAD OIDC as the OIDC provider. Start the SharePoint Management Shell and run the following script to create it:

> [!NOTE]
> Be sure to follow the instructions mentioned in the following PowerShell script.

```powershell
# Define claim types
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

# Public key of the AAD OIDC signing certificate. Please replace <x5c cert string> with the encoded cert string which you get from x5c certificate string of the keys of jwks_uri from Step #1
$encodedCertStr = <x5c cert string>
$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 @(,[System.Convert]::FromBase64String($encodedCertStr))
# Set the AAD OIDC URL where users are redirected to authenticate. Please replace <tenantid> accordingly
$authendpointurl = "https://login.microsoftonline.com/<tenantid>/oauth2/authorize"
$registeredissuernameurl = " https://sts.windows.net/<tenantid>/"
$signouturl = " https://login.microsoftonline.com/<tenantid>/oauth2/logout"

# Please replace <Application (Client) ID> with the value saved in step #3 in AAD setup section
$clientIdentifier = <Application (Client)ID>

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "contoso.local" -Description "contoso.local" -ImportTrustCertificate $signingCert -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -RegisteredIssuerName $registeredissuernameurl  -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -DefaultClientIdentifier $clientIdentifier
```

Here, `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is extended to support OIDC by using the following parameters:

| Parameter | Description |
|------------|-------------|
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ImportTrustCertificate     | It takes a list of X509 Certificates, which will be used to validate `id_token` from OIDC identifier. If the OIDC IDP uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint will then validate `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A `SPClaimTypeMapping` object, which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| RegisteredIssuerName | Specifying the issuer identifier, which issues the `id_token`. It will be used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifying the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifying the sign out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server, which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specify the response type of IDP which can be accepted by this token issuer. It can accept two strings, `id_token` and `code id_token`. If this parameter is not provided, it will use `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store:
>
> `New-SPTrustedRootAuthority -Name "AAD OIDC signing root authority" -Certificate $signingCert`

#### Configure SharePoint to trust AAD OIDC by using metadata endpoint

SharePoint Server Subscription Edition now supports OIDC metadata discovery capability during configuration.

By using the metadata endpoint provided from the OIDC identity provider, some of the configuration will be retrieved from the OIDC provider metadata endpoint directly, including:

1. Certificate
2. Issuer
3. Authorization Endpoint
4. SignoutURL

This can simplify the configuration of the OIDC token issuer.

By using the below PowerShell example, we can use metadata endpoint from AAD to configure SharePoint to trust AAD OIDC.

> [!NOTE]
> Be sure to follow the instructions mentioned in the following PowerShell script.

```powershell
# Define claim types
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

# Set the AAD metadata endpoint URL. Please replace <TenantID> with the value saved in step #3 in AAD setup section  
$metadataendpointurl = "https://login.microsoftonline.com/<TenantID>/.well-known/openid-configuration"

# Please replace <Application (Client) ID> with the value saved in step #3 in AAD setup section
$clientIdentifier = <Application (Client)ID>

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "contoso.local" -Description "contoso.local" -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -DefaultClientIdentifier $clientIdentifier -MetadataEndPoint $ metadataendpointurl
```

| Parameter | Description |
|------------|-------------|
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ImportTrustCertificate     | A certificate that will be used to validate `id_token` from OIDC identifier. |
| ClaimsMappings | A `SPClaimTypeMapping` object, which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server, which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| MetadataEndPoint | Specifying the well-known metadata endpoint from OIDC identity provider, which can be used to retrieve latest certificate, issuer, authorization endpoint, and sign out endpoint. |

### Step 4: Configure the SharePoint web application

In this step, you configure a web application in SharePoint to be federated with the AAD OIDC, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

The important rules to respect here are:

- The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler.
- The SharePoint URL that will use AAD OIDC federation must be configured with HTTPS.

There are two possible configurations:

- If you create a new web application and use both Windows and AAD OIDC authentication in the Default zone:

    1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

        ```powershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
        $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

    2. Follow [Create a web application in SharePoint Server](/sharepoint/administration/create-a-web-application) to create a new web application enabling HTTPS/SSL named SharePoint - OIDC on contoso.local.
    3. Open the SharePoint Central Administration site.
    4. Open the web application you just created and pick **contoso.local** as **Trusted Identity Provider**.

        :::image type="content" source="../media/authentication-providers.jpg" alt-text="Authentication Providers":::

    5. Open the SharePoint Central Administration site.
    6. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.

    7. Filter the display with the new web application and confirm that you see something like this:

        :::image type="content" source="../media/new-web-application.png" alt-text="New web application":::

- If you extend an existing web application to set AD FS/AAD OIDC authentication on a new zone:

    1. Start the SharePoint Management Shell and run the following script:

        ```powershell
        # This script creates a trusted authentication provider for OIDC
    
        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
        $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

    2. Open the SharePoint Central Administration site.
    3. Open the web application you want to extend OIDC authentication to and pick **contoso.local** as **Trusted Identity Provider**.

        :::image type="content" source="../media/authentication-providers-2.jpg" alt-text="Authentication Providers 2":::

    4. Open the SharePoint Central Administration site.
    5. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
    6. Filter the display with the web application that was extended and confirm that you see something like this:

        :::image type="content" source="../media/sharepoint-administration-site.png" alt-text="SharePoint Administration Site":::

### Step 5: Ensure web application is configured with SSL certificate

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

### Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (AAD) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections** > **Create site collections**.
3. Type a title, URL, and select the template Team Site.
4. In the Primary Site Collection Administrator section, click the :::image type="content" source="../media/Book-icon.png" alt-text="Book Icon People Picker"::: (book) icon to open the People Picker dialog.
5. In the People Picker dialog, type the Windows administrator account, for example **yvand**.
6. On the left, filter the list by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people.png" alt-text="Select people":::

7. Select the account and click **OK**.
8. In the Secondary Site Collection Administrator section, select the book icon to open the People Picker dialog.
9. In the People Picker dialog, type the exact email value of the AAD administrator account, for example **yvand@contoso.local**.
10. On the left, filter the list by selecting **contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-2.png" alt-text="Select people 2":::

11. Select the account and choose **OK** to close the People Picker dialog.
12. Select **OK** to create the site collection.

Once the site collection is created, you should be able to sign-in to it using either the Windows or the federated site collection administrator account.

### Step 7: Set up People Picker

In OIDC authentication the People Picker does not validate the input, which can lead to misspellings or users accidentally choosing the wrong claim type. This can be addressed using the new UPA backed claim provider in SharePoint Server.

To do this, perform the following steps:

#### 1. Create new claim provider

In the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-provider) you have already created an OIDC `SPTrustedIdentityTokenIssuer` by using `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet. In this step, you will create a claim provider which uses the User Profile Application service to search and resolve users and groups in the People Picker and specifies to use the OIDC `SPTrustedIdentityTokenIssuer`:

  ```powershell
  $claimprovider = New-SPClaimProvider -AssemblyName "Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c" -DisplayName 'OIDC Claim Provider' -Type "Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider" -TrustedTokenIssuer $tokenissuer -Description “OIDC Claim Provider” -Default:$false
  ```

There are three parameters that need to be specified here:

| Parameter | Description |
|------------|-------------|
| AssemblyName | To be specified as "Microsoft.SharePoint, Version=16.0.0.0, Culture=neutral, publicKeyToken=71e9bce111e9429c". |
| Type | To be specified as "Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider" so that this command creates a claim provider which uses UPA as the claim source. |
| TrustedTokenIssuer | To be specified as the OIDC `SPTrustedIdentityTokenIssuer` created in the [previous step](#step-3-configure-sharepoint-to-trust-the-identity-provider) which will use this claim provider. This is a new parameter the user needs to provide when the type of the claim provider is "Microsoft.SharePoint.Administration.Claims.SPTrustedBackedByUPAClaimProvider". |
| Default | As we have created a claim provider by using this cmdlet, this cmdlet can only work with SPTrustedIdentityTokenIssuer and “Default” parameter must be set to false so that it won’t be used by any other authentication method assigned to the web application by default. |

#### 2. Connect `SPTrustedIdentityTokenIssuer` with `SPClaimProvider`

In this step, the OIDC `SPTrustedIdentityTokenIssuer` uses the claim provider created in [step 1](#1-create-new-claim-provider) for searching and resolving users and groups:

  ```powershell
  Set-SPTrustedIdentityTokenIssuer <token issuer name> -ClaimProvider <claim provider object> -IsOpenIDConnect
  ```

The following parameters need to be specified here:

| Parameter | Description |
|------------|-------------|
| token issuer name | The token issuer this People Picker will use. |
| -ClaimProvider | The `SPClaimProvider` which will be used to generate claim. |
| -IsOpenIDConnect | Required when `SPTrustedIdentityTokenIssuer` is OIDC `SPTrustedIdentityTokenIssuer`. Without this parameter OIDC `SPTrustedIdentityTokenIssuer` configuration will fail. |

An example of this command is:

  ```powershell
  $claimprovider = Get-SPClaimProvider -Identity "UPATest"
  Set-SPTrustedIdentityTokenIssuer "ADFS Provider" -ClaimProvider $claimprovider -IsOpenIDConnect
  ```

#### 3. Synchronize profiles to UPSA

Now, customers can start to synchronize profiles into the SharePoint User Profile Application service from the identity provider used in the organization so that the newly created claim provider can work on the correct data set.

There are two ways to synchronize user profiles into the SharePoint User Profile Application service:

- By creating a new SharePoint Active Directory Import (AD Import) connection with **Trusted Claims Provider Authentication** as the **Authentication Provider Type** in the connection setting. To utilize AD Import, see [Manage user profile synchronization in SharePoint Server](/sharepoint/administration/manage-profile-synchronization).

    :::image type="content" source="../media/add-new-sync-connection-2.png" alt-text="Add New Synchronization Connections":::

- By using Microsoft Identity Manager (MIM). To utilize MIM, see [Microsoft Identity Manager in SharePoint Servers](../administration/microsoft-identity-manager-in-sharepoint-server.md#microsoft-identity-manager-in-sharepoint-server).
  - There should be two agents inside the MIM synchronization Manager UX after MIM is set up. One agent is used to import user profiles from the source IDP to the MIM database. The other agent is used to export user profiles from the MIM database to the SharePoint User Profile Application service.

During the synchronization, the following three properties need to be provided to the User Profile Application service:

- `SPS-ClaimID`
- `SPS-ClaimProviderID`
- `SPS-ClaimProviderType`

    1. `SPS-ClaimID`

        During the synchronization, you must pick which unique identity property in the source will be mapped to the `SPS-ClaimID` property in the User Profile Application service. We suggest using **Email** or **User Principal Name** for the `SPS-ClaimID`. The corresponding **IdentifierClaim** value needs to be set when token issuer is created from the [New-SPTrustedIdentityTokenIssuer](/powershell/module/sharepoint-server/new-sptrustedidentitytokenissuer) cmdlet.

        For AD Import synchronization, **Central Administration > Application Management > Manage service applications > User Profile Service Application > Manage User Properties** will allow administrators to edit the `SPS-ClaimID` to indicate which property in the source identity provider should be synchronized to `SPS-ClaimID`. (The display name of this property is **Claim User Identifier** in the UX, and it can be customized to other display names by the administrator.) For example, if email is to be used as the `SPS-ClaimID`, **Claim User Identifier** should be set to **Email**.

        :::image type="content" source="../media/SPS-ClaimID-1.png" alt-text="SPS-ClaimID":::
        :::image type="content" source="../media/SPS-ClaimID-2.png" alt-text="SPS-ClaimProviderID":::
        :::image type="content" source="../media/SPS-ClaimID-3.png" alt-text="SPS-ClaimProviderType":::

        MIM synchronization is done by mapping **Email** or **User Principal Name** to `SPS-ClaimID` in the MIM database to the SharePoint User Profile Application service agent:
        - In the MIM synchronization Service Manager, select the agent and open the **Configure Attribute Flow**. You can map **mail** to `SPS-ClaimID`.

            :::image type="content" source="../media/SPS-ClaimID-4.png" alt-text="SPS-ClaimID4":::

    2. `SPS-ClaimProviderID` and `SPS-ClaimProviderType`

        For AD Import synchronization, these properties can be modified in **User Profile Service Application > Configure Synchronization Connections > Create New Connection** when you create a new AD Import synchronization connection.

        - `SPS-ClaimProviderID` should be set to the provider name created in [step 1](#1-create-new-claim-provider) by the `New-SPClaimProvider` cmdlet.
        - `SPS-ClaimProviderType` should be set to `SPTrustedBackedByUPAClaimProvider`.

        For MIM synchronization, these properties can be set in the **Configure Attribute Flow** for the MIM database to SharePoint User Profile Application service agent:

        - `SPS-ClaimProviderType` should be set to **Trusted** as Constant type.
        - `SPS-ClaimProviderID` should be set to the provider name created in [step 1](#1-create-new-claim-provider) by the `New-SPClaimProvider` cmdlet.

        :::image type="content" source="../media/configure-attribute-flow-2.png" alt-text="Configure Attribute Flow":::

#### 4. Make groups searchable

To enable the People Picker control to work with groups, the following steps need to be followed:

1. Group object must have a property named “SID” of type “groupid” in the identity provider.

    You can create a `ClaimTypeMapping` object by using [New-SPClaimTypeMapping](/powershell/module/sharepoint-server/new-spclaimtypemapping) and then provide this object to [New-SPTrustedIdentityTokenIssuer](/powershell/module/sharepoint-server/new-sptrustedidentitytokenissuer) cmdlet with `-ClaimsMappings` parameter.

    ```powershell
    $sidClaimMap = New-SPClaimTypeMapping -IncomingClaimType "http://schemas.microsoft.com/ws/2008/06/identity/claims/groupsid" -IncomingClaimTypeDisplayName "SID" -SameAsIncoming 
    $tokenissuer = New-SPTrustedIdentityTokenIssuer -ClaimsMappings $sidClaimMap, $emailClaimMap
    ```

    This sample cmdlet first creates a 'claimmap' object of type 'groupsid' and indicates that it works with the “SID” property of the group and then creates a new identity issuer which can understand this mapping.

2. Synchronize “SID” property of groups from the identity provider to the “SID” property in User Profile Application service.
    1. For AD Import synchronization, SID will be synchronized automatically without additional setup from the source identity provider to the SharePoint User Profile Application service.
    2. For MIM synchronization, the property mapping needs to be taken from the identity provider to MIM and then from MIM to the SharePoint User Profile Application service so that MIM can synchronize the group “SID” from the identity provider to the SharePoint User Profile Application service. This is similar to how we do user profile synchronization for the `SPS-ClaimID` property for user profiles.

3. For MIM synchronization, “sAMAccountName” should also be mapped to “accountName” from MIM to the SharePoint User Profile Application service. If it doesn’t exist, admin should create mapping pair from “sAMAccountName” to “accountName” in MIM manually.

#### 5. Enable fields being searchable in UPSA

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

## Setup OIDC authentication in SharePoint Server with AD FS

### Prerequisites

Ensure you have the following resources before you configure with AD FS OIDC:

1. A SharePoint Server farm.
2. AD FS in Windows Server 2016 or later, already created, with the public key of the AD FS signing certificate exported in a `.cer` file.

This article uses the following values for:

| Value | Link |
|---------|---------|
| SharePoint site URL | `https://spsites.contoso.local/` |
| AD FS site URL     | `https://adfs.contoso.local/adfs/` |
| AD FS authentication endpoint | `https://adfs.contoso.local/adfs/oauth2/authorize` |
| RegisteredIssuerName URL | `https://adfs.contoso.local/adfs/` |
| AD FS SignOut URL  | `https://adfs.contoso.local/adfs/oauth2/logout` |
| Identity claim type | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| Windows site collection administrator | contoso\yvand |
| Email value of the federated (AD FS) site collection administrator | yvand@contoso.local |

### Step 1: Setup Identity Provider

If you choose to use AD FS as identity provider, perform the following steps to setup OIDC with AD FS:

1. In AD FS Management, right-click on **Application Groups** and select **Add Application Group**.
2. In the **Welcome** page, enter **ADFSSSO** in the **Name** field and under **Client-Server applications**, select the **Web browser accessing a web application** template. Then, click **Next**.

    :::image type="content" source="../media/add-application-group-wizard.png" alt-text="Add Application Group Wizard":::

3. In the **Native Application** page, copy the **Client Identifier** value. It will be used later as the value for `DefaultClientIdentifier` parameter during SharePoint configuration.
4. Under the **Redirect URL** field, enter `https://spsites.contoso.local/` and choose **Add**. Then click **Next**.

    :::image type="content" source="../media/add-application-group-wizard-2.png" alt-text="Add Application Group Wizard 2":::

5. In the **Summary** page, click **Next**.

    :::image type="content" source="../media/add-application-group-wizard-3.png" alt-text="Add Application Group Wizard 3":::

6. In the **Complete** page, click **Close**.
7. Export Token-signing certificate from AD FS. This token-signing certificate will be used in SharePoint setup.

    :::image type="content" source="../media/adfs-certificates.png" alt-text="AD FS Certificate Export 1":::

    :::image type="content" source="../media/adfs-certificate-export-2.png" alt-text="AD FS Certificate Export 2":::

    :::image type="content" source="../media/adfs-certificate-export-3.png" alt-text="AD FS Certificate Export 3":::

    :::image type="content" source="../media/adfs-certificate-export-4.png" alt-text="AD FS Certificate Export 4":::

8. Ensure that the required claim ID is included in the `id_token` from AD FS. Let’s take email as an example:

    We assume that your AD FS has configured the rule that read identifier claim from attribute store, such as AD. Perform the following steps to create Issuance Transform Rule for this specific web application we created in AD FS previously:

    1. Open the web application you just created and go to **Issue Transformation Rule** tab.

        :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

        :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

    2. Select **Add Rule** and select **Send LDAP Attributes as Claims** from the option list.

        :::image type="content" source="../media/add-transform-claim-rule.png" alt-text="Add Transform Claim Rule":::

    3. Give your Claim rule a name of **AD** and select **Active Directory** from the Attribute store dropdown menu. Create two mappings using the drop-down boxes as shown:

        | Attribute | Value |
        |---------|---------|
        | E-Mail-Addresses | E-Mail Address |
        | Token-Groups - Qualified by Domain Name | Role |

        :::image type="content" source="../media/add-transform-claim-rule-2.png" alt-text="Add Transform Claim Rule 2":::

    4. Select **Finish** to close the Rule wizard and select **OK** to close the web application properties. Select **OK** one more time to complete the Rule.

If you are setting OIDC with SharePoint Server, nbf claim must be configured in AD FS server side in the web application you just created. If nbf claim doesn’t exist in this web application, perform the following steps to create it:

1. Open the web application you just created and go to **Issue Transformation Rule** tab.

    :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

    :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

2. Select **Add Rule** and then select **Apply**. In the **Add Transform Claim Rule Wizard** select **Send Claims Using a Custom Rule** from the **Claim rule template** options.

    :::image type="content" source="../media/add-transform-claim-rule-3.JPG" alt-text="Add Transform Claim Rule 3":::

3. Select **Next** and input the following string in the **Custom rule** field:

    `c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"] => issue(Type = "nbf", Value = "0");`

    :::image type="content" source="../media/add-transform-claim-rule-4.JPG" alt-text="Add Transform Claim Rule 4":::

4. Select **Finish**.

### Step 2: Change SharePoint Farm properties

In this step, you will need to modify the farm properties. Start the SharePoint Management Shell and run the following script:

> [!NOTE]
> Be sure to follow the instructions mentioned in the following PowerShell script.

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

### Step 3: Configure SharePoint to Identity Providers

In this step, you create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AD FS as OIDC provider. Start the SharePoint Management Shell and run the following script to create it:

> [!NOTE]
> Be sure to follow the instructions mentioned in the following PowerShell script.

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
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ImportTrustCertificate     |  It takes a list of X509 Certificates, which will be used to validate `id_token` from OIDC identifier. If the OIDC IDP uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint will then validate `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A SPClaimTypeMapping object, which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| RegisteredIssuerName | Specifying the issuer identifier, which issues the `id_token`. It will be used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifying the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifying the sign out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server, which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specify the response type of IDP which can be accepted by this token issuer. It can accept two strings, `id_token` and `code id_token`. If this parameter is not provided, it will use `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store and there are two possible options to do this:
>
> - If the AD FS signing certificate is issued by a certificate authority (best practice for security reasons).
>
>     The public key of the issuer's certificate (and all the intermediates) must be added to the store. Start the SharePoint Management Shell and run the following script to add it:
>
>     ```powershell
>     $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing issuer.cer")
>     New-SPTrustedRootAuthority -Name "adfs.contoso.local signing root authority" -Certificate $rootCert
>     ```
>
> - If the ADFS signing certificate is a self-signed certificate (not recommended for security reasons).
>
>     The public key of the ADFS signing certificate itself must be added to the store. Start the SharePoint Management Shell and run the following script to add it:
>
>     ```powershell
>     $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
>     New-SPTrustedRootAuthority -Name "adfs.contoso.local signing certificate" -Certificate $rootCert
>     ```

### Step 4: Configure the SharePoint web application

In this step, you configure a web application in SharePoint to be federated with the AD FS OIDC, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

The important rules to respect here are:

- The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler.
- SharePoint URL that will use AD FS OIDC federation must be configured with HTTPS.

There are two possible configurations:

- If you create a new web application and use both Windows and AD FS OIDC authentication in the Default zone:
  1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

        ```powershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
        $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

  2. Follow [Create a web application in SharePoint Server](/sharepoint/administration/create-a-web-application) to create a new web application enabling HTTPS/SSL named SharePoint - OIDC on contoso.local.
  3. Open the SharePoint Central Administration site.
  4. Open the web application you just created and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers-3.jpg" alt-text="Authentication Providers 3":::

  5. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
  6. Filter the display with the new web application and confirm that you see something like this:

      :::image type="content" source="../media/alternate-access-mapping-collection.png" alt-text="Alternate Access Mapping Collection-1":::

- If you extend an existing web application to set AD FS OIDC authentication on a new zone:
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
    5. Filter the display with the web application that was extended and confirm that you see something like this:

        :::image type="content" source="../media/alternate-access-mapping-collection-2.png" alt-text="Alternate Access Mapping Collection":::

### Step 5: Ensure web application is configured with SSL certificate

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

### Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (AD FS) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections**.
3. Type a Title, URL, and select the template Team Site.
4. In the Primary Site Collection Administrator section, click on the book icon to open the People Picker dialog.
5. In the People Picker dialog, type the Windows administrator account, for example **yvand**.
6. On the left, filter the list by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people-3.png" alt-text="Select People 3":::

7. Select the account and choose **OK**.
8. In the Secondary Site Collection Administrator section, select the book icon to open the People Picker dialog.
9. In the People Picker dialog, type the exact email value of the AD FS administrator account, for example **yvand@contoso.local**.
10. On the left, filter the list by selecting **Contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-4.png" alt-text="Select People 4":::

11. Select the account and choose **OK**.
12. Select **OK** to create the site collection.

Once the site collection is created, you should be able to sign-in to it using either the Windows or the federated site collection administrator account.

### Step 7: Set up People Picker

For more information on how to set up People Picker, see [Step 7: Set up People Picker](#step-7-set-up-people-picker).
