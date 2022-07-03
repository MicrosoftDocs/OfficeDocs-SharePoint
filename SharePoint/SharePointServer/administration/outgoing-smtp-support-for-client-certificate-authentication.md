---
title: "Outgoing SMTP support for client certificate authentication"
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
 
## Outgoing SMTP support for client certificate authentication

Some SMTP servers may require the use of client certificates for authentication before accepting email messages. SharePoint now supports client certificate authentication when sending emails to an SMTP server. The outbound SMTP settings in SharePoint must be configured to use TLS connection encryption and a certificate must be assigned to use this capability. The certificate must be in SharePoint's End Entity certificate store, the certificate's private key must be imported, and the certificate's enhanced key usage extension must specify the certificate is valid for client authentication if that extension is present.

A `-Certificate <SPServerCertificatePipeBind>` parameter has been added to the following cmdlet parameter set:

```powershell
Set-SPWebApplication [-Identity] <SPWebApplicationPipeBind> -SMTPServer <String> [-Certificate <SPServerCertificatePipeBind>] [-DisableSMTPEncryption] [-Force] [-NotProvisionGlobally] [-OutgoingEmailAddress <String>] [-ReplyToEmailAddress <String>] [-SMTPServerPort <Int32>] [-SMTPCredentials <PSCredential>]
```

To assign a certificate to the outbound SMTP settings through Central Administration, set Use TLS connection encryption and Use client certificate authentication to **Yes**, and then select the client certificate from the **Client certificate** drop-down list.