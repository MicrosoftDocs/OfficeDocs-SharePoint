---
# Required metadata
# For more information, see https://review.learn.microsoft.com/en-us/help/platform/learn-editor-add-metadata?branch=main
# For valid values of ms.service, ms.prod, and ms.topic, see https://review.learn.microsoft.com/en-us/help/platform/metadata-taxonomies?branch=main

title:       Use Certificate Based Authentication in migration
description: Describe how to use Certificate Based Authentication in migration
author:      zacsun-ms # GitHub alias
ms.author:   zhaosu # Microsoft alias
manager:     dapodean
ms.service:  # Add the ms.service or ms.prod value
# ms.prod:   # To use ms.prod, uncomment it and delete ms.service
ms.topic:    Use Certificate Based Authentication in migration
ms.date:     10/16/2024
---

# Migrate with Certificate Based Authentication

Certificate Based Authentication (CBA) is supported in SPMT (SharePoint Migration Tool) builds newer than v4.1.125.11.

CBA with SPMT allows customers to use Azure App Registrations with certificate authentication as the identity model to migrate on-premise content to SharePoint and OneDrive for Business.

## Preparation Steps

__1. Register an application__

Follow [the instructions](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate) to register an application in the Microsoft Entra admin center.

__2. Grant permissions__

Under this registered application, choose different levels of API permissions as needed.

If you want to limit the registered application to specific SharePoint sites, add the following API permissions.

- 'Sites.Selected' under SharePoint API for REST and CSOM (SharePoint Client-Side Object Model) calls.

- 'Sites.Selected' under Microsoft Graph API for MS Graph sites-related API.

- 'Sites.Read.All' under Microsoft Graph APIfor searching sites and looking up the root site.

- 'User.Read.All' and Group.Read.All under Microsoft Graph APIfor resolving the user mapping.

- 'Organization.Read.All' under Microsoft Graph API for sending telemetry to the right Geo location.

Granting SharePoint 'AllSites.FullControl' permission under SharePoint and Microsoft Graph API to the application enables the application to move content into all sites of your tenant.

__3. Upload certificate__

Upload the public key of your X.509 certificate, issued by the Enterprise Public Key Infrastructure (PKI), to the registered application as an application credential. 

After uploading the certificate, copy the value in 'Thumbprint' for future use.

__4. Create configuration file__

Prepare a config file named "CertificateConfig.json" with following content. 


```
{
    "Thumbprint":"thumbprint for the cert",
    "TenantId":"Tenant ID",
    "ClientId":"App registration Id"
}
```

Copy "CertificateConfig.json" under %appdata%\Microsoft\MigrationToolStorage. If the folder does not exist, create it manually.

## Grant destination site access permission

If you set SharePoint Sites.Selected permission for the registered application, you need to grant access permissions of the destination sites to the application. 'FullControl' permission is required for SPMT to create destination document library.

Both MS Graph API and PowerShell PnP support granting application permission.

- Use Microsoft Graph API [Create permission - Microsoft Graph v1.0 | Microsoft Learn](https://learn.microsoft.com/en-us/graph/api/site-post-permissions?view=graph-rest-1.0&tabs=http) to grant 'owner' permission role on the sites.

- Use PowerShell PnP command “Grant-PnPAzureADAppSitePermission” to set 'FullControl' permission needed for the application.

[https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html](https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html)

## Using CBA with SPMT

If the "CertificateConfig.json" file contains the correct attributes, SPMT starts without prompting users to enter SharePoint admin credentials. However, if the file is incorrectly formatted, an error message appears “The application will exit because of sign-in failure. Please double-check and try again” after SPMT is launched. If wrong attribute values are provided in the "CertificateConfig.json" file, all migrations fail with errors in the migration report indicating insufficient permissions.

If the "CertificateConfig.json" file is not provided, SPMT asks users to enter SharePoint admin credentials.

---
