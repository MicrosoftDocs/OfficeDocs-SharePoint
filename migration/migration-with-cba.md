---
ms.date:     10/16/2024
title:       Use Certificate Based Authentication in migration
description: Describing how to use Certificate Based Authentication in migration.
author:      zacsun-ms
ms.author:   zhaosu
manager:     dapodean
ms.reviewer: zhaosu
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
ms.topic: article
search.appverid: MET150

---

# Migrate with Certificate Based Authentication

Certificate Based Authentication (CBA) is supported in SPMT (SharePoint Migration Tool) builds newer than v4.1.125.11.

CBA with SPMT allows customers to use Azure App Registrations with certificate authentication as the identity model to migrate on-premises content to SharePoint and OneDrive.

## Preparation Steps

### 1. Register an application

Follow [the instructions](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app?tabs=certificate) to register an application in the Microsoft Entra admin center.

### 2. Grant permissions

Under this registered application, choose different levels of API permissions as needed.

If you want to limit the registered application to specific SharePoint sites, add the following API permissions.

- 'Sites.Selected' under SharePoint API for accessing REST and CSOM (SharePoint Client-Side Object Model) calls.
- 'Sites.Selected' under Microsoft Graph API for sites-related oerations.
- 'Sites.Read.All' under Microsoft Graph API for searching sites and looking up the root site.
- 'User.Read.All' and Group.Read.All under Microsoft Graph API for resolving the user mapping.
- 'Organization.Read.All' under Microsoft Graph API for sending telemetry to the right Geo location.

Granting SharePoint the 'AllSites.FullControl' permission under the SharePoint and Microsoft Graph API to the application lets the application move content into all your tenant sites.

### 3. Upload certificate

- Upload the public key of your X.509 certificate, issued by the Enterprise Public Key Infrastructure (PKI), to the registered application as an application credential.
- After uploading the certificate, copy the value in 'Thumbprint' for future use.

### 4. Create configuration file

Prepare a config file named "CertificateConfig.json" with following content:

```
{
    "Thumbprint":"thumbprint for the cert",
    "TenantId":"Tenant ID",
    "ClientId":"App registration Id"
}
```

Copy "CertificateConfig.json" under %appdata%\Microsoft\MigrationToolStorage. If the folder doesn't exist, create it manually.

## Grant destination site access permission

If you set the SharePoint Sites.Selected permission for the registered application, you need to grant access permissions of the destination sites to the application. **FullControl** permission is required for SPMT to create a destination document library.

Both Microsoft Graph API and PowerShell PnP support granting the application permission.

- Use Microsoft Graph API to grant the **Owner** permission role on the sites. [Create permission - Microsoft Graph v1.0 | Microsoft Learn](https://learn.microsoft.com/graph/api/site-post-permissions?view=graph-rest-1.0&tabs=http)
- Use PowerShell PnP command “Grant-PnPAzureADAppSitePermission” to set the **FullControl** permission needed for the application.

[https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html](https://pnp.github.io/powershell/cmdlets/Grant-PnPAzureADAppSitePermission.html)

## Using CBA with SPMT

If the "CertificateConfig.json" file contains the correct attributes, SPMT starts without prompting users to enter SharePoint admin credentials. However, if the file is incorrectly formatted, an error message appears "The application will exit because of sign-in failure. Please double-check and try again." after SPMT is launched. If wrong attribute values are provided in the "CertificateConfig.json" file, all migrations fail with errors in the migration report indicating insufficient permissions.

If the "CertificateConfig.json" file isn't provided, SPMT asks users to enter SharePoint admin credentials.
