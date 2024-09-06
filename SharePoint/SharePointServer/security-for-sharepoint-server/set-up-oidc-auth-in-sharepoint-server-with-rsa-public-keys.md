---
ms.date: 08/06/2024
title: "Set up OIDC authentication in SharePoint Server using RSA public keys"
ms.reviewer: Wesleywu
ms.author: serdars
author: alekyaj
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how to set up OIDC authentication in SharePoint Server using RSA public keys with Microsoft Entra ID."
---

# Set up OIDC authentication in SharePoint Server using RSA public keys

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

OIDC is an authentication protocol that uses JSON Web Tokens (JWTs) to verify the identity of users, and grant them access to protected resources. JWTs are digitally signed using either symmetric keys (shared between the issuer and the consumer) or asymmetric keys (public/private key pairs).  

SharePoint Server currently supports OIDC auth flow with x5c keys, which are certificates that contain the public key and other metadata. However, some OIDC providers may not use x5c keys, but instead use RSA public keys that are directly represented with RSA modulus and RSA public exponent. To support these providers, SharePoint Server added the ability to parse and validate RSA public keys in JWTs. This new feature is intended to promote OIDC authentication among 3rd-party IdPs without X.509 support like PingFederate and Okta.  

This article will help you understand how to set up OIDC authentication in SharePoint Server using RSA public keys.

## Prerequisites

To configure OpenID Connect (OIDC) using RSA public keys with Microsoft Entra ID, you need the following resources:

1. A SharePoint Server Subscription Edition (SPSE) farm

2. Microsoft Entra Global Administrator role of the M365 tenant

> [!IMPORTANT]
> Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

The following values are examples for Microsoft Entra OIDC setup:

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
1. Go to the **Register an application** page `https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps`.
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

## Step 2: Change SharePoint farm properties

In this step, you need to modify the SharePoint Server farm properties based on the version of your SharePoint Server farm.

- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version 24H1, see [Configure SPSE Version 24H1 or higher version](#configure-sharepoint-server-subscription-edition-version-24h1-or-higher-versions-with-early-release-feature-preference).
- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version preceding 24H1, see [Configure SPSE prior to Version 24H1](#configure-sharepoint-server-subscription-edition-prior-to-version-24h1).

### Configure SharePoint Server Subscription Edition Version 24H1 or higher versions with Early Release feature preference 

Starting with SharePoint Server Subscription Edition Version 24H1 (March 2024), if the SharePoint farm is configured for [Early Release feature preference](/sharepoint/administration/feature-release-rings#early-release), you can configure SharePoint Server farm properties by employing SharePoint Certificate Management to manage the nonce cookie certificate. The nonce cookie certificate is part of the infrastructure to ensure OIDC authentication tokens are secure. Run the following PowerShell script to configure:

> [!IMPORTANT]
> To use this script, the SharePoint farm must be set to Early Release, as noted above.  If it is not, the script will complete without error, but the call to $farm.UpdateNonceCertificate() will not do anything.  If you do not want to configure your farm for Early Release, then you must use the [Configure SPSE prior to Version 24H1](#configure-sharepoint-server-subscription-edition-prior-to-version-24h1) steps instead.

> [!NOTE]
> Start the SharePoint Management Shell as a farm administrator to run the following script. Read the instructions mentioned in the following PowerShell script carefully. You will need to enter your own environment-specific values in certain places.

```powershell
# Set up farm properties to work with OIDC

# Create the Nonce certificate
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"

# Import certificate to Certificate Management
$certPath = "<path and file name to save the exported cert.  ex: c:\certs\nonce.pfx>"
$certPassword = ConvertTo-SecureString -String "<password>" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath $certPath -Password $certPassword
$nonceCert = Import-SPCertificate -Path $certPath -Password $certPassword -Store "EndEntity" -Exportable:$true

# Update farm property
$farm = Get-SPFarm 
$farm.UpdateNonceCertificate($nonceCert,$true)
```

### Configure SharePoint Server Subscription Edition prior to Version 24H1

Prior to the 24H1 (March 2024) update, the nonce cookie certificate must be managed manually.  This includes manually installing it on each server in the farm and setting permissions on the private key.  The following PowerShell script can be used to accomplish that.

> [!NOTE]
>
> Start the SharePoint Management Shell as a farm administrator to run the following script. Read the instructions mentioned in the following PowerShell script carefully. You will need to enter your own environment-specific values in certain places.

```powershell
# Set up farm properties to work with OIDC
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -Provider 'Microsoft Enhanced RSA and AES Cryptographic Provider' -Subject "CN=SharePoint Cookie Cert"
$rsaCert = [System.Security.Cryptography.X509Certificates.RSACertificateExtensions]::GetRSAPrivateKey($cert)
$fileName = $rsaCert.key.UniqueName

# If you have multiple SharePoint servers in the farm, you need to export the certificate by Export-PfxCertificate and import the certificate to all other SharePoint servers in the farm by Import-PfxCertificate. 

# After the certificate is successfully imported to SharePoint Server, we will need to grant access permission to the certificate's private key.

$path = "$env:ALLUSERSPROFILE\Microsoft\Crypto\RSA\MachineKeys\$fileName"
$permissions = Get-Acl -Path $path

# Replace the <web application pool account> with the real application pool account of your web application
$access_rule = New-Object System.Security.AccessControl.FileSystemAccessRule(<Web application pool account>, 'Read', 'None', 'None', 'Allow')
$permissions.AddAccessRule($access_rule)
Set-Acl -Path $path -AclObject $permissions

# Then update farm properties
$farm = Get-SPFarm
$farm.Properties['SP-NonceCookieCertificateThumbprint']=$cert.Thumbprint
$farm.Properties['SP-NonceCookieHMACSecretKey']='seed'
$farm.Update()
```

> [!IMPORTANT]
> The nonce cookie certificate, with private key, must be installed on all SharePoint servers in the farm.  Also, permission to the private key must be given to the web application pool service account on each server.  Failure to complete this step will result OIDC authentication failures. 
> It's recommended to use the PowerShell example above to set permission on the private key file to ensure it's done correctly.

## Step 3: Configure SharePoint to trust the identity provider using RSA public keys

In this step, you create or set up a `SPTrustedTokenIssuer` to store the configuration that SharePoint needs to trust as the OIDC provider. You can configure SharePoint to trust the identity provider either manually or by using the metadata endpoint.

### Configure SharePoint to trust OIDC by using metadata endpoint

An admin can follow the same PowerShell command that is used for x5c keys when using a metadata endpoint for RSA public keys. SharePoint figures out which kind of key is used from the metadata endpoint response and creates the `SPTrustedIdentityTokenIssuer` appropriately. For more information, see [Configure SharePoint to trust Microsoft Entra OIDC by using metadata endpoint](set-up-oidc-auth-in-sharepoint-server-with-msaad.md#configure-sharepoint-to-trust-microsoft-entra-oidc-by-using-metadata-endpoint)for an example.

### Configure SharePoint to trust OIDC manually

When manually creating or setting up the `SPTrustedIdentityTokenIssuer` for RSA public keys, you must specify a new `-PublicKey` parameter while running the `New-SPTrustedIdentityTokenIssuer`and `Set-SPTrustedIdentityTokenIssuer` cmdlets to define the RSA public key modulus and exponent.

#### New-SPTrustedIdentityTokenIssuer

You can run the following PowerShell cmdlet with `-PublicKey` parameter:

```powershell
New-SPTrustedIdentityTokenIssuer -Name "RSA-Manual" -Description "RSA Manually Created" -PublicKey $publicKeyXML -ClaimsMappings $emailClaimMap -IdentifierClaim $emailClaimMap.InputClaimType -DefaultClientIdentifier $clientIdentifier -RegisteredIssuerName $registeredissuernameurl -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -Scope "openid profile" 
```

The `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet uses the following parameters:

| Parameter | Description |
|------------|-------------|
|Name     | Gives a name to the new token issuer. |
|Description     | Gives a description to the new token issuer. |
| PublicKey |Specifies that the value should be an XML string defining the RSA public key modulus and exponent <br> Example of `$publicKeyXML` value: <p> `<RSAKeyValue><Modulus>modulus</Modulus><Exponent>exponent</Exponent></RSAKeyValue>`|
| ClaimsMappings | A `SPClaimTypeMapping` object, which is used to identify which claim in the `id_token` is regarded as identifier in SharePoint. |
| IdentifierClaim | Specifies the type of identifier. |
| DefaultClientIdentifier | Specifies the `client_id` of SharePoint server, which is assigned by OIDC identity provider. This is validated against aud claim in `id_token`. |
| RegisteredIssuerName | Specifies the issuer identifier, which issues the `id_token`. It's used to validate the `id_token`. |
| AuthorizationEndPointUrl | Specifies the authorization endpoint of the OIDC identity provider. |
| SignoutUrl | Specifies the sign out endpoint of the OIDC identity provider. |

To extract the proper $publicKeyXML value from an x509 certificate, you can run the following PowerShell command: 

```powershell
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 

$cert.Import("c:\certs\YourSigningCertificateHere.cer") 

$publicKeyXml = $cert.PublicKey.Key.ToXmlString($false) 
```

#### Set-SPTrustedIdentityTokenIssuer 

The `Set-SPTrustedIdentityTokenIssuer` cmdlet now supports an additional `-PublicKey` parameter for RSA public keys and takes the same `<RSAKeyValue><Modulus>modulus</Modulus><Exponent>exponent</Exponent></RSAKeyValue>` XML string that `New-SPTrustedIdentityTokenIssuer` uses. Example:

```powershell
Set-SPTrustedIdentityTokenIssuer -Identity "RSA-Manual" -PublicKey $publicKeyXml -IsOpenIDConnect 
```

## Step 4: Configure the SharePoint web application

In this step, you configure a web application in SharePoint to be federated with the Microsoft Entra OIDC, using the `SPTrustedIdentityTokenIssuer` created in the previous step.

> [!IMPORTANT]
>
> - The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the Search crawler. 
> - The SharePoint URL that will use Microsoft Entra OIDC federation must be configured with Hypertext Transfer Protocol Secure (HTTPS).

You can complete this configuration either by:

- Creating a new web application and using both Windows and Microsoft Entra OIDC authentication in the default zone.
- Extending an existing web application to set Microsoft Entra OIDC authentication on a new zone.

To **create a new web application**, do the following:

1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

      ```powershell
      # This script creates a trusted authentication provider for OIDC
      
      $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
      $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
      ```

  2. Follow [Create a web application in SharePoint Server](../administration/create-a-web-application.md) to create a new web application enabling HTTPS/Secure Sockets Layer (SSL) named SharePoint - OIDC on contoso.local.
  3. Open the SharePoint Central Administration site.
  4. Select the web application you created, choose "Authentication Providers" in the Ribbon, click the link for the Default zone, and pick **contoso.local** as **Trusted Identity Provider**.

      :::image type="content" source="../media/authentication-providers.jpg" alt-text="Authentication Providers":::

  5. In the SharePoint Central Administration site, navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.

  6. Filter the display with the new web application and confirm that you see the following information:

      :::image type="content" source="../media/new-web-application.png" alt-text="New web application":::

To **extend an existing web application** and configure it to use the "contoso.local" trusted provider, do the following:

1. Start the SharePoint Management Shell and run PowerShell to extend the web application.  The following example extends the web application to the Intranet zone and configures the zone to use the "Contoso.local" trusted provider for authentication.

   > [!NOTE] 
   > For this to work, you must have a valid certificate named 'SharePoint OIDC Site' imported to the farm.  See [SSL certificate management operations](../administration/ssl-certificate-management.md) for more information.

   ```powershell
   # Get the trusted provider
   $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
   $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
   # Get the web app
   $wa = Get-SPWebApplication http://spsites
   # Extend the web app to the "Intranet" zone using trusted provider (OIDC) auth and a SharePoint managed certificate called "SharePoint OIDC Site"
   New-SPWebApplicationExtension -Identity $wa -Name "spsites" -port 443 -HostHeader 'spsites.contoso.local'-AuthenticationProvider $ap -SecureSocketsLayer -UseServerNameIndication -Certificate 'SharePoint OIDC Site' -Zone 'Intranet' -URL 'https://spsites.contoso.local' 
   ```

2. In the SharePoint Central Administration site, navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
3. Filter the display with the web application that was extended and confirm that you see the following information:

      :::image type="content" source="../media/sharepoint-administration-site.png" alt-text="SharePoint Administration Site":::

## Step 5: Ensure the web application is configured with SSL certificate

Since OIDC 1.0 authentication can only work with HTTPS protocol, a certificate must be set on the corresponding web application. If not already configured, perform the following steps to set the certificate:

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

Once the site collection is created, you should be able to sign-in using either the Windows or the federated site collection administrator account.

## Step 7: Set up People Picker

In OIDC authentication, the People Picker doesn't validate the input, which can lead to misspellings or users accidentally selecting the wrong claim type. This can be addressed either by using a Custom Claims Provider, or by using the new UPA-backed claim provider included in SharePoint Server Subscription Edition.  To configure a UPA-backed claim provider, see [Enhanced People Picker for modern authentication](/sharepoint/administration/enhanced-people-picker-for-trusted-authentication-method)
