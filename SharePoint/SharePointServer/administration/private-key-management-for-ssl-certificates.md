---
title: "Private key management for SSL certificates"
ms.reviewer: 
ms.author: serdars
author: nimishasatapathy
manager: serdars
ms.date: 03/14/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how SSL certificate implements private key management."
---

# Private key management for SSL certificates

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

To better support least privileges scenarios and minimize the permissions given to certificate private keys, SharePoint Server Subscription Edition Version 23H1 applies more granular and sophisticated permission management for these private keys. The permissions will be based on the certificate assignments and will be dynamically updated when the certificate assignments change.

For example, if a certificate is assigned to perform client certificate authentication to an Simple Mail Transfer Protocol (SMTP) server, SharePoint will ensure the process that’s connecting to the SMTP server has the necessary permissions to use the private key of that certificate. If a certificate is no longer assigned to perform client certificate authentication to an SMTP server, SharePoint will remove permissions for that process so it no longer has access to the private key of that certificate.

The following APIs has been added
*Microsoft.SharePoint.Administration.CertificateManagement.SPServerCertificate* class to allow third-party integration with this functionality.