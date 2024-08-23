---
ms.date: 07/11/2021
title: "Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)"
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
description: "Learn how to set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)."
---

# Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS)

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

## Prerequisites

When you configure SharePoint Server with Active Directory Federation Services (AD FS) using OpenID Connect (OIDC) authentication, you need the following resources to perform the configuration:

1. A SharePoint Server Subscription Edition farm.
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

In this step, you need to modify the SharePoint Server farm properties based on the version of your SharePoint Server farm.

- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version 24H1, see [Configure SPSE Version 24H1 or higher version](#configure-sharepoint-server-subscription-edition-version-24h1-or-higher-versions-with-early-release-feature-preference).
- For more information on configuring SharePoint farm properties for SharePoint Server Subscription Edition Version preceding 24H1, see [Configure SPSE prior to Version 24H1](#configure-sharepoint-server-subscription-edition-prior-to-version-24h1).

#### Configure SharePoint Server Subscription Edition Version 24H1 or higher versions with Early Release feature preference 

Starting with SharePoint Server Subscription Edition Version 24H1 (March 2024), if the SharePoint farm is configured for [Early Release feature preference](/sharepoint/administration/feature-release-rings#early-release), you can configure SharePoint Server farm properties by employing SharePoint Certificate Management to manage the nonce cookie certificate. The nonce cookie certificate is part of the infrastructure to ensure OIDC authentication tokens are secure. Run the following PowerShell script to configure:
> [!IMPORTANT] 
> To use this script, the SharePoint farm must be set to Early Release, as noted above.  If it is not, the script will complete without error, but the call to $farm.UpdateNonceCertificate() will not do anything.  If you do not want to configure your farm for Early Release, then you must use the [Configure SPSE prior to Version 24H1](#configure-sharepoint-server-subscription-edition-prior-to-version-24h1) steps instead.

> [!Note]
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

#### Configure SharePoint Server Subscription Edition prior to Version 24H1

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

# Update farm properties
$farm = Get-SPFarm
$farm.Properties['SP-NonceCookieCertificateThumbprint']=$cert.Thumbprint
$farm.Properties['SP-NonceCookieHMACSecretKey']='seed'
$farm.Update()
```

## Step 3: Configure SharePoint to trust the identity providers

In this step, you'll create a `SPTrustedTokenIssuer` that will store the configuration that SharePoint needs to trust AD FS as an OIDC provider. Start the SharePoint Management Shell as a farm administrator and run the following script to create it:

> [!NOTE]
> Read the instructions mentioned in the following PowerShell script carefully.  You will need to input environment-specific values in several places.

```powershell
# Define claim types
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming

# Public key of the AD FS signing certificate
$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
# Set the AD FS URL where users are redirected to authenticate
$authendpointurl = "https://adfs.contoso.local/adfs/oauth2/authorize"
$registeredissuernameurl = "https://adfs.contoso.local/adfs"
$signouturl = "https://adfs.contoso.local/adfs/oauth2/logout"

# Replace <Client Identifier> with the value you saved in step #3 of AD FS Setup section
$clientIdentifier = "<Your Client Identifier>"

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "Contoso.local" -Description "Contoso.local" -ImportTrustCertificate $signingCert -ClaimsMappings $email -IdentifierClaim $email.InputClaimType  -RegisteredIssuerName $registeredissuernameurl  -AuthorizationEndPointUri $authendpointurl -SignOutUrl $signouturl -DefaultClientIdentifier $clientIdentifier
```

The `New-SPTrustedIdentityTokenIssuer` PowerShell cmdlet is extended to support OIDC by using the following parameters:

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
>     The public key of the AD FS signing certificate must be added to the store. Start the SharePoint Management Shell and run the following script to add the certificate:
>
>     ```powershell
>     $rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
>     New-SPTrustedRootAuthority -Name "adfs.contoso.local signing certificate" -Certificate $rootCert
>     ```

## Step 4: Configure a SharePoint web application

In this step, you'll configure a web application in SharePoint to use AD FS OIDC authentication, using the `SPTrustedIdentityTokenIssuer` that was created in the previous step.

> [!IMPORTANT]
>
> - The default zone of the SharePoint web application must have Windows authentication enabled. This is required for the search crawler.
> - The SharePoint URL that will use AD FS OIDC federation must be configured with HTTPS.

You can complete this configuration either by:

- Creating a new web application and using both Windows and AD FS OIDC authentication in the Default zone. To create a new web application, do the following:

  1. Start the SharePoint Management Shell and run the following script to create a new `SPAuthenticationProvider`:

     ```powershell
     # This script creates a trusted authentication provider for OIDC    
     $sptrust = Get-SPTrustedIdentityTokenIssuer "contoso.local"
     $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
     ```

  2. Follow [Create a web application in SharePoint Server](/sharepoint/administration/create-a-web-application) to create a new web application enabling HTTPS/SSL named SharePoint - OIDC on contoso.local.

  3. Open the SharePoint Central Administration site.

  4. Open the web application you created, choose "Authentication Providers" in the Ribbon, click the link for the "Default" zone, and pick **contoso.local** as **Trusted Identity Provider**.

     :::image type="content" source="../media/authentication-providers-3.jpg" alt-text="Authentication Providers 3":::

  5. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.
  
  6. Filter the display with the new web application and confirm that you see the following information:

     :::image type="content" source="../media/alternate-access-mapping-collection.png" alt-text="Alternate Access Mapping Collection-1":::

- Extending an existing web application to set AD FS OIDC authentication on a new zone. To extend an existing web application, do the following:

  1. Start the SharePoint Management Shell and run PowerShell to extend the web application:

     **Example:**

     ```powershell
     # Get the trusted provider
     $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
     $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
     # Get the web app
     $wa = Get-SPWebApplication http://spsites
     # Extend the web app to the "Intranet" zone using trusted provider auth and a SharePoint managed certificate called "SharePoint OIDC Site"
     New-SPWebApplicationExtension -Identity $wa -Name "spsites" -port 443 -HostHeader 'spsites.contoso.local'-AuthenticationProvider $ap -SecureSocketsLayer -UseServerNameIndication -Certificate 'SharePoint OIDC Site' -Zone 'Intranet' -URL 'https://spsites.contoso.local' 
     ```

  2. Navigate to **System Settings** > **Configure Alternate Access Mappings** > **Alternate Access Mapping Collection**.

  3. Filter the display with the web application that was extended and confirm that you see the following information:

     :::image type="content" source="../media/alternate-access-mapping-collection-2.png" alt-text="Alternate Access Mapping Collection":::

## Step 5: Ensure the web application is configured with SSL certificate

Since OpenID Connect 1.0 authentication can only work with HTTPS protocol, a certificate must be set on the corresponding web application. If you have not already done so, perform the following steps to set a certificate:

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

Once the site collection is created, you should be able to sign-in using either the Windows or the federated (AD FS OIDC) site collection administrator account.

## Step 7: Set up People Picker
In OIDC authentication, the People Picker doesn't validate the input, which can lead to misspellings or users accidentally selecting the wrong claim type. This can be addressed either by using a Custom Claims Provider, or by using the new UPA-backed claim provider included in SharePoint Server Subscription Edition.  To configure a UPA-backed claim provider, see [Enhanced People Picker for modern authentication](/sharepoint/administration/enhanced-people-picker-for-trusted-authentication-method).
