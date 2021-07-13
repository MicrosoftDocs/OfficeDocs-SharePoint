---
title: "OIDC 1.0 authentication"
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

In SharePoint 2019 and prior versions, SharePoint Server supported three types of authentication methods:

1. Windows authentication (NTLM, Kerberos, etc.)
2. Forms-based authentication
3. SAML 1.1-based authentication

In view of an increasing number of customers demanding support for modern authentication protocols such as OpenID Connect (OIDC) 1.0 and Security Assertion Markup Language (SAML) 2.0, SharePoint Server Subscription Edition now supports OIDC 1.0 authentication protocol.

With this new capability, you can now set up an OIDC-enabled `SPTrustedIdentityTokenIssuer` that works with a remote identity provider to enable OIDC authentication.

> [!NOTE]
> Only SharePoint with Active Directory Federation Services (AD FS) and Azure Active Directory (AAD) are validated for OIDC connections. Other third-party identity providers might not currently work.

SharePoint Server Subscription Edition now supports basic manual OIDC configuration through PowerShell along with the support for OIDC metadata discovery capability during configuration.

Using the metadata endpoint provided from OIDC identity provider, the following configurations can be retrieved from OIDC provider metadata endpoint directly:

1. Certificate
2. Issuer
3. Authorization Endpoint
4. SignoutURL

This can simplify the configuration of OIDC token issuer.

`New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is updated for OIDC metadata endpoint configuration using the following parameters:

New-SPTrustedIdentityTokenIssuer -Name < issuer name > -Description < Issuer description > -ClaimsMappings < ClaimMappings >  -IdentifierClaim < InputClaimType >  -DefaultClientIdentifier < client_id >  -MetadataEndPoint < metadata endpoint >

| Parameter | Description |
|------------|-------------|
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ClaimsMappings     | A `SPClaimTypeMapping` object which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
|IdentifierClaim     | Specifying which type the identifier is. |
|DefaultClientIdentifier     | Specify the `client_id` of SharePoint server which is assigned by OIDC identity provider. This will be validated against 'aud' claim in `id_token`. |
|MetadataEndPoint     | Specifying the well-known metadata endpoint from OIDC identity provider which can be used to retrieve latest certificate, issuer, authorization endpoint and sign out endpoint. |

SharePoint Server Subscription Edition also supports picking a certificate from a rotating list of signing certificates to digitally sign the `id_token` as SharePoint needs to validate the digital signature of the OIDC `id_token`. Previously, each `SPTrustedIdentityTokenIssuer` only supported one signing certificate, so they couldn’t support a rotating list of signing certificates.

With SharePoint Server Subscription Edition, the **ImportTrustCertificate** parameter of the `New-SPTrustedIdentityTokenIssuer` cmdlet has been updated to support a list of certificate objects, that allows SharePoint to support a rotating list of signing certificates for `id_token` validation.

As a result of the switch to Windows Identity Foundation 4.5 framework, several changes have been made to the PowerShell cmdlets to set up OIDC authentication. For more information, see the updated OIDC Setup Guide.

## Setup OIDC authentication in SharePoint Server with AAD

### Overview of federated authentication

In federated authentication, SharePoint processes OIDC tokens issued by a trusted, external Security Token Service (STS) or identity provider (IDP). A user who attempts to log on is redirected to that Security Token Service (STS), which authenticates the user and generates a JSON web token (JWT) token upon successful authentication. SharePoint then processes this token and uses it to create its own and authorizes the user to access the site.

You need to do configurations both in identity provider and SharePoint to make the authentication flow work normally.

1. Configurations in identity provider requires you to register SharePoint web application as trusted party with redirection URL which will redirect client back to SharePoint web application. To do that:
    - Register redirect URL of SharePoint to IDP so that IDP will pass through JWT token back to the endpoint in SharePoint which will process the token.
    - Register original URL of SharePoint to IDP so that only authentication request from registered URL can be accepted.
    - Specify user identifier claim in the token for it to get aligned with SharePoint so that SharePoint Server can know which claim should be used as unique identity for the login user.
2. Configurations in SharePoint require IDP to be configured through `SPTrustedIdentityTokenIssuer` so that it can be used for SharePoint web application authentication. To do that:
    - Setup certificates from IDP so that trust can be setup between SharePoint and identity provider.
    - Setup authentication endpoint from IDP so that authentication will be rely to IDP.
    - Setup logout endpoint from IDP so that a logout from SharePoint will also result in a logout from IDP.
    - Align user identifier claim with IDP so that SharePoint is able to know which claim to use to identify a login user.

### Prerequisites

To perform the configuration, you need the following resources when you configure with Azure Active Directory OIDC:

1. A SharePoint Server Subscription Edition farm
2. AAD administration privilege and M365 tenant

This article uses the following values for AAD OIDC setup:

| Value | Link |
|---------|---------|
| SharePoint site URL | https://spsites.contoso.local/ |
| OIDC site URL     | https://sts.windows.net/< tenantid >/ |
| AAD OIDC authentication endpoint     | https://login.microsoftonline.com/< tenantid >/oauth2/authorize |
| AAD OIDC RegisteredIssuerName URL     | https://sts.windows.net/< tenantid >/ |
| AAD OIDC SignOut URL     | https://login.microsoftonline.com/>< tenantid >/oauth2/logout |
| Identity claim type     | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |
| Windows site collection administrator     | contoso\yvand |
| Email value of the federated (AD FS) site collection administrator     | yvand@contoso.local |

### Step 1: Setup Identity Provider

If you choose to use AAD as federated identity provider, perform the following steps to setup AAD OIDC:

1. Go to the **App Registration** page <https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps>.
2. Enter the following for Redirect URL: <https://spsites.contoso.local/> and select **Register**.

    :::image type="content" source="../media/register-an-app.PNG" alt-text="Register an application":::

3. Save **Directory(tenant) ID** as it is the tenant ID that we will use in future and save **Application (client) ID** which will be used as **DefaultClientIdentifier** in SharePoint setup.

    :::image type="content" source="../media/sharepoint-onprem-oidc-connection.png" alt-text="Save Application":::

4. After registering, go to the **Authentication** tab and enable **ID tokens**, then select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-authentication.png" alt-text="Enable ID Tokens":::

5. Go to the **API permissions** tab and add **email** and **profile** permissions.

    :::image type="content" source="../media/sharepoint-oidc-api-permissions.png" alt-text="API Permissions":::

6. Go to the **Token configuration** tab and add **email**, **groups** and **upn** optional claims.

    :::image type="content" source="../media/sharepoint-oidc-token-configuration.png" alt-text="Token Configuration":::

7. Go to the **Manifest** tab, and manually change **replyUrlsWithType.url** from <https://spsites.contoso.local/> to <https://spsites.contoso.local/>*. Then select **Save**.

    :::image type="content" source="../media/sharepoint-oidc-manifest.png" alt-text="Manifest":::

8. Get OIDC authentication information from OIDC discovery endpoint.

In AAD, there are 2 versions of OIDC authentication endpoints. Therefore, there are 2 versions of OIDC discovery endpoints, respectively:

- V1.0: <https://login.microsoftonline.com/< TenantID >/.well-known/openid-configuration>
- V2.0: <https://login.microsoftonline.com/< TenantID >/v2.0/.well-known/openid-configuration>

Replace TenantID with the **Directory(tenant) ID** saved in step #3, and connect to the endpoint by your browser. Then, save the following information:

| Value | Link |
|---------|---------|
| authorization_endpoint | https://login.microsoftonline.com/< tenantid >/oauth2/authorize |
| end_session_endpoint   | https://login.microsoftonline.com/< tenantid >/oauth2/logout |
| issuer     | https://sts.windows.net/< tenantid >/ |
| jwks_uri     | https://login.microsoftonline.com/common/discovery/keys |

Open jwks_uri (<https://login.microsoftonline.com/common/discovery/keys>), and save **x5c** certificate string of the first **key** for later use in SharePoint setup (if the first key doesn’t work, try the second or third key).

:::image type="content" source="../media/sharepoint-setup-keys.png" alt-text="Discovery keys":::

### Step 2: Change SharePoint Farm properties

In this step, modify farm properties.

```azurepowershell
# Setup farm properties to work with OIDC
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject “CN=SharePoint Cookie Cert”
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
$f.Farm.Properties['SPO-SignInContextCertificateThumbprint']=$cert.Thumbprint
$f.Farm.Properties['SPO-SignInGateKeeperHashSeed']='seed'
$f.Farm.Update()
```

### Step 3: Configure SharePoint to Identity Providers

You can configure SharePoint to Identity Providers in the following two ways:

- Configure SharePoint to trust AAD as OIDC provider manually
- Configure SharePoint to trust AAD as OIDC provider by using metadata endpoint
  - By using metadata endpoint, a lot of parameters you need in 'Configure SharePoint to trust AAD as OIDC provider manually' can be automatically retrieved by metadata endpoint.

#### Configure SharePoint to trust AAD as OIDC provider manually

In this step, you create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AAD OIDC as OIDC provider. Start the SharePoint Management Shell and run the following script to create it:

PowerShell

```azurepowershell
# Define claim types
#If you are using SharePoint Server TAP build 16.0.13727.10000 or later build
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

#If you are using SharePoint Server TAP build 16.0.13628.10000 or earlier build
$email = New-SPClaimTypeMapping -IncomingClaimType "email" -IncomingClaimTypeDisplayName "EmailAddress" -LocalClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 

# Public key of the AAD OIDC signing certificate. Please replace <x5c cert string> with the encoded cert string which you get from x5c certificate string of the keys of jwks_uri from Step #1
$encodedCertStr = <x5c cert string>
$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 @(,[System.Convert]::FromBase64String($encodedCertStr))
# Set the AAD OIDC URL where users are redirected to authenticate. Please replace <tenanted> accordingly
$authendpointurl = "https://login.microsoftonline.com/<tenantid>/oauth2/authorize"
$registeredissuernameurl = " https://sts.windows.net/<tenantid>/"
$signouturl = " https://login.microsoftonline.com/<tenantid>/oauth2/logout"

# Please replace <Application (Client) ID> with the value saved in step #3 in AAD setup section
$clientIdentifier = <Application (Client)ID>

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "Contoso.local" -Description "Contoso.local" -ImportTrustCertificate $signingCert -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -RegisteredIssuerName $registeredissuernameurl  -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -DefaultClientIdentifier $clientIdentifier
```

Here, `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is extended to support OIDC by using the following parameters:

| Parameter | Description |
|------------|-------------|
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ImportTrustCertificate     | It takes a list of X509 Certificates which will be used to validate `id_token` from OIDC identifier. If the OIDC IDP uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint will then validate `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A `SPClaimTypeMapping` object which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| RegisteredIssuerName | Specifying the issuer identifier which issues the `id_token`. It will be used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifying the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifying the sign out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specify the response type of IDP can be accepted by this token issuer. It can accept 2 strings, `id_token` and `code id_token`. If this parameter is not provided, it will use `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store:
>
> `New-SPTrustedRootAuthority -Name "AAD OIDC signing root authority" -Certificate $signingCert`

#### Configure SharePoint to trust AAD OIDC by using metadata endpoint

SharePoint Server Subscription Edition now supports OIDC meta data discovery capability during configuration.

By using the metadata endpoint provided from OIDC identity provider, some of the configuration will be retrieved from OIDC provider metadata endpoint directly, including:

1. Certificate
2. Issuer
3. Authorization Endpoint
4. SignoutURL

This can simplify the configuration of OIDC token issuer.

By using below PowerShell example, we can use metadata endpoint from AAD to configure SharePoint to trust AAD OIDC.

```azurepowershell
# Define claim types
#If you are using SharePoint Server TAP build 16.0.13727.10000 or later build
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

#If you are using SharePoint Server TAP build 16.0.13628.10000 or earlier build
$email = New-SPClaimTypeMapping -IncomingClaimType "email" -IncomingClaimTypeDisplayName "EmailAddress" -LocalClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 

# Set the AAD metadata endpoint URL 
$metadataendpointurl = "https://login.microsoftonline.com/<TenantID>/.well-known/openid-configuration"

# Please replace <Application (Client) ID> with the value saved in step #3 in AAD setup section
$clientIdentifier = <Application (Client)ID>

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "Contoso.local" -Description "Contoso.local" -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -DefaultClientIdentifier $clientIdentifier -MetadataEndPoint $ metadataendpointurl
```

New-SPTrustedIdentityTokenIssuer -Name < issuer name > -Description < Issuer description > -ClaimsMappings < ClaimMappings >  -IdentifierClaim < InputClaimType >  -DefaultClientIdentifier < client_id >  -MetadataEndPoint < metadata endpoint >

| Parameter | Description |
|------------|-------------|
|Name     | Giving a name to this new token issuer. |
|Description     | Giving a description to this new token issuer. |
|ImportTrustCertificate     | A certificate which will be used to validate `id_token` from OIDC identifier. |
| ClaimsMappings | A `SPClaimTypeMapping` object which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| MetadataEndPoint | Specifying the well-known metadata endpoint from OIDC identity provider which can be used to retrieve latest certificate, issuer, authorization endpoint and sign out endpoint. |

### Step 4: Configure the SharePoint web application

In this step you configure a web application in SharePoint to be federated with the AAD OIDC, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

The important rules to respect here are:

- The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler.
- SharePoint URL that will use AAD OIDC federation must be configured with HTTPS.

There are two possible configurations:

- If you create a new web application and use both Windows and AAD OIDC authentication in the Default zone:

    1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

        ```azurepowershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
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

    ```azurepowershell
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

### Step 5: Ensure that an HTTPS certificate is set in IIS

As SharePoint URL uses HTTPS protocol (<https://spsites.contoso.local/>), a certificate must be set on the corresponding Internet Information Services (IIS) site. Perform the following steps to set a certificate on the corresponding IIS:

- Generate the site certificate:

    > [!NOTE]
    > You may skip this step if you have already generated the certificate.
    > 
    > 1. Open the Windows PowerShell console.
    > 2. Run the following script to generate a self-signed certificate and add it to the computer's MY store:
    > 
    >     `New-SelfSignedCertificate -DnsName "spsites.contoso.local" -CertStoreLocation "cert:\LocalMachine\My"`
    >

    > [!IMPORTANT]
    > Self-signed certificates are suitable only for test purposes. In production environments, we strongly recommend that you use certificates issued by a certificate authority instead.

- Set the certificate:

    1. Open the Internet Information Services Manager console.
    2. Expand the server in the tree view, expand **Sites**, select the **SharePoint - ADFS** on contoso.local site, and select **Bindings**.
    3. Select https binding and then select **Edit**.
    4. In the TLS/SSL certificate field, choose spsites.contoso.local certificate and then select **OK**.

### Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (AD FS) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections** > **Create site collections**.
3. Type a Title, Url, and select the template Team Site.
4. In the Primary Site Collection Administrator section, click on the book icon to open the people picker dialog.
5. In the people picker dialog, type the Windows administrator account, for example **yvand**.
6. On the left, filter the list by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people.png" alt-text="Select people":::

7. Select the account and choose **OK**.
8. In the Secondary Site Collection Administrator section, select the book icon to open the people picker dialog.
9. In the people picker dialog, type the exact email value of the AD FS administrator account, for example **yvand@contoso.local**.
10. On the left, filter the list by selecting **Contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-2.png" alt-text="Select people 2":::

11. Select the account and choose **OK**.
12. Select **OK** to create the site collection.

Once the site collection is created, you should be able to sign-in to it using either the Windows or the federated site collection administrator account.

### Step 7: Set up people picker

In OIDC authentication, the people picker does not validate the input, which can lead to misspellings or users accidentally choosing the wrong claim type. This can be addressed using the new UPA backed claim provider in SharePoint Server.

## Setup OIDC authentication in SharePoint Server with AD FS

### Overview of federated authentication

In federated authentication, SharePoint processes OIDC tokens issued by a trusted, external Security Token Service (STS) or identity provider (IDP). A user who attempts to log on is redirected to that STS, which authenticates the user and generates a JWT token upon successful authentication. SharePoint then processes this token and uses it to create its own and authorizes the user to access the site.

You need to do configurations both in identity provider and SharePoint to make the authentication flow work normally.

1. Configurations in identity provider require you to register SharePoint web application as trusted party with redirection URL which will redirect client back to SharePoint web application. To do that:

    - Redirect URL of SharePoint needs to be registered to IDP so that IDP will pass through JWT token back to the endpoint in SharePoint which will process the token.
    - Original URL of SharePoint needs to be registered to IDP so that only authentication request from registered URL can be accepted.
    - User identifier claim needs to be specified in the token and get aligned with SharePoint so that SharePoint server can know which claim should be used as unique identity for the login user.
2. Configurations in SharePoint require IDP to be configured through `SPTrustedIdentityTokenIssuer` so that it can be used for SharePoint web application authentication. To do that:

    - Certificates from IDP need to be setup so that trust can be setup between SharePoint and identity provider.
    - Authentication endpoint from IDP needs to be setup so that authentication will be rely to IDP.
    - Logout endpoint from IDP needs to be setup so that a logout from SharePoint will also logout from IDP.
    - User identifier claim needs to be aligned with IDP so that SharePoint can identity which claim to use to identify a login user.

### Prerequisites

You would require the following resources when you configure with AD FS OIDC:

1. A SharePoint Server farm.
2. AD FS in Windows Server 2016 TP4 or later, already created, with the public key of the AD FS signing certificate exported in a .cer file.

This article uses the following values for:

| Value | Link |
|---------|---------|
| SharePoint site URL | https://spsites.contoso.local/ |
| AD FS site URL     | https://adfs.contoso.local/adfs/ |
| AD FS authentication endpoint | https://adfs.contoso.local/adfs/oauth2/authorize |
| RegisteredIssuerName URL | https://adfs.contoso.local/adfs/ |
| AD FS SignOut URL  | https://adfs.contoso.local/adfs/oauth2/logout |
| Identity claim type | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |
| Windows site collection administrator | contoso\yvand |
| Email value of the federated (AD FS) site collection administrator | yvand@contoso.local |

### Step 1: Setup Identity Provider

If you choose to use AD FS as identity provider, perform the following steps to setup OIDC with AD FS:

1. In AD FS Management, right-click on **Application Groups** and select **Add Application Group**.
2. On the Application Group Wizard, enter **ADFSSSO** in the **Name** field and under **Client-Server applications**, select the **Web browser accessing a web application** template. Then, select **Next**.

    :::image type="content" source="../media/add-application-group-wizard.png" alt-text="Add Application Group Wizard":::

3. Copy the **Client Identifier** value. It will be used later as the value for `DefaultClientIdentifier` parameter during SharePoint configuration.
4. Under the **Redirect URL** field, enter <https://spsites.contoso.local/> and choose **Add**. Then select **Next**.

    :::image type="content" source="../media/add-application-group-wizard-2.png" alt-text="Add Application Group Wizard 2":::

5. On the **Summary** screen, select **Next**.

    :::image type="content" source="../media/add-application-group-wizard-3.png" alt-text="Add Application Group Wizard 3":::

6. On the **Complete** screen, select **Close**.
7. Export Token-signing certificate from AD FS. This token-signing certificate will be used in SharePoint setup.

    :::image type="content" source="../media/adfs-certificates.png" alt-text="AD FS Certificate Export 1":::

    :::image type="content" source="../media/adfs-certificate-export-2.png" alt-text="AD FS Certificate Export 2":::

    :::image type="content" source="../media/adfs-certificate-export-3.png" alt-text="AD FS Certificate Export 3":::

    :::image type="content" source="../media/adfs-certificate-export-4.png" alt-text="AD FS Certificate Export 4":::

8. Ensure that the required claim ID is included in the `id_token` from AD FS. Let’s take email as an example:

    We assume that your AD FS has configured the rule that read identifier claim from attribute store, such as AD. Perform the following steps to create Issuance Transform Rule for this specific web application we created in AD FS above:

    1. Open the web application you just created and go to 'Issue Transformation Rule' tab.

        :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

        :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

    2. Select **Add Rule** followed by **Pass Through or Filter an Incoming Claim** from the **Claim rule template** options.

        :::image type="content" source="../media/add-transform-claim-rule.JPG" alt-text="Add Transform Claim Rule":::

    3. Select **Next** and fill in the next form as shown.

        :::image type="content" source="../media/add-transform-claim-rule-2.jpg" alt-text="Add Transform Claim Rule 2":::

    4. Select **Finish**.

If you are setting OIDC with SharePoint Server, nbf claim must be configured in AD FS server side in the web application you just created. If nbf claim doesn’t exist in this web application, perform the following steps to create it:

1. Open the web application you just created and go to **Issue Transformation Rule** tab.

    :::image type="content" source="../media/issue-transformation-rule.jpg" alt-text="Issue Transformation Rule":::

    :::image type="content" source="../media/issue-transformation-add-rule.JPG" alt-text="Issue Transformation Add Rule":::

2. Select **Add Rule** followed by **Send Claims Using a Custom Rule** from the **Claim rule template** options.

    :::image type="content" source="../media/add-transform-claim-rule-3.JPG" alt-text="Add Transform Claim Rule 3":::

3. Select **Next** and input the following string in the **Custom rule** field:

    `c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"] => issue(Type = "nbf", Value = "0");`

    :::image type="content" source="../media/add-transform-claim-rule-4.JPG" alt-text="Add Transform Claim Rule 4":::

4. Select **Finish**.

### Step 2: Change SharePoint Farm properties

In this step, modify the farm properties.

```azurepowershell
# Setup farm properties to work with OIDC
#Create a self-signed certificate in one SharePoint Server in the farm
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject “CN=SharePoint Cookie Cert”

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
$f.Farm.Properties['SPO-SignInContextCertificateThumbprint']=$cert.Thumbprint
$f.Farm.Properties['SPO-SignInGateKeeperHashSeed']='seed'
$f.Farm.Update()
```

### Step 3: Configure SharePoint to Identity Providers

In this step you create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AD FS as OIDC provider. Start the SharePoint Management Shell and run the following script to create it:

PowerShell

```azurepowershell
# Define claim types
#If you are using SharePoint Server TAP build 16.0.13727.10000 or later build
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

#If you are using SharePoint Server TAP build 16.0.13628.10000 or earlier build
$email = New-SPClaimTypeMapping -IncomingClaimType "email" -IncomingClaimTypeDisplayName "EmailAddress" -LocalClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 

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
|ImportTrustCertificate     |  It takes a list of X509 Certificates which will be used to validate `id_token` from OIDC identifier. If the OIDC IDP uses more than one certificate to digital sign the `id_token`, import these certificates and SharePoint will then validate `id_token` by matching the digital signature generated by using these certificates. |
| ClaimsMappings | A SPClaimTypeMapping object which will be used to identify which claim in the `id_token` will be regarded as identifier in SharePoint. |
| IdentifierClaim | Specifying which type the identifier is. |
| RegisteredIssuerName | Specifying the issuer identifier which issues the `id_token`. It will be used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifying the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifying the sign out endpoint of the OIDC identity provider. |
| DefaultClientIdentifier | Specify the `client_id` of SharePoint server which is assigned by OID identity provider. This will be validated against aud claim in `id_token`. |
| ResponseTypesSupported | Specify the response type of IDP can be accepted by this token issuer. It can accept 2 strings, `id_token` and `code id_token`. If this parameter is not provided, it will use `code id_token` as default. |

> [!IMPORTANT]
> The relevant certificate must be added to the SharePoint root authority certificate store and there are two possible options to do this:
>
> - If the AD FS signing certificate is issued by a certificate authority (best practice for security reasons).
>
>     The public key of the issuer's certificate (and all the intermediates) must be added to the store. Start the SharePoint Management Shell and run the following script to add it:
>
> ```azurepowershell
> $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing issuer.cer")
> New-SPTrustedRootAuthority -Name "adfs.contoso.local signing root authority" -Certificate $rootCert
> ```
>
> - If the ADFS signing certificate is a self-signed certificate (not recommended for security reasons).
>
>     The public key of the ADFS signing certificate itself must be added to the store. Start the SharePoint Management Shell and run the following script to add it:
>
> ```azurepowershell
> $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
> New-SPTrustedRootAuthority -Name "adfs.contoso.local signing certificate" -Certificate $rootCert
> ```

### Step 4: Configure the SharePoint web application

In this step you configure a web application in SharePoint to be federated with the AD FS OIDC, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

The important rules to respect here are:

- The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler.
- SharePoint URL that will use AD FS OIDC federation must be configured with HTTPS.

There are 2 possible configurations:

- If you create a new web application and use both Windows and AD FS OIDC authentication in the Default zone:
  1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

        ```azurepowershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
        $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

  2. Follow [Create a web application in SharePoint Server](/sharepoint/administration/create-a-web-application) to create a new web application enabling HTTPS/SSL named SharePoint - OIDC on contoso.local.
  3. Open the SharePoint Central Administration site.
  4. Open the web application you just created and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers-3.jpg" alt-text="Authentication Providers 3":::

  5. Open the SharePoint Central Administration site.
  6. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
  7. Filter the display with the new web application and confirm that you see something like this:

      :::image type="content" source="../media/alternate-access-mapping-collection.png" alt-text="Alternate Access Mapping Collection":::

- If you extend an existing web application to set AD FS OIDC authentication on a new zone:
    1. Start the SharePoint Management Shell and run the following script:

        ```azurepowershell
        # This script creates a trusted authentication provider for OIDC
        
        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
        $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        ```

    2. Open the SharePoint Central Administration site.
    3. Open the web application you want to extend OIDC authentication to and pick **contoso.local** as **Trusted Identity Provider**.

        :::image type="content" source="../media/authentication-providers-4.jpg" alt-text="Authentication Providers 4":::

    4. Open the SharePoint Central Administration site.
    5. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
    6. Filter the display with the web application that was extended and confirm that you see something like this:

        :::image type="content" source="../media/alternate-access-mapping-collection-2.png" alt-text="Alternate Access Mapping Collection":::

### Step 5: Ensure that an HTTPS certificate is set in IIS

As SharePoint URL uses HTTPS protocol (<https://spsites.contoso.local/>), a certificate must be set on the corresponding Internet Information Services (IIS) site. Perform the following steps to set a certificate on the corresponding IIS:

- Generate the site certificate:

    > [!NOTE]
    > You may skip this step if you already generated the certificate.
    >
    > 1. Open the Windows PowerShell console.
    > 2. Run the following script to generate a self-signed certificate and add it to the computer's MY store:
    >
    >     `New-SelfSignedCertificate -DnsName "spsites.contoso.local" -CertStoreLocation "cert:\LocalMachine\My"`
    >

    > [!IMPORTANT]
    > Self-signed certificates are suitable only for test purposes. In production environments, we strongly recommend that you use certificates issued by a certificate authority instead.

- Set the certificate:

 1. Open the Internet Information Services Manager console.
 2. Expand the server in the tree view, expand **Sites**, select the **SharePoint - ADFS** on contoso.local site, and select **Bindings**.
 3. Select https binding and then select **Edit**.
 4. In the TLS/SSL certificate field, choose spsites.contoso.local certificate and then select **OK**.

### Step 6: Create the site collection

In this step, you create a team site collection with two administrators: One as a Windows administrator and one as a federated (AD FS) administrator.

1. Open the SharePoint Central Administration site.
2. Navigate to **Application Management** > **Create site collections** > **Create site collections**.
3. Type a Title, Url, and select the template Team Site.
4. In the Primary Site Collection Administrator section, click on the book icon to open the people picker dialog.
5. In the people picker dialog, type the Windows administrator account, for example **yvand**.
6. On the left, filter the list by selecting **Organizations**. Following is a sample output:

    :::image type="content" source="../media/select-people-3.png" alt-text="Select People 3":::

7. Select the account and choose **OK**.
8. In the Secondary Site Collection Administrator section, select the book icon to open the people picker dialog.
9. In the people picker dialog, type the exact email value of the AD FS administrator account, for example **yvand@contoso.local**.
10. On the left, filter the list by selecting **Contoso.local**. Following is a sample output:

    :::image type="content" source="../media/select-people-4.png" alt-text="Select People 4":::

11. Select the account and choose **OK**.
12. Select **Ok** to create the site collection.

Once the site collection is created, you should be able to sign-in to it using either the Windows or the federated site collection administrator account.

### Step 7: Set up people picker

In OIDC authentication, the people picker does not validate the input, which can lead to misspellings or users accidentally choosing the wrong claim type. This can be addressed using the new UPA backed claim provider in SharePoint Server.
