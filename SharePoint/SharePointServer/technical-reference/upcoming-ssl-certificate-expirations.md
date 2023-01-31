---
title: "Upcoming SSL certificate expirations"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
audience: ITPro
f1.keywords:
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid:
description: "Learn how to replace the upcoming SSL expiring certificates."
---

# Upcoming SSL certificate expirations

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 

 **Rule Name:** Upcoming SSL certificate expirations.
  
 **Summary:** SSL certificates currently in use in the farm will expire within the certificate expiration attention threshold (60 days by default). Once an SSL certificate expires, it's no longer valid to secure the resource. Users will receive error messages from their web browsers and client applications when accessing web sites that use expired SSL certificates.
  
 **Cause:** SSL certificates currently in use in the farm will expire.
  
 **Resolution: Renew or replace these certificates to ensure uninterrupted access to these resources. You can renew or replace these certificates from the Certificate Management page in Central Administration.**
