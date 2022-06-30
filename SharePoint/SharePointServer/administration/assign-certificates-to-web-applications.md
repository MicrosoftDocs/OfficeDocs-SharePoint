---
title: "Assign certificates to web applications"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how you can use Secure Sockets Layer (SSL) certificate management to monitor and manage the lifecycle of SSL certificates in your SharePoint farm."
---

 
## Assign certificates to web applications

SharePoint supports assigning SharePoint-managed certificates, which are imported by using the [Import-SPCertificate](/powershell/module/sharepoint-server/import-spcertificate) PowerShell cmdlet, to web applications with an SSL binding. The certificate must be in SharePoint's End Entity certificate store and the certificate's private key must also be imported. You can assign a certificate when the web application is first created or after it's created.

A `-Certificate <SPServerCertificatePipeBind>` parameter has been added to the following cmdlets and commands:

- [New-SPWebApplication](/powershell/module/sharepoint-server/new-spwebapplication)
- [New-SPWebApplicationExtension](/powershell/module/sharepoint-server/new-spwebapplicationextension)
- [Set-SPWebApplication](/powershell/module/sharepoint-server/set-spwebapplication)
- [New-SPCentralAdministration](/powershell/module/sharepoint-server/new-spcentraladministration)
- [Set-SPCentralAdministration](/powershell/module/sharepoint-server/set-spcentraladministration)
- [PSConfig.exe -cmd adminvs](/previous-versions/office/sharepoint-server-2010/cc263093(v=office.14))

The `SPServerCertificatePipeBind` accepts the following values:

- **String:** Friendly name of the certificate.
- **String:** Thumbprint of the certificate.
- **String:** Serial number of the certificate.
- **GUID:** ID property of the SPServerCertificate object.

To assign a certificate to a web application when creating that web application or extending a web application to an additional zone through Central Administration, set "Use Server Sockets Layer (SSL)" to Yes, and then select the server certificate from the Server Certificate drop-down list.