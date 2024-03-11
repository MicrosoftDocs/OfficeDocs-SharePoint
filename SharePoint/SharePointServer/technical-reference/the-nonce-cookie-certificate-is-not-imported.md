---
title: "Certificate Management is not managing the nonce cookie certificate (SharePoint Server)"
ms.author: serdars
author: serdars
manager: serdars
ms.date: 03/08/2024
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn to ensure proper management and notification of the certificate expiration to avoid issues with the Web Application Pool account while enabling OIDC in a web application."
---

# Certificate Management is not managing the nonce cookie certificate (SharePoint Server)

[!INCLUDE[[appliesto-xxx-xxx-xxx-SUB-xxx-md.md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

**Rule Name:** SharePoint Server doesn't manage the nonce cookie certificate.

**Summary:** OpenID Connect (OIDC) authentication is configured in your SharePoint Server farm, but the certificate used to generate the nonce cookie isn't managed by the Certificate Management of SharePoint Server. As a result, you don't receive any system notification if that certificate is close to expiration, which would lead to farm service outage. SharePoint Server doesn't automatically grant required permissions of nonce cookie certificate to the Web Application Pool account if you enable OIDC for web applications, and you need to do it manually.

**Cause:** SharePoint Server farm currently uses the certificate that is used to generate the nonce cookie but doesn't manage it.

**Resolution:** **Import the nonce cookie certificate**

Ensure proper management and notification of the certificate expiration by following the steps below to avoid issues with Web Application Pool account while enabling OIDC in web application:

1. Import nonce cookie certificate in Certificate Management of SharePoint Server.
1. Start SharePoint Management Shell and run the following script to update the certificate property.

   ```powershell
    # Use one of the commands to acquire nonce cookie certificate imported:
    $nonceCert = Get-SPCertificate -DisplayName <the certificate name>
    $nonceCert = Get-SPCertificate -Thumbprint <thumbprint>

    # Update
    $farm = Get-SPFarm 
    $farm.UpdateNonceCertificate($nonceCert, $true)
   ```

For more information, see [Change SharePoint farm properties](../security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-msaad.md#step-2-change-sharepoint-farm-properties).
